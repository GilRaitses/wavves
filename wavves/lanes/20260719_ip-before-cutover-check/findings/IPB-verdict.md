# IPB-VERDICT — ip-before-cutover check

```yaml
verdict: REVISE
blocks_w2: true
blocks_w3: false
blocks_w4: false
blocks_w5: false
blockers:
  - id: soft-pass
    wave: w2
    evidence_path: findings/IPB-adversarial.md
    summary: Soft produce PASS / warn-only cutover can defeat IP-before-cutover
  - id: no-detector
    wave: w2
    evidence_path: findings/IPB-completeness.md
    summary: Acceptance lacks runnable detector / fixture homes
repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
reconciled_at: "2026-07-23T03:22:00-04:00"
```

## Lane verdict

**REVISE.** All four lenses agree. VIB-class failure is real; BUILD unsafe
until hard remasure-before-cutover and mechanical detectors are locked.

## Next

Revise FR and/or `/mod-decide` → no BUILD while `blocks_w2`.
