# FR-20260722 — mod-decide decision-alignment interpretability

- **Status:** ready-for-mod-check
- **Date:** 2026-07-22 (America/New_York)
- **Product surface:** `mod-decide` skill + decide playbook + examples/usage
- **Source evidence (pax IWD admit round):**
  - `wavves/lanes/20260722_island-wide-discovery/findings/IWD-W2R-TRAIN-WIRE.md`
  - `decisions/IWD-D5-island-admit-posture.md` (pick D — full admit)
  - `decisions/IWD-D6-first-build-scope.md` (pick B — coverage BUILD first)
  - Operator feedback: hygiene leans (A/B hold) recreated indefinite-hold
    loops; operator wanted successor-system BUILD (island coverage supersedes
    Midtown N) but options/leans did not surface **named exits** or
    **program-alignment** until challenged
- **evidence_verified_against:** pax `2c04e8b273f6e949a0774d514a97de81f40b3105`
  (TRAIN-WIRE land; admit locks authored same session)
- **Originating mod feedback:** O0.R3 — bake decision-clarity into mod-decide;
  reject indefinite hold recommends without exit criteria; align options to
  standing program intent (successor coverage vs fixture micro-rail)

## Problem

`/mod-decide` today presents A/B/C/D with an optional lean, then waits.
That is necessary but **not sufficient** when the open call is a
**program gate** (admit vs hold, coverage BUILD vs fixtures-rail):

1. **Indefinite-hold bias** — hygiene-safe leans default to Hold / Eval-only
   without stating how the hold is *exited*, so O0/operator loops:
   decide → hold → more hygiene → decide → hold.
2. **Misaligned option grain** — options that look like product forks
   (admit train vs hold) can hide the real program fork (island coverage
   BUILD that supersedes Midtown N vs Path-3 fixture bookkeeping).
3. **Lean without alignment check** — lean can contradict standing charter
   intent (“island-wide successor”) while still looking “safe.”
4. **No interpretability contract** — operator cannot see, in one block:
   what each pick unlocks next, what it permanently blocks, and which
   prior lock / intent it serves.

**Fail id (proposed):** `PROC-DECIDE-HOLD-NO-EXIT` — mod-decide recommends
or leans Hold / ban without named exit criteria and without a
program-alignment line tying options to standing intent.

**Fail id (proposed):** `PROC-DECIDE-GRAIN-MISMATCH` — option set is
fixture/N bookkeeping while standing intent is successor-system BUILD
(or the reverse), with no explicit grain callout.

## Feature sketch (DECIDE-ALIGN)

| id | target | change |
|---|---|---|
| DA-01 | `mod-decide` | For each call, require an **Exit / unlock** line per option that is a hold, ban, or pause (what concrete artifact or wave lifts it). Ban leans that are hold-with-no-exit. |
| DA-02 | `mod-decide` | Require a **Program alignment** stanza before the first call: 2–4 bullets of standing intent from waveset/charter/prior locks (verbatim cites). Each option must tag `aligns` / `defers` / `conflicts` against that intent. |
| DA-03 | `mod-decide` | When the call is admit/hold/build-scope, force a **grain check**: is this fixtures-rail, coverage BUILD, or claim-surface? If operator intent (from charter or prior message) names successor coverage, default option set must include that BUILD path as a first-class pick — not only hold/eval/train N. |
| DA-04 | `mod-decide` | Lean rules: prefer options that `aligns` with standing intent when hygiene exits already exist (freeze wire, check PASS). Hygiene lean to hold is allowed only with exit criteria **and** explicit “defers standing intent.” |
| DA-05 | `mod-decide` draft | Locked-decisions draft gains `program_intent` + per-pick `unlocks_next` fields. |
| DA-06 | `decide` playbook / `examples/usage.md` | Document anti-loop: after check/wire PASS, admit/build-scope decide must not re-open hygiene; route hold-only picks through DA-01. |
| DA-07 | evals | Fixture: post-wire admit decide that leans Hold with no exit → FAIL `PROC-DECIDE-HOLD-NO-EXIT`. Fixture: options omit coverage BUILD while waveset intent says supersede Midtown N → FAIL `PROC-DECIDE-GRAIN-MISMATCH`. |

### Per-option template (required)

```text
- <LETTER>: <one-line pick>
  unlocks_next: <wave/charter/artifact or "none — permanent park">
  exit_criteria: <if hold/ban: named condition; else "n/a">
  program_tag: aligns | defers | conflicts
```

### Lean template (required when lean present)

```text
Lean: <LETTER> because <aligns with intent X>; hygiene Y already closed
      via <path>. Hold alternatives defer intent until <exit>.
```

## Where it lands

| option | meaning | lean |
|---|---|---|
| A | Docs-only note in examples | weak |
| B | Patch `mod-decide/SKILL.md` + decide playbook + evals | **required** |
| C | Registry flags only | insufficient |
| D | Also add operator-facing “alignment card” in Locked paste | strong companion to B |

## Risks

- Longer decide turns (mitigate: templates; still one call at a time)
- Over-fitting to IWD vocabulary (keep grain labels generic:
  fixtures-rail / coverage-build / claim-surface / park)
- Operator may still pick hold — allowed if exit_criteria named

## Operator decision

Accept / revise / reject, then `/mod-check` this FR before BUILD charter into
the wavves plugin. Do not ship skill text from this file alone.
