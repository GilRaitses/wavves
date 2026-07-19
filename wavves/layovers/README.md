# layovers

Reports produced by `/layover`, the read-only preflight audit for a bespoke
multi-repo desktop workspace. One dated file per run, named
`<workspace-name>-<YYYYMMDD>.md`, where `<workspace-name>` comes from the
audited `.code-workspace` file's basename (or an operator-supplied label
when the input was an explicit folder list instead of a workspace file).

Each report covers every sibling repo the workspace names: remotes, branch
vs upstream sync state (including the no-upstream case), uncommitted tracked
changes, untracked files, and stashes. No report ever marks a file
confirmed-safe; filename-pattern hints add a soft review-first note only.

## What this is for

Eyes-open inventory before you **manually** attach a Cursor cloud agent to
**one** sibling repo. Cloud agents stay per-repo; they cannot open the local
multi-root workspace.

## What this is not

- Not a multi-repo cloud migration
- Not autoconfiguration of a cloud agent
- Not a substitute for starting `/wavves` or `/charter` in that cloud thread

This directory holds reports only. `/layover` never writes anywhere else,
and never mutates any audited repo it reads from.
