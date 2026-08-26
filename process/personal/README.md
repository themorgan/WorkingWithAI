<!-- Last updated: 2026-08-24 09:26:15 (Buenos Aires) by Morgan F, to version 3 -->

# The personal pack

A "pack" in BestPractice's own vocabulary (practice 23,
[process/upstream/INSTALL.md](../upstream/INSTALL.md) §7) is a small rulebook
too specific to belong in the public BestPractice repo but too general to
belong to just one project. This one is exactly that middle ground: personal
conventions Morgan wants in **every** repo she starts, not generic enough for
the public upstream and not specific enough to live in just one project's own
[AGENTS.md](../../AGENTS.md).

Unlike a domain-compliance pack, this one has no *dedicated, single-purpose*
repo of its own — it lives here, in RepoPersonalPreferences (which also
carries this repo's own BestPractice install, since it's a normal working
repo too, not just the pack's source), and gets copied into each new repo
alongside BestPractice itself (see [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md)).
Within *this* repo, `upstream.commit` in
[../manifest_personal.json](../manifest_personal.json) stays `null` — the
vendored tree here *is* upstream for the pack, per the pack anatomy rule
([process/upstream/INSTALL.md](../upstream/INSTALL.md) §7). In a
*dependent* repo the pack is vendored into, that repo's own
`manifest_personal.json` instead records this repo's real URL and commit
(§18 below) — a subtree-tracked dependency in place of the eventual
dedicated-repo split §7 anticipates, which a scheduled check (§15) then keeps
current, the same way [process/manifest.json](../manifest.json) tracks
BestPractice.

## The rules, and why

Section numbers follow the reading order: **§1 runs to §18 top to bottom,
in groups, and a reorganization renumbers them.** Related rules sit next to
each other, the everyday ones come before the rare ones (BestPractice
practice 36), and the rules *about* keeping the pack itself current sit at
the end, where a reader who just wants to know how to work here never has to
scroll past them. The cost is that a § number is a pointer into the current
file, not a permanent name for a rule: whenever this file is reorganized,
every citation of it — [AGENTS.md](../../AGENTS.md),
[MAP.md](../../MAP.md), [GLOSSARY.md](../../GLOSSARY.md),
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md),
[TODO.md](../../TODO.md)'s decision records, the manifests, the templates,
and every repo this pack is installed into — gets updated in the same
commit, never left pointing at whatever rule now holds the old number. A
reorganization that can't reach a dependent repo's citations doesn't ship
until it can.

**Start with §1 and §2** — they govern how every other rule here is
applied: on conflict, this pack wins; where it only restates BestPractice,
it gets dropped. The rest, in order:

| Group | Rules |
|---|---|
| Relationship to BestPractice | §1 (this pack wins on conflict), §2 (don't duplicate) |
| Who, when, and where — the header and trailer on every commit and file | §3 (commit author and email), §4 (Buenos Aires dates and timezone), §5 (last-updated timestamp, and who made it), §6 (session-link trailer) |
| How a session decides and lands work | §7 (decide small calls), §8 (`go`/`merge` shorthand), §9 (TODO gate before every push), §10 (mirror agent-relevant instructions into [AGENTS.md](../../AGENTS.md)), §11 (light check before every commit) |
| Code this pack helps write | §12 (platform-neutral LLM integrations), §13 (fail gracefully) |
| Keeping the vendored copies current (the meta rules) | §14 (BestPractice sync), §15 (its sibling, the pack sync), §16 (end-of-session drift check, layered on both) |
| Installing the pack into a repo | §17 (default branch), §18 (the install procedure itself) |

### §1. On conflict with BestPractice, this pack wins

BestPractice sets the default; where a rule in this pack and a rule of
BestPractice's own genuinely disagree on the same point, this pack's rule
governs — in this repo, and in every repo the pack gets installed into.
Several rules below already do this in their own particular way — §3
replaces, rather than defers to, BestPractice's "ask before the first
commit" default, and §7 sharpens its "ask when genuinely unsure" default
toward a narrower one — so this section states the general rule up front
rather than leaving a reader to notice it separately in each entry's own
reasoning. Where this pack is silent on a point, BestPractice's own rule
stands undisturbed — the pack only narrows or overrides where it actually
speaks.

### §2. Don't duplicate BestPractice

This pack exists to add to BestPractice or override it, not to restate it.
A rule here that only repeats something BestPractice already establishes on
its own — same substance, no actual change in outcome — gets dropped from
this file the next time it's touched: a restated rule is a second place for
the same idea to drift out of sync with the first, for no benefit over
leaving BestPractice's own text to stand alone. Applies at install time too
(§18 below): weaving [templates/AGENTS_ADDENDUM.md.template](templates/AGENTS_ADDENDUM.md.template)
into a target repo's freshly-instantiated `AGENTS.md`, skip any bullet whose
substance that repo's BestPractice install already carries verbatim, rather
than installing a second copy of the same sentence.

### §3. Commit author is always "Morgan F"

BestPractice's own convention (practice: commits credited to the human
driving the session) asks the agent to find out who that is before the
first commit. Here, that's already decided — don't ask:

