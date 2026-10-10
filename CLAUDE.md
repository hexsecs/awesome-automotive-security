# CLAUDE.md

A curated awesome list of automotive security resources. The product is
`README.md`; everything else exists to keep it accurate and trustworthy.

## Sources of truth

Read these rather than restating them here:

* `CONTRIBUTING.md`: inclusion criteria, entry format, ordering rules, and
  section-specific rules for Research Papers and Books.
* `data/hosts.toml`: which link hosts are reliable, which are excluded from
  link checking, and which to avoid. The validator rejects `avoid` hosts.
* `data/decisions.toml`: candidates rejected, entries removed, and archived
  entries deliberately kept, each with its reason. Never re-propose a rejected
  or removed URL; overturning one means deleting its record in the same change
  and saying why.
* `data/leads.toml`: candidates found but not yet openable or confirmed. Discovery
  re-tries them; settle one by adding or rejecting it and deleting its record.
* `prompts/*.md`: the runbooks for automated work. The Routines and the
  Actions workflows both read them, so change behaviour there, not in YAML.

## Before every push

```
python3 scripts/validate_list.py
```

It must pass. CI also runs lychee over `README.md`, so open every new URL
yourself before adding it: a URL you have not fetched is a CI round waiting to
fail.

When you change anything under `scripts/` or `tests/`, also run
`python3 -m unittest discover -s tests`; CI does.

Before researching, `python3 scripts/probe_egress.py` shows which hosts this
session can reach, and `python3 scripts/check_candidate.py URL...` vets a
candidate (duplicates, past decisions, host rules, and for GitHub archived,
dormant, moved and fork-parent state) before you spend effort on it.

`python3 scripts/list_health.py` reports thin sections and archived, moved or
dormant GitHub entries (`--no-github` for coverage only, when the API is
unreachable). Use it to choose where research effort goes.

## Automation map

| What | Where | When | Does |
| --- | --- | --- | --- |
| Validate | `validate.yml` | PRs touching the list or `data/` | structure, host and decision checks; lychee on the README |
| Link check | `link-check.yml` | Mondays | lychee over everything; opens an issue on failure |
| Health | `health.yml` | 15th of the month | `list_health.py`; opens an issue on unacknowledged findings |
| Discovery | Routine, `prompts/discover.md` | 1st of the month | researches additions, drafts a PR |
| Sweep | Routine, `prompts/sweep.md` | daily | triages `new-entry` issues, fixes `broken-link` issues, records rejections from review |

The Claude-driven work runs as Claude Code Routines because CI has no Claude
credential. `discover.yml`, `triage.yml` and the `fix-links` job are the same
runbooks wired to GitHub events; they skip until an `ANTHROPIC_API_KEY` or
`CLAUDE_CODE_OAUTH_TOKEN` secret exists. They use
`anthropics/claude-code-action@v1`, where tool permissions go in
`claude_args --allowedTools` (the old `allowed_tools` input is ignored), Bash
is limited to exact commands, and `.git/` is unreadable.

Automated PRs start their body with `<!-- automated: <runbook> -->`; the sweep
finds them by that marker to learn from how they were reviewed. PRs that the
platform opens from a Routine's pushed branch arrive with the marker
HTML-escaped, so the runbooks match the text `automated: <runbook>`, not the
delimiters. Nothing merges without a human.

## Lessons

Append here when you learn something non-obvious that is not yet a rule. Once
a lesson becomes a rule, move it into `CONTRIBUTING.md` or a data file and
delete it here, so this file stays short.

* Keep one commit per logical change with a body that explains *why*; the
  history is how later sessions learn what was tried.
* Routine sessions have neither `gh` nor GitHub tools. Their first sweep with a
  `broken-link` issue open (#27) did nothing, because the runbook said only
  "list open issues". Plain `curl` to `api.github.com` for this repository
  works from the sandbox without a token, so the runbooks now say so. Calls
  for other repositories may be refused; `list_health.py --no-github` then
  gives coverage alone.
* When several agents work in parallel, give each a disjoint set of files and
  shared schemas up front; their branches then merge without conflicts.
* A Routine's session starts with only the repositories and MCP servers in its
  own config. The discovery and sweep Routines were created with neither, so
  their sessions had no repository and no `add_repo`, could not push, and were
  still recorded as succeeded. Select this repository on each Routine in
  claude.ai; `create_trigger` cannot attach connectors in this organization.
* The Routine prompts live in the trigger config, not in this repository. Both
  end by requiring a first line of `RESULT: ...`, because the scheduler's
  status says nothing about what a run achieved; read that line, not the
  status.
* A cloud session's egress proxy may allow far less than CI does. In the
  2026-10 discovery run only `github.com` was reachable, and only through
  WebFetch: `curl` to GitHub got a proxy 403, and arxiv.org, usenix.org,
  ndss-symposium.org, ocslab.hksecurity.net, automotiveisac.com and
  i.blackhat.com were all refused. That is the sandbox, not the host, so do not
  record those hosts in `data/hosts.toml`. Park unreachable candidates
  in `data/leads.toml`, unproposed, rather than adding links you could not open.
* Probe egress before planning research (`scripts/probe_egress.py`). The
  proxy's policy is set per environment, and an edit to it reaches only new
  sessions, not the one that is running. In one session WebFetch failed DNS on every host (`ENOTFOUND`) while
  plain `curl` through the proxy reached them, so try both. Zenodo and
  tudatalib answered 403 to the sandbox yet passed CI's lychee, so a sandbox
  403 is not a dead link.
* A summary from WebFetch is a lead, not evidence. "No indication of archival"
  is not "not archived", and it rarely gives a last-commit date. Before listing
  a GitHub project, check the real repository state with
  `scripts/check_candidate.py`, which reads archived, last push and fork parent
  from the API, and check whether it is a fork: CANgaroo was listed as a
  4-star fork of a 187-star project for weeks.
* CI's link check proves a URL answers, not that it is the thing you meant. A
  search-result link whose page you could not open needs a second source for
  its identity (an AutoHack Zenodo record, a GEM-CAN article page that was not
  the data). Say in the PR which links you did not open.
* Parallel sessions land overlapping entries. Between opening a PR and merging
  it, #37 added the same AutoHack entry and #39 added an Uptane entry that made
  mine redundant. Fetch `main` and grep for each URL and name before pushing
  and again before merging.
* Match the repository's merge style. A PR of several deliberate commits gets a
  merge commit, not a squash, or the history stops teaching later sessions
  anything. Check `git log` on `main` for what was used before merging.
* After a squash-merged PR, reset the working branch to `main` before new work.
  If the assigned branch name must be reused, the remote copy has diverged;
  `--force-with-lease` is fine only when it holds nothing but merged history.
* A review bot's claim about a URL is a claim to verify, not an order. When you
  cannot verify it, reply with what you could confirm and leave the decision to
  the maintainer instead of swapping in a link you have not opened.
