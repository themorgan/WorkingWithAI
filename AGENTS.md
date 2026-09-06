<!-- Last updated: 2026-09-05 21:37:23 (Buenos Aires) by Morgan F, to version 30 -->

# Repository instructions — read me first

**Orientation: read [MAP.md](MAP.md) first** — the repository map. It covers
the brainstorm ([RANDOM_NOTES.md](content/RANDOM_NOTES.md)) and indexes the practice layer that
keeps this repo well-run.

## Where things are (quick index — check here BEFORE searching the repo)

| Looking for… | Go to |
|---|---|
| The theory behind this repo — named, explained, not argued for | [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) |
| The less obvious benefits those ideas produce | [REASONS_WHY.md](content/REASONS_WHY.md) |
| The one-page pitch for why this repo's approach is unique | [THREE_PILLARS.md](content/THREE_PILLARS.md) |
| What humans are good at — the one full list | [HUMANS_AT_OUR_BEST.md](content/HUMANS_AT_OUR_BEST.md) |
| Canonical names — use these, don't invent new ones | [GLOSSARY.md](GLOSSARY.md) |
| The brainstorm itself | [RANDOM_NOTES.md](content/RANDOM_NOTES.md) |
| The three-stage pipeline (idea → rules now testing → company policy) | [README.md](README.md) |
| Rules actually in force now, and promotion candidates | [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) |
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
[`write-like-a-human`](content/RULES_NOW_TESTING.md#write-like-a-human), now
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
   - [TODO.md](TODO.md) and [RANDOM_NOTES.md](content/RANDOM_NOTES.md): **append-only — keep both
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
  [COMPANY_BUILDING_RULES.md](content/COMPANY_BUILDING_RULES.md),
  [AI_GOVERNANCE_TO_COCREATE.md](content/AI_GOVERNANCE_TO_COCREATE.md),
  [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md), [REASONS_WHY.md](content/REASONS_WHY.md),
  [RULES_NOW_TESTING.md](content/RULES_NOW_TESTING.md) — carries its own
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
`python3 tools/precedent_resolve.py --repo .` — this genuinely resolves all
three sources today and reports precedence, shadowing, and the combined
resident-block token budget.

**Gap closed 2026-09-03:** the loading channels that pull a slug's `## Rule`
text into context automatically —
[precedent_show.py](process/upstream/tools/precedent_show.py),
[precedent_paths.py](process/upstream/tools/precedent_paths.py),
[precedent_gate.py](process/upstream/tools/precedent_gate.py) — stay
single-source by design (each hardcodes its own repo as `ROOT`). What closes
the gap is
[tools/precedent_sync_views.py](tools/precedent_sync_views.py): it
materializes every declared source (universal, team, individual, and any
repo-local set) into a real, ordinary `practices/` tree and regenerates the
block below from that same resolved set — the same renderer BestPractice's
own `AGENTS.md` uses on itself. Run
`python3 tools/precedent_sync_views.py --repo .` after any source changes
(a new team/individual practice, a re-vendored universal set); run it with
`--check` to confirm the generated block hasn't drifted from a fresh sync.
Do not hand-edit the block below — the next sync overwrites it.

<!-- BEGIN GENERATED: precedent-loader -->

<!-- Regenerate with: python3 tools/build_views.py -- do not hand-edit this block, tools/verify_harness.py's regeneration check fails on drift. -->

### Resident block (~659 of 2000 token budget, 10 of 107 practices (1 individual, 3 team, 6 universal))

**bold-key-phrases.** People don't read; they skim, and bolding makes skimming easy. Bold the key phrases in a document by default, without being asked, scaling with length -- a long paragraph or document is where a skimmer most needs a spine to follow, a short note usually needs little or none.

**buenos-aires-dates.** Every date is my own Buenos Aires local calendar date, never the session container's system clock and never UTC. Two mechanisms: a prose date (a doc's "as of" note, a last-updated header) uses the Buenos Aires calendar date on the day the text was written; a git commit gets the right offset by running the commit itself under `TZ="America/Argentina/Buenos_Aires"` -- git resolves the offset from `TZ` at commit time, so no manual arithmetic is needed.

