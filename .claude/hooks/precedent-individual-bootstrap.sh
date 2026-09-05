#!/bin/bash
# <!-- Last updated: 2026-08-31 21:10:00 (Buenos Aires) by Morgan F, to version 1 -->
#
# SessionStart hook: makes precedent-individual resolvable with zero manual
# steps in a Claude Code on the web session. Runs before the session's first
# tool call (synchronous -- see the note below on why), clones or updates
# this repo to a fixed local path, and writes the user-level config that
# tools/precedent_resolve.py (in a Precedent checkout) reads on every
# resolve. Nobody -- dev or not -- ever runs a command by hand for this.
#
# Only runs remotely (Claude Code on the web); a normal machine already has
# a persistent home directory, so this would be a no-op there anyway.
#
# WHY SYNCHRONOUS, NOT ASYNC: if the individual source isn't ready before
# the session's first tool call, an early precedent_resolve.py run degrades
# gracefully (silently missing the individual set) rather than failing --
# which is the right behavior for a resolve, but the wrong behavior for a
# session that should have had the individual set the whole time. Running
# this synchronously removes the race entirely. The clone is small and
# fast, so the added session-start latency is minor.
#
# WHY THIS DOESN'T HALT THE SESSION ON FAILURE: fail-gracefully
# (precedent-team-maintainers/practices/fail-gracefully.md) -- if this
# environment can't reach precedent-individual (no credential, no network),
# say so on stderr and exit 0. precedent_resolve.py already knows how to
# report "individual source not available" cleanly; a hook that hard-fails
# the whole session over a missing personal-preference layer would be a
# worse failure than the one it's trying to prevent.

set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

CFG="$HOME/.config/precedent/config.json"
CLONE="$HOME/precedent-individual"
REPO_URL="https://github.com/themorgan/precedent-individual.git"

if [ -d "$CLONE/.git" ]; then
  git -C "$CLONE" pull --ff-only --quiet 2>/dev/null || true
else
  if ! git clone --quiet "$REPO_URL" "$CLONE" 2>/dev/null; then
    echo "precedent-individual bootstrap: could not clone $REPO_URL -- this environment may not have read access to it. Individual practices will not be in force this session; team and universal still resolve normally." >&2
    exit 0
  fi
fi

mkdir -p "$(dirname "$CFG")"
cat > "$CFG" <<JSON
{
  "format_version": 1,
  "individual": {"name": "precedent-individual", "path": "$CLONE"}
}
JSON
