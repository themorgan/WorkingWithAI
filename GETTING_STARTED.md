<!-- Last updated: 2026-09-04 10:49:37 (Buenos Aires) by Morgan F, to version 12 -->

# Getting started with `WorkingWithAI`

Welcome. This project runs on a simple idea: **the project's memory lives
in its repository, and you work with that memory by talking to an AI
assistant.** Ask what the team has decided and why — the assistant
answers from the project's own records. Describe a change you want — the
assistant makes it everywhere it applies, and the team reviews it before
it becomes shared. Decisions don't get lost in chat history, nobody
overwrites anyone's work, and a person who joins today can be useful
within the hour. You do not need to be a programmer.

This particular project is a running brainstorm: [RANDOM_NOTES.md](content/RANDOM_NOTES.md) is
where prompts, workflows, and observations about working with AI get
captured as they come up. Want the thinking behind it before the
how-to? [OUR_PHILOSOPHY.md](content/OUR_PHILOSOPHY.md) explains the underlying
ideas, and [REASONS_WHY.md](content/REASONS_WHY.md) covers what they actually buy
you.

## How contributing works — five steps

One difference from tools like Google Docs matters here: in Google Docs,
your edits appear for everyone instantly. In this project, **your changes
are drafted privately and join the shared project only after review.**
That is what makes it safe for many people — and many AI assistants — to
work at the same time. The whole loop:

1. **Set up your AI tool** (one time). See
   [Setting up your AI tool](#setting-up-your-ai-tool) below for your
   tool's exact steps.
2. **Ask what needs doing.** Say *"What are the open items?"* — the
   assistant reads the project's to-do list for you. (This step is
   optional: changes you think of yourself are just as welcome.)
3. **Describe the change you want.** The assistant makes it on your own
   private working copy — a version of the project only your conversation
   touches, so nothing you do can break the shared project.
4. **Look at what it made.** The assistant's reply ends with links to the
   changed files; open them and ask for adjustments until it's right.
5. **Say "propose this to the team."** The assistant packages your change
   for review — the technical name is a *pull request* — and an
   administrator, not you, decides when it joins the shared project.
   Until that happens, nobody else sees your change: unlike Google Docs,
   nothing becomes shared automatically.

## Setting up your AI tool

Before any of it works, an administrator must have given your GitHub
account access to `themorgan/WorkingWithAI` — if you don't
have access yet, ask Morgan (morgan@westegg.com). Then follow the section
for your tool:

### Claude users (Claude Code)

The most complete experience, on web, desktop, or phone. *(As of
2026-08.)*

1. Go to [claude.ai/code](https://claude.ai/code) (or open the Claude
   mobile app's Code area).
2. Start a new session on `themorgan/WorkingWithAI` — the
   first time, approve the GitHub authorization it requests.
3. **If this is Morgan, or the first session in a while:** ask it to also
   add the `themorgan/precedent-team-maintainers` repo (and, if you're
   Morgan, `themorgan/precedent-individual` too) before doing anything
   else — *"also add repo themorgan/precedent-team-maintainers"* is
   enough. This is what lets the project's team (and Morgan's own
   personal) practices actually apply; skipping it isn't a mistake, it
   just means those don't kick in for that session. See
   `AGENTS.md`'s "Build-environment gotchas" for why this is a one-time,
   per-session ask rather than something wired in permanently.
4. Ask your first question, e.g.: *"Review the project context, then tell
   me what needs my attention."*

Claude Code reads the project's instruction files automatically. Nothing
else to set up.

### Codex users

*(As of 2026-08.)*

1. Open Codex (in ChatGPT or at its own interface) and connect it to
   `themorgan/WorkingWithAI`.
2. Codex follows the project's instruction files automatically.
3. Give it a task or a question, the same way as any coding session.

### ChatGPT users

A plain ChatGPT conversation with the GitHub connector can **read** this
project and answer questions dependably. **Making changes** from a plain
conversation is not currently reliable *(as of 2026-08)* — have Codex
make the changes, or hand them to a teammate who uses Claude Code or
Codex; the project's automatic checks protect the result either way.

1. Connect the GitHub connector to `themorgan/WorkingWithAI`
   if you haven't.
2. Start each new project conversation with:

   > Work on `themorgan/WorkingWithAI`. Start with its README
   > and follow the repository's agent instructions before answering.

3. Then ask your question or describe the change you want.

### Gemini users

The Gemini CLI (a desktop tool) is already wired to this project's
instructions — nothing for you to configure. *(As of 2026-08; a
phone-based Gemini workflow is unverified.)*

### Grok users

Not yet verified with this workflow *(as of 2026-08)*. If Grok can reach
the repository, use the same starting instruction as ChatGPT users above.

### Any other assistant

Any assistant that can read this repository understands the same one-line
opener:

> Work on `themorgan/WorkingWithAI`. Start with its README and
> follow the repository's agent instructions before answering.

## Tips while you work

- **Ask before hunting.** The fastest way to learn anything about this
  project is to ask your assistant — it reads the project's map and
  decision records for you.
- **Ask what's new.** Approved changes don't appear in your old
  conversations by themselves. Each new session, the assistant catches
  you up on what changed since you last worked — and you can ask
  *"what's new?"* at any time.
- **Change by describing, not editing.** Say what is wrong and what you
  want instead; the assistant makes the change everywhere it applies and
  the team reviews it before it becomes shared.
