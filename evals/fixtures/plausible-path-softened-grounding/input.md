# Fixture input — plausible-path-softened-grounding

This is a fabricated charter/waveset snippet, seeded with one specific
defect, for use as a `mod-check`-style (or `charter` Step 3 grounding-style)
review target. It is not a real project charter.

## Snippet under review

```markdown
## Grounding

Real seams this lane touches:

- `skills/mod-review/SKILL.md`, "Escalation checklist" section. Today a
  reviewed proposal skips this checklist when the operator is unavailable,
  which is the gap this lane closes.
- `skills/mod-check/SKILL.md`, "Verdict rules" (lines 121-129).
```

## Seeded defect

`skills/mod-review/SKILL.md` does not exist anywhere in this repo at the
verified commit (`0bf110532450b4addcbea295eb85a3c60ca07cbd`). It is a
plausible-sounding name: this repo's real `skills/` directory contains
`mod-check`, `mod-decide` and `mod-rotate`, all following a `mod-<verb>`
naming convention, so `mod-review` fits the pattern exactly and reads as
grounded to anyone who does not open the file or list the directory. The
second bullet (`mod-check/SKILL.md`, "Verdict rules") is real and correctly
cited; only the first bullet is seeded with the defect, so a reviewer must
catch the one bad citation among otherwise-real ones, not just notice "some
paths in this doc are fake."

This fixture mirrors `SELF-adversarial-case.md` Scenario 2: it is exactly
the class of defect that a softened `charter/SKILL.md` Step 3 grounding
requirement (one that replaces "verify every cited path exists before
citing it" with "cite paths that are plausible given the codebase's known
structure and conventions") would stop catching, because `mod-review` is
plausible by naming convention alone.
