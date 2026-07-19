# PBB-W1a — playbook-shape

```yaml
lens: playbook-shape
wave: PBB-W1a
repo_state_verified_against: 517dd85190cf93cf744434338dec4b1eb1d859c5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Verdict (this lens)

Shape for `skills/wavves/playbooks/proof-before-accept.md` is fixed by
paragraph-tunnel playbook + PBA locks. Route is **dispatch STEPS** (no
`/proof-gate` slash skill). Leaf stays under wavves playbooks; router row
is INT-only.

## Required playbook sections

1. **Route line** — dispatch STEPS; no `/proof-gate` in v0 (PBA-LAND defer A).
2. **Model lock** — any adversarial/ACCEPT evaluator subagents use
   `model: cursor-grok-4.5-high-fast`.
3. **Classifier** — waveset `proof_required: yes|no|n/a` (PBA-CLASSIFIER).
   Defaults guidance: visitor/product execution → `yes`; mod-check /
   research-discovery / plugin-meta / outbound-copy-only → `no` or `n/a`
   with one-line rationale.
4. **Mandatory fields when `proof_required: yes`:**
   - `proof_job` (one sentence, operator-facing)
   - `proof_reference` (path/URL/figure class, or `none` + rationale)
   - `chrome_freeze` (non-proof-serving path/surface list + proof-serving
     allowlist) (PBA-FREEZE)
   - `visual_accept` (`yes`/`no`; `no` requires rationale) (PBA-OPTOUT)
5. **Closed fail vocab** with mechanical vs review-only labels:
   - mechanical (fixture checker): `PROC-PASS-NO-PROOF`, `PROC-NO-VISUAL`,
     opt-out missing-rationale as `PROC-PASS-NO-PROOF` or companion
     detection under those ids
   - review / live harness: `PROC-CHROME-THRASH`, `PROC-DEBT-AS-DONE`,
     `PROC-BLANK-CANVAS` (DOM/host live; not sole BUILD ACCEPT on review ids)
6. **STEPS checklist** (tunnel order analogue):
   - confirm `proof_required` set
   - if `yes`, confirm four fields + rationale rules
   - confirm named harness command in waveset/ACCEPT
   - run `python3 evals/check_proof_before_accept.py` when fixtures in scope
   - run DOM/host harness for product ACCEPT (height ≤ 0 / blank-canvas FAIL)
   - screenshot-vs-reference optional when `visual_accept: yes`
   - report verdict + capture paths; never docs-only ACCEPT
7. **WIRING note (INT only)** — router row in `skills/wavves/SKILL.md`;
   do not edit SKILL.md in W2.

## Shape reference

`skills/wavves/playbooks/paragraph-tunnel.md`: numbered STEPS, closed vocab,
model lock, lane-type table, INT wiring deferral.

## W2a ownership

`skills/wavves/playbooks/proof-before-accept.md` (NEW).

## Commit file list

- `wavves/lanes/20260718_proof-before-accept-build/findings/PBB-playbook-shape.md`

No git. Escalation to O0 only.
