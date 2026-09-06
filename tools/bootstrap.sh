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

# Team practice source (precedent.json's "team" source: a sibling clone at
# ../precedent-team-maintainers). If it's already there, fast-forward pull
# it. If it isn't, clone it.
#
# The URL below is hardcoded, deliberately, after an earlier version of
# this script hardcoded it, got reverted, and was then put back --
# Morgan's own call, made with the tradeoff explicit: precedent.json's
# schema only ever records {level, name, path} for a source, never a git
# remote URL, so nothing here is DERIVED from precedent.json -- this is
# WorkingWithAI's own script stating WorkingWithAI's own currently-real
# fact, the same way precedent-individual's own bootstrap script hardcodes
# ITS OWN url (bootstrap/session-start.sh in that repo) rather than
# inferring it from anything. The coupling this creates: if precedent.json's
# team source is EVER repointed at a different repo, this URL has to be
# updated by hand to match -- it will not follow automatically, and
# nothing here checks that they still agree. That's a real cost, accepted
# knowingly rather than by accident.
TEAM_CLONE="../precedent-team-maintainers"
TEAM_REPO_URL="https://github.com/themorgan/precedent-team-maintainers.git"
if [ -d "$TEAM_CLONE/.git" ]; then
  git -C "$TEAM_CLONE" pull --ff-only --quiet 2>/dev/null || true
elif ! git clone --quiet "$TEAM_REPO_URL" "$TEAM_CLONE" 2>/dev/null; then
  # Fail gracefully (precedent-team-maintainers/practices/fail-gracefully.md):
  # most likely this environment doesn't have read access to that repo yet
  # (a fresh Claude Code Remote/Cloud session -- see AGENTS.md's
  # "Build-environment gotchas" for the add_repo step that fixes it) rather
  # than the URL itself being wrong. Never block the session over this.
  echo "NOTE: could not clone $TEAM_REPO_URL to $TEAM_CLONE -- this environment may not have read access to it yet. Team practices are not in force via precedent.json until it's present. See AGENTS.md's 'Build-environment gotchas'." >&2
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

# Repair a single-branch clone's refspec before anything tries to fetch.
# A repository attached mid-session (Claude Code's `add_repo`, and any
# `git clone --single-branch`) is handed exactly one refspec --
# `+refs/heads/main:refs/remotes/origin/main`. Push a feature branch from
# such a clone and the push genuinely succeeds, but no `origin/<branch>`
# ref is ever written, so every later `git rev-list origin/<branch>..HEAD`
# fails to resolve and the branch reads as "unpushed, no remote
# counterpart" forever -- including to a Stop hook that then blocks the
# turn. Seen 2026-09-06 on two consumer repos whose work was already
# safely on GitHub; the honest-looking remedy (push again) changes
# nothing, because the push was never the problem.
#
# Widening the refspec is local config only: it adds no commits, moves no
# refs, and re-running it is a no-op. Doing it here means the freshness
# block below can actually resolve origin/<branch> on a feature branch,
# which on a single-branch clone it silently could not.
if git rev-parse --git-dir >/dev/null 2>&1; then
  if ! git config --get-all remote.origin.fetch 2>/dev/null | grep -q 'refs/heads/\*'; then
    git config --add remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*' 2>/dev/null && \
      echo "NOTE: this clone fetched only one branch; widened remote.origin.fetch so other branches resolve. (See AGENTS.md gotchas: a single-branch clone makes every other branch read as 'unpushed' forever.)" >&2
  fi
fi
