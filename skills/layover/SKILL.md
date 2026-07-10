---
name: layover
description: >-
  Reads a bespoke multi-root .code-workspace file (or an explicit folder
  list) and produces a read-only preflight audit of every sibling repo:
  remotes, branch-vs-upstream sync state, uncommitted tracked changes,
  untracked files, and stashes. Use for /layover, or when preflighting a
  bespoke multi-repo desktop workspace before a cloud agent takes over
  moderation of one of its repos, so the operator knows exactly what
  local-only state a fresh clone would never see. Audit-only: writes
  nothing but its own report, mutates no audited repo.
disable-model-invocation: true
---

# layover

A read-only preflight audit for a bespoke, desktop-only, multi-root
workspace. Cursor's cloud agents attach per-repo to a pushed remote; they
cannot open a local `.code-workspace` file spanning several sibling repos.
Before a cloud agent takes over moderation of any one of those repos, `/layover`
tells the operator exactly what local-only state exists in each sibling that
a fresh clone from the remote would never surface.

The audit is the entire scope. Staging, hydration-file writing and actual
handoff mechanics are explicitly out of scope for a future skill, not built
here.

## Non-negotiables

1. **Audit-only.** `/layover` writes exactly one file: its own report. It
   performs no other write, anywhere, ever.
2. **Zero mutation of audited repos.** Only read-only git commands run
   against any audited repo: `git config --get`, `git rev-parse`,
   `git rev-list`, `git status` (no flags that stage or discard), `git
   stash list`, `git ls-files --others`. Never `git add`, `git commit`,
   `git push`, or `git stash` (the mutating verb, as opposed to `git stash
   list`). This holds against every audited repo, without exception, even
   when a repo looks safe to tidy up.
3. **Never classify a file as confirmed-safe.** Every untracked or
   uncommitted file carries the same top-level flag: needs human review
   before staging. A filename-pattern hint (see below) may add a soft
   "review this one first" note. It never produces a hard safe/unsafe
   verdict, and a pattern miss is never read as clearance.
4. **Sibling inventory only.** `/layover` maps which repos make up the
   workspace and each one's standalone git health. It does not trace
   imports, submodules, or cross-repo code references.
5. **Generic input.** `/layover` takes a `.code-workspace` file path or an
   explicit folder list. It is not a script bound to one operator's
   workspace.

## Input format

One of:

- A path to a `.code-workspace` file. Parse its top-level `folders` array;
  each entry's `path` is resolved relative to the **workspace file's own
  directory** (not the current working directory), matching VS Code /
  Cursor's own resolution rule. Absolute paths are used as-is.
- An explicit list of folder paths, when the operator names folders
  directly instead of a workspace file.

**Path validation runs before any git check.** For each resolved folder:

- Path does not exist on disk: flagged, blocking line for that entry
  ("path does not exist"). No git check runs against it.
- Path exists but has no `.git`: flagged, blocking line, distinct message
  ("exists but is not a git repository"). No git check runs against it.
- Path exists and is a git repo: proceed to the per-repo checks below.

A `.code-workspace` file that fails to parse as JSON is its own flagged,
blocking line for the whole run ("workspace file did not parse as JSON"),
not a crash and not a silent skip.

## Per-repo checks

Run in this order, all read-only:

1. **Remotes.** `git config --get-regexp '^remote\..*\.url$'`. Lists every
   configured remote by name and URL. Never assumes the remote is named
   `origin` — some repos use a different name or carry more than one. Zero
   remotes configured is its own reported state ("no remote configured"),
   never left blank.
2. **Branch.** `git rev-parse --abbrev-ref HEAD`. A detached HEAD (literal
   output `HEAD`) is itself a flagged condition, since a fresh clone
   defaults to the remote's default branch, not a detached commit.
