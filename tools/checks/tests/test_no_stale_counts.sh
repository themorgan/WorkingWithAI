#!/bin/bash
# Two-direction test for check_no_stale_counts.py:
#   1. plant a wrong "<N> practices" count in a tracked markdown file --
#      require the check to fire;
#   2. the real, current, unplanted repo -- require the check to stay clean.
set -euo pipefail
cd "$(dirname "$0")/../../.."
ROOT="$(pwd)"
SCRATCH="$(mktemp -d)"
trap 'rm -rf "$SCRATCH"' EXIT

git clone -q "$ROOT" "$SCRATCH"
cd "$SCRATCH"
echo "" >> README.md
echo "This set has 999 practices, definitely not the real count." >> README.md
git add README.md
git -c user.name="Test" -c user.email="test@example.com" commit -q -m "planted violation: wrong practice count"

if python3 tools/checks/check_no_stale_counts.py > /dev/null; then
  echo "FAIL: check_no_stale_counts.py did not fire on a planted wrong count" >&2
  exit 1
fi
echo "ok: fires on planted violation"

# 3. the same planted count, but inside a tree this repo VENDORED rather
#    than wrote -- require silence. A consuming repo cannot fix a number in
#    somebody else's document, and 81 such findings is what made this check
#    unreadable in a real four-source install (2026-09-06).
cd "$SCRATCH"
git reset -q --hard HEAD~1          # undo case 1's planted count first
mkdir -p process/upstream
cat > precedent.json <<'JSON'
{"format_version": 1, "sources": [{"level": "universal", "name": "u", "path": "process/upstream"}]}
JSON
echo "Their set has 999 practices, and that is their business." > process/upstream/THEIRS.md
git add precedent.json process/upstream/THEIRS.md
git -c user.name="Test" -c user.email="test@example.com" commit -q -m "vendored tree with its own count"

if ! python3 tools/checks/check_no_stale_counts.py > /dev/null; then
  echo "FAIL: fired on a count inside a vendored source tree the repo did not write" >&2
  exit 1
fi
echo "ok: silent on vendored content"

# 4. and still fires on the repo's OWN file in the same working tree, so
#    case 3 cannot be satisfied by a check that simply stopped running.
echo "This set has 999 practices, definitely not the real count." >> README.md
git add README.md
git -c user.name="Test" -c user.email="test@example.com" commit -q -m "planted violation beside the vendored tree"
if python3 tools/checks/check_no_stale_counts.py > /dev/null; then
  echo "FAIL: went silent everywhere, not just on vendored content" >&2
  exit 1
fi
echo "ok: still fires on this repo's own content"

cd "$ROOT"
if ! python3 tools/checks/check_no_stale_counts.py > /dev/null; then
  echo "FAIL: check_no_stale_counts.py is not clean on the real, current repo (including its own 40-practices line)" >&2
  exit 1
fi
echo "ok: clean on real content"
