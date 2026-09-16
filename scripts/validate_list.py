#!/usr/bin/env python3
"""Structural checks for README.md.

Enforces the conventions described in CONTRIBUTING.md so that both human and
automated contributions stay consistent. Exits non-zero on any error.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

README = Path(__file__).resolve().parent.parent / "README.md"

ENTRY_RE = re.compile(r"^\* \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\) - (?P<desc>.+)$")
TOC_RE = re.compile(r"^\* \[(?P<title>[^\]]+)\]\(#(?P<anchor>[^)]+)\)$")

# Sections that hold links to other lists rather than tools.
TOC_HEADING = "## Contents"

# Section with its own ordering rule, enforced below.
PAPERS_SECTION = "Research Papers"
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")


def anchor_for(heading: str) -> str:
    """GitHub's anchor slug for a heading."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    return re.sub(r"\s+", "-", slug)


def main() -> int:
    text = README.read_text(encoding="utf-8")
    lines = text.split("\n")
    errors: list[str] = []

    # --- collect sections and entries ---
    sections: list[str] = []
    entries: list[tuple[int, str, str, str]] = []  # lineno, name, url, desc
    toc: list[str] = []

    in_toc = False
    current_section = None

    for i, line in enumerate(lines, start=1):
        if line.startswith("## "):
            heading = line[3:].strip()
            in_toc = line.strip() == TOC_HEADING
            if not in_toc:
                sections.append(heading)
                current_section = heading
            continue

        if not line.startswith("* "):
            continue

        if in_toc:
            m = TOC_RE.match(line)
            if not m:
                errors.append(f"{i}: malformed table-of-contents line: {line}")
            else:
                toc.append(m.group("title"))
                expected = anchor_for(m.group("title"))
                if m.group("anchor") != expected:
                    errors.append(
                        f"{i}: anchor '#{m.group('anchor')}' should be '#{expected}'"
                    )
            continue

        m = ENTRY_RE.match(line)
        if not m:
            errors.append(
                f"{i}: entry does not match '* [Name](url) - Description.': {line}"
            )
            continue

        name, url, desc = m.group("name"), m.group("url"), m.group("desc")
        entries.append((i, name, url, desc, current_section))

        if current_section is None:
            errors.append(f"{i}: entry appears before any section heading")
        if not desc.endswith("."):
            errors.append(f"{i}: description for '{name}' must end with a period")
        if len(desc) < 25:
            errors.append(f"{i}: description for '{name}' is too short to be useful")
        parsed = urlparse(url)
        if parsed.scheme != "https":
            errors.append(f"{i}: '{name}' must use an https URL, got '{url}'")
        if not parsed.netloc:
            errors.append(f"{i}: '{name}' has a malformed URL '{url}'")

    # --- table of contents must match the actual sections, in order ---
    if toc != sections:
        errors.append(
            "table of contents does not match section headings.\n"
            f"  contents:  {toc}\n"
            f"  headings:  {sections}"
        )

    # --- duplicates ---
    def normalise(url: str) -> str:
        u = url.rstrip("/").lower()
        return u[len("https://") :] if u.startswith("https://") else u

    for url, count in Counter(normalise(u) for _, _, u, _, _ in entries).items():
        if count > 1:
            where = [str(i) for i, _, u, _, _ in entries if normalise(u) == url]
            errors.append(f"duplicate URL '{url}' on lines {', '.join(where)}")

    for name, count in Counter(n.lower() for _, n, _, _, _ in entries).items():
        if count > 1:
            where = [str(i) for i, n, _, _, _ in entries if n.lower() == name]
            errors.append(f"duplicate entry name '{name}' on lines {', '.join(where)}")

    # --- Section layout: a blank line after each heading, none between entries ---
    for i, line in enumerate(lines):
        if line.startswith("## ") and i + 1 < len(lines) and lines[i + 1].strip():
            errors.append(f"{i + 2}: '{line[3:].strip()}' needs a blank line after the heading")
        if line.startswith("* [") and i + 1 < len(lines):
            following = lines[i + 1 :]
            nxt = next((l for l in following if l.strip()), "")
            if not lines[i + 1].strip() and nxt.startswith("* ["):
                errors.append(f"{i + 2}: blank line inside a list; entries are consecutive")

    # --- Every other section is alphabetical by entry name ---
    previous = {}
    for lineno, name, _, _, section in entries:
        if section == PAPERS_SECTION:
            continue
        key = name.casefold()
        last = previous.get(section)
        if last and key < last[0]:
            errors.append(
                f"{lineno}: '{name}' is out of order — it follows '{last[1]}'. "
                f"{section} is alphabetical by entry name, ignoring case."
            )
        else:
            previous[section] = (key, name)

    # --- Research Papers are ordered by year of publication, oldest first ---
    papers = [(i, n, d) for i, n, _, d, sec in entries if sec == PAPERS_SECTION]
    previous_year = 0
    previous_name = None
    for lineno, name, desc in papers:
        match = YEAR_RE.search(desc)
        if not match:
            errors.append(
                f"{lineno}: '{name}' must state its publication year, as "
                "'Surname et al., Venue Year.'"
            )
            continue
        year = int(match.group(0))
        if year < previous_year:
            errors.append(
                f"{lineno}: '{name}' ({year}) is out of order — it follows "
                f"'{previous_name}' ({previous_year}). {PAPERS_SECTION} is "
                "ordered by year, oldest first."
            )
        else:
            previous_year, previous_name = year, name

    if errors:
        print(f"{len(errors)} problem(s) found in README.md:\n", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"README.md OK: {len(sections)} sections, {len(entries)} entries, "
        "table of contents in sync."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
