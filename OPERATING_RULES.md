<!-- Last updated: 2026-08-28 09:00:00 (Buenos Aires) by Morgan F, to version 2 -->

# Operating rules — what's actually in force

This is the third stage of this repo's pipeline (see
[README.md](README.md)'s "How this repo's ideas become company policy"):
[FIFTEEN_RULES.md](FIFTEEN_RULES.md) argues *why*; [COCREATION_DESIGN.md](COCREATION_DESIGN.md)
designs *how* the AI systems themselves should be built so the healthy
pattern is the default; this document is *what's actually in force, right
now* — the checklist a session in any of Morgan's real work is expected to
follow today, revised the moment practice teaches something. A rule earns
its way onto this list from the brainstorm or one of the two essays; it
earns its way *off* — into [RepoPersonalPreferences](https://github.com/themorgan/RepoPersonalPreferences)'s
personal pack, for automatic rollout to every project Morgan runs — only
once it's actually proven itself here. See [TODO.md](TODO.md) for what's
currently pending that move.

**This document does not get vendored anywhere.** Unlike `process/upstream/`
or `process/personal/`, it has no manifest entry and no sync workflow — it's
native to this repo, the same as [IDEAS.md](IDEAS.md), because working out
which rules are ready is exactly this repo's job. Nothing here is real
company policy for another project until a session has separately gone into
RepoPersonalPreferences and landed it there (see "Promotion" below) —
mentioning a rule here is not the same as adopting it elsewhere.

## Status key

- **Trial** — being tried in real work now; not yet proven enough to port.
- **Ready to promote** — proven; the next session touching
  RepoPersonalPreferences should land it there.
- **Promoted** — already landed in RepoPersonalPreferences. Kept here only
  as a pointer, not restated in full — full restatement would just be a
  second copy of the same rule that can drift out of sync with the first,
  the same reasoning the personal pack's own §2 gives for not duplicating
  BestPractice.

## Rules

### 1. Push-back mode on writing-and-thinking work — *Promoted*

[RepoPersonalPreferences §19](https://github.com/themorgan/RepoPersonalPreferences/blob/main/process/personal/README.md).
Argue a genuine counter-case before building on a stated stance; flag a
serious unresolved disagreement before calling a piece done. Never on
code or other technical work. Origin: this repo, 2026-08-26 (see
[TODO.md](TODO.md)).

### 2. Provider-neutral LLM integrations — *Promoted*

[RepoPersonalPreferences §12](https://github.com/themorgan/RepoPersonalPreferences/blob/main/process/personal/README.md).
Build any LLM integration against a swappable model/token/base-URL
interface; assume an OpenRouter credential absent other instruction.
[COCREATION_DESIGN.md](COCREATION_DESIGN.md) names this as a hedge on
FIFTEEN_RULES rule 1 (context as capital, strandable by a vendor switch),
already required by the pack before this document existed.

### 3. Argue in the open — *Trial*

When reviewing or commenting on writing-and-thinking work (a PR review, a
comment thread, feedback on a draft), post a stated, half-formed position
and invite disagreement — instead of a clean, finished-looking
suggestion. The point is to keep the disagreement itself in the record,
not just its resolution (FIFTEEN_RULES rule 4; COCREATION_DESIGN
"Argue in the open"; IDEAS.md's "PR comments as argument, not just the
record").

### 4. Two reflexes, asked out loud mid-task — *Trial*

Before calling a nontrivial piece of work done, state the answer to both,
in the reply itself, not just silently in reasoning:

- Have I done this shape before, or will I again?
- Is there a way this could be *better* — not just faster?

(FIFTEEN_RULES rule 6; COCREATION_DESIGN: "the two reflexes... belong in
the system prompt, not just in a human's habit.")

### 5. Write like a human, not an LLM — *Trial*

Superseded its original draft (2026-08-27), which pointed at FIFTEEN_RULES
rule 13's fingerprints by hand because "no tooling exists for this yet."
It turned out tooling already existed, just not wired up here: a whole
repo, [VoiceGuidelinesToSoundHuman](https://github.com/themorgan/VoiceGuidelinesToSoundHuman),
maintains exactly this ruleset — [HUMAN_VOICE_RULES.md](https://github.com/themorgan/VoiceGuidelinesToSoundHuman/blob/main/HUMAN_VOICE_RULES.md),
already consumed by other repos in production (VoiceDefinitionMorgan,
VoiceDefinitionCelia, the WriteLike app). Vendored here at
[process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md)
(2026-08-28), kept current by its own weekly sync and session-start check
— see [AGENTS.md](AGENTS.md)'s "Voice" section, which is where the actual
rule now lives: it governs everything a session writes in this repo,
chat replies included, not just committed documents. Still *Trial* here
rather than jumping straight to Promoted — this is the first repo applying
it to general assistant output rather than only the WriteLike voice-pack
path, and that's a new use of it worth testing before it becomes a default
in RepoPersonalPreferences.

### 6. Dark-process self-audit, including the session's own habits — *Trial*

Periodically — tie this to the same cadence as the recurring BestPractice
check-in in [TODO.md](TODO.md) — list workflows whose only interface is a
human inbox, including the assistant's own ("email Morgan to change this
config" counts), and propose an addressable alternative (FIFTEEN_RULES
rule 11; COCREATION_DESIGN "Configure the AI to hunt its own dark
processes").

### 7. Contradiction-scanning across the corpus, as a recurring job — *Trial*

Periodically re-read [IDEAS.md](IDEAS.md) (and, now, this document) for
entries that have come to disagree with each other — the same recurring
cadence as item 6, not a one-off pass someone has to remember to run
(IDEAS.md's meta section; COCREATION_DESIGN "Keeping the corpus honest").

## Not yet ready for this list

These ideas from [COCREATION_DESIGN.md](COCREATION_DESIGN.md) need either
more real testing or actual infrastructure this repo doesn't have yet —
writing them as rules now would be systematizing before the third
instance, exactly what FIFTEEN_RULES rule 5 warns against. Tracked instead
as open items in [TODO.md](TODO.md):

- **Active/proactive resurfacing** ("you decided X six weeks ago,
  unprompted") — needs something that actively mines and ranks history,
  not just answers when asked.
- **Automatic workflow-candidate detection** — mining commit/session
  history for recurring task shapes, rather than relying on rule 4's
  human-triggered reflex.
- **Situational, inferred cost-awareness** — COCREATION_DESIGN's own text
  records that a fixed "surface spend per outcome" policy was already
  proposed and rejected in discussion; only the passive log survived.
  The harder half — inferring *which* posture applies — is still open.
- **A coldstart test** — can a fresh session, given only the memory store,
  reconstruct the state of any live decision? Worth running periodically,
  but it's a manual audit today, not an automatable gate.
- **Deeper "normie"-employee engagement**, beyond push-back mode (item 1)
  — visible reminders of the deeper mode, making rule-extraction "in your
  face," proactive resurfacing of a relevant rule. IDEAS.md's own "Why
  BestPractice specifically works" open question.

## Promotion — moving a rule from here into RepoPersonalPreferences

1. Mark the rule **Ready to promote** here, with a line on what proved it
   out (which sessions, what it caught or avoided).
2. In a separate session against RepoPersonalPreferences, land it as a new
   numbered section appended past its current last section — that pack's
   own convention for adding a rule without a full renumbering pass across
   every dependent repo's citations (see its §19-§21 for worked examples).
3. Come back here, mark the rule **Promoted**, and cut its entry down to a
   pointer only, per the status key above.
4. Note the move in [TODO.md](TODO.md)'s decision record, same as any
   other cross-repo change.

*(Origin: a session on 2026-08-27 that had initially recommended landing
these ideas directly into RepoPersonalPreferences's
[process/personal/README.md](https://github.com/themorgan/RepoPersonalPreferences/blob/main/process/personal/README.md) —
corrected by Morgan, who wants this repo to actually try a rule out before
it becomes company-wide policy. See [TODO.md](TODO.md) for the decision
record.)*
