#!/usr/bin/env python3
"""check_assorted_notes.py -- the mechanical check for practices/assorted-notes.md.

# practice: assorted-notes

Scope: tree, over every file tracked in the repo. The practice's Rule is
that nothing in a `content/ASSORTED_NOTES.md` (or a legacy equivalent not
yet renamed) may be *referenced* from anywhere else -- it exists precisely
for content not ready to be pointed to. A real reference, in a repo whose
own standing convention is "doc references are links, never bare
filenames" (`doc-references-are-links`), takes the form of a markdown
link whose target path ends in one of the recognized filenames. This
check looks for exactly that: a markdown link `[...](...ASSORTED_NOTES.md)`
(or a legacy name) anywhere outside the practice file that defines this
convention and the notes file itself.

It cannot see a prose reference with no link ("see the notes file for
why") -- that's a judgment call with no reliable mechanical signature,
same as `checkable-gets-checked`'s own standing allowance for a practice
that is only partly checkable. The link form is the common, catchable
case in a repo that otherwise always links.

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
NOTES_FILENAMES = ("ASSORTED_NOTES.md", "BRAINSTORM.md", "NOTES.md", "IDEAS.md")

LINK_RE = re.compile(
    r"\]\(([^)]*(?:" + "|".join(re.escape(n) for n in NOTES_FILENAMES) + r"))\)"
)

# Files allowed to mention the notes file's own path without that counting
# as a reference to its *content* -- the practice file that documents the
# convention, and the notes file itself (a self-link, e.g. a header anchor).
EXEMPT_BASENAMES = {"assorted-notes.md"} | {n.lower() for n in NOTES_FILENAMES}

# This check's own machinery: its docstring illustrates the exact link
# pattern it looks for, and its test plants that pattern as a fixture --
# neither is a real reference to real notes content.
EXEMPT_PATHS = {
    "tools/checks/check_assorted_notes.py",
    "tools/checks/tests/test_assorted_notes.sh",
}


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
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in LINK_RE.finditer(line):
                findings.append(f"{path}:{lineno}: links to {m.group(1)!r}")
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
