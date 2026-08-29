#!/usr/bin/env python3
# Last updated: 2026-08-29 10:15:00 (Buenos Aires) by Morgan F, to version 6
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

  record <source> <notice>    Persist a freshness notice into TODO.md's
                              "## Pending Drift Reviews" section (creating
                              it if absent) instead of leaving it as a
                              stdout-only line a session can read past.
                              <source> is a short slug ("bestpractice" or
                              "personal-pack"); <notice> is the text to
                              record (typically the exact line `fresh` — or
                              process/upstream/tools/checkin.py's own
                              `fresh` — just printed). Idempotent: updates
                              the source's existing open (unchecked) entry
                              in place rather than piling up duplicates.
                              Always exits 0 (README.md#drift-notice — a notice,
                              never a gate); a missing TODO.md is a WARN,
                              not a failure.

  resolve <source> [note]     Check off <source>'s open entry in TODO.md's
                              "## Pending Drift Reviews" section — call this
                              once its drift has actually been reviewed
                              (the update was taken, or deliberately
                              deferred). [note], if given, is appended to
                              the checked-off line. A no-op, not an error,
                              when there's no open entry for <source>.

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
      python3 process/personal/tools/pack_sync.py record bestpractice "NOTICE: ..."
      python3 process/personal/tools/pack_sync.py resolve bestpractice "took the update"
      python3 process/personal/tools/pack_sync.py status ../RepoPersonalPreferences
      python3 process/personal/tools/pack_sync.py update ../RepoPersonalPreferences
"""
import datetime, filecmp, io, json, pathlib, re, shutil, subprocess, sys, tarfile, tempfile

HERE = pathlib.Path(__file__).resolve()
_top = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=HERE.parent,
                      capture_output=True, text=True).stdout.strip()
ROOT = pathlib.Path(_top) if _top else HERE.parents[3]
SUBTREE = 'process/personal'
PACK = ROOT / SUBTREE
MANIFEST = ROOT / 'process' / 'manifest_personal.json'

# --- Pending Drift Reviews (README.md#drift-notice) ---------------------------------
# A session-start freshness notice used to be stdout-only: printed once, then
# gone the moment a session's attention moved to whatever concrete task was
# actually in front of it. That's exactly what happened in a dependent repo
# on 2026-08-27 -- a BestPractice-drift notice fired, was never raised, and
# only surfaced when the user asked directly a full task later (real name
# kept out of this vendored file, per README.md#private-repo-scrub).
# record()/resolve() below persist the same notice into the target repo's own
# TODO.md instead, so it survives past the turn it fired in and shows up in
# light_check.py's output on every commit (a WARN, still never a gate --
# README.md#drift-notice is explicit that taking an update stays deliberate) until
# someone actually resolves it.
TODO = ROOT / 'TODO.md'
# Local adaptation for this repo: kept sentence case ("Pending drift
# reviews") rather than the pack's own NY Times-style default, matching
# this repo's existing, consistent heading practice
# (process/personal/README.md#header-caps explicitly leaves the choice to
# each repo). Re-apply this line after any future mirror from
# RepoPersonalPreferences.
PENDING_HEADING = '## Pending drift reviews'
PENDING_INTRO = (
    "Auto-maintained by `pack_sync.py record` / `resolve`\n"
    "([`drift-notice`](process/personal/README.md#drift-notice)) -- a\n"
    "session-start freshness notice lands here, not just on stdout, so it\n"
    "can't lose a priority fight against whatever task is already in front\n"
    "of a session and go unaddressed. `light_check.py` warns on every commit\n"
    "while an entry below stays unchecked. Check an item off (or run\n"
    "`pack_sync.py resolve <source>`) once its drift has actually been\n"
    "reviewed -- the update taken, or deliberately deferred with a reason."
)


OPEN_ENTRY_RE = re.compile(r'^- \[ \] \*\*([\w.-]+)\*\* \(([^)]*)\): (.*)$',
                           re.MULTILINE)


def _entry_pattern(source):
    return re.compile(rf'^- \[ \] \*\*{re.escape(source)}\*\* \([^)]*\): .*$',
                      re.MULTILINE)


def open_entries(todo_text):
    """(source, date, notice) for every open "## Pending Drift Reviews" line.

    Shared with light_check.py so both tools agree on exactly one format --
    scoped to the section body so an unrelated TODO.md line that happens to
    look similar is never mistaken for a drift entry.
    """
    if PENDING_HEADING not in todo_text:
        return []
    start = todo_text.index(PENDING_HEADING) + len(PENDING_HEADING)
    end = todo_text.find('\n## ', start)
    body = todo_text[start:end if end != -1 else len(todo_text)]
    return [m.groups() for m in OPEN_ENTRY_RE.finditer(body)]


def record(source, notice):
    """Persist a freshness notice into TODO.md; idempotent per source."""
    notice = ' '.join(notice.split())  # collapse to one line
    if not TODO.exists():
        print(f"pack_sync record: WARN no TODO.md at repo root -- "
              f"'{source}' notice was NOT persisted, only printed above.")
        return 0
    text = TODO.read_text(encoding='utf-8')
    today = datetime.date.today().isoformat()
    line = f"- [ ] **{source}** ({today}): {notice}"

    existing = _entry_pattern(source)
    if existing.search(text):
        text = existing.sub(line, text, count=1)
    elif PENDING_HEADING in text:
        head_idx = text.index(PENDING_HEADING)
        next_idx = text.find('\n## ', head_idx + len(PENDING_HEADING))
        insert_at = next_idx if next_idx != -1 else len(text)
        before = text[:insert_at].rstrip('\n')
        after = text[insert_at:]
        text = before + '\n' + line + '\n\n' + after.lstrip('\n')
    else:
        section = f"{PENDING_HEADING}\n\n{PENDING_INTRO}\n\n{line}\n\n"
        m = re.search(r'\n(## )', text)
        text = (text[:m.start() + 1] + section + text[m.start() + 1:] if m
               else text.rstrip('\n') + '\n\n' + section)

    TODO.write_text(text, encoding='utf-8')
    print(f"pack_sync record: TODO.md's '{PENDING_HEADING}' updated -- "
          f"{source} drift noted for review.")
    return 0


def resolve(source, note=''):
    """Check off <source>'s open TODO.md entry. No-op if none is open."""
    if not TODO.exists():
        return 0
    text = TODO.read_text(encoding='utf-8')
    m = _entry_pattern(source).search(text)
    if not m:
        print(f"pack_sync resolve: no open '{source}' entry in TODO.md -- nothing to do.")
        return 0
    today = datetime.date.today().isoformat()
    new_line = m.group(0).replace('- [ ]', '- [x]', 1) + f" -- resolved {today}"
    if note:
        new_line += f": {note}"
    text = text[:m.start()] + new_line + text[m.end():]
    TODO.write_text(text, encoding='utf-8')
    print(f"pack_sync resolve: '{source}' entry checked off in TODO.md.")
    return 0


