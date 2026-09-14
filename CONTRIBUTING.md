# Contributing

Thanks for helping keep this list useful. The goal is a list a working automotive
security researcher can skim and trust — not a mirror of every repository that
mentions CAN.

## What earns a place on the list

An entry should meet all of these:

1. **Automotive-specific.** It targets vehicles, ECUs, vehicle networks, or
   vehicle-adjacent infrastructure (EV charging, V2X, telematics backends).
   General-purpose tools belong here only when their automotive support is a
   headline feature — Scapy qualifies because of its DoIP/SOME/IP/SecOC layers;
   a generic hex editor does not.
2. **Useful to security work.** Analysis, reverse engineering, testing, defence,
   compliance, or learning. Pure tuning and telemetry projects are out of scope
   unless they are commonly used as security tooling.
3. **Publicly reachable.** A working URL that does not require an NDA, a sales
   call, or a login to learn what the thing is.
4. **Not already covered better elsewhere.** If a dedicated Awesome list covers
   a whole subdomain, link that list under
   [Related Awesome Lists](README.md#related-awesome-lists) instead of copying
   its contents here.
5. **Alive, or historically important.** Archived projects are fine when they
   are still the canonical implementation (URH) or a landmark piece of research.
   Abandoned projects with a maintained successor should link the successor.

## Entry format

One line per entry, in this exact shape:

```
* [Name](https://example.com/project) - Description ending in a period.
```

* Sentence case description, one sentence, ending in a period.
* Say what it *does* and what makes it distinct. "CAN tool" is not a description;
  "black-box CAN analysis framework with modular fuzzing and ECU discovery" is.
* No marketing adjectives, no star counts, no "the best".
* Insert new entries in alphabetical order by name within their section,
  ignoring case. [Research Papers](README.md#research-papers) is the sole
  exception and is ordered chronologically instead. Nothing is append-only:
  find the entry's place rather than adding it at the end.
* Add any new section to the `## Contents` table of contents as well.

Run the validator before opening a pull request:

```
python3 scripts/validate_list.py
```

## Research papers

The [Research Papers](README.md#research-papers) section is for foundational
and influential work, not for every new paper. To be listed, a paper should be
peer-reviewed (or a landmark industry report such as the Miller and Valasek
vehicle work) and should have visibly shaped later research or practice.

* Entries are ordered chronologically by year of publication, oldest first,
  rather than alphabetically like every other section. Insert a new paper at
  its place in the sequence. `scripts/validate_list.py` enforces the ordering
  and requires every entry to state a year.
* Link an open-access copy where one exists: the venue's own page for USENIX,
  NDSS, and similar, otherwise arXiv, an institutional repository, or the
  authors' copy. Avoid paywalled links when an open one is available.
* Credit authors as `Surname et al., Venue Year.` at the start of the
  description, then say in one sentence what the paper established.
* Some hosts answer the link checker with a bot challenge rather than the page.
  `dl.acm.org`, `ieeexplore.ieee.org` and `infoscience.epfl.ch` are therefore
  excluded from link checking, and their URLs are not machine-verified. Use one
  only when no open copy exists, and check the link by hand before adding it.
  Prefer dropping a candidate over adding a fourth excluded host: hosts that
  have proven reliable here are `usenix.org`, `arxiv.org`, `ndss-symposium.org`
  and `tches.iacr.org`. Known to bot-challenge, so avoid: `link.springer.com`,
  `eprint.iacr.org`, `semanticscholar.org`, `researchgate.net`, and Pure
  repository instances such as `pure.kaist.ac.kr`.

## Commercial entries

Commercial and closed-source tools are allowed when they are genuinely used in
the field, but the description must be neutral and factual. Pull requests that
add only a vendor's own product, from an account with no other history, will be
looked at sceptically.

## Automated maintenance

This repository maintains itself in part:

* `validate.yml` checks list formatting on every pull request.
* `link-check.yml` runs weekly and opens an issue when links rot.
* `discover.yml` runs monthly, researches candidate additions against the
  criteria above, and opens a **draft** pull request for a human to review.

Nothing lands automatically. Every automated proposal still needs a maintainer
to read it, check the links, and merge it.