```
git config user.name "Morgan F"
git config user.email "morgan@westegg.com"
```

The email is Morgan's own address, used to identify her as the author of
every commit. `tools/bootstrap.sh` runs this at session start (see §18
below), so it never needs to be typed by hand.

This rule replaces only the *identity* half of BestPractice's own
convention. It says nothing about co-authorship, so BestPractice's own
`Co-Authored-By:` trailer naming the assistant still applies, undisturbed —
§1's "where this pack is silent, BestPractice stands", in its most concrete
form.

### §4. Every date is Buenos Aires local time

Not the session container's system clock, and not UTC. Two mechanisms, one
rule:

- **Prose dates** (a doc's "as of" note, a last-updated header) are the
  Buenos Aires calendar date on the day the text was written.
- **Git timestamps** get the right offset by running the commit itself under
  `TZ="America/Argentina/Buenos_Aires"` — git's own C library resolves the
  offset from `TZ` at commit time, so no manual date arithmetic is needed:
  `TZ="America/Argentina/Buenos_Aires" git commit -m "..."`.

Argentina has held UTC−3 year-round, with no daylight saving, since 2009
*(verified 2026-08-21)*. If that ever changes, both mechanisms above and the
sync workflows' cron lines in §14 and §15 need re-deriving —
[TODO.md](../../TODO.md) carries a standing reminder to re-check this the
next time this file is touched.

### §5. A "last updated" timestamp, author, and version — at the top of files, when reasonable

Markdown files get
`<!-- Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by NAME, to version N -->`
as their first line — a full timestamp, not just a calendar date: hour,
minute, and second, in Buenos Aires local time, the same clock §4 already
uses everywhere else. A bare date can't tell two same-day edits apart; the
time of day can. `NAME` is whoever made the edit — in this repo and every
repo this pack is installed into, that's always "Morgan F" (§3), the same
name every commit is already authored as — so the header settles who last
touched the file without a reader needing to go check `git blame`. `N` is a
plain integer counter *private to that one file*: 1 the first time the
header is added, incremented by 1 each subsequent time the file's content
changes. Update the line whenever you touch the file's content, not its
formatting alone — that's also the trigger for bumping `N`.

The "to version N" phrasing is deliberate: it names that one file's own
version, not a repo-wide release number, so bumping it is a one-file edit,
never a reason to touch anything else. That also means installing this rule
doesn't mean retrofitting a header onto every existing file at once — a
file only picks up (or bumps) its header when it's actually being edited
for some other reason; the header describes that file's edit history, not a
standing obligation to sweep the repo. Files in a comment-bearing format
(`.sh`, `.yml`) get the equivalent in that syntax. Skipped where it can't
help: JSON has no comment syntax, and anything under `process/upstream/`
must stay a byte-for-byte mirror of the public repo — never hand-edited,
header included.

### §6. Commit messages link the session where the change was planned

A `Session: <url>` trailer on every commit. For Claude Code,
`https://claude.ai/code/session_<ID>`. For the unattended sync (§14),
which has no chat session behind it, the workflow run's own URL stands in.
If a tool has no shareable link at all, the trailer says so explicitly
(`Session: none available (<tool>)`) rather than being silently omitted —
so a reviewer can tell "considered and skipped" from "forgotten" at a
glance.

### §7. Decide small calls yourself; only stop for big ones

Default to continuing, not asking. When a judgment call is needed to keep
the work moving — filling in a default, picking between two reasonable
implementations, resolving an ambiguity that doesn't change the shape of
what gets delivered — make the call and note it in the normal end-of-work
reply, rather than stopping to ask first. Reserve stopping and asking
(BestPractice's own `AskUserQuestion` or equivalent) for calls that are
genuinely big: hard or costly to undo, change what gets delivered or to
whom, spend real money, touch credentials or production, or are the kind
of toss-up where two reasonable people would clearly land in different
places.

A small or moderate call made this way still gets surfaced, just not as an
interruption: it goes in **both** places — the same end-of-work reply that
already lists files touched (practice 12), *and* the commit message itself,
under a "Judgment calls made:" heading, the same way the sync (§14)
already lists its own judgment calls under "Judgment calls to review:"
rather than blocking on each one. The chat reply is easy to miss once a
thread scrolls on; the commit message is the one copy that survives into
`git log` and the PR diff, where it stays visible for as long as the repo
does — so a member reviewing a merged PR later (not just reading the reply
in the moment) can still see what was decided on their behalf. Skip the
heading only when a commit truly made no judgment calls — don't pad it with
"none" noise on every commit, but never omit it when a call was actually
made. This sharpens BestPractice's own "ask when genuinely unsure" default
toward Morgan's own risk tolerance: most calls in day-to-day work here (a
wording choice, which of two valid layouts to use, a template's exact
phrasing) are small enough to just make.

### §8. "go" or "merge" as a standalone final sentence authorizes commit + merge

If Morgan's message, at a point where you've said you're ready to commit
(or ready to commit and merge), ends with `go` or `merge` standing alone as
its own sentence — case-insensitive, whether that's the whole message on
one line or the last sentence of a longer one, set off by ordinary
sentence-ending punctuation — treat it as her authorization, right there,
to commit the pending work and merge it into the default branch, following
this repo's usual conventions (author identity, Buenos Aires timestamp,
session trailer, the audits) without asking again first. "That was perfect.
merge", "Go.", and a lone line reading `MERGE` all count; "let's merge the
two lists" and "go check the logs" don't, because there the word is part of
a longer sentence, not standing alone as the message's last one. This isn't
a new kind of permission — it's shorthand for the same authorization
BestPractice's own "merge only when the user says so" default already asks
for (woven into every installed `AGENTS.md`'s Git / workflow section); `go`
and `merge` are just the standalone forms that count as saying so. Where
context leaves it ambiguous whether the trailing word is this shorthand or
just part of the sentence's own meaning — or where multiple pending items
make it unclear what "merge" would even apply to — don't assume: ask.

### §9. TODO.md gets reconciled before every push

Woven into the installed [AGENTS.md](../../AGENTS.md)'s merge runbook as
step 0c, right after BestPractice's own capture gate (0) and export gate
(0b): before pushing, check the thread's discussion against
[TODO.md](../../TODO.md) — add ideas that came up but never got a line,
remove or check off what this branch just implemented. `TODO.md` drifting
out of sync with what was actually decided is common enough in practice
that it earns its own gate rather than staying an occasional "oh, I should
update that" afterthought.

### §10. Agent-relevant instructions in a README or other key file also go in AGENTS.md

`AGENTS.md` is the file a session is told to read first (BestPractice's own
entry-point convention); a README, a `CONTRIBUTING.md`, a
[GETTING_STARTED.md](../../GETTING_STARTED.md), or any other key file can still pick up its own operational instructions over
time — a setup step, a gotcha, a rule about how to work in the repo — written
where a human reader would look for it, not where an agent is told to look.
When any such file gains an instruction that would be useful for an agent to
know (not general project description, not end-user documentation — the
operational kind: how to build it, a constraint on how to work, a step an
agent would otherwise miss), fold the same instruction into `AGENTS.md` too,
in its own words if that reads better there, rather than leaving it stranded
in the other file for an agent to find only by accident. This runs both
ways an author might add such a line — whether it lands first in the README
(or other key file) and needs pulling into `AGENTS.md`, or is written into
`AGENTS.md` directly and never mirrored back to where a human would expect
to read it; either direction, the same instruction ends up in both places.
It does not run the other way for content that only belongs in one place: a
README's marketing framing, install screenshots, or badges have no
business in `AGENTS.md`, and `AGENTS.md`'s own meta-structure (the quick
index, the merge runbook mechanics) has no business padding out a README
written for a human skimming the repo for the first time. Check for this at
the capture gate (merge runbook step 0, [AGENTS.md](../../AGENTS.md)) the
same way any other captured decision gets folded in — a stray instruction
left in only one file is exactly the kind of drift that gate exists to
catch.

