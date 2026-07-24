---
lens: completeness
wave_id: KVC-W1c
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
artifact: feature-requests/20260723_wave-context-kv-cache.md
verdict_lean: REVISE
model: cursor-grok-4.5-high-fast
---

# KVC-W1c — completeness lens

Read-only completeness pass on the context/KV-cache FR before decide/BUILD.
Compared sketch rows KV-01…06, fail ids, acceptance, open calls, and non-goals
against WOF resume/checkpoint, PAS standing/remasure, and mod-rotate +
wavves-init §4–5 bootstrap fences. Did not grade other lenses.

## Inventory

### Covered (enough for mod-check intake)

| id | item | note |
|---|---|---|
| CMP-KVC-01 | Three cache homes named | WOF checkpoint, PAS standing, rotations/INDEX |
| CMP-KVC-02 | Fail ids closed for BUILD table | five `PROC-KV-*` with WOF/PAS bind notes |
| CMP-KVC-03 | Non-goals present | no PUO/IPB/MDA; no neural/use_cache; no tensor isomorphism; no auto-BUILD WOF/PAS |
| CMP-KVC-04 | Open calls parked | CACHE-NAME, WOF-BIND, ROTATION-TEMPLATE for `/mod-decide` |
| CMP-KVC-05 | KV-05 harness path named | `evals/check_wave_context_kv_cache.py` |
| CMP-KVC-06 | KV-05 case themes named | yield-no-checkpoint FAIL; resume-with-checkpoint PASS; standing stale FAIL; empty-rotations hydrate-claim FAIL; isomorphism phrasing FAIL |
| CMP-KVC-07 | Next sequence | mod-check → mod-decide → charter BUILD after WOF/PAS remasure |

### Missing or under-specified (BUILD readiness gaps)

| id | gap | severity |
|---|---|---|
| CMP-KVC-10 | Checkpoint field list incomplete vs WOF + tip-hash orphan | high |
| CMP-KVC-11 | Standing invalidation steps not enumerated | high |
| CMP-KVC-12 | ROTATION-TEMPLATE open while KV-03 assumes “from template” | high |
| CMP-KVC-13 | KV-05 fixtures not directory-enumerated; several fail/PASS cases absent | high |
| CMP-KVC-14 | KV-06 docs target ambiguous | med |
| CMP-KVC-15 | Acceptance checklist thin vs fail table | med |
| CMP-KVC-16 | Rollback / partial-land non-goal coverage absent | med |
| CMP-KVC-17 | Optional thin playbook + skill patch owners unowned | med |
| CMP-KVC-18 | Silent tip-hash + INDEX match rules without AC/eval | med |

## Acceptance gaps

| AC sketch # | stated | gap | CMP id |
|---|---|---|---|
| 1 | Checkpoint schema named + eval fixture | Names four ideas (charge table, pending worker ids, next integrate step, tip hash). WOF resume lock has first three only; **tip hash not in WOF v0**. No required YAML/markdown field names, charge-table row shape, or “rollup substitutes for checkpoint” rule for `PROC-KV-RESUME-NO-CACHE`. | CMP-KVC-10, CMP-KVC-15 |
| 2 | Standing remasure = invalidation; stale FAIL fixture | Does not cite PAS path `wavves/standing/<YYYYMMDD>_<label>.md` or PS-02 row fields. No remasure checklist (registry/`active_dispatch`, dispatch/waveset, gate honesty, tip or clock stamp). No AC for rewrite-before-move as a distinct PASS fixture. | CMP-KVC-11 |
| 3 | Bootstrap/first-rotation fence; empty-rotations FAIL | KV-03 says skill “writes r01 from template” while open call ROTATION-TEMPLATE is unresolved (file vs skill prose only). mod-rotate today says follow newest rotations/ file; empty dir has no shape. wavves-init §4–5 bootstrap assigns O0.R1 in step-log but does not require a first rotation file; live INDEX has `current_rotation: none`. INDEX match rule in KV-03 has no AC row. | CMP-KVC-12, CMP-KVC-18 |
| 4 | Analogy label required in visitor “KV cache” sentences | No fixture named for missing-analogy FAIL (distinct from isomorphism FAIL). CACHE-NAME still open. | CMP-KVC-13, CMP-KVC-15 |
| 5 | PUO/IPB/MDA untouched | Covered as non-goal; no mechanical check stated (acceptable if BUILD file allowlist later). | CMP-KVC-03 |

**Fail ids without matching acceptance bullets:** `PROC-KV-RESUME-NO-CACHE` appears in the fail table but not in acceptance 1–5.

