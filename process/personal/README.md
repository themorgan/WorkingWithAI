<!-- Last updated: 2026-08-29 14:55:51 (Buenos Aires) by Morgan F, to version 39 -->

# The Personal Pack

A "pack" in BestPractice's own vocabulary (practice 23,
[process/upstream/INSTALL.md](../upstream/INSTALL.md) §7) is a small
rulebook too specific to belong in the public BestPractice repo but too
general to belong to just one project. This one is exactly that middle
ground: personal conventions Morgan wants in **every** repo he starts, not
generic enough for the public upstream and not specific enough to live in
just one project's own [AGENTS.md](../../AGENTS.md).

Unlike a domain-compliance pack, this one has no *dedicated, single-purpose*
repo of its own — it lives here, in RepoPersonalPreferences (which also
carries this repo's own BestPractice install, since it's a normal working
repo too, not just the pack's source), and gets copied into each new repo
alongside BestPractice itself (see
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md)). Within *this* repo,
`upstream.commit` in [../manifest_personal.json](../manifest_personal.json)
stays `null` — the vendored tree here *is* upstream for the pack, per the
pack anatomy rule ([process/upstream/INSTALL.md](../upstream/INSTALL.md)
§7). In a *dependent* repo the pack is vendored into, that repo's own
`manifest_personal.json` instead records this repo's real URL and commit
([`install`](#install) below) — a subtree-tracked dependency in place of the
eventual dedicated-repo split [INSTALL.md](../upstream/INSTALL.md) §7
anticipates, which a scheduled check ([`pack-sync`](#pack-sync)) then keeps
current, the same way [process/manifest.json](../manifest.json) tracks
BestPractice.

## The Rules, and Why

**Every rule has a permanent slug — `deep-check`, `go-merge` — and that slug
is the only thing anything ever cites.** A citation is a link to the rule's
own anchor: `` [`deep-check`](process/personal/README.md#deep-check) `` from
anywhere else in a repo, `` [`deep-check`](#deep-check) `` inside this file.
The slug is assigned when the rule is written and never changes, even if the
rule is retitled, regrouped, or rewritten; the anchor above each heading is
what makes it a real link rather than a name to go hunting for
([`rule-links`](#rule-links)).

**The numbers on the headings are positional, and nothing cites them.** They
say where a rule sits in the reading order, top to bottom, and
they change whenever the file is reorganized, which is exactly why a
citation must not depend on one. This split is what makes a reorganization
cheap: moving a rule is an edit to this file (and its group table below),
not a sweep through every citation in every repo the pack is installed into.
[`light-check`](#light-check) enforces it: a bare `§N`-style reference to a
rule of this pack fails the check, and a cited slug that doesn't resolve to
an anchor here fails it too. (`§` still belongs to another document's own
numbering — `INSTALL.md §2`, or SoundHuman's `HUMAN_VOICE_RULES.md §17` —
where the file name sits right next to it; see [`rule-links`](#rule-links).)

The order itself follows the reader: related rules sit next to each other,
the everyday ones come before the rare ones (BestPractice practice 36), and
the two groups a session touches least — installing the pack into a new
repo, and keeping the vendored copies current — sit at the end, where a
reader who just wants to know how to work here never has to scroll past
them. A new rule goes where it belongs rather than at the end; there is no
longer a citation cost for putting it there — the concrete steps for doing
that are [`new-rule-placement`](#new-rule-placement), below.

**Start with [`bestpractice-wins`](#bestpractice-wins) and
[`no-duplication`](#no-duplication)** — they govern how every other rule
here is applied: on conflict, this pack wins; where it only restates
BestPractice, it gets dropped. The rest, in order:

| # | Rule | What it says |
|---|---|---|
| | **Relationship to BestPractice** | |
| 1 | [`bestpractice-wins`](#bestpractice-wins) | On conflict, this pack wins; where it's silent, BestPractice stands |
| 2 | [`no-duplication`](#no-duplication) | A rule that only restates BestPractice gets dropped |
| | **Who these rules describe** | |
| 3 | [`morgan-scope`](#morgan-scope) | Morgan's pronouns, and every Morgan-specific fact scoped to Morgan actually making the change |
| | **Who, when, and where — the header and trailer on every commit and file** | |
| 4 | [`commit-author`](#commit-author) | Commit author and email |
| 5 | [`buenos-aires-dates`](#buenos-aires-dates) | Buenos Aires dates and commit timestamps |
| 6 | [`file-header`](#file-header) | Last-updated timestamp, who made it, per-file version |
| 7 | [`generated-file-marker`](#generated-file-marker) | Auto-generated files get a `.generated.<ext>` name and a "don't edit by hand" header instead of `file-header`'s own |
| 8 | [`session-trailer`](#session-trailer) | The `Session:` trailer on every commit |
| | **How a session decides, argues, and writes** | |
| 9 | [`small-calls`](#small-calls) | Decide small calls; only stop for big ones |
| 10 | [`push-back`](#push-back) | Push-back mode, on writing-and-thinking work only |
| 11 | [`trim-prose`](#trim-prose) | Trim iteratively-edited prose on two triggers |
| 12 | [`list-item-parity`](#list-item-parity) | Cocreated list items stay comparable in length; default short |
| | **How a session lands work** | |
| 13 | [`go-merge`](#go-merge) | `go`/`merge` as standing merge authorization |
| 14 | [`todo-gate`](#todo-gate) | TODO.md reconciled before every push |
| 15 | [`light-check`](#light-check) | The light check, on every commit path |
| 16 | [`deep-check`](#deep-check) | The deep check: every audit, plus an open-ended coherence review |
| 17 | [`quiet-checks`](#quiet-checks) | Don't repeat the same backlog explanation every run; "checks passed" is still fine |
| 18 | [`mirror-into-agents`](#mirror-into-agents) | Agent-relevant instructions mirrored into [AGENTS.md](../../AGENTS.md) |
| 19 | [`new-rule-placement`](#new-rule-placement) | A new pack rule lands in reading-order position, renumbered and mirrored — never appended |
| | **Documentation conventions** | |
| 20 | [`branch-links`](#branch-links) | A mentioned branch is always a link |
| 21 | [`rule-links`](#rule-links) | Anything mentioned that has a destination is a link to it — in replies as much as in files |
| 22 | [`durable-list-anchors`](#durable-list-anchors) | A durable numbered list gets a permanent slug and anchor per entry, not just a position number |
| 23 | [`brainstorm-citations`](#brainstorm-citations) | A formal document cites another formal document, never a specific point inside an explicit brainstorm document |
| 24 | [`file-mention-links`](#file-mention-links) | In chat and PR/commit text, every file mention is a clickable link, even inside code |
| 25 | [`no-stale-counts`](#no-stale-counts) | Don't state a count that will drift; describe it instead |
| 26 | [`header-caps`](#header-caps) | One header capitalization schema; NY Times headline style by default |
| 27 | [`sensitive-characterization-scrub`](#sensitive-characterization-scrub) | Scrub, or ask first, before committing a strong/negative/sensitive characterization of a real person |
| 28 | [`private-repo-scrub`](#private-repo-scrub) | Private repo names scrubbed before anything vendors |
| | **Code this pack helps write** | |
| 29 | [`llm-neutral`](#llm-neutral) | Platform-neutral LLM integrations; OpenRouter assumed |
| 30 | [`fail-gracefully`](#fail-gracefully) | Always fail gracefully |
| | **Installing the pack into a repo** | |
| 31 | [`default-branch`](#default-branch) | A repo's default branch is `main` |
| 32 | [`blank-blocklist`](#blank-blocklist) | The scrub blocklist stays blank at install |
| 33 | [`content-subdirs`](#content-subdirs) | Content-oriented repos group their deliverable content |
| 34 | [`install`](#install) | The install procedure itself |
| | **Keeping the vendored copies current (the meta rules)** | |
| 35 | [`bestpractice-sync`](#bestpractice-sync) | The scheduled BestPractice sync |
| 36 | [`pack-sync`](#pack-sync) | Its sibling: the scheduled pack sync |
| 37 | [`drift-notice`](#drift-notice) | The session-start drift notice, layered on both |
| 38 | [`fresh-check-escalation`](#fresh-check-escalation) | When the freshness check can't reach the source, say so — then verify directly |
| 39 | [`automation-issues`](#automation-issues) | Unattended automation reports its own blockers |

<a id="bestpractice-wins"></a>

### 1. On Conflict with BestPractice, This Pack Wins (`bestpractice-wins`)

BestPractice sets the default; where a rule in this pack and a rule of
BestPractice's own genuinely disagree on the same point, this pack's rule
governs — in this repo, and in every repo the pack gets installed into.
Several rules below already do this in their own particular way —
[`commit-author`](#commit-author) replaces, rather than defers to,
BestPractice's "ask before the first commit" default, and
[`small-calls`](#small-calls) sharpens its "ask when genuinely unsure"
default toward a narrower one — so this section states the general rule up
front rather than leaving a reader to notice it separately in each entry's
own reasoning. Where this pack is silent on a point, BestPractice's own rule
stands undisturbed — the pack only narrows or overrides where it actually
speaks.

<a id="no-duplication"></a>

### 2. Don't Duplicate BestPractice (`no-duplication`)

This pack exists to add to BestPractice or override it, not to restate it. A
rule here that only repeats something BestPractice already establishes on
its own — same substance, no actual change in outcome — gets dropped from
this file the next time it's touched: a restated rule is a second place for
the same idea to drift out of sync with the first, for no benefit over
leaving BestPractice's own text to stand alone. Applies at install time too
([`install`](#install) below): weaving
[templates/AGENTS_ADDENDUM.md.template](templates/AGENTS_ADDENDUM.md.template)
into a target repo's freshly-instantiated `AGENTS.md`, skip any bullet whose
substance that repo's BestPractice install already carries verbatim, rather
than installing a second copy of the same sentence.

<a id="morgan-scope"></a>

### 3. Morgan's Pronouns, and Who These Identity Rules Apply To (`morgan-scope`)

**Morgan is a man; use he/him pronouns for him.** Any document a session
writes that refers to him — a reply, a commit message, `GETTING_STARTED.md`,
a review sensitivity note, anything — uses "he"/"him"/"his", never
"she"/"her". If a document already in the repo uses "she"/"her" for him,
that's a mistake to fix in the same pass a session next touches that
document, not a repo-wide sweep on its own (the same "only the files
actually touched" scope [`file-header`](#file-header) already uses for its
own header rule).

**This rule, and every other Morgan-specific fact in this pack — his
pronouns, `git config user.name "Morgan F"` and his email
([`commit-author`](#commit-author)), Buenos Aires as *his* timezone
([`buenos-aires-dates`](#buenos-aires-dates)), `themorgan` as the
attributing GitHub username, the specific words "go"/"merge" as
authorization ([`go-merge`](#go-merge)) — apply only when Morgan is the one
actually driving the change.** They are facts about one person, not
properties of this pack's behavior in general. When a different GitHub user,
or a different person entirely, is the one making a change (co-authoring a
repo this pack is installed into, running a session on their own account,
opening their own PR against a repo that carries this pack), none of those
Morgan-specific facts apply to *them* — don't attribute their commits to
"Morgan F", don't assume their timezone is Buenos Aires, don't refer to them
as "he" absent them actually saying so, and don't require the exact word
"go"/"merge" from them if they haven't adopted that convention themselves.
Ask, or use the generic BestPractice default
([`bestpractice-wins`](#bestpractice-wins): where this pack is silent,
BestPractice stands — "ask before the first commit" is exactly the default
this restores for someone who isn't Morgan), rather than assuming the pack's
facts about Morgan describe whoever happens to be typing.

This is the same distinction the "Working in parallel" section of
[AGENTS.md](../../AGENTS.md) already draws for commit attribution generally
("commits are credited to the human driving them") — this section makes
explicit that the same applies to every other personal fact in this pack,
not just authorship, since a second contributor showing up was always the
scenario that section anticipated and this pack predates.

<a id="commit-author"></a>

### 4. Commit Author Is Always "Morgan F" (`commit-author`)

BestPractice's own convention (practice: commits credited to the human
driving the session) asks the agent to find out who that is before the first
commit. Here, that's already decided — don't ask:

```
git config user.name "Morgan F"
git config user.email "morgan@westegg.com"
```

The email is Morgan's own address, used to identify him as the author of
every commit. `tools/bootstrap.sh` runs this at session start (see
[`install`](#install) below), so it never needs to be typed by hand.

This rule replaces only the *identity* half of BestPractice's own
convention. It says nothing about co-authorship, so BestPractice's own
`Co-Authored-By:` trailer naming the assistant still applies, undisturbed —
[`bestpractice-wins`](#bestpractice-wins)'s "where this pack is silent,
BestPractice stands", in its most concrete form.

This whole rule is a fact about Morgan specifically — it applies only when
he's the one actually driving the change; see
[`morgan-scope`](#morgan-scope) for exactly what that does and doesn't carry
over to someone else.

<a id="buenos-aires-dates"></a>

### 5. Every Date Is Buenos Aires Local Time (`buenos-aires-dates`)

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
sync workflows' cron lines in [`bestpractice-sync`](#bestpractice-sync) and
[`pack-sync`](#pack-sync) need re-deriving — [TODO.md](../../TODO.md)
carries a standing reminder to re-check this the next time this file is
touched.

Buenos Aires is Morgan's own timezone specifically, not a repo-wide default
— see [`morgan-scope`](#morgan-scope) for who this does and doesn't apply
to.

<a id="file-header"></a>

### 6. A "Last Updated" Timestamp, Author, and Version — at the Top of Files, When Reasonable (`file-header`)

Markdown files get `<!-- Last updated: YYYY-MM-DD HH:MM:SS (Buenos Aires) by
NAME, to version N -->` as their first line — a full timestamp, not just a
calendar date: hour, minute, and second, in Buenos Aires local time, the
same clock [`buenos-aires-dates`](#buenos-aires-dates) already uses
everywhere else. A bare date can't tell two same-day edits apart; the time
of day can. `NAME` is whoever made the edit — "Morgan F"
([`commit-author`](#commit-author)) when Morgan is the one making the edit,
in this repo and every repo this pack is installed into (see
[`morgan-scope`](#morgan-scope) for who that does and doesn't cover), the
same name every commit is already authored as — so the header settles who
last touched the file without a reader needing to go check `git blame`;
otherwise `NAME` is simply whoever actually made the edit. `N` is a plain
integer counter *private to that one file*: 1 the first time the header is
added, incremented by 1 each subsequent time the file's content changes.
Update the line whenever you touch the file's content, not its formatting
alone — that's also the trigger for bumping `N`.

The "to version N" phrasing is deliberate: it names that one file's own
version, not a repo-wide release number, so bumping it is a one-file edit,
never a reason to touch anything else. That also means installing this rule
doesn't mean retrofitting a header onto every existing file at once — a file
only picks up (or bumps) its header when it's actually being edited for some
other reason; the header describes that file's edit history, not a standing
obligation to sweep the repo. Files in a comment-bearing format (`.sh`,
`.yml`) get the equivalent in that syntax. Skipped where it can't help: JSON
has no comment syntax, and anything under `process/upstream/` must stay a
byte-for-byte mirror of the public repo — never hand-edited, header
included.

<a id="generated-file-marker"></a>

### 7. Auto-Generated Files Are Named and Marked So Nobody Edits Them by Hand (`generated-file-marker`)

A file a script or process produces — regenerated on demand, never meant to
carry a hand edit of its own — is easy to mistake for a companion file
someone maintains directly, especially when the two live in the same
directory under similar names (a full note and a short auto-generated
summary of it, say). Two mechanisms make the difference visible without
opening the file, and this rule asks for both together, not either alone:

- **Naming.** An auto-generated file's own name carries `.generated.`
  immediately before its extension — `SUMMARY.generated.md`,
  `metrics.generated.csv`, generalized as `.generated.<ext>` for any file
  type. It shows up in a directory listing, a `git diff`, and a pull
  request's file list alike, without anyone needing to open the file first.
  This is a naming convention, not a location one: it doesn't require a
  dedicated `generated/` subdirectory (a repo already grouping content per
  [`content-subdirs`](#content-subdirs) can still do that on top), so it
  works equally well for one generated file sitting beside its hand-authored
  source and for a whole batch of them.
- **Header.** A generated file's first line (or its file format's own
  comment syntax) reads `<!-- AUTO-GENERATED by <script/process> from
  <source file(s)> — DO NOT EDIT BY HAND. Regenerate with: <command> -->`.
  This *replaces* [`file-header`](#file-header)'s own "last updated / by
  NAME / to version N" header on that file, rather than sitting beside it: a
  generated file has no hand-edit history of its own worth recording — the
  "who last touched it, when" a human editor would otherwise look for is
  exactly what this header is instead warning a human editor away from
  creating. Skip it only where [`file-header`](#file-header) already skips
  its own header for the same underlying reason — a format with no comment
  syntax (JSON), or a vendored byte-for-byte mirror under
  `process/upstream/`.

Neither mechanism is retroactive on its own: a file only picks up the suffix
and header once a real generation process for it is actually stood up, the
same "only the files actually touched" scope [`file-header`](#file-header)
already uses for its own header rule — this rule gives the convention a
name and a form, not a mandate to rename files that aren't actually
generated by anything yet. Not scoped to Morgan — a repo-hygiene habit, like
[`content-subdirs`](#content-subdirs), not a fact about one person.

<a id="session-trailer"></a>

### 8. Commit Messages Link the Session Where the Change Was Planned (`session-trailer`)

A `Session: <url>` trailer on every commit. For Claude Code,
`https://claude.ai/code/session_<ID>`. For the unattended sync
([`bestpractice-sync`](#bestpractice-sync)), which has no chat session
behind it, the workflow run's own URL stands in. If a tool has no shareable
link at all, the trailer says so explicitly (`Session: none available
(<tool>)`) rather than being silently omitted — so a reviewer can tell
"considered and skipped" from "forgotten" at a glance.

<a id="small-calls"></a>

### 9. Decide Small Calls Yourself; Only Stop for Big Ones (`small-calls`)

Default to continuing, not asking. When a judgment call is needed to keep
the work moving — filling in a default, picking between two reasonable
implementations, resolving an ambiguity that doesn't change the shape of
what gets delivered — make the call and note it in the normal end-of-work
reply, rather than stopping to ask first. Reserve stopping and asking
(BestPractice's own `AskUserQuestion` or equivalent) for calls that are
genuinely big: hard or costly to undo, change what gets delivered or to
whom, spend real money, touch credentials or production, or are the kind of
toss-up where two reasonable people would clearly land in different places.

A small or moderate call made this way still gets surfaced, just not as an
interruption: it goes in **both** places — the same end-of-work reply that
already lists files touched (practice 12), *and* the commit message itself,
under a "Judgment calls made:" heading, the same way the sync
([`bestpractice-sync`](#bestpractice-sync)) already lists its own judgment
calls under "Judgment calls to review:" rather than blocking on each one.
The chat reply is easy to miss once a thread scrolls on; the commit message
is the one copy that survives into `git log` and the PR diff, where it stays
visible for as long as the repo does — so a member reviewing a merged PR
later (not just reading the reply in the moment) can still see what was
decided on their behalf. Skip the heading only when a commit truly made no
judgment calls — don't pad it with "none" noise on every commit, but never
omit it when a call was actually made. This sharpens BestPractice's own "ask
when genuinely unsure" default toward Morgan's own risk tolerance: most
calls in day-to-day work here (a wording choice, which of two valid layouts
to use, a template's exact phrasing) are small enough to just make.

<a id="push-back"></a>

### 10. Push-Back Mode: Argue, Don't Just Comply, on Writing-and-Thinking Work (`push-back`)

[`small-calls`](#small-calls) governs *judgment calls*: filling in a
default, picking between two fine implementations, resolving an ambiguity
that doesn't change what gets delivered — decide those yourself. This rule
governs something different: *contested reasoning* on work where the
deliverable is prose meant to persuade or be judged by a human reader as an
argument — a memo, a strategy call, a brainstorm entry, an essay, a decision
writeup — rather than work meant to run.

**Never applies to code, scripts, configuration, infrastructure work,
debugging, or any other technical task Morgan asks for** — including a
technical sub-conversation happening inside a repo, session, or document
that also does writing-and-thinking work elsewhere. The test is what the
*current piece of work* is for, not which repo or file it lives in: a
design-doc conversation about tradeoffs is push-back mode; the
implementation that follows from it is not, even in the same session, even
in the same file.

Two mechanisms:

- **Reactive.** When Morgan states a stance or a framing, and there's a
  genuine, serious counter-case worth making, make it before building on the
  stance as given — don't silently adopt it and proceed as if it were
  already settled.
- **Proactive.** Before handing over a finished piece of this kind of
  writing, if there's something that seriously matters left unresolved or
  disputable, say so before calling the piece done.

**Never push back just to push back.** This is not a quota — it does not
require finding an objection in every exchange, and a piece with no real
problem should be handed over as-is, stated plainly as such, rather than
manufacturing a disagreement to satisfy this rule. Reserve pushback for
where it could actually help in a serious or deep way: a claim that might
not hold up, a framing that's quietly doing too much work, an option that
was dismissed too fast. Surface-level notes (wording, tone, a
[`small-calls`](#small-calls)-sized call) stay in
[`small-calls`](#small-calls)'s lane, not this one. Morgan can also opt out
for a specific exchange — "just record this," "no pushback needed here" —
for cases like dictating a quote or logging something verbatim, without
triggering the back-and-forth.

**This rule is less objective than almost everything else in this pack, and
that's worth stating plainly rather than dressing it up as mechanically
enforceable.** Nearly every other rule here is checkable — a git config
value, a file's presence, a timestamp format, a workflow that either ran or
didn't. This one isn't: nothing here can distinguish, from the outside, a
session that stayed quiet on a real problem out of excessive deference from
one that correctly found nothing serious to say, or a session performing
disagreement it doesn't actually have from one raising a genuine one. The
rule leans entirely on the model's own honest judgment about whether a given
disagreement is real and worth the interruption. There's no mechanical fix
for that; the best available check is Morgan noticing, over time, whether
pushback shows up when it should and stays quiet when it should — and saying
so if the calibration drifts.

<a id="trim-prose"></a>

### 11. Trim Iteratively-Edited Prose on Two State-Free Triggers, Not a Running Count (`trim-prose`)

Prose that gets tweaked repeatedly in the same conversation — a paragraph
revised, then revised again — tends to only grow: each pass adds a clause or
qualifier without anyone removing what the new wording made redundant. Left
unchecked, the result is a paragraph several times its original length,
carrying the same point plus a pile of overlapping caveats.

The fix is a trim pass, but not one gated on a running count — edits since
the last trim, or current length against some earlier baseline. That
requires state persisted across edits, and often across sessions, at a cost
disproportionate to a minor problem. Use two cheap, state-free triggers
instead:

- **Immediate, on a substantial edit.** The moment a paragraph gets a
  substantial edit — a rewritten sentence, or roughly a sentence or more
  added — give just that paragraph a quick trim before moving on. This
  piggybacks on work already happening (the paragraph is already open and
  being reworked) rather than adding a separate scan.
- **Before calling the piece done.** Independent of edit size, if a
  paragraph has grown noticeably longer than the point it's making warrants,
  trim it before finishing. This catches slow drift from a run of edits each
  too small on its own to trigger the first bullet.

Both fire at a checkpoint that already exists — making an edit, declaring
the piece finished — not from a mechanical count: no counters, no stored
baselines, no separate audit pass over paragraphs nothing touched.

Scoped the same as [`push-back`](#push-back): prose meant to be read and
judged by a human — docs, memos, emails, brainstorm entries — not code,
scripts, configuration, or other work meant to run. Not scoped to Morgan — a
writing-quality habit, not a fact about one person, so it applies regardless
of who is driving the session.

<a id="list-item-parity"></a>

### 12. Cocreated List Items Stay Roughly Comparable in Length — Default Short (`list-item-parity`)

When cowriting a list, or a document with several short-ish sections in a
row that function like one (each entry covering comparable ground — a set
of options, a set of rules, a set of findings), keep each item to
approximately the same length as its neighbors. This matters most during
revision: it's natural to edit one point, expand it while you're in there,
and leave the others untouched — even though nothing about that item's
actual importance grew relative to the rest. Left unwatched, the list ends
up looking like it ranks items by how recently someone touched them rather
than by what they're worth.

**If one item genuinely carries more weight than the others, that's a signal
to reconsider its place in the list, not a license to let it balloon
in place.** Check whether it makes more sense to pull it out of the list
entirely and give it its own section — special treatment for a genuinely
special point, rather than a list that quietly stops being a list of peers.

**Watch for this at both ends: when a list is first drafted, and every time
an existing item in one gets revised.** The failure mode this rule exists to
catch is specifically the second one — a list that started balanced and
drifted lopsided one edit at a time.

**Default to the shorter side for list items and list-like sections, not the
longer side, unless explicitly told otherwise.** Absent a specific
instruction to go long on a given item, err toward brevity — a list is
easier to scan and to keep in parity when every entry already tends short.

**This is a strong preference, not a hard rule.** There are foreseeable
exceptions — a list where the items are genuinely, legitimately uneven in
what they need to say, or where padding a short item just to match its
neighbors would make it worse, not better. Use judgment
([`small-calls`](#small-calls)) rather than mechanically padding or trimming
to force parity that doesn't fit the content.

Scoped the same as [`push-back`](#push-back) and [`trim-prose`](#trim-prose):
a writing-quality habit that applies to cowritten prose and documents, not to
code, scripts, or configuration. Not scoped to Morgan — it applies regardless
of who is driving the session.

<a id="go-merge"></a>

### 13. "go" or "merge" as a Standalone Final Sentence Authorizes Commit + Merge (`go-merge`)

If Morgan's message, at a point where you've said you're ready to commit (or
ready to commit and merge), ends with `go` or `merge` standing alone as its
own sentence — case-insensitive, whether that's the whole message on one
line or the last sentence of a longer one, set off by ordinary
sentence-ending punctuation — treat it as his authorization, right there, to
commit the pending work and merge it into the default branch, following this
repo's usual conventions (author identity, Buenos Aires timestamp, session
trailer, the audits) without asking again first. "That was perfect. merge",
"Go.", and a lone line reading `MERGE` all count; "let's merge the two
lists" and "go check the logs" don't, because there the word is part of a
longer sentence, not standing alone as the message's last one. This isn't a
new kind of permission — it's shorthand for the same authorization
BestPractice's own "merge only when the user says so" default already asks
for (woven into every installed `AGENTS.md`'s Git / workflow section); `go`
and `merge` are just the standalone forms that count as saying so. Where
context leaves it ambiguous whether the trailing word is this shorthand or
just part of the sentence's own meaning — or where multiple pending items
make it unclear what "merge" would even apply to — don't assume: ask.

This exact wording is Morgan's own shorthand specifically — see
[`morgan-scope`](#morgan-scope) — not something to expect or require from
anyone else driving a change in a repo this pack is installed into.

<a id="todo-gate"></a>

### 14. TODO.md Gets Reconciled Before Every Push (`todo-gate`)

Woven into the installed [AGENTS.md](../../AGENTS.md)'s merge runbook as
step 0c, right after BestPractice's own capture gate (0) and export gate
(0b): before pushing, check the thread's discussion against
[TODO.md](../../TODO.md) — add ideas that came up but never got a line,
remove or check off what this branch just implemented. `TODO.md` drifting
out of sync with what was actually decided is common enough in practice that
it earns its own gate rather than staying an occasional "oh, I should update
that" afterthought.

<a id="light-check"></a>

### 15. A Light Check Runs on Every Commit Path (`light-check`)

[tools/light_check.py](tools/light_check.py) — merge-conflict markers,
invalid JSON/YAML/Python syntax, secret-shaped strings (an AWS-style key ID,
a private-key PEM header, a GitHub token), broken relative doc links, and
(repo-wide, every run, regardless of what changed) that `process/personal/`
is actually vendored: `process/manifest_personal.json` exists, parses, has
at least one entry, and every entry's `local_path` exists on disk. That last
check exists specifically to catch the pack having been dropped into a repo
by a plain copy rather than installed per [`install`](#install) below —
copying gets you the files but not the tracked provenance (upstream commit,
per-file hashes) that makes the pack auditable and syncable, and a `cp -r`
won't necessarily touch `manifest_personal.json` at all, so this can't be
scoped to changed files the way the other checks are. BestPractice's
[doc_lint.py](../upstream/tools/doc_lint.py) is Markdown-specific
(accidental strikethrough, unlinked references, unglossed acronyms); this is
the broader, cheaper net for "something obviously went wrong" that isn't a
style question. Run it yourself before every commit, same as `doc_lint.py`;
it's also wired as
[templates/github-actions/light-check.yml.template](templates/github-actions/light-check.yml.template)
→
[.github/workflows/light-check.yml](../../.github/workflows/light-check.yml)
so it binds every path to the default branch even when a session forgets —
the same reasoning BestPractice's own [TODO.md](../../TODO.md) gives for
preferring required CI checks over runbook steps alone. This is also why the
vendoring check belongs in `light_check.py` specifically rather than only in
prose here: once a repo has installed the pack, this check is already wired
into that repo's own CI on every push and PR, so a future session (or
person) that drops `process/personal/` into a *new* repo without going
through [`install`](#install) gets caught the moment `light-check.yml` runs
— install-time correctness enforced automatically, not just documented.

<a id="deep-check"></a>

### 16. The Deep Check: Every Audit, Plus an Open-Ended Coherence Review (`deep-check`)

BestPractice practice 44 asks every repo for two named check levels, and
[GLOSSARY.md](../../GLOSSARY.md) names this pack's pair: the **light check**
([`light-check`](#light-check), every commit) and the **deep check**. This
section says what the deep check actually is, so that "deep check" is
something Morgan can ask for by name and get the same thing every time.

**The mechanical half — every audit, all three:**

```
python3 process/upstream/tools/doc_lint.py
python3 process/personal/tools/light_check.py
python3 process/upstream/tools/practice_audit.py
```

([doc_lint.py](../upstream/tools/doc_lint.py),
[light_check.py](tools/light_check.py),
[practice_audit.py](../upstream/tools/practice_audit.py).) This half is the
merge runbook's step 3 ([AGENTS.md](../../AGENTS.md)) and runs on every
merge, unprompted. All three must pass before the merge commits.

**The review half — a read of the repo's own rules and documents against
each other.** The audits catch broken links, bad syntax, and an unscrubbed
blocklist hit; they can't catch a rule that now contradicts another rule, or
a section that stopped making sense three edits ago.

**Scope: the whole repo, not just the pack.** In a repo that vendored this
pack, the review covers everything that repo has written for itself — its
own `AGENTS.md`, `README.md`, [MAP.md](../../MAP.md),
[GLOSSARY.md](../../GLOSSARY.md), [TODO.md](../../TODO.md),
`GETTING_STARTED.md`, its deliverable content, its scripts and workflows —
*and* the vendored `process/personal/` tree, *and* the fit between the two:
a repo-local rule that contradicts a pack rule, an install step whose output
no longer exists, a pack rule the repo silently stopped following. The one
exception is `process/upstream/`, which is a byte-for-byte mirror and is
never edited locally — read it to check the repo against it, never to fix it
in place ([`bestpractice-sync`](#bestpractice-sync) is how that tree
changes). A deep check that only looked at the pack would miss most of what
actually drifts in a working repo.

**What to look for. This list is a starting point, not a specification — the
point of the review is to find what's wrong, including the kinds of wrong
nobody has thought to list yet.** Anything that makes the repo harder to
trust or follow belongs in the report, whether or not it matches a bullet
below:

- **Contradictions** — two rules that can't both be followed, or a rule
  whose own carve-outs have eaten it.
- **Stale references** — a slug, practice number, filename, heading, or
  click-path that points at something that moved or no longer exists; a
  positional number cited as if it were a name
  ([`rule-links`](#rule-links)); numbering that skips, repeats, or runs out
  of order; an orphaned name — a repo, tool, or file this repo mentions by a
  name it no longer goes by, once a rename elsewhere left the old name
  sitting in this repo's own prose. The trigger is a rename the session
  already knows about — it made the rename, or was told about it — not a
  standing audit of every name this repo happens to mention; nothing here
  watches other repos for renames on its own.
- **Fragments** — a sentence, note, or heading left behind by an earlier
  edit: a "temporary" caveat whose occasion has passed, a note about a
  reorganization that already happened.
- **Needless repetition** — the same rule stated in full in several places,
  where one statement plus pointers would do
  ([`no-duplication`](#no-duplication) is the same instinct, pointed at
  BestPractice rather than at this repo).
- **Disproportion** — paragraphs of detail on a minor point, or a rule
  buried in a group that no longer fits it (practice 36's ordering, and this
  file's own reading order).
- **Formatting and spacing** — inconsistent heading levels and
  capitalization ([`header-caps`](#header-caps)), a bullet that lost the
  blank line its neighbours have, mixed list markers or indent widths, a
  table whose columns no longer line up, stray double blank lines or
  trailing whitespace, a code fence with no language, wrapping that suddenly
  changes width mid-document, a missing or stale "last updated" header
  ([`file-header`](#file-header)).
- **Self-application** — a rule this pack asks of every repo it installs
  into that this repo doesn't yet follow itself
  ([`header-caps`](#header-caps) was exactly this).
- **[TODO.md](../../TODO.md) drift** — items already done, no longer
  relevant, or never actually decided; [`todo-gate`](#todo-gate) is the
  per-push version of the same check.
- **Anything else the read turns up.** If something is wrong and none of the
  categories above name it, it is still a finding — report it, and if it's
  the kind of thing that will recur, add a bullet here so the next deep
  check looks for it deliberately.

Fix what the review turns up in the same pass — these are
[`small-calls`](#small-calls)-sized almost every time — then re-run the
mechanical half, since the fixes themselves can break a link. Anything
deliberately left alone gets a line in [TODO.md](../../TODO.md) saying so,
rather than being silently dropped.

**When it runs.** The mechanical half: every merge, per the runbook. The
full deep check, both halves: whenever Morgan asks for one by name ("deep
check"), and whenever a session has just done the kind of work that invites
drift — a batch of rules added or reordered, a rule that changed shape, an
install into a new repo, or a merge that resolved conflicts in several
shared files. It is deliberately not a per-commit gate: the review half
costs a careful read of the whole repo, which is exactly why
[`light-check`](#light-check) exists to carry the cheap checks on every
commit instead.

<a id="quiet-checks"></a>

### 17. Don't Repeat the Same Backlog Explanation Every Run (`quiet-checks`)

The merge runbook's step 3 ([AGENTS.md](../../AGENTS.md)) runs the deep
check's mechanical half — [doc_lint.py](../upstream/tools/doc_lint.py),
[light_check.py](tools/light_check.py), and
[practice_audit.py](../upstream/tools/practice_audit.py) — before every
merge, and each of those can report a real backlog: `doc_lint.py --all`
alone turns up a substantial pre-existing pile of "unlinked file reference"
and "unglossed acronym" warnings across this repo's own docs, none of it
caused by the branch being merged, none of it gated (`doc_lint.py`'s own
scope is files changed vs the default branch — "fix what you touch," per
[AGENTS.md](../../AGENTS.md)'s Conventions section).

**This targets one specific habit, not check-reporting in general: a session
that explains away that same unchanging backlog with the same sentence every
single commit** — "pre-existing warnings only, unrelated to my edit," or an
equivalent restatement — is repeating a disclaimer that never changes and
never informs the next step; the runbook already moves on to checking branch
state and committing regardless of what that sentence says. Drop that
specific recurring explanation.

**This does not mean staying silent about checks in general.** A plain
"checks passed" (or "checks failed, here's why") is normal, often exactly
what's wanted, and stays fine wherever reporting status is the natural thing
to do — an end-of-work summary, a reply wrapping up the task just finished,
anywhere a person would want to know the outcome. The distinction is between
*reporting an outcome*, which is fine, and *re-explaining the same known,
static backlog* every time as though it were new information, which isn't.

**Concretely:** run the checks; if the result is clean, either say so
plainly and move on, or say nothing and move on — both are fine, and it's
ordinary judgment about the reply's context which fits better. What doesn't
belong is a repeated aside walking through *why* the warnings don't matter
(they're pre-existing, they're unrelated to this edit, the count) on every
single run — say that reasoning once if it's genuinely useful context, never
as boilerplate. A run that actually failed, or a warning the current edit
introduced that wasn't already sitting in the backlog, is new information
every time and always worth flagging.

Not scoped to Morgan — like [`branch-links`](#branch-links) and
[`rule-links`](#rule-links), this is a habit about how a session
communicates, not a fact about one person.

<a id="mirror-into-agents"></a>

### 18. Agent-Relevant Instructions in a README or Other Key File Also Go in AGENTS.md (`mirror-into-agents`)

`AGENTS.md` is the file a session is told to read first (BestPractice's own
entry-point convention); a README, a `CONTRIBUTING.md`, a
[GETTING_STARTED.md](../../GETTING_STARTED.md), or any other key file can
still pick up its own operational instructions over time — a setup step, a
gotcha, a rule about how to work in the repo — written where a human reader
would look for it, not where an agent is told to look. When any such file
gains an instruction that would be useful for an agent to know (not general
project description, not end-user documentation — the operational kind: how
to build it, a constraint on how to work, a step an agent would otherwise
miss), fold the same instruction into `AGENTS.md` too, in its own words if
that reads better there, rather than leaving it stranded in the other file
for an agent to find only by accident. This runs both ways an author might
add such a line — whether it lands first in the README (or other key file)
and needs pulling into `AGENTS.md`, or is written into `AGENTS.md` directly
and never mirrored back to where a human would expect to read it; either
direction, the same instruction ends up in both places. It does not run the
other way for content that only belongs in one place: a README's marketing
framing, install screenshots, or badges have no business in `AGENTS.md`, and
`AGENTS.md`'s own meta-structure (the quick index, the merge runbook
mechanics) has no business padding out a README written for a human skimming
the repo for the first time. Check for this at the capture gate (merge
runbook step 0, [AGENTS.md](../../AGENTS.md)) the same way any other
captured decision gets folded in — a stray instruction left in only one file
is exactly the kind of drift that gate exists to catch.

<a id="new-rule-placement"></a>

### 19. A New Pack Rule Lands in Reading-Order Position, Never Appended (`new-rule-placement`)

"The Rules, and Why" (above) already states the design intent — related
rules sit together, everyday rules before rare ones, and a new rule goes
where it belongs rather than at the end, since the slug carries every
citation and the position number carries none. That's reasoning a session
has to reconstruct from the front matter each time; this rule makes it an
actual, repeatable checklist instead — the same gap
[`quiet-checks`](#quiet-checks) closed for how a session reports a check,
and [`no-stale-counts`](#no-stale-counts) closed for how a session states a
count.

**When adding a new rule to this pack:**

1. Pick where it belongs by subject, among the existing groups (the table's
   own section headers) — not at the end of the file, and not wherever the
   diff happens to be easiest to write. If no existing group fits, that's a
   signal the groups themselves may need a fresh look, not a reason to bolt
   the new rule onto the last one.
2. Assign it a permanent slug now — never renumbered later — and an
   `<a id="slug"></a>` anchor, in [`rule-links`](#rule-links)'s citation
   form.
3. Renumber every rule after the insertion point by one, in both the
   headings and the group table, so the reading order stays a single
   unbroken 1-to-N sequence with no gaps or duplicates. Check for any prose
   — including this file's own front matter — that names the total count in
   passing; [`no-stale-counts`](#no-stale-counts) is exactly the rule
   against leaving one of those stale.
4. Mirror the new rule everywhere [`mirror-into-agents`](#mirror-into-agents)
   and [`install`](#install) already require it to live: the woven bullet in
   `AGENTS.md`'s Personal Setup Rules, in the same reading-order position
   (the `agents-addendum` manifest entry's own "one bullet per README.md
   section, in README.md's own reading order" convention), the install
   template
   ([templates/AGENTS_ADDENDUM.md.template](templates/AGENTS_ADDENDUM.md.template)),
   `MAP.md`'s rule table, and `NEW_REPO_SETUP.md`'s group-by-group
   enumeration.
5. Re-run [`light-check`](#light-check) — it fails a bare `§N` citation and
   a slug with no matching anchor — and record the addition as a `TODO.md`
   decision entry ([`todo-gate`](#todo-gate)).

**Enforced only in part.** [`light-check`](#light-check) catches a broken
slug citation or a stray `§N` reference to a pack rule; nothing mechanically
checks that a new rule actually landed in the right group, or that every
mirror picked it up. That gap is exactly what
[`deep-check`](#deep-check)'s review exists to catch — adding a rule to the
pack is already one of the "work that invites drift" triggers
[`deep-check`](#deep-check) names for running one.

Not scoped to Morgan — a documentation-quality habit, like
[`rule-links`](#rule-links) and [`no-stale-counts`](#no-stale-counts).

<a id="branch-links"></a>

### 20. A Mentioned Branch Is Always a Link (`branch-links`)

BestPractice's own practice 11 (doc references are links) covers files at
the repo's current tree — a relative markdown link, not a bare backticked
filename. It doesn't reach a git branch: a branch name isn't a path at the
current tree, it's a ref, so a relative link doesn't apply to it the same
way. This rule closes that gap: **any time a reply names a git branch — not
only in the Files-touched footer practice 12 already requires, but anywhere
in running text, a status update, a decision note — link it**, the same
underlying reasoning as practice 11 extended to cover refs as well as paths.
Link to that branch's tree view on whichever host the repo actually lives on
(for GitHub: `https://github.com/<owner>/<repo>/tree/<branch-name>`); a repo
whose remote points elsewhere uses that host's own equivalent view. A bare
branch name in backticks or plain prose is the failure mode this rule exists
to catch, the same way an unlinked filename is what practice 11 catches.
Applies to a branch in this repo and to a branch in any other repo a reply
happens to mention (a sibling PR, a related project) — link to that branch
on its own host, not this repo's.

This isn't scoped to Morgan the way [`morgan-scope`](#morgan-scope)'s facts
are — it's a documentation-quality habit, not a fact about one person, so it
applies regardless of who is driving the session.

<a id="rule-links"></a>

### 21. A Mentioned Rule, Item, or Destination Is Always a Link (`rule-links`)

[`branch-links`](#branch-links) closed the gap practice 11 (doc references
are links) leaves for a git branch — a ref, not a path, so a relative
markdown link doesn't reach it the same way. This rule closes the rest of
it, and states the general principle both are instances of: **anything
mentioned that has a destination gets a link to that destination, the first
time it's mentioned.** Naming a thing and leaving the reader to go find it
is the failure mode; it costs the writer a few seconds and the reader a
search every single time.

**Where it applies: any prose either of us writes** — a document in the
repo, a commit message, a PR description, and **a reply in chat**, which is
the one people forget. A reply that says "fixed in the header rule, see the
TODO item" is exactly as unhelpful as a document that says it; a reply is
usually *more* disposable, which is why it needs the links more, not less.

**What has a destination:**

| Mentioned | Links to |
|---|---|
| A file in the repo | Its path — practice 11's own rule, relative markdown link, never a bare backticked name |
| A rule of this pack | Its anchor, in the canonical form below |
| A BestPractice practice, a [TODO.md](../../TODO.md) entry, a [GLOSSARY.md](../../GLOSSARY.md) term, a decision record, a `process/manifest*.json` entry | The file it lives in, with the specific thing named in the link text, and its anchor where the host renders one |
| A git branch | Its tree view on that repo's own host ([`branch-links`](#branch-links)) |
| A commit | The commit page (`…/commit/<sha>`), the short SHA as the link text |
| A pull request or issue | Its page. GitHub auto-links `#43` in comments, but *not* in repo markdown, which is where the gaps show up |
| A service, tool, spec, standard, or documentation page named in prose | Its canonical page |

**First use, not every use.** Link a thing the first time a given document
or reply names it, then use the plain name after that. A paragraph that
links the same service four times is worse than one that links it once —
this rule is about the reader being able to get there, not about maximizing
link density.

**Not inside code.** A URL, path, or filename inside a code span or code
block is a value — a config setting, a template, a command to run — not a
reference. Leave it alone.

For this pack's own rules the link has one canonical form, and it is not
optional:

- From another file in the repo: ``
  [`deep-check`](process/personal/README.md#deep-check) ``
- From inside this file: `` [`deep-check`](#deep-check) ``
- In a file where markdown links don't render (a script comment, a YAML
  prompt, a manifest note): `` `deep-check`
  (process/personal/README.md#deep-check) ``

The link text is the slug, because the slug is the rule's permanent name
(see "The Rules, and Why" above). A positional number — a bare `§` followed
by a digit, or "rule 14" — is never a citation: it names where the rule sits
today, not which rule it is, and [`light-check`](#light-check) fails a
commit that uses one for a rule of this pack. `§` still belongs to a
document we don't control the numbering of — BestPractice's own sections
(`INSTALL.md §2`), or another vendored pack's own numbered file (SoundHuman's
`HUMAN_VOICE_RULES.md §17`) — cited with that file's name right next to it.
The check recognizes the shape generically (any `<Filename>.md §N`), not a
fixed list of filenames, so a newly vendored pack needs no separate update
here (found via a real false positive against SoundHuman's own numbering,
2026-08-29), and the same file-qualified form is the general citation for
any other document's own reference-able, independently-numbered rules or
protocols too — this repo's included, should one ever gain its own outside
this file. The one carve-out is a bare `README.md`: in this repo's
convention that's always this pack's own file, so it still forces the slug
form rather than exempting it.

That slug half is the only part a script can check. The rest — a commit, a
PR number, an external page — can't be told from ordinary prose mechanically
without flagging every hex string and every product name, so it stays a
judgment call, caught by [`deep-check`](#deep-check)'s review rather than by
a gate.

This isn't scoped to Morgan the way [`morgan-scope`](#morgan-scope)'s facts
are — like [`branch-links`](#branch-links), it's a documentation-quality
habit, not a fact about one person, so it applies regardless of who is
driving the session.

<a id="durable-list-anchors"></a>

### 22. A Durable Numbered List Gets a Permanent Slug and Anchor per Entry, Not Just a Position Number (`durable-list-anchors`)

[`rule-links`](#rule-links) already draws this line for the pack's own
rules: cite by permanent slug — `` [`slug`](process/personal/README.md#slug) `` —
never by the heading number, because the number moves whenever the file
is reorganized and the slug never does. This rule generalizes that same
fix to any repo's own content, not just this pack: **a numbered list
whose entries hold real, durable content — standing rules, named ideas,
arguments meant to last — likely to be cited elsewhere as "item N" or
"rule N," gets the identical treatment.** Each entry gets a permanent
`<a id="slug"></a>` anchor; every citation to it, anywhere, uses
`` `slug` (file.md#slug) ``; the visible number stays in the list purely as
reading-order furniture nobody actually cites.

**Found the hard way, in a dependent repo.** A session
folded a new idea into an existing numbered item as an awkward corollary,
specifically to dodge the sweep of renumbering every "item N"
cross-reference a plain insertion would have forced — the exact failure
this rule exists to prevent. A slugged list has nothing to renumber:
insert the new entry wherever it actually belongs, in reading order, and
every existing citation keeps working untouched. Position-only numbering
makes every future insertion a choice between distorting the list's own
logical order (bolting the idea onto whatever's nearby) or paying for a
repo-wide citation sweep; a slug removes that choice, the same removal
[`new-rule-placement`](#new-rule-placement) already banks on for this
pack's own rules.

**Which lists this covers, and which it doesn't.** The line is whether an
entry is genuinely likely to be **cited elsewhere, by position, on its
own** — a repo's own core-philosophy list, a numbered rules-for-running-
the-company essay, a rules-in-force checklist are exactly this shape. A
**short bullet list** — three or four quick options, a table row set, a
"not yet ready" set of open questions — doesn't need it: the overhead of
assigning and maintaining slugs would outweigh any benefit, since nothing
outside the list is likely to reference one bullet by position in the
first place. This extends to an explicit brainstorm document's own
numbered entries too, where one exists
([`brainstorm-citations`](#brainstorm-citations), below, governs whether a
*formal* document may cite one — this rule is orthogonal, about whether
the brainstorm's own internal cross-references, like one entry noting
it's "a corollary of" an earlier one, survive the brainstorm's own
append-only growth without drifting).

**Mechanics, matching [`rule-links`](#rule-links)'s own form exactly:**

- An `<a id="slug"></a>` immediately above each entry — its own heading if
  the list already uses real headings, or immediately before the bold
  lead-in paragraph if it doesn't (COMPANY_BUILDING_RULES.md's fifteen
  rules are exactly this second shape today: bold paragraphs, no
  headings — the anchor works the same either way, since it's an
  invisible HTML target, not a heading itself).
- The slug is assigned once, at the entry's creation, and never changes —
  not when the list is reordered, split, or the entry is retitled.
  [`no-stale-counts`](#no-stale-counts) already asks not to state a count
  that will drift; a positional citation is the same failure applied to
  an individual entry instead of a total.
- Every citation, in every file and in chat, uses `` `slug` (file.md#slug) `` —
  never a bare "item N" / "rule N", the same failure
  [`rule-links`](#rule-links) already calls out for this pack's own rules,
  now extended to any repo's own durable lists.
- The visible position number stays in the heading or paragraph lead-in as
  a reading-order aid for a human skimming top to bottom — it is not, and
  never becomes, a citable identifier.

**A heading-based list still needs its own explicit anchor, not just
GitHub's auto-generated one.** GitHub derives a heading's anchor from its
rendered text, number included (`### 7. Contradiction-Scanning...` becomes
`#7-contradiction-scanning...`) — so even a list that already uses real
headings silently breaks every citation to it the moment an entry is
renumbered, unless an explicit `<a id="slug"></a>` decouples the two the
same way this pack's own rules already do.

Not scoped to Morgan — a documentation-quality habit, like
[`rule-links`](#rule-links), so it applies regardless of who is driving
the session or which repo the pack is installed into.

<a id="brainstorm-citations"></a>

### 23. A Formal Document Cites Another Formal Document, Never a Specific Point Inside the Brainstorm (`brainstorm-citations`)

Some repos keep an explicit brainstorm document — a running, loosely
organized dump of raw ideas, dropped in as they occur, explicitly not
vetted prose (the same "raw material versus deliverable" distinction
[`content-subdirs`](#content-subdirs) already draws, one level up: the
brainstorm is where an idea starts, not where it's meant to be trusted
from). [`rule-links`](#rule-links) says anything mentioned gets a link to
its destination; that default has a blind spot here. A **formal
document** — an essay, a theory or reasons write-up, a rules-in-force
checklist, anything meant to state a settled or settling claim — citing a
specific entry, numbered item, or open question inside the brainstorm as
that claim's own support borrows a credibility the brainstorm entry never
earned: it's raw material precisely because nobody has argued it through
yet, so pointing at it as though it were backing is citing an idea to
itself.

**The rule: a formal document links another formal document for a
substantive point, never a specific entry inside a brainstorm document.**
If the idea a formal document wants to cite hasn't actually been promoted
into some formal document's own text yet, don't cite the brainstorm entry
as a stand-in — add the idea to whichever formal document it fits (a
sentence, a corollary, a new small item — [`list-item-parity`](#list-item-parity)
governs how), then link there instead. This is the "promote a cluster of
brainstorm entries once they earn a formal document" move a repo with
this kind of pipeline typically already has, applied one level down: to a
single citation, not a whole section.

**What this doesn't reach:** a document's own provenance note ("promoted
out of the brainstorm," "started as a brainstorm entry") states a true
fact about that document's history, not a citation used as support for a
claim, and stays fine linking to the brainstorm directly. Likewise,
linking the brainstorm document itself as an object — pointing a reader
there to browse it, or noting where new raw material should go — isn't
the pattern this rule catches; only a specific interior point cited as
justification is.

Not scoped to Morgan — a documentation-quality habit, like
[`rule-links`](#rule-links), so it applies regardless of who is driving
the session in a repo that keeps a brainstorm document of this kind.

<a id="file-mention-links"></a>

### 24. In Chat and PR/Commit Text, Every File Mention Is a Clickable Link — Even Inside Code (`file-mention-links`)

[`rule-links`](#rule-links) already says a file gets linked "the first time
it's mentioned," using a relative markdown link, and explicitly leaves a
filename inside a code span alone — a value, not a reference. Both defaults
are right for a document actually committed to the repo, where a relative
link resolves and a reader can scroll back to find the first one. Neither
holds outside a committed file: a session's own chat replies, and prose
written straight to GitHub (a PR description, a commit message — the
"release notes" a member actually reads) aren't part of the repo tree, so a
relative link doesn't resolve there at all, and a reader skimming a long
reply or PR body has no "first one" to scroll back to — they want whichever
mention is in front of them to work.

**The rule, for those two surfaces only** — a chat reply; a PR description,
issue, or commit message aimed at GitHub — **never inside a document
actually committed to the repo, where [`rule-links`](#rule-links)'s own
defaults stand unchanged:**

- Every mention of a specific file in the repo is a clickable link to that
  file on GitHub, not only the first mention in a given reply or PR body.
- It stays inside its code span rather than growing a separate marker like a
  trailing 🔗: `` `AGENTS.md` `` becomes
  `` [`AGENTS.md`](https://github.com/<owner>/<repo>/blob/<branch>/AGENTS.md) ``
  — the same monospace text as today, now clickable.
- Absolute GitHub URLs only
  (`https://github.com/<owner>/<repo>/blob/<branch>/<path>`) — a relative
  link doesn't resolve on either surface.
- **Which branch:** whichever one the discussion is actually about — an open
  PR's own head branch while it's still open, the default branch once it's
  merged or the reply isn't tied to a particular PR — the same choice the
  "Files touched" footer already makes for its own two links (practice 12).

Not mechanically enforced — a chat reply and a PR/commit body both live
outside anything [`light-check`](#light-check) or [`deep-check`](#deep-check)
can scan, so this rides on session habit alone, the same as
[`quiet-checks`](#quiet-checks). Found via a direct ask: a member wanted to
click whichever file mention was in front of him — in a reply or in a PR
body — without hunting for wherever the first link happened to land, or
leaving the page to go find the file by hand. Not scoped to Morgan — a
documentation habit, like [`branch-links`](#branch-links).

<a id="no-stale-counts"></a>

### 25. Don't State a Count That Will Drift — Describe It Instead (`no-stale-counts`)

Prose that cites an exact count of something that changes over time — how
many numbered rules this pack has, how many warnings a lint tool currently
reports, how many items sit in a growing list — reads precisely today and
goes stale the moment that thing changes, with nothing to flag it: no audit
checks a sentence like "Twenty-nine numbered sections" against the actual
count, so it just sits there being wrong until a session happens to notice.
Both halves of that example are real: [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md)
said "Twenty-nine numbered sections" while the pack already had thirty, and
[`quiet-checks`](#quiet-checks)'s own text, written the same day, cited
"over a hundred" pre-existing warnings — a figure that shifts on nearly
every edit to the files it describes. Both are fixed as part of adding this
rule.

**When the exact count isn't the point being made, don't state it.** Most of
these sentences only need to convey "there are several," "the list grows,"
"a real backlog exists" — not the precise figure. Rewrite to the qualitative
form: "numbered sections" instead of "twenty-nine numbered sections," "a
real backlog" instead of "over a hundred warnings." Dropping the number
outright is usually the right fix — not swapping it for a vaguer-but-still-
numeric approximation ("dozens," "~100") that will just go stale on a slower
clock.

**This isn't a rule against numbers in general.** A version number
([`file-header`](#file-header)), a date
([`buenos-aires-dates`](#buenos-aires-dates)), or a count that's genuinely
the point of the sentence and maintained alongside the thing it counts (the
group table above, kept current with the rules it lists) all stay exact.
The target is specifically a count of something that can change independent
of the sentence stating it, where the number isn't actually the point —
scene-setting detail that happened to be numeric when it was written.

**Not mechanically enforced** — a count that will drift can't be told from
one that won't without reading intent, so this rides on
[`deep-check`](#deep-check)'s review, the same as [`rule-links`](#rule-links)'s
non-slug citation kinds. Not scoped to Morgan — a documentation-quality
habit, like [`trim-prose`](#trim-prose).

<a id="header-caps"></a>

### 26. Header Capitalization: Pick One Consistent Schema — NY Times Headline Style Is the Pack's Default (`header-caps`)

[AGENTS.md](../../AGENTS.md)'s own Conventions section already states the
general rule for *this* repo: headers and subheaders at the same rank must
all follow one capitalization style, never mixed — found the hard way when
this file's own later sections drifted into a different style, and a
different heading level, from its earlier ones, fixed here and in the
dependent repo where it first surfaced
([`private-repo-scrub`](#private-repo-scrub) — the real name and full
account stay out of anything vendored, kept instead in this repo's own
[TODO.md](../../TODO.md) decision record). That fix says *be consistent*; it
deliberately left *which* style to each repo, and RepoPersonalPreferences'
own first answer — sentence case — was itself just this repo's own choice,
not a pack-wide default a new repo could start from.

This closes that gap for every repo the personal pack is installed into
([`install`](#install)): absent a documented reason to pick something else,
use **NY Times headline-style capitalization** — capitalize principal words
(nouns, verbs, adjectives, adverbs, pronouns), lowercase minor words
(articles, short prepositions, coordinating conjunctions) except at the very
start or end of the header — consistently across every header and subheader
in the document. Same "pick one, don't mix" requirement AGENTS.md's own
Conventions section already states for headers generally; this just gives a
new repo a starting answer instead of a blank page. A repo is free to choose
differently and document that choice inline the same way
RepoPersonalPreferences documents its own choice, in its own
[AGENTS.md](../../AGENTS.md). RepoPersonalPreferences carried its own
sentence-case carve-out here until 2026-08-28, when Morgan dropped it: this
repo now follows the same default it recommends to every dependent repo
rather than exempt itself from it (see [TODO.md](../../TODO.md)'s decision
record).

Not scoped to Morgan the way [`morgan-scope`](#morgan-scope)'s facts are — a
documentation-quality default, not a fact about one person, so it applies
regardless of who is driving the session in a given dependent repo.

<a id="sensitive-characterization-scrub"></a>

### 27. Scrub Sensitive Characterizations of Real People, Unless Told Otherwise (`sensitive-characterization-scrub`)

Assume whoever is driving a session here talks about real people — friends,
colleagues, prospective partners, anyone the work touches — as candidly and
directly as they would with a trusted collaborator, because that candor is
exactly what makes the collaboration useful. That candor is not, on its own,
safe to carry forward verbatim into anything committed. Found the hard way in
a dependent repo's own brainstorm notes: a direct, off-the-cuff description
of a real, named acquaintance — said only for the conversation — made it into
a committed document, which was then shown to that person, reading back more
bluntly than intended (the specific text and the fuller account stay in this
repo's own [TODO.md](../../TODO.md) decision record, never here — per
[`private-repo-scrub`](#private-repo-scrub), below).

**The rule:** before anything actually gets committed — a document, a
brainstorm entry, a code comment, a commit message — assume the specific,
identifiable real people it describes may eventually read it themselves:
shown to them directly, come across in a repo that stops being private, or
read over someone's shoulder. Where a description of a real person is
unusually direct, strong, negative, or otherwise sensitive enough that the
person themselves might wince reading it, don't commit it as given — soften
it, or ask first:

- **Default to a euphemism that keeps the substance, not the edge.** A blunt
  personal trait restated as an indirect institutional or situational one
  usually does the job — "very well-connected" becomes something like "given
  the team's strong network," "difficult to work with" becomes something
  like "a working style this project hasn't fully adapted to." The reader
  still gets the practical point without it reading as a direct judgment of
  the person.
- **Ask, don't guess, when no softened phrasing preserves what the point
  needs** — or when it's genuinely unclear whether a rewrite is soft enough.
- This isn't a ban on describing real people, and it doesn't reach the
  conversation itself — keep talking as openly as usual there. It only gates
  what actually gets written down: ordinary, neutral, complimentary, or
  already-public description needs none of this.

Not mechanically enforced — a script can't judge whether a characterization
is sensitive enough to soften, or already fine as written, so, like
[`push-back`](#push-back), this rides on the session's own judgment at the
moment of writing, and on [`deep-check`](#deep-check)'s later review. Not
scoped to Morgan the way [`morgan-scope`](#morgan-scope)'s facts are — a
documentation/privacy habit, like [`private-repo-scrub`](#private-repo-scrub)
below, so it applies to whoever is driving a session in a repo this pack is
installed into, characterizing whoever they're discussing.

<a id="private-repo-scrub"></a>

### 28. Private Repo Names and Specifics Get Scrubbed Before Anything Vendors or Is Shared (`private-repo-scrub`)

Two privacy boundaries look alike but aren't the same one.
[`blank-blocklist`](#blank-blocklist)'s
[process/scrub_blocklist.txt](../scrub_blocklist.txt) protects Morgan's own
identity from reaching the *public* BestPractice repo. This rule protects
something else: RepoPersonalPreferences also names, links to, and draws
lessons from several of Morgan's *other private* repos — the real incidents
behind [`content-subdirs`](#content-subdirs) and
[`header-caps`](#header-caps), among others — and nothing stopped one of
those repos' actual names, links, or internal details from riding along
inside `process/personal/` or [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md)
into every dependent repo this pack installs into ([`install`](#install)
vendors `process/personal/`'s whole tree byte-for-byte, the same as
BestPractice itself — nothing on that path scrubs anything).
[`content-subdirs`](#content-subdirs) and [`header-caps`](#header-caps) both
did exactly this, naming one such repo and linking to it in text that ships
on every future install — fixed in the same pass this rule was added.

**The rule:** anything that actually ships elsewhere — everything under
`process/personal/` (including
[templates/AGENTS_ADDENDUM.md.template](templates/AGENTS_ADDENDUM.md.template)
and every other template) and [NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) —
may describe the situation that prompted a rule only in general terms ("a
dependent repo," "an earlier project," "a past install"), never by a private
repo's real name, its URL, or specifics about its internal layout that would
identify it. RepoPersonalPreferences' own name is the one standing
exception: it's the pack's source, already named in every dependent repo's
own `process/manifest_personal.json` ([`install`](#install) step 6), so
there is nothing to protect there. This doesn't reach content that never
leaves this repo — [TODO.md](../../TODO.md)'s own decision records, this
repo's own `AGENTS.md` Conventions section, commit messages — which can and
should keep naming the real repo, since that is exactly where the full story
belongs.

**The master record, and its vendor-safe twin.** Keep the complete, specific
account — the real repo name, what happened, why it mattered — in
[TODO.md](../../TODO.md)'s decision record for that item, the same way it
already is for [`content-subdirs`](#content-subdirs) and
[`header-caps`](#header-caps). Alongside it, write out the exact scrubbed
sentence that actually appears in the vendored text, labeled **"Vendor-safe
version:"**. That sentence is then the one to copy, verbatim, anywhere else
the same story needs telling (a §, a template bullet, a later rewrite) — so
a later session reuses an already-approved scrub instead of re-deriving one
from scratch each time, and can't accidentally reintroduce the name while
paraphrasing it fresh. See TODO.md's [`content-subdirs`](#content-subdirs),
[`header-caps`](#header-caps), and
[`private-repo-scrub`](#private-repo-scrub) decision records for the worked
examples this rule was written from.

**Enforcement.** [tools/light_check.py](tools/light_check.py) now scans
everything under `process/personal/` plus
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) against
[private_repo_blocklist.txt](private_repo_blocklist.txt) — a list of
Morgan's other private repo names, the same "one regex per line, err broad"
shape as [scrub_blocklist.txt](../scrub_blocklist.txt) — and fails the
commit if a match turns up in that scope. Add a line to that blocklist the
moment a new private repo gets named in this tree for illustration and needs
scrubbing instead, the same "the moment it shows up" discipline
`scrub_blocklist.txt`'s own header already asks for.

Not scoped to Morgan the way [`morgan-scope`](#morgan-scope)'s facts are — a
documentation/privacy habit, not a fact about one person, so it applies
regardless of who is drafting content in this repo.

<a id="llm-neutral"></a>

### 29. LLM Integrations Stay Platform-Neutral; OpenRouter Is the Default Assumption (`llm-neutral`)

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

<a id="fail-gracefully"></a>

### 30. Always Fail Gracefully (`fail-gracefully`)

Any code this pack helps write or set up anticipates its own common failure
modes rather than letting them surface as an unhandled crash. Concretely:
before shipping code that depends on something outside its own control — a
required config variable or environment variable, a file that's supposed to
exist, a network call, a third-party credential — write it to check for the
absence or failure case on purpose and degrade in a way the caller can act
on: a clear error message naming exactly what's missing and how to fix it, a
documented fallback/default, or a clean non-zero exit — never a raw stack
trace, a silent wrong answer, or a hang. This is a coding-quality rule for
what this pack builds, not a repository-process rule like most of the rest
of this file; it belongs here rather than upstream because it is general
enough for every repo Morgan starts, and simple enough that raising it to a
persuasive, attributed BestPractice submission per
[process/upstream/INSTALL.md](../upstream/INSTALL.md) §4 isn't worth the
effort yet — check-in remains the outlet if that changes (see
[TODO.md](../../TODO.md)'s recurring check-in item).

<a id="default-branch"></a>

### 31. A New Repo's Default Branch Is `main`, Set Once at Install (`default-branch`)

Two different situations both land here, and they're handled differently —
telling them apart is the first step:

**An existing repo whose default branch isn't `main`.** GitHub only defaults
a freshly-created repository to `main` on its own; plenty of repos predate
that default or arrived some other way (an import, a mirror, an org-level
policy) and still sit on `master` or something else — this repo itself did,
until it was fixed by hand (2026-08-21). At install time
([`install`](#install) below), check the target repo's current default
branch; if it isn't already `main`, set it once — via the GitHub API's
repo-update endpoint (`PATCH /repos/{owner}/{repo}` with `default_branch:
"main"`) where the session's tools reach that far, otherwise as a one-click
item (**Settings → General → Default branch**, the pencil icon next to the
current default) disclosed in the new repo's `GETTING_STARTED.md`
administrator section like any other click-path (BestPractice practice 37,
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8). One-time per repo —
once set, every subsequent clone, PR, and Actions run already targets `main`
on its own, nothing to repeat.

**A brand-new, blank repo with no branches yet — the more common case for
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md).** There is no "current default
branch" to check here — GitHub doesn't assign one at all until something is
actually pushed to it, so the check-then-set flow above has nothing to check
and nothing to set (an install session once treated this as the first case
anyway, discovered the repo had no `main` at all partway through, and
created one via the GitHub API from a planning branch's tip after the fact —
needless, and avoidable). Instead: **make this repo's very first commit
directly on a branch literally named `main`, and push that first** — not a
feature or planning branch. GitHub adopts the first branch ever pushed to an
empty repository as its default automatically, so this alone satisfies the
rule; there is nothing left to check or set afterward, and nothing to ask
Morgan about first. Only once that first commit is on `main` does the usual
feature-branch-plus-PR workflow (`AGENTS.md`'s "Git / workflow" section)
start applying to every commit after it.

<a id="blank-blocklist"></a>

### 32. Scrub Blocklist Stays Blank at Install — Never Ask, Never Remind (`blank-blocklist`)

BestPractice's own install procedure
([process/upstream/INSTALL.md](../upstream/INSTALL.md) §1 step 4) asks the
target repo's user for private vocabulary to seed
`process/scrub_blocklist.txt` before any check-in from that repo to the
public BestPractice repo — the mechanism `practice_audit.py` enforces
against so nothing proprietary leaks into `process/upstream/`. This pack
overrides that default, per [`bestpractice-wins`](#bestpractice-wins):
Morgan doesn't use the check-in-to-public- BestPractice path in the repos
this pack installs into, so a session installing BestPractice there never
asks him for blocklist content and never volunteers a draft seeded from repo
context on his behalf, the way an earlier session once did unprompted. Write
`process/scrub_blocklist.txt` with just its explanatory header comment and
no entries, and move on — no follow-up reminder, ever, in that install
session or a later one. If Morgan ever wants the feature, he'll say so
himself; a session can seed or extend the blocklist at that point, per
BestPractice's own procedure, same as always.

This is a rule about the *install-time default for a new, dependent repo* —
it doesn't reach back to reopen or blank out a blocklist a repo already has
populated and is actively relying on. RepoPersonalPreferences' own
[process/scrub_blocklist.txt](../scrub_blocklist.txt) is exactly that case:
this repo genuinely does check practices into the public BestPractice repo
from time to time (`AGENTS.md`'s practice-export policy), so its blocklist
keeps doing real work protecting Morgan's actual identity from ever reaching
that public repo, and stays as populated and reviewed as it already is.
Don't touch it under this rule.

<a id="content-subdirs"></a>

### 33. Content-Oriented Repos: Group Deliverable Content in a Subdirectory — a Recommendation, Not a Rule (`content-subdirs`)

Every other rule in this pack is something a session does or checks,
[`push-back`](#push-back) excepted by its own disclaimer. This one is the
same kind of exception: advisory only, resting on judgment
([`small-calls`](#small-calls)) rather than an audit — stated here so a
session doesn't start treating root-level content clutter as an install-time
defect the way a missing manifest entry actually is.

**The pattern.** A repo whose deliverable is the writing itself — a
brainstorm, a manuscript, an argument, a decision record — accumulates two
different kinds of root-level files: the navigation layer
([MAP.md](../../MAP.md), [GLOSSARY.md](../../GLOSSARY.md),
[TODO.md](../../TODO.md), a README, an `AGENTS.md`,
[GETTING_STARTED.md](../../GETTING_STARTED.md), and this pack's own
`VOICE.md`/`STYLEGUIDE.md` where installed — see
[`mirror-into-agents`](#mirror-into-agents) for the same generic/this-repo
distinction) that exists to help a reader find and use the repo, and the
deliverable content itself. Left alone, both pile up at root together, and
enough of the second kind reads as cluttered even when the first is doing
exactly what it should. A repo doing this well groups the manuscript and its
supporting notes each into their own named subdirectory — say `book/` and
`brainstorm/` — while the navigation layer stays at root
([`private-repo-scrub`](#private-repo-scrub) — the repo this was first
noticed in isn't named here on purpose; the full account, with its real
name, lives in this repo's own [TODO.md](../../TODO.md) decision record
instead).

**The recommendation.** In a **content-oriented repo** — one whose
deliverable is the writing itself, not software that runs — once root
accumulates three or more documents that are deliverable content rather than
navigation, consider grouping that content under one or more named
subdirectories, the same pattern described above. A **code-oriented repo**
doesn't get this recommendation at all — its root-level clutter, if any, is
a different problem with its own existing conventions (`src/`, `lib/`,
whatever the language's own idiom is), and this pack has nothing to add
there.

**Where this doesn't reach.** This pack's own two homes are process repos,
not content repos, by the same test: RepoPersonalPreferences' deliverable is
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) and BestPractice's is the
practice layer itself — in both, the content and the navigation layer are
the same thing, so there's no split to group, and this recommendation
doesn't reach either, the same way [`drift-notice`](#drift-notice)'s
drift-check doesn't reach back into RepoPersonalPreferences on itself.

**Not mechanically enforced, and not retroactive.** Unlike almost everything
else in this pack, nothing checks for this — no
[light_check.py](tools/light_check.py) rule, no audit. Raise it as a
judgment call under [`small-calls`](#small-calls) when a session actually
notices root cluttered with deliverable content — at the capture gate
([AGENTS.md](../../AGENTS.md) merge runbook step 0), or when a new
content-oriented repo is first taking shape at install
([`install`](#install)) — never as a reason to force a restructure on its
own. It is never retroactive by itself, either: an existing repo already
past the threshold doesn't get rewritten just because this rule now exists —
a restructure means updating every relative link into the moved files
(practice 11), real work with real link-churn, worth doing only once someone
actually decides to do it.

<a id="install"></a>

### 34. Installing This Pack into a Repo (`install`)

Do this **after** BestPractice itself is installed
([process/upstream/INSTALL.md](../upstream/INSTALL.md) §1) — see
[NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) for the combined, one-pass
version of both steps.

1. Vendor this directory's tree (not `.git`) to `process/personal/` in the
   target repo, the same way BestPractice itself gets vendored.
2. Weave
   [templates/AGENTS_ADDENDUM.md.template](templates/AGENTS_ADDENDUM.md.template)
   into the target repo's `AGENTS.md`, right after the "Conventions"
   section, insert its "0c. TODO gate" step into the merge runbook, and
   append the [`quiet-checks`](#quiet-checks) sentence to the end of the
   runbook's step 3.
3. Install the three workflow templates:
   [templates/github-actions/upstream-sync.yml.template](templates/github-actions/upstream-sync.yml.template)
   → `.github/workflows/bestpractice-upstream-sync.yml`,
   [templates/github-actions/light-check.yml.template](templates/github-actions/light-check.yml.template)
   → `.github/workflows/light-check.yml`, and
   [templates/github-actions/personal-pack-sync.yml.template](templates/github-actions/personal-pack-sync.yml.template)
   → `.github/workflows/personal-pack-sync.yml` ([`pack-sync`](#pack-sync)
   below — needs its own secret, disclosed in step 9).
4. Extend `tools/bootstrap.sh` (already installed by BestPractice,
   [INSTALL.md](../upstream/INSTALL.md) §1) with two snippets, run once per
   clone, in this order: the `git config user.name` / `user.email` lines
   from [`commit-author`](#commit-author) above, then
   [templates/bootstrap-freshness.sh.template](templates/bootstrap-freshness.sh.template)'s
   line — the session-start freshness notice for this pack
   ([`drift-notice`](#drift-notice)), skipped only when installing on
   RepoPersonalPreferences itself ([`drift-notice`](#drift-notice)'s
   exemption).
5. Add [process/personal/tools/light_check.py](tools/light_check.py) and
   [process/personal/tools/pack_sync.py](tools/pack_sync.py) to the
   harness's pre-approved command allowlist (for Claude Code:
   `.claude/settings.json`), the same way
   [doc_lint.py](../upstream/tools/doc_lint.py) and
   [practice_audit.py](../upstream/tools/practice_audit.py) already are.
6. Add an entry to `process/manifest_personal.json` for every file installed
   in steps 1-3 (schema: identical to BestPractice's own [manifest
   schema](../upstream/INSTALL.md) §5, with `upstream.vendored_at` pointing
   at `process/personal` in *this* repo). The manifest's top-level
   `upstream.repo` / `upstream.commit` fields are a separate thing from
   these entries — they record where the `process/personal/` tree *itself*
   came from, not any one installed file — and get set differently depending
   on which repo is doing the installing: **inside RepoPersonalPreferences
   itself** (installing the pack on itself, as this repo's own
   `process/manifest_personal.json` does), the tree already *is* upstream,
   so both stay `null`, per the pack anatomy rule
   ([process/upstream/INSTALL.md](../upstream/INSTALL.md) §7). **Installing
   into any other, dependent repo**, set `upstream.repo:
   "https://github.com/themorgan/RepoPersonalPreferences"` and
   `upstream.commit` to this repo's real HEAD commit at install time — that
   repo genuinely depends on a specific commit of this one, and
   [`pack-sync`](#pack-sync)'s sync workflow needs something real to compare
   against. `scrub_blocklist` stays `null` either way (see this repo's own
   [process/manifest_personal.json](../manifest_personal.json) for a worked
   example of the null-both-ways, self-hosting case).
7. Run `python3 process/upstream/tools/practice_audit.py --update-baseline`
   ([practice_audit.py](../upstream/tools/practice_audit.py)) — it audits
   every `process/manifest*.json` it finds, this pack's included, in one
   pass.
8. Check the target repo's default branch
   ([`default-branch`](#default-branch) above); if it isn't already `main`,
   set it once now via the API where the session's tools reach that far,
   otherwise add it to the click-path disclosure in the new repo's
   `GETTING_STARTED.md` administrator section
   ([NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8).
9. Disclose the `PERSONAL_PACK_TOKEN` secret step 3's pack-sync workflow
   needs — what it is and its exact click-path are stated in full in
   [`pack-sync`](#pack-sync) below, and again in the target repo's own
   `GETTING_STARTED.md` for the administrator who has to click it; this step
   is the reminder to *do* that disclosure, in the same channel as step 8:
   no session's tools can mint or set that token, so the install reply says
   once that it's Morgan's to add
   ([NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8).

This procedure applies exactly the same way when the target repo already has
some of these pieces present because they arrived via an already-dependent
repo — a fork, a copy, or a chain-vendor — rather than fresh from the
canonical source named in steps 1-4 above. Do steps 1-9 for whichever pieces
are actually missing; don't skip any of them just because *something* under
`process/upstream/` or `process/personal/` is already there — presence of
the tree is not evidence the sync workflows or the `AGENTS.md` sections came
with it. [`drift-notice`](#drift-notice)'s end-of-session check is what
catches this after the fact if it's missed at install time, but an install
session that notices the gap up front should just close it, the same way it
would for a from-scratch install.

<a id="bestpractice-sync"></a>

### 35. A Sync Keeps BestPractice Current, Unattended (`bestpractice-sync`)

*([`pack-sync`](#pack-sync) is this rule's sibling — the same shape, pointed
at the personal pack instead of BestPractice. Change one and check the
other. [`drift-notice`](#drift-notice) layers an end-of-session drift check
on top of this one and [`pack-sync`](#pack-sync) both — same comparison, but
it only asks, never merges unattended.)*

[templates/github-actions/upstream-sync.yml.template](templates/github-actions/upstream-sync.yml.template)
→ `.github/workflows/bestpractice-upstream-sync.yml`. Runs on a schedule —
**weekly by default** (Mondays at 09:00 Buenos Aires); the workflow file's
`on.schedule` block carries a commented-out daily cron line right next to
the active weekly one, so switching cadence (or moving either to a different
time of day) is a one-line comment/uncomment in the workflow file, not a
rewrite. A cheap `check` job compares `process/manifest.json`'s recorded
upstream commit against BestPractice's actual HEAD via `git ls-remote` — no
model call, no cost, on a quiet run. If upstream moved, an `update` job runs
[Claude Code as a GitHub
Action](https://github.com/anthropics/claude-code-action) to take the update
per BestPractice's own [INSTALL.md](../upstream/INSTALL.md) §2:
three-way-merge each manifest entry through its recorded adaptation, re-run
every gate ([doc_lint.py](../upstream/tools/doc_lint.py),
[light_check.py](tools/light_check.py),
[practice_audit.py](../upstream/tools/practice_audit.py)), **resolve any
open `bestpractice` entry in [TODO.md](../../TODO.md)'s "## Pending Drift
Reviews" section in the same commit** (`pack_sync.py resolve bestpractice` —
[`drift-notice`](#drift-notice) below; a no-op when there's none), commit
with every judgment call it made spelled out under a "Judgment calls to
review:" heading in the commit message, open a PR, and — once this repo's
own checks pass on that PR — merge it to the default branch. That resolve
step is what keeps this scheduled sync and [`drift-notice`](#drift-notice)'s
own persisted notice honest with each other — without it, an unattended run
landing *after* a session already recorded a pending-review entry would fix
the drift but leave that entry claiming, forever, that it's still
unreviewed.

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

**If neither credential is set when upstream has moved,** the `update` job
is skipped rather than attempted and failing on an auth error — a
`note-missing-credential` job leaves a `::warning::` in that run's summary
and opens (or updates) a GitHub issue
([`automation-issues`](#automation-issues)), so a quiet-looking sync can
still be told apart from a real "nothing to sync" run without anyone having
to go digging through Actions history. `CLAUDE_CODE_OAUTH_TOKEN` and
`ANTHROPIC_API_KEY` are only ever spent by this `update` job's Claude Code
call (and its personal-pack-sync sibling's, [`pack-sync`](#pack-sync)) — no
other automation in this repo uses either. A chat session asked to run the
sync manually doesn't need either secret at all, since it's already Claude;
it should just take the update itself following
[INSTALL.md](../upstream/INSTALL.md) §2 above, and remind the user to set
one of the two so future unattended runs don't need to be asked for by hand.

<a id="pack-sync"></a>

### 36. A Sync Keeps the Personal Pack Itself Current (`pack-sync`)

The pack's own analogue of [`bestpractice-sync`](#bestpractice-sync)'s
BestPractice sync — same shape, a separate workflow and a separate concern.
[`bestpractice-sync`](#bestpractice-sync) keeps a dependent repo's
`process/upstream/` current with the public BestPractice repo; this keeps
that same repo's `process/personal/` current with *this* repo,
RepoPersonalPreferences, once Morgan is adding rules to the pack often
enough that copy-once-at-install stops being enough (the reason this section
exists at all — see [TODO.md](../../TODO.md) for the decision record).

[templates/github-actions/personal-pack-sync.yml.template](templates/github-actions/personal-pack-sync.yml.template)
→ `.github/workflows/personal-pack-sync.yml`. Runs on the same
weekly-by-default, daily-optional schedule as
(Tuesdays at 04:15 Buenos Aires — deliberately outside Morgan's working
hours, so an unattended self-merging run is skimmed as a finished thing
the next morning rather than landing mid-workday; no longer tied to
[`bestpractice-sync`](#bestpractice-sync)'s own Monday 09:00 slot, which
stays where it is at BestPractice's owner Alex's preference so the two never race over the same working tree; the commented-out
daily alternative sits fifteen minutes after
[`bestpractice-sync`](#bestpractice-sync)'s own daily alternative for the
same reason — switching either workflow's cadence independently still keeps
them apart). A cheap `check` job compares `process/manifest_personal.json`'s
recorded `upstream.commit` against this repo's actual HEAD via an
authenticated `git ls-remote` — no model call, no cost, on a quiet run. If
the pack moved, an `update` job runs [Claude Code as a GitHub
Action](https://github.com/anthropics/claude-code-action) to take the
update: mirror `process/personal/` from a fresh clone via
[tools/pack_sync.py](tools/pack_sync.py) ([`install`](#install) above —
genuinely simpler than BestPractice's own check-in machinery, since the pack
is a one-way dependency with no landing-PR phase to wait through), re-weave
any changed template sections into the target repo's own `AGENTS.md` and
other installed, adapted copies, re-run every gate, **resolve any open
`personal-pack` entry in [TODO.md](../../TODO.md)'s "## Pending Drift
Reviews" section in the same commit** (`pack_sync.py resolve personal-pack`
— [`drift-notice`](#drift-notice) below; a no-op when there's none, same
reasoning as [`bestpractice-sync`](#bestpractice-sync)'s own resolve step),
commit with every judgment call spelled out under a "Judgment calls to
review:" heading, open a PR, and — once the target repo's own checks pass on
that PR — merge it to the default branch.

**The one real difference from [`bestpractice-sync`](#bestpractice-sync):**
RepoPersonalPreferences is *private*, where the public BestPractice repo
isn't, so both jobs need their own repository secret to reach it —
`PERSONAL_PACK_TOKEN`, a GitHub personal access token (fine-grained,
read-only, scoped to just `themorgan/RepoPersonalPreferences`), in addition
to the Claude credential [`bestpractice-sync`](#bestpractice-sync) already
needs (`CLAUDE_CODE_OAUTH_TOKEN` or `ANTHROPIC_API_KEY` — either one), plus
the same "Allow auto-merge" and Actions-can-open-PRs toggles. **No workflow,
and no session, can mint or install this token on Morgan's behalf** — an
administrator (Morgan) has to generate it himself at
[github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)
and add it at the target repo's own **Settings → Secrets and variables →
Actions → New repository secret**. `check` still skips the update rather
than failing the workflow when the token is missing (a private-repo
credential shouldn't block an otherwise-successful install), but every such
run now also emits a `::warning::` GitHub Actions annotation and opens (or
updates) a GitHub issue ([`automation-issues`](#automation-issues)) — a
per-run smoke test, visible in both the Actions UI and the repo's own issues
list on every firing, not just a one-time install reminder — so a token that
was never set, or later revoked, gets noticed the same day rather than by
chance. An install session mentions it once in its reply, alongside the
other click-paths ([NEW_REPO_SETUP.md](../../NEW_REPO_SETUP.md) step 8,
[`install`](#install) step 9); the per-run warning and issue carry it from
there, so there's no need to keep raising it in later sessions.

If a run ever can't confidently resolve something, same as
[`bestpractice-sync`](#bestpractice-sync): it leaves the PR open, unmerged,
with a comment explaining exactly what it couldn't do — it never forces a
merge past a failing check.

<a id="drift-notice"></a>

### 37. A Session-Start Notice Asks About Drift Immediately, Not at the End (`drift-notice`)

The scheduled syncs ([`bestpractice-sync`](#bestpractice-sync),
[`pack-sync`](#pack-sync)) close the gap *between* sessions — they run
whether or not anyone opens the repo. This rule closes a narrower gap, and
closes it as early as possible: the one scheduled run hasn't caught up yet
because it hasn't fired since the drift happened, even though a session —
and the person who can approve an update — is right here, from the very
first turn. It's additive, not a replacement: dropping either scheduled sync
in favor of this would leave updates unnoticed for however long the repo
sits idle between sessions, which is exactly the gap
[`bestpractice-sync`](#bestpractice-sync) and [`pack-sync`](#pack-sync)
exist to bound.

Detection is automated and immediate — a session doesn't have to remember to
run anything:

- **BestPractice half — already wired.** `tools/bootstrap.sh` runs
  `checkin.py fresh` on every session start (practice 13): one clone-free
  `git ls-remote` against the public BestPractice repo, printed as a single
  notice line only when [process/manifest.json](../manifest.json)'s recorded
  `upstream.commit` is stale — silent when current or unreachable, never a
  gate, no model call.
- **Personal-pack half — newly wired ([`install`](#install) step 4).**
  `tools/bootstrap.sh` now also runs `python3
  process/personal/tools/pack_sync.py fresh`
  ([tools/pack_sync.py](tools/pack_sync.py)) on every session start, from
  [templates/bootstrap-freshness.sh.template](templates/bootstrap-freshness.sh.template)
  — the same shape, comparing
  [manifest_personal.json](../manifest_personal.json)'s recorded
  `upstream.commit` against RepoPersonalPreferences's actual HEAD. Only in a
  repo where this pack is vendored in as a dependency (i.e. every repo
  *except* RepoPersonalPreferences itself — see the exemption below).

Because both run as part of the same session-start hook that already sets up
the environment, their output is right there in the opening turn — a session
raises whichever one fired as part of catching the member up, not something
saved for the end.

**A fired notice is also persisted, not just printed (added 2026-08-27,
after an incident the same day — see [TODO.md](../../TODO.md)).** A purely
stdout-only notice competes for a session's attention against whatever
concrete task the human actually opened the session to do, and can lose that
fight silently: it was read (it's in the transcript), but never acted on,
and nothing forces it back into view once the turn moves on — exactly what
happened in a dependent repo, where a BestPractice-drift notice fired, was
never raised, and only surfaced when the user asked directly a full task
later ([`private-repo-scrub`](#private-repo-scrub) — the real name is in the
TODO.md entry cited above, not here). `tools/bootstrap.sh`'s freshness lines
(both halves above, from
[templates/bootstrap-freshness.sh.template](templates/bootstrap-freshness.sh.template))
now capture whatever `checkin.py fresh` / `pack_sync.py fresh` print and,
when either fired, both still print it (nothing about the immediate, in-turn
notice changes) **and** call `python3 process/personal/tools/pack_sync.py
record <source> "<notice>"` ([tools/pack_sync.py](tools/pack_sync.py)) to
write it into the target repo's own [TODO.md](../../TODO.md), under a `##
Pending Drift Reviews` heading the tool creates on first use — idempotently:
re-firing the same source's notice updates that source's one open entry in
place (a newer commit hash, say) rather than piling up duplicates. That
entry is not a new kind of gate — [`drift-notice`](#drift-notice)'s own rule
that taking an update stays deliberate is unchanged — but it is now
something [tools/light_check.py](tools/light_check.py) checks for repo-wide
on *every* commit path (a WARN, same non-fatal treatment as its other soft
checks) for as long as it stays open, the same mechanical "can't be silently
skipped" treatment [`light-check`](#light-check)'s vendoring check already
gives a different failure mode. Resolve an entry with `python3
process/personal/tools/pack_sync.py resolve <source> [note]` once its drift
has actually been reviewed — the update taken, or deliberately deferred with
a reason — which checks it off in place rather than deleting it, so the
record survives in [TODO.md](../../TODO.md)'s history the same way any other
completed item there does. The scheduled syncs
([`bestpractice-sync`](#bestpractice-sync), [`pack-sync`](#pack-sync)) call
`resolve` themselves, in the same commit that lands their update, so an
entry a session recorded doesn't sit stale after an unattended run fixes the
same drift first.

**Taking either update stays deliberate, whenever it's raised.** Never take
it without being asked, whether that's the first exchange of the session or
later — this is the one deliberate difference from
[`bestpractice-sync`](#bestpractice-sync) and [`pack-sync`](#pack-sync),
which merge unattended. A human is already present to answer, so there's no
reason to skip the ask the way the scheduled runs have to. If asked to
proceed, take the update the same way a manually-requested sync already does
([`bestpractice-sync`](#bestpractice-sync)'s own closing paragraph, and
[`pack-sync`](#pack-sync)'s sibling): BestPractice per
[INSTALL.md](../upstream/INSTALL.md) §2, the personal pack per
[pack_sync.py](tools/pack_sync.py) — every gate re-run, opened as a PR,
merged only once the user approves it (not auto-merged the way the scheduled
`update` jobs are, since a human is already in the loop to say yes).

**A successful merge in the same session re-asks too, not just the
end-of-session fallback below.** If a session-start notice fired and its
entry in TODO.md's `## Pending Drift Reviews` section is still open once a
merge (the runbook above) lands successfully — the update was neither taken
nor formally resolved with `pack_sync.py resolve` — say so again right after
that merge, naming the same entry, and ask directly whether to take it now,
the same way it was asked (or should have been asked) at session start. A
landed merge is a natural checkpoint before a session's attention moves on to
something else: earlier than the vaguer end-of-session fallback below, and a
direct question rather than a warning line in an audit's output a session
can read past. It doesn't replace either — the fallback below still catches
a session that never merges anything, and [`light-check`](#light-check)'s
per-commit warning still catches a session that skips this too. Skip the
re-ask only when the entry already closed during the session — taken, or
`resolve`d with a deferral reason — since that already answers the question
this re-ask exists to ask.

**RepoPersonalPreferences is exempt from the personal-pack half of this —
both the session-start notice and its end-of-session fallback below — on
itself,** the same reason [`pack-sync`](#pack-sync)'s workflow isn't
installed here at all: the vendored tree here *is* upstream for the pack
(the pack anatomy rule, [INSTALL.md](../upstream/INSTALL.md) §7), so
comparing it against itself is circular, not a real drift check. Neither
`templates/bootstrap-freshness.sh.template`'s line nor `pack_sync.py fresh`
runs against this repo's own `tools/bootstrap.sh`. The BestPractice half
still applies here, unexempted — this repo genuinely vendors
`process/upstream/` from the public BestPractice repo, same as any dependent
repo does.

**Fallback, for whenever a session-start notice didn't fire or drift
happened mid-session** (an indirect install with no working bootstrap wiring
yet, a long-running session, offline at start but reachable later): at the
end of every chat session, right after the merge runbook's own steps (after
landing the branch's own work, not instead of it), repeat the same cheap
comparisons — no model call needed, just `git ls-remote` against each source
and a look at the recorded manifest commit, the same comparisons the
session-start notices already make (always the BestPractice comparison; the
personal-pack comparison too, except in RepoPersonalPreferences itself, per
the exemption above). If either has moved and hasn't already been raised and
answered earlier in the session, say so plainly — which repo, the recorded
commit, the actual HEAD — and ask whether to take the update now before
ending the session.

**This also has to survive an indirect install.** The comparisons above
assume a fully-installed repo — files present, manifest current, bootstrap
wiring in place. That's not guaranteed when either tree arrived by some path
other than a session actually running [INSTALL.md](../upstream/INSTALL.md)
§1 or [`install`](#install): a fork, a template-repo "use this template," a
plain file copy, or — the case that prompted this paragraph — a repo that
vendored from an *already-dependent* repo instead of from the canonical
source. Any of those can carry `process/upstream/` and/or
`process/personal/` without carrying the mechanisms that keep them current.
So the same check also verifies, cheaply, whenever either tree is present:
does `.github/workflows/bestpractice-upstream-sync.yml` exist (when
`process/upstream/` is present), does
`.github/workflows/personal-pack-sync.yml` exist (when `process/personal/`
is present and this isn't RepoPersonalPreferences itself, per the exemption
above), does `tools/bootstrap.sh` actually carry both freshness snippets,
and does `AGENTS.md` actually carry the woven-in sections (the
`agents-addendum` entry's `section_marker`, per
[manifest_personal.json](../manifest_personal.json))? If any of those is
missing, that's an incomplete install, not drift — say so plainly (which
piece is missing) and offer to finish it, in-session: run whichever of
[`install`](#install)'s steps (or [INSTALL.md](../upstream/INSTALL.md) §1's)
produces the missing piece, sourced from the canonical repo — the public
BestPractice repo, or RepoPersonalPreferences for the pack — regardless of
which repo the files already on disk actually arrived from. The one-way,
single-source design ([`pack-sync`](#pack-sync)) holds even when the copy
that got here took an extra hop: a chain-vendored repo gets the same
standing mechanisms as one installed straight from canonical, not a frozen
snapshot of whatever its immediate parent happened to have.

**The Claude credential gets the same clean-skip treatment here as in
[`bestpractice-sync`](#bestpractice-sync):** `check` also verifies one is
set, and if the pack moved but both `CLAUDE_CODE_OAUTH_TOKEN` and
`ANTHROPIC_API_KEY` are blank, `update` is skipped with a
`note-missing-credential` warning in the run's summary (and a GitHub issue,
[`automation-issues`](#automation-issues)) rather than an auth failure — the
*sync itself* still skips silently on a missing `PERSONAL_PACK_TOKEN` per
the paragraph above, exactly as before, but
[`automation-issues`](#automation-issues) now means that skip isn't silent
about being reported, either. Same fallback applies: a chat session asked to
run this sync manually can just take the update itself, in-session, and
should remind the user to set one of the two Claude credentials afterward.

This section, unlike the rest of this pack, does not itself get vendored
"live" into RepoPersonalPreferences — this repo is the pack's source, so
running a workflow here to check whether the pack has moved from here would
be circular. Only the *template* lives here, at
[templates/github-actions/personal-pack-sync.yml.template](templates/github-actions/personal-pack-sync.yml.template),
for dependent repos to instantiate.

<a id="fresh-check-escalation"></a>

### 38. When the Freshness Check Can't Reach the Source, Say So — Then Verify Directly (`fresh-check-escalation`)

[`drift-notice`](#drift-notice)'s personal-pack half runs one `git ls-remote`
against RepoPersonalPreferences (private) at every session start, and was
built deliberately silent on any failure — offline, a timeout, a transient
blip — treating it the same as "nothing has moved," because a notice that
turns out to mean only "the network hiccuped" would be worse than no notice
at all. That silence assumption breaks down for one case it wasn't built to
handle: an environment with no git credentials for a private repo at all,
ever — not a blip, a standing gap. There, `git ls-remote` fails the exact
same way every single session, so the existing design reads it as
"confirmed current" indefinitely, masking real drift for as long as that
environment exists (found directly: a dependent repo's session, 2026-08-29,
where `git ls-remote` against RepoPersonalPreferences came back `fatal:
could not read Username for 'https://github.com': terminal prompts
disabled` — a fast, clean failure, not a hang).

**The mechanical half.** [tools/pack_sync.py](tools/pack_sync.py)'s `fresh()`
now tells the two failure modes apart. `git ls-remote` returning nothing
because it genuinely found nothing — an unreachable host, a dead network, a
slow timeout — still prints nothing, unchanged: offline stays quiet, exactly
as [`drift-notice`](#drift-notice) already documents. But a `git ls-remote`
that comes back with a real, fast error (a non-zero exit) now prints one
line — `COULD NOT VERIFY: ...`, naming the repo and the error, pointing back
here — instead of vanishing into the same silent branch. That line rides
every mechanism [`drift-notice`](#drift-notice) already built for its own
`NOTICE:` line: raised at session start, captured and recorded into
[TODO.md](../../TODO.md)'s `## Pending Drift Reviews` under the same
`personal-pack` source slug, warned on by [`light-check`](#light-check)
while the entry stays open, resolved the same way
(`pack_sync.py resolve personal-pack [note]`). The scheduled sync
([`pack-sync`](#pack-sync)) is unaffected — its own `check` job runs an
authenticated `git ls-remote` directly and never calls `fresh()`.

**The judgment half, for whichever session sees that line.** "Could not
verify" is not "confirmed fresh" — don't read the absence of a `NOTICE:`
line as an answer once a `COULD NOT VERIFY:` line has said the check itself
didn't run. If the environment offers any way to reach the source directly —
attaching a GitHub repo to the session read-only, an available `gh`/API
credential, anything short of pushing to it — use it: clone or attach
RepoPersonalPreferences, then compare with `python3
process/personal/tools/pack_sync.py status <clone>` against the manifest's
recorded `upstream.commit`, instead of trusting silence. That is exactly how
the gap this rule exists for got closed the one time it was hit
(a dependent repo, 2026-08-29 — the same sync that added
[`generated-file-marker`](#generated-file-marker),
[`file-mention-links`](#file-mention-links), and
[`sensitive-characterization-scrub`](#sensitive-characterization-scrub) to
that repo). If no such mechanism exists in that environment either, say so
plainly instead of reporting the sync as current: "personal-pack freshness
could not be verified in this environment" is honest, where silence that
reads as "nothing to do" is not.

**Doesn't apply to RepoPersonalPreferences on itself** — the same exemption
[`drift-notice`](#drift-notice) already carries: this repo's own
`process/personal/` *is* the pack's source, so there is no separate source
repo for it to ever fail to reach.

<a id="automation-issues"></a>

### 39. Unattended Automation Reports Its Own Blockers as a GitHub Issue (`automation-issues`)

Any unattended job in this repo — today that means the two scheduled syncs
([`bestpractice-sync`](#bestpractice-sync), [`pack-sync`](#pack-sync)), and
any future one this pack or a project built with it adds — that hits
something blocking it from finishing its normal work (a missing or revoked
secret, an unexpected failure, anything that leaves it unable to complete)
reports that blocker by opening (or updating) a GitHub issue, not only a
`::warning::` Actions annotation or a job-summary line. Keep the annotation
too — it's free and some readers will still see it — but treat it as a
backup, not the primary channel.

**Why an issue, specifically.** An Actions annotation lives inside one
workflow run; nobody sees it unless they already know to go check that run.
A GitHub issue persists in the repo itself, appears in the normal issues
list, and rides GitHub's own notification system (email, mobile push,
whatever the account has configured) for free — no notification
infrastructure to build, no new secret to manage, nothing beyond the
`issues: write` permission on the job that needs it.

**Mechanism:**
[tools/report_automation_issue.py](tools/report_automation_issue.py) —
`python3 process/personal/tools/report_automation_issue.py <label> "<title>"
"<body>"`. Idempotent by design: one open issue per `<label>`, not one per
run — a second call with the same label comments on the existing open issue
(with a "Recurred: `<date>`" stamp) instead of opening a duplicate, so a
blocker that fires every week for months reads as one ongoing problem with a
comment thread, not fifty separate issues burying the repo's issue list.
Needs `issues: write` on the calling job (a one-line addition to its
`permissions:` block — no repository-settings toggle, unlike `pull-requests:
write`) and a `GH_TOKEN` (or `GITHUB_TOKEN`) environment variable set on the
step, typically `${{ github.token }}`. Fails gracefully
([`fail-gracefully`](#fail-gracefully)) if `gh` isn't authenticated or the
API call fails for any reason — prints a WARN, exits 0, never turns a
failure to *report* a blocker into a second, more confusing blocker.

**Applied today** in both [`bestpractice-sync`](#bestpractice-sync)'s and
[`pack-sync`](#pack-sync)'s `note-missing-credential` jobs (missing Claude
credential), and in [`pack-sync`](#pack-sync)'s `check` job (missing
`PERSONAL_PACK_TOKEN`) — the last of these is a deliberate widening of that
credential's previous "stays a silent skip" treatment
([`pack-sync`](#pack-sync)'s own security note): the *sync itself* still
skips silently when the token is missing, exactly as before, but the fact
that it's skipping is no longer silent. A repo secret that's normally set
once at install and never touched again is a low-noise case for this
mechanism — the idempotent comment-not-duplicate design means a missing
token produces one issue that quietly accumulates weekly "still missing"
comments, not fifty.
