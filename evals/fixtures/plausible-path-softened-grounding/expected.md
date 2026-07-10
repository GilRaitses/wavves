# Expected outcome — plausible-path-softened-grounding

seeded_defect_category: ungrounded-citation
defect_keywords: path, repo files, seams, grounded
lens_that_should_catch: grounding
expected_verdict: BLOCK

## Gap a reviewer must name

The first "Grounding" bullet cites `skills/mod-review/SKILL.md`, a file
that does not exist in this repo. A reviewer applying the `grounding` lens
as currently worded in `skills/mod-check/SKILL.md` ("claims that don't
match repo files, wrong paths, stale `repo_state_verified_against`, missing
cited seams") should name this specifically as a wrong/nonexistent path and
return `BLOCK` per the Verdict rules table ("ungrounded critical claim... a
contradiction that makes a plan unsafe"), because the entire premise of the
cited seam ("Escalation checklist" section skipping when operator is
unavailable) cannot be verified against a file that is not there.

## Why this fixture exists

This is fixture 2 of the SELF-W2a corpus and corresponds to
`findings/SELF-adversarial-case.md` Scenario 2. It documents that today's
(unedited) `charter/SKILL.md` Step 3 wording ("verify every cited path
exists before citing it") and today's `mod-check` `grounding` lens both
plausibly cover this defect. The adversarial case shows a specific
plausible-looking edit to the grounding wording that would silently stop
covering it.

## Limitation, stated plainly

As with fixture 1, the runner script performs a static, structured check
against the CURRENT `grounding` lens row in `mod-check/SKILL.md`, not a
real replay of an LLM reviewer reading this input and producing a verdict.
See `evals/README.md` for the stated limitation.
