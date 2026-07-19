# PBA — proof-before-accept-check

## Intent

Adversarial sanity-check of
`feature-requests/20260718_proof-before-accept.md`. No build. No
implementation plan.

## Artifact

- path: `feature-requests/20260718_proof-before-accept.md`
- landing_commit_hash: n/a
- branch: `main`
- repo_state_verified_against: `af0c0788cb2dbb865cbce6721fcdcbf6642b11d4`
- evidence cited: originating product repo doctrine
  (multi-surface proof-then-consume yaml, foreign pin);
  visitor rebuild / product-look / beta visitor lanes

## Locked

- read-only reviewers (check wave only)
- high-reasoning / **Grok only** (`cursor-grok-4.5-high-fast`) for every wave member
- verdict must be GO | REVISE | BLOCK with named gaps

## Locked decisions (do NOT reopen)

- PBA-LAND: C+D+B+E; defer slash-skill A
- PBA-CLASSIFIER: waveset field proof_required: yes|no|n/a
- PBA-HARNESS: DOM/host-metrics hard + mechanical check_proof_before_accept.py; screenshot optional
- PBA-FREEZE: non-proof-serving freeze + proof-serving allowlist
- PBA-OPTOUT: none/no require rationale on proof_required:yes
- PBA-LENS: proof-bar conditional default for proof_required:yes / product-visitor FRs

## Waves

### Wave 1 — adversarial check (parallel, high-reasoning) — COMPLETE

- PBA-W1a grounding → findings/PBA-grounding.md (REVISE)
- PBA-W1b contradictions → findings/PBA-contradictions.md (REVISE)
- PBA-W1c completeness → findings/PBA-completeness.md (REVISE)
- PBA-W1d adversarial → findings/PBA-adversarial.md (REVISE)

### Gate

- PBA-VERDICT: **REVISE** → findings/PBA-verdict.md → mod-decide complete

### Next (not this check lane)

- BUILD charter with Locked decisions pasted (C+D+B+E). Grok-only subagents.

## Out of scope

- writing the implementation plan
- code changes
- commits / push / deploy

## Model routing

| role | recommended_model_tier | reason |
|---|---|---|
| every wave member | cursor-grok-4.5-high-fast | adversarial judgment; house Grok lock for check lanes |

**model_enforcement:** every Task/subagent launch MUST set
`model: cursor-grok-4.5-high-fast`. No Claude/Composer fallback.
