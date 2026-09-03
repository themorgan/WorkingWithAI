#!/bin/bash
# Two-direction test for check_buenos_aires_dates.py:
#   1. plant the exact violation in a scratch copy -- require the check to fire;
#   2. the real, current, unplanted repo -- require the check to stay clean.
set -euo pipefail
cd "$(dirname "$0")/../../.."
ROOT="$(pwd)"
SCRATCH="$(mktemp -d)"
trap 'rm -rf "$SCRATCH"' EXIT

git clone -q "$ROOT" "$SCRATCH"
cd "$SCRATCH"
git config user.name "Morgan F"
git config user.email "morgan@westegg.com"
touch planted-violation.txt
git add planted-violation.txt
TZ="UTC" git commit -q -m "planted violation: wrong tz offset"

if python3 tools/checks/check_buenos_aires_dates.py > /dev/null; then
  echo "FAIL: check_buenos_aires_dates.py did not fire on a planted non-Buenos-Aires commit offset" >&2
  exit 1
fi
echo "ok: fires on planted violation"

cd "$ROOT"
if ! python3 tools/checks/check_buenos_aires_dates.py > /dev/null; then
  echo "FAIL: check_buenos_aires_dates.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
