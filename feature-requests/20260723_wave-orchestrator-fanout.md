# FR-20260723 — Wave orchestrator fan-out + moderator background etiquette

- **Status:** mod-decide-complete (residual locks A/A; ready `/charter` BUILD)
- **Date:** 2026-07-23 (America/New_York)
- **WOF check:** `wavves/lanes/20260723_wave-orchestrator-fanout-check/` —
  verdict **REVISE** (`findings/WOF-verdict.md`); this file applies that revise
- **Product surface:** `skills/charter/SKILL.md` Roles + Dispatch mechanics;
  `skills/wavves-init/SKILL.md` Roles template; live `wavves/AGENTS.md`;
  README tracking table; `/wavves` router + proceed/charter playbooks;
  O0 etiquette; eval checker + fixtures
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
  - Lane-local bind (illustration only, not BUILD hydration): pax
    `wavves/lanes/20260722_island-wide-discovery/OPERATOR_ORCHESTRATION.md`
    + `dispatch-w29.md` `role: wave_orchestrator`
- **evidence_verified_against:** pax `20782d2d7` (OPERATOR_ORCHESTRATION
  background bind); IWD-W29 orchestrator early return after W29a launch
  (foreign pins are illustration; BUILD remasures in-repo seams only)
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

Older etiquette (“orchestrator owns completion; no empty mid-dispatch return”
from `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md`:
“Mid-dispatch empty returns… orchestrator owns completion; no return until
RECONCILE+GATE”) conflicts with “background + integrate on notify” unless the
skill states both with named leave-acts (locked below).

### Fail ids (closed for BUILD)

| id | fail condition | detector |
|---|---|---|
| `PROC-ORCH-SOLO-BUILD` | wave agent executes multiple charge ids itself instead of one background worker per independent charge | mechanical (trace: charge_id → worker_id map missing or same worker for ≥2 independent charges) |
| `PROC-ORCH-EARLY-EXIT` | wave orchestrator `return_to_O0` before rollup+gate (or hard FAIL / legal operator_gate) exists on disk | mechanical (orch_returned_before_rollup) |
| `PROC-ORCH-LAUNCH-AND-EXIT` | fan-out of N background workers then immediate `return_to_O0` before integrate/rollup (fake fan-out; W29 generalized). Keep distinct from EARLY-EXIT | mechanical (charges_launched≥1, rollup absent, orch_returned) |
| `PROC-ORCH-FOREGROUND-HOLD` | wave orch awaits workers by poll / blocking parent await, or launches a charge worker without background | mechanical when trace shows poll/blocking await; else review-only |
| `PROC-ORCH-ROLE-COLLAPSE` | charge-worker work done inside the wave-orchestrator Task (or O0) despite triad labels | mechanical (missing charge_id→worker_id; orch authored charge findings) |
| `PROC-ORCH-DEP-OVERCLAIM` | false shared-write / dependency claim used to serialize a+b+c+d under the shared-target non-goal | mechanical (serialize without colliding file path) |
| `PROC-ORCH-NO-RESUME-CONTRACT` | yield or session end with no durable checkpoint (charge table state, pending worker ids, next integrate step) and no rollup | mechanical (yield without checkpoint path) |
| `PROC-MOD-FOREGROUND-HOLD` | moderator/O0 runs lane BUILD inline, foreground-awaits a wave, or holds the operator session window instead of background-dispatch + release + reconcile-on-notify | review-only (transcript / closed ban list) |
| `PROC-MOD-PROGRESS-THEATER` | O0 narrates / “checks shortly” / holds chat with status prose instead of release + reconcile-on-notify | review-only |

## Leave-acts (locked vocabulary)

Three distinct acts. Do not collapse them under “return” or “end turn.”

| act | who | meaning | legal when |
|---|---|---|---|
| `return_to_O0` | wave orchestrator | finished handoff to O0; wave no longer owned by orch Task | **only** when rollup+gate exists on disk, or hard FAIL artifact, or legal `operator_gate` escalate artifact. Launching a child ≠ return authority. |
| `yield_awaiting_children` | wave orchestrator | ends the orch turn to await completion notifications; **responsibility persists** | allowed; **requires** checkpoint artifact before yield (see resume contract). Not a `return_to_O0`. Not a poll/timer promise. |
| `O0_release_window` | O0 / moderator | ends the operator-facing turn after charter + background deploy (+ AUTH/git land if that is the land) | always after deploy; integrate on notify. Distinct from orch leave-acts. |

**Bind:** `PROC-ORCH-EARLY-EXIT` and `PROC-ORCH-LAUNCH-AND-EXIT` attach only to
illegal `return_to_O0`. `yield_awaiting_children` without checkpoint →
`PROC-ORCH-NO-RESUME-CONTRACT`. Busy-wait / poll instead of yield →
`PROC-ORCH-FOREGROUND-HOLD`.

