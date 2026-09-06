#!/bin/bash
# Two-direction test for check_my_identity_is_not_private.py:
#   1. plant each protected term in a blocklist -- require the check to fire;
#   2. a genuinely private term in the same file -- require silence;
#   3. the real, current repo -- require the check to stay clean.
#
# NOTE: cases 1 and 2 clone the repo, so they test the COMMITTED check.
# Commit your change before expecting a local edit to show up here.
set -euo pipefail
cd "$(dirname "$0")/../../.."
ROOT="$(pwd)"

for term in "Morgan F" "themorgan" "Buenos Aires" "America/Argentina/Buenos_Aires"; do
  SCRATCH="$(mktemp -d)"
  (
    set -e
    git clone -q "$ROOT" "$SCRATCH"
    cd "$SCRATCH"
    printf '\\b%s\\b\n' "$term" >> leak-blocklist.txt
    git add -A
    git -c user.name=T -c user.email=t@e commit -q -m "planted: $term"
    if python3 tools/checks/check_my_identity_is_not_private.py > /dev/null; then
      echo "FAIL: did not fire on a blocklist listing '$term'" >&2
      exit 1
    fi
  )
  status=$?
  rm -rf "$SCRATCH"
  [ "$status" -eq 0 ] || exit "$status"
  echo "ok: fires on '$term'"
done

# A term that IS private must still be listable without complaint.
SCRATCH2="$(mktemp -d)"
(
  set -e
  git clone -q "$ROOT" "$SCRATCH2"
  cd "$SCRATCH2"
  printf '\\bAcmeCorp-Project-Redacted\\b\n' >> leak-blocklist.txt
  git add -A
  git -c user.name=T -c user.email=t@e commit -q -m "planted: a genuinely private term"
  if ! python3 tools/checks/check_my_identity_is_not_private.py > /dev/null; then
    echo "FAIL: fired on a genuinely private term" >&2
    exit 1
  fi
)
status=$?
rm -rf "$SCRATCH2"
[ "$status" -eq 0 ] || exit "$status"
echo "ok: silent on a genuinely private term"

if ! python3 tools/checks/check_my_identity_is_not_private.py > /dev/null; then
  echo "FAIL: not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
