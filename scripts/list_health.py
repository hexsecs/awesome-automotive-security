#!/usr/bin/env python3
"""Deterministic health report for README.md.

Answers two questions without any AI in the loop:

* Coverage: how many entries each section holds, and which are thin enough to
  be worth a targeted research pass.
* GitHub status: which listed repositories are archived, have moved (the
  listed URL now redirects), have gone missing, or have not been pushed to in
  years. CONTRIBUTING.md criterion 5 asks that entries be "alive, or
  historically important"; this makes the first half checkable.

Archived or dormant does not mean wrong: URH is archived and still canonical.
The report surfaces candidates for a human to judge, it does not judge them.

Prints Markdown by default, or JSON with --json. Always exits 0 unless
--fail-on-findings is given and something is archived, moved or missing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

README = Path(__file__).resolve().parent.parent / "README.md"

ENTRY_RE = re.compile(r"^\* \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\) - (?P<desc>.+)$")
TOC_HEADING = "## Contents"

API = "https://api.github.com/repos/{owner}/{repo}"
USER_AGENT = "awesome-automotive-security-list-health"
UNAUTHENTICATED_LIMIT = 60

# First path segments on github.com that are site pages, not repository owners.
NON_REPO_PREFIXES = {
    "about", "apps", "codespaces", "collections", "contact", "customer-stories",
    "enterprise", "events", "explore", "features", "issues", "login",
    "marketplace", "new", "notifications", "orgs", "organizations", "pricing",
    "pulls", "readme", "search", "security", "settings", "site", "sponsors",
    "topics", "trending", "users",
}
NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+$")

# Categories that --fail-on-findings treats as actionable.
ACTIONABLE = ("archived", "moved", "missing")


def parse_readme(text: str) -> tuple[list[str], list[dict[str, Any]]]:
    """Return section headings in order, and entries tagged with their section."""
    sections: list[str] = []
    entries: list[dict[str, Any]] = []
    current: str | None = None
    for lineno, line in enumerate(text.split("\n"), start=1):
        if line.startswith("## "):
            current = None if line.strip() == TOC_HEADING else line[3:].strip()
            if current is not None:
                sections.append(current)
            continue
        if current is None:
            continue
        m = ENTRY_RE.match(line)
        if m:
            entries.append(
                {"line": lineno, "section": current, "name": m.group("name"), "url": m.group("url")}
            )
    return sections, entries


def github_repo(url: str) -> tuple[str, str] | None:
    """Map a github.com URL to (owner, repo), or None if it is not a repository.

    Deeper paths such as /tree/main/docs still map to their repository; a
    trailing slash or a .git suffix is ignored.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return None
    if parsed.netloc.lower() not in ("github.com", "www.github.com"):
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2 or parts[0].lower() in NON_REPO_PREFIXES:
        return None
    owner, repo = parts[0], parts[1]
    if repo.lower().endswith(".git"):
        repo = repo[: -len(".git")]
    if not (NAME_RE.match(owner) and NAME_RE.match(repo)) or repo in (".", ".."):
        return None
    return owner, repo


def coverage(sections: list[str], entries: list[dict[str, Any]], thin: int) -> list[dict[str, Any]]:
    """Entry count per section, ascending, flagging sections below `thin`."""
    counts = {s: 0 for s in sections}
    for e in entries:
        counts[e["section"]] += 1
    # Stable sort keeps README order among sections with equal counts.
    ordered = sorted(sections, key=lambda s: counts[s])
    return [{"section": s, "entries": counts[s], "thin": counts[s] < thin} for s in ordered]


def fetch_repo(owner: str, repo: str, token: str | None, timeout: float) -> dict[str, Any]:
    """Query the GitHub API for one repository. Never raises.

    Returns {"status": int | None, "data": dict | None, "error": str | None,
    "remaining": int | None, "reset": int | None, "retry_after": int | None}.
    """
    req = urllib.request.Request(
        API.format(owner=owner, repo=repo),
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USER_AGENT,
        },
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    def limits(headers: Any) -> dict[str, int | None]:
        def num(name: str) -> int | None:
            value = headers.get(name) if headers is not None else None
            return int(value) if value and value.isdigit() else None

        return {"remaining": num("X-RateLimit-Remaining"), "reset": num("X-RateLimit-Reset"),
                "retry_after": num("Retry-After")}

    try:
        # urllib follows the API's 301 for renamed repositories, so a move shows
        # up as a full_name that differs from the one requested.
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"status": resp.status, "data": data, "error": None, **limits(resp.headers)}
    except urllib.error.HTTPError as err:
        return {"status": err.code, "data": None, "error": f"HTTP {err.code} {err.reason}",
                **limits(err.headers)}
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as err:
        reason = getattr(err, "reason", err)
        return {"status": None, "data": None, "error": f"{type(err).__name__}: {reason}",
                "remaining": None, "reset": None, "retry_after": None}


