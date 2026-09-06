#!/usr/bin/env python3
"""check_assorted_notes.py -- the mechanical check for practices/assorted-notes.md.

# practice: assorted-notes

Scope: tree, over every file tracked in the repo. The practice's Rule is
that nothing outside `content/ASSORTED_NOTES.md` (or a legacy equivalent
not yet renamed) may *cite* an idea from inside it -- but a plain link
from a listing context is allowed, since inventorying that the file
exists is not the same as citing something inside it. Two such contexts:
a directory-listing document (any `README.md` or `MAP.md`, at any
depth), and a "## See also" section in ANY file -- a page-to-page
cross-reference footer is the same listing move distributed per-page
instead of centralized in one index. A real citation, in a repo whose
own standing convention is "doc references are links, never bare
filenames" (`doc-references-are-links`), takes the form of a markdown
link whose target path ends in one of the recognized filenames. This
check looks for exactly that: a markdown link `[...](...ASSORTED_NOTES.md)`
(or a legacy name) outside the practice file, the notes file itself, any
listing document, and any "## See also" section.

It cannot see a prose reference with no link ("see the notes file for
why") -- that's a judgment call with no reliable mechanical signature,
same as `checkable-gets-checked`'s own standing allowance for a practice
that is only partly checkable. The link form is the common, catchable
case in a repo that otherwise always links.

A link's target is matched by its *basename* exactly, not by whether it
ends in one of the recognized filenames as a substring -- a real link to
`content/MARKETING_IDEAS.md` or `content/RANDOM_NOTES.md` is not a
reference to `ASSORTED_NOTES.md`/`NOTES.md`/`IDEAS.md` just because its
own filename happens to end the same way. The same basename-exact rule
applies to the listing-document exemption: a file merely named
`SOMETHING_README.md` doesn't qualify -- only a basename that is exactly
`README.md` or `MAP.md` does.

Exit 0 and print nothing when clean. Exit 1 and print the practice's own
Rule text (never a paraphrase) plus the specific finding(s) on a violation.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PRACTICE_FILE = ROOT / "practices" / "assorted-notes.md"

# Legacy names this practice says to consolidate into ASSORTED_NOTES.md --
# a link to any of these, in an unrenamed legacy repo, is the same violation.
LEGACY_FILENAMES = ("BRAINSTORM.md", "NOTES.md", "IDEAS.md")
CANONICAL_FILENAME = "ASSORTED_NOTES.md"


def notes_filenames() -> tuple:
    """The canonical name always; the legacy names only until the migration
    this practice describes has actually happened.

    "In an unrenamed legacy repo" is the condition the comment above states
    and the check did not test: it matched any file named NOTES.md, anywhere,
    forever. Once `content/ASSORTED_NOTES.md` exists the consolidation is
    done, and a file that merely shares a legacy name is an ordinary file
    with its own subject -- 2026-09-06, a repo with a perfectly good
    content/ASSORTED_NOTES.md was flagged for linking `book-moses/NOTES.md`,
    a manuscript-scoped brainstorm about Moses that is not this repo's
    catch-all and was never meant to become it. Reading the legacy names as
    permanent turns a one-time migration rule into a standing ban on a
    common filename."""
    if (ROOT / "content" / CANONICAL_FILENAME).is_file():
        return (CANONICAL_FILENAME,)
    return (CANONICAL_FILENAME,) + LEGACY_FILENAMES

# Matches any markdown link's target; the target is then checked against
# notes_filenames() by basename, not by this regex, so a filename that merely
# ends the same way (MARKETING_IDEAS.md, RANDOM_NOTES.md) doesn't match.
LINK_RE = re.compile(r"\]\(([^)]+)\)")

# Files allowed to mention the notes file's own path without that counting
# as a reference to its *content* -- the practice file that documents the
# convention, and the notes file itself (a self-link, e.g. a header anchor).
# Any README.md or MAP.md, at any depth, is also exempt: a directory listing
# names what exists, which isn't citing anything inside it -- see the Rule's
# own "listing vs. citation" distinction.
EXEMPT_BASENAMES = (
    {"assorted-notes.md", "readme.md", "map.md"}
    | {n.lower() for n in notes_filenames()}
)

# This check's own machinery: its docstring illustrates the exact link
# pattern it looks for, and its test plants that pattern as a fixture --
# neither is a real reference to real notes content.
EXEMPT_PATHS = {
    "tools/checks/check_assorted_notes.py",
    "tools/checks/tests/test_assorted_notes.sh",
}

# A "## See also" section is a listing context too -- exempt lines inside
# one, from its heading to the next "## " heading or end of file.
SEE_ALSO_RE = re.compile(r"^## See also\s*$")
HEADING_RE = re.compile(r"^## ")


def rule_text() -> str:
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def find_violations() -> list[str]:
    findings = []
    for path in tracked_files():
        if pathlib.Path(path).name.lower() in EXEMPT_BASENAMES:
            continue
        if path in EXEMPT_PATHS:
            continue
        full = ROOT / path
        try:
            text = full.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        in_see_also = False
        for lineno, line in enumerate(text.splitlines(), start=1):
            if SEE_ALSO_RE.match(line):
                in_see_also = True
                continue
            if HEADING_RE.match(line):
                in_see_also = False
            if in_see_also:
                continue
            for m in LINK_RE.finditer(line):
                target = m.group(1)
                if pathlib.Path(target).name in notes_filenames():
                    findings.append(f"{path}:{lineno}: links to {target!r}")
    return findings


if __name__ == "__main__":
    findings = find_violations()
    if findings:
        print(f"VIOLATION: {PRACTICE_FILE.stem}")
        for f in findings:
            print(f"  {f}")
        print("\nthe rule:")
        print("  " + rule_text().replace("\n", "\n  "))
        sys.exit(1)
    sys.exit(0)
