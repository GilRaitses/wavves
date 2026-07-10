# Fixture input — unrunnable-gate-narrowed-adversarial-lens

This is a fabricated spec/plan snippet, seeded with one specific defect, for
use as a `mod-check`-style review target. It is not a real project spec.

## Snippet under review

```markdown
### Wave 3 — acceptance

`FOO-ACCEPT` verifies the new caching layer is safe to ship. The gate will
be verified by running the acceptance test suite and confirming everything
passes before promoting the change to `main`. On failure, the wave escalates
to O0.
```

## Seeded defect

The paragraph never states:

- which test suite (no path, no command),
- what harness or environment it runs in,
- what the pass/fail threshold is (all tests green? some allowed to skip?
  some flaky tests excluded?),
- who or what actually invokes it (a human, a CI job, the acceptance
  subagent itself).

"The gate will be verified by running the acceptance test suite" is a
claim that a gate exists and is runnable, with zero information that would
let an independent reviewer or a different agent actually run it. This is
the "gates that can't actually run" failure mode named in
`skills/mod-check/SKILL.md` line 79 (current, unedited wording) and in
`skills/charter/SKILL.md`'s Execution Wiring rule 2 ("Gates are runnable,
evidence is captured... the verdict cites measured numbers, never a
claim").

This fixture mirrors `SELF-adversarial-case.md` Scenario 1: it is exactly
the class of defect that a narrowed `adversarial` lens wording (one that
replaces "gates that can't actually run" with code-execution-flavored
clauses like "error handling gaps, missing input validation, edge cases in
the happy path") would stop catching, because an unrunnable-gate claim is
none of those three things.