def rate_limit_note(reset: int | None) -> str:
    when = datetime.fromtimestamp(reset, timezone.utc).strftime("%Y-%m-%d %H:%M UTC") if reset else "unknown"
    return f"rate limit exhausted (resets {when})"


def check_github(
    entries: list[dict[str, Any]],
    token: str | None,
    dormant_years: float,
    max_repos: int | None,
    timeout: float,
    now: datetime,
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    """Query each distinct listed repository once, sequentially, and classify it."""
    repos: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for e in entries:
        key = github_repo(e["url"])
        if key:
            repos.setdefault((key[0].lower(), key[1].lower()), []).append({**e, "owner": key[0], "repo": key[1]})

    findings: dict[str, list[dict[str, Any]]] = {
        "archived": [], "moved": [], "missing": [], "dormant": [], "errors": [], "unchecked": [],
    }
    meta: dict[str, Any] = {"repos": len(repos), "checked": 0, "authenticated": bool(token),
                            "warnings": []}
    if not token and len(repos) > UNAUTHENTICATED_LIMIT:
        meta["warnings"].append(
            f"No GITHUB_TOKEN or GH_TOKEN set: {len(repos)} repositories exceed the "
            f"unauthenticated limit of {UNAUTHENTICATED_LIMIT} requests per hour, so some "
            "will likely be reported as unchecked."
        )

    cutoff = now - timedelta(days=365.25 * dormant_years)
    stop_reason: str | None = None

    for index, group in enumerate(repos.values()):
        first = group[0]
        listed = f"{first['owner']}/{first['repo']}"
        row = {"entries": [e["name"] for e in group], "sections": sorted({e["section"] for e in group}),
               "lines": [e["line"] for e in group], "url": first["url"], "repo": listed}

        if stop_reason is None and max_repos is not None and index >= max_repos:
            stop_reason = f"--max-repos {max_repos} reached"
        if stop_reason:
            findings["unchecked"].append({**row, "reason": stop_reason})
            continue

        result = fetch_repo(first["owner"], first["repo"], token, timeout)
        status, data = result["status"], result["data"]
        # Primary limit: 403 with no requests remaining. Secondary limit: 429,
        # or 403 with Retry-After. Either way, stop rather than retry.
        rate_limited = status == 429 or (
            status == 403 and (result["remaining"] == 0 or result["retry_after"] is not None)
        )

        if rate_limited:
            stop_reason = rate_limit_note(result["reset"])
            findings["unchecked"].append({**row, "reason": stop_reason})
            continue

        meta["checked"] += 1
        if status == 404:
            findings["missing"].append(row)
        elif data is None or status is None or status >= 300:
            findings["errors"].append({**row, "error": result["error"] or f"HTTP {status}"})
        else:
            full_name = str(data.get("full_name", ""))
            if full_name and full_name.lower() != listed.lower():
                findings["moved"].append({**row, "new_repo": full_name,
                                          "new_url": data.get("html_url") or f"https://github.com/{full_name}"})
            pushed = data.get("pushed_at")
            if data.get("archived"):
                findings["archived"].append({**row, "pushed_at": pushed})
            elif pushed:
                try:
                    pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
                except ValueError:
                    pushed_dt = None
                if pushed_dt and pushed_dt < cutoff:
                    findings["dormant"].append({**row, "pushed_at": pushed})

        # Honour the rate limit: once it is spent, stop rather than hammer the API.
        if result["remaining"] == 0 and stop_reason is None:
            stop_reason = rate_limit_note(result["reset"])

    if stop_reason:
        meta["warnings"].append(f"Stopped querying early: {stop_reason}.")
    for rows in findings.values():
        rows.sort(key=lambda r: r["entries"][0].casefold())
    return findings, meta


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def render_markdown(report: dict[str, Any]) -> str:
    """Render the report as GitHub-flavoured Markdown."""
    cov, findings, meta = report["coverage"], report["findings"], report["github"]
    thin = [c for c in cov if c["thin"]]
    out: list[str] = ["# List health report", ""]

    summary = (f"{report['entries']} entries in {len(cov)} sections; "
               f"{len(thin)} section(s) under {report['thin_threshold']} entries.")
    if meta is not None:
        summary += (f" GitHub: {meta['checked']} of {meta['repos']} repositories checked — "
                    + ", ".join(f"{len(findings[k])} {k}" for k in
                                ("archived", "moved", "missing", "dormant", "errors", "unchecked"))
                    + ".")
    out += [f"**Summary:** {summary}", "", f"Generated {report['generated']}.", ""]

    for warning in (meta or {}).get("warnings", []):
        out += [f"> **Warning:** {warning}", ""]

    out += ["## Coverage", "", "| Section | Entries | |", "| --- | ---: | --- |"]
    for c in cov:
        flag = f"thin (< {report['thin_threshold']})" if c["thin"] else ""
        out.append(f"| {md_escape(c['section'])} | {c['entries']} | {flag} |")
    out.append("")

    if meta is None:
        return "\n".join(out)

    out += [
        "Archived or dormant does not mean wrong: CONTRIBUTING.md criterion 5 keeps "
        "archived projects that are still canonical (URH is archived and canonical) or "
        "historically important. Moved and missing entries usually need a URL fix.",
        "",
    ]

    def entry_cell(row: dict[str, Any]) -> str:
        return md_escape(", ".join(row["entries"])) + f" (L{', L'.join(map(str, row['lines']))})"

    def section_cell(row: dict[str, Any]) -> str:
        return md_escape(", ".join(row["sections"]))

    tables = {
        "archived": ("Archived", ["Entry", "Section", "Listed URL", "Last push"],
                     lambda r: [entry_cell(r), section_cell(r), r["url"], (r["pushed_at"] or "")[:10]]),
        "moved": ("Moved (listed URL redirects)", ["Entry", "Section", "Listed URL", "New URL"],
                  lambda r: [entry_cell(r), section_cell(r), r["url"], r["new_url"]]),
        "missing": ("Missing (404)", ["Entry", "Section", "Listed URL"],
                    lambda r: [entry_cell(r), section_cell(r), r["url"]]),
        "dormant": (f"Dormant (no push in {report['dormant_years']:g}+ years)",
                    ["Entry", "Section", "Listed URL", "Last push"],
                    lambda r: [entry_cell(r), section_cell(r), r["url"], (r["pushed_at"] or "")[:10]]),
        "errors": ("Request errors", ["Entry", "Listed URL", "Error"],
                   lambda r: [entry_cell(r), r["url"], md_escape(r["error"])]),
        "unchecked": ("Unchecked", ["Entry", "Listed URL", "Reason"],
                      lambda r: [entry_cell(r), r["url"], md_escape(r["reason"])]),
    }
    for key, (title, headers, cells) in tables.items():
        rows = findings[key]
        out += [f"## {title}", ""]
        if not rows:
            out += ["None.", ""]
            continue
        out.append("| " + " | ".join(headers) + " |")
        out.append("|" + " --- |" * len(headers))
        for row in rows:
            out.append("| " + " | ".join(cells(row)) + " |")
        out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--readme", type=Path, default=README, help="list to check (default: README.md)")
    parser.add_argument("--thin", type=int, default=5, metavar="N",
                        help="flag sections with fewer than N entries (default: 5)")
    parser.add_argument("--dormant-years", type=float, default=3, metavar="Y",
                        help="flag repositories not pushed to in Y years (default: 3)")
    parser.add_argument("--max-repos", type=int, default=None, metavar="N",
                        help="query at most N repositories; report the rest as unchecked")
    parser.add_argument("--no-github", action="store_true",
                        help="coverage only; make no network requests")
    parser.add_argument("--timeout", type=float, default=20, help="per-request timeout in seconds")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    parser.add_argument("--fail-on-findings", action="store_true",
                        help="exit 1 if any repository is archived, moved or missing")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    sections, entries = parse_readme(args.readme.read_text(encoding="utf-8"))
    report: dict[str, Any] = {
        "generated": now.strftime("%Y-%m-%d %H:%M UTC"),
        "entries": len(entries),
        "thin_threshold": args.thin,
        "dormant_years": args.dormant_years,
        "coverage": coverage(sections, entries, args.thin),
        "findings": None,
        "github": None,
    }

    if not args.no_github:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or None
        findings, meta = check_github(entries, token, args.dormant_years, args.max_repos,
                                      args.timeout, now)
        report["findings"], report["github"] = findings, meta
        for warning in meta["warnings"]:
            print(f"warning: {warning}", file=sys.stderr)

    # Print only once everything is gathered, so a crash leaves no partial report.
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(render_markdown(report))

    if args.fail_on_findings and report["findings"]:
        if any(report["findings"][k] for k in ACTIONABLE):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