**environment-gotchas.** Every expensive environment discovery (a package that must be
installed, a tool that silently doesn't work, a path that does work) is
written into a "do NOT rediscover these" section — with the story of what
failed and why, not just the fix.

**nonblocking-questions.** Once a question is worth asking at all, asking is not itself a stopping point. A session holding a queue of work and an open question doesn't go idle waiting for the answer -- it keeps going on everything the answer doesn't touch.

**orientation-map.** A top-level `MAP.md` indexes the repo: what the key deliverables
are, where everything lives, and — crucially — which supporting documents back
each part of each deliverable. Every session reads it before doing anything.

**quick-index.** The project instructions file carries a "check here BEFORE searching
the repo" table: *looking for X → go to Y*, one row per thing sessions
actually hunt for.

**reply-links-files.** A session's reply that created or modified files ends with a
"Files touched" list: each entry links the file on the working branch *and*
its post-merge location, with a one-line description. The reader must be able
to open the work from the chat, not merely learn it exists.

**repo-is-memory.** Everything a future session needs — orientation, open items,
decisions, lessons — lives in committed files. A session's chat thread is
disposable; if knowledge exists only in a thread, it is already lost.

**small-calls.** Default to continuing, not asking. When a judgment call is needed to keep the work moving -- filling in a default, picking between two reasonable implementations, resolving an ambiguity that doesn't change the shape of what gets delivered -- make the call and note it, rather than stopping to ask first. Reserve stopping and asking for calls that are genuinely big: hard or costly to undo, change what gets delivered or to whom, spend real money, touch credentials or production, or are the kind of toss-up where two reasonable people would clearly land in different places.

**verify-postcondition.** After any state-changing operation, check **the state you wanted**,
not that the command reported success. Name the postcondition before you run
the command — *"no unpushed commits on any branch"*, *"the gate passed"*,
*"the file contains X"* — and then test that, independently of whatever the
command printed.

### Occasion index

```
When a README or other key file just gained an operational instruction:
  mirror-into-agents — an agent-relevant instruction lands in both AGENTS.md and its human home
When a change must propagate across several parallel artifacts:
  parallel-artifact-ledger — ledger the transfer verdict per member, per change
When a commit fixes, closes, or resolves something a document names in prose as a known, open issue:
  resolved-issue-note-updates — When a commit fixes a bug, closes a gap, or resolves a limitation that some ...
When a computation books a transfer between two parties:
  name-both-sides-of-ledger — name both sides; check what is charged against what is received
When a convention is violated for the first time:
  convention-to-audit — promote a costly broken convention to a script that exits non-zero
When a document presents a script-derived figure:
  docs-track-models — every script-derived figure sits inside a generated block
When a document replaces or is replaced by an earlier one:
  index-remembers-past — put the lineage in the index, not in either document
When a new rule is proposed and its scope isn't obvious:
  rule-scope-ask — unclear if a new rule is repo-wide or one document? ask once
When a numbered list's entries are durable content likely to be cited by position:
  durable-list-anchors — anchor and slug each entry of a durable numbered list, not just its number
When a paragraph just got a substantial edit, or the piece is done:
  trim-prose — trim a paragraph right after editing it, and before calling it done
When a person explicitly asks for a full practice audit (or "practice check") across the whole catalogue:
  full-practice-audit — sweep every source's full catalogue, one practice at a time, on request only
When a practice lands or a candidate is raised, at any level:
  disclose-landing — state plainly what happened and where — individual, named team, or universal
When a project of mine vendors a universal practice set as tracked files:
  bestpractice-sync — a scheduled workflow keeps the vendored universal copy current
When a project repo vendors this team's own practice set, and it has moved:
  pack-sync — the team-set sync is the universal sync's sibling, against a private repo
When a review finds a defect:
  mistakes-become-rules — root-cause the miss, then encode the prevention
When a session starts in a repo that vendors a universal or team set:
  drift-notice — check source freshness at session start; raise it right away, not later
When a session-start freshness check against a private source can't be reached:
  fresh-check-escalation — tell "could not verify" apart from "confirmed fresh"; verify directly
When a standing constraint on one file gets stated a second time:
  doc-recipe — present-tense rules for one file, in doc-recipes/<name>.recipe.md
When a tool warns about already-published git history:
  no-rewrite-for-warnings — fix the setting forward; never rewrite published history
When about to commit:
  light-check — a cheap mechanical audit runs before every commit, not just merges
When about to commit a document that characterizes a real, identifiable person:
  sensitive-characterization-scrub — soften or ask before committing a blunt description of a real person
When about to format connected prose as bullet points:
  list-restraint — don't reformat connected reasoning as bullet fragments
When about to push after a thread of work:
  todo-gate — add missed ideas, check off finished ones, before every push
When adding a new rule to a maintained rules document:
  new-rule-placement — place a new rule by subject, slug it, renumber, mirror, re-check
When adding or reviewing a team-set rule:
  no-duplication — a rule that only restates universal gets dropped
When an install step adds something GitHub-specific:
  github-setup-disclosed — disclose GitHub-specific setup where the project's people read
When an unattended scheduled job hits something blocking its normal work:
  automation-issues — a blocked scheduled job opens or updates an issue, not just a log line
When asked for a "deep check" by name, or after drift-inviting work:
  deep-check — every mechanical audit, plus a full read of the repo against itself
When bringing a vendored practice layer into a new or existing repo:
  install — vendor the tree, weave conventions into AGENTS.md, wire checks and manifest
When building a mechanism that makes something discoverable or reachable:
  affordance-is-shared — name who else the mechanism you just built now serves
When building a permutation or configuration-sweep table:
  permutation-frontier-column — one full table with a computed Frontier column
When building a variant of an existing thing:
  variant-re-derives — re-derive what a variant inherits; limits bind, choices do not
When building or committing a generated artifact:
  generated-artifact-provenance — stamp a build code and a manifest; never hand-edit output
When building or setting up a system that talks to an LLM:
  llm-neutral — build LLM integrations provider-neutral; assume an OpenRouter token
When checking whether the practices that should have fired for recent work actually fired:
  routing-audit — run the mechanical coverage check now; roll the deep-read slice forward
When citing support for a claim in a formal document:
  brainstorm-citations — cite a formal document for support, never a raw brainstorm entry
When committing anything:
  session-trailer — a Session: <url> trailer on every commit
When committing anything that touches the vendored/public tree:
  scrub-gate — the public tree is public-safe at all times, not just at check-in
When comparing an option against a baseline:
  check-source-architecture — check both options exist in the source before costing them
When counting or matching entries by name against other entries that may share a prefix:
  match-parsed-id-not-prefix — When counting how many files or entries share a name (recurrence, a duplicat...
When creating a file a later regeneration will overwrite:
  derived-file-marker — a regenerated file's header names its source, recipe, and command
When creating a repo's content/ directory, or migrating a legacy BRAINSTORM.md/NOTES.md/IDEAS.md into the new system:
  assorted-notes — a default content/ASSORTED_NOTES.md holds notes never referenced elsewhere
When deciding where a new rule belongs:
  layered-practice-packs — generic, domain, repo-local — each rule to its own layer
When deciding whether to build or buy a component:
  build-buy-decompose — decompose first; one verdict per part, on ownership grounds
When drafting or reviewing prose meant to persuade or be judged:
  push-back — argue a real counter-case before building on a stated stance
When drafting or revising a list, or a document with list-like sections:
  list-item-parity — keep list items comparable in length; default to the shorter side
When editing a markdown file that carries this header:
  file-header — markdown files get a last-updated/by-me/version header
When ending a reply in which I committed something:
  next-steps-after-commit — after a commit, close the reply by naming what I still need to do
When exporting a tool across a repo boundary:
  engine-plus-host-shims — one vendored engine, thin host shims, never a fork
When finishing a substantial work-product, before the merge-time capture gate:
  second-pass-capture — a separate capture pass after the work, not inside it
When installing Precedent into a project I'll work on from Claude Code Web:
  claude-web-bootstrap — wire the SessionStart hook so this set clones and configures itself
When installing a vendored practice layer that could check in upstream:
  blank-blocklist — leave a check-in blocklist blank at install; don't ask, don't remind
When laying out a repo's root directory, or a root that's grown crowded with agent/tooling files:
  content-directory — put working files in content/ so they don't mix with agent/tooling files
When leaving a placeholder or fill-in-later note mid-draft:
  draft-marker — wrap a draft placeholder in ➡️ TEXT ⬅️, bold and all caps
When making the first commit in a fresh clone or session:
  commit-author — git config user.name/email to Morgan F, don't ask
When mentioning a repo file in a chat reply, PR description, or commit message:
  file-mention-links — every file mention in chat or PR/commit text is a live GitHub link
When merging a branch:
  capture-gate — capture the follow-on work in the thread that created the need
When merging a branch that improved a generic practice:
  practice-export-loop — vendor upstream as tracked files; check improvements back in
When merging a branch that touches shared files:
  merge-runbook — write conflict resolution per file class, once, then follow it
When migrating a repo off an old practice system onto Precedent:
  migration-scrubs-vocabulary — scrub the old system's vocabulary the same session, not on request
When my message ends on the standing merge-authorization phrase:
  go-merge — "Go merge" alone at the end means sync, confirm branch, commit, and merge
When naming a git branch in a document, reply, or status update:
  branch-links — link every git branch mentioned to its tree view
When naming a new file:
  no-version-suffix — name a file for what it is; the repository is the version
When naming anything that has a destination, in a document or a reply:
  rule-links — link anything mentioned that has a destination, on first use
When naming what "run the checks" means in a repo:
  two-check-levels — name a fast check and a full check; say which gates what
When ordering sections in a document:
  section-order-by-frequency — order sections by how often the reader needs them
When printing a numeric quantity that will be compared across rows:
  one-formatter-per-quantity — one formatter per quantity kind, declared in one module
When publishing a document with a multi-column sortable table:
  tabular-shared-renderer — ship a sortable render from the one shared renderer
When quoting or compressing someone else's figures:
  quote-discipline — compression rounds against you; qualifiers travel with the figure
When reporting a check's outcome that includes a known pre-existing backlog:
  quiet-checks — "checks passed" is fine; don't re-explain the same old backlog
When reporting a computed total or a negative feasibility result:
  verify-decomposition — check the parts, not the total; never assert an impossibility
When reviewing a draft's balance before calling it done:
  proportional-emphasis — give a point space matching its importance, not its drafting mood
When root has accumulated three or more deliverable-content documents:
  content-subdirs — group deliverable content under a named subdirectory -- a recommendation
When setting up a new repo's session start:
  session-bootstrap — setup lives in a session-start hook, not in memory
When setting up a new repo, or installing into an existing one:
  default-branch — check or set the default branch to main, once, at install
When starting an outward-facing deliverable:
  frame-from-audience-question — build it around the audience's question, not your material
When starting work the repository may already cover:
  search-by-purpose — search by purpose and by mechanism before concluding nothing exists
When tracking state that multiple documents need to agree on:
  registry-source-of-truth — state lives in one machine-readable registry; documents derive
When writing a README or other project-facing entry document:
  lead-with-what-it-is — say what the project is before how it is maintained
When writing a document that cites a computed number:
  computed-numbers-in-scripts — computed content lives in a sync-gated generated block
When writing a new convention or rule:
  checkable-gets-checked — attempt a mechanical check before leaving a new practice advisory-only
  cite-the-incident — record the failure a rule prevents, inline with the rule
When writing a reader-facing deliverable with supporting apparatus:
  deliverables-look-like-output — the deliverable holds only what its audience needs
When writing a rule that depends on the outside world:
  volatile-rules-carry-dates — a rule about the outside world carries its date, inline
When writing a script whose numbers a document will cite:
  scripts-assert-properties — scripts assert their own properties and their cited anchors
When writing a sentence that cites an exact, changeable count:
  no-stale-counts — drop a count that will go stale; say "several", not the number
When writing an outward-facing document:
  readers-vocabulary — use the reader's words; gloss inline or replace
When writing an outward-facing summary of claims:
  outward-summary-discipline — claims-to-source table, honest sums, a recorded adversarial pass
When writing code because a specific practice requires it:
  code-cites-practice — cite the practice's slug in a comment, right where the code is
When writing code that depends on something outside its own control:
  fail-gracefully — degrade on a missing config, file, network call, or credential
When writing content that will vendor or ship into another repo:
  private-repo-scrub — name a private repo only in general terms in anything that ships elsewhere
When writing or editing a document:
  acronyms-glossary — expand acronyms on first use; keep one central glossary
  docs-are-current-state — state what is true now; version control holds the history
  label-describes-content — "one line" must be one line; else name it for its content
When writing or filling out a pull-request description:
  pr-template-honest-gates — write the body from the diff; an unchecked box is fine
When writing or reviewing a document's headers:
  header-caps — one capitalization schema per document; default to headline style
When writing or triaging an open item:
  todo-is-a-handoff — queue only for a stated blocked-on/out-of-scope reason — otherwise just do it
```

### Standing instruction

Before starting work of a kind named in the occasion index above, run `python3 tools/precedent_show.py SLUG` for each listed slug to load its Rule. When editing a file, `python3 tools/precedent_paths.py FILE` prints any on-demand practice whose `applies_to` matches it, without needing the index at all. At a named moment — merging, reviewing, pushing, ending a turn — run `python3 tools/precedent_gate.py merge|review|push|reply`: some practices fire at a moment rather than in a file, and no path glob reaches those.

<!-- END GENERATED -->

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
  reports 63 SCRUB failures inside `process/upstream/` itself — a real,
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
