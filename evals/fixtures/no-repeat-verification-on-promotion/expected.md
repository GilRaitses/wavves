# Expected outcome — no-repeat-verification-on-promotion

seeded_defect_category: missing-regression-check-before-promotion
defect_keywords: acceptance criteria, rollback, assumptions
lens_that_should_catch: completeness
expected_verdict: BLOCK

## Gap a reviewer must name

The proposal has no acceptance criteria tied to any corpus or repeat-trial
check, and silently assumes "wording only, no behavior change expected" is
true without evidence. A reviewer applying the `completeness` lens as
currently worded in `skills/mod-check/SKILL.md` ("missing acceptance
criteria, unowned edges, silent assumptions, absent rollback / non-goals")
should name the missing acceptance criteria (no fixture corpus, no
repeat-verification requirement) and the silent assumption ("no behavior
change expected," asserted rather than checked) and return `BLOCK`,
because the proposal is about to land directly on an installed skill file
per `charter/SKILL.md` lines 213-216, with no independent check standing
between "the moderator agrees" and "the live file changes."

## Why this fixture exists

This is fixture 3 of the SELF-W2a corpus. It is not one of the two
Scenario fixtures from `SELF-W1b`; it is constructed directly from
`findings/SELF-inventory.md`'s finding that `charter/SKILL.md`'s promotion
path (lines 213-214, "the moderator reviews the proposal, checks evidence
and asks the operator") has no regression-check or repeat-trial requirement.
It demonstrates the same root-cause gap from a different angle: instead of
asking "would an edited lens still catch a defect," it asks "would today's
promotion pipeline even notice that the proposed edit itself is the
regression."

## Limitation, stated plainly

As with fixtures 1 and 2, the runner script performs a static, structured
check against the CURRENT `completeness` lens row in `mod-check/SKILL.md`,
not a real replay of an LLM reviewer reading this input and producing a
verdict. See `evals/README.md` for the stated limitation.
