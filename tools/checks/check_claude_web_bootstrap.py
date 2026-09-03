#!/usr/bin/env python3
"""check_claude_web_bootstrap.py -- the mechanical check for
practices/claude-web-bootstrap.md.

# practice: claude-web-bootstrap

Scope: tree. The practice's actual claim -- "every project gets this hook
installed" -- is about *other* projects' `.claude/` trees, which this repo
has no visibility into, so that half can't be checked from here (see the
practice file's own Install section). What this check verifies is that the
canonical artifacts this repo publishes for other projects to copy --
`bootstrap/session-start.sh` and `bootstrap/settings.snippet.json` -- still
satisfy the structural invariants the practice's own Detail section spells
out. Those invariants are exactly what would silently break the bootstrap
for every consuming project if they regressed:

- the script is git-tracked executable (mode 100755) and starts with a
  bash shebang;
- it never exits non-zero -- a hard failure here would fail the whole
  session over a missing personal-preference layer, which is precisely
  what "fails gracefully" means;
- the settings snippet is valid JSON, and its hook command path does not
  live under "$HOME" -- the hook that bootstraps precedent-individual
  cannot itself live somewhere only that bootstrap would create;
- the hook entry is not marked "async": true -- synchronous is the whole
  point (see the script's own header).

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


def rule_text() -> str:
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


def find_violations() -> list[str]:
    findings = []

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
