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

# BestPractice upstream freshness notice (see PRACTICES.md practice 13):
# detection is automated -- one ls-remote against the public upstream,
# silent when current or offline; TAKING the update stays deliberate
# (INSTALL.md sec.2) because installs are adaptive and unattended mirrors
# are the mechanism class that loses content.
python3 process/upstream/tools/checkin.py fresh 2>/dev/null || true

# Personal pack (process/personal/README.md §3 and §18 step 4): commit
# author identity, every session, idempotent.
git config user.name "Morgan F"
git config user.email "morgan@westegg.com"

# Personal pack session-start freshness notice (process/personal/README.md
# §16 and §18 step 4): cheap, non-blocking, notice only -- never takes the
# update itself.
python3 process/personal/tools/pack_sync.py fresh 2>/dev/null || true

# Voice guidelines session-start freshness notice (AGENTS.md's "Voice"
# section): same shape as the two notices above, for
# process/voice/HUMAN_VOICE_RULES.md against its source,
# SoundHuman.
python3 process/voice/tools/voice_sync.py fresh 2>/dev/null || true
