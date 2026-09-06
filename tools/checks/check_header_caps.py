#!/usr/bin/env python3
"""check_header_caps.py -- the mechanical check for practices/header-caps.md.

# practice: header-caps

Scope: tree, over every tracked `*.md` file (applies_to). This covers one
half of the rule, the half that's unambiguous regardless of which scheme a
document picked: "headers and subheaders at the same rank in a document
must all follow one capitalization style, never mixed."

It does NOT check the other half -- that the default scheme, absent a
documented reason otherwise, is specifically NY Times headline style.
Classifying a word as "principal" vs. "minor" for headline-style has
enough genuine edge cases (a preposition used adjectivally, a short verb
that's actually the sentence's main verb) that a check built on a fixed
word list would misfire regularly rather than actually enforce the rule --
see the practice file's own Install section for where this is documented.

What IS checkable without a word list: the same word, appearing in more
than one header at the same rank in the same document, capitalized one
way in one header and a different way in another (excluding each header's
own first and last word, which the rule already exempts from the
minor-word rule) is exactly a scheme mix caught in the act -- direct
evidence of the violation the rule's first sentence names, with no
heuristic about what "principal" means required.

Exit 0 and print nothing when clean. Exit 1 and print the practice's own
Rule text (never a paraphrase) plus the specific finding(s) on a violation.
"""
import os
import pathlib
import json
import re
import subprocess
import sys
from collections import defaultdict

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
PRACTICE_FILE = SOURCE_ROOT / "practices" / "header-caps.md"

ATX_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")


# --- shared:scope-helper — keep byte-identical across every copy ---
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
# and the fix has to go to the generator anyway. 2026-09-06: a mirrored
# voice pack, whose first line reads "GENERATED FILE - do not hand-edit",
# was the last thing standing between a real consumer and a clean run.
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
# --- end shared:scope-helper ---


def rule_text() -> str:
    # A materialized check runs in whatever repo its source was resolved
    # into, and the practice file it quotes is not guaranteed to be there:
    # a repo that declares the source but never materializes it, or a
    # practice retired out of the tree, both leave PRACTICE_FILE absent.
    # Unguarded, this raised FileNotFoundError from inside the violation
    # PRINTER -- so the finding was correctly detected, correctly printed,
    # and then buried under a traceback. Found 2026-09-06 running every
    # source-supplied check against BestPractice; 14 of the 16 shared this
    # exact body. The Rule text being unavailable is not the check failing.
    if not PRACTICE_FILE.is_file():
        return "(practice file not found at %s)" % PRACTICE_FILE
    text = PRACTICE_FILE.read_text(encoding="utf-8")
    m = re.search(r"## Rule\n(.*?)\n## ", text, re.S)
    return m.group(1).strip() if m else "(no Rule found)"


def tracked_md_files() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "*.md"],
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in result.stdout.splitlines()
            if line.strip() and not not_ours(line.strip())]


def headers_by_rank(text: str) -> dict[int, list[str]]:
    by_rank: dict[int, list[str]] = defaultdict(list)
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = ATX_RE.match(line)
        if m:
            by_rank[len(m.group(1))].append(m.group(2))
    return by_rank


def find_violations() -> list[str]:
    findings = []
    for rel in tracked_md_files():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for rank, headers in headers_by_rank(text).items():
            if len(headers) < 2:
                continue
            # word (lowercased) -> set of capitalization states seen, excluding
            # each header's own first/last word (the rule's own exemption)
            seen: dict[str, set[bool]] = defaultdict(set)
            examples: dict[str, list[str]] = defaultdict(list)
            for header in headers:
                words = WORD_RE.findall(header)
                if len(words) < 3:
                    continue  # nothing but boundary words to compare
                for w in words[1:-1]:
                    key = w.lower()
                    seen[key].add(w[0].isupper())
                    examples[key].append(f"{w!r} in {header!r}")
            for word, states in seen.items():
                if len(states) > 1:
                    findings.append(
                        f"{rel} (h{rank}): {word!r} capitalized inconsistently across "
                        f"same-rank headers -- {'; '.join(examples[word])}"
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
