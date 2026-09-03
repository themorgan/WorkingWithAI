#!/bin/bash
# Two-direction test for check_claude_web_bootstrap.py, one case per
# structural invariant it checks:
#   A. session-start.sh loses its tracked executable bit;
#   B. session-start.sh gains a hard `exit 1`;
#   C. the settings snippet's hook command references $HOME;
#   D. the settings snippet's hook entry sets "async": true.
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
    eval "$mutate"
    if python3 tools/checks/check_claude_web_bootstrap.py > /dev/null; then
      echo "FAIL: check_claude_web_bootstrap.py did not fire on: $label" >&2
      exit 1
    fi
    echo "ok: fires on planted violation ($label)"
  )
  local status=$?
  rm -rf "$scratch"
  return $status
}

run_case "executable bit dropped" '
chmod -x bootstrap/session-start.sh
git add bootstrap/session-start.sh
'

run_case "hard exit 1 introduced" '
sed -i "s/exit 0\$/exit 1/" bootstrap/session-start.sh
'

run_case "\$HOME reference in hook command" '
python3 - <<PY
import json, pathlib
p = pathlib.Path("bootstrap/settings.snippet.json")
d = json.loads(p.read_text())
d["hooks"]["SessionStart"][0]["hooks"][0]["command"] = "\$HOME/precedent-individual/bootstrap/session-start.sh"
p.write_text(json.dumps(d, indent=2))
PY
'

run_case "async: true set" '
python3 - <<PY
import json, pathlib
p = pathlib.Path("bootstrap/settings.snippet.json")
d = json.loads(p.read_text())
d["hooks"]["SessionStart"][0]["hooks"][0]["async"] = True
p.write_text(json.dumps(d, indent=2))
PY
'

if ! python3 tools/checks/check_claude_web_bootstrap.py > /dev/null; then
  echo "FAIL: check_claude_web_bootstrap.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
