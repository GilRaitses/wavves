# MKK — mod-kick-check

## Intent

Adversarial sanity-check of `feature-requests/20260808_mod-kick.md`.
No build. No implementation plan.

## Artifact

- path: `feature-requests/20260808_mod-kick.md`
- landing_commit_hash: `n/a` (working-tree FR; not yet committed at check start)
- branch: `main`
- repo_state_verified_against: `b7ce95f075e89183a49e0486b6764ec299aeecac`
- index: `feature-requests/README.md` row FR-20260808-mod-kick

## Locked

- read-only reviewers
- verdict must be GO | REVISE | BLOCK with named gaps
- product FR → include proof-bar (W1e)
- distinguish kick vs mod-rotate; do not collapse products
- no invent of BUILD plan

## Waves

### Wave 1 — adversarial check (parallel, high-reasoning)

- MKK-W1a grounding → findings/MKK-grounding.md
- MKK-W1b contradictions → findings/MKK-contradictions.md
- MKK-W1c completeness → findings/MKK-completeness.md
- MKK-W1d adversarial → findings/MKK-adversarial.md
- MKK-W1e proof-bar → findings/MKK-proof-bar.md

### Gate

- MKK-VERDICT: O0 reconciles into findings/MKK-verdict.md.
  Pass metric: every blocking gap named with evidence, or GO with zero blockers.

## Out of scope

- writing the implementation plan
- code changes / skill authorship
- commits / push / deploy
- chartering BUILD
