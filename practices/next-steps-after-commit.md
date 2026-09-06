---
slug:        next-steps-after-commit
title:       A reply that commits closes with an explicit Next Steps line
tier:        on-demand
severity:    default
applies_to:  ["**"]
occasion:    "ending a reply in which I committed something"
gates:       ["reply"]
index_clause: "after a commit, close the reply by naming what I still need to do"
checked_by:  null
defines:     []
status:      active
supersedes:  []
overrides:   null
added:       2026-09-04
approved_by: "Morgan F; revised 2026-09-04, Morgan F, to also require closing branch-deletion recommendations; revised again 2026-09-04, Morgan F, to require a direct merged-PR-page link for branches the session merges itself"
---
## Rule
Any reply that made a commit ends with an explicit **Next Steps** statement addressed to me: what, if anything, I need to do now. If there's nothing left for me to do, say so directly -- "There is nothing else you need to do" or equivalent -- rather than leaving it implied. This holds even when the reply already asked me a question or mentioned an action item earlier in its body: restate it at the end anyway, because the end is the part I'm least likely to miss.

That closing statement also names any branch, in any repo touched during the session, that the branch-cleanup method calls safe to delete: a branch whose most recent PR merged, or whose most recent PR closed without merging because a later PR superseded it (called out as such, separately from the merged ones) -- identified by who opened/drove that PR (my GitHub login, not git commit authorship, since a Claude Code commit is always authored as `Claude <noreply@anthropic.com>` regardless of who is running the session), and never a branch created by someone else, the default branch, or the branch the session itself is working on. A branch with an open PR, or no PR at all, is left alone and doesn't need naming here. Group the list by repo when more than one is touched; say plainly that there's nothing to flag when the method turns up no candidates.

Whenever the session itself merges a pull request, that closing line also names the branch that PR merged from, says it's now safe to delete, and gives a direct, clickable link to the merged PR's own page (e.g. `https://github.com/<owner>/<repo>/pull/<number>`) -- GitHub shows a one-click **Delete branch** button right there once a PR is merged, so the link is what turns "safe to delete" into something I can act on without hunting for it myself. Do this for every branch the session merges in that session, not just the last one, across whichever repo(s) the session touched. This is narrower than the branch-cleanup method above: it fires only for a PR the session itself merged in that same session. Naming a branch this way is never license to also scan for other, older merged branches beyond that -- retroactively hunting down every stale merged branch in a repo is a separate, one-off task, done only when I ask for it directly, not something this standing practice performs on its own.

## Detail
This isn't a request for a summary of what changed -- that's the commit message and diff's job. It's specifically about *my* follow-on actions: approve something, review a PR, run a command, answer a question the reply raised, wait on something else, or nothing at all. A reply with no commit in it doesn't need this -- it's the commit that makes the omission costly, since a commit is exactly the kind of action whose loose ends (a push still pending, a PR still to open, a check still red) are easy to bury in a long reply and easy for me to miss.

The branch-deletion note piggybacks on the same closing line for the same reason: a merged or superseded branch left lying around is exactly the kind of loose end this practice already exists to surface, and I'm no more likely to go looking for it unprompted than any other follow-on action. It's a recommendation, never an action taken on its own -- nothing gets deleted without my confirmation.

The session-merge case gets the extra link because the session already has everything the link needs -- it just performed that exact merge, so it knows the PR's URL without looking anything up. That's also why it stays scoped to that session's own merges rather than growing into a general branch audit: a broader sweep for other old merged branches sitting around a repo is real, separate work, with its own judgment calls about what's actually safe, and folding it silently into every closing line would turn a cheap habit into an open-ended chore.

## Why
I write long replies, and the important trailing detail -- a question I asked, a step I flagged as still needed -- gets lost in the length even when it was stated clearly earlier in the same message. Restating it as a short, explicit closing line costs little and means I never have to re-read a whole reply to find out whether anything is still on me. The same is true of a branch that's done its job: nobody deletes it unless someone is told it's safe to, and a direct link to the one page that already has the delete button saves me the extra step of finding that page myself.

## Story
Raised directly, as a standing personal preference, rather than in response to a specific missed handoff. Extended on 2026-09-04, in the same conversation that first worked out the identify-by-PR-author branch-cleanup method, to fold that method's output into this practice's existing closing line rather than leaving it as a one-off report. Extended again the same day to require a direct link to the merged PR's own page -- where GitHub's one-click Delete branch button already lives -- whenever the session performs the merge itself within that session, and to draw an explicit line between that narrow case and the broader branch-cleanup method's own scan, which this addition doesn't widen.

## Install
No mechanical check, for the same reason `go-merge` has none: this governs how a reply gets *written*, not any property of the repo tree, a commit, or a diff. There's no artifact after the fact that distinguishes a reply that correctly named "nothing else to do" from one that just happened not to need anything -- both leave an identical commit behind, and the one place the omission is visible is the conversation transcript itself, which a repo-scoped check script has no access to.
