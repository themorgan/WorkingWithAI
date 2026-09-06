#!/usr/bin/env python3
# Last updated: 2026-09-02 (Buenos Aires) by a Precedent beta-test session, to version 4
"""report_automation_issue.py — persist an unattended job's blocker as a
GitHub issue, not just a log line or Actions annotation.

Relocated from process/personal/tools/ 2026-09-02 when process/personal/ was
retired (see process/PRECEDENT_MIGRATION.md) — a generic utility, not
personal-pack content, so it moved to this repo's own tools/ rather than
being dropped. precedent-team-maintainers/practices/automation-issues.md
carries the same rule now: any unattended job in this repo that hits
something blocking it -- a missing or revoked secret, an unexpected
failure, anything that stops it finishing its normal work -- reports that
blocker here instead of (or in addition to) a `::warning::` Actions
annotation. An annotation only exists inside one specific workflow run;
nobody sees it unless they already know to go looking. A GitHub issue
persists in the repo itself and rides GitHub's own notification system
(email, mobile push) for free -- no notification infrastructure to build.

Idempotent by design: one open issue per <label>, not one per run. A
second call with the same label comments on the existing open issue
(with a "recurred" stamp) instead of opening a duplicate -- a blocker that
fires every week should read as one ongoing problem, not fifty separate
ones.

Requires the `gh` CLI (preinstalled on GitHub-hosted runners) authenticated
via a GH_TOKEN or GITHUB_TOKEN environment variable with `issues: write`
permission -- set both in the calling workflow job, e.g.:

  permissions:
    issues: write
  steps:
    - env:
        GH_TOKEN: ${{ github.token }}
      run: python3 tools/report_automation_issue.py ...

Fails gracefully (precedent-team-maintainers/practices/fail-gracefully.md):
if `gh` isn't authenticated, isn't installed, or the API call fails for any
reason, this prints a clear WARN to stderr and exits 0 rather than failing
the calling job -- a failure to *report* a blocker should never itself
become a second, more confusing blocker (the run's own `::warning::`
annotation, left in place by the caller, is the fallback that still gets
through).

Run:  python3 tools/report_automation_issue.py \\
        <label> "<title>" "<body>"
"""
import datetime, json, subprocess, sys


def _gh(args, **kwargs):
    return subprocess.run(['gh'] + args, capture_output=True, text=True, **kwargs)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    label, title, body = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Idempotent: the label itself may not exist yet on a fresh repo.
        _gh(['label', 'create', label, '--color', 'd93f0b',
             '--description', 'Unattended automation is blocked and needs attention',
             '--force'])

        existing = _gh(['issue', 'list', '--label', label, '--state', 'open',
                        '--json', 'number', '--limit', '1'])
        rows = json.loads(existing.stdout) if existing.returncode == 0 and existing.stdout.strip() else []

        if rows:
            number = rows[0]['number']
            stamp = f"Recurred: {datetime.date.today().isoformat()}\n\n{body}"
            r = _gh(['issue', 'comment', str(number), '--body', stamp])
            if r.returncode != 0:
                print(f"report_automation_issue: WARN couldn't comment on #{number}: "
                      f"{r.stderr.strip()}", file=sys.stderr)
                return 0
            print(f"report_automation_issue: commented on existing open issue "
                  f"#{number} (label '{label}').")
        else:
            r = _gh(['issue', 'create', '--title', title, '--body', body,
                     '--label', label])
            if r.returncode != 0:
                print(f"report_automation_issue: WARN couldn't open an issue: "
                      f"{r.stderr.strip()}", file=sys.stderr)
                return 0
            print(f"report_automation_issue: opened {r.stdout.strip()} (label '{label}').")
    except Exception as e:
        print(f"report_automation_issue: WARN unexpected error, not reported "
              f"as an issue: {e}", file=sys.stderr)
    return 0


if __name__ == '__main__':
    # `--help` is what anyone types first, and this used to answer with a
    # usage FAIL. The module docstring is the usage text. (Same fix applied
    # across the upstream engine's tools on 2026-09-06.)
    if any(a in ('--help', '-h') for a in sys.argv[1:]):
        print((__doc__ or '').strip())
        sys.exit(0)
    sys.exit(main())
