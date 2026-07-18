# FR-20260718 — Proof-before-accept (process-PASS fail mode)

- **Status:** ready-for-mod-check
- **Date:** 2026-07-18 (America/New_York)
- **Product surface:** wavves skills / charter ACCEPT templates / playbooks + evals
- **Source evidence (pax):**
  - `.ddb/decisions/pax_multi_surface_proof_then_consume_doctrine_v1_20260718.yaml`
  - `wavves/lanes/20260718_route-first-ux/` (RFU ACCEPT PASS while operator
    reported /beta felt empty; map height 0 until hotfix `c76e19b`)
  - `wavves/lanes/20260715_comfort-route-explorer/` + BETA W4 intent
    (alts + shade forks) vs process gates that scored shell honesty
- **evidence_verified_against:** pax `b083b5a76e580265ab3ebabaeb1df1053dc8a565`
  (repo state at FR authoring; doctrine lands in same pax pass — not this FR's landing)
- **landing_commit_hash:** _(O0 completion report only; never self-embed)_

## Problem

wavves can **PASS ACCEPT** on process metrics (LAND-C, honesty labels, e2e
shell, HEAD match) while the operator's **product Proof** never became
visible. That is a method failure mode, not only a product bug.

Symptoms observed in pax klosr beta program:

1. Multiple chrome rebuild lanes (BETA → CRE → RFU) without a frozen Proof.
2. ACCEPT graded mount/honesty/LAND-C, not "screenshot vs reference class."
3. Debt notes closed as residuals while the felt product stayed empty
   (including a height-0 map that still left chrome PASS).
4. No bake→visitor **consumer contract**, so workbench/chrome thrash is
   invited later.

**Fail id (proposed):** `PROC-PASS-NO-PROOF` — ACCEPT (or check) treats
process/shell gates as sufficient when the lane's named Proof job is unset,
unmeasured, or visually unverified.

## Feature sketch

Add a reusable **Proof-before-accept** pattern to wavves:

1. **Charter mandatory fields** — every product/UX lane must declare:
   - `proof_job` (one sentence, operator-facing)
   - `proof_reference` (path/URL/figure class or `none` with rationale)
   - `chrome_freeze` (what must not change until Proof ACCEPT)
   - `visual_accept` (screenshot/capture required: yes/no)
2. **mod-check lens** — new or extended adversarial lens hunts:
   - ACCEPT criteria that can PASS without the proof_job
   - chrome-only waves with no proof_job
   - debt-close treated as product done
3. **mod-decide / charter gate** — block BUILD unlock when `proof_job` missing
   on visitor/product lanes; require visual_accept capture path in ACCEPT
   dispatch when `visual_accept: yes`.
4. **EXECUTION_WIRING addition** — runnable visual gate: capture screenshot
   (or named DOM proof markers) and fail ACCEPT if proof markers absent or
   map host height 0 / blank black-canvas class.
5. **Evals** — fixtures: process-only ACCEPT criteria → FAIL; proof_job +
   visual capture present → PASS.

### Default fail vocabulary (method)

| id | fail condition |
|---|---|
| PROC-PASS-NO-PROOF | ACCEPT/check can green without measuring proof_job |
| PROC-CHROME-THRASH | New IA/chrome wave with no frozen proof_job |
| PROC-DEBT-AS-DONE | Residual debt close treated as product PASS |
| PROC-NO-VISUAL | visual_accept required but no capture harness |
| PROC-BLANK-CANVAS | Map/product host height 0 or empty canvas while chrome PASS |

## Where it lands (options for mod-decide)

| option | meaning | lean |
|---|---|---|
| A | New skill `/proof-gate` | optional later |
| B | Extend `mod-check` with a fifth default lens `proof-bar` | strong |
| C | Harden `charter` ACCEPT template + `EXECUTION_WIRING.md` visual rule | **required** |
| D | Playbook `skills/wavves/playbooks/proof-before-accept.md` + evals | **required** |
| E | Mention in `mod-decide` AUTH sync: proof_job must appear in waveset locks | strong |

Recommended combo for BUILD: **C + D + B** (charter+wiring + playbook/evals +
mod-check lens). Defer standalone skill (A) unless the playbook outgrows one
file.

## Acceptance (BUILD in wavves_build)

1. Charter template / playbook documents `proof_job`, `proof_reference`,
   `chrome_freeze`, `visual_accept`.
2. Eval fixture(s) under `evals/fixtures/` demonstrate PROC-PASS-NO-PROOF FAIL
   and a PASS case with proof fields + visual gate named.
3. `mod-check` (or playbook check) instructions require hunting process-only
   ACCEPT criteria on product lanes.
4. No install from this folder; ship only via chartered lane + operator accept.

## Non-goals

- Replacing purpose-gates / public-copy-gates / paragraph-tunnel.
- Mandating visual gates for pure research/read-only check lanes.
- Implementing klosr Proof-1 inside wavves_build (that is a pax/klosr lane).

## Operator note

Spawned from pax multi-surface Proof-then-consume ratification and the
operator judgment that beta process PASS did not equal a felt product.
Dispatch this FR from a wavves_build moderator thread (`/mod-check` first).
