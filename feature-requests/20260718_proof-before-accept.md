# FR-20260718 — Proof-before-accept (process-PASS fail mode)

- **Status:** chartered (BUILD lane `20260718_proof-before-accept-build`)
- **Check lane:** `wavves/lanes/20260718_proof-before-accept-check/`
- **Build lane:** `wavves/lanes/20260718_proof-before-accept-build/`
- **Date:** 2026-07-18 (America/New_York)
- **Product surface:** wavves skills / charter ACCEPT templates / playbooks + evals
- **Source evidence (pax @ `b083b5a76e580265ab3ebabaeb1df1053dc8a565`):**
  - `/Users/gilraitses/pax/.ddb/decisions/pax_multi_surface_proof_then_consume_doctrine_v1_20260718.yaml`
  - `/Users/gilraitses/pax/wavves/lanes/20260718_route-first-ux/` (RFU ACCEPT PASS on process/shell gates while operator reported /beta felt empty; post-ACCEPT collapsed MapLibre host height hotfix `c76e19b` per RFU waveset; PRP fail bar uses `clientHeight ≤ 0` class)
  - `/Users/gilraitses/pax/wavves/lanes/20260715_comfort-route-explorer/` (CRE ACCEPT PASS-WITH-RESIDUALS)
  - `/Users/gilraitses/pax/wavves/lanes/20260715_beta-visitor-interact/` (BETA W4 alts + shade forks vs process gates)
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
   (including a **collapsed / zero-height-class** map host that still left
   chrome PASS; see RFU waveset hotfix `c76e19b` and PRP `clientHeight ≤ 0`
   fail bar — not a transcribed pre-hotfix `clientHeight: 0` capture).
4. No bake→visitor **consumer contract**, so workbench/chrome thrash is
   invited later.

**Fail id (proposed):** `PROC-PASS-NO-PROOF` — ACCEPT (or check) treats
process/shell gates as sufficient when the lane's named Proof job is unset,
unmeasured, or visually unverified.

## Feature sketch

Add a reusable **Proof-before-accept** pattern to wavves:

1. **Charter mandatory fields** — every lane with `proof_required: yes` must
   declare (schema/homes locked in mod-decide):
   - `proof_job` (one sentence, operator-facing)
   - `proof_reference` (path/URL/figure class or `none` with rationale)
   - `chrome_freeze` (path/surface list that must not change until Proof ACCEPT)
   - `visual_accept` (`yes`/`no`; `no` requires rationale on proof_required lanes)
2. **mod-check lens** — new or extended adversarial lens hunts:
   - ACCEPT criteria that can PASS without the proof_job
   - chrome-only waves with no proof_job
   - debt-close treated as product done
3. **mod-decide / charter gate** — (fork: unlock vs ACCEPT-only; see options)
   when `proof_required: yes` and `proof_job` missing.
4. **EXECUTION_WIRING addition** — runnable proof gate with named harness
   command + JSON capture (prefer primary product host / DOM metrics; screenshot
   vs reference optional). Fail ACCEPT if proof markers absent or primary
   product host height ≤ 0 / blank-canvas class while chrome PASS.
5. **Evals** — mechanical fixtures (paragraph-tunnel shape): process-only
   ACCEPT criteria → FAIL with PROC-*; proof fields + named visual/DOM gate
   → PASS. Docs-only BUILD ACCEPT forbidden.

### Default fail vocabulary (method)

| id | fail condition |
|---|---|
| PROC-PASS-NO-PROOF | ACCEPT/check can green without measuring proof_job |
| PROC-CHROME-THRASH | New IA/chrome wave with no frozen proof_job |
| PROC-DEBT-AS-DONE | Residual debt close treated as product PASS |
| PROC-NO-VISUAL | visual_accept required but no capture harness |
| PROC-BLANK-CANVAS | Primary product host height ≤ 0 or empty canvas while chrome PASS |

## Where it lands (options for mod-decide)

| option | meaning | lean |
|---|---|---|
| A | New skill `/proof-gate` | optional later |
| B | Extend `mod-check` with a fifth default lens `proof-bar` | strong |
| C | Harden `charter` ACCEPT template + `EXECUTION_WIRING.md` visual rule | **required** |
| D | Playbook `skills/wavves/playbooks/proof-before-accept.md` + evals | **required** |
| E | Mention in `mod-decide` AUTH sync: proof_job must appear in waveset locks | strong |

**Locked for BUILD:** **C + D + B + E**. Defer standalone skill (A).
See `wavves/lanes/20260718_proof-before-accept-check/decisions/LOCKED-DECISIONS.md`.

## Acceptance (BUILD in wavves_build)

1. Charter template / playbook documents `proof_required` + the four fields
   with homes and pass metrics.
2. `python3 evals/check_proof_before_accept.py` (or named equivalent) PASS on
   `proof-before-accept-*` fixtures including PROC-PASS-NO-PROOF FAIL and a
   PASS case; capture under lane `gate-captures/`.
3. Named DOM/host harness command documented in EXECUTION_WIRING (runnable;
   not assertion-only). Screenshot-vs-reference may be optional operator step.
4. `mod-check` (or playbook check) instructions require hunting process-only
   ACCEPT criteria on `proof_required: yes` lanes.
5. No install from this folder; ship only via chartered lane + operator accept.

## Non-goals

- Replacing purpose-gates / public-copy-gates / paragraph-tunnel.
- Mandating visual gates for lanes with `proof_required: no` or `n/a`
  (research/read-only check, plugin-meta, outbound-copy-only).
- Implementing klosr Proof-1 inside wavves_build (that is a pax/klosr lane).

## Operator note

Spawned from pax multi-surface Proof-then-consume ratification and the
operator judgment that beta process PASS did not equal a felt product.
Mod-decide complete via operator `¯\_(ツ)_/¯` (proceed as recommended).
