# KVC-VERDICT — wave-context-kv-cache check

```yaml
verdict: REVISE
blocks_w2: true
blocks_w3: false
blocks_w4: false
blocks_w5: false
blockers:
  - id: CX-KVC-01
    wave: w2
    evidence_path: findings/KVC-contradictions.md
    summary: Alias/bind PROC-KV-* vs WOF/PAS ids lacks emit precedence (dual FAIL / split-brain)
  - id: CX-KVC-02
    wave: w2
    evidence_path: findings/KVC-contradictions.md
    summary: CACHE-NAME checkpoint-only option conflicts with title + locked KV analogy sentence + KV-04
  - id: CX-KVC-03
    wave: w2
    evidence_path: findings/KVC-contradictions.md
    summary: WOF-BIND still offers "part of WOF BUILD" while WOF is SHIPPED
  - id: CX-KVC-06
    wave: w2
    evidence_path: findings/KVC-contradictions.md
    summary: KV-03 locks "from template" while ROTATION-TEMPLATE open; mod-rotate has no empty-dir path
  - id: GAP-KVC-G1
    wave: w2
    evidence_path: findings/KVC-grounding.md
    summary: WOF-BIND open call presupposes unlanded WOF BUILD
  - id: CMP-KVC-10
    wave: w2
    evidence_path: findings/KVC-completeness.md
    summary: KV-01 tip-hash additive vs WOF v0 resume schema (three fields only)
  - id: CMP-KVC-11
    wave: w2
    evidence_path: findings/KVC-completeness.md
    summary: Standing remasure/invalidation steps not imported from PAS
  - id: CMP-KVC-13
    wave: w2
    evidence_path: findings/KVC-completeness.md
    summary: KV-05 fixture dirs / cases under-enumerated for BUILD
  - id: FM-KVC-02
    wave: w2
    evidence_path: findings/KVC-adversarial.md
    summary: Chat-inventory not bound to a PROC-KV id (stale-only bind leaves invent loophole)
  - id: FM-KVC-03
    wave: w2
    evidence_path: findings/KVC-adversarial.md
    summary: Empty rotations + hydrate claim is live; first-write fence unlocked
repo_state_verified_against: de75b4c4118c78dcc0164fdaa916bbc53f99225f
reconciled_at: "2026-07-23T13:35:00-04:00"
lenses:
  - findings/KVC-grounding.md
  - findings/KVC-contradictions.md
  - findings/KVC-completeness.md
  - findings/KVC-adversarial.md
lens_leans: [REVISE, REVISE, REVISE, REVISE]
```

## Lane verdict

**REVISE.** All four lenses lean REVISE. Not BLOCK: wired WOF/PAS/rotate
seams remasure; non-goals and analogy bans are stated; Next already forbids
BUILD from this folder alone. Not GO: open calls and alias/schema gaps make
a faithful CTX-KV BUILD unsafe if chartered now.

`blocks_w2: true` means do not `/charter` CTX-KV BUILD until FR revise and/or
`/mod-decide` locks clear the blockers below.

## Lens rollup

| lens | file | lean | top ids |
|---|---|---|---|
| grounding | `KVC-grounding.md` | REVISE | GAP-KVC-G1, G2, G3 |
| contradictions | `KVC-contradictions.md` | REVISE | CX-KVC-01…10 (block BUILD: 01, 02, 03, 06) |
| completeness | `KVC-completeness.md` | REVISE | CMP-KVC-10…18 |
| adversarial | `KVC-adversarial.md` | REVISE | FM-KVC-01…09 |

## Required revise themes (before BUILD)

1. **WOF-BIND** — Drop "part of WOF BUILD." Choose separate CTX-KV BUILD
   (remeasure) and/or thin patch list on shipped WOF seams + evals/docs.
2. **Fail-id emit precedence** — Lock dual-bind vs rename-only vs WOF/PAS id
   canonical for `PROC-KV-YIELD-NO-CACHE`, `PROC-KV-STANDING-STALE`, and
   `PROC-KV-RESUME-NO-CACHE` overlap.
3. **CACHE-NAME** — Drop checkpoint-only visitor option, or rewrite title /
   locked sentence / KV-04 before decide.
4. **ROTATION-TEMPLATE** — Decide before locking KV-03 "from template";
   define empty-`rotations/` first-write + bootstrap exception vs INDEX.
5. **Checkpoint schema** — Tip hash: additive WOF patch (reopen/bind) or drop
   from KV-01; align Problem #1 with SHIPPED WOF resume contract.
6. **PAS bind honesty** — Standing remasure steps + chat-inventory coverage;
   do not call PAS-bound ids "closed for BUILD" until PAS land remasured.
7. **KV-05 / KV-06** — Enumerate fixture dirs; pick docs home; bind chat-inventory
   and analogy-missing FAIL cases.

## Non-blocking

- GAP-KVC-G3 INDEX open-FR omit (O0 inventory remasure).
- README WOF status lag vs SHIPPED body (NIT-1).
- RTH tip ≠ KVC tip (illustration only).

## Recommended actions (ordered)

1. FR revise applying themes 1–7 (or `/mod-decide` locks that close CACHE-NAME,
   WOF-BIND, ROTATION-TEMPLATE + emit precedence + tip-hash).
2. Remasure WOF (SHIPPED) and PAS (awaiting BUILD) land status before any
   CTX-KV BUILD charter.
3. Re-`/mod-check` only if revise is large; else `/mod-decide` → `/charter` BUILD.
4. No git from this orch. No skill edits. No BUILD from this lane alone.

## Leave-act

`return_to_O0` with this file. Checkpoint
`findings/KVC-W1-orch-checkpoint.md` satisfied (all four returns present).
