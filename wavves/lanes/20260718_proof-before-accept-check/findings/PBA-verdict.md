# PBA-VERDICT — proof-before-accept check

```yaml
verdict: REVISE
blocks_w2: true
blocks_w3: true
blocks_w4: true
blocks_w5: true
date: 2026-07-18
repo_state_verified_against: af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
artifact: feature-requests/20260718_proof-before-accept.md
lenses:
  grounding: REVISE
  contradictions: REVISE
  completeness: REVISE
  adversarial: REVISE
blockers:
  - id: G1-paths
    wave: w2
    evidence_path: findings/PBA-grounding.md
    summary: Originating product repo evidence paths need root+foreign-pin; beta visitor lane uncited; height-0 stronger than measured captures
  - id: CX-unlock-combo
    wave: w2
    evidence_path: findings/PBA-contradictions.md
    summary: BUILD-unlock claim needs option E or drop unlock; product/UX classifier missing; chrome_freeze vs proof delivery conflict
  - id: B-schema-harness
    wave: w2
    evidence_path: findings/PBA-completeness.md
    summary: proof_* fields lack schema/pass metrics; visual gate not runnable; BUILD ACCEPT can green without Proof
  - id: FM-process-pass
    wave: w2
    evidence_path: findings/PBA-adversarial.md
    summary: Docs-only ACCEPT recreates process-PASS; PROC-* ids inoperable; opt-out defaults; DOM-marker happy path
```

## Lane verdict

**REVISE.** All four lenses agree. The fail mode is real and grounded in originating product repo
doctrine + visitor rebuild / product-look / beta visitor lanes. The FR is not BUILD-ready until product forks and
runnable gates are locked.

Not BLOCK: salvageable via FR edits + `/mod-decide` locks.

## Top blockers (merged)

1. **Lane classifier** — define visitor/product vs research/check/plugin-meta
   (or `proof_required: yes|no|n/a`) before mandatory fields apply.
2. **Land combo** — either require **E** with C+D+B for BUILD-unlock, or drop
   unlock and keep ACCEPT-only under C.
3. **Runnable proof** — name harness command + JSON schema + FAIL conditions
   (prefer DOM/host metrics; screenshot optional). No docs-only BUILD ACCEPT.
4. **Operable PROC-*** — mechanical detector/fixtures that emit closed fail
   ids (paragraph-tunnel shape).
5. **Evidence hygiene** — originating product repo paths with foreign pin; cite beta visitor lane; soften height-0
   to collapsed/zero-height class with cited captures.
6. **Field schema** — `proof_job` / `proof_reference` / `chrome_freeze` /
   `visual_accept` homes, validation, and ACCEPT pass metrics; close opt-out
   loopholes (`none` / `visual_accept: no` without rationale gates).

## Finding files

- `findings/PBA-grounding.md`
- `findings/PBA-contradictions.md`
- `findings/PBA-completeness.md`
- `findings/PBA-adversarial.md`

## recommended_actions

```yaml
recommended_actions:
  - action: operator_gate
    id: revise-fr
    summary: Edit FR-20260718 to close blockers above (or paste locks for mod-decide)
  - action: dispatch
    id: mod-decide
    summary: After FR revise (or with operator-pasted locks), /mod-decide then /charter BUILD
    depends_on: revise-fr
  - action: commit
    id: pba-check-artifacts
    summary: Commit PBA check lane + PTB ACCEPT artifacts when operator asks
    files:
      - wavves/lanes/20260718_proof-before-accept-check/
      - wavves/lanes/20260715_paragraph-tunnel-build/gate-captures/PTB-ACCEPT*
      - feature-requests/
      - skills/wavves/SKILL.md
      - wavves/INDEX.md
      - wavves/registry.yml
      - wavves/step-log.md
```
