#!/bin/bash
# Two-direction test for check_commit_author.py:
#   1. plant the exact violation in a scratch copy -- require the check to fire;
#   2. the real, current, unplanted repo -- require the check to stay clean.
set -euo pipefail
cd "$(dirname "$0")/../../.."
ROOT="$(pwd)"
SCRATCH="$(mktemp -d)"
trap 'rm -rf "$SCRATCH"' EXIT

git clone -q "$ROOT" "$SCRATCH"
cd "$SCRATCH"
git config user.name "Someone Else"
git config user.email "someone@example.com"
touch planted-violation.txt
git add planted-violation.txt
GIT_AUTHOR_NAME="Someone Else" GIT_AUTHOR_EMAIL="someone@example.com" \
GIT_COMMITTER_NAME="Someone Else" GIT_COMMITTER_EMAIL="someone@example.com" \
  git commit -q -m "planted violation: wrong author"

if python3 tools/checks/check_commit_author.py > /dev/null; then
  echo "FAIL: check_commit_author.py did not fire on a planted wrong-author commit" >&2
  exit 1
fi
echo "ok: fires on planted violation"

cd "$ROOT"
if ! python3 tools/checks/check_commit_author.py > /dev/null; then
  echo "FAIL: check_commit_author.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
