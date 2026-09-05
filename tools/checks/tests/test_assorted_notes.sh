#!/bin/bash
# Two-direction test for check_assorted_notes.py:
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
mkdir -p content
echo "whatever is on my mind" > content/ASSORTED_NOTES.md
mkdir -p docs
echo "See [the notes](../content/ASSORTED_NOTES.md) for why." > docs/planted-reference.md
git add content/ASSORTED_NOTES.md docs/planted-reference.md
git commit -q -m "planted violation: a doc links to ASSORTED_NOTES.md"

if python3 tools/checks/check_assorted_notes.py > /dev/null; then
  echo "FAIL: check_assorted_notes.py did not fire on a planted reference" >&2
  exit 1
fi
echo "ok: fires on planted violation"

cd "$ROOT"
if ! python3 tools/checks/check_assorted_notes.py > /dev/null; then
  echo "FAIL: check_assorted_notes.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
