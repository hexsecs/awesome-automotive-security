# Discover new entries

You are maintaining the awesome-automotive-security list in this repository.
This runbook is read both by the `discover.yml` GitHub Action and by the
scheduled Claude Code Routine, so it does not assume either. Where it says
"open a draft PR" or "comment", use `gh` or your GitHub tools, whichever you
have.

## Before you start

0. If an open PR whose body starts with `<!-- automated: discover -->` was
   opened this calendar month, another runner has already done this month's
   pass: stop without changes.
1. Read `CONTRIBUTING.md`. It defines the inclusion criteria and the exact
   entry format, and every rule in it binds you.
2. Read `data/hosts.toml`. Never link a host listed under `avoid`; prefer
   hosts listed under `reliable`.
3. Read `data/decisions.toml`. Never propose anything recorded there. If you
   believe a recorded decision should be overturned (an archived project
   revived, a paper that has since become influential), you may propose it
   only by deleting its record in the same change and arguing the case in the
   PR body.
4. Run `python3 scripts/list_health.py` and read the report. Thin sections are
   where research effort goes first; archived, moved and dormant entries are
   candidates for a successor or a URL update.

If the run was given a focus area, concentrate on it.

## Research

1. Build the set of URLs already in `README.md`.
2. Research automotive security tools, research artifacts, datasets, and
   learning resources published or meaningfully updated in roughly the last
   year, weighted towards the thin sections. Look at GitHub topics
   (automotive-security, car-hacking, can-bus, iso15118, uds), recent
   conference output (DEF CON Car Hacking Village, Black Hat, Pwn2Own
   Automotive, escar, VehicleSec), and academic venues (NDSS VehicleSec,
   USENIX Security).
3. For every candidate, FETCH THE URL AND CONFIRM IT RESOLVES before proposing
   it. Never propose a link you have not opened. Note whether the project is
   archived; propose archived projects only when they are still canonical or
   historically important, and say so in the description.
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
  record transient reasons such as a host being down today.
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
   decisions and host records you added and why. Flag anything you were
   unsure about so a human can adjudicate it.

Never merge anything and never push to `main`. A maintainer reviews every
proposal.
