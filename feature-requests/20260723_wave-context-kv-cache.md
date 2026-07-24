# FR-20260723 — Wave/context KV cache (durable resume state)

- **Status:** ready-for-mod-check
- **Date:** 2026-07-23 (America/New_York)
- **Product surface:** charter leave-acts / checkpoint; proceed standing remasure;
  mod-rotate hydration; optional thin playbook; evals
- **Inspiration (analogy only):** [KV Caching Explained (Hugging Face)](https://huggingface.co/blog/not-lain/kv-caching) —
  cache past K/V so each new step computes a new Q against history instead of
  recomputing the full past. **Not** ML weights, **not** RotatE KG embedding.
- **Wired FRs only:** WOF resume/checkpoint, PAS stale-queue, mod-rotate /
  rotation hydration. **Out of scope:** PUO, IPB, MDA, voice.

## Problem

Three open/standing surfaces recompute or invent “past context” instead of
resuming from a durable cache:

1. **WOF** — wave orch yields or exits without
   `findings/<wave>-orch-checkpoint.md` → `PROC-ORCH-NO-RESUME-CONTRACT` /
   launch-and-exit; O0 re-prompts from chat memory.
2. **PAS** — proceed-all-standing moves from a standing file without remasure
   → `PROC-PROCEED-STALE-QUEUE`; or invents inventory from chat →
   `PROC-PROCEED-CHAT-INVENTORY`.
3. **mod-rotate** — successor is told to hydrate from rotation files while
   `wavves/rotations/` can be empty and INDEX `current_rotation: none`
   (RTH-W1e R2). Continuity prose without a written cache.

KV-cache analogy (locked sentence): **the durable artifact is the K/V;
the new notify / proceed / hydrate step is the Q; replaying the transcript
is standard inference without cache.**

## Non-goals

- Does not replace AUTH-11 (PUO), IP-before-cutover (IPB), or decide-align (MDA).
- Does not install a neural cache or change model `use_cache`.
- Does not claim isomorphism to transformer KV tensors.
- Does not auto-BUILD WOF/PAS; this FR is the shared seam + evals + skill text.

## Feature sketch (CTX-KV)

| id | target | change |
|---|---|---|
| KV-01 | charter / WOF land | Mandate checkpoint schema for `yield_awaiting_children`: charge table, pending worker ids, next integrate step, tip hash. Resume = load checkpoint + apply notify (new Q). Missing checkpoint on yield → FAIL id already in WOF. |
| KV-02 | proceed / PAS | Standing file is the program cache. Remasure = invalidate+rewrite before move. Stale file without remasure → `PROC-PROCEED-STALE-QUEUE`. Document as cache invalidation, not chat search. |
| KV-03 | mod-rotate / init | First-rotation / bootstrap fence: if `rotations/` empty, rotation skill writes r01 from template (not chat memory). INDEX `current_rotation` + `current_identity` must match newest rotation or explicit bootstrap. |
| KV-04 | vocabulary | Product text may say **context cache** / **KV-cache analogy**; must say **analogy**; ban “we implement transformer KV cache.” |
| KV-05 | evals | `evals/check_wave_context_kv_cache.py` + fixtures: yield-without-checkpoint FAIL; resume-with-checkpoint PASS; standing stale FAIL; empty rotations + hydrate-claim FAIL; RotatE/isomorphism phrasing FAIL. |
| KV-06 | docs | One paragraph in README tracking or charter EXECUTION_WIRING pointing at checkpoint + standing + rotations as the three cache homes. |

## Fail ids (closed for BUILD)

| id | fail condition |
|---|---|
| `PROC-KV-YIELD-NO-CACHE` | orch yield/leave without checkpoint artifact (alias/bind to WOF `PROC-ORCH-NO-RESUME-CONTRACT`) |
| `PROC-KV-RESUME-NO-CACHE` | resume integrate without readable checkpoint or rollup |
| `PROC-KV-STANDING-STALE` | all-standing move without remasure against live registry/dispatch (bind PAS stale) |
| `PROC-KV-ROTATION-EMPTY-CLAIM` | hydrate/continuity claim while `current_rotation: none` and `rotations/` empty |
| `PROC-KV-ISOMORPHISM-CLAIM` | product text claims transformer KV or Raft isomorphism for this seam |

## Acceptance (sketch)

1. Checkpoint schema named and checked in eval fixture.
2. Standing remasure rule named as invalidation; fixture covers stale FAIL.
3. Bootstrap/first-rotation fence named; empty-rotations claim FAIL fixture.
4. Analogy label required in any visitor sentence that names “KV cache.”
5. PUO/IPB/MDA untouched.

## Open calls (for `/mod-decide`)

1. **CACHE-NAME** — product term: `context cache` vs `KV cache (analogy)` vs
   checkpoint-only (no KV in visitor copy).
2. **WOF-BIND** — land as part of WOF BUILD vs separate CTX-KV BUILD after WOF.
3. **ROTATION-TEMPLATE** — ship template file under `wavves/rotations/_template.md`
   vs only skill prose for first write.

## Next

`/mod-check` → `/mod-decide` open calls → `/charter` BUILD (after WOF/PAS
land status remasured). No BUILD from this folder alone.
