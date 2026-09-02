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
# detection is automated -- one ls-remote, silent when current or offline;
# TAKING an update stays deliberate (INSTALL.md Sec.2) because installs are
# adaptive and unattended mirrors are the mechanism class that loses
# content.
#
# PAUSED during the precedent-beta-v01 beta test (process/manifest.json's
# _note, process/PRECEDENT_MIGRATION.md): `checkin.py fresh` compares
# process/manifest.json's recorded commit against the remote's DEFAULT
# branch HEAD (main) unconditionally -- it has no way to track a named
# non-default branch. Since this repo deliberately vendors
# precedent-beta-v01, not main, right now, that comparison would print a
# false "upstream has moved" notice every single session for as long as the
# beta lasts. Re-enable this block once precedent-beta-v01 merges to main
# and process/manifest.json is repointed at the default branch:
#
#   BESTPRACTICE_NOTICE="$(python3 process/upstream/tools/checkin.py fresh 2>/dev/null)" || BESTPRACTICE_NOTICE=""
#   if [ -n "$BESTPRACTICE_NOTICE" ]; then
#     echo "$BESTPRACTICE_NOTICE"
#   fi
echo "NOTE: BestPractice freshness check is paused -- this repo tracks alex137/BestPractice@precedent-beta-v01 (a beta branch), not its default branch. See process/manifest.json and process/PRECEDENT_MIGRATION.md."

# Team practice source freshness (precedent.json's "team" source): best
# effort, fail gracefully (precedent-team-maintainers/practices/fail-
# gracefully.md) -- a fast-forward pull of the sibling clone
# precedent_resolve.py reads live. Silent when already current or when the
# sibling clone isn't present in this environment (a fresh container
# without that repo attached); never blocks the session.
if [ -d "../precedent-team-maintainers/.git" ]; then
  git -C ../precedent-team-maintainers pull --ff-only --quiet 2>/dev/null || true
fi

# Personal pack (RepoPersonalPreferences) commit-identity setup was retired
# 2026-09-02 along with process/personal/ -- that fact now lives in
# precedent-individual's own `commit-author` practice, resolved live rather
# than hardcoded here. Until this repo's session-start tooling resolves and
# prints on-demand individual/team practices automatically (a phase-6 gap --
# see process/PRECEDENT_MIGRATION.md), the identity this repo has used since
# its BestPractice install is set directly, matching that practice's Rule:
git config user.name "Morgan F"
git config user.email "morgan@westegg.com"

# Voice guidelines session-start freshness notice (AGENTS.md's "Voice"
# section): same shape as the two notices above, for
# process/voice/HUMAN_VOICE_RULES.md against its source,
# SoundHuman.
python3 process/voice/tools/voice_sync.py fresh 2>/dev/null || true
