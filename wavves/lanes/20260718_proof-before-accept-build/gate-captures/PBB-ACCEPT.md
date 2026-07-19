# PBB-ACCEPT — gate capture

lane: PBB (proof-before-accept-build)
gate: PBB-ACCEPT
date: 2026-07-18 (America/New_York)
evaluator: O0 (independent of PBB-W1/W2 authorship)
repo_state_verified_against: `09c4e575e745956803180839540a5c3e16cb52e7`
INT unlock: operator proceed alias `¯\_(ツ)_/¯` (prior turn)

## Pass metric (stated before the run)

1. `python3 evals/check_proof_before_accept.py` → PASS all fixtures
2. Playbook + EXECUTION_WIRING document classifier, freeze allowlist, opt-out
   rationale, harness
3. No `/proof-gate` skill directory
4. Paragraph-tunnel surfaces still pass mechanical regression

## (1) Mechanical checker — measured

```
PASS  proof-before-accept-no-visual-fail: verdict=FAIL fail_ids=['PROC-NO-VISUAL']
PASS  proof-before-accept-optout-no-rationale-fail: verdict=FAIL fail_ids=['PROC-PASS-NO-PROOF']
PASS  proof-before-accept-proc-pass-no-proof-fail: verdict=FAIL fail_ids=['PROC-PASS-NO-PROOF']
PASS  proof-before-accept-with-proof-pass: verdict=PASS fail_ids=[]

summary: pass=4 fail=0 total=4
EXIT:0
```

Capture: `gate-captures/PBB-ACCEPT-proof.json`

## (2) Spot-check — locks present

| lock | evidence | result |
|---|---|---|
| classifier `proof_required` | playbook + charter SKILL Meta | PASS |
| freeze + allowlist | playbook steps 4; EXECUTION_WIRING Rule 2b | PASS |
| opt-out rationale | playbook + mechanical optout fixture | PASS |
| harness named | `check_proof_before_accept.py` + Rule 2b DOM/host contract | PASS |
| proof-bar conditional | mod-check SKILL.md | PASS |
| AUTH sync proof_job | mod-decide SKILL.md step 5b | PASS |
| router | wavves SKILL.md playbook row + list | PASS |

## (3) No slash skill

`skills/proof-gate` does not exist.

## (4) Paragraph-tunnel regression

`python3 evals/check_paragraph_tunnel.py` → summary pass=6 fail=0 total=6.

## Known gap (disclosed, non-blocking for method ACCEPT)

`scripts/proof_host_probe.py` not shipped; EXECUTION_WIRING names the JSON
contract and example command for product lanes to bind.

## Originating-mod read (O0.R3 → wavves_build)

Landed `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md`
(`538437c`). Summary: PBB matches method fail (`PROC-PASS-NO-PROOF`); keep
C+D+B+E; do not reopen. Felt-product / product-look bar is the **product-look lane**
(originating product repo), not a PBB regress. Before next visitor product
`proof_required: yes`: DOM hard
+ capture-then-grade + independent product-look grade + author ≠ ACCEPT +
ship probe (or cite Playwright `clientHeight`).

## Verdict

**PASS.** PBB ACCEPT criteria met for the method surface (playbook +
mechanical evals + skill wiring). FR-20260718 shipped. No reopen.