3. **Upstream ahead/behind, including the no-upstream case.** First check
   `git rev-parse --abbrev-ref --symbolic-full-name @{u}` and read its exit
   code, not just its stdout. A non-zero exit (no upstream configured, or
   detached HEAD) is reported literally as `no upstream configured` (or the
   detached-HEAD variant) — never coerced into `0/0` and never silently
   skipped. Only when that check exits `0` does the audit run
   `git rev-list --left-right --count @{u}...HEAD`, which prints
   `<behind>\t<ahead>` (left = commits in upstream not in HEAD, right =
   commits in HEAD not in upstream).
4. **Uncommitted tracked changes.** `git status --porcelain=v1
   --untracked-files=no`. Empty output means the tracked tree is clean.
5. **Untracked files, with grouping above 20.**
   `git ls-files --others --exclude-standard` (respects `.gitignore`).
   - 20 files or fewer: report the flat path list.
   - Above 20: group by top-level path segment (the first directory
     component) with a per-bucket count, sorted descending, instead of
     dumping a flat list. Files sitting directly at repo root (no `/` in
     the path) go into a synthetic `(root)` bucket; if that bucket alone
     still exceeds 20, sub-group it by file extension.
   - The full flat list is never discarded. State in the report that it is
     available on request, without printing it inline once grouped.
   - Filename-pattern hint: a file matching `*.env`, `*.pem`, `*.key`,
     `credentials*.json`, `*secret*`, `id_rsa` (or similar) gets a soft
     "review this one first" annotation next to its entry (or, once
     grouped, a count of how many matched files fell into that bucket).
     This is a hint only. It never becomes a safe/unsafe verdict per
     Non-negotiable 3, and its absence never means a file is clear.
6. **Stashes.** `git stash list`. Empty means no stashes. Non-empty is
   reported as the full list of stash entries — stashes are the same class
   of local-only-invisible-to-a-fresh-clone risk as untracked files and
   unpushed commits, so they are never skipped.

## Report template

One markdown file per run. Sections, in order:

```markdown
# layover — <workspace-name> — <YYYYMMDD>

## Summary

| repo | path | remotes | branch | vs upstream | uncommitted | untracked | stashes | flags |
|---|---|---|---|---|---|---|---|---|
| <name> | <resolved path> | <count> | <branch> | <ahead>/<behind> or "no upstream" | clean/dirty | <count> | <count> | <blocking flags, if any> |

## <repo name>

- path: <resolved path>
- remotes: <name -> url, one per line, or "no remote configured">
- branch: <branch, or "detached HEAD">
- vs upstream: <ahead>/<behind>, or "no upstream configured"
- uncommitted tracked changes: <clean, or the porcelain lines>
- untracked files: <count>. <flat list if <=20, grouped-by-directory table
  if >20, full list stated as available on request>
- review-first hints: <filename-pattern matches, if any, with the explicit
  caveat that this is a soft note, never a verdict>
- stashes: <none, or the full stash list>

<repeat per repo, including a section for any path-validation failure with
its blocking reason and no git detail beneath it>
```

Never render a per-file or per-repo verdict of "safe". The strongest
language available for any file is a review-first hint; the report's job is
to surface what a fresh clone would miss, not to certify what is fine to
discard or stage.

## Output path

`wavves/layovers/<workspace-name>-<YYYYMMDD>.md`, in the **invoking repo's
own** `wavves/` home (not the audited repos — none of them are written to,
per the zero-mutation guarantee). `<workspace-name>` derives from the
`.code-workspace` file's basename (without the extension), or from an
operator-supplied label when the input was an explicit folder list.

If the invoking repo has no `wavves/` home yet, route to the `bootstrap`
playbook (`wavves-init`) first, the same rule the router already applies
before `/charter`.

## Related

- `wavves` (`/wavves`) routes here when the operator wants a workspace
  preflight before a handoff.
- `charter` (`/charter`) is the full multi-wave lane system this skill was
  built under; `/layover` itself is a single-purpose leaf skill, not a lane.
- `wavves-init` (`/wavves-init`) for the bootstrap-first case.
