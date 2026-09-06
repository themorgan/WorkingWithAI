#!/bin/bash
# Two-direction test for check_file_header.py, both planted violations it's
# meant to catch:
#   A. content changed but the version wasn't bumped;
#   B. the header line is malformed.
# Plus a planted NON-violation it must NOT catch:
#   C. vendored third-party content with its own, different, complete
#      attribution convention that happens to start "<!-- Last updated:"
#      too -- not this practice's business (real incident: this check used
#      to flag every such file as a malformed attempt at Morgan's header).
# Then: the real, current, unplanted repo must stay clean.
set -euo pipefail
cd "$(dirname "$0")/../../.."
ROOT="$(pwd)"

run_case() {
  local label="$1"
  local mutate="$2"
  local scratch
  scratch="$(mktemp -d)"
  git clone -q "$ROOT" "$scratch"
  (
    cd "$scratch"
    git config user.name "Morgan F"
    git config user.email "morgan@westegg.com"
    eval "$mutate"
    TZ="America/Argentina/Buenos_Aires" git commit -q -am "planted violation: $label"
    if python3 tools/checks/check_file_header.py > /dev/null; then
      echo "FAIL: check_file_header.py did not fire on: $label" >&2
      exit 1
    fi
    echo "ok: fires on planted violation ($label)"
  )
  local status=$?
  rm -rf "$scratch"
  return $status
}

run_clean_case() {
  local label="$1"
  local mutate="$2"
  local scratch
  scratch="$(mktemp -d)"
  git clone -q "$ROOT" "$scratch"
  (
    cd "$scratch"
    git config user.name "Morgan F"
    git config user.email "morgan@westegg.com"
    eval "$mutate"
    TZ="America/Argentina/Buenos_Aires" git commit -q -am "planted non-violation: $label"
    if ! python3 tools/checks/check_file_header.py > /dev/null; then
      echo "FAIL: check_file_header.py fired on a non-violation: $label (false positive)" >&2
      exit 1
    fi
    echo "ok: stays clean on planted non-violation ($label)"
  )
  local status=$?
  rm -rf "$scratch"
  return $status
}

run_case "content changed, version not bumped" '
python3 - <<PY
import pathlib
p = pathlib.Path("README.md")
lines = p.read_text().splitlines()
lines.append("Planted content change without a version bump.")
p.write_text("\n".join(lines) + "\n")
PY
'

run_case "malformed header line" '
python3 - <<PY
import pathlib
p = pathlib.Path("README.md")
lines = p.read_text().splitlines()
lines[0] = "<!-- Last updated: 2026-08-31 by Morgan F, to version 2 -->"
p.write_text("\n".join(lines) + "\n")
PY
'

run_clean_case "vendored file with its own, different, complete attribution" '
mkdir -p vendor
cat > vendor/THIRD_PARTY.md <<EOF
<!-- Last updated: 2026-01-01 10:00:00 (Some Other Zone) by Someone Else, to version 1 -->

Vendored content with its own header convention, not Morgan'"'"'s.
EOF
git add vendor/THIRD_PARTY.md
'

if ! python3 tools/checks/check_file_header.py > /dev/null; then
  echo "FAIL: check_file_header.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