def _git(clone, *args):
    return subprocess.run(['git', '-C', str(clone)] + list(args),
                          capture_output=True, text=True).stdout.strip()


def _files(base):
    return {p.relative_to(base) for p in base.rglob('*')
            if p.is_file() and '.git' not in p.parts}


def _diff(clone_subtree):
    """(added, modified, deleted) needed to bring the pack tree to match a
    clone's subtree -- i.e. from the UPDATE's own perspective, not a bare
    set difference: "added" is new in the clone (copy it into PACK),
    "deleted" is gone from the clone (remove it from PACK). Getting this
    backwards once made update() try to unlink a file that only exists in
    the clone, and copy a file from the clone that only exists in PACK --
    both raise FileNotFoundError the moment a dependent repo's mirror
    actually adds or removes a file, which every prior exercise of this
    path had happened not to do (origin: 2026-08-29, a dependent repo's
    session hit this on this pack's own new private_repo_blocklist.txt)."""
    ours, theirs = _files(PACK), _files(clone_subtree)
    added = sorted(theirs - ours)
    deleted = sorted(ours - theirs)
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
                  f"(process/personal/README.md#drift-notice).")
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
    if args and args[0] == 'record':
        if len(args) < 3:
            sys.exit(__doc__)
        return record(args[1], ' '.join(args[2:]))
    if args and args[0] == 'resolve':
        if len(args) < 2:
            sys.exit(__doc__)
        return resolve(args[1], ' '.join(args[2:]))
    if len(args) < 2 or args[0] not in ('status', 'update'):
        sys.exit(__doc__)
    clone = _clone_or_die(args[1])
    if args[0] == 'status':
        return status(clone)
    return update(clone, force='--force' in args)


if __name__ == '__main__':
    sys.exit(main())
