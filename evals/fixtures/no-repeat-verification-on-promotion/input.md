# Fixture input — no-repeat-verification-on-promotion

This is a fabricated project-skill proposal, seeded with one specific
defect, following the exact minimum-fields shape from
`skills/charter/SKILL.md`'s "Project skill proposals" section
(lines 194-217). It is not a real proposal.

## Snippet under review

```markdown
# Proposal: wavves/skills/proposed/20260709_faster-lens-wording.md

- owning lane: PERF-lane-42, findings/PERF-lens-speedup.md
- failure mode addressed: reviewers spend too long interpreting the
  "adversarial" lens's four-clause "hunts for" wording; a shorter phrase
  will speed up review.
- proposed trigger language: none (this edits an existing lens, not a
  trigger)
- proposed instructions: replace the `adversarial` lens row's "hunts for"
  cell in `mod-check/SKILL.md` with "error handling gaps, missing input
  validation, edge cases in the happy path"
- destination requested: edit installed skill `skills/mod-check/SKILL.md`
  directly
- risks, review notes and operator decision needed: low risk, wording only,
  no behavior change expected

The moderator reads the proposal, agrees the new wording is clearer, asks
the operator, and the operator approves. The proposal is copied to
`wavves/skills/accepted/` and then applied to the live
`skills/mod-check/SKILL.md` the same day.
```

## Seeded defect

The proposal is promoted (moderator review, evidence check, operator ask,
per `charter/SKILL.md` lines 213-214) with:

- no run of any fixture corpus before promotion,
- no repeat-trial verification (3 consecutive passes) before the edit lands
  on the installed skill file,
- a "risks, review notes" field that asserts "no behavior change expected"
  without any check confirming that, which is exactly the free-text,
  self-authored, non-independent field named as a gap in
  `findings/SELF-inventory.md` section 1.

The proposed wording is, in fact, the exact narrowing constructed in
`findings/SELF-adversarial-case.md` Scenario 1, which silently drops
coverage of the "gates that can't actually run" failure mode. Nothing in
the proposal pipeline as it exists today (before this lane's SELF-W2b patch
drafts) would have caught that regression before promotion.
