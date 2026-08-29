<!-- Last updated: 2026-08-29 15:12:22 (Buenos Aires) by Morgan F, to version 10 -->

# Rules now testing — the current state of what we're trying

This is the second stage of this repo's pipeline (see
[README.md](README.md)'s "How this repo's ideas become company policy"):
[COMPANY_BUILDING_RULES.md](COMPANY_BUILDING_RULES.md) argues *why*;
[AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md) designs *how*
the AI systems themselves should be built so the healthy pattern is the
default; this document is *what's actually being tried right now* — not
settled policy, not a finished essay, but the checklist a session in any
of Morgan's real work is expected to follow today, revised the moment
practice teaches something. A rule earns
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
  the same reasoning the personal pack's own
  [`no-duplication`](process/personal/README.md#no-duplication) gives for
  not duplicating BestPractice.

## Rules

<a id="push-back-writing-thinking"></a>

### 1. Push-back mode on writing-and-thinking work — *Promoted*

[`push-back`](process/personal/README.md#push-back).
Argue a genuine counter-case before building on a stated stance; flag a
serious unresolved disagreement before calling a piece done. Never on
code or other technical work.

<a id="provider-neutral-llm"></a>

### 2. Provider-neutral LLM integrations — *Promoted*

[`llm-neutral`](process/personal/README.md#llm-neutral).
Build any LLM integration against a swappable model/token/base-URL
interface; assume an OpenRouter credential absent other instruction.
Hedges [`capital-asset`](COMPANY_BUILDING_RULES.md#capital-asset)
(context as capital).

<a id="argue-in-the-open"></a>

### 3. Argue in the open — *Trial*

On writing-and-thinking work — a PR review, comment thread, feedback on
a draft — post a half-formed position and invite disagreement instead of
a finished one. Keeps the disagreement in the record, not just its
resolution
([`co-create-dont-delegate`](COMPANY_BUILDING_RULES.md#co-create-dont-delegate)).

<a id="three-reflexes-out-loud"></a>

### 4. Three reflexes, asked out loud mid-task — *Trial*

Before calling work done, answer all three out loud in the reply:

- What rules or protocols should come from this?
- Have I done this shape before, or will I again?
- Is there a way this could be better — not just faster?

([`three-questions`](COMPANY_BUILDING_RULES.md#three-questions).)

<a id="write-like-a-human"></a>

### 5. Write like a human, not an LLM — *Trial*

Follow [process/voice/HUMAN_VOICE_RULES.md](process/voice/HUMAN_VOICE_RULES.md),
vendored from [SoundHuman](https://github.com/themorgan/SoundHuman)
and synced automatically ([AGENTS.md](AGENTS.md)'s "Voice" section) —
governs everything written here, chat replies included. Still *Trial*:
first repo applying it beyond WriteLike.

<a id="dark-process-self-audit"></a>

### 6. Dark-process self-audit, including the session's own habits — *Trial*

Periodically, same cadence as the BestPractice check-in — list workflows
whose only interface is a human inbox, the assistant's own included, and
propose an addressable alternative
([`no-dark-processes`](COMPANY_BUILDING_RULES.md#no-dark-processes)).

<a id="contradiction-scanning"></a>

### 7. Contradiction-scanning across the corpus, as a recurring job — *Trial*

Periodically re-read [IDEAS.md](IDEAS.md) and this document for entries
that now disagree — same cadence as
[`dark-process-self-audit`](#dark-process-self-audit), not a one-off.

## Not yet ready for this list

These ideas from [AI_GOVERNANCE_TO_COCREATE.md](AI_GOVERNANCE_TO_COCREATE.md)
need either more real testing or actual infrastructure this repo doesn't
have yet — writing them as rules now would be systematizing before the
third instance, exactly what
[`think-in-workflows`](COMPANY_BUILDING_RULES.md#think-in-workflows) warns
against. Tracked instead as open items in [TODO.md](TODO.md):

- **Active/proactive resurfacing** ("you decided X six weeks ago,
  unprompted") — needs something that actively mines and ranks history,
  not just answers when asked.
- **Automatic workflow-candidate detection** — mining commit/session
  history for recurring task shapes, rather than relying on
  [`three-reflexes-out-loud`](#three-reflexes-out-loud)'s human-triggered
  reflex.
- **Situational, inferred cost-awareness** — AI_GOVERNANCE_TO_COCREATE's own text
  records that a fixed "surface spend per outcome" policy was already
  proposed and rejected in discussion; only the passive log survived.
  The harder half — inferring *which* posture applies — is still open.
- **A coldstart test** — can a fresh session, given only the memory store,
  reconstruct the state of any live decision? Worth running periodically,
  but it's a manual audit today, not an automatable gate.
- **Deeper "normie"-employee engagement**, beyond
  [`push-back-writing-thinking`](#push-back-writing-thinking) — visible
  reminders of the deeper mode, making rule-extraction "in your face,"
  proactive resurfacing of a relevant rule. IDEAS.md's own "Why
  BestPractice specifically works" open question.

## Promotion — moving a rule from here into RepoPersonalPreferences

1. Mark the rule **Ready to promote** here, with a line on what proved it
   out (which sessions, what it caught or avoided).
2. In a separate session against RepoPersonalPreferences, land it in
   reading-order position among the existing rule groups (not appended to
   the end), with its own permanent slug and anchor — that pack's own
   convention for adding a rule without a renumbering pass across every
   dependent repo's citations, since citations use the slug, not the
   position ([`new-rule-placement`](process/personal/README.md#new-rule-placement)).
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