### §11. A light check runs on every commit path

[tools/light_check.py](tools/light_check.py) — merge-conflict markers,
invalid JSON/YAML/Python syntax, secret-shaped strings (an AWS-style key ID,
a private-key PEM header, a GitHub token), broken relative doc links, and
(repo-wide, every run, regardless of what changed) that `process/personal/`
is actually vendored: `process/manifest_personal.json` exists, parses, has
at least one entry, and every entry's `local_path` exists on disk. That
last check exists specifically to catch the pack having been dropped into a
repo by a plain copy rather than installed per §18 below — copying gets you
the files but not the tracked provenance (upstream commit, per-file
hashes) that makes the pack auditable and syncable, and a `cp -r` won't
necessarily touch `manifest_personal.json` at all, so this can't be scoped
to changed files the way the other checks are. BestPractice's
[doc_lint.py](../upstream/tools/doc_lint.py) is Markdown-specific
(accidental strikethrough, unlinked references, unglossed acronyms); this
is the broader, cheaper net for "something obviously went wrong" that isn't
a style question. Run it yourself before every commit, same as
`doc_lint.py`; it's also wired as
[templates/github-actions/light-check.yml.template](templates/github-actions/light-check.yml.template)
→ [.github/workflows/light-check.yml](../../.github/workflows/light-check.yml)
so it binds every path to the default branch even when a session
forgets — the same reasoning BestPractice's own [TODO.md](../../TODO.md)
gives for preferring required CI checks over runbook steps alone. This is
also why the vendoring check belongs in `light_check.py` specifically
rather than only in prose here: once a repo has installed the pack, this
check is already wired into that repo's own CI on every push and PR, so a
future session (or person) that drops `process/personal/` into a *new*
repo without going through §18 gets caught the moment `light-check.yml`
runs — install-time correctness enforced automatically, not just documented.