## Non-goals coverage check

| non-goal | covered in FR body | acceptance / eval / rollback | gap |
|---|---|---|---|
| No PUO / IPB / MDA | yes | AC #5 only; no file allowlist | light (decide/BUILD can lock) |
| No neural cache / `use_cache` | yes | none | CMP-KVC-16 |
| No transformer KV isomorphism claim | yes | KV-05 isomorphism FAIL + fail id | ok |
| No auto-BUILD WOF/PAS from this FR alone | yes (Next) | no rollback if CTX-KV lands before WOF/PAS | CMP-KVC-16; open WOF-BIND |

No rollback section: if WOF-BIND = separate CTX-KV BUILD after WOF, what happens on partial skill land or dual fail-id alias conflict is unowned.

## KV-05 fixtures: named vs missing

Harness path: `evals/check_wave_context_kv_cache.py` (file absent at tip; expected pre-BUILD).
WOF pattern to match: `evals/fixtures/wave-orch-fanout-*/` with `trace.json` + `expected.md`.

| case | in KV-05 prose | fixture dir / shape named | BUILD-ready? |
|---|---|---|---|
| yield without checkpoint → FAIL | yes | no | no — CMP-KVC-13 |
| resume with checkpoint → PASS | yes | no | no |
| standing stale without remasure → FAIL | yes | no | no |
| empty rotations + hydrate claim → FAIL | yes | no | no |
| RotatE / isomorphism phrasing → FAIL | yes | no | no |
| resume without checkpoint/rollup → `PROC-KV-RESUME-NO-CACHE` | fail table only | no | no — CMP-KVC-13 |
| standing remasure-then-move → PASS | no | no | no — CMP-KVC-11 |
| chat-invented standing inventory → FAIL | problem cites PAS chat-inventory; KV-05 omits | no | no |
| INDEX `current_rotation` mismatch vs newest file → FAIL | KV-03 implies | no | no — CMP-KVC-18 |
| visitor “KV cache” without analogy label → FAIL | AC #4 | no | no |
| tip hash absent/present on yield checkpoint | KV-01 adds tip hash | no | no — CMP-KVC-10 |
| bootstrap writes r01 (template or prose path) → PASS | KV-03 implies | no; blocked on ROTATION-TEMPLATE | no — CMP-KVC-12 |

## Unowned edges / silent assumptions

1. **Tip hash** added in KV-01 without WOF schema amend or decide call (CMP-KVC-10, CMP-KVC-18).
2. **Skill patch owners** for charter leave-acts, proceed remasure wording, mod-rotate empty-dir fence, wavves-init INDEX match: no KV row ownership matrix (CMP-KVC-17).
3. **Optional thin playbook** in product surface header; no sketch id (CMP-KVC-17).
4. **KV-06** “README tracking or charter EXECUTION_WIRING”: two homes, no choose-one; no AC checkbox (CMP-KVC-14).
5. **Alias/bind** of `PROC-KV-*` to WOF/PAS fail ids: dual emission vs rename-only not specified for harness (CMP-KVC-13).
6. **Standing path/schema** assumed from PAS but not restated or linked as import (CMP-KVC-11).

## Rotation template vs skill prose (open call)

Open call 3 (ROTATION-TEMPLATE) is not closed. KV-03 prose already picks “from template,” which prejudges decide. For BUILD readiness: either close ROTATION-TEMPLATE first, or rewrite KV-03 to “from locked template **or** locked skill-prose section shape” with one PASS fixture per chosen path. mod-rotate + wavves-init §4–5 alone do not close the empty-`rotations/` first-write fence.

## Docs (KV-06)

Target is vague: root README tracking table vs `skills/charter/EXECUTION_WIRING.md` (or both). “One paragraph” has no required nouns (checkpoint path, standing path, rotations/INDEX). No eval. CMP-KVC-14.

## Verdict lean

**REVISE** — seam and fail ids are good enough for mod-check, but BUILD readiness is incomplete: checkpoint fields (esp. tip hash), standing invalidation steps, rotation template decide vs KV-03, KV-05 fixture enumeration, KV-06 landing path, and several acceptance/fail mismatches.

Not **BLOCK**: non-goals and wired scope are present; open calls are correctly routed to `/mod-decide`; Next forbids BUILD from this folder alone.

## no-git statement

This charge worker ran no git commands. Tip `de75b4c4118c78dcc0164fdaa916bbc53f99225f` taken from waveset / dispatch only. No skill edits. No BUILD. No other-lens grading.