- **Your work is credited to Morgan F.** Every commit in this project is
  authored as "Morgan F" (a GitHub noreply address, never a real inbox),
  with the assistant recorded as a co-author. See
  [`commit-author`](https://github.com/themorgan/precedent-individual/blob/main/practices/commit-author.md)
  if you ever need to change that.
- **Small calls happen without asking.** The assistant makes small and
  moderate judgment calls itself and tells you what it decided when the
  work is done, instead of interrupting you for each one. It still stops
  and asks first for anything genuinely big. See
  [`small-calls`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/small-calls.md).

## For the administrator: approving changes

Members draft changes on their own private copies; nothing joins the
shared project until you approve it. Your side of the loop is also just
conversation:

- **Ask "what's waiting for me?"** Your assistant lists each pending
  proposal and summarizes it in plain language.
- **Three answers, all in chat:** *approve* ("merge it"), *adjust*
  ("merge it, but keep the old title"), or *send back*.

### Automatic checks installed for this project

- **A Markdown check runs on every pull request** (a GitHub Actions
  workflow) and catches formatting mistakes before they reach the shared
  project. It needs no maintenance. Details:
  [process/upstream/GITHUB_ACTIONS.md](process/upstream/GITHUB_ACTIONS.md).
- **A light check runs on every push and pull request** — merge-conflict
  markers, broken syntax, obvious secret-shaped strings, and broken
  in-repo doc links, beyond what the Markdown check looks for. Details:
  [`light-check`](https://github.com/themorgan/precedent-team-maintainers/blob/main/practices/light-check.md).
- **A scheduled check for BestPractice updates, normally unattended —
  weekly by default** (Mondays; a commented-out daily cron line sits right
  next to the active weekly one in the workflow file), when upstream has
  moved, takes the update, integrates it using its own judgment, and opens
  and merges a pull request — noting every judgment call in the commit
  message for you to review after the fact. **Currently paused** (its
  schedule is commented out) for the duration of a beta test that
  deliberately tracks a not-yet-merged BestPractice branch instead of the
  usual released one — see [process/PRECEDENT_MIGRATION.md](process/PRECEDENT_MIGRATION.md) for why and
  when it resumes. While paused it can still be run by hand
  (`workflow_dispatch`), and needs one Claude credential either way —
  either works, only one is required:
  - `CLAUDE_CODE_OAUTH_TOKEN` — the preferred option if you're a Claude
    Pro or Max subscriber: run `claude setup-token` locally (Claude Code
    CLI) to generate it, then add it at this repository's **Settings →
    Secrets and variables → Actions → New repository secret**, named
    `CLAUDE_CODE_OAUTH_TOKEN`. No separate API billing.
  - `ANTHROPIC_API_KEY` — an Anthropic API key with billing enabled,
    added the same way, named `ANTHROPIC_API_KEY`.

  It also needs **Settings → General → Pull Requests → "Allow auto-merge"**
  turned on, and Actions allowed to create pull requests (**Settings →
  Actions → General → Workflow permissions → "Allow GitHub Actions to
  create and approve pull requests"**). If neither Claude credential is set
  when upstream has moved, the workflow skips the update cleanly and leaves
  a `::warning::` in that run's summary — check the Actions tab's run
  summaries if a scheduled run seems to have done nothing. A chat session
  can take the update manually in the meantime without either secret; if it
  does, it should remind you to set one. Details:
  [`bestpractice-sync`](https://github.com/themorgan/precedent-individual/blob/main/practices/bestpractice-sync.md).
- **Team practices resolve live from a sibling checkout, with no vendoring
  and no sync to run** — [precedent-team-maintainers](https://github.com/themorgan/precedent-team-maintainers)
  is read directly, so there's nothing to keep in sync and no token to
  provision. The one thing this does require: whatever environment runs a
  session on this project needs read access to `precedent-team-maintainers`
  as well (the same access this project's own repo needs), since
  `precedent.json` expects to find it checked out as a sibling directory.
- **A second scheduled check keeps the voice guidelines current** — same
  weekly-by-default, daily-optional cadence, pointed at
  [SoundHuman](https://github.com/themorgan/SoundHuman)
  (private) — the "write like a human, not an LLM" ruleset this project's
  own writing follows. **This needs its own repository secret named
  `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN`** — a GitHub personal access token
  (fine-grained, read-only, scoped to just that one repo):
  1. Generate the token at
     [github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta):
     resource owner your account, repository access "Only select
     repositories" → `themorgan/SoundHuman` only,
     permissions **Contents → Read-only**, nothing else. Copy the value
     immediately — GitHub only shows it once.
  2. Add it at this repository's **Settings → Secrets and variables →
     Actions → New repository secret**, named
     `VOICEGUIDELINESTOSOUNDHUMAN_TOKEN`.

  Same **"Allow auto-merge"** and Actions-can-open-PRs toggles, same
  Claude-credential requirement, and the same clean-skip behavior if either
  is missing. Details: [AGENTS.md](AGENTS.md)'s "Voice" section.
- **Every pull request opens with a standard template** — what changed,
  why, files touched, and a short checklist. An unchecked box on that
  checklist is normal.
- **This repo's default branch.** GitHub only defaults a freshly-created
  repository to `main` on its own — this repo started completely empty,
  with no branches at all, so the very first branch pushed to it became
  the default automatically. If **Settings → General → Default branch**
  doesn't already show `main`, switch it there (a `main` branch with the
  same install content is already pushed, ready to be set as default), then
  delete the old default branch once you've confirmed `main` looks right.
