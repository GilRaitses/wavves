# FR-20260723 — Proceed-all-standing (`queue all standing and move`)

- **Status:** revised-after-PAS (awaiting re-check or `/mod-decide`)
- **Date:** 2026-07-23 (America/New_York)
- **PAS check:** `wavves/lanes/20260723_proceed-all-standing-check/` —
  verdict **REVISE** (`findings/PAS-verdict.md`); this file applies that revise
- **Product surface:** `proceed` playbook + `skills/wavves/SKILL.md` routing +
  thin `/shrug` leaf (`skills/shrug/`)
- **Source evidence (originating session, same night as `/set-key` land):**
  - Operator: listed what still stands → then shrug + all-standing scope
  - O0 executed: dispatch densify follow; land `/set-key`; surface train-busy
    as **operator_gate** (no invent); leave already-PASS research as skip_done
  - Bare shrug already maps → `/wavves proceed` for `recommended_actions` only
    (`playbooks/proceed.md`)
- **evidence_verified_against:** wavves `/set-key` skill land `17539cb` +
  set-key docs handoff land `e437b9b` (`wavves/handoffs/20260723_set-key_docs_version_bump.md`);
  originating-session pins outside this repo are illustration only
- **Originating mod feedback:** make “inventory standing → move what can →
  gate what cannot” a first-class proceed mode, not ad-hoc O0 improvisation

## Problem

Today `/wavves proceed` only executes an ordered **`recommended_actions`**
block from a single verdict / mod-decide / AUTH-10 reconcile. It does **not**
define how to proceed when the operator says:

- “all still standing”
- “queue all standing and move”
- shrug or `/shrug` **plus** an explicit all-standing scope

Without a product surface, O0 invents a standing list from chat memory. That
works once and fails on rotation: no durable queue, no shared schema for
`movable` vs `operator_gate` vs `already_done`, no rule that blocked locks
must surface instead of being skipped or forced.

### Fail ids (closed for BUILD)

| id | fail condition |
|---|---|
| `PROC-PROCEED-NO-STANDING-QUEUE` | all-standing runs without a remasured, persisted standing inventory + class per item |
| `PROC-PROCEED-FORCE-BLOCKED-LOCK` | pass reopens/invents past a hard lock instead of an operator_gate artifact |
| `PROC-PROCEED-SHRUG-WIDEN` | bare shrug / bare `/shrug` (or fuzzy widen) executed as all-standing |
| `PROC-PROCEED-COMMIT-WITHOUT-AUTH` | `commit` land without this-turn authorize + `files:` list (AUTH-10) |
| `PROC-PROCEED-DISPATCH-STORM` | multiple background dispatches ignoring `active_dispatch` / `conflicts_with` / AUTH-05 |
| `PROC-PROCEED-CHAT-INVENTORY` | queue rows from chat/transcript without disk remasure of `source_path` |
| `PROC-PROCEED-STALE-QUEUE` | moves from a persisted standing file without remasure against live registry/dispatch/gates |
| `PROC-PROCEED-SILENT-SKIP-LOCK` | hard lock classified `skip_done` / `out_of_scope` with no gate artifact path |

## Feature sketch (PROCEED-STANDING)

