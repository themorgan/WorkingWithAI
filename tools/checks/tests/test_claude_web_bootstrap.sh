#!/bin/bash
# Two-direction test for check_claude_web_bootstrap.py, one case per
# structural invariant it checks:
#   A. session-start.sh loses its tracked executable bit;
#   B. session-start.sh gains a hard `exit 1`;
#   C. the settings snippet's hook command references $HOME;
#   D. the settings snippet's hook entry sets "async": true.
# Plus, on a repo standing in for a CONSUMING project (no bootstrap/ dir --
# that's this repo's own publishing path, never a consumer's):
#   E. a working consumer install (.claude/hooks/*.sh wired into
#      .claude/settings.json, synchronous, fails gracefully) must NOT be
#      flagged (real incident: this check assumed every repo it ran in was
#      precedent-individual itself and flagged every consuming project for
#      lacking bootstrap/session-start.sh and bootstrap/settings.snippet.json);
#   F. no consumer install attempt at all is still a real violation.
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

run_clean_case() {
  local label="$1"
  local mutate="$2"
  local scratch
  scratch="$(mktemp -d)"
  git clone -q "$ROOT" "$scratch"
  (
    cd "$scratch"
    eval "$mutate"
    if ! python3 tools/checks/check_claude_web_bootstrap.py > /dev/null; then
      echo "FAIL: check_claude_web_bootstrap.py fired on a non-violation: $label (false positive)" >&2
      exit 1
    fi
    echo "ok: stays clean on planted non-violation ($label)"
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

run_clean_case "working consumer install (no bootstrap/ dir at all)" '
git rm -q -r bootstrap
mkdir -p .claude/hooks
cat > .claude/hooks/precedent-individual-bootstrap.sh <<EOF
#!/bin/bash
set -uo pipefail
CFG="\$HOME/.config/precedent/config.json"
CLONE="\$HOME/precedent-individual"
if [ -d "\$CLONE/.git" ]; then
  git -C "\$CLONE" pull --ff-only --quiet 2>/dev/null || true
else
  if ! git clone --quiet https://github.com/themorgan/precedent-individual.git "\$CLONE" 2>/dev/null; then
    exit 0
  fi
fi
mkdir -p "\$(dirname "\$CFG")"
echo "{}" > "\$CFG"
EOF
chmod +x .claude/hooks/precedent-individual-bootstrap.sh
cat > .claude/settings.json <<EOF
{
  "hooks": {
    "SessionStart": [
      {"hooks": [{"type": "command", "command": "\$CLAUDE_PROJECT_DIR/.claude/hooks/precedent-individual-bootstrap.sh"}]}
    ]
  }
}
EOF
git add .claude/hooks/precedent-individual-bootstrap.sh .claude/settings.json
'

run_case "no consumer install and no bootstrap/ dir (real violation)" '
git rm -q -r bootstrap
'

if ! python3 tools/checks/check_claude_web_bootstrap.py > /dev/null; then
  echo "FAIL: check_claude_web_bootstrap.py is not clean on the real, current repo" >&2
  exit 1
fi
echo "ok: clean on real content"
