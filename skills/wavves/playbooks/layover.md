# Layover playbook

Route: **layover** (`/layover`)

```
- [ ] 1. Verify <repo>/wavves/ exists. If missing, run bootstrap first.
- [ ] 2. Read the layover skill (skills/layover/SKILL.md) in full.
- [ ] 3. Resolve the input: a .code-workspace file path, or an explicit
        folder list. Parse folders[].path relative to the workspace
        file's own directory when a workspace file was given.
- [ ] 4. Validate every resolved folder path exists on disk and is a git
        repo BEFORE any git check. Flag missing paths and non-git
        directories as blocking lines for that entry, distinctly.
- [ ] 5. Per valid repo, run the read-only check set: remotes (all of
        them, never assume "origin"), branch, upstream ahead/behind
        (explicit no-upstream / detached-HEAD handling, never 0/0),
        uncommitted tracked changes, untracked files (grouped by
        top-level directory or extension above 20 files), stash list.
- [ ] 6. Apply filename-pattern hints as soft "review this first" notes
        only. Never emit a safe/unsafe verdict for any file.
- [ ] 7. Write the report to wavves/layovers/<workspace-name>-<date>.md
        in the invoking repo's own wavves/ home (summary table, then a
        detail section per repo).
- [ ] 8. Confirm zero mutation: no git add|commit|push|stash ran against
        any audited repo during the run.
- [ ] 9. Report the report path, the summary table, and any blocking
        flags (missing paths, no-upstream repos, non-git folders) to the
        operator.
```

Lane types this playbook covers (same leaf skill, different operator framing):

| type | operator says |
|:-----|:--------------|
| pre-handoff audit | preflight this workspace before a cloud agent takes over |
| multi-repo inventory | what's local-only across these sibling repos |
| stale-clone check | what would a fresh clone of this repo miss |

This playbook produces a report only. It never stages, commits, or hands
off any of the audited repos; those steps are out of scope for `/layover`
and belong to a future skill.
