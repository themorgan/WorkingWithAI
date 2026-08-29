#!/bin/bash
# Bootstrap (BestPractice practice 13) — environment setup as code,
# harness-neutral. Wired by templates/harness/*/ so every supported agent
# runs this at session start; the rest fall back to the instructions file's
# directive to run it manually.
set -euo pipefail

# Python deps the repo's scripts import (cmarkgfm is doc_lint's exact
# GitHub-renderer check; pyyaml is light_check's YAML-syntax check):
pip install --quiet cmarkgfm pyyaml 2>/dev/null || \
  echo "WARN: pip install failed - doc_lint strikethrough check and light_check YAML check will be skipped" >&2

# BestPractice upstream freshness notice (see PRACTICES.md practice 13) and
# the personal pack's own sibling check
# (process/personal/README.md#drift-notice): detection is automated -- one
# ls-remote each, silent when current or offline; TAKING an update stays
# deliberate (INSTALL.md §2) because installs are adaptive and unattended
# mirrors are the mechanism class that loses content. Each is wrapped to
# also persist a fired notice into TODO.md's "## Pending drift reviews"
# section, not just print it -- a stdout-only notice can lose a priority
# fight against whatever task is already in front of a session (origin: a
# dependent repo, 2026-08-27 -- real name kept out of anything vendored,
# per process/personal/README.md#private-repo-scrub).
BESTPRACTICE_NOTICE="$(python3 process/upstream/tools/checkin.py fresh 2>/dev/null)" || BESTPRACTICE_NOTICE=""
if [ -n "$BESTPRACTICE_NOTICE" ]; then
  echo "$BESTPRACTICE_NOTICE"
  python3 process/personal/tools/pack_sync.py record bestpractice "$BESTPRACTICE_NOTICE" 2>/dev/null || true
fi

# Personal pack (process/personal/README.md#commit-author and
# process/personal/README.md#install step 4): commit author identity,
# every session, idempotent.
git config user.name "Morgan F"
git config user.email "morgan@westegg.com"

PACK_NOTICE="$(python3 process/personal/tools/pack_sync.py fresh 2>/dev/null)" || PACK_NOTICE=""
if [ -n "$PACK_NOTICE" ]; then
  echo "$PACK_NOTICE"
  python3 process/personal/tools/pack_sync.py record personal-pack "$PACK_NOTICE" 2>/dev/null || true
fi

# Voice guidelines session-start freshness notice (AGENTS.md's "Voice"
# section): same shape as the two notices above, for
# process/voice/HUMAN_VOICE_RULES.md against its source,
# SoundHuman.
python3 process/voice/tools/voice_sync.py fresh 2>/dev/null || true