**Foreground frame (locked):** “Foreground” means holding the
**operator-visible or parent-blocking** turn (poll, blocking await, inline
BUILD in that window). A charge worker’s own Task session doing its one
charge is not `PROC-ORCH-FOREGROUND-HOLD`. O0 holding the mod chat is
`PROC-MOD-FOREGROUND-HOLD` / `PROC-MOD-PROGRESS-THEATER`.

## Mid-dispatch vs background — locked replacement sentences

Strike the ambiguous “no empty mid-dispatch return” paraphrase. Ship these
three sentences (OF-10) in charter Roles/Dispatch + wavves-init Roles +
home AGENTS:

1. **Workers always background.** Every charge-worker Task launch is
   non-blocking / background. Wave orchestrators themselves are launched
   background by O0 (v0: background-Task-only; fresh-thread wave orch is
   out of scope / Non-goal).
2. **Orchestrator returns to O0 only when rollup+gate or hard FAIL (or
   legal operator_gate escalate) exists on disk.** Launching children is
   not return authority. “Empty” means `return_to_O0` without
   rollup/checkpoint/gate artifact.
3. **Yield requires checkpoint.** If the host forces the orch Task to end
   before rollup, write
   `findings/<wave>-orch-checkpoint.md` (pending charges, worker ids,
   next integrate step) before any leave; resume is notify-driven, never
   poll/timer/monitor promises. Responsibility persists across
   notify-driven resumes.

Source phrase retained for history only (not product text): “orchestrator
owns completion; no return until RECONCILE+GATE exist.”

## Role rename (1:1, locked)

| live name (today) | product name (this FR) |
|---|---|
| O0 / Moderator | O0 (unchanged) |
| Dispatched orchestrator / Dispatched orchestrators/runners | **wave orchestrator** |
| Parallel subagents / Wave subagents | **charge worker** |

Do not keep two triads on one surface after BUILD. Charge workers are the
allowed wave members (not nested O0-class orchestrators). Charter depth text
must say charge-worker Tasks are in-scope for a wave; further background
orchestrators remain forbidden unless the charter grants them.

## Resume contract (v0 lock)

**Mechanism B (mandatory checkpoint):** If the orch Task yields before
rollup, it MUST write `findings/<wave>-orch-checkpoint.md` with at least:
charge table state, pending worker ids, next integrate step. Return without
rollup|FAIL|operator_gate **and** without checkpoint →
`PROC-ORCH-NO-RESUME-CONTRACT` (and usually `PROC-ORCH-EARLY-EXIT` /
`PROC-ORCH-LAUNCH-AND-EXIT`).

**Return contract minimum:** per charge id → `worker_agent_id` **or**
explicit `serialized_reason` citing a real shared **file** path that
collides (same file, not same directory). Missing map →
`PROC-ORCH-ROLE-COLLAPSE` / `PROC-ORCH-SOLO-BUILD`.

**Shared-write exception (locked):** Default is fan-out. Shared write target
→ sequential **separate** background workers (one charge id each), never
multi-charge solo in one agent. False “shared findings/” without a
colliding file → `PROC-ORCH-DEP-OVERCLAIM`.

**Legal `return_to_O0` classes only:** (1) rollup PASS/FAIL on disk,
(2) hard FAIL artifact, (3) operator_gate escalate artifact. Everything else
is EARLY-EXIT / LAUNCH-AND-EXIT / NO-RESUME-CONTRACT.

**O0 resume (etiquette §5):** fail remediation only, not the default
critical path. Resume binds to the checkpoint path above. Early exit remains
a fail even when O0 remediates.

## Moderator (O0) background etiquette (required product text)

Ship as a named etiquette block in README tracking table +
`skills/charter/SKILL.md` + `skills/wavves-init/SKILL.md` Roles + live
`wavves/AGENTS.md` + optional `/wavves` router mention (not only densify/set-key
asides). **O0 launch rules only in this block** (wave-orch fan-out lives in
OF-02…05).

1. **Dispatch background.** O0 always launches wave orchestrators and heavy
   BUILD non-blocking / background. O0 does not paste-run a wave in the mod
   thread.
2. **Release the window (`O0_release_window`).** After charter + background
   deploy (+ AUTH sync / git if that is the land), O0 ends the turn. Do not
   keep the chat occupied waiting on adapters, densify, SODA pulls, or FCMG
   binds.
3. **No poll.** Do not busy-wait or “check again shortly.” Integrate when
   completion notifications / operator ping arrives.
