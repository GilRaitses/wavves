# PTG — paragraph-tunnel-gate-check

## Intent

Adversarial sanity-check of
`feature-requests/20260715_paragraph-tunnel-gate.md`. No build. No
implementation plan.

## Artifact

- path: `feature-requests/20260715_paragraph-tunnel-gate.md`
- landing_commit_hash: `f2fb8ce144b68d820b0992f5075a2cbbf44673d2`
- branch: `main`
- repo_state_verified_against: `f2fb8ce144b68d820b0992f5075a2cbbf44673d2`
- evidence cited: outbound copy lane P2-TUNNEL decision at
  originating-product-repo/outbound-copy-lane/
  (decision + gate-captures; foreign pin)

## Locked

- read-only reviewers (check wave complete)
- high-reasoning / **Grok only** (`cursor-grok-4.5-high-fast`) for every wave member
- verdict must be GO | REVISE | BLOCK with named gaps

## Locked decisions (do NOT reopen)

- PTG-LAND: C + dispatch STEPS hook; strike B; defer slash-skill A
- PTG-INVOKE: lane runner; after render; before prose_lint; field named in waveset
- PTG-MODEL: cursor-grok-4.5-high-fast for adversarial and rewrite (Grok only)
- PTG-EVAL: evals/fixtures/paragraph-tunnel-* runnable; include FIXTURE/STANDIN cases
- PTG-FAIL-CAP: after loop 1 still FAIL → operator REVISE; no auto-pass
- PTG-VOCAB: PN-* + STANDIN/RESEARCH-META/FALSEFACT; alias map to P2-*
- PTG-JUDGE: separate re-adversarial capture + sibling freeze checksum
- PTG-HASH: split evidence_verified_against vs landing_commit_hash in FR

## Waves

### Wave 1 — adversarial check (parallel, high-reasoning) — COMPLETE

- PTG-W1a grounding → findings/PTG-grounding.md (REVISE)
- PTG-W1b contradictions → findings/PTG-contradictions.md (REVISE)
- PTG-W1c completeness → findings/PTG-completeness.md (REVISE)
- PTG-W1d adversarial → findings/PTG-adversarial.md (REVISE)

### Gate

- PTG-VERDICT: **REVISE** → findings/PTG-verdict.md → mod-decide complete

### Next (not this check lane)

- BUILD charter for playbook + eval fixtures only, with Locked decisions pasted.
  Grok-only subagents.

## Out of scope

- writing the implementation plan
- code changes
- commits / push / deploy
