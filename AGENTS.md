<!-- Last updated: 2026-08-27 23:09:41 (Buenos Aires) by Morgan F, to version 5 -->

# Repository instructions — read me first

**Orientation: read [MAP.md](MAP.md) first** — the repository map. It covers
the brainstorm ([IDEAS.md](IDEAS.md)) and indexes the practice layer that
keeps this repo well-run.

## Where things are (quick index — check here BEFORE searching the repo)

| Looking for… | Go to |
|---|---|
| Canonical names — use these, don't invent new ones | [GLOSSARY.md](GLOSSARY.md) |
| The brainstorm itself | [IDEAS.md](IDEAS.md) |
| The three-stage pipeline (idea → rules now testing → company policy) | [README.md](README.md) |
| Rules actually in force now, and promotion candidates | [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) |
| The voice guidelines (write like a human, not an LLM) | [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md) |
| Open items: analyses, verifications, decisions | [TODO.md](TODO.md) |
| Practice layer: vendored BestPractice copy, manifest, scrub blocklist | `process/` |

## Voice — every reply and every document

This repo's own writing follows
[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md),
vendored from
[SoundHuman](https://github.com/themorgan/VoiceGuidelinesToSoundHuman)
(tracked in [process/manifest_voice.json](process/manifest_voice.json), kept
current by a weekly sync plus a session-start check — see "A third scheduled
check keeps the voice guidelines current" below). It governs **everything a
session writes here, not just committed documents** — the chat reply itself
is in scope too. Check outward-facing prose against it before calling a
piece done; this is [RULES_NOW_TESTING.md](RULES_NOW_TESTING.md) item 5, now
backed by a real, vendored ruleset instead of a manual checklist. Its own
§17 sets the precedence rule if that ever conflicts with a more specific,
person-authored voice pack: the person-specific rules win.

## Build-environment gotchas — do NOT rediscover these

- At session start, run `bash tools/bootstrap.sh` before other work (Claude
  Code runs it automatically via the SessionStart hook — see
  `.claude/settings.json`).

## Git / workflow

- Develop on a feature branch; open a PR; merge only when the user says so
  (except the BestPractice sync, the pack sync, and the voice guidelines
  sync, which merge their own PRs unattended — see
  [process/personal/README.md](process/personal/README.md) §14, §15, and
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
   (practice 10): did this thread's work imply anything that must be
   captured — a document update, a registry entry, a decision record? Fold
   it now.
   **0b. Export gate** (practice 14): did this thread improve a *generic*
   BestPractice practice (not the personal pack, which never exports)?
   Fold the abstracted form into `process/upstream/` now, per
   [process/upstream/INSTALL.md](process/upstream/INSTALL.md) §3, and run
   the scrub audit.
   **0c. TODO gate (personal pack §9):** re-read this thread's discussion
   against [TODO.md](TODO.md) — add any idea that came up but never got a
   line; remove or check off anything this branch just implemented. Do
   this every push.
1. Fetch and merge `main` locally.
2. Resolve by fixed per-file-class rules (practice 9):
   - `process/manifest.json` / `process/manifest_personal.json` /
     `process/manifest_voice.json`: **union** of both sides — never drop an
     entry or a status.
   - [TODO.md](TODO.md) and [IDEAS.md](IDEAS.md): **append-only — keep both
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
     ([process/personal/README.md](process/personal/README.md) §15).
   - **[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md): never hand-merge either,** same
     reasoning — it must stay byte-identical to whatever
     [voice_sync.py](process/voice/tools/voice_sync.py) `update` last
     mirrored from SoundHuman; resolve by re-running that
     sync, not by editing the file directly.
3. Run the audits — **all must pass before the merge commits**:
   `python3 process/upstream/tools/doc_lint.py`,
   `python3 process/personal/tools/light_check.py`, and
   `python3 process/upstream/tools/practice_audit.py`.
4. Commit the merge, push, land per this repo's convention.

## Conventions

- **Sections are ordered by the reader's frequency, not the writer's**
  (practice 36): a document walking through rules in multiple sections puts
  common, everyday content first and rare edge cases / contingencies last,
  unless the subject matter dictates otherwise. Ask: would most readers
  have to scroll past this section to reach the one they opened the
  document for?
- **PR descriptions come from the diff, not the template** (practice 39):
  write "What changed" / "Why" / "Files touched" from what actually
  happened on this branch. Check a `## Gates` box only when it is actually
  true for this change — an unchecked box, or a "not applicable" note, is
  normal. Never check every box just to make the form look complete.
- **Doc references are links** (practice 11): relative markdown links,
  never bare backticked filenames. Use `≈`, not `~`, for "approximately".
  `python3 process/upstream/tools/doc_lint.py` checks these conventions on
  files changed vs the default branch; run it on what you touch before
  committing.
- **Volatile rules carry their dates** (practice 16): anything asserted
  here about an external platform or tool carries *as of / verified
  `<date>`* inline, in Buenos Aires local time (personal pack §4, stricter
  than BestPractice's own default of "the contributor's local calendar
  date" — here, the contributor's local calendar date always means Buenos
  Aires, regardless of where a session physically runs).
- **Outward-facing documents use the reader's words** (practice 34): this
  repo's README and [GETTING_STARTED.md](GETTING_STARTED.md) are read by
  people who are not developers. Terms that name a category are the
  reader's word, a plain equivalent, or glossed inline — never left to a
  glossary. Jargon arrives from the sources a session just read, so run
  the check as a separate pass after drafting.
- **Reply convention** (practice 12): every reply that created or modified
  files ends with a "Files touched" list — branch link + post-merge link +
  one-line description per file.

## Personal setup rules (Morgan's pack)

These extend BestPractice's own conventions above; they are this repo's
personal layer (`process/personal/`), not upstream BestPractice, and they
never get exported to the public BestPractice repo.

- **On conflict with BestPractice, this pack wins.** BestPractice sets the
  default; where a rule here and a rule of BestPractice's own genuinely
  disagree on the same point, this pack's rule governs. Where this pack is
  silent, BestPractice's own rule stands undisturbed — this pack only
  narrows or overrides where it actually speaks
  ([process/personal/README.md](process/personal/README.md) §1).

- **Don't duplicate BestPractice.** This pack exists to add to BestPractice
  or override it, not restate it. A bullet here that only repeats what
  BestPractice already establishes on its own gets dropped the next time
  this file is touched, rather than left as a second copy that can drift
  out of sync with the first
  ([process/personal/README.md](process/personal/README.md) §2).

- **Commits are always authored "Morgan F".** Use Morgan's own email
  address:
  `git config user.name "Morgan F"` and
  `git config user.email "morgan@westegg.com"`
  once per clone ([tools/bootstrap.sh](tools/bootstrap.sh) does this
  automatically). This replaces, rather than defers to, BestPractice's own
  "ask before the first commit" default — the identity is already decided,
  so don't ask. It replaces only the *identity* half: the pack says nothing
  about co-authorship, so BestPractice's own `Co-Authored-By:` trailer
  naming the assistant still applies (personal pack §1 — where this pack is
  silent, BestPractice stands).

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
  seems dated.)

- **Files carry a "last updated" timestamp, who made it, and a version
  number — near the top, when reasonable.** For a Markdown file: `<!--
  Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by NAME, to version N
  -->` as the first line. `NAME` is whoever made the edit — always "Morgan
  F" here. `N` is a plain integer counter private to that one file: 1 the
  first time the header is added, +1 each subsequent time the file's
  content changes. Only files actually changed pick up or bump the header —
  never a repo-wide sweep. Skip it where a leading comment would break the
  file (JSON has none) or where the file is a vendored, byte-for-byte copy
  under `process/upstream/`, `process/personal/`, or `process/voice/`.

- **Commit messages link the assistant session where the change was
  planned.** Add a trailer, `Session: <url>` — for Claude Code,
  `https://claude.ai/code/session_<ID>`. For the unattended sync workflows,
  use that workflow run's own URL instead. If a tool has no shareable link
  at all, the trailer says so explicitly (`Session: none available
  (<tool>)`) rather than being silently omitted.

- **Decide small calls yourself; only stop for big ones.** Default to
  continuing, not asking. Make small or moderate calls (a default value, a
  phrasing choice, an ambiguity that doesn't change the shape of what gets
  delivered) yourself, and note it in **both** the end-of-work reply and
  the commit message itself, under a "Judgment calls made:" heading (skip
  the heading only when there truly were none). Reserve stopping and
  asking for calls that are genuinely big: hard or costly to undo, change
  what gets delivered or to whom, spend real money, touch credentials or
  production, or are a toss-up two reasonable people would clearly land
  differently on.

- **`go` or `merge` as a standalone final sentence means: commit and merge
  to main.** If Morgan's message, at a point where you've said you're
  ready, ends with `go` or `merge` as its own sentence — case-insensitive —
  that's authorization, right there, to commit the pending work and merge
  it into `main`, using this repo's usual conventions, without asking
  again first. If it's ambiguous whether the trailing word is this
  shorthand or ordinary language in context, ask rather than assume
  ([process/personal/README.md](process/personal/README.md) §8).

- **TODO.md gate — step 0c of the merge runbook above, before every
  push.** [TODO.md](TODO.md) drifting out of sync with what was actually
  decided is the specific failure this gate exists to catch.

- **Agent-relevant instructions in a README or other key file also go in
  this AGENTS.md.** A README, `CONTRIBUTING.md`,
  [GETTING_STARTED.md](GETTING_STARTED.md), or any other key file can pick
  up its own operational instructions over time — fold the same
  instruction into `AGENTS.md` too, in its own words if that reads better
  here. This runs both directions
  ([process/personal/README.md](process/personal/README.md) §10).

- **A light check runs on every commit path**
  ([.github/workflows/light-check.yml](.github/workflows/light-check.yml),
  [process/personal/tools/light_check.py](process/personal/tools/light_check.py))
  — conflict markers, invalid JSON/YAML/Python syntax, secret-shaped
  strings, broken doc links, and (repo-wide, every run) that
  `process/personal/` is actually vendored. Run it yourself before
  committing, the same way as [doc_lint.py](process/upstream/tools/doc_lint.py)
  and [practice_audit.py](process/upstream/tools/practice_audit.py); CI
  runs it too.

- **LLM integrations stay platform-neutral; OpenRouter is the default
  assumption.** Any system this pack helps set up that talks to an LLM
  should be built against a provider-neutral interface — model name,
  token, and base URL as swappable config. Absent other instruction,
  assume the credential in hand is an OpenRouter token, not a given
  vendor's own key ([process/personal/README.md](process/personal/README.md)
  §12).

- **Always fail gracefully.** Any code you write or set up here anticipates
  its own common failure modes rather than letting them surface as an
  unhandled crash: a clear error message naming exactly what's missing and
  how to fix it, a documented fallback/default, or a clean non-zero exit —
  never a raw stack trace, a silent wrong answer, or a hang
  ([process/personal/README.md](process/personal/README.md) §13).

- **A scheduled check keeps BestPractice itself current — weekly by
  default, one line to switch to daily**
  ([.github/workflows/bestpractice-upstream-sync.yml](.github/workflows/bestpractice-upstream-sync.yml)):
  unattended, it takes any upstream update, integrates it with its own
  judgment, and merges it — recording every judgment call in the commit
  message. Authenticates with either `CLAUDE_CODE_OAUTH_TOKEN` or
  `ANTHROPIC_API_KEY` — only one is required.

- **A second scheduled check keeps the personal pack itself current**
  (`.github/workflows/personal-pack-sync.yml`): same shape, pointed at
  `process/personal/` against RepoPersonalPreferences (private). Needs its
  own repository secret, `PERSONAL_PACK_TOKEN`
  ([process/personal/README.md](process/personal/README.md) §15).

- **A third scheduled check keeps the voice guidelines current**
  ([.github/workflows/voice-guidelines-sync.yml](.github/workflows/voice-guidelines-sync.yml)):
  same shape again, pointed at
  [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md)
  against [SoundHuman](https://github.com/themorgan/VoiceGuidelinesToSoundHuman)
  (private, one file rather than a whole subtree — see
  [voice_sync.py](process/voice/tools/voice_sync.py)). Needs its own
  repository secret, `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN` — the same secret
  name that repo's own docs already use for its other known consumers
  (VoiceDefinitionMorgan, VoiceDefinitionCelia). Runs fifteen minutes after
  the personal-pack sync's own weekly slot, same reasoning as that slot's
  own fifteen-minute offset from the BestPractice sync.

- **All three scheduled syncs skip cleanly, not loudly, when neither Claude
  credential is set.** If asked to run one manually, no secret is needed —
  take the update in-session, then remind Morgan to set one so future
  unattended runs don't need to be asked for by hand.

- **A session-start notice asks about drift immediately, not at the
  end.** `tools/bootstrap.sh` runs all three freshness notices
  (`checkin.py fresh`, `pack_sync.py fresh`, `voice_sync.py fresh`) on every
  session start — a one-line notice only when a source has moved, never a
  gate. Raise whichever fired as part of catching the member up. Taking
  any update stays deliberate whenever it's raised. **Fallback:** repeat
  the same cheap comparison at the end of the session too, if it wasn't
  already raised and answered
  ([process/personal/README.md](process/personal/README.md) §16).

- **This repo's default branch is `main`, checked once at install.** If it
  isn't already `main`, set it once — via the GitHub API's repo-update
  endpoint where the session's tools reach that far, otherwise as a
  one-click item (Settings → General → Default branch) disclosed in
  [GETTING_STARTED.md](GETTING_STARTED.md)'s administrator section
  ([process/personal/README.md](process/personal/README.md) §17).

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
