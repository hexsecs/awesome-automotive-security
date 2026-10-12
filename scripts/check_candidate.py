#!/usr/bin/env python3
"""Vet candidate URLs before proposing them.

For each URL, answers the questions that discovery got wrong by hand:

* Is it already listed, already a lead, or already turned away? (README.md,
  data/leads.toml, data/decisions.toml)
* Do the host rules in data/hosts.toml allow it?
* For a GitHub repository: is it archived, dormant, renamed, or a fork of a
  project with far more stars? These come from the GitHub API, not from a page
  summary, which rarely says.
* For anything else: does it open, where does it end up after redirects, and
  what is its title? A refusal here is the host's bot filter or the sandbox's
  proxy, which scripts/probe_egress.py tells apart; it is not proof the link is
  dead.

BLOCKERS stop a proposal (a rejected or removed decision, an avoid host, a
duplicate). WARNINGS need a human judgement (archived, dormant, a fork, a
redirect, an unopened link). Neither replaces reading the project: this checks
facts, it does not judge whether the thing belongs on the list.

Exits 1 if any URL has a blocker, otherwise 0. Set GITHUB_TOKEN for the API's
higher rate limit.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from list_health import fetch_repo, github_repo, normalise, parse_readme, rate_limit_note
from probe_egress import classify
from validate_list import EXCLUDING_KINDS, host_matches, load_decisions, load_hosts, load_leads

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
USER_AGENT = "awesome-automotive-security-check-candidate"
# Third-party mirror of GitHub repository metadata. Used only when the GitHub API
# itself is refused, as it is for repositories outside a cloud session's scope.
ECOSYSTEMS = "https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/{name}"

DORMANT_YEARS = 2.0
# A fork is worth a warning when its parent is this many times more starred.
FORK_PARENT_RATIO = 3
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def local_findings(
    url: str,
    entries: list[dict[str, Any]],
    decisions: list[dict],
    leads: list[dict],
    hosts: dict[str, list[dict]],
) -> tuple[list[str], list[str]]:
    """Checks that need no network. Returns (blockers, warnings). Pure."""
    blockers: list[str] = []
    warnings: list[str] = []
    key = normalise(url)
    repo = github_repo(url)

    def same_project(other: str) -> bool:
        if normalise(other) == key:
            return True
        theirs = github_repo(other)
        return bool(repo and theirs and repo[0].lower() == theirs[0].lower()
                    and repo[1].lower() == theirs[1].lower())

    for e in entries:
        if same_project(e["url"]):
            blockers.append(f"already listed as '{e['name']}' in {e['section']} (line {e['line']})")
    if repo:
        for e in entries:
            if e["name"].casefold() == repo[1].casefold() and not same_project(e["url"]):
                warnings.append(f"an entry named '{e['name']}' already exists ({e['url']}); "
                                "is this the same project under another URL?")

    for d in decisions:
        if d.get("url") and same_project(d["url"]):
            ref = f" in {d['ref']}" if d.get("ref") else ""
            if d.get("decision") in EXCLUDING_KINDS:
                blockers.append(f"{d['decision']}{ref} on {d.get('date')}: {d.get('reason')} "
                                "To overturn it, delete its record in the same change and say why.")
            elif d.get("decision") == "kept":
                warnings.append(f"recorded as kept{ref}: {d.get('reason')}")

    for lead in leads:
        if same_project(lead["url"]):
            warnings.append(f"already a lead ({lead.get('date')}): {lead.get('reason')}")

    host = (urlparse(url).hostname or "").lower()
    for record in hosts.get("avoid", []):
        allowed = {normalise(u) for u in record.get("allow", [])}
        if host_matches(host, record["host"]) and key not in allowed:
            blockers.append(f"host {host} is under avoid in data/hosts.toml: {record.get('reason')}")
    for record in hosts.get("excluded", []):
        if host_matches(host, record["host"]):
            warnings.append(f"host {host} is excluded from link checking, so CI will not verify "
                            f"this link; open it by hand. {record.get('reason')}")
    return blockers, warnings


def repo_findings(data: dict[str, Any], listed: tuple[str, str], parent: dict[str, Any] | None,
                  now: datetime) -> tuple[list[str], list[str]]:
    """Judge a GitHub API repository record. Returns (facts, warnings). Pure."""
    facts: list[str] = []
    warnings: list[str] = []
    full = str(data.get("full_name", ""))
    stars = data.get("stargazers_count")
    facts.append(f"{full or '/'.join(listed)}: {stars} stars, {data.get('forks_count')} forks, "
                 f"license {(data.get('license') or {}).get('spdx_id') or 'none'}")
    if data.get("description"):
        facts.append(f"description: {data['description']}")

    if full and full.lower() != "/".join(listed).lower():
        warnings.append(f"moved: the URL redirects to {full}; link that instead")
    if data.get("archived"):
        warnings.append("archived: only proposable if still canonical or historically "
                        "important (CONTRIBUTING.md criterion 5); say so in the description")
    pushed = data.get("pushed_at")
    if pushed:
        try:
            when = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        except ValueError:
            when = None
        if when:
            age = (now - when).days
            facts.append(f"last push {when.date()} ({age} days ago)")
            if age > DORMANT_YEARS * 365.25:
                warnings.append(f"dormant: no push for {age // 365} years")
    if data.get("fork"):
        source = parent or {}
        pname = source.get("full_name") or (data.get("parent") or {}).get("full_name") or "its parent"
        pstars = source.get("stargazers_count")
        note = f"fork of {pname}" + (f" ({pstars} stars)" if pstars is not None else "")
        if pstars is not None and stars is not None and pstars >= max(10, FORK_PARENT_RATIO * stars):
            warnings.append(f"{note}, against {stars} here: the parent is probably the "
                            "canonical project (CANgaroo was listed as a 4-star fork of a 187-star one)")
        else:
            warnings.append(note + "; check which one is canonical")
    return facts, warnings


def from_ecosystems(raw: dict[str, Any]) -> dict[str, Any]:
    """Reshape an ecosyste.ms repository record like a GitHub API one. Pure."""
    license_id = raw.get("license")
    if isinstance(license_id, dict):
        license_id = license_id.get("spdx_id") or license_id.get("key")
    source = raw.get("source_name")
    return {
        "full_name": raw.get("full_name"),
        "stargazers_count": raw.get("stargazers_count"),
        "forks_count": raw.get("forks_count"),
        "license": {"spdx_id": str(license_id).upper()} if license_id else None,
        "description": raw.get("description"),
        "archived": bool(raw.get("archived")),
        "pushed_at": raw.get("pushed_at"),
        "fork": bool(raw.get("fork")),
        "parent": {"full_name": source} if source else None,
    }


def fetch_ecosystems(full_name: str, timeout: float) -> dict[str, Any] | None:
    """One repository from ecosyste.ms, or None if it is not indexed or unreachable."""
    from urllib.parse import quote

    req = urllib.request.Request(ECOSYSTEMS.format(name=quote(full_name, safe="")),
                                 headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return from_ecosystems(json.loads(resp.read().decode("utf-8")))
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return None


def check_github(url: str, repo: tuple[str, str], token: str | None, timeout: float,
                 now: datetime) -> tuple[list[str], list[str]]:
    result = fetch_repo(repo[0], repo[1], token, timeout)
    status, data = result["status"], result["data"]
    if status == 404:
        return [], ["GitHub reports no such repository (404): deleted, private, or mistyped"]
    if status == 429 or (status == 403 and result["remaining"] == 0):
        return [], [f"GitHub API {rate_limit_note(result['reset'])}; set GITHUB_TOKEN or retry later"]

    via = ""
    if data is None:
        # The API is refused here (a cloud session is bound to its own repositories).
        # ecosyste.ms mirrors the same facts; it is third-party and can lag.
        data = fetch_ecosystems("/".join(repo), timeout)
        if data is None:
            kind, detail = classify(status, result["error"])
            why = ("the egress proxy refused api.github.com for this repository"
                   if kind == "blocked" or status == 403 else detail)
            return [], [f"could not read repository state ({why}), and ecosyste.ms does not "
                        "index it; check archived status, last commit and fork parent by hand "
                        "before proposing it"]
        via = "ecosyste.ms (third party; can lag the real repository)"

    parent = None
    if data.get("fork") and (data.get("parent") or {}).get("full_name"):
        pname = data["parent"]["full_name"]
        if via:
            parent = fetch_ecosystems(pname, timeout)
        else:
            owner, name = pname.split("/", 1)
            parent = fetch_repo(owner, name, token, timeout)["data"]
    facts, warnings = repo_findings(data, repo, parent, now)
    if via:
        facts.insert(0, f"source: {via}")
    return facts, warnings


def check_page(url: str, timeout: float) -> tuple[list[str], list[str]]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    status: int | None = None
    error: str | None = None
    final = url
    body = ""
    ctype = ""
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status, final = resp.status, resp.geturl()
            ctype = resp.headers.get("Content-Type", "")
            if "html" in ctype.lower():
                body = resp.read(65536).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as err:
        status = err.code
    except urllib.error.URLError as err:
        error = str(err.reason)
    except (TimeoutError, OSError) as err:
        error = str(err)

    verdict, detail = classify(status, error)
    facts: list[str] = []
    warnings: list[str] = []
    if verdict == "reachable" and status is not None and status < 400:
        facts.append(f"opens (HTTP {status}); {ctype.split(';')[0] or 'unknown type'}")
        title = TITLE_RE.search(body)
        if title:
            facts.append("title: " + re.sub(r"\s+", " ", title.group(1)).strip()[:160])
    elif verdict == "reachable":
        warnings.append(f"the host answered {detail}; the page is probably gone")
    elif verdict == "refused":
        warnings.append(f"unopened: the host refused an automated client ({detail}). Not proof the "
                        "link is dead; confirm what it is from a second source, say it was not "
                        "opened, or park it in data/leads.toml")
    else:
        warnings.append(f"unopened: {verdict} ({detail}). If scripts/probe_egress.py says the proxy "
                        "blocks this host, park it in data/leads.toml rather than proposing it")
    if status is not None and status < 400 and normalise(final) != normalise(url):
        warnings.append(f"redirects to {final}; link the final URL unless the redirect is a "
                        "stable canonical alias")
    return facts, warnings


def check(url: str, context: dict[str, Any], timeout: float, token: str | None,
          now: datetime, offline: bool) -> dict[str, Any]:
    blockers, warnings = local_findings(url, context["entries"], context["decisions"],
                                        context["leads"], context["hosts"])
    facts: list[str] = []
    if urlparse(url).scheme != "https":
        blockers.append("must be an https URL")
    elif not offline:
        repo = github_repo(url)
        f, w = (check_github(url, repo, token, timeout, now) if repo else check_page(url, timeout))
        facts += f
        warnings += w
    return {"url": url, "blockers": blockers, "warnings": warnings, "facts": facts}


def render(results: list[dict[str, Any]]) -> str:
    out: list[str] = []
    for r in results:
        verdict = "BLOCKED" if r["blockers"] else ("CHECK" if r["warnings"] else "CLEAR")
        out.append(f"## {r['url']}  [{verdict}]")
        for label, key in (("facts", "facts"), ("BLOCKER", "blockers"), ("warning", "warnings")):
            for line in r[key]:
                out.append(f"- {label}: {line}" if key != "facts" else f"- {line}")
        out.append("")
    return "\n".join(out).rstrip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("urls", nargs="+", help="candidate URLs")
    parser.add_argument("--offline", action="store_true",
                        help="only check against README.md and data/, no network")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    problems: list[str] = []
    hosts = load_hosts(problems)
    decisions = load_decisions(problems)
    leads = load_leads(problems)
    if problems:
        print("data files have problems; run scripts/validate_list.py:\n  "
              + "\n  ".join(problems), file=sys.stderr)
        return 2
    _, entries = parse_readme(README.read_text(encoding="utf-8"))
    context = {"entries": entries, "decisions": decisions, "leads": leads, "hosts": hosts}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    now = datetime.now(timezone.utc)

    results = [check(u, context, args.timeout, token, now, args.offline) for u in args.urls]
    print(json.dumps(results, indent=2) if args.json else render(results))
    return 1 if any(r["blockers"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
