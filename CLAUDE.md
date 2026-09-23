# CLAUDE.md

A curated awesome list of automotive security resources. The product is
`README.md`; everything else exists to keep it accurate and trustworthy.

## Sources of truth

Read these rather than restating them here:

* `CONTRIBUTING.md`: inclusion criteria, entry format, ordering rules, and
  section-specific rules for Research Papers and Books.
* `data/hosts.toml`: which link hosts are reliable, which are excluded from
  link checking, and which to avoid. The validator rejects `avoid` hosts.
* `data/decisions.toml`: candidates that were rejected or entries that were
  removed, with reasons. Never re-propose anything recorded there; overturning
  a decision means deleting its record in the same change and saying why.

## Before every push

```
python3 scripts/validate_list.py
```

It must pass. CI also runs lychee over `README.md`, so open every new URL
yourself before adding it: a URL you have not fetched is a CI round waiting to
fail.

`python3 scripts/list_health.py` reports thin sections and archived, moved or
dormant GitHub entries. Use it to choose where research effort goes.

## Automation map

| Workflow | When | Does |
| --- | --- | --- |
| `validate.yml` | every PR touching the list | structure checks and lychee on the README |
| `link-check.yml` | Mondays | lychee over everything; on failure opens an issue and a draft fix PR |
| `discover.yml` | 1st of the month | researches additions, opens a draft PR |
| `triage.yml` | `new-entry` issue opened | checks the suggestion against the criteria, comments, drafts a PR if it qualifies |
| `health.yml` | monthly | runs `list_health.py`, opens an issue on findings |

The Claude-driven workflows use `anthropics/claude-code-action@v1`: tool
permissions go in `claude_args --allowedTools` (the old `allowed_tools` input
is ignored), and `id-token: write` is required so PRs are opened with the App
token and therefore trigger CI. Nothing merges without a human.

## Lessons

Append here when you learn something non-obvious that is not yet a rule. Once
a lesson becomes a rule, move it into `CONTRIBUTING.md` or a data file and
delete it here, so this file stays short.

* Keep one commit per logical change with a body that explains *why*; the
  history is how later sessions learn what was tried (for example which hosts
  failed and why an entry was re-hosted).