| id | target | change |
|---|---|---|
| PS-01 | `playbooks/proceed.md` | Mode fork at top: **AUTH-10 proceed** vs **`proceed-all-standing`**. All-standing Step 0 builds Standing queue from disk; never from transcript search. |
| PS-02 | Standing queue schema + persist | Persist **only** at `wavves/standing/<YYYYMMDD>_<label>.md` (create dir if missing). One file per pass. Overwrite not append. Empty inventory → write empty queue + stop (no moves). Schema rows: `{id, source_path, class, proposed_action, result, land_hash, gate_path, blocked_reason}` where `class` ∈ `dispatch` \| `commit` \| `operator_gate` \| `skip_done` \| `out_of_scope`. `source_path` must exist on disk at inventory time. Order: operator-named lane/FR keys first (when present), then registry order inside scope. |
| PS-03 | Scope then remasure | **Scope formula (lock):** union of (a) lane codes / registry keys / explicit paths named in the triggering utterance, (b) else active lanes in `wavves/INDEX.md` for this repo only. **Forbidden:** registry-wide crawl of every lane without named scope; transcript search as inventory source. **Remasure inside scope only:** `wavves/registry.yml` status + `active_dispatch`; lane `dispatch*.md` / waveset open rows; named `*_OPERATOR_GATE.md` / lock ABSENT honesty; open FRs/handoffs **named in the trigger** (candidates only until `source_path` remasures). Operator paste list = candidates; unverified names → `operator_gate` (“unverified standing claim”), never `dispatch`/`commit`. |
| PS-04 | Move rules | Classify **full queue first**, then: `dispatch` → background only (honor `active_dispatch` / `conflicts_with` / AUTH-05; no storm); `commit` → AUTH-10 shape only (`files:` required; commit/push only when this turn authorizes proceed/ship for that land — all-standing alone is not blanket multi-land auth); `operator_gate` → write/surface gate artifact, **do not** invent unlock; `skip_done` → one-line cite of PASS artifact; `out_of_scope` → cite scope boundary, no dispatch/commit, include on return card as not-moved. Never invent work for non-gating already-PASS research unless operator expands charter. Open FR / docs handoff without executable class → `out_of_scope` or `operator_gate`, not premature BUILD. |
| PS-05 | Gate-continue semantics | After classify: execute **all** non-gate moves (`dispatch` / `commit` / `skip_done` / `out_of_scope` card lines), **then** surface every `operator_gate` together. Do not halt the whole pass at the first gate. Do not dispatch/commit after inventing past a gate. |
| PS-06 | Triggers (closed) | Widen to all-standing **only** on explicit phrases in the same utterance: `all still standing`, `queue all standing and move`, `proceed all standing`, `/wavves proceed all standing`, `/shrug` + one of those phrases, emoji shrug + one of those phrases. **Drop** bare “the rest” as a widen trigger. Bare `¯\_(ツ)_/¯` and bare `/shrug` → AUTH-10 `recommended_actions` only (`PROC-PROCEED-SHRUG-WIDEN` if widened). |
| PS-07 | `/shrug` leaf | Thin `skills/shrug/SKILL.md` (`disable-model-invocation: true`): discoverable alias for emoji shrug. Bare `/shrug` → AUTH-10 proceed. `/shrug` + all-standing phrase → proceed-all-standing. No wider body than proceed. |
| PS-08 | Router wiring | Patch `skills/wavves/SKILL.md`: proceed row + description mention all-standing mode; playbook list stays `proceed.md`; leaf table adds `/shrug`. |
| PS-09 | Return card | Emit from the standing file after the pass: id \| class \| result \| land_hash or gate_path \| blocked_reason. |
| PS-10 | Evals | `evals/check_proceed_all_standing.py` + fixtures under `evals/fixtures/proceed-all-standing-*/` covering: no queue file → FAIL; blocked lock → operator_gate not dispatch; open dispatchable → background dispatch; already PASS → skip_done with cite; bare shrug with leftover chat → AUTH-10 only; commit without `files:` → FAIL; stale standing file without remasure → FAIL. |

## Triggers

| phrase | route |
|---|---|
| `¯\_(ツ)_/¯` alone | AUTH-10 proceed (`recommended_actions`) |
| `/shrug` alone | same |
| shrug or `/shrug` + closed all-standing phrase | **proceed-all-standing** |
| `/wavves proceed all standing` | **proceed-all-standing** |
| `queue all standing and move` / `all still standing` | **proceed-all-standing** |

## Acceptance

- [ ] Playbook mode fork: AUTH-10 vs proceed-all-standing; bare shrug/`/shrug` non-widen
- [ ] Thin `/shrug` leaf ships
- [ ] `skills/wavves/SKILL.md` routing/description updated
- [ ] Standing queue at `wavves/standing/…` written before moves; schema + empty-queue rule
- [ ] `python3 evals/check_proceed_all_standing.py` PASS on fixtures above
- [ ] README / usage / index list `/shrug` and all-standing triggers
- [ ] Re-`/mod-check` GO or `/mod-decide` locks complete before BUILD charter

## Non-goals

- Auto-unlocking hard locks without operator
- Polling background runners
- Replacing mod-decide / mod-check
- Cross-lane “do everything in the registry” without operator-named scope
- Transcript search as an inventory source

## Open calls (for `/mod-decide` — residual only)

1. **COMMIT-AUTH-GRAIN** — does one all-standing authorize utterance cover every
   `commit` row with explicit `files:`, or does each land need its own
   `operator_gate` / “ship it” when multi-repo?
2. **SCOPE-FALLBACK** — when the trigger names no lanes and INDEX has zero
   active lanes: empty queue + stop (default lean) vs refuse mode with message

(Bare-shrug non-widen, standing path `wavves/standing/`, scope-then-remasure,
gate-continue, `/shrug` leaf, and SKILL wiring are **locked** above — not open.)

## Evidence pointers (originating pass; illustration)

| standing item | class (as run) | note |
|---|---|---|
| densify follow | dispatch | originating dispatch artifact |
| `/set-key` FR → skill | commit | wavves `17539cb` + handoff `e437b9b` |
| Train busy / ridership | operator_gate | originating gate finding |
| TOP research | skip_done | already PASS; non-gating |

## Next

`/mod-decide` residual open calls (or re-`/mod-check` if O0 wants a second
pass) → `/charter` BUILD into proceed playbook + `/shrug` leaf + evals.
No BUILD while PAS `blocks_w2` uncleared relative to this revise.
