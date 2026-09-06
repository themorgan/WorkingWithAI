#!/usr/bin/env python3
"""check_my_identity_is_not_private.py -- my-identity-is-not-private.

Fails if a blocklist in this repository lists my display name, my GitHub
owner name, my city or my timezone. Those appear in the upstream practice
layer's own date headers, so blocklisting them makes a scrub gate report
failures no edit here can clear -- one repo sat at 116 of them, with its
own instructions saying that gate must pass before any commit touching
`process/`. practice: my-identity-is-not-private.

Exit 0 clean, 1 violated, 2 could-not-run.
"""
import json
import os
import pathlib
import re
import sys

# TWO different questions, which used to share one name -- and that is exactly
# how a practice file went missing. SOURCE_ROOT is the practice set this script
# ships in; ROOT is the repository it AUDITS.
#
# They are the same directory in both normal cases: run in place inside its own
# set, and materialized into a consuming repo (where precedent_materialize.py
# has written practices/ and tools/checks/ side by side). They differ in the
# third case -- a repo that DECLARES this source but never materializes it, and
# runs the script in place against itself. Precedent's own repo is exactly
# that: its practices/ is the universal catalogue, so `parents[2]/practices/`
# resolved to a directory this practice was never in, and rule_text() raised
# FileNotFoundError from inside the violation printer (2026-09-06). The rule
# text always ships beside the script, so it is looked up against SOURCE_ROOT
# and can no longer be absent; only what to audit is overridable.
SOURCE_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
ROOT = pathlib.Path(os.environ.get("PRECEDENT_CHECK_ROOT") or SOURCE_ROOT)
PRACTICE_FILE = SOURCE_ROOT / "practices" / "my-identity-is-not-private.md"

# Named exactly as the practice names them. A blocklist line is a regex, so
# the comparison is on the line's text with regex punctuation stripped --
# `\bMorgan F\b` and `Morgan F` are the same listing.
PROTECTED = ("Morgan F", "themorgan", "Buenos Aires",
             "America/Argentina/Buenos_Aires")

BLOCKLIST_GLOBS = ("**/scrub_blocklist.txt", "**/leak-blocklist.txt",
                   "**/*blocklist*.txt")

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


# A file whose own header says it is generated is not this repo's text
# either, whoever produced it. `generated-artifact-provenance` requires the
# marker precisely so nothing hand-edits the output; a check that then
# demands a hand-edit there is asking for the one thing the file forbids,
# and the fix has to go to the generator anyway.
_GENERATED_MARKERS = ("do not hand-edit", "do not edit", "generated file",
                      "derived artifact", "auto-generated", "autogenerated")


def _looks_generated(rel) -> bool:
    p = ROOT / rel
    try:
        with p.open(encoding="utf-8", errors="ignore") as fh:
            head = "".join(next(fh, "") for _ in range(6)).lower()
    except OSError:
        return False
    return any(m in head for m in _GENERATED_MARKERS)


def not_ours(rel) -> bool:
    """True when `rel` is content this repo vendored, materialized, or
    generated rather than wrote."""
    rel = str(rel).replace("\\", "/")
    return (rel.startswith(_FOREIGN) or rel in _MATERIALIZED
            or _looks_generated(rel))

def rule_text() -> str:
    if not PRACTICE_FILE.is_file():
        return "(practice file not found)"
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


def _bare(line: str) -> str:
    """A blocklist line with its regex punctuation removed."""
    return re.sub(r"\\b|\\|\^|\$|\(|\)|\[|\]|\+|\*|\?", "", line).strip()


def find_violations() -> list:
    seen, findings = set(), []
    for pattern in BLOCKLIST_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            if rel in seen or not path.is_file():
                continue
            seen.add(rel)
            # A .template documents the format rather than configuring
            # anything, and vendored or materialized trees are not ours.
            if rel.endswith(".template") or not_ours(rel):
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8",
                                                    errors="ignore").splitlines(), 1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                bare = _bare(stripped)
                for term in PROTECTED:
                    if bare.lower() == term.lower():
                        findings.append(
                            f"{rel}:{i}: lists {term!r}, which is not private. "
                            f"It appears in upstream's own date headers, so "
                            f"listing it makes this repo's scrub gate report "
                            f"failures nothing here can clear. Remove the line.")
    return findings


if __name__ == "__main__":
    found = find_violations()
    if found:
        print(f"VIOLATION: {PRACTICE_FILE.stem}")
        for f in found:
            print(f"  {f}")
        print("")
        print("the rule:")
        for line in rule_text().splitlines():
            print(f"  {line}")
        sys.exit(1)
    sys.exit(0)