4. **Reconcile then land.** On return: remasure against disk, git per
   protocol, update registry/waveset. Do not re-do charge work in O0
   (violation → `PROC-MOD-FOREGROUND-HOLD` / role collapse).
5. **Resume is fail remediation only.** If a wave orchestrator early-exits,
   O0 may background-resume from the checkpoint artifact — still without
   foreground-holding. Resume is not the designed critical path.
6. **Say what shipped.** Brief operator note: what was backgrounded + where.
   Live progress theater / “checking shortly” → `PROC-MOD-PROGRESS-THEATER`.

**Closed O0 ban list during active dispatch:** AwaitShell / blocking Task
await on the wave; inline BUILD diffs for charge work in the mod thread;
“I’ll check again shortly”; fresh-thread operator-facing runner used as the
wave (counts as `PROC-MOD-FOREGROUND-HOLD` unless paste is an explicit
non-mod window and O0 has released).

## Feature sketch (ORCH-FANOUT + MOD-BG)

| id | target | change |
|---|---|---|
| OF-01 | **Primary:** `skills/charter/SKILL.md` (“The three roles” + Dispatch mechanics); `skills/wavves-init/SKILL.md` Roles section; live `wavves/AGENTS.md` §2 same BUILD; README “What wavves tracks” (or new Roles rows); optional one-line in `skills/wavves/SKILL.md` router | Define three roles without collapse using rename table above: **O0** → **wave orchestrator** → **charge worker**. Do **not** treat `skills/wavves/SKILL.md` alone or a nonexistent “README Roles” heading as the primary seam. |
| OF-02 | Fan-out rule (charter Dispatch + dispatch paste) | Each charge id → its own background Task/worker when independent. Default fan-out. Sequence only real deps. Shared colliding **file** → sequential separate workers, never multi-charge solo. Forbidden: one agent serializes a+b+c+d. |
| OF-03 | Background rule (split) | **O0→wave orch:** background Task (see Moderator etiquette §1). **Wave orch→charge workers:** all charge-worker launches background / non-blocking (OF-03 body; not folded into O0-only prose). |
| OF-04 | Completion + leave-acts | Ship leave-act table + legal return classes. Wave orchestrator must not `return_to_O0` until rollup+gate (or hard FAIL / operator_gate). Launching child ≠ wave complete. Integrate on completion notifications; no busy-poll. Yield ⇒ checkpoint. |
| OF-05 | Dispatch paste template | **Landing path:** default “You are” block inside `skills/charter/SKILL.md` Dispatch mechanics + canonical example snippet at `skills/charter/dispatch-wave-orchestrator.example.md`. Contents: `role: wave_orchestrator`; “Do not execute charges yourself”; critical-path example `a → (b‖c) → d`; fan-out + background + no-early-exit + checkpoint-on-yield. |
| OF-06 | AGENTS template + live home | Patch Roles in `skills/wavves-init/SKILL.md` and live `wavves/AGENTS.md` in the same BUILD. Pax / foreign home sync is operator follow-on (Non-goal), not a wavves_build Acceptance gate. |
| OF-07 | Eval | `evals/check_wave_orchestrator_fanout.py` + fixtures `evals/fixtures/wave-orch-fanout-*/` over **synthetic orch traces** (fields: charges_launched, worker_ids, rollup_path present\|absent, orch_returned_before_rollup, checkpoint_path present\|absent, serialize_reason). Mechanical emit minimum: EARLY-EXIT, LAUNCH-AND-EXIT, SOLO-BUILD, ROLE-COLLAPSE, DEP-OVERCLAIM, NO-RESUME-CONTRACT. Include FOREGROUND-HOLD case (mechanical if trace supports; else labeled review-only). MOD-FOREGROUND-HOLD / MOD-PROGRESS-THEATER: review-only fixtures or labeled review cases. Assert: fake 3-charge dispatch → ≥2 worker ids when independent; return after N launches before rollup → LAUNCH-AND-EXIT; no solo multi-charge BUILD. **Mechanical PASS ≠ live Cursor Task fan-out judgment.** |
| OF-08 | Moderator etiquette | Document the six-point **Moderator (O0) background etiquette** block above in charter + wavves-init + live AGENTS + README; fail ids `PROC-MOD-FOREGROUND-HOLD`, `PROC-MOD-PROGRESS-THEATER`. Cross-link `skills/set-key/SKILL.md` densify note back to this canonical block. |
| OF-09 | Proceed/charter playbooks | One line each in `skills/wavves/playbooks/proceed.md` and `skills/wavves/playbooks/charter-lane.md`: O0 dispatch → background; `O0_release_window`; no foreground BUILD. (O0 lines only; do not paste wave-orch fan-out rules into OF-09.) |
| OF-10 | Mid-dispatch wording | Ship the three locked replacement sentences above; retire “empty mid-dispatch return” as product text. |

