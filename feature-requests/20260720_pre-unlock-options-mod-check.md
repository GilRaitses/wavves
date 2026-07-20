# FR-20260720 — Pre-unlock options mod-check (AUTH-11)

- **Status:** draft → ready-for-mod-check
- **Date:** 2026-07-20 (America/New_York)
- **Product surface:** wavves skills / charter / mod-check / proceed playbook /
  registry schema
- **Source evidence (pax):**
  - `wavves/lanes/20260720_rl-win-track/` (RLW) — W1 reconcile recommended bare
    `unlock W2`; W2 is options-only
  - `wavves/lanes/20260720_rlw-charter-mod-check/` (RWC) — mod-check **REVISE**;
    blockers B1–B5 closed only after check; then W2 options unlock safe
  - `findings/RWC-verdict.md` (AUTH-04 REVISE; `blocks_w2: true`)
  - `decisions/RLW-W2-OPTIONS-UNLOCK.md` (options-memo only after REVISE apply)
  - `gate-captures/RLW-W2.json` (W2 PASS_WITH_GAPS; DECIDE/BUILD still false)
- **evidence_verified_against:** pax `07c00007f` tip at FR authoring
  (W2 pause + mistaken pax `skills/proposed/` filing removed in same cleanup)
- **Originating mod feedback:** O0.R3 after operator affirmed RWC check was
  worth it for unlock hygiene; asked FR in wavves build (not pax proposed)

## Problem

Charters with a **gated options memo** (unlock-before-DECIDE ranking wave) can
recommend `unlock W2` from discovery reconcile while the charter surface is
stale or incomplete:

1. waveset still says prior wave **IN FLIGHT** after reconcile complete
2. soft “primary” seed vs lock “neither pre-selected”
3. missing options-wave ACs / non-goals / rollback / stop rules
4. undefined honesty terms (e.g. distill-ablated) + harness defaults that
   re-enter forbidden paths
5. bare `unlock W2` false green under `PASS_WITH_GAPS`

Today **AUTH-05** only gates W2+ after **mod-decide** when waveset is older
than newest decisions. It does **not** auto-invoke `/mod-check` when O0 is
about to unlock an options/memo wave after discovery reconcile. RLW needed a
manual `/mod-check` (RWC); that check was load-bearing for a safe unlock.

**Fail id (proposed):** `PROC-UNLOCK-NO-CHECK` — options-wave unlock proceeds
from reconcile recommend without mod-check GO or REVISE-applied synced to
current waveset.

## Feature sketch (AUTH-11)

| id | target | change |
|---|---|---|
| AUTH-11a | `charter` | If any wave is `options-only` / options memo / unlock-before-DECIDE, set `pre_unlock_mod_check: required` in waveset + registry |
| AUTH-11b | `charter` reconcile | When recommending unlock of such a wave, emit `recommended_actions` that include `/mod-check` first; do not treat unlock as next dispatch until GO or REVISE-applied |
| AUTH-11c | `mod-check` | Default artifact bundle for this trigger: `waveset.md` + `LOCKED-DECISIONS.md` + latest `*-RECONCILE.md` (+ gate JSON). Verdict must set `blocks_<options_wave>` for unlock safety |
| AUTH-11d | `proceed` | If source recommends unlock-options and no sibling check lane is `verdict-go` / `verdict-revise-applied` against current waveset mtime, **route to check first** |
| AUTH-11e | registry | Optional: `pre_unlock_mod_check: required\|waived`, `pre_unlock_check_lane`, `options_wave_id` |

### Implicit need heuristic (charter write)

A wave **implicitly needs** pre-unlock mod-check when ≥2 of:

1. Marked GATED and described as options / ranking / memo (not BUILD)
2. Prior wave is discovery with `PASS_WITH_GAPS` allowed
3. Success depends on honesty locks (claim HOLD, distill-not-authority, ledger)
4. Unlock language appears in reconcile (`recommended_next_for_O0: unlock …`)

Waive only with explicit operator `pre_unlock_mod_check: waived` + one-line
reason in LOCKED.

### Playbook sketch

**`playbooks/proceed.md`** — after locating recommended_actions:

```text
If actions include unlock of an options-only / gated memo wave
and pre_unlock_mod_check is required (or heuristic matches) and no current
check lane shows verdict-go or verdict-revise-applied synced to waveset:
  route to check playbook first; do not dispatch the options wave this turn.
```

Also: `charter-lane.md` / `charter/SKILL.md` default flag; `mod-check` “When
to use”; `examples/usage.md` path reconcile → check → unlock options.

## Where it lands

| option | meaning | lean |
|---|---|---|
| A | Extend AUTH-05 only | weak (wrong trigger: mod-decide vs options unlock) |
| B | New AUTH-11 on charter + proceed + mod-check | **required** |
| C | Registry fields only | insufficient alone |
| D | Evals: unlock-options without check → FAIL PROC-UNLOCK-NO-CHECK | strong |

## Risks

- Extra latency on every options unlock (waive trivial mechanical memos)
- False positive: every GATED W2 treated as options (require options/memo
  language or explicit flag)
- Double-check after REVISE apply (`verdict-revise-applied` + synced waveset
  clears; re-check only on waveset drift)

## Operator decision

Accept / revise / reject, then `/mod-check` this FR before BUILD charter.
Do not install into live plugin from this file alone.
