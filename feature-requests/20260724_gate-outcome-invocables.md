# FR-20260724 — Gate-outcome invocables (`next` / `remedia` / `park` / `accept`)

- **Status:** draft → ready-for-mod-check
- **Date:** 2026-07-24 (America/New_York)
- **Product surface:** `skills/wavves/SKILL.md` router + new playbooks
  (`playbooks/next.md`, `playbooks/remedia.md`, `playbooks/park.md`,
  extend `playbooks/proceed.md` / ACCEPT unlock); thin Cursor command leaves
  optional (`/wavves-next`, `/wavves-remedia`, …) that route into wavves
- **Source evidence (same-day multi-mod session, America/New_York):**
  - DDX ACCEPT `PASS_WITH_GAPS` → operator asked fix Hook1 vs invent DDX2;
    O0 needed a durable “next vs remedia” fork instead of chat paste
  - DDX-R1 closed Hook1 smoke; leftover `real_pin_ckpt_hash_disk_mismatch`;
    operator again needed remedia-vs-phase-map without invent
  - BCA W2 `PASS_WITH_GAPS` (live G07 blocked on deploy) → proceed to W3
    vs remedia L08 — same fork
  - Yield park miss (orch `yield_awaiting_children`) already FR’d via
    docs-gap A–D; this FR is the **operator-facing** command surface after
    gate outcomes, not the yield pickup rule itself
- **evidence_verified_against:** pax DDX ACCEPT park + DDX-R1
  `PASS_WITH_GAPS` + BCA W2 land (remeasure live registry/gates at BUILD;
  originating hashes are illustration only)
- **Originating mod feedback:** after complete PASS or PASS_WITH_GAPS,
  operator should say one invocable — **next** (advance waveset) or
  **remedia** (thin loop on named gap) — instead of composing long pastes.
  Bare shrug stays AUTH-10 `recommended_actions` only (do not widen).

## Problem

wavves has `/wavves proceed` (AUTH-10 recommended_actions) and
proceed-all-standing, plus `/charter`, `/mod-decide`, `/mod-rotate`. It does
**not** define first-class operator moves for:

1. Gate **PASS** (or PASS_WITH_GAPS the operator accepts) → advance to the
   waveset’s `recommended_next` only
2. Gate **FAIL** or PASS_WITH_GAPS with a **named** residual the operator
   wants closed → thin remediation wave / remedia loop (respect remediation
   cap)
3. End-of-day / switch-mod **park** without invent
4. Explicit **ACCEPT unlock** when INT is done and O0 holds operator auth

Without these, each mod improvises pastes. That fails on rotation and
cross-mod days (BCA ‖ DDX).

### Fail ids (closed for BUILD)

| id | fail condition |
|---|---|
| `PROC-NEXT-CHAT-INVENT` | `/wavves next` invents a successor lane or wave not named in rollup/registry/waveset `recommended_next` |
| `PROC-NEXT-ON-FAIL` | `next` runs while latest GATE is FAIL without operator remedia/accept-residual |
| `PROC-REMEDIA-UNNAMED` | remedia charters without a named gap id from GATE/ADV/ACCEPT residuals |
| `PROC-REMEDIA-SCOPE-CREEP` | remedia rebuilds the parent wave or opens phase-map / new program |
| `PROC-REMEDIA-CAP-IGNORE` | remedia exceeds waveset remediation-loop cap without `operator_gate` |
| `PROC-PARK-ACTIVE-ORCH` | park leaves `active_dispatch` set / orphans orch without checkpoint note |
| `PROC-ACCEPT-AUTO` | ACCEPT chartered without explicit `/wavves accept` (or AUTH-10 action that names ACCEPT) |
| `PROC-ACCEPT-CLEAR-RESIDUAL` | ACCEPT clears a named PASS_WITH_GAPS residual without remasure proof |
| `PROC-SHRUG-AS-NEXT` | bare shrug widens to `next`/`remedia` (shrug = AUTH-10 recommended_actions only) |

## Feature sketch (GATE-OUTCOME)

| id | target | change |
|---|---|---|
| GO-01 | `skills/wavves/SKILL.md` | Router rows: `next`, `remedia` (aliases `remediate`, `remedial`), `park`, `accept`. Description: gate-outcome moves after PASS / PASS_WITH_GAPS / FAIL. |
| GO-02 | `playbooks/next.md` | Step 0: remasure latest `*-GATE.md` + `gate-captures/*.json` + `registry.yml` for the **named** lane (utterance or sole `active`/`recommended` lane). If FAIL → stop, suggest remedia. If PASS or PASS_WITH_GAPS: read `recommended_next` / waveset next gated wave; charter or dispatch **only** that. No invent. Emit return card. |
| GO-03 | `playbooks/remedia.md` | Require named gap (`gap:` / residual id from GATE). Charter thin `LANE-Rn` or waveset remedia slot; scope = gap only; remasure parent gate after; honor remedia cap → else `operator_gate`. Forbidden: new program lane, phase-map invent, clearing unrelated residuals. |
| GO-04 | `playbooks/park.md` | Set `active_dispatch: null` (registry + handoff stamp); refuse invent; optional `/mod-rotate` pointer; do not kill foreign-lane orch. |
| GO-05 | ACCEPT unlock | `/wavves accept` (or AUTH-10 row `accept`) charters ACCEPT with explicit residual/non-claim list copied from INT/prior ACCEPT gaps. Never implies residual cleared. |
| GO-06 | Yield interaction | Playbooks cite yield-pickup A–D (docs gap): `next`/`remedia`/`park` still remasure disk same turn on orch notify; they do not replace yield resume. |
| GO-07 | Evals | Fixtures: PASS→next dispatches W3 not invent; PASS_WITH_GAPS+named gap→remedia; FAIL+next→FAIL; bare shrug≠next; remedia without gap name→FAIL; accept without INT PASS→FAIL. |

## Triggers

| phrase | route |
|---|---|
| `/wavves next` · `next wave` · `advance after pass` | **next** |
| `/wavves remedia` · `remediate` · `remedial wave` · `close the named gap` | **remedia** (gap must be named or latest GATE residual sole) |
| `/wavves park` · `park this lane` | **park** |
| `/wavves accept` · `unlock ACCEPT` | **accept** |
| `¯\_(ツ)_/¯` / `/shrug` alone | AUTH-10 `recommended_actions` only (**not** next/remedia) |
| shrug + explicit `next` / `remedia` in same utterance | that playbook |

## Acceptance

- [ ] Router + four playbook surfaces (next/remedia/park/accept) landed
- [ ] Fail ids above have eval fixtures that FAIL closed
- [ ] Bare shrug cannot widen to next/remedia
- [ ] Remedia requires named gap; respects remedia cap
- [ ] Next never invents DDX2-style successor without waveset/registry row
- [ ] Docs mention yield-pickup A–D as complementary, not replaced
- [ ] README index row + status lifecycle

## Non-goals

- Replacing `/charter` or `/mod-decide`
- Auto-choosing remedia vs next without operator (except AUTH-10 when
  `recommended_actions` already names one)
- Implementing BCA W3 or DDX-R2 inside this FR
- Patent / product claim language

## Suggested charter shape (after mod-check GO)

Lane `GOI` (gate-outcome-invocables): W1 playbook drafts + eval fixtures;
W2 wire router; ACCEPT = eval green + docs.

## Operator one-liners (product promise)

```text
/wavves next          # after PASS (or accepted PASS_WITH_GAPS)
/wavves remedia <gap> # close named residual only
/wavves park          # stop invent; clear active_dispatch stamp
/wavves accept        # unlock ACCEPT with residuals listed
```
