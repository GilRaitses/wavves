# FR-20260723 — Proceed-all-standing (`queue all standing and move`)

- **Status:** ready-for-mod-check
- **Date:** 2026-07-23 (America/New_York)
- **Product surface:** `proceed` playbook + `/wavves` routing + optional leaf
  skill or proceed mode (`proceed-all` / standing queue)
- **Source evidence (pax IWD, same session as `/set-key` land):**
  - Operator: listed what still stands → then
    `¯\_(ツ)_/¯ and all the rest of those still standing`
  - O0 executed the open stack in one proceed pass:
    - charter+dispatch Google densify follow (`IWD-W27`)
    - ship `/set-key` skill + land standing rule
    - surface train-busy as **operator_gate** (IWD-V3; no invent)
    - TOP left as already-PASS non-gating (no fake work)
  - Standing alias already maps shrug → `/wavves proceed` for
    `recommended_actions` only (`playbooks/proceed.md`, pax
    `.cursor/rules/shrug-means-proceed.mdc`)
- **evidence_verified_against:** pax `4a7d6c91d` (W27 dispatch + set-key rule);
  wavves `fd12cb8` (set-key docs handoff); klosr key remasured set
- **Originating mod feedback:** O0.R3 — operator wants the “inventory everything
  still standing → move what can → gate what cannot” pass as a first-class
  wavves proceed mode, not an ad-hoc O0 improvisation

## Problem

Today `/wavves proceed` only executes an ordered **`recommended_actions`**
block from a single verdict / mod-decide / AUTH-10 reconcile. It does **not**
define how to proceed when the operator says:

- “all the rest of those still standing”
- “queue everything open and move”
- shrug **plus** an explicit all-standing scope

Without a product surface, O0 invents a standing list from chat memory. That
works once and fails on rotation: no durable queue, no shared schema for
`movable` vs `operator_gate` vs `already_done`, no rule that blocked locks
(e.g. IWD-V3 ridership) must surface instead of being “cleverly” skipped or
forced.

**Fail id (proposed):** `PROC-PROCEED-NO-STANDING-QUEUE` — proceed/all-standing
runs without a remasured standing inventory (registry + active_dispatch +
named gates + open FRs/handoffs) and without classifying each item as
dispatch / commit / operator_gate / skip(already complete).

**Fail id (proposed):** `PROC-PROCEED-FORCE-BLOCKED-LOCK` — all-standing pass
reopens or invents past a hard lock (example: train busy before newer
ridership) instead of emitting an operator_gate artifact.

## Feature sketch (PROCEED-STANDING)

| id | target | change |
|---|---|---|
| PS-01 | proceed playbook | Add mode **`proceed-all-standing`** (triggers below). Step 0: build a **Standing queue** from live surfaces, not chat memory. |
| PS-02 | Standing queue schema | Ordered list of `{id, source_path, class, action}` where `class` ∈ `dispatch` \| `commit_land` \| `operator_gate` \| `skip_done` \| `out_of_scope`. Persist under lane or home: `wavves/standing/<YYYYMMDD>_<label>.md` (or lane `standing.md`). |
| PS-03 | Inventory sources (mandatory remasure) | For the active program/lane set: `registry.yml` status + `active_dispatch`; lane `dispatch.md` / waveset open rows; named `*_OPERATOR_GATE.md` / lock ABSENT honesty; open product FRs/handoffs the operator just named; optional “what still stands” list if the operator pasted one this turn (verify each against disk). |
| PS-04 | Move rules | `dispatch` → background only; `commit_land` → only when shrug/proceed authorizes; `operator_gate` → write/surface gate, **do not** invent unlock; `skip_done` → one-line cite of PASS artifact; never invent work for non-gating research already PASS unless operator expands charter. |
| PS-05 | Trigger language | `all still standing`, `queue all standing and move`, `proceed all standing`, and shrug **when** followed by all-standing scope. Bare shrug alone remains AUTH-10 `recommended_actions` only (do not widen bare shrug). |
| PS-06 | Return card | Table: id \| class \| action taken \| land hash or gate path \| blocked reason. |

## Triggers (proposed)

| phrase | route |
|---|---|
| `¯\_(ツ)_/¯` alone | existing proceed (`recommended_actions`) |
| `¯\_(ツ)_/¯` + “all still standing” / “the rest” | **proceed-all-standing** |
| `/wavves proceed all standing` | **proceed-all-standing** |
| “queue all standing and move” | **proceed-all-standing** |

## Acceptance

- [ ] Playbook documents proceed-all-standing vs bare proceed (no widen of bare shrug)
- [ ] Standing queue is written to disk before moves
- [ ] Eval/fixture: blocked lock → operator_gate, not dispatch
- [ ] Eval/fixture: open dispatchable wave → background dispatch
- [ ] Eval/fixture: already PASS → skip_done with cite
- [ ] README / usage / index row when shipped
- [ ] `/mod-check` GO (or REVISE applied) before BUILD charter of the skill change

## Non-goals

- Auto-unlocking hard locks (ridership, API ToS, spend) without operator
- Polling background runners
- Replacing mod-decide / mod-check
- Cross-lane “do everything in the registry” without an operator-named scope
  (default scope = current conversation’s program / named lanes)

## Evidence pointers (this originating pass)

| standing item | class (as run) | artifact |
|---|---|---|
| Google densify (key set) | dispatch | `dispatch-w27.md` |
| `/set-key` FR → skill | commit_land (product) | wavves `17539cb` + docs handoff |
| Train busy / ridership | operator_gate | `findings/IWD-V3-TRAIN-BUSY-OPERATOR-GATE.md` |
| TOP 2-complex | skip_done | W25-TOP PASS; non-gating |

## Next

`/mod-check` this FR → `/mod-decide` any open calls (queue path, bare-shrug
non-widen, persistence path) → `/charter` BUILD into proceed playbook (+
optional thin leaf if slash-only surface wanted).
