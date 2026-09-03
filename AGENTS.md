<!-- Last updated: 2026-09-03 11:05:52 (Buenos Aires) by Morgan F, to version 26 -->

# Repository instructions — read me first

**Orientation: read [MAP.md](MAP.md) first** — the repository map. It covers
the brainstorm ([RANDOM_NOTES.md](docs-team/RANDOM_NOTES.md)) and indexes the practice layer that
keeps this repo well-run.

## Where things are (quick index — check here BEFORE searching the repo)

| Looking for… | Go to |
|---|---|
| The theory behind this repo — named, explained, not argued for | [OUR_PHILOSOPHY.md](docs-team/OUR_PHILOSOPHY.md) |
| The less obvious benefits those ideas produce | [REASONS_WHY.md](docs-team/REASONS_WHY.md) |
| The one-page pitch for why this repo's approach is unique | [THE_REVOLUTIONARY_FORMULA.md](docs-team/THE_REVOLUTIONARY_FORMULA.md) |
| What humans are good at — the one full list | [HUMANS_AT_OUR_BEST.md](docs-team/HUMANS_AT_OUR_BEST.md) |
| Canonical names — use these, don't invent new ones | [GLOSSARY.md](GLOSSARY.md) |
| The brainstorm itself | [RANDOM_NOTES.md](docs-team/RANDOM_NOTES.md) |
| The three-stage pipeline (idea → rules now testing → company policy) | [README.md](README.md) |
| Rules actually in force now, and promotion candidates | [RULES_NOW_TESTING.md](docs-team/RULES_NOW_TESTING.md) |
| The voice guidelines (write like a human, not an LLM) | [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) |
| Open items: analyses, verifications, decisions | [TODO.md](TODO.md) |
| Practice layer: vendored BestPractice copy, `precedent.json` sources, scrub blocklist | `process/`, [precedent.json](precedent.json) |
| How this repo migrated from BestPractice-only to Precedent's three-source model (2026-09-02 beta test), and what still doesn't work | [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md) |

## Voice — every reply and every document

