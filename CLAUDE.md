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
* `prompts/*.md`: the runbooks for automated work. The Routines and the
  Actions workflows both read them, so change behaviour there, not in YAML.

## Before every push

```
python3 scripts/validate_list.py
```

It must pass. CI also runs lychee over `README.md`, so open every new URL
yourself before adding it: a URL you have not fetched is a CI round waiting to
fail.

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
finds them by that marker to learn from how they were reviewed. Nothing merges
without a human.

## Lessons

Append here when you learn something non-obvious that is not yet a rule. Once
a lesson becomes a rule, move it into `CONTRIBUTING.md` or a data file and
delete it here, so this file stays short.

* Keep one commit per logical change with a body that explains *why*; the
  history is how later sessions learn what was tried.
* This sandbox's proxy may refuse `api.github.com` repository calls; use the
  GitHub tools instead, or `list_health.py --no-github`.
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
