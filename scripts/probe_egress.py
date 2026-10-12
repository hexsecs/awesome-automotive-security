#!/usr/bin/env python3
"""Which hosts can this session reach? Run it before planning discovery.

A cloud session's egress proxy may allow far less than CI does, and the failure
looks the same from the outside: a link that "does not open". They are not the
same, and discovery should treat them differently:

* reachable   the host answered with a page. Fetch candidates on it as normal.
* refused     the host answered but refused an automated client (403, 429, 503
              or a 202 challenge). The network path works; this is the host's own
              bot filter, so a link on it may still be fine in CI. Do not record
              the host in data/hosts.toml on this evidence alone.
* blocked     the egress proxy refused the connection. That is the sandbox, not
              the host. Candidates there cannot be opened this session; park
              them in data/leads.toml instead of proposing them.
* dns         the name did not resolve.
* error       anything else, such as a timeout.

Probes use the standard library over HTTPS_PROXY, so this tests the same path
curl takes. A tool with its own network stack (WebFetch, a browser) can still
behave differently from what is reported here; if the two disagree, trust the
tool you will actually use and say so in the PR.

Prints Markdown by default, or JSON with --json. Exits 0 unless --require names
a host that is not reachable.
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    sys.exit("probe_egress.py needs Python 3.11 or newer, for tomllib.")

ROOT = Path(__file__).resolve().parent.parent
HOSTS = ROOT / "data" / "hosts.toml"
USER_AGENT = "awesome-automotive-security-egress-probe"

# Hosts discovery commonly needs, beyond those already in data/hosts.toml.
DISCOVERY_HOSTS = (
    "github.com",
    "api.github.com",
    "raw.githubusercontent.com",
    "arxiv.org",
    "www.usenix.org",
    "www.ndss-symposium.org",
    "zenodo.org",
    "doi.org",
    "openalex.org",
    "owasp.org",
    "automotiveisac.com",
    "i.blackhat.com",
    "media.defcon.org",
    "ocslab.hksecurity.net",
    "books.google.com",
)

# Statuses that mean "the host answered but is filtering automated clients".
REFUSAL_STATUSES = {202, 401, 403, 405, 406, 429, 451, 503}


def classify(status: int | None, error: str | None) -> tuple[str, str]:
    """Map one probe outcome to (verdict, detail). Pure, so it is testable."""
    if status is not None:
        if status in REFUSAL_STATUSES:
            return "refused", f"HTTP {status}"
        if status < 400:
            return "reachable", f"HTTP {status}"
        return "reachable", f"HTTP {status} (host answered)"
    text = (error or "").lower()
    # http.client reports a refused CONNECT as "Tunnel connection failed: 403 ...".
    if "tunnel connection failed" in text or "proxy" in text and "forbidden" in text:
        return "blocked", error or "proxy refused the connection"
    if "name or service not known" in text or "nodename nor servname" in text \
            or "enotfound" in text or "temporary failure in name resolution" in text \
            or "no address associated" in text:
        return "dns", error or "name did not resolve"
    return "error", error or "unknown error"


def probe(host: str, timeout: float) -> dict[str, str | int | None]:
    """GET https://host/ once. Never raises."""
    req = urllib.request.Request(f"https://{host}/", headers={"User-Agent": USER_AGENT})
    status: int | None = None
    error: str | None = None
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
    except urllib.error.HTTPError as err:
        status = err.code
    except urllib.error.URLError as err:
        error = str(err.reason)
    except (socket.timeout, TimeoutError):
        error = "timed out"
    except OSError as err:
        error = str(err)
    verdict, detail = classify(status, error)
    return {"host": host, "verdict": verdict, "detail": detail, "status": status}


def listed_hosts() -> list[str]:
    """Exact hosts from data/hosts.toml; prefix patterns cannot be probed."""
    try:
        with HOSTS.open("rb") as f:
            data = tomllib.load(f)
    except (OSError, tomllib.TOMLDecodeError):
        return []
    hosts = [r["host"] for group in data.values() for r in group
             if isinstance(r.get("host"), str) and not r["host"].endswith(".*")]
    return hosts


def hosts_to_probe(extra: list[str], only_listed: bool) -> list[str]:
    ordered = ([] if only_listed else list(DISCOVERY_HOSTS)) + listed_hosts() + extra
    seen: set[str] = set()
    return [h for h in ordered if not (h in seen or seen.add(h))]


def render(results: list[dict]) -> str:
    out = ["# Egress probe", "", "| Host | Result | Detail |", "| --- | --- | --- |"]
    for r in results:
        out.append(f"| {r['host']} | {r['verdict']} | {str(r['detail']).replace('|', '/')} |")
    by = {v: [r["host"] for r in results if r["verdict"] == v]
          for v in ("reachable", "refused", "blocked", "dns", "error")}
    out += ["", f"**{len(by['reachable'])} reachable, {len(by['refused'])} refused by the host, "
            f"{len(by['blocked'])} blocked by the proxy, {len(by['dns'])} dns, "
            f"{len(by['error'])} other.**"]
    if by["blocked"]:
        out += ["", "Blocked by the egress proxy (the sandbox, not the host). Park candidates "
                "there in data/leads.toml: " + ", ".join(by["blocked"]) + "."]
    if by["refused"]:
        out += ["", "Refused automated clients from here; may still pass in CI: "
                + ", ".join(by["refused"]) + "."]
    if by["dns"]:
        out += ["", "Did not resolve here. If curl reaches them, the fault is in the fetch tool, "
                "not the network: " + ", ".join(by["dns"]) + "."]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("hosts", nargs="*", help="extra hosts to probe")
    parser.add_argument("--only-listed", action="store_true",
                        help="probe only hosts in data/hosts.toml plus those given")
    parser.add_argument("--require", default="", metavar="HOST,HOST",
                        help="exit 1 unless each of these is reachable")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    hosts = hosts_to_probe(args.hosts, args.only_listed)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda h: probe(h, args.timeout), hosts))

    print(json.dumps(results, indent=2) if args.json else render(results))

    required = [h for h in args.require.split(",") if h]
    unreachable = [h for h in required
                   if next((r["verdict"] for r in results if r["host"] == h), "error") != "reachable"]
    if unreachable:
        print(f"\nRequired but not reachable: {', '.join(unreachable)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
