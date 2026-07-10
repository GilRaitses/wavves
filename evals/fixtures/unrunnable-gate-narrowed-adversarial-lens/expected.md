# Expected outcome — unrunnable-gate-narrowed-adversarial-lens

seeded_defect_category: unrunnable-gate
defect_keywords: gate, run, harness, pass
lens_that_should_catch: adversarial
expected_verdict: REVISE

## Gap a reviewer must name

The acceptance wave's gate ("run the acceptance test suite and confirm
everything passes") is described but not runnable by an outside party: no
command, harness, invocation point or pass/fail threshold is stated. A
reviewer applying the `adversarial` lens as currently worded in
`skills/mod-check/SKILL.md` ("failure modes, unsafe defaults, \"works on
happy path only\", gates that can't actually run") should name this
specifically as a "gate that can't actually run" and return `REVISE`, not
`GO`, until the spec states the concrete harness and pass metric.

## Why this fixture exists

This is fixture 1 of the SELF-W2a corpus and corresponds to
`findings/SELF-adversarial-case.md` Scenario 1. It documents that today's
(unedited) `adversarial` lens wording plausibly covers this defect. The
adversarial case shows a specific plausible-looking edit to that lens's
wording that would silently stop covering it.

## Limitation, stated plainly

This `expected.md` and the runner script that reads it do not replay an
actual `mod-check` review. The runner performs a static, structured check:
does the CURRENT `adversarial` lens row in `mod-check/SKILL.md` contain
wording that plausibly maps to `unrunnable-gate` (via the `defect_keywords`
list above)? A PASS here means "the current lens wording still claims
coverage of this category," not "an LLM reviewer, given this input, would
actually produce a REVISE verdict." That gap is named in `evals/README.md`
as a known limitation for a future wave with a real replay harness.
