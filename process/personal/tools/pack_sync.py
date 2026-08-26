#!/usr/bin/env python3
"""pack_sync.py — keep process/personal/ current with its source repo.

Sibling to process/upstream/tools/checkin.py, but for the personal pack
(process/manifest_personal.json) instead of BestPractice
(process/manifest.json), and simpler: the personal pack is a ONE-WAY
dependency. Its canonical tree lives at process/personal/ inside
RepoPersonalPreferences (the manifest's upstream.repo) — a dependent repo
only ever takes updates from there, it never proposes local pack changes
back (there is no check-in loop for this layer, unlike BestPractice's
INSTALL.md §4). So "take an update" and "record what was taken" are one
step here, not checkin.py's separate update/record two-phase cycle.

The source tree lives at process/personal/ *inside* the source repo too
(same relative path both sides — SUBTREE below) because RepoPersonalPreferences
is not a single-purpose pack repo; it also carries its own BestPractice
install alongside the pack. checkin.py's UPSTREAM constant assumes the
whole clone root is the vendored tree; this diffs one subtree of the clone
instead — the reason this couldn't just be `checkin.py --manifest ...`.

  fresh                       Session-start staleness notice: one
                              `git ls-remote` of the manifest's upstream
                              repo (RepoPersonalPreferences, private —
                              silently skipped if the ambient git
                              credentials can't reach it), compared to the
                              recorded upstream.commit. Prints one line only
                              when the pack has moved; always exits 0 (a
                              notice, never a gate).

  status <clone>              Compare process/personal/ against
                              <clone>/process/personal/: list
                              Added/Modified/Deleted files, show the
                              manifest's recorded upstream.commit vs the
                              clone's HEAD. Exit 1 if the trees differ.

  update <clone> [--force]    Pull the clone's default branch, mirror its
                              process/personal/ subtree over this repo's
                              own, then record the clone's HEAD as the new
                              upstream.commit. REFUSES if the local tree
                              differs from what upstream.commit last
                              recorded — that difference is local drift the
                              mirror would silently clobber; reconcile it by
                              hand first, or pass --force to overwrite.

Run:  python3 process/personal/tools/pack_sync.py fresh
      python3 process/personal/tools/pack_sync.py status ../RepoPersonalPreferences
      python3 process/personal/tools/pack_sync.py update ../RepoPersonalPreferences
"""
import datetime, filecmp, io, json, pathlib, shutil, subprocess, sys, tarfile, tempfile

HERE = pathlib.Path(__file__).resolve()
_top = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=HERE.parent,
                      capture_output=True, text=True).stdout.strip()
ROOT = pathlib.Path(_top) if _top else HERE.parents[3]
SUBTREE = 'process/personal'
PACK = ROOT / SUBTREE
MANIFEST = ROOT / 'process' / 'manifest_personal.json'


def _git(clone, *args):
    return subprocess.run(['git', '-C', str(clone)] + list(args),
                          capture_output=True, text=True).stdout.strip()


def _files(base):
    return {p.relative_to(base) for p in base.rglob('*')
            if p.is_file() and '.git' not in p.parts}


def _diff(clone_subtree):
    """(added, modified, deleted) of the pack tree vs a clone's subtree."""
    ours, theirs = _files(PACK), _files(clone_subtree)
    added = sorted(ours - theirs)
    deleted = sorted(theirs - ours)
    modified = sorted(p for p in ours & theirs
                      if not filecmp.cmp(PACK / p, clone_subtree / p, shallow=False))
    return added, modified, deleted


def _manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))


def _clone_or_die(arg):
    clone = pathlib.Path(arg).resolve()
    if not (clone / '.git').exists():
        sys.exit(f"pack_sync FAIL: {clone} is not a git clone")
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
            print(f"NOTICE: the personal pack's source has moved ({head[:12]}; your base "
                  f"{recorded[:12]}) — review at the next session "
                  f"(process/personal/README.md sec.14).")
    except Exception:
        pass
    return 0


