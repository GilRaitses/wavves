# FR-20260723 — Wave orchestrator fan-out (no solo BUILD / no early exit)

- **Status:** ready-for-mod-check
- **Date:** 2026-07-23 (America/New_York)
- **Product surface:** `/wavves` skill + README roles + charter/dispatch
  templates + `AGENTS.md` Roles; optional playbook note under proceed/charter
- **Source evidence (pax IWD, O0.R3, same night as ridership/busy bind):**
  - Operator: wave subagents must be **orchestrators that deploy sub-agents**,
    not solo builders that serialize charge a+b+c+d
  - Operator: deploy **background only** — never hold the operator session
    window on long BUILD
  - Observed fail: O0 dispatched one `generalPurpose` “runner” that did the
    whole wave inline (slow, non-distributed)
  - Observed fail: wave “orchestrator” returned PASS-ish after only
    background-launching **W29a**, exiting before b‖c → d — **stalls the wave**
    unless O0 manually resumes
  - Lane-local bind (not portable): pax
    `wavves/lanes/20260722_island-wide-discovery/OPERATOR_ORCHESTRATION.md`
    + `dispatch-w29.md` `role: wave_orchestrator`
- **evidence_verified_against:** pax `20782d2d7` (OPERATOR_ORCHESTRATION
  background bind); IWD-W29 orchestrator early return after W29a launch
- **Originating mod feedback:** O0.R3 — plugin/home text is half-clear on
  O0→background and **uncleared** on orchestrator→parallel charge workers
  and “do not return until critical path completes”

## Problem

wavves already says:

- O0 dispatches **background** work and must not poll
- Dispatches often label the paste target “orchestrator”
- `AGENTS.md` mentions “Wave subagents: one bounded disjoint task each”

That is **not enough**. Agents still:

1. Treat the wave orchestrator as a **solo builder** for all charge rows
2. Or launch one child and **return immediately**, abandoning the critical path
3. Foreground-block the operator session on long work

Older etiquette (“orchestrator owns completion; no empty mid-dispatch return”)
conflicts with “background + integrate on notify” unless the skill states
both: **workers background**, **orchestrator stays responsible until rollup**.

**Fail id (proposed):** `PROC-ORCH-SOLO-BUILD` — wave agent executes multiple
charge ids itself instead of deploying one background worker per charge
(where independent).

**Fail id (proposed):** `PROC-ORCH-EARLY-EXIT` — wave orchestrator returns to
O0 after launching the first background child, before dependent charges and
rollup are done (wave stalls).

**Fail id (proposed):** `PROC-ORCH-FOREGROUND-HOLD` — O0 or wave orchestrator
runs long BUILD in the foreground / holds the operator session window.

## Feature sketch (ORCH-FANOUT)

| id | target | change |
|---|---|---|
| OF-01 | `skills/wavves/SKILL.md` + README Roles | Define three roles without collapse: **O0** (charter, background-dispatch wave orchestrator, reconcile, git) → **wave orchestrator** (read charge table; deploy workers; integrate; rollup) → **charge worker** (one charge id). |
| OF-02 | Fan-out rule | Each charge id in the dispatch table → its own background Task/worker when independent. Sequence only real deps (e.g. artifact before default URL). Forbidden: one agent serializes a+b+c+d. |
| OF-03 | Background rule | All wave orchestrator and charge-worker Task launches use background / non-blocking. Never hold the operator session on densify/bind/long BUILD. |
| OF-04 | Completion rule | Wave orchestrator **must not return** to O0 until rollup+gate (or hard FAIL). Launching child ≠ wave complete. Integrate on completion notifications; no busy-poll. |
| OF-05 | Dispatch template | Default “You are” block: `role: wave_orchestrator`; “Do not execute charges yourself”; critical-path example `a → (b‖c) → d`. |
| OF-06 | `AGENTS.md` (plugin home template) | Promote OF-01…04 into Roles; keep portable across repos. |
| OF-07 | Eval | Fixture: fake 3-charge dispatch → assert ≥2 parallel workers after first PASS; assert no early orchestrator return; assert no solo multi-charge BUILD. |

## Acceptance

- [ ] README + SKILL name O0 / wave orchestrator / charge worker and the three fail ids
- [ ] Dispatch paste template includes fan-out + background + no-early-exit
- [ ] Home `AGENTS.md` Roles updated in wavves-init template (and pax home synced when shipped)
- [ ] Eval/fixture for `PROC-ORCH-EARLY-EXIT` and `PROC-ORCH-SOLO-BUILD`
- [ ] `/mod-check` GO (or REVISE applied) before BUILD charter of the skill change
- [ ] Resolve wording conflict with “no empty mid-dispatch return” without reintroducing foreground holds

## Non-goals

- Changing git rules (runners still never git; O0 lands)
- Auto-polling / session-blocking waits
- Requiring max parallelism when charges truly share one write target
- Rewriting historical lane dispatches en masse (template + skill going forward)

## Evidence pointers

| item | path / note |
|---|---|
| Lane bind (interim) | pax `wavves/lanes/20260722_island-wide-discovery/OPERATOR_ORCHESTRATION.md` |
| W29 dispatch role | pax `.../dispatch-w29.md` (`role: wave_orchestrator`) |
| Early exit | W29 orchestrator returned after background-deploying W29a only |
| Prior related note | `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md` (empty mid-dispatch returns) |
