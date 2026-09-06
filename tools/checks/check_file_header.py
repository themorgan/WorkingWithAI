#!/usr/bin/env python3
"""check_file_header.py -- the mechanical check for practices/file-header.md.

# practice: file-header

Scope: change, over every markdown file tracked in the repo (applies_to
"**/*.md"). A file "carries this header" (the practice's own occasion
clause) once its first line matches the format below -- untouched files
that never had one are not required to grow one; that's a per-edit choice,
not a repo-wide sweep, per the practice's own Detail section. A line has
to both start "<!-- Last updated:" *and* name Morgan to count as an
attempt at this header -- vendored third-party content (e.g. a consuming
repo's process/upstream/ tree) can have its own, different, complete
attribution convention that happens to share the prefix; that's not this
practice's business and isn't flagged as malformed.

Two things are checked mechanically for every file that does carry it:

1. Format -- the first line must match the header exactly:
   <!-- Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by Morgan F, to version N -->
   with N a plain positive integer.

2. Version continuity, against this file's own content in the parent
   commit (HEAD~1) where available:
   - if the file's body (everything after the header line) changed,
     N must have increased from the parent commit's N;
   - if the body did not change, N must be unchanged too (no header
     "touch-up" without a real edit).
   A file with no parent version (newly added, or the header is new in
   this commit) is exempt from continuity -- there is nothing to compare
   against -- but a freshly added header must start at version 1.

Exit 0 and print nothing when clean. Exit 1 and print the practice's own
Rule text (never a paraphrase) plus the specific finding(s) on a violation.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PRACTICE_FILE = ROOT / "practices" / "file-header.md"

HEADER_RE = re.compile(
    r"^<!-- Last updated: (\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2}):(\d{2}) "
    r"\(Buenos Aires\) by Morgan F, to version (\d+) -->$"
)
# A line that's clearly *trying* to be the header but doesn't match exactly
# -- used to flag malformed headers, not just missing ones.
HEADER_ATTEMPT_RE = re.compile(r"^<!--\s*Last updated:", re.IGNORECASE)


def is_header_attempt(line: str) -> bool:
    # A "Last updated:" prefix alone isn't enough to call a line an attempt
    # at *this* header format -- vendored third-party content (e.g. a
    # consuming repo's process/upstream/ tree) can carry its own, different,
    # complete attribution convention that happens to start the same way.
    # That's not this practice's business and shouldn't be flagged as
    # malformed just for not saying "Morgan F". Require the name too.
    return bool(HEADER_ATTEMPT_RE.match(line)) and "morgan" in line.lower()


def rule_text() -> str:
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


# --- scope: this repo's own content only ---------------------------------
#
# A check runs in two very different places. In the SOURCE repo that
# authors these practices, everything is authored and everything is in
# scope. In a CONSUMING repo, `practices/` is precedent_materialize.py's
# output and the universal source's `path` (e.g. `process/upstream/`) is a
# vendored copy of somebody else's tree -- content this repo did not write
# and cannot fix. Reporting a finding there is noise: the fix belongs in
# the source, and the consumer's only options are to ignore its own gate or
# to hand-edit a file the next sync overwrites.
#
# 2026-09-06, in a real four-source consumer: no-stale-counts reported 81
# findings, 81 of them inside materialized practices/ and vendored
# process/upstream/; private-repo-scrub reported 12 of 26 there. A gate
# that loud is a gate nobody reads.
#
# Attributed by the COMMITTED MANIFEST.json (which precedent_materialize.py
# writes, recording exactly which files it produced) and by precedent.json's
# declared source paths -- never by which sources happen to resolve in this
# environment, which is the mistake that once failed a repo's own CI on
# every team- and individual-sourced file because a bare checkout can reach
# neither. A repo-local source at `local/` stays in scope: that IS the
# repo's own hand-authored content.
def _foreign_prefixes() -> tuple:
    out = set()
    cfg = ROOT / "precedent.json"
    if cfg.is_file():
        try:
            for s in json.loads(cfg.read_text(encoding="utf-8")).get("sources", []):
                p = str(s.get("path", "")).strip().strip("/")
                if p and p != "local" and not p.startswith("..") and (ROOT / p).is_dir():
                    out.add(p + "/")
        except (OSError, json.JSONDecodeError, AttributeError):
            pass
    return tuple(sorted(out))


def _materialized_files() -> frozenset:
    mf = ROOT / "MANIFEST.json"
    if not mf.is_file():
        return frozenset()
    try:
        m = json.loads(mf.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return frozenset()
    files = {f"practices/{e['slug']}.md" for e in m.get("practices", []) if "slug" in e}
    files |= {e["path"] for e in m.get("checks", []) if "path" in e}
    return frozenset(files)


_FOREIGN = _foreign_prefixes()
_MATERIALIZED = _materialized_files()


def not_ours(rel) -> bool:
    """True when `rel` is content this repo vendored or materialized rather
    than wrote."""
    rel = str(rel).replace("\\", "/")
    return rel.startswith(_FOREIGN) or rel in _MATERIALIZED


def tracked_md_files() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "*.md"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines()
            if line.strip() and not not_ours(line.strip())]


def read_at_head(path: str, rev: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{rev}:{path}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def find_violations() -> list[str]:
    findings = []
    for path in tracked_md_files():
        current = read_at_head(path, "HEAD")
        if current is None:
            continue
        lines = current.splitlines()
        first = lines[0] if lines else ""

        if not is_header_attempt(first):
            continue  # doesn't carry the header at all -- not required to

        m = HEADER_RE.match(first)
        if not m:
            findings.append(f"{path}: first line looks like the header but doesn't match the required format: {first!r}")
            continue

        version = int(m.group(5))
        body = "\n".join(lines[1:])

        parent = read_at_head(path, "HEAD~1")
        if parent is None:
            if version != 1:
                findings.append(f"{path}: header is new in this commit but starts at version {version}, expected 1")
            continue

        parent_lines = parent.splitlines()
        parent_first = parent_lines[0] if parent_lines else ""
        parent_m = HEADER_RE.match(parent_first)
        if not parent_m:
            # The parent commit may have carried a MALFORMED header attempt
            # (a real published incident: a previous commit's own header
            # dropped its HH:MM:SS component, per this check's own history)
            # rather than no header at all -- "no header in the parent" and
            # "a broken header in the parent" are different situations, and
            # treating the second as the first forces every subsequent
            # correctly-formatted commit to restart numbering at 1, which
            # would misrepresent a file's real edit history for one
            # already-published formatting slip. Recover a version number
            # from the malformed line if one is findable at all, and only
            # fall back to "no header" semantics when it truly isn't.
            if is_header_attempt(parent_first):
                loose = re.search(r"version (\d+)", parent_first)
                if loose:
                    parent_version = int(loose.group(1))
                    parent_body = "\n".join(parent_lines[1:])
                    if body != parent_body:
                        if version <= parent_version:
                            findings.append(
                                f"{path}: content changed since the parent commit's "
                                f"(malformed-header) version {parent_version} but "
                                f"version stayed at {version} -- bump it"
                            )
                    else:
                        if version != parent_version:
                            findings.append(
                                f"{path}: version changed from {parent_version} to "
                                f"{version} but the file's content didn't change -- "
                                "only bump N when content changes"
                            )
                    continue
            if version != 1:
                findings.append(f"{path}: header is new (parent revision carried none) but starts at version {version}, expected 1")
            continue

        parent_version = int(parent_m.group(5))
        parent_body = "\n".join(parent_lines[1:])

        if body != parent_body:
            if version <= parent_version:
                findings.append(
                    f"{path}: content changed since the parent commit but version stayed at {version} "
                    f"(was {parent_version}) -- bump it"
                )
        else:
            if version != parent_version:
                findings.append(
                    f"{path}: version changed from {parent_version} to {version} but the file's content "
                    "didn't change -- only bump N when content changes"
                )
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