## Acceptance

- [ ] `skills/charter/SKILL.md` three-role table + dispatch mechanics updated (fan-out, leave-acts, background, no-early-exit, checkpoint-on-yield)
- [ ] `skills/wavves-init/SKILL.md` Roles + live `wavves/AGENTS.md` Roles updated with rename table (same BUILD)
- [ ] README (+ optional `/wavves` router) name O0 / wave orchestrator / charge worker and the fail ids table
- [ ] Moderator background etiquette block present (OF-08), not buried under densify-only; set-key densify links back
- [ ] Dispatch paste at `skills/charter/SKILL.md` Dispatch mechanics + `skills/charter/dispatch-wave-orchestrator.example.md` includes fan-out + background + no-early-exit + checkpoint
- [ ] OF-09 one-liners in `playbooks/proceed.md` and `playbooks/charter-lane.md`
- [ ] Leave-acts + OF-10 replacement sentences shipped; “empty mid-dispatch return” not reintroduced as absolute session-hold
- [ ] `python3 evals/check_wave_orchestrator_fanout.py` PASS on `evals/fixtures/wave-orch-fanout-*/` covering at least: EARLY-EXIT, LAUNCH-AND-EXIT, SOLO-BUILD, ROLE-COLLAPSE, DEP-OVERCLAIM, NO-RESUME-CONTRACT, **PROC-ORCH-FOREGROUND-HOLD** (mechanical or explicit review-only label), plus review-only MOD-FOREGROUND-HOLD / MOD-PROGRESS-THEATER cases
- [ ] Fail ids documented in skill/README; append to `wavves/failure_log.yml` only when observed in a real run (ids may ship in skill text first)
- [ ] Re-`/mod-check` GO or `/mod-decide` residual locks complete before BUILD charter

## Non-goals

- Changing git rules (runners still never git; O0 lands)
- Auto-polling / session-blocking waits / timer or monitor promises
- Requiring max parallelism when charges truly share one colliding write **file** (sequential separate workers still required)
- Rewriting historical lane dispatches en masse (template + skill going forward)
- Replacing operator judgment pauses (gates still surface; they do not justify foreground BUILD)
- Foreign pax path hydration or “pax home synced when shipped” as a wavves_build Acceptance hard gate (operator follow-on)
- Fresh-thread wave orchestrator policy (v0 = background-Task-only)
- Claiming stdlib fixtures fully prove live multi-agent Cursor Task fan-out

## Rollback

Operator may withdraw fan-out paste requirements per lane. Skill prose revert
is ordinary skill lifecycle (proposal → accepted). New PROC-* ids append to
`wavves/failure_log.yml` only when observed in a real run.

## Open calls (for `/mod-decide` — residual only)

**CLOSED 2026-07-23 (operator sleep drive-through / O0.R4 lean locks):**

1. **FOREGROUND-HOLD-MECH → A** — mechanical when trace encodes
   poll/blocking await; else review-only
   (`wavves/lanes/20260723_wave-orchestrator-fanout-check/decisions/WOF-FOREGROUND-HOLD-MECH.md`).
2. **CHECKPOINT-FILENAME → A** — `findings/<wave>-orch-checkpoint.md`
   (`.../decisions/WOF-CHECKPOINT-FILENAME.md`).

Paste: `.../decisions/LOCKED-DECISIONS.md`.

(Leave-acts, OF-01 seams, eval home+checker, missing fail ids, OF-10
sentences, rename table, shared-write sequential-workers, legal return
classes, resume=remediation, pax sync out of AC were already locked — not open.)

## Evidence pointers

| item | path / note |
|---|---|
| Lane bind (interim, illustration) | pax `wavves/lanes/20260722_island-wide-discovery/OPERATOR_ORCHESTRATION.md` |
| W29 dispatch role (illustration) | pax `.../dispatch-w29.md` (`role: wave_orchestrator`) |
| Early exit | W29 orchestrator returned after background-deploying W29a only |
| Early exit (recurrence) | pax RLI-W2 orch returned after launching W2a only (2026-07-23 ~03:42–03:46 EDT); no checkpoint; O0 remasured + finished critical path |
| Prior related note | `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md` (mid-dispatch empty returns; orchestrator owns completion) |
| WOF check | `wavves/lanes/20260723_wave-orchestrator-fanout-check/findings/WOF-verdict.md` |
| Locked decisions | `wavves/lanes/20260723_wave-orchestrator-fanout-check/decisions/LOCKED-DECISIONS.md` |

## Next

`/charter` BUILD into charter skill + wavves-init/AGENTS + paste example +
evals. Residual mod-decide closed. Clear WOF `blocks_w2` on BUILD charter
AUTH sync.
