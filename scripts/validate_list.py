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
        entries.append((i, name, url, desc))

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

    for url, count in Counter(normalise(u) for _, _, u, _ in entries).items():
        if count > 1:
            where = [str(i) for i, _, u, _ in entries if normalise(u) == url]
            errors.append(f"duplicate URL '{url}' on lines {', '.join(where)}")

    for name, count in Counter(n.lower() for _, n, _, _ in entries).items():
        if count > 1:
            where = [str(i) for i, n, _, _ in entries if n.lower() == name]
            errors.append(f"duplicate entry name '{name}' on lines {', '.join(where)}")

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
