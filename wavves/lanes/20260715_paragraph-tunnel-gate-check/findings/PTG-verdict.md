# PTG-verdict

```yaml
verdict: REVISE
blocks_w2: false
blocks_w3: false
blocks_w4: false
blocks_w5: false
blockers:
  - id: G-LANDING
    wave: w2
    evidence_path: findings/PTG-completeness.md
    summary: A|B|C landing unlocked; B phase-leaks; BUILD needs pick
  - id: G-INVOKE
    wave: w2
    evidence_path: findings/PTG-completeness.md
    summary: Who/when/field-path for tunnel unset
  - id: G-MODEL
    wave: w2
    evidence_path: findings/PTG-completeness.md
    summary: Adversarial + rewrite model tier unset
  - id: G-EVAL / FM-1
    wave: w2
    evidence_path: findings/PTG-adversarial.md
    summary: Acceptance sketch is not a runnable gate
  - id: G-FAIL-CAP / FM-rewrite
    wave: w2
    evidence_path: findings/PTG-adversarial.md
    summary: Loop cap 1 with no post-cap escalate; self-graded rewrite
  - id: FM-VOCAB
    wave: w2
    evidence_path: findings/PTG-adversarial.md
    summary: Closed vocab misses stand-in / research-meta / false-fact; PN-FIXTURE untested
  - id: G1-HASH
    wave: w2
    evidence_path: findings/PTG-grounding.md
    summary: FR mislabels landing commit as repo_state_verified_against
  - id: C1-B
    wave: w2
    evidence_path: findings/PTG-contradictions.md
    summary: Option B collapses mid-render tunnel into mod-check
```

## Lens rolls

| lens | lean | agent |
|---|---|---|
| grounding | REVISE | [PTG-W1a](20695a7e-f5e3-4510-8b39-40d4ebc6e2f6) |
| contradictions | REVISE | [PTG-W1b](c13bb294-110c-444c-b8dc-d624dca2fcdf) |
| completeness | REVISE | [PTG-W1c](2f19221b-9b9e-482d-9d90-3ffa86231324) |
| adversarial | REVISE | [PTG-W1d](5da83e88-94d6-494a-a85a-4e4c24510fd8) |

**Model lock:** all lenses `cursor-grok-4.5-high-fast`.

## Lane verdict: REVISE

Salvageable. Route to `/mod-decide` before any BUILD charter. Not BLOCK:
problem, live APPL evidence, and non-goals ground. Not GO: landing, invoker,
model, runnable eval, fail-after-cap, vocab gaps, and B phase leak.

## Recommended actions (AUTH-10)

1. `/mod-decide` on open calls below (operator `¯\_(ツ)_/¯` → apply recommended picks).
2. Patch FR hygiene (hash fields, PN↔P2 map, strike B) before `/charter`.
3. Do not charter BUILD until Locked decisions land in waveset + registry.
4. Subagent model for this product family remains Grok only.

## Open calls for mod-decide (ordered)

1. **PTG-LAND** — A / B / C / A+C (recommend: **C + dispatch STEPS hook**; strike B; defer slash-skill A)
2. **PTG-INVOKE** — who/when/field (recommend: runner; after render; before prose_lint; field named in waveset)
3. **PTG-MODEL** — tiers (recommend: **Grok** both gates)
4. **PTG-EVAL** — fixture home + runnable pass metric
5. **PTG-FAIL-CAP** — post-cap path (recommend: escalate operator REVISE)
6. **PTG-VOCAB** — extend + alias map
7. **PTG-JUDGE** — separate re-adversarial capture + freeze check
8. **PTG-HASH** — FR evidence vs landing fields
