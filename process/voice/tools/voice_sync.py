#!/usr/bin/env python3
"""voice_sync.py — keep process/voice/HUMAN_VOICE_RULES.md current with its source repo.

Sibling to process/personal/tools/pack_sync.py, same shape, for a different
manifest (process/manifest_voice.json) and source
(https://github.com/themorgan/VoiceGuidelinesToSoundHuman, private). One
real difference from pack_sync.py: that source repo has no process/ tree of
its own — HUMAN_VOICE_RULES.md sits at its repo root — so this tracks a
single FILE, not a subtree. "Take an update" and "record what was taken"
are one step, same as the personal pack: this is a one-way dependency, no
check-in loop back to the source.

  fresh                       Session-start staleness notice: one
                              `git ls-remote` of the manifest's upstream
                              repo (private — silently skipped if the
                              ambient git credentials can't reach it),
                              compared to the recorded upstream.commit.
                              Prints one line only when it's moved; always
                              exits 0 (a notice, never a gate).

  status <clone>              Compare process/voice/HUMAN_VOICE_RULES.md
                              against <clone>/HUMAN_VOICE_RULES.md. Exit 1
                              if they differ.

  update <clone> [--force]    Pull the clone's default branch, copy its
                              HUMAN_VOICE_RULES.md over this repo's own,
                              then record the clone's HEAD as the new
                              upstream.commit. REFUSES if the local file
                              differs from what upstream.commit last
                              recorded — that difference is local drift the
                              mirror would silently clobber; reconcile it by
                              hand first, or pass --force to overwrite.

Run:  python3 process/voice/tools/voice_sync.py fresh
      python3 process/voice/tools/voice_sync.py status ../SoundHuman
      python3 process/voice/tools/voice_sync.py update ../SoundHuman
"""
import filecmp, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve()
_top = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=HERE.parent,
                      capture_output=True, text=True).stdout.strip()
ROOT = pathlib.Path(_top) if _top else HERE.parents[3]
FILENAME = 'HUMAN_VOICE_RULES.md'
LOCAL = ROOT / 'process' / 'voice' / FILENAME
MANIFEST = ROOT / 'process' / 'manifest_voice.json'


def _git(clone, *args):
    return subprocess.run(['git', '-C', str(clone)] + list(args),
                          capture_output=True, text=True).stdout.strip()


def _manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))


def _clone_or_die(arg):
    clone = pathlib.Path(arg).resolve()
    if not (clone / '.git').exists():
        sys.exit(f"voice_sync FAIL: {clone} is not a git clone")
    return clone


def fresh():
    """Session-start staleness notice: automated detection, deliberate take."""
    try:
        up = _manifest().get('upstream', {})
        repo, recorded = up.get('repo'), up.get('commit')
        if not repo or not recorded:
            return 0
        out = subprocess.run(['git', 'ls-remote', repo, 'HEAD'],
                             capture_output=True, text=True, timeout=10)
        head = out.stdout.split()[0] if out.returncode == 0 and out.stdout else ''
        if head and head != recorded:
            print(f"NOTICE: the voice guidelines' source has moved ({head[:12]}; your base "
                  f"{recorded[:12]}) — review at the next session "
                  f"(AGENTS.md 'Voice' section).")
    except Exception:
        pass
    return 0


def _default_branch(clone):
    return (_git(clone, 'symbolic-ref', '--short', 'refs/remotes/origin/HEAD').rsplit('/', 1)[-1]
            or 'main')


def status(clone):
    branch = _default_branch(clone)
    theirs = clone / FILENAME
    differ = not theirs.exists() or not filecmp.cmp(LOCAL, theirs, shallow=False)
    recorded = _manifest().get('upstream', {}).get('commit')
    head = _git(clone, 'rev-parse', 'HEAD')
    print(f"{'M' if differ else '='} {FILENAME}")
    print(f"voice file vs clone ({branch}): {'differs' if differ else 'identical'}")
    print(f"manifest upstream.commit: {recorded}")
    print(f"clone HEAD:               {head}"
          + ("  (== recorded)" if head == recorded else "  (!= recorded)"))
    return 1 if differ else 0


def update(clone, force=False):
    branch = _default_branch(clone)
    _git(clone, 'checkout', branch)
    _git(clone, 'pull', 'origin', branch)
    if not force:
        recorded = _manifest().get('upstream', {}).get('commit')
        if not recorded:
            sys.exit("voice_sync FAIL: no upstream.commit recorded in the manifest — "
                     "cannot tell local drift from upstream movement; pass --force to mirror anyway")
        show = subprocess.run(['git', '-C', str(clone), 'show', f'{recorded}:{FILENAME}'],
                              capture_output=True)
        if show.returncode != 0:
            sys.exit(f"voice_sync FAIL: recorded commit {recorded[:12]} (or {FILENAME} within it) "
                     f"not found in the clone — fetch it there, or pass --force")
        if show.stdout != LOCAL.read_bytes():
            sys.exit("voice_sync FAIL: process/voice/HUMAN_VOICE_RULES.md differs from the "
                     "recorded upstream commit's version — that is local drift the mirror would "
                     "clobber. Reconcile it by hand first, or pass --force to overwrite. (This "
                     "file should never be hand-edited here in the first place — see AGENTS.md's "
                     "merge runbook.)")
    theirs = clone / FILENAME
    head = _git(clone, 'rev-parse', 'HEAD')
    if filecmp.cmp(LOCAL, theirs, shallow=False):
        print(f"voice_sync update: {FILENAME} already identical to clone {branch} — nothing to mirror.")
    else:
        LOCAL.write_bytes(theirs.read_bytes())
        print(f"voice_sync update OK: mirrored {FILENAME} from clone {branch} @ {head[:12]}")
    manifest = _manifest()
    old = manifest['upstream'].get('commit')
    manifest['upstream']['commit'] = head
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n',
                        encoding='utf-8')
    print(f"manifest upstream.commit: {old} -> {head}")
    print("next: run the gates, then commit process/voice/ and process/manifest_voice.json together.")
    return 0


def main():
    args = sys.argv[1:]
    if args and args[0] == 'fresh':
        return fresh()
    if len(args) < 2 or args[0] not in ('status', 'update'):
        sys.exit(__doc__)
    clone = _clone_or_die(args[1])
    if args[0] == 'status':
        return status(clone)
    return update(clone, force='--force' in args)


if __name__ == '__main__':
    sys.exit(main())