This repo's own writing follows
[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md),
vendored from
[SoundHuman](https://github.com/themorgan/SoundHuman)
(tracked in [process/manifest_voice.json](process/manifest_voice.json), kept
current by a weekly sync plus a session-start check — see
[GETTING_STARTED.md](GETTING_STARTED.md)'s "A second scheduled check keeps
the voice guidelines current"). It governs **everything a
session writes here, not just committed documents** — the chat reply itself
is in scope too. Check outward-facing prose against it before calling a
piece done; this is
[`write-like-a-human`](docs-team/RULES_NOW_TESTING.md#write-like-a-human), now
backed by a real, vendored ruleset instead of a manual checklist.
HUMAN_VOICE_RULES.md's own §17 sets the precedence rule if that ever
conflicts with a more specific, person-authored voice pack: the
person-specific rules win.

## Build-environment gotchas — do NOT rediscover these

- At session start, run `bash tools/bootstrap.sh` before other work (Claude
  Code runs it automatically via the SessionStart hook — see
  `.claude/settings.json`).
- **A brand-new Claude Code Remote/Cloud session started on this repo alone
  does not automatically have git read access to `precedent-team-maintainers`
  or `precedent-individual`** — the team and individual sources
  `precedent.json` and the individual bootstrap hook depend on. Session
  repo access is scoped per session (attached at session creation, or added
  mid-session with the `add_repo` tool); it isn't inherited just because a
  file references a repo by name. **No token or secret is involved** —
  `add_repo` extends the session's scope using the same GitHub identity
  already behind the session, so it only ever succeeds because that
  identity (Morgan's own GitHub account) is already a collaborator on both
  target repos, exactly as it is today; there is nothing to configure or
  store to make this work.
  **This step must never wait for a human to notice or ask: at the very
  start of every session on this repo, before running `tools/bootstrap.sh`,
  call `add_repo` (read access) for `themorgan/precedent-team-maintainers`
  and, if this is Morgan, `themorgan/precedent-individual` — silently, with
  no confirmation needed first.** This is a read-only scope extension, not
  a credential or production change, so it's exactly the kind of call
  [`small-calls`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/small-calls.md)
  (team source) says to just make. A person only ever attaches the one
  repo they're actually working in (`WorkingWithAI`); reaching for the
  other two is this session's own job, every single time, not something
  set up once and assumed to stick — repo access, like everything else
  under "Repository Scope," is a per-session grant that does not persist
  to the next session.
  - **Individual** (`precedent-individual`): once added,
    `.claude/hooks/precedent-individual-bootstrap.sh` clones (or pulls) it
    and writes the user config automatically, every session.
  - **Team** (`precedent-team-maintainers`): once added, `tools/bootstrap.sh`
    clones it (to `../precedent-team-maintainers`) if it isn't already
    there, or fast-forward pulls it if it is. Its clone URL is hardcoded in
    that script as WorkingWithAI's own currently-real fact (not derived
    from `precedent.json`, which never records a git URL — see the
    script's own comment for the tradeoff that creates: if the team source
    ever changes repos, the script's URL has to be updated by hand to
    match).
  - **Either one:** if `add_repo` itself fails (the acting GitHub identity
    genuinely lacks access), or `tools/bootstrap.sh` still prints a
    "could not clone" note afterward, or `precedent_resolve.py` reports a
    source as missing — that is a real access gap, not something a retry
    fixes: say so plainly and move on; individual/team practices are just
    silently not in force that session. Declaring or cloning either source
    is **read-only and one-directional**: it lets this repo's session read
    their practices, and does not grant anyone with access to those repos
    — Alex included — any access back to this repo. That's governed
    entirely by `themorgan/WorkingWithAI`'s own GitHub collaborator
    settings, unrelated to `precedent.json`.

## Git / workflow

- Develop on a feature branch; open a PR; merge only when the user says so
  (except the BestPractice sync and the voice guidelines sync, which merge
  their own PRs unattended — see
  [`bestpractice-sync`](https://github.com/themorgan/precedent-individual/blob/main/practices/bestpractice-sync.md)
  (it's Morgan's own preference about his own projects' automation, not a
  convention Alex separately agreed to for his; see that practice's own
  `## Story`) and [GETTING_STARTED.md](GETTING_STARTED.md)'s "A second
  scheduled check keeps the voice guidelines current"; the BestPractice
  sync itself is paused for the duration of the precedent-beta-v01 beta
  test, see [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)).
- **Start every thread by merging latest `origin/main` into your branch.**
- **Then catch the member up.** Summarize what changed on `origin/main`
  since the last session, including anything any of the three syncs merged
  unattended. Do the same any time she asks "what's new?".

(Session start, in order: call `add_repo` for the two sibling practice
repos — see "Build-environment gotchas" above, no asking first — then
`bash tools/bootstrap.sh`, then these two.)

### Merging a thread branch (runbook — follow, don't improvise)

Conflicts in shared files are EXPECTED. The fast, safe path:

0. **Capture gate — before the merge, in the thread that did the work**
   ([practice 10](process/upstream/PRACTICES.md#10-capture-in-the-thread-that-created-the-need--before-the-merge)):
   did this thread's work imply anything that must be
   captured — a document update, a registry entry, a decision record? Fold
   it now.
   **0b. Export gate** ([practice 14](process/upstream/PRACTICES.md#14-the-practice-export-loop-how-this-repo-propagates)):
   did this thread improve a *generic* BestPractice practice? Fold the
   abstracted form into `process/upstream/` now, per
   [process/upstream/INSTALL.md](process/upstream/INSTALL.md) §3, and run
   the scrub audit.
   **0c. TODO gate** ([`todo-gate`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/todo-gate.md))**:** re-read this thread's discussion
   against [TODO.md](TODO.md) — add any idea that came up but never got a
   line; remove or check off anything this branch just implemented. Do
   this every push.
1. Fetch and merge `main` locally.
2. Resolve by fixed per-file-class rules ([practice 9](process/upstream/PRACTICES.md#9-a-merge-runbook-with-fixed-per-file-class-rules)):
   - `process/manifest.json` / `process/manifest_voice.json` / `precedent.json`:
     **union** of both sides — never drop an entry, a status, or a source.
   - [TODO.md](TODO.md) and [RANDOM_NOTES.md](docs-team/RANDOM_NOTES.md): **append-only — keep both
     sides' additions.**
   - Same content file edited on both sides: keep both sides' text.
   - **`process/upstream/`: never hand-merge.** It must stay byte-identical
     to whatever [checkin.py](process/upstream/tools/checkin.py) `update`
     last mirrored — resolve by re-running the sync
     ([INSTALL.md](process/upstream/INSTALL.md) §2), not by editing
     vendored files directly. (Paused for the precedent-beta-v01 beta —
     see [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md).)
   - **[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md): never hand-merge either,** same
     reasoning — it must stay byte-identical to whatever
     [voice_sync.py](process/voice/tools/voice_sync.py) `update` last
     mirrored from SoundHuman; resolve by re-running that
     sync, not by editing the file directly.
   - **Nothing under `process/personal/` should ever appear again** — that
     path is retired; a merge that still has changes queued against it
     predates [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)
     and needs that record read before resolving it.
3. Run the audits — **all must pass before the merge commits**:
   `python3 process/upstream/tools/doc_lint.py`,
   `python3 tools/light_check.py`, and
   `python3 process/upstream/tools/practice_audit.py`. A plain "checks
   passed" is fine; skip re-explaining the same known pre-existing backlog
   every time — a run that actually fails, or a warning your own edit
   newly introduced, is always worth flagging
   ([`quiet-checks`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/quiet-checks.md)).
4. Commit the merge, push, land per this repo's convention.

## Conventions

- **Sections are ordered by the reader's frequency, not the writer's**
  ([practice 36](process/upstream/PRACTICES.md#36-section-order-follows-the-readers-frequency-not-the-writers-derivation-order)):
  a document walking through rules in multiple sections puts
  common, everyday content first and rare edge cases / contingencies last,
  unless the subject matter dictates otherwise. Ask: would most readers
  have to scroll past this section to reach the one they opened the
  document for?
- **PR descriptions come from the diff, not the template** ([practice 39](process/upstream/PRACTICES.md#39-a-default-pr-template-captures-the-living-doc-gates--honestly-not-mechanically)):
  write "What changed" / "Why" / "Files touched" from what actually
  happened on this branch. Check a `## Gates` box only when it is actually
  true for this change — an unchecked box, or a "not applicable" note, is
  normal. Never check every box just to make the form look complete.
- **Doc references are links** ([practice 11](process/upstream/PRACTICES.md#11-document-references-are-links-approximation-is)):
  relative markdown links, never bare backticked filenames.
- **A durable numbered list is cited by permanent slug, never by
  position** ([`durable-list-anchors`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/durable-list-anchors.md)):
  every rule or item in this repo's own essay lists —
  [COMPANY_BUILDING_RULES.md](docs-team/COMPANY_BUILDING_RULES.md),
  [AI_GOVERNANCE_TO_COCREATE.md](docs-team/AI_GOVERNANCE_TO_COCREATE.md),
  [OUR_PHILOSOPHY.md](docs-team/OUR_PHILOSOPHY.md), [REASONS_WHY.md](docs-team/REASONS_WHY.md),
  [RULES_NOW_TESTING.md](docs-team/RULES_NOW_TESTING.md) — carries its own
  `<a id="slug"></a>` anchor, cited everywhere as
  `` `slug` (file.md#slug) ``, never as a bare "rule 4" or "item 3". This
  supersedes the older split between "anchored when the source list uses
  real headings" and "linked to the bare file when it doesn't" — every one
  of these lists gets an explicit anchor now, headed or not, since even a
  heading's own GitHub-auto-generated anchor bakes in the position number
  and breaks the same way on renumbering. A short bullet list (not one of
  the four lists above) doesn't need this. Use `≈`, not `~`, for
  "approximately".
  `python3 process/upstream/tools/doc_lint.py` checks link conventions on
  files changed vs the default branch; run it on what you touch before
  committing.
- **Volatile rules carry their dates** ([practice 16](process/upstream/PRACTICES.md#16-volatile-rules-carry-their-dates)):
  anything asserted
  here about an external platform or tool carries *as of / verified
  `<date>`* inline, in Buenos Aires local time
  ([`buenos-aires-dates`](https://github.com/themorgan/precedent-individual/blob/main/practices/buenos-aires-dates.md)), stricter
  than BestPractice's own default of "the contributor's local calendar
  date" — here, the contributor's local calendar date always means Buenos
  Aires, regardless of where a session physically runs).
- **Outward-facing documents use the reader's words** ([practice 34](process/upstream/PRACTICES.md#34-outward-facing-documents-use-the-readers-vocabulary-not-the-sources)):
  this
  repo's README and [GETTING_STARTED.md](GETTING_STARTED.md) are read by
  people who are not developers. Terms that name a category are the
  reader's word, a plain equivalent, or glossed inline — never left to a
  glossary. Jargon arrives from the sources a session just read, so run
  the check as a separate pass after drafting.
- **Reply convention** ([practice 12](process/upstream/PRACTICES.md#12-every-reply-links-the-files-it-touched)):
  every reply that created or modified
  files ends with a "Files touched" list — branch link + post-merge link +
  one-line description per file. A touched HTML render or picture also
  gets its rendered-view (artifact) link when the harness offers one — a
  repo link shows source, not the render.

## Practice sources (Precedent)

This repo resolves practices from three sources, per
[Precedent](https://github.com/alex137/BestPractice/tree/precedent-beta-v01)'s
three-source model (migration history, for anyone curious how this repo
got here from a single vendored pack: [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)).
**New session and team/individual practices don't seem to apply? Read
"Build-environment gotchas" above first** — this almost always means the
session doesn't have repo access to precedent-team-maintainers or
precedent-individual yet, not a bug in the resolver.

- **Universal** — [process/upstream/PRACTICES.md](process/upstream/PRACTICES.md).
  Still a physical vendored copy, tracked by
  [process/manifest.json](process/manifest.json), exactly as before (see
  "Practice export" below) — unchanged by this migration except which
  branch it tracks.
- **Team** — [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers)
  (Morgan and Alex's own conventions; migrated from RepoPersonalPreferences).
  Declared in [precedent.json](precedent.json), resolved live from a sibling
  clone (`../precedent-team-maintainers`) rather than vendored.
- **Individual** — [precedent-individual](https://github.com/themorgan/precedent-individual)
  (Morgan's own person-specific facts: commit identity, Buenos Aires as his
  timezone, file-header naming, the `go`/`merge` shorthand). **Never**
  declared in this repo's own tracked config — naming it here would leak
  its existence and location to anyone with read access to this repo, which
  is exactly the leak the three-source split exists to prevent. It resolves
  instead from Morgan's own user-level config
  (`~/.config/precedent/config.json`), which
  [.claude/hooks/precedent-individual-bootstrap.sh](.claude/hooks/precedent-individual-bootstrap.sh)
  clones and writes automatically at the start of every Claude Code Web
  session on this repo, before the first tool call — nobody runs a command
  by hand for this.

**To see the full merged, in-force rule set:**
`python3 process/upstream/tools/precedent_resolve.py --repo .` — this
genuinely resolves all three sources today and reports precedence,
shadowing, and the combined resident-block token budget.

**Known gap, as of this beta (2026-09-02):** the loading channels that pull
a slug's `## Rule` text into context automatically —
`precedent_show.py`, `precedent_paths.py`, `precedent_gate.py` — are
single-source on the precedent-beta-v01 branch and only ever read
`process/upstream/practices/`; there is no built extractor yet for a team
or individual slug, so nothing here yet regenerates this section's content
automatically the way BestPractice's own `AGENTS.md` resident block is
generated. Until that lands, open the practice file directly —
`<sibling clone>/practices/<slug>.md` — and read its `## Rule` section. The
two lists below are a hand-curated stopgap for exactly that reason: the
short `## Rule` text of the practices this repo's sessions need most often,
so day-to-day work doesn't depend on that gap closing first. They are not
the full catalogue — run the resolve command above, or open the source
repos directly, for anything not listed here.

### Always in force (resident, across every source)

- **buenos-aires-dates** (individual). Every date is Morgan's own Buenos
  Aires local calendar date, never the session container's system clock and
  never UTC. Two mechanisms: a prose date (a doc's "as of" note, a
  last-updated header) uses the Buenos Aires calendar date on the day the
  text was written; a git commit gets the right offset by running the
  commit itself under `TZ="America/Argentina/Buenos_Aires"`.
- **small-calls** (team). Default to continuing, not asking. When a
  judgment call is needed to keep the work moving, make the call and note
  it, rather than stopping to ask first. Reserve stopping and asking for
  calls that are genuinely big: hard or costly to undo, change what gets
  delivered or to whom, spend real money, touch credentials or production,
  or a toss-up two reasonable people would clearly land differently on.
- **nonblocking-questions** (team). Once a question is worth asking at all,
  asking is not itself a stopping point. A session holding a queue of work
  and an open question doesn't go idle waiting for the answer — it keeps
  going on everything the answer doesn't touch.
- **bold-key-phrases** (team). Bold the key phrases in a document by
  default, without being asked, scaling with length.

### On demand, frequently needed in this repo

- **commit-author** (individual). `git config user.name "Morgan F"` and
  `git config user.email "morgan@westegg.com"` once per clone
  ([tools/bootstrap.sh](tools/bootstrap.sh) does this automatically),
  before the first commit — don't ask who the author is first.
  BestPractice's own `Co-Authored-By:` trailer naming the assistant still
  applies; this replaces only the identity half.
- **go-merge** (individual). If Morgan's message, at a point where you've
  said you're ready, ends with `go`, `merge`, or `PR & merge` standing
  alone as its own sentence (case-insensitive), treat it as authorization,
  right there, to commit the pending work and merge it, using this repo's
  usual conventions, without asking again first.
- **file-header** (individual). A markdown file Morgan maintains gets
  `<!-- Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by Morgan F, to
  version N -->` as its first line — a full timestamp, not just a date. `N`
  is a plain integer counter private to that file: 1 the first time the
  header is added, +1 each subsequent content change.
- **session-trailer** (team). A `Session: <url>` trailer on every commit —
  for Claude Code, `https://claude.ai/code/session_<ID>`. For unattended
  automation with no chat session behind it, the workflow run's own URL
  stands in; if a tool has no shareable link at all, say so explicitly
  (`Session: none available (<tool>)`).
- **todo-gate** (team). Before pushing, check the thread's discussion
  against [TODO.md](TODO.md): add any idea that came up but never got a
  line, remove or check off anything this branch just implemented.
- **rule-links** (team). Anything mentioned that has a destination gets a
  link to that destination, the first time it's mentioned — in any
  document, a commit message, a PR description, or a reply in chat (the
  one people forget).
- **doc-recipe** (team). A recipe is the spec for one file: what the next
  pass should produce, or how a document is always to be written — present
  tense and rewritable, never a history (history lives in `git log` and
  this repo's own decision records). Recipes for this repo's own documents
  live in `doc-recipes/` and `docs-team/doc-recipes/`.
- **private-repo-scrub** (team, `severity: blocking`). Anything that ships
  into another repo describes the situation that prompted a rule only in
  general terms, never by a private repo's real name, URL, or identifying
  layout details. Doesn't reach content that never leaves this repo — its
  own decision records, [TODO.md](TODO.md), commit messages — which can and
  should keep naming the real repo.
- **sensitive-characterization-scrub** (team). Before anything actually
  gets committed that describes a real, identifiable person candidly or
  strongly, assume they may eventually read it themselves — soften it, or
  ask first, rather than committing it as given.
- **mirror-into-agents** (team). When a README, `CONTRIBUTING.md`,
  [GETTING_STARTED.md](GETTING_STARTED.md), or any other key file gains an
  operational instruction useful for an agent to know, fold the same
  instruction into this `AGENTS.md` too. Runs both directions.
- **deep-check** (team). A deep check has two halves: every audit script
  the repo maintains, run together (the merge runbook's mechanical half,
  not optional); and a read of the repo's own rules and documents against
  each other for contradictions or drift the audits can't catch. Run it
  when Morgan asks for a "deep check" by name, or after work that invites
  drift.
- **quiet-checks** (team, linked above in the merge runbook). Don't repeat
  the same pre-existing-backlog explanation every run — a plain "checks
  passed" is fine; a run that actually fails, or a warning your own edit
  newly introduces, is always worth flagging.
- **light-check** (team). This repo's own copy lives at
  [tools/light_check.py](tools/light_check.py) — see that practice's own
  Detail section on why each vendoring repo keeps its own rather than
  inheriting a shared one — run on every commit path via
  [.github/workflows/light-check.yml](.github/workflows/light-check.yml).

The team source carries many more rules than the hand-curated stopgap list
above — deliberately not restated here, per
[`no-duplication`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/no-duplication.md):
don't restate a resolved source. Run `python3 process/upstream/tools/precedent_resolve.py --repo .`
for the full, current set.

### Scheduled syncs

- **BestPractice sync**
  ([.github/workflows/bestpractice-upstream-sync.yml](.github/workflows/bestpractice-upstream-sync.yml)):
  unattended, weekly by default, takes an upstream BestPractice update and
  merges it. **Paused** (schedule commented out, `workflow_dispatch` only)
  for the duration of the precedent-beta-v01 beta test — see the workflow's
  own header comment and
  [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md).
- **Team and individual sources are resolved live from sibling clones, not
  vendored-and-synced by a scheduled workflow** — keeping those sibling
  clones themselves current is `tools/bootstrap.sh`'s job (a best-effort
  `git pull --ff-only` at session start for the team clone; the individual
  clone's own bootstrap hook does the same for itself), not a GitHub
  Actions workflow.
- **Voice guidelines sync**
  ([.github/workflows/voice-guidelines-sync.yml](.github/workflows/voice-guidelines-sync.yml)):
  unrelated source (SoundHuman), same shape as the BestPractice sync above,
  still active weekly. Needs its own repository secret,
  `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN`.
- **Unattended automation reports its own blockers as a GitHub issue, not
  only a log line** — [tools/report_automation_issue.py](tools/report_automation_issue.py),
  a generic utility, per
  [`automation-issues`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/automation-issues.md).
- **Both remaining scheduled syncs skip cleanly, not loudly, when neither
  Claude credential is set.** If asked to run one manually, no secret is
  needed — take the update in-session, then remind Morgan to set one so
  future unattended runs don't need to be asked for by hand.

## Working in parallel (multi-member repos)

Single-member today (just Morgan) — these conventions stay installed per
BestPractice's own template guidance, ready the moment a second person or
assistant works this repo, rather than being retrofitted later.

- **Claim before you start.** When taking on a [TODO.md](TODO.md) item,
  mark it claimed — *(claimed: NAME, date, branch)* — as the branch's first
  commit. Check [TODO.md](TODO.md) claims and open branches/PRs for overlap
  before starting.
- **Flag changes to the people they matter to.** Commits are credited to
  the human driving them, so the history says whose work a diff reworks.

### Review sensitivities (accumulated)

## Administrator requests you must know how to handle

- **"What's waiting for me?"** List open PRs and branches ahead of `main`
  with no PR yet; summarize each in plain language; merge only what's
  approved in conversation.
- **"Add project members"** — ask for their GitHub username, what they'll
  work on, and which AI tool they use; grant access at this repo's
  **Settings → Collaborators → Add people**; point them at
  [GETTING_STARTED.md](GETTING_STARTED.md).

## Practice export — BestPractice (policy)

- `process/upstream/` is a vendored copy of the public
  [BestPractice](https://github.com/alex137/BestPractice) repo, tracked in
  this repo (currently the `precedent-beta-v01` branch, not `main` — a
  deliberate beta-test pin, see
  [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)).
  **Public-safe invariant:** nothing proprietary may appear under
  `process/upstream/`, ever.
  `python3 process/upstream/tools/practice_audit.py`
  ([practice_audit.py](process/upstream/tools/practice_audit.py)) enforces
  this against
  [process/scrub_blocklist.txt](process/scrub_blocklist.txt) and must pass
  before committing anything that touches `process/`. **Known exception,
  as of the precedent-beta-v01 vendor (2026-09-03):** this currently
  reports 62 SCRUB failures inside `process/upstream/` itself — a real,
  understood collision, not a leak; see
  [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md)'s "A
  real finding" section before treating a fresh run of this audit as
  broken or trying to "fix" it by editing the vendored tree.
- The team and individual sources
  ([precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers),
  [precedent-individual](https://github.com/themorgan/precedent-individual))
  are never vendored into this repo at all (see "Practice sources
  (Precedent)" above) — there is nothing under either name here to export
  from or scrub. Improving one of those sets happens directly in its own
  repo, in a separate session with access to it.
- Export gate = merge runbook step 0b, for `process/upstream/` only.
  Periodic check-in per [process/upstream/INSTALL.md](process/upstream/INSTALL.md)
  §4 (recurring item in [TODO.md](TODO.md)) — in practice this repo mostly
  consumes BestPractice rather than improving it, and is paused for the
  duration of the beta (same reason as the sync above: `checkin.py`'s
  commands assume default-branch tracking).
- [process/manifest.json](process/manifest.json) is the installed-practices
  registry for `process/upstream/`; when a vendored file changes locally,
  export + re-baseline, or flip the entry to `diverged`.
  [precedent.json](precedent.json) plays the analogous role for the team
  source, but as a source *declaration* (a path to resolve live), not a
  per-file manifest — there is nothing to re-baseline there, only the path
  and level.