### §12. LLM integrations stay platform-neutral; OpenRouter is the default assumption

Whenever a system this pack helps set up needs to talk to an LLM, build it
against a provider-neutral interface — model name, API key/token, and base
URL as swappable configuration, not hard-wired to one vendor's SDK, auth
header shape, or response schema. That keeps swapping providers, or dropping
in whichever token happens to be on hand, a config change rather than a
rewrite chasing call sites through the codebase.

Absent a specific instruction otherwise, assume the credential in hand is an
[OpenRouter](https://openrouter.ai) token, not a given vendor's own key —
that's the provider Morgan actually uses day to day, so it's the safer
default to design and test against. OpenRouter's own API is itself
OpenAI-request-shaped and fronts most major model providers behind one key
and one endpoint *(verified 2026-08-22)*, so it doubles as a sensible
default shape for the neutral interface itself, not just the default
credential — re-verify this claim if OpenRouter's API shape is ever the
reason a piece of code built against this rule breaks.

### §13. Always fail gracefully

Any code this pack helps write or set up anticipates its own common failure
modes rather than letting them surface as an unhandled crash. Concretely:
before shipping code that depends on something outside its own control —
a required config variable or environment variable, a file that's supposed
to exist, a network call, a third-party credential — write it to check for
the absence or failure case on purpose and degrade in a way the caller can
act on: a clear error message naming exactly what's missing and how to fix
it, a documented fallback/default, or a clean non-zero exit — never a raw
stack trace, a silent wrong answer, or a hang. This is a coding-quality rule
for what this pack builds, not a repository-process rule like most of the
rest of this file; it belongs here rather than upstream because it is
general enough for every
repo Morgan starts, and simple enough that raising it to a persuasive,
attributed BestPractice submission per
[process/upstream/INSTALL.md](../upstream/INSTALL.md) §4 isn't worth the
effort yet — check-in remains the outlet if that changes (see
[TODO.md](../../TODO.md)'s recurring check-in item).

### §14. A sync keeps BestPractice current, unattended

*(§15 is this rule's sibling — the same shape, pointed at the personal pack
instead of BestPractice. Change one and check the other. §16 layers an
end-of-session drift check on top of this one and §15 both — same
comparison, but it only asks, never merges unattended.)*

[templates/github-actions/upstream-sync.yml.template](templates/github-actions/upstream-sync.yml.template)
→ `.github/workflows/bestpractice-upstream-sync.yml`. Runs on a schedule —
**weekly by default** (Mondays at 09:00 Buenos Aires); the workflow file's
`on.schedule` block carries a commented-out daily cron line right next to
the active weekly one, so switching cadence (or moving either to a
different time of day) is a one-line comment/uncomment in the workflow
file, not a rewrite. A cheap `check` job compares `process/manifest.json`'s
recorded upstream commit against BestPractice's actual HEAD via
`git ls-remote` — no model call, no cost, on a quiet run. If upstream
moved, an `update` job runs
[Claude Code as a GitHub Action](https://github.com/anthropics/claude-code-action)
to take the update per BestPractice's own
[INSTALL.md](../upstream/INSTALL.md) §2: three-way-merge each manifest
entry through its recorded adaptation, re-run every gate
([doc_lint.py](../upstream/tools/doc_lint.py),
[light_check.py](tools/light_check.py),
[practice_audit.py](../upstream/tools/practice_audit.py)), commit with
every
judgment call it made spelled out under a "Judgment calls to review:"
heading in the commit message, open a PR, and — once this repo's own checks
pass on that PR — merge it to the default branch.

**Requires**, once per repo: a Claude credential — either repository secret
`CLAUDE_CODE_OAUTH_TOKEN` (a Claude Pro/Max subscriber generates this by
running `claude setup-token` locally; no per-call billing) or repository
secret `ANTHROPIC_API_KEY` (an Anthropic API key with billing enabled);
either satisfies the requirement, and only one is needed — plus "Allow
auto-merge" turned on, and Actions permitted to open pull requests. See
[GETTING_STARTED.md](../../GETTING_STARTED.md)'s administrator section for
the exact click-path in a given repo (BestPractice practice 37 — every
GitHub-specific requirement gets disclosed there, not just here).

If a run ever can't confidently resolve something, it leaves the PR open,
unmerged, with a comment explaining exactly what it couldn't do — it never
forces a merge past a failing check.

**If neither credential is set when upstream has moved,** the `update`
job is skipped rather than attempted and failing on an auth error — a
`note-missing-credential` job leaves a plain `::warning::` in that run's
summary instead, so a quiet-looking sync can still be told apart from a
real "nothing to sync" run. `CLAUDE_CODE_OAUTH_TOKEN` and
`ANTHROPIC_API_KEY` are only ever spent by this `update` job's Claude Code
call (and its personal-pack-sync sibling's, §15) — no other automation in
this repo uses either. A chat session asked to run the sync manually
doesn't need either secret at all, since it's already Claude; it should
just take the update itself following [INSTALL.md](../upstream/INSTALL.md)
§2 above, and remind the user to set one of the two so future unattended
runs don't need to be asked for by hand.

### §15. A sync keeps the personal pack itself current

The pack's own analogue of §14's BestPractice sync — same shape, a
separate workflow and a separate concern. §14 keeps a dependent repo's
`process/upstream/` current with the public BestPractice repo; this keeps
that same repo's `process/personal/` current with *this* repo,
RepoPersonalPreferences, once Morgan is adding rules to the pack often
enough that copy-once-at-install stops being enough (the reason this
section exists at all — see [TODO.md](../../TODO.md) for the decision
record).

[templates/github-actions/personal-pack-sync.yml.template](templates/github-actions/personal-pack-sync.yml.template)
→ `.github/workflows/personal-pack-sync.yml`. Runs on the same
weekly-by-default, daily-optional schedule as §14 (Mondays at 09:15 Buenos
Aires, fifteen minutes after §14's own weekly slot so the two never race
over the same working tree; the commented-out daily alternative sits
fifteen minutes after §14's own daily alternative for the same reason —
switching either workflow's cadence independently still keeps them apart).
A cheap `check` job compares `process/manifest_personal.json`'s recorded
`upstream.commit` against this repo's actual HEAD via an authenticated
`git ls-remote` — no model call, no cost, on a quiet run. If the pack
moved, an `update` job runs
[Claude Code as a GitHub Action](https://github.com/anthropics/claude-code-action)
to take the update: mirror `process/personal/` from a fresh clone via
[tools/pack_sync.py](tools/pack_sync.py) (§18 below — genuinely simpler
than BestPractice's own check-in machinery, since the pack is a one-way
dependency with no landing-PR phase to wait through), re-weave any changed
template sections into the target repo's own `AGENTS.md` and other
installed, adapted copies, re-run every gate, commit with every judgment
call spelled out under a "Judgment calls to review:" heading, open a PR,
and — once the target repo's own checks pass on that PR — merge it to the
default branch.

**The one real difference from §14:** RepoPersonalPreferences is *private*,
where the public BestPractice repo isn't, so both jobs need their own
repository secret to reach it — `PERSONAL_PACK_TOKEN`, a GitHub personal
access token (fine-grained, read-only, scoped to just
`themorgan/RepoPersonalPreferences`), in addition to the Claude credential
§14 already needs (`CLAUDE_CODE_OAUTH_TOKEN` or `ANTHROPIC_API_KEY` — either
one), plus the same "Allow auto-merge" and Actions-can-open-PRs
toggles. **No workflow, and no session, can mint or install this token on
Morgan's behalf** — an administrator (Morgan) has to generate it herself at
[github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)
and add it at the target repo's own **Settings → Secrets and variables →
Actions → New repository secret**. `check` still skips the update rather
than failing the workflow when the token is missing (a private-repo
credential shouldn't block an otherwise-successful install), but every
such run now also emits a `::warning::` GitHub Actions annotation — a
per-run smoke test, visible in the Actions UI on every firing, not just a
one-time install reminder — so a token that was never set, or later
revoked, gets noticed the same day rather than by chance. A session
installing this pack should still say so explicitly in its reply the first
time, not rely solely on the recurring workflow warning to be the first
notice — see [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8 and §13
step 9 below, both of which repeat this reminder for exactly that reason.

If a run ever can't confidently resolve something, same as §14: it leaves
the PR open, unmerged, with a comment explaining exactly what it couldn't
do — it never forces a merge past a failing check.

### §16. A session-start notice asks about drift immediately, not at the end

The scheduled syncs (§14, §15) close the gap *between* sessions — they run
whether or not anyone opens the repo. This rule closes a narrower gap, and
closes it as early as possible: the one scheduled run hasn't caught up yet
because it hasn't fired since the drift happened, even though a session —
and the person who can approve an update — is right here, from the very
first turn. It's additive, not a replacement: dropping either scheduled
sync in favor of this would leave updates unnoticed for however long the
repo sits idle between sessions, which is exactly the gap §14 and §15
exist to bound.

Detection is automated and immediate — a session doesn't have to remember
to run anything:

- **BestPractice half — already wired.** `tools/bootstrap.sh` runs
  `checkin.py fresh` on every session start (practice 13): one clone-free
  `git ls-remote` against the public BestPractice repo, printed as a
  single notice line only when [process/manifest.json](../manifest.json)'s
  recorded `upstream.commit` is stale — silent when current or
  unreachable, never a gate, no model call.
- **Personal-pack half — newly wired (§18 step 4).** `tools/bootstrap.sh`
  now also runs `python3 process/personal/tools/pack_sync.py fresh`
  ([tools/pack_sync.py](tools/pack_sync.py)) on every session start, from
  [templates/bootstrap-freshness.sh.template](templates/bootstrap-freshness.sh.template) —
  the same shape, comparing
  [manifest_personal.json](../manifest_personal.json)'s recorded
  `upstream.commit` against RepoPersonalPreferences's actual HEAD. Only in
  a repo where this pack is vendored in as a dependency (i.e. every repo
  *except* RepoPersonalPreferences itself — see the exemption below).

Because both run as part of the same session-start hook that already sets
up the environment, their output is right there in the opening turn — a
session raises whichever one fired as part of catching the member up, not
something saved for the end.

**Taking either update stays deliberate, whenever it's raised.** Never
take it without being asked, whether that's the first exchange of the
session or later — this is the one deliberate difference from §14 and
§15, which merge unattended. A human is already present to answer, so
there's no reason to skip the ask the way the scheduled runs have to. If
asked to proceed, take the update the same way a manually-requested sync
already does (§14's own closing paragraph, and §15's sibling): BestPractice
per [INSTALL.md](../upstream/INSTALL.md) §2, the personal pack per
[pack_sync.py](tools/pack_sync.py) — every gate re-run, opened as a PR,
merged only once the user approves it (not auto-merged the way the
scheduled `update` jobs are, since a human is already in the loop to say
yes).

**RepoPersonalPreferences is exempt from the personal-pack half of this —
both the session-start notice and its end-of-session fallback below — on
itself,** the same reason §15's workflow isn't installed here at all: the
vendored tree here *is* upstream for the pack (the pack anatomy rule,
[INSTALL.md](../upstream/INSTALL.md) §7), so comparing it against itself
is circular, not a real drift check. Neither
`templates/bootstrap-freshness.sh.template`'s line nor `pack_sync.py
fresh` runs against this repo's own `tools/bootstrap.sh`. The BestPractice
half still applies here, unexempted — this repo genuinely vendors
`process/upstream/` from the public BestPractice repo, same as any
dependent repo does.

**Fallback, for whenever a session-start notice didn't fire or drift
happened mid-session** (an indirect install with no working bootstrap
wiring yet, a long-running session, offline at start but reachable
later): at the end of every chat session, right after the merge runbook's
own steps (after landing the branch's own work, not instead of it), repeat
the same cheap comparisons — no model call needed, just `git ls-remote`
against each source and a look at the recorded manifest commit, the same
comparisons the session-start notices already make (always the
BestPractice comparison; the personal-pack comparison too, except in
RepoPersonalPreferences itself, per the exemption above). If either has
moved and hasn't already been raised and answered earlier in the session,
say so plainly — which repo, the recorded commit, the actual HEAD — and
ask whether to take the update now before ending the session.

**This also has to survive an indirect install.** The comparisons above
assume a fully-installed repo — files present, manifest current, bootstrap
wiring in place. That's not guaranteed when either tree arrived by some
path other than a session actually running
[INSTALL.md](../upstream/INSTALL.md) §1 or §18 below: a fork, a
template-repo "use this template," a plain file copy, or — the case that
prompted this paragraph — a repo that vendored from an *already-dependent*
repo instead of from the canonical source. Any of those can carry
`process/upstream/` and/or `process/personal/` without carrying the
mechanisms that keep them current. So the same check also verifies,
cheaply, whenever either tree is present: does
`.github/workflows/bestpractice-upstream-sync.yml` exist (when
`process/upstream/` is present), does
`.github/workflows/personal-pack-sync.yml` exist (when `process/personal/`
is present and this isn't RepoPersonalPreferences itself, per the
exemption above), does `tools/bootstrap.sh` actually carry both freshness
snippets, and does `AGENTS.md` actually carry the woven-in sections (the
`agents-addendum` entry's `section_marker`, per
[manifest_personal.json](../manifest_personal.json))? If any of those is
missing, that's an incomplete install, not drift — say so plainly (which
piece is missing) and offer to finish it, in-session: run whichever of
§18's steps (or [INSTALL.md](../upstream/INSTALL.md) §1's) produces the
missing piece, sourced from the canonical repo — the public BestPractice
repo, or RepoPersonalPreferences for the pack — regardless of which repo
the files already on disk actually arrived from. The one-way,
single-source design (§15) holds even when the copy that got here took an
extra hop: a chain-vendored repo gets the same standing mechanisms as one
installed straight from canonical, not a frozen snapshot of whatever its
immediate parent happened to have.

**The Claude credential gets the same clean-skip treatment here as in
§14:** `check` also verifies one is set, and if the pack moved but both
`CLAUDE_CODE_OAUTH_TOKEN` and `ANTHROPIC_API_KEY` are blank, `update` is
skipped with a `note-missing-credential` warning in the run's summary
rather than an auth failure — distinct from a missing `PERSONAL_PACK_TOKEN`,
which stays a silent skip per the paragraph above. Same fallback applies:
a chat session asked to run this sync manually can just take the update
itself, in-session, and should remind the user to set one of the two
Claude credentials afterward.

This section, unlike the rest of this pack, does not itself get vendored
"live" into RepoPersonalPreferences — this repo is the pack's source, so
running a workflow here to check whether the pack has moved from here
would be circular. Only the *template* lives here, at
[templates/github-actions/personal-pack-sync.yml.template](templates/github-actions/personal-pack-sync.yml.template),
for dependent repos to instantiate.

### §17. A new repo's default branch is `main`, set once at install

GitHub only defaults a freshly-created repository to `main` on its own;
plenty of repos predate that default or arrived some other way (an import,
a mirror, an org-level policy) and still sit on `master` or something
else — this repo itself did, until it was fixed by hand (2026-08-21).
At install time (§18 below), check the target repo's current default
branch; if it isn't already `main`, set it once — via the GitHub API's
repo-update endpoint (`PATCH /repos/{owner}/{repo}` with
`default_branch: "main"`) where the session's tools reach that far,
otherwise as a one-click item (**Settings → General → Default branch**,
the pencil icon next to the current default) disclosed in the new repo's
`GETTING_STARTED.md` administrator section like any other click-path
(BestPractice practice 37, [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md)
step 8). One-time per repo — once set, every subsequent clone, PR, and
Actions run already targets `main` on its own, nothing to repeat.

## §18. Installing this pack into a repo

Do this **after** BestPractice itself is installed
([process/upstream/INSTALL.md](../upstream/INSTALL.md) §1) — see
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) for the combined, one-pass
version of both steps.

1. Vendor this directory's tree (not `.git`) to `process/personal/` in the
   target repo, the same way BestPractice itself gets vendored.
2. Weave
   [templates/AGENTS_ADDENDUM.md.template](templates/AGENTS_ADDENDUM.md.template)
   into the target repo's `AGENTS.md`, right after the "Conventions" section,
   and insert its "0c. TODO gate" step into the merge runbook.
3. Install the three workflow templates:
   [templates/github-actions/upstream-sync.yml.template](templates/github-actions/upstream-sync.yml.template)
   → `.github/workflows/bestpractice-upstream-sync.yml`,
   [templates/github-actions/light-check.yml.template](templates/github-actions/light-check.yml.template)
   → `.github/workflows/light-check.yml`, and
   [templates/github-actions/personal-pack-sync.yml.template](templates/github-actions/personal-pack-sync.yml.template)
   → `.github/workflows/personal-pack-sync.yml` (§15 above — needs its own
   secret, disclosed in step 9).
4. Extend `tools/bootstrap.sh` (already installed by BestPractice,
   [INSTALL.md](../upstream/INSTALL.md) §1) with two snippets, run once per
   clone, in this order: the `git config user.name` / `user.email` lines
   from §3 above, then
   [templates/bootstrap-freshness.sh.template](templates/bootstrap-freshness.sh.template)'s
   line — the session-start freshness notice for this pack (§16), skipped
   only when installing on RepoPersonalPreferences itself (§16's
   exemption).
5. Add [process/personal/tools/light_check.py](tools/light_check.py) and
   [process/personal/tools/pack_sync.py](tools/pack_sync.py) to the
   harness's pre-approved command allowlist (for Claude Code:
   `.claude/settings.json`), the same way
   [doc_lint.py](../upstream/tools/doc_lint.py) and
   [practice_audit.py](../upstream/tools/practice_audit.py) already are.
6. Add an entry to `process/manifest_personal.json` for every file installed
   in steps 1-3 (schema: identical to BestPractice's own
   [manifest schema](../upstream/INSTALL.md) §5, with
   `upstream.vendored_at` pointing at `process/personal` in *this* repo).
   The manifest's top-level `upstream.repo` / `upstream.commit` fields are
   a separate thing from these entries — they record where the
   `process/personal/` tree *itself* came from, not any one installed
   file — and get set differently depending on which repo is doing the
   installing: **inside RepoPersonalPreferences itself** (installing the
   pack on itself, as this repo's own `process/manifest_personal.json`
   does), the tree already *is* upstream, so both stay `null`, per the pack
   anatomy rule ([process/upstream/INSTALL.md](../upstream/INSTALL.md) §7).
   **Installing into any other, dependent repo**, set
   `upstream.repo: "https://github.com/themorgan/RepoPersonalPreferences"`
   and `upstream.commit` to this repo's real HEAD commit at install time —
   that repo genuinely depends on a specific commit of this one, and §15's
   sync workflow needs something real to compare against. `scrub_blocklist`
   stays `null` either way (see this repo's own
   [process/manifest_personal.json](../manifest_personal.json) for a worked
   example of the null-both-ways, self-hosting case).
7. Run `python3 process/upstream/tools/practice_audit.py --update-baseline`
   ([practice_audit.py](../upstream/tools/practice_audit.py)) — it audits
   every `process/manifest*.json` it finds, this pack's included, in one
   pass.
8. Check the target repo's default branch (§17 above); if it isn't already
   `main`, set it once now via the API where the session's tools reach
   that far, otherwise add it to the click-path disclosure in the new
   repo's `GETTING_STARTED.md` administrator section
   ([NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8).
9. Disclose the secret step 3's workflow needs, same click-path channel as
   step 8: a repository secret `PERSONAL_PACK_TOKEN` (a GitHub personal
   access token, fine-grained, read-only, scoped to just
   `themorgan/RepoPersonalPreferences`) at the target repo's **Settings →
   Secrets and variables → Actions → New repository secret**. No session's
   tools can mint or set this on Morgan's behalf — say so explicitly in the
   install reply, every time, not just in `GETTING_STARTED.md` (§15 above;
   [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8).

This procedure applies exactly the same way when the target repo already
has some of these pieces present because they arrived via an
already-dependent repo — a fork, a copy, or a chain-vendor — rather than
fresh from the canonical source named in steps 1-4 above. Do steps 1-9 for
whichever pieces are actually missing; don't skip any of them just because
*something* under `process/upstream/` or `process/personal/` is already
there — presence of the tree is not evidence the sync workflows or the
`AGENTS.md` sections came with it. §16's end-of-session check is what
catches this after the fact if it's missed at install time, but an
install session that notices the gap up front should just close it, the
same way it would for a from-scratch install.
