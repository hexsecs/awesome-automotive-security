# Discover new entries

You are maintaining the awesome-automotive-security list in this repository.
This runbook is read both by the `discover.yml` GitHub Action and by the
scheduled Claude Code Routine, so it does not assume either. Where it says
"open a draft PR" or "comment", use `gh` or your GitHub tools, whichever you
have. If you have neither, as in a Routine session, follow "Reaching GitHub"
in `prompts/sweep.md`.

## Before you start

0. If an open PR whose body's first line contains `automated: discover` was
   opened this calendar month, another runner has already done this month's
   pass: stop without changes. Match that text, not the `<!--` delimiters,
   which arrive HTML-escaped on PRs opened automatically from a pushed branch.
1. Read `CONTRIBUTING.md`. It defines the inclusion criteria and the exact
   entry format, and every rule in it binds you.
2. Read `data/hosts.toml`. Never link a host listed under `avoid`; prefer
   hosts listed under `reliable`.
3. Read `data/decisions.toml`. Never propose anything recorded there. If you
   believe a recorded decision should be overturned (an archived project
   revived, a paper that has since become influential), you may propose it
   only by deleting its record in the same change and arguing the case in the
   PR body.
4. Run `python3 scripts/list_health.py` (with `GITHUB_TOKEN` set if you have
   one) and read the report. If its GitHub API calls all fail, as they can in
   a sandbox, run it with `--no-github` for coverage alone. Thin sections are
   one input, not the whole plan: archived, moved and dormant entries are
   candidates for a successor or a URL update.
5. Run `python3 scripts/probe_egress.py`. A cloud session's egress proxy can
   allow far less than CI does, and a blocked host looks the same as a dead
   link. The probe separates hosts the proxy blocks (the sandbox's limit) from
   hosts that answer but refuse automated clients (their bot filter) and from
   DNS failures. Plan research around what is reachable. Never record a host in
   `data/hosts.toml` on the strength of a sandbox block. If a fetch tool fails
   where the probe succeeds, try `curl` through the same proxy, and say in the PR
   which tool failed.
6. Read `data/leads.toml`: candidates earlier runs found but could not open.
   Re-try each one. If it now opens and qualifies, add it to `README.md` and
   delete the lead; if it fails CONTRIBUTING.md, record a `rejected` decision
   and delete the lead; if it still cannot be opened, leave it, and update its
   `reason` only if you learned something.

If the run was given a focus area, concentrate on it.

## Research

1. Build the set of URLs already in `README.md`.
2. Research automotive security tools, research artifacts, datasets, and
   learning resources published or meaningfully updated in roughly the last
   year. Give thin sections some attention, but do not limit the search to
   them: a thin section can simply be a small subfield, and new tools,
   datasets and papers often belong in well-populated sections. Cover every
   section each run. Look at GitHub topics
   (automotive-security, car-hacking, can-bus, iso15118, uds), recent
   conference output (DEF CON Car Hacking Village, Black Hat, Pwn2Own
   Automotive, escar, VehicleSec), and academic venues (NDSS VehicleSec,
   USENIX Security).
3. For every candidate, run `python3 scripts/check_candidate.py <url>` and also
   FETCH THE URL AND CONFIRM IT RESOLVES before proposing it. Never propose a
   link you have not opened. The checker covers what a page summary does not:
   whether the URL is already listed, a lead, or recorded in
   `data/decisions.toml`; the host rules; and for a GitHub repository whether it
   is archived, dormant, renamed, or a fork of a more-used project (it reads
   the GitHub API, and falls back to ecosyste.ms, labelled as third-party, where
   the API is refused). A BLOCKER means do not propose it. Answer every WARNING
   in the PR. Note whether the project is archived; propose archived projects
   only when they are still canonical or historically important, and say so in
   the description.
4. Drop anything already on the list, anything failing the CONTRIBUTING.md
   criteria, and anything whose whole subdomain is better served by a linked
   Awesome list.

## Change

1. Add the survivors to the right sections of `README.md` in the required
   format, in alphabetical order by name within the section. Research Papers
   is the one exception: it is ordered by year of publication, oldest first.
   Never append to the end of a section.
2. Quality over volume: five well-checked entries beat thirty unchecked ones.
   Zero good candidates is an acceptable outcome.
3. Fix existing entries whose links now 404 or redirect to a new canonical
   home, including any the health report flagged as moved.

## Leave the next run smarter

This is what makes the list improve rather than just grow. In the same PR:

* **Durable rejections.** A candidate you researched and dropped for a reason
  that will still hold next month (out of scope, superseded, vendor-only
  marketing, no open copy anywhere) gets a `rejected` record in
  `data/decisions.toml`, so no future run spends effort on it again. Do not
  record transient reasons such as a host being down today. Only record clear
  failures of CONTRIBUTING.md (plainly out of scope, an `avoid` host with no
  open copy, a duplicate of a listed entry).
* **Leads.** A candidate that looks worth proposing but whose link you could
  not open (the proxy blocks the host, or the page needs a browser) goes into
  `data/leads.toml`, with what you know and exactly what is unverified. It is
  neither an addition nor a rejection. This replaces leaving such candidates
  only in the PR body, which the next run never reads.
* **Flag borderline candidates, do not reject them.** If a candidate is a
  judgement call (low traction, overlaps a listed tool, thin evidence of use),
  the decision is the maintainer's, not yours. Add it to `README.md` like any
  other entry, and list it in a "Flagged for review" section of the PR body
  with your concern. Record no `rejected` decision for it. If the maintainer
  removes it in review, the sweep records the rejection.
* **Host lessons.** If a host bot-challenged you or served the page only to a
  browser, add it to `data/hosts.toml` under `avoid` with the reason. If a new
  host worked reliably, add it under `reliable`.

## Finish

1. Run `python3 scripts/validate_list.py` and make it pass.
2. If nothing changed, stop without opening a PR.
3. Otherwise commit on a new branch named `discover/<YYYY-MM>` and open a
   DRAFT pull request against `main`. Start the body with the line
   `<!-- automated: discover -->` so later runs can find it. Then list each
   proposed entry with the evidence you gathered: what it is, why it meets
   the criteria, and confirmation that you opened the link. List the
   decisions, leads and host records you added or resolved, and why. Put every borderline
   candidate under "Flagged for review" as described above.

Never merge anything and never push to `main`. A maintainer reviews every
proposal.
