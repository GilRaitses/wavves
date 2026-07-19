# Proof-before-accept playbook

Route: **dispatch STEPS** (lane runner; no `/proof-gate` slash skill in v0)

Pre-ACCEPT gate for visitor/product surfaces that claim visual or runtime
proof. Order is fixed: **classify → declare fields → freeze chrome → run
harness → ACCEPT only on evidence**. Does not replace prose_lint or
mod-check. Does not invent a slash skill.

Model lock: adversarial and ACCEPT evaluator subagents MUST use
`model: cursor-grok-4.5-high-fast` (no Claude/Composer fallback).

Classifier: waveset field `proof_required: yes|no|n/a` (not keyword
inference). Defaults guidance: visitor/product execution → `yes`;
mod-check / research-discovery / plugin-meta / outbound-copy-only → `no`
or `n/a` with one-line rationale.

When `proof_required: yes`, waveset MUST name:

- `proof_job` (one sentence, operator-facing)
- `proof_reference` (path, URL, or figure class; or `none` with written
  rationale)
- `chrome_freeze` (non-proof-serving path/surface list plus proof-serving
  allowlist)
- `visual_accept` (`yes` / `no`; `no` requires written rationale)

Opt-out: `proof_reference: none` or `visual_accept: no` on
`proof_required: yes` without written rationale is FAIL
(`PROC-PASS-NO-PROOF`).

Closed fail vocab (label mechanical vs review/live):

| id | class | meaning |
|:---|:------|:--------|
| `PROC-PASS-NO-PROOF` | mechanical | ACCEPT claimed without required proof fields, harness, or opt-out rationale |
| `PROC-NO-VISUAL` | mechanical | visual proof required but missing or skipped without rationale |
| `PROC-CHROME-THRASH` | review / live | edits outside freeze; proof-serving allowlist violated |
| `PROC-DEBT-AS-DONE` | review / live | known debt or placeholder treated as ACCEPT-ready |
| `PROC-BLANK-CANVAS` | review / live (DOM/host) | height ≤ 0, collapsed, or blank canvas at proof surface |

Mechanical checker may emit only `PROC-PASS-NO-PROOF` and `PROC-NO-VISUAL`
(opt-out missing-rationale folds under `PROC-PASS-NO-PROOF`). Review/live
ids are not sole BUILD ACCEPT criteria from the fixture script alone.

Named harness:

- `python3 evals/check_proof_before_accept.py` (fixture / field gate)
- DOM/host hard gate for product ACCEPT:
  `python3 skills/charter/scripts/proof_host_probe.py` (see EXECUTION_WIRING
  Rule 2b). height ≤ 0 or blank-canvas → FAIL (`PROC-BLANK-CANVAS`)
- When `visual_accept: yes`, capture-then-grade is **required** (frozen
  captures + independent product-look review against `proof_reference`).
  DOM/host green alone is **not** ACCEPT-complete. Screenshot miss alone is
  never the blank-canvas hard gate; DOM/host metrics remain required.

```
- [ ] 1. Confirm waveset sets `proof_required` to yes, no, or n/a.
        If no or n/a, require one-line rationale. Stop this playbook when
        proof is not required; do not invent proof fields.
- [ ] 2. If `proof_required: yes`, confirm all four fields are present:
        `proof_job`, `proof_reference`, `chrome_freeze`, `visual_accept`.
- [ ] 3. If `proof_reference: none` or `visual_accept: no`, confirm written
        rationale is on disk in waveset or linked decision. Missing
        rationale → FAIL `PROC-PASS-NO-PROOF`.
- [ ] 4. Confirm `chrome_freeze` lists non-proof-serving surfaces to freeze
        and names the proof-serving allowlist. Absolute freeze with no
        allowlist is invalid (blocks proof delivery).
- [ ] 5. Confirm waveset / ACCEPT packet names the harness:
        `python3 evals/check_proof_before_accept.py`, plus DOM/host hard
        gate `python3 skills/charter/scripts/proof_host_probe.py` for
        product ACCEPT.
- [ ] 6. When fixtures are in scope, run
        `python3 evals/check_proof_before_accept.py`. Require PASS. Capture
        under `gate-captures/`. Mechanical FAIL ids only:
        `PROC-PASS-NO-PROOF`, `PROC-NO-VISUAL`.
- [ ] 7. For product/visitor ACCEPT with `proof_required: yes`, run
        `python3 skills/charter/scripts/proof_host_probe.py` on the proof
        surface (`--url` / `--selector`, or documented equivalent). height
        ≤ 0 or blank canvas → FAIL `PROC-BLANK-CANVAS`. Do not ACCEPT on
        docs alone. Do not hand-author the host JSON.
- [ ] 8. If `visual_accept: yes`, capture-then-grade is required (frozen
        captures + independent product-look review against
        `proof_reference`). DOM/host green ≠ done. Screenshot miss alone is
        not the blank-canvas hard gate; DOM/host metrics still required.
- [ ] 9. Adversarial / ACCEPT evaluators use
        `model: cursor-grok-4.5-high-fast`. Emit fail ids from the closed
        vocab. Label each id mechanical vs review/live. Review-only ids
        (`PROC-CHROME-THRASH`, `PROC-DEBT-AS-DONE`) need live or review
        evidence, not fixture-script green alone.
- [ ] 10. Report: proof_required value, field completeness, harness
        verdict, fail ids, capture paths. Never docs-only ACCEPT when
        `proof_required: yes`.
```

Lane types this playbook covers:

| type | operator says |
|:-----|:--------------|
| visitor / product execution | `proof_required: yes`; harness before ACCEPT |
| mod-check / research / plugin-meta / copy-only | `proof_required: no` or `n/a` + rationale |
| opt-out with rationale | `proof_reference: none` or `visual_accept: no` only with written why |

## WIRING (INT only — do not edit SKILL.md in W2a)

Add router row + playbook list entry in `skills/wavves/SKILL.md` during INT:
playbook `proof-before-accept` → `playbooks/proof-before-accept.md`; leaf =
dispatch STEPS; no `/proof-gate` slash skill in v0.
