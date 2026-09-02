<!-- Last updated: 2026-09-01 22:52:50 (Buenos Aires) by Morgan F, to version 18 -->

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
| Practice layer: vendored BestPractice copy, manifest, scrub blocklist | `process/` |

## Voice — every reply and every document

This repo's own writing follows
[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md),
vendored from
[SoundHuman](https://github.com/themorgan/SoundHuman)
(tracked in [process/manifest_voice.json](process/manifest_voice.json), kept
current by a weekly sync plus a session-start check — see "A third scheduled
check keeps the voice guidelines current" below). It governs **everything a
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

## Git / workflow

- Develop on a feature branch; open a PR; merge only when the user says so
  (except the BestPractice sync, the pack sync, and the voice guidelines
  sync, which merge their own PRs unattended — see
  [`bestpractice-sync`](process/personal/README.md#bestpractice-sync),
  [`pack-sync`](process/personal/README.md#pack-sync), and
  this file's "A third scheduled check keeps the voice guidelines current"
  below).
- **Start every thread by merging latest `origin/main` into your branch.**
- **Then catch the member up.** Summarize what changed on `origin/main`
  since the last session, including anything any of the three syncs merged
  unattended. Do the same any time she asks "what's new?".

(Session start, in order: `bash tools/bootstrap.sh` — see "Build-environment
gotchas" above — then these two.)

### Merging a thread branch (runbook — follow, don't improvise)

Conflicts in shared files are EXPECTED. The fast, safe path:

0. **Capture gate — before the merge, in the thread that did the work**
   ([practice 10](process/upstream/PRACTICES.md#10-capture-in-the-thread-that-created-the-need--before-the-merge)):
   did this thread's work imply anything that must be
   captured — a document update, a registry entry, a decision record? Fold
   it now.
   **0b. Export gate** ([practice 14](process/upstream/PRACTICES.md#14-the-practice-export-loop-how-this-repo-propagates)):
   did this thread improve a *generic*
   BestPractice practice (not the personal pack, which never exports)?
   Fold the abstracted form into `process/upstream/` now, per
   [process/upstream/INSTALL.md](process/upstream/INSTALL.md) §3, and run
   the scrub audit.
   **0c. TODO gate** ([`todo-gate`](process/personal/README.md#todo-gate))**:** re-read this thread's discussion
   against [TODO.md](TODO.md) — add any idea that came up but never got a
   line; remove or check off anything this branch just implemented. Do
   this every push.
1. Fetch and merge `main` locally.
2. Resolve by fixed per-file-class rules ([practice 9](process/upstream/PRACTICES.md#9-a-merge-runbook-with-fixed-per-file-class-rules)):
   - `process/manifest.json` / `process/manifest_personal.json` /
     `process/manifest_voice.json`: **union** of both sides — never drop an
     entry or a status.
   - [TODO.md](TODO.md) and [RANDOM_NOTES.md](docs-team/RANDOM_NOTES.md): **append-only — keep both
     sides' additions.**
   - Same content file edited on both sides: keep both sides' text.
   - **`process/upstream/`: never hand-merge.** It must stay byte-identical
     to whatever [checkin.py](process/upstream/tools/checkin.py) `update`
     last mirrored — resolve by re-running the sync
     ([INSTALL.md](process/upstream/INSTALL.md) §2), not by editing
     vendored files directly.
   - **`process/personal/`: never hand-merge either.** It must stay
     byte-identical to whatever
     [pack_sync.py](process/personal/tools/pack_sync.py) `update` last
     mirrored — resolve by re-running that sync
     ([`pack-sync`](process/personal/README.md#pack-sync)).
   - **[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md): never hand-merge either,** same
     reasoning — it must stay byte-identical to whatever
     [voice_sync.py](process/voice/tools/voice_sync.py) `update` last
     mirrored from SoundHuman; resolve by re-running that
     sync, not by editing the file directly.
3. Run the audits — **all must pass before the merge commits**:
   `python3 process/upstream/tools/doc_lint.py`,
   `python3 process/personal/tools/light_check.py`, and
   `python3 process/upstream/tools/practice_audit.py`. A plain "checks
   passed" is fine; skip re-explaining the same known pre-existing backlog
   every time — a run that actually fails, or a warning your own edit
   newly introduced, is always worth flagging
   ([`quiet-checks`](process/personal/README.md#quiet-checks)).
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
  position** ([`durable-list-anchors`](process/personal/README.md#durable-list-anchors)):
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
  ([`buenos-aires-dates`](process/personal/README.md#buenos-aires-dates)), stricter
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

## Personal setup rules (Morgan's pack)

These extend BestPractice's own conventions above; they are this repo's
personal layer (`process/personal/`), not upstream BestPractice, and they
never get exported to the public BestPractice repo.

- **On conflict with BestPractice, this pack wins.** BestPractice sets the
  default; where a rule here and a rule of BestPractice's own genuinely
  disagree on the same point, this pack's rule governs. Where this pack is
  silent, BestPractice's own rule stands undisturbed — this pack only
  narrows or overrides where it actually speaks
  ([`bestpractice-wins`](process/personal/README.md#bestpractice-wins)).

- **Don't duplicate BestPractice.** This pack exists to add to BestPractice
  or override it, not restate it. A bullet here that only repeats what
  BestPractice already establishes on its own gets dropped the next time
  this file is touched, rather than left as a second copy that can drift
  out of sync with the first
  ([`no-duplication`](process/personal/README.md#no-duplication)).

- **The identity facts below are about Morgan specifically — they apply
  only when Morgan is the one actually driving the change.** The
  `git config user.name`/`user.email` identity (below), Buenos Aires as
  the timezone for dates and commit timestamps (below), "Morgan F" as the
  `NAME` in a file's last-updated header (below), the `themorgan` GitHub
  attribution, Morgan's own he/him pronouns, and the `go`/`merge`
  shorthand (further below) are facts about one person, not defaults for
  whoever happens to be committing. When a different GitHub user or person
  drives a change in this repo — co-authoring, running their own session,
  opening their own PR — none of this carries over automatically: don't
  attribute their commits to "Morgan F", don't assume their timezone is
  Buenos Aires, don't refer to them as "he" absent them saying so, and
  don't require the exact "go"/"merge" wording from them. Fall back to
  BestPractice's own generic default instead (ask, don't assume) for
  anyone who isn't Morgan
  ([`morgan-scope`](process/personal/README.md#morgan-scope)). Each bullet
  below that states one of these facts carries a short pointer back to
  this one.

- **Commits are always authored "Morgan F".** Use Morgan's own email
  address:
  `git config user.name "Morgan F"` and
  `git config user.email "morgan@westegg.com"`
  once per clone ([tools/bootstrap.sh](tools/bootstrap.sh) does this
  automatically). This replaces, rather than defers to, BestPractice's own
  "ask before the first commit" default — the identity is already decided,
  so don't ask. It replaces only the *identity* half: the pack says nothing
  about co-authorship, so BestPractice's own `Co-Authored-By:` trailer
  naming the assistant still applies
  ([`bestpractice-wins`](process/personal/README.md#bestpractice-wins) —
  where this pack is silent, BestPractice stands). This whole bullet is one
  of the Morgan-specific facts scoped above — for anyone who isn't Morgan,
  ask instead
  ([`commit-author`](process/personal/README.md#commit-author)).

- **Every date is a Buenos Aires local calendar date**, not the session's
  system clock. Two places this bites:
  - Any date written into a document ("as of / verified `<date>`", a
    file's last-updated header) uses `America/Argentina/Buenos_Aires`
    local time.
  - Git commit timestamps: prefix the commit command with
    `TZ="America/Argentina/Buenos_Aires"` so the recorded author/committer
    offset is Buenos Aires', not the container's —
    `TZ="America/Argentina/Buenos_Aires" git commit -m "..."`.
  (Argentina has held UTC−3 year-round, no daylight saving, since 2009 —
  verified 2026-08-21; re-verify if this rule is ever touched and the fact
  seems dated.) Buenos Aires is *Morgan's* timezone specifically — one of
  the facts scoped above — not a default for someone else driving the
  change
  ([`buenos-aires-dates`](process/personal/README.md#buenos-aires-dates)).

- **Files carry a "last updated" timestamp, who made it, and a version
  number — near the top, when reasonable.** For a Markdown file: `<!--
  Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by NAME, to version N
  -->` as the first line. `NAME` is whoever made the edit — "Morgan F"
  when Morgan is driving (one of the facts scoped above), otherwise
  whoever actually made the edit. `N` is a plain integer counter private
  to that one file: 1 the first time the header is added, +1 each
  subsequent time the file's content changes. Only files actually changed
  pick up or bump the header — never a repo-wide sweep. Skip it where a
  leading comment would break the file (JSON has none) or where the file
  is a vendored, byte-for-byte copy under `process/upstream/`,
  `process/personal/`, or `process/voice/`
  ([`file-header`](process/personal/README.md#file-header)).

- **A derived file is marked by a header naming what replaces it.** The
  test is replacement, not authorship: where an assistant writes every
  document, "auto-generated" picks out no subset, so what matters is
  whether a fresh pass overwrites the file wholesale. A *derived* file —
  one regeneration replaces — carries, in its own comment syntax, four
  fixed fields followed by a plain routing sentence: `DERIVED from <source
  or glob> @ <source commit SHA at generation>`, `Recipe: <path>`,
  `Regenerate with: <command or plain instruction>`, then "edits here are
  safe to make but not durable — regeneration replaces this file; to make
  a change stick, edit the source or the recipe." It replaces
  [`file-header`](process/personal/README.md#file-header)'s own header
  rather than sitting beside it. An *agent-maintained* file, edited in
  place and never wholly replaced, is an ordinary source file and keeps
  `file-header` — [MAP.md](MAP.md) is this kind. The `@ <sha>` stamp is
  load-bearing because generation is usually a nondeterministic LLM call,
  so no comparison of content can tell a hand edit from an honest re-run;
  the stamp can, and it also shows when the source has moved on and the
  derived file is stale. Editing a derived file is allowed — the edit is a
  bug report, routed into the source (a missing fact) or the recipe (how
  this file should read) before the work lands, never left in place to be
  destroyed. There is deliberately no filename marker: `git grep -l
  "DERIVED from"` is the index, and a derived file is flagged in
  [MAP.md](MAP.md)'s tables when added. Not retroactive
  ([`derived-file-marker`](process/personal/README.md#derived-file-marker)).

- **A recipe holds a file's standing rules, with reasons — never its
  history.** Present tense and rewritable: the rules in force now, not a
  record of how they got that way, because a running log only grows and
  is never pruned. Recipes live in a `doc-recipes/` subdirectory beside
  the documents they govern, keeping a `.recipe.md` infix
  (`book/doc-recipes/CHAPTER1.recipe.md`) — the subdirectory so recipes
  don't double every listing, the infix because editor tabs and search
  results show bare basenames. Format: a `file-header`, a title, a
  `Source:` line where there is one, and a flat list — one rule per line,
  its reason an em-dash clause and only where a reader might otherwise
  delete the rule as arbitrary, or a short commit SHA in parentheses
  where the reason is really an origin story. `Source:` present means the
  file is derived; absent means standing constraints on a document written
  directly. A derived file's recipe is created with the file; a written
  document's starts the *second* time the same constraint is restated
  about it. It gets updated when the output is corrected, or a constraint
  is stated twice; adding a line means rereading the whole recipe, and any
  line a repo-wide convention now covers gets deleted. A rule appearing in
  a second recipe was never per-file — promote it to the repo's own
  conventions and delete it from both. Editing a recipe never triggers a
  regeneration
  ([`doc-recipe`](process/personal/README.md#doc-recipe)).

- **Commit messages link the assistant session where the change was
  planned.** Add a trailer, `Session: <url>` — for Claude Code,
  `https://claude.ai/code/session_<ID>`. For the unattended sync
  workflows, use that workflow run's own URL instead. If a tool has no
  shareable link at all, the trailer says so explicitly (`Session: none
  available (<tool>)`) rather than being silently omitted
  ([`session-trailer`](process/personal/README.md#session-trailer)).

- **Decide small calls yourself; only stop for big ones.** Default to
  continuing, not asking. Make small or moderate calls (a default value, a
  phrasing choice, an ambiguity that doesn't change the shape of what gets
  delivered) yourself, and note it in **both** the end-of-work reply and
  the commit message itself, under a "Judgment calls made:" heading (skip
  the heading only when there truly were none). Reserve stopping and
  asking for calls that are genuinely big: hard or costly to undo, change
  what gets delivered or to whom, spend real money, touch credentials or
  production, or are a toss-up two reasonable people would clearly land
  differently on
  ([`small-calls`](process/personal/README.md#small-calls)).

- **When a proposed rule's scope is ambiguous, ask which layer it belongs
  to.** A carve-out from
  [`small-calls`](process/personal/README.md#small-calls) above, because
  the cost that matters here isn't undoing the mistake but noticing it:
  both misfilings are silent. A rule that is really general, filed onto one
  document, ends up restated across several recipes in several phrasings,
  drifting; a rule that is really local, filed as a repo convention,
  quietly constrains every document in the repo. So when it is genuinely
  unclear whether a newly proposed rule governs one document or the whole
  repo, ask once, in the moment — the question is nearly free while the
  rule is still in front of the person proposing it, and expensive weeks
  later. The test is whether the rule's own text would still make sense
  applied to a different document: "only short paragraphs" would, so ask;
  "keep the Series A section under one page" names this document's own
  structure and is local on its face; "use em dashes, not semicolons" is
  plainly house style and goes to the repo's conventions. Asking on all
  three trains the person to wave the question through. Ask with a guess
  and its reason, so confirming costs a word
  ([`rule-scope-ask`](process/personal/README.md#rule-scope-ask)).

- **Push-back mode: argue, don't just comply, on writing-and-thinking work
  — never on technical or code work.** On work whose deliverable is prose
  meant to persuade or be judged by a human reader as an argument: argue a
  genuine counter-case before building on a stance as stated, and flag a
  serious unresolved disagreement before calling a piece done. Never
  applies to code, scripts, configuration, infrastructure, or debugging.
  Not a quota — never push back just to push back, and hand over a piece
  with no real problem as-is rather than manufacturing an objection.
  Reserve it for where it could actually help in a serious or deep way
  ([`push-back`](process/personal/README.md#push-back)).

- **Trim iteratively-edited prose on two triggers, not a running count.**
  Immediately after any substantial edit to a paragraph, give it a quick
  trim; independent of that, trim anything that's grown noticeably longer
  than the point it's making warrants. Same scope as push-back mode above:
  prose meant to be read and judged by a human, not code, scripts, or
  configuration
  ([`trim-prose`](process/personal/README.md#trim-prose)).

- **Cocreated list items stay roughly comparable in length — default
  short.** When cowriting a list, or several short-ish sections that
  function like one, keep each item roughly the same length as its
  neighbors — it's natural to expand one during a later edit while its
  neighbors stay untouched, even though nothing about its actual
  importance changed. A strong preference, not a hard rule
  ([`list-item-parity`](process/personal/README.md#list-item-parity)).

- **Use a list only when the content is actually a list, not as a
  formatting crutch.** Still an entirely ordinary list — never banned — for
  a genuine enumeration a reader will scan or reference individually
  (ingredients, steps, options, a checklist). What it catches: content with
  connective logic — "because," "so," one point building on the last —
  reformatted as bullet fragments that erase those connections because it
  reads as more put-together that way; reading the bullets back as plain
  connected sentences should lose nothing. A judgment call — when unsure,
  prose is the safer default
  ([`list-restraint`](process/personal/README.md#list-restraint)).

- **`go` or `merge` as a standalone final sentence means: commit and merge
  to main.** If Morgan's message, at a point where you've said you're
  ready, ends with `go` or `merge` as its own sentence — case-insensitive —
  that's authorization, right there, to commit the pending work and merge
  it into `main`, using this repo's usual conventions, without asking
  again first. If it's ambiguous whether the trailing word is this
  shorthand or ordinary language in context, ask rather than assume. This
  exact wording is Morgan's own shorthand — one of the facts scoped
  above — so don't expect or require it from anyone else; fall back to
  asking
  ([`go-merge`](process/personal/README.md#go-merge)).

- **TODO.md gate — step 0c of the merge runbook above, before every
  push.** [TODO.md](TODO.md) drifting out of sync with what was actually
  decided is the specific failure this gate exists to catch
  ([`todo-gate`](process/personal/README.md#todo-gate)).

- **A light check runs on every commit path**
  ([.github/workflows/light-check.yml](.github/workflows/light-check.yml),
  [process/personal/tools/light_check.py](process/personal/tools/light_check.py))
  — conflict markers, invalid JSON/YAML/Python syntax, secret-shaped
  strings, broken doc links, and (repo-wide, every run) that
  `process/personal/` is actually vendored. Run it yourself before
  committing, the same way as [doc_lint.py](process/upstream/tools/doc_lint.py)
  and [practice_audit.py](process/upstream/tools/practice_audit.py); CI
  runs it too
  ([`light-check`](process/personal/README.md#light-check)).

- **The deep check — every audit, plus an open-ended coherence review**
  ([`deep-check`](process/personal/README.md#deep-check)). The merge
  runbook's audits are the mechanical half and aren't optional. The other
  half is a read of the whole repo against itself — `AGENTS.md`, `MAP.md`,
  `TODO.md`, `GLOSSARY.md`, the vendored `process/personal/` and
  `process/voice/` trees, and the fit between them — for contradictions,
  stale slugs or references, formatting drift, and anything else that
  makes the repo harder to trust or follow. Run it when Morgan asks for a
  "deep check" by name, or after work that invites drift (rules added or
  reordered, a merge that resolved conflicts across several shared
  files); fix what it turns up in the same pass. Not a per-commit gate —
  the light check above carries that cadence.

- **Don't repeat the same backlog explanation every run.** A run can turn
  up a real pre-existing backlog that predates the current edit and isn't
  gated — explaining it away with the same disclaimer every commit adds
  nothing; a plain "checks passed" is fine. A run that actually fails, or
  a warning your own edit newly introduces, is always worth flagging
  ([`quiet-checks`](process/personal/README.md#quiet-checks)).

- **Agent-relevant instructions in a README or other key file also go in
  this AGENTS.md.** A README, `CONTRIBUTING.md`,
  [GETTING_STARTED.md](GETTING_STARTED.md), or any other key file can pick
  up its own operational instructions over time — fold the same
  instruction into `AGENTS.md` too, in its own words if that reads better
  here. This runs both directions
  ([`mirror-into-agents`](process/personal/README.md#mirror-into-agents)).

- **A mentioned rule, item, or destination is always a link** — a repo
  file, a rule of this pack, a [TODO.md](TODO.md) entry, a
  [GLOSSARY.md](GLOSSARY.md) term, a git branch, a commit, a PR. Covers
  replies in chat as much as files in the repo. The pack's own rules cite
  by permanent slug, `` [`slug`](process/personal/README.md#slug) ``,
  never by heading number — the number moves whenever the file is
  reorganized, the slug never does
  ([`rule-links`](process/personal/README.md#rule-links)).

- **A durable numbered list gets a permanent slug and anchor per entry,
  not just a position number.** A list whose entries hold real content
  likely to be cited elsewhere as "item N"/"rule N" (this repo's own
  [COMPANY_BUILDING_RULES.md](docs-team/COMPANY_BUILDING_RULES.md),
  [AI_GOVERNANCE_TO_COCREATE.md](docs-team/AI_GOVERNANCE_TO_COCREATE.md),
  [OUR_PHILOSOPHY.md](docs-team/OUR_PHILOSOPHY.md), [REASONS_WHY.md](docs-team/REASONS_WHY.md),
  [RULES_NOW_TESTING.md](docs-team/RULES_NOW_TESTING.md)) gets an `<a id="slug"></a>`
  anchor per entry, cited everywhere as `` `slug` (file.md#slug) ``, never
  a bare number — even a list that already has real headings, since
  GitHub's own auto-generated anchor still bakes the position number in.
  A short bullet list is exempt
  ([`durable-list-anchors`](process/personal/README.md#durable-list-anchors)).

- **A formal document cites another formal document, never a specific
  point inside an explicit brainstorm document.** [RANDOM_NOTES.md](docs-team/RANDOM_NOTES.md) is
  raw material, not vetted prose; a formal document citing a specific
  brainstorm entry as a claim's own support borrows credibility that
  entry never earned. If the idea hasn't been promoted into a formal
  document's own text yet, add it there first, then link there instead
  ([`brainstorm-citations`](process/personal/README.md#brainstorm-citations)).

- **Don't state a count that will drift — describe it instead.** "Several
  findings," not an exact number, unless the count is the actual point
  ([`no-stale-counts`](process/personal/README.md#no-stale-counts)).

- **Header capitalization: pick one consistent schema — this repo already
  has, and keeps, its own.** This repo's headers are already sentence
  case throughout; the pack's own default for a repo starting from a
  blank page is NY Times headline style, but a repo that already made and
  kept a consistent choice has nothing to change
  ([`header-caps`](process/personal/README.md#header-caps)).

- **Private repo names and specifics get scrubbed before anything vendors
  or is shared.** Applies to whoever maintains the pack's own source
  (RepoPersonalPreferences), not to this repo's own work — this repo
  names itself and its own history plainly in [TODO.md](TODO.md), this
  `AGENTS.md`, and commit messages, which never leave it (see the Voice
  section's own references to its source repo, below)
  ([`private-repo-scrub`](process/personal/README.md#private-repo-scrub)).

- **LLM integrations stay platform-neutral; OpenRouter is the default
  assumption.** Any system this pack helps set up that talks to an LLM
  should be built against a provider-neutral interface — model name,
  token, and base URL as swappable config. Absent other instruction,
  assume the credential in hand is an OpenRouter token, not a given
  vendor's own key
  ([`llm-neutral`](process/personal/README.md#llm-neutral)).

- **Always fail gracefully.** Any code you write or set up here anticipates
  its own common failure modes rather than letting them surface as an
  unhandled crash: a clear error message naming exactly what's missing and
  how to fix it, a documented fallback/default, or a clean non-zero exit —
  never a raw stack trace, a silent wrong answer, or a hang
  ([`fail-gracefully`](process/personal/README.md#fail-gracefully)).

- **This repo's default branch is `main`, checked once at install.** If it
  isn't already `main`, set it once — via the GitHub API's repo-update
  endpoint where the session's tools reach that far, otherwise as a
  one-click item (Settings → General → Default branch) disclosed in
  [GETTING_STARTED.md](GETTING_STARTED.md)'s administrator section
  ([`default-branch`](process/personal/README.md#default-branch)).

- **In a content-oriented repo, group deliverable content under a
  subdirectory once root gets cluttered — a recommendation, not a
  rule.** Nothing checks for this, and it's never retroactive on its own —
  raise it as a judgment call if root ever accumulates several
  deliverable documents at once
  ([`content-subdirs`](process/personal/README.md#content-subdirs)).

- **A new pack rule lands in reading-order position, never appended.**
  Something RepoPersonalPreferences (this pack's own source) does when it
  adds a rule, mirrored into this repo's `AGENTS.md` on the next update —
  not something this repo initiates itself, since the pack only ever
  flows one way, in
  ([`new-rule-placement`](process/personal/README.md#new-rule-placement)).

- **A scheduled check keeps BestPractice itself current — weekly by
  default, one line to switch to daily**
  ([.github/workflows/bestpractice-upstream-sync.yml](.github/workflows/bestpractice-upstream-sync.yml)):
  unattended, it takes any upstream update, integrates it with its own
  judgment, and merges it — recording every judgment call in the commit
  message. Authenticates with either `CLAUDE_CODE_OAUTH_TOKEN` or
  `ANTHROPIC_API_KEY` — only one is required
  ([`bestpractice-sync`](process/personal/README.md#bestpractice-sync)).

- **A second scheduled check keeps the personal pack itself current**
  (`.github/workflows/personal-pack-sync.yml`): same shape, pointed at
  `process/personal/` against RepoPersonalPreferences (private). Needs its
  own repository secret, `PERSONAL_PACK_TOKEN`
  ([`pack-sync`](process/personal/README.md#pack-sync)).

- **A third scheduled check keeps the voice guidelines current**
  ([.github/workflows/voice-guidelines-sync.yml](.github/workflows/voice-guidelines-sync.yml)):
  same shape again, pointed at
  [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md)
  against [SoundHuman](https://github.com/themorgan/SoundHuman)
  (private, one file rather than a whole subtree — see
  [voice_sync.py](process/voice/tools/voice_sync.py)). Needs its own
  repository secret, `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` — the same secret
  name that repo's own docs already use for its other known consumers
  (VoiceDefinitionMorgan, VoiceDefinitionCelia). Runs fifteen minutes after
  the personal-pack sync's own weekly slot, same reasoning as that slot's
  own fifteen-minute offset from the BestPractice sync.

- **Unattended automation reports its own blockers as a GitHub issue, not
  only a log line.** A missing credential or other blocker in any of the
  three scheduled syncs above opens (or comments on) a GitHub issue via
  [process/personal/tools/report_automation_issue.py](process/personal/tools/report_automation_issue.py),
  alongside the existing `::warning::` annotation, since an annotation
  only lives inside one workflow run and nobody sees it unless they
  already know to look
  ([`automation-issues`](process/personal/README.md#automation-issues)).

- **All three scheduled syncs skip cleanly, not loudly, when neither Claude
  credential is set.** If asked to run one manually, no secret is needed —
  take the update in-session, then remind Morgan to set one so future
  unattended runs don't need to be asked for by hand.

- **A session-start notice asks about drift immediately, not at the
  end.** `tools/bootstrap.sh` runs all three freshness notices
  (`checkin.py fresh`, `pack_sync.py fresh`, `voice_sync.py fresh`) on every
  session start — a one-line notice only when a source has moved, never a
  gate. Raise whichever fired as part of catching the member up. **A fired
  BestPractice or personal-pack notice is also persisted**, not just
  printed: `tools/bootstrap.sh` wraps those two to also run `python3
  process/personal/tools/pack_sync.py record <source> "<notice>"`, writing
  it into this repo's own [TODO.md](TODO.md) under a `## Pending drift
  reviews` heading (kept sentence case here, matching this repo's own
  header convention). Resolve one with `python3
  process/personal/tools/pack_sync.py resolve <source> [note]` once its
  drift has actually been reviewed. Taking any update stays deliberate
  whenever it's raised. **Fallback:** repeat the same cheap comparison at
  the end of the session too, if it wasn't already raised and answered
  ([`drift-notice`](process/personal/README.md#drift-notice)).

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
  this repo. **Public-safe invariant:** nothing proprietary may appear
  under `process/upstream/`, ever.
  `python3 process/upstream/tools/practice_audit.py`
  ([practice_audit.py](process/upstream/tools/practice_audit.py)) enforces
  this against
  [process/scrub_blocklist.txt](process/scrub_blocklist.txt) and must pass
  before committing anything that touches `process/`.
- `process/personal/` is categorically never exported — it opts out of the
  scrub entirely because it exists specifically to hold Morgan's own
  vocabulary.
- Export gate = merge runbook step 0b. Periodic check-in per
  [process/upstream/INSTALL.md](process/upstream/INSTALL.md) §4 (recurring
  item in [TODO.md](TODO.md)) — in practice this repo mostly consumes
  BestPractice rather than improving it.
- [process/manifest.json](process/manifest.json) and
  [process/manifest_personal.json](process/manifest_personal.json) are the
  installed-practices registries; when a practice file changes locally,
  export + re-baseline, or flip the entry to `diverged`.
