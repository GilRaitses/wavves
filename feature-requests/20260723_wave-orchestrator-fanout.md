# FR-20260723 — Wave orchestrator fan-out + moderator background etiquette

- **Status:** ready-for-mod-check
- **Date:** 2026-07-23 (America/New_York)
- **Product surface:** `/wavves` skill + README roles + charter/dispatch
  templates + `AGENTS.md` Roles; proceed/charter playbooks; O0 etiquette
- **Source evidence (pax IWD, O0.R3, same night as ridership/busy bind):**
  - Operator: wave subagents must be **orchestrators that deploy sub-agents**,
    not solo builders that serialize charge a+b+c+d
  - Operator: deploy **background only** — never hold the operator session
    window on long BUILD (applies to **moderator/O0** and wave orchestrators)
  - Observed fail: O0 dispatched one `generalPurpose` “runner” that did the
    whole wave inline (slow, non-distributed) and/or foreground-held the chat
  - Observed fail: wave “orchestrator” returned PASS-ish after only
    background-launching **W29a**, exiting before b‖c → d — **stalls the wave**
    unless O0 manually resumes
  - Lane-local bind (not portable): pax
    `wavves/lanes/20260722_island-wide-discovery/OPERATOR_ORCHESTRATION.md`
    + `dispatch-w29.md` `role: wave_orchestrator`
- **evidence_verified_against:** pax `20782d2d7` (OPERATOR_ORCHESTRATION
  background bind); IWD-W29 orchestrator early return after W29a launch
- **Originating mod feedback:** O0.R3 — plugin/home text is half-clear on
  O0→background and **uncleared** on orchestrator→parallel charge workers,
  “do not return until critical path completes”, and **moderator session
  etiquette** (release the window; integrate on notify)

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

**Fail id (proposed):** `PROC-ORCH-FOREGROUND-HOLD` — wave orchestrator or
charge worker runs long BUILD in the foreground.

**Fail id (proposed):** `PROC-MOD-FOREGROUND-HOLD` — **moderator/O0** runs
lane BUILD inline, foreground-awaits a wave, or otherwise holds the operator
session window instead of background-dispatch + release + reconcile-on-notify.

## Moderator (O0) background etiquette (required product text)

Ship as a named etiquette block in README + `AGENTS.md` Roles + `/wavves`
skill (not only densify/set-key asides):

1. **Dispatch background.** Wave orchestrators and heavy BUILD always launch
   non-blocking / background. O0 does not paste-run a wave in the mod thread.
2. **Release the window.** After charter + background deploy (+ AUTH sync /
   git if that is the land), O0 ends the turn. Do not keep the chat occupied
   waiting on adapters, densify, SODA pulls, or FCMG binds.
3. **No poll.** Do not busy-wait or “check again shortly.” Integrate when
   completion notifications / operator ping arrives. (Matches existing
   “never blocks polling a dispatch”; make it unmissable.)
4. **Reconcile then land.** On return: remasure against disk, git per protocol,
   update registry/waveset. Do not re-do charge work in O0.
5. **Chain ownership vs session hold.** If a wave orchestrator early-exits,
   O0 may background-resume it — still without foreground-holding the session.
6. **Say what shipped.** Brief operator note: what was backgrounded + where;
   not a live progress theater.

## Feature sketch (ORCH-FANOUT + MOD-BG)

| id | target | change |
|---|---|---|
| OF-01 | `skills/wavves/SKILL.md` + README Roles | Define three roles without collapse: **O0** (charter, background-dispatch wave orchestrator, reconcile, git) → **wave orchestrator** (read charge table; deploy workers; integrate; rollup) → **charge worker** (one charge id). |
| OF-02 | Fan-out rule | Each charge id in the dispatch table → its own background Task/worker when independent. Sequence only real deps (e.g. artifact before default URL). Forbidden: one agent serializes a+b+c+d. |
| OF-03 | Background rule (workers) | All wave orchestrator and charge-worker Task launches use background / non-blocking. |
| OF-04 | Completion rule | Wave orchestrator **must not return** to O0 until rollup+gate (or hard FAIL). Launching child ≠ wave complete. Integrate on completion notifications; no busy-poll. |
| OF-05 | Dispatch template | Default “You are” block: `role: wave_orchestrator`; “Do not execute charges yourself”; critical-path example `a → (b‖c) → d`. |
| OF-06 | `AGENTS.md` (plugin home template) | Promote OF-01…05 + moderator etiquette into Roles; keep portable across repos. |
| OF-07 | Eval | Fixture: fake 3-charge dispatch → assert ≥2 parallel workers after first PASS; assert no early orchestrator return; assert no solo multi-charge BUILD. |
| OF-08 | Moderator etiquette | Document the six-point **Moderator (O0) background etiquette** block above in README + skill + home AGENTS; fail id `PROC-MOD-FOREGROUND-HOLD`. Cross-link set-key densify note so it is not the only place this lives. |
| OF-09 | Proceed/charter playbooks | One line each: dispatch → background; O0 releases session; no foreground BUILD. |

## Acceptance

- [ ] README + SKILL name O0 / wave orchestrator / charge worker and the four fail ids
- [ ] Moderator background etiquette block present (OF-08), not buried under densify-only
- [ ] Dispatch paste template includes fan-out + background + no-early-exit
- [ ] Home `AGENTS.md` Roles updated in wavves-init template (and pax home synced when shipped)
- [ ] Eval/fixture for `PROC-ORCH-EARLY-EXIT`, `PROC-ORCH-SOLO-BUILD`, and `PROC-MOD-FOREGROUND-HOLD`
- [ ] `/mod-check` GO (or REVISE applied) before BUILD charter of the skill change
- [ ] Resolve wording conflict with “no empty mid-dispatch return” without reintroducing foreground holds

## Non-goals

- Changing git rules (runners still never git; O0 lands)
- Auto-polling / session-blocking waits
- Requiring max parallelism when charges truly share one write target
- Rewriting historical lane dispatches en masse (template + skill going forward)
- Replacing operator judgment pauses (gates still surface; they do not justify foreground BUILD)

## Evidence pointers

| item | path / note |
|---|---|
| Lane bind (interim) | pax `wavves/lanes/20260722_island-wide-discovery/OPERATOR_ORCHESTRATION.md` |
| W29 dispatch role | pax `.../dispatch-w29.md` (`role: wave_orchestrator`) |
| Early exit | W29 orchestrator returned after background-deploying W29a only |
| Prior related note | `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md` (empty mid-dispatch returns) |
