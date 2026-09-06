#!/usr/bin/env python3
"""check_claude_web_bootstrap.py -- the mechanical check for
practices/claude-web-bootstrap.md.

# practice: claude-web-bootstrap

Scope: tree. This repo plays two different roles with respect to this
practice, and the check has to tell them apart:

1. **This repo IS precedent-individual, the publisher.** Here, what gets
   checked is that the canonical artifacts this repo publishes for other
   projects to copy -- `bootstrap/session-start.sh` and
   `bootstrap/settings.snippet.json` -- still satisfy the structural
   invariants the practice's own Detail section spells out. Those
   invariants are exactly what would silently break the bootstrap for
   every consuming project if they regressed:

   - the script is git-tracked executable (mode 100755) and starts with a
     bash shebang;
   - it never exits non-zero -- a hard failure here would fail the whole
     session over a missing personal-preference layer, which is precisely
     what "fails gracefully" means;
   - the settings snippet is valid JSON, and its hook command path does
     not live under "$HOME" -- the hook that bootstraps
     precedent-individual cannot itself live somewhere only that
     bootstrap would create;
   - the hook entry is not marked "async": true -- synchronous is the
     whole point (see the script's own header).

2. **This repo is a project that consumed this practice** (materialized
   this repo's files into its own tree per the practice's own Install
   section) -- the common case for every project this check runs in that
   isn't precedent-individual itself. Here `bootstrap/session-start.sh`
   and `bootstrap/settings.snippet.json` are never expected to exist --
   those are this repo's own publishing paths, not a consumer's. What's
   checked instead is that the *consumer* pattern the Install section
   describes is actually in place: a `.claude/hooks/*.sh` script that
   clones precedent-individual and writes
   `~/.config/precedent/config.json`, wired into that project's own
   `.claude/settings.json` under `hooks.SessionStart`, synchronously (no
   `"async": true`), and still failing gracefully (never a hard non-zero
   exit). Only when *neither* the publisher files nor a working consumer
   install is found does this check report a real violation.

Exit 0 and print nothing when clean. Exit 1 and print the practice's own
Rule text (never a paraphrase) plus the specific finding(s) on a violation.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PRACTICE_FILE = ROOT / "practices" / "claude-web-bootstrap.md"
SCRIPT = ROOT / "bootstrap" / "session-start.sh"
SNIPPET = ROOT / "bootstrap" / "settings.snippet.json"

# Where a *consuming* project's own copy of this practice lives, per the
# practice file's own Install section (step 1: copy the script to
# .claude/hooks/; step 2: merge the snippet into .claude/settings.json).
CONSUMER_HOOKS_DIR = ROOT / ".claude" / "hooks"
CONSUMER_SETTINGS = ROOT / ".claude" / "settings.json"


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


def tracked_mode(path: pathlib.Path) -> str | None:
    rel = path.relative_to(ROOT)
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-s", str(rel)],
        capture_output=True,
        text=True,
        check=True,
    )
    line = result.stdout.strip()
    if not line:
        return None
    return line.split()[0]


def _consumer_script_candidates() -> list[pathlib.Path]:
    if not CONSUMER_HOOKS_DIR.is_dir():
        return []
    candidates = []
    for script in sorted(CONSUMER_HOOKS_DIR.glob("*.sh")):
        try:
            text = script.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if "precedent-individual" in text and ".config/precedent/config.json" in text:
            candidates.append(script)
    return candidates


def find_consumer_install() -> tuple[bool, list[str]]:
    """Look for a working *consumer* install of this practice (this repo
    isn't precedent-individual itself, but materialized its files per the
    practice's own Install section).

    Returns (ok, findings):
    - ok=True: a working install was found -- the caller reports no
      violation, full stop.
    - ok=False, findings non-empty: an install attempt exists but is
      broken in a specific, nameable way.
    - ok=False, findings empty: no install attempt exists at all -- the
      caller should fall back to its own (publisher-file) findings.
    """
    candidates = _consumer_script_candidates()
    if not candidates:
        return False, []

    settings_rel = CONSUMER_SETTINGS.relative_to(ROOT)
    if not CONSUMER_SETTINGS.exists():
        rel = candidates[0].relative_to(ROOT)
        return False, [f"{rel}: looks like a claude-web-bootstrap install but {settings_rel} is missing -- not wired into a SessionStart hook"]

    try:
        data = json.loads(CONSUMER_SETTINGS.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, [f"{settings_rel}: not valid JSON ({e})"]

    entries = (data.get("hooks") or {}).get("SessionStart") or []

    for script in candidates:
        rel = script.relative_to(ROOT)
        wired_hook = None
        for entry in entries:
            for hook in entry.get("hooks", []):
                command = hook.get("command", "")
                if rel.as_posix() in command or script.name in command:
                    wired_hook = hook
                    break
            if wired_hook is not None:
                break
        if wired_hook is None:
            continue  # not this candidate -- maybe another one is wired in

        if wired_hook.get("async") is True:
            return False, [f"{settings_rel}: hook entry for {rel} sets \"async\": true -- this bootstrap must run synchronously"]

        text = script.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = re.search(r"\bexit\s+([0-9]+)\b", line)
            if m and m.group(1) != "0":
                return False, [f"{rel}:{lineno}: `exit {m.group(1)}` -- this hook must fail gracefully (exit 0 always) rather than fail the session"]

        return True, []  # wired, synchronous, fails gracefully -- a working install

    rel = candidates[0].relative_to(ROOT)
    return False, [f"{rel}: looks like a claude-web-bootstrap install but no SessionStart hook entry in {settings_rel} references it"]


def find_violations() -> list[str]:
    findings = []

    if not SCRIPT.exists() or not SNIPPET.exists():
        # Not the publisher repo (or the publisher files are broken) --
        # before assuming that's a violation, check for a working consumer
        # install instead; a consuming project is never expected to have
        # its own bootstrap/ directory.
        ok, consumer_findings = find_consumer_install()
        if ok:
            return []
        if consumer_findings:
            return consumer_findings
        # else: no consumer install attempt either -- fall through and let
        # the checks below report the real violation.

    if not SCRIPT.exists():
        findings.append(f"{SCRIPT.relative_to(ROOT)}: missing")
    else:
        mode = tracked_mode(SCRIPT)
        if mode != "100755":
            findings.append(f"{SCRIPT.relative_to(ROOT)}: git-tracked mode is {mode}, expected 100755 (executable)")

        text = SCRIPT.read_text(encoding="utf-8")
        if not text.startswith("#!/bin/bash") and not text.startswith("#!/usr/bin/env bash"):
            findings.append(f"{SCRIPT.relative_to(ROOT)}: doesn't start with a bash shebang")

        for lineno, line in enumerate(text.splitlines(), start=1):
            m = re.search(r"\bexit\s+([0-9]+)\b", line)
            if m and m.group(1) != "0":
                findings.append(
                    f"{SCRIPT.relative_to(ROOT)}:{lineno}: `exit {m.group(1)}` -- this hook must fail gracefully "
                    "(exit 0 always) rather than fail the session"
                )

    if not SNIPPET.exists():
        findings.append(f"{SNIPPET.relative_to(ROOT)}: missing")
    else:
        try:
            data = json.loads(SNIPPET.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            findings.append(f"{SNIPPET.relative_to(ROOT)}: not valid JSON ({e})")
            data = None

        if data is not None:
            try:
                entries = data["hooks"]["SessionStart"]
            except (KeyError, TypeError):
                findings.append(f"{SNIPPET.relative_to(ROOT)}: no hooks.SessionStart array")
                entries = []

            for entry in entries:
                for hook in entry.get("hooks", []):
                    command = hook.get("command", "")
                    if "$HOME" in command or command.startswith("~"):
                        findings.append(
                            f"{SNIPPET.relative_to(ROOT)}: hook command references $HOME ({command!r}) -- "
                            "must live in the consuming project's own tracked tree instead"
                        )
                    if hook.get("async") is True:
                        findings.append(
                            f"{SNIPPET.relative_to(ROOT)}: hook entry sets \"async\": true -- "
                            "this bootstrap must run synchronously"
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
