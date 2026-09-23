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
Systematization papers are the exception: a well-executed SoK or survey that
maps a subfield earns its place on quality alone, since its value to a reader
is immediate and does not depend on having accumulated citations.

* Entries are ordered chronologically by year of publication, oldest first,
  rather than alphabetically like every other section. Insert a new paper at
  its place in the sequence. `scripts/validate_list.py` enforces the ordering
  and requires every entry to state a year.
* Link an open-access copy where one exists: the venue's own page for USENIX,
  NDSS, and similar, otherwise arXiv, an institutional repository, or the
  authors' copy. Avoid paywalled links when an open one is available.
* Credit authors as `Surname et al., Venue Year.` at the start of the
  description, then say in one sentence what the paper established.
* Many paper hosts answer the link checker with a bot challenge rather than
  the page. Before choosing a URL, check the host against
  [Link hosts](#link-hosts): prefer a `reliable` host, never use an `avoid`
  one, and use an `excluded` host only when no open copy exists, checking the
  link by hand before adding it. Prefer dropping a candidate over extending the
  exclusions.

## Books

The [Books](README.md#books) section is for full-length books whose subject is
automotive or vehicle security, plus the vehicle network references that such
work depends on, such as CAN protocol guides. General security or embedded
titles that merely contain a vehicle chapter belong elsewhere, or nowhere.

* Link the publisher's page, or a free full-text edition where the author or
  publisher offers one. Where the publisher's own site refuses automated
  clients, link a neutral catalogue record instead so the entry stays
  machine-checkable. [Link hosts](#link-hosts) records which book hosts pass
  and which refuse.
* Credit the author, publisher and year as `Author, Publisher Year.` at the
  start of the description, then say what the book covers in one sentence.

## Commercial entries

Commercial and closed-source tools are allowed when they are genuinely used in
the field, but the description must be neutral and factual. Pull requests that
add only a vendor's own product, from an account with no other history, will be
looked at sceptically.

## Link hosts

What the list has learned about link hosts lives in one place,
[`data/hosts.toml`](data/hosts.toml), in three groups:

* `excluded` hosts bot-challenge automated clients but have stable,
  DOI-backed URLs. They are allowed, and both link-check workflows skip them,
  so their links are not machine-verified.
* `avoid` hosts bot-challenge and usually have an open alternative.
  `scripts/validate_list.py` rejects any entry linking to one.
* `reliable` hosts have passed the link checker here.

When a host teaches you something new, add a `[[excluded]]`, `[[avoid]]` or
`[[reliable]]` table with its `host` and a `reason` saying what the checker
returned and in which pull request. The validator and both workflows read the
file, so nothing else needs editing. Its header explains how hosts match,
including prefix patterns such as `pure.*`.

## Automated maintenance

This repository maintains itself in part:

* `validate.yml` checks list formatting on every pull request.
* `link-check.yml` runs weekly and opens an issue when links rot.
* Both link checks take their exclusions from `data/hosts.toml`.
* `discover.yml` runs monthly, researches candidate additions against the
  criteria above, and opens a **draft** pull request for a human to review.

Nothing lands automatically. Every automated proposal still needs a maintainer
to read it, check the links, and merge it.
