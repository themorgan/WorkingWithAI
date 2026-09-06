#!/bin/bash
# Two-direction test for check_assorted_notes.py:
#   1. plant the exact violation in a scratch copy -- require the check to fire;
#   2. plant a NON-violation -- a link to a filename that merely ENDS the
#      same way (MARKETING_IDEAS.md, RANDOM_NOTES.md) -- require the check
#      to stay clean (real incident: a substring match on the link target
#      flagged these purely for ending in IDEAS.md/NOTES.md);
#   3. plant a listing-document link -- a README.md and a MAP.md, each
#      linking to ASSORTED_NOTES.md -- require the check to stay clean
#      (the 2026-09-05 revision's whole point: a directory listing may
#      link to it; only a citation of its content may not);
#   4. plant a "## See also" link to ASSORTED_NOTES.md in an ordinary
#      page, alongside an ordinary (non-exempt) link to it earlier in
#      the same file -- require the check to fire on the ordinary link
#      but not on the See also one;
#   5. the real, current, unplanted repo -- require the check to stay clean.
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
SCRATCH2="$(mktemp -d)"
git clone -q "$ROOT" "$SCRATCH2"
(
  cd "$SCRATCH2"
  git config user.name "Morgan F"
  git config user.email "morgan@westegg.com"
  mkdir -p content
  echo "marketing copy" > content/MARKETING_IDEAS.md
  echo "loose thoughts" > content/RANDOM_NOTES.md
  mkdir -p docs
  cat > docs/planted-non-reference.md <<'EOF'
Real links, to real files that just happen to end the same way:
[marketing](../content/MARKETING_IDEAS.md) and [notes](../content/RANDOM_NOTES.md).
EOF
  git add content/MARKETING_IDEAS.md content/RANDOM_NOTES.md docs/planted-non-reference.md
  git commit -q -m "planted non-violation: links to MARKETING_IDEAS.md and RANDOM_NOTES.md"
  if ! python3 tools/checks/check_assorted_notes.py > /dev/null; then
    echo "FAIL: check_assorted_notes.py fired on links to MARKETING_IDEAS.md/RANDOM_NOTES.md (false positive)" >&2
    exit 1
  fi
  echo "ok: stays clean on planted non-violation (MARKETING_IDEAS.md, RANDOM_NOTES.md)"
)
status=$?
rm -rf "$SCRATCH2"
if [ "$status" -ne 0 ]; then
  exit "$status"
fi

cd "$ROOT"
SCRATCH3="$(mktemp -d)"
git clone -q "$ROOT" "$SCRATCH3"
(
  cd "$SCRATCH3"
  git config user.name "Morgan F"
  git config user.email "morgan@westegg.com"
  mkdir -p content
  echo "whatever is on my mind" > content/ASSORTED_NOTES.md
  cat > README.md <<'EOF'
# Scratch repo

- [content/ASSORTED_NOTES.md](content/ASSORTED_NOTES.md) -- notes with no obvious home elsewhere.
EOF
  cat > MAP.md <<'EOF'
# Map

| content/ASSORTED_NOTES.md | General notes, listed here for discoverability. |
|---|---|
| [content/ASSORTED_NOTES.md](content/ASSORTED_NOTES.md) | as above |
EOF
  git add content/ASSORTED_NOTES.md README.md MAP.md
  git commit -q -m "planted non-violation: README.md and MAP.md link to ASSORTED_NOTES.md"
  if ! python3 tools/checks/check_assorted_notes.py > /dev/null; then
    echo "FAIL: check_assorted_notes.py fired on a README.md/MAP.md listing link (false positive)" >&2
    exit 1
  fi
  echo "ok: stays clean on a README.md/MAP.md listing link"
)
status=$?
rm -rf "$SCRATCH3"
if [ "$status" -ne 0 ]; then
  exit "$status"
fi

cd "$ROOT"
SCRATCH4="$(mktemp -d)"
git clone -q "$ROOT" "$SCRATCH4"
(
  cd "$SCRATCH4"
  git config user.name "Morgan F"
  git config user.email "morgan@westegg.com"
  mkdir -p content
  echo "whatever is on my mind" > content/ASSORTED_NOTES.md
  cat > docs-page.md <<'EOF'
# An ordinary page

See [the notes](content/ASSORTED_NOTES.md) for background on this claim.

## See also

- [content/ASSORTED_NOTES.md](content/ASSORTED_NOTES.md) -- related notes.
EOF
  git add content/ASSORTED_NOTES.md docs-page.md
  git commit -q -m "planted: an ordinary citation plus a See also link in one file"
  out="$(python3 tools/checks/check_assorted_notes.py || true)"
  if ! echo "$out" | grep -q "docs-page.md:3:"; then
    echo "FAIL: check_assorted_notes.py did not fire on the ordinary (non-See-also) citation" >&2
    echo "$out" >&2
    exit 1
  fi
  if echo "$out" | grep -q "docs-page.md:7:"; then
    echo "FAIL: check_assorted_notes.py fired on a See also link (false positive)" >&2
    echo "$out" >&2
    exit 1
  fi
  echo "ok: fires on the ordinary citation, not on the See also link, in the same file"
)
status=$?
rm -rf "$SCRATCH4"
if [ "$status" -ne 0 ]; then
  exit "$status"
fi

# Once content/ASSORTED_NOTES.md exists the consolidation this practice
# describes has happened, and a legacy NAME is just a filename again. A repo
# with a real ASSORTED_NOTES.md was flagged for linking book-moses/NOTES.md,
# a manuscript brainstorm that is not its catch-all (2026-09-06).
SCRATCH5="$(mktemp -d)"
(
  set -e
  git clone -q "$ROOT" "$SCRATCH5"
  cd "$SCRATCH5"
  mkdir -p content book-moses
  echo "# Assorted notes" > content/ASSORTED_NOTES.md
  echo "# Moses notes" > book-moses/NOTES.md
  echo "See [the Moses notes](book-moses/NOTES.md) for that draft." > TODO.md
  git add -A
  git -c user.name="Test" -c user.email="test@example.com" commit -q -m "migrated repo, unrelated NOTES.md"
  if ! python3 tools/checks/check_assorted_notes.py > /dev/null; then
    echo "FAIL: fired on a legacy-named file in a repo that already has content/ASSORTED_NOTES.md" >&2
    exit 1
  fi
  echo "ok: legacy names stop counting once the migration is done"

  # ...and the canonical file is still guarded in that same repo, so the
  # case above cannot be met by a check that simply stopped running.
  echo "Per [the notes](content/ASSORTED_NOTES.md), we should ship it." > TODO.md
  git add -A
  git -c user.name="Test" -c user.email="test@example.com" commit -q -m "citation of the real notes file"
  if python3 tools/checks/check_assorted_notes.py > /dev/null; then
    echo "FAIL: stopped guarding content/ASSORTED_NOTES.md itself" >&2
    exit 1
  fi
  echo "ok: still fires on a citation of the canonical notes file"
)
status=$?
rm -rf "$SCRATCH5"
if [ "$status" -ne 0 ]; then
  exit "$status"
fi

if ! python3 tools/checks/check_assorted_notes.py > /dev/null; then
  echo "FAIL: check_assorted_notes.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