def _default_branch(clone):
    return (_git(clone, 'symbolic-ref', '--short', 'refs/remotes/origin/HEAD').rsplit('/', 1)[-1]
            or 'main')


def status(clone):
    branch = _default_branch(clone)
    added, modified, deleted = _diff(clone / SUBTREE)
    recorded = _manifest().get('upstream', {}).get('commit')
    head = _git(clone, 'rev-parse', 'HEAD')
    for p in added:
        print(f"  A {p}")
    for p in modified:
        print(f"  M {p}")
    for p in deleted:
        print(f"  D {p}")
    n = len(added) + len(modified) + len(deleted)
    print(f"pack vs clone ({branch}): {n} file(s) differ "
          f"({len(added)} added, {len(modified)} modified, {len(deleted)} deleted)")
    print(f"manifest upstream.commit: {recorded}")
    print(f"clone HEAD:               {head}"
          + ("  (== recorded)" if head == recorded else "  (!= recorded)"))
    return 1 if n else 0


def update(clone, force=False):
    branch = _default_branch(clone)
    _git(clone, 'checkout', branch)
    _git(clone, 'pull', 'origin', branch)
    if not force:
        recorded = _manifest().get('upstream', {}).get('commit')
        if not recorded:
            sys.exit("pack_sync FAIL: no upstream.commit recorded in the manifest — "
                     "cannot tell local drift from upstream movement; pass --force to mirror anyway")
        tar = subprocess.run(['git', '-C', str(clone), 'archive', recorded, '--', SUBTREE],
                             capture_output=True)
        if tar.returncode != 0 or not tar.stdout:
            sys.exit(f"pack_sync FAIL: recorded commit {recorded[:12]} (or {SUBTREE} within it) "
                     f"not found in the clone — fetch it there, or pass --force")
        with tempfile.TemporaryDirectory() as td:
            tarfile.open(fileobj=io.BytesIO(tar.stdout)).extractall(td)
            base = pathlib.Path(td) / SUBTREE
            ours, theirs = _files(PACK), _files(base)
            drift = sorted(ours ^ theirs) + sorted(
                p for p in ours & theirs
                if not filecmp.cmp(PACK / p, base / p, shallow=False))
        if drift:
            for p in drift:
                print(f"  local change: {p}")
            sys.exit("pack_sync FAIL: process/personal/ differs from the recorded upstream "
                     "commit — that is local drift the mirror would clobber. Reconcile it by "
                     "hand first, or pass --force to overwrite.")
    clone_subtree = clone / SUBTREE
    added, modified, deleted = _diff(clone_subtree)
    head = _git(clone, 'rev-parse', 'HEAD')
    if not (added or modified or deleted):
        print(f"pack_sync update: process/personal/ already identical to clone {branch} — "
              f"nothing to mirror.")
    else:
        for p in added + modified:
            (PACK / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(clone_subtree / p, PACK / p)
        for p in deleted:
            (PACK / p).unlink()
        print(f"pack_sync update OK: mirrored {len(added) + len(modified)} file(s), "
              f"deleted {len(deleted)} from {SUBTREE} (clone {branch} @ {head[:12]})")
    manifest = _manifest()
    old = manifest['upstream'].get('commit')
    manifest['upstream']['commit'] = head
    manifest['upstream']['_note'] = (
        f"commit = RepoPersonalPreferences hash last synced from "
        f"(recorded {datetime.date.today().isoformat()}).")
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n',
                        encoding='utf-8')
    print(f"manifest upstream.commit: {old} -> {head}")
    print("next: re-weave any changed template sections (e.g. AGENTS_ADDENDUM.md.template")
    print("      into this repo's AGENTS.md) by hand, re-run the gates, then commit")
    print("      process/personal/ and process/manifest_personal.json together.")
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
