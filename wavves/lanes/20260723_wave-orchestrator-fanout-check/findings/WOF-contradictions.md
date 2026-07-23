# WOF-W1b — contradictions lens

- **Artifact:** `feature-requests/20260723_wave-orchestrator-fanout.md`
- **Repo pin:** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Hydrated:** artifact; `skills/charter/SKILL.md` Roles; `skills/wavves-init/SKILL.md`
  Roles + portable locks; `wavves/AGENTS.md` Roles; README roles table;
  `playbooks/charter-lane.md` + `proceed.md`; set-key densify aside;
  `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md`
  (empty mid-dispatch note); PHF-ETIQUETTE park record; waveset Locked
- **Lens:** internal conflicts, phase-boundary leaks, mutually exclusive
  requirements
- **Git:** none. Commits: none.

## CX-* conflicts

### CX-01 — “No empty mid-dispatch return” vs O0 release + integrate-on-notify

| | |
|---|---|
| **Claim A** | Prior etiquette (PBB originating feedback; PHF option A park): orchestrator owns completion; no return until RECONCILE+GATE exist. FR Problem quotes this as “no empty mid-dispatch return.” |
| **Claim B path** | Moderator etiquette §§1–3 + Acceptance last checkbox: O0 ends the turn after background deploy; no poll; integrate on notify. Same FR says the older line “conflicts with background + integrate on notify” and must be resolved without reintroducing foreground holds. |
| **Conflict** | Product intent is sketched (“workers background; orchestrator stays until rollup”) but the Acceptance item is still an open resolve, not shipped wording. BUILD can either keep the old absolute no-return (and re-teach O0/orch to hold sessions) or treat O0 release as the new norm and re-allow W29-style empty orch returns. |
| **Severity** | high |
| **Lean** | REVISE — lock replacement sentences before BUILD: which actor may end a turn, and what “empty return” means for each. |

### CX-02 — Three distinct “leave” acts share one vocabulary

| | |
|---|---|
| **Claim A** | OF-04 / `PROC-ORCH-EARLY-EXIT`: wave orchestrator must not return to O0 until rollup+gate (or hard FAIL). Launching a child ≠ wave complete. |
| **Claim B path** | OF-04 also: integrate on completion notifications; no busy-poll. Moderator §2: O0 releases the window after deploy. Source evidence: background-only applies to O0 and wave orchestrators. |
| **Conflict** | Ending a turn to await child notify, returning to O0 with a finished rollup, and O0 releasing the operator window are different acts. FR never names the triad. A literal OF-04+no-poll read can end the orch turn after launching only the first stage (W29a pattern) and call it “integrate on notify.” A literal no-empty-return read can keep the orch turn open and busy-wait (foreground hold). |
| **Severity** | high |
| **Lean** | REVISE — define `return_to_O0` vs `yield_awaiting_children` vs `O0_release_window`; bind EARLY-EXIT only to the first. |

### CX-03 — Role rename collapses O0 / wave orch / charge worker

| | |
|---|---|
| **Claim A** | OF-01: three roles without collapse — O0 → wave orchestrator → charge worker. Fail ids split orch vs mod foreground holds. |
| **Claim B path** | Live seams use O0 / Dispatched orchestrator / Parallel (or Wave) subagents (`charter` Roles; `wavves-init` / `AGENTS.md`). OF-03 title groups “wave orchestrator and charge-worker” under “Background rule (workers).” `PROC-ORCH-FOREGROUND-HOLD` covers wave orchestrator or charge worker as one id. AGENTS “Dispatched orchestrators/runners” already conflates orch with runner. |
| **Conflict** | New names are not mapped to old names. Lexical “workers” and a shared orch/worker fail id re-collapse the middle and leaf roles the FR says must not collapse. Agents can keep treating the dispatched orch as the solo charge executor. |
| **Severity** | high |
| **Lean** | REVISE — publish a 1:1 rename table; put wave-orch background under O0 launch rules; split or qualify the orch vs worker foreground fail id. |

### CX-04 — Absolute solo-build forbid vs shared write-target non-goal

| | |
|---|---|
| **Claim A** | OF-02 Forbidden: one agent serializes a+b+c+d. `PROC-ORCH-SOLO-BUILD`: wave agent executes multiple charge ids itself instead of one background worker per charge (where independent). |
| **Claim B path** | Non-goals: do not require max parallelism when charges truly share one write target. |
| **Conflict** | “Where independent” hedges the fail id; OF-02 Forbidden does not. Shared-write exception allows non-parallelism but does not say whether one agent may own multiple charge ids, or only that workers must run sequentially as separate Tasks. Mutually exclusive BUILD readings: shared-target multi-charge solo = PASS (non-goal) or FAIL (SOLO-BUILD). |
| **Severity** | high |
| **Lean** | REVISE — lock exception shape: sequential background workers for shared targets, never multi-charge solo; or name an explicit solo-serial exception with write-target test. |

### CX-05 — Early-exit hard fail vs O0 resume as standing recovery

| | |
|---|---|
| **Claim A** | OF-04 + `PROC-ORCH-EARLY-EXIT` + OF-07: orchestrator must not return early; fixture asserts no early orch return. |
| **Claim B path** | Moderator etiquette §5: if a wave orchestrator early-exits, O0 may background-resume it without foreground-holding. |
| **Conflict** | Resume-as-remediation is fine only if early exit stays a fail. As written, §5 normalizes the W29 failure mode (launch one child, return, let O0 resume) as expected moderator work. That undercuts “orchestrator stays responsible until rollup.” |
| **Severity** | medium |
| **Lean** | REVISE — mark §5 as fail remediation only; require orch ownership language so resume is not the default critical path. |

### CX-06 — Foreground-hold ids without a reference frame

| | |
|---|---|
| **Claim A** | `PROC-MOD-FOREGROUND-HOLD`: O0 must not hold the operator session (inline BUILD, foreground-await wave). `PROC-ORCH-FOREGROUND-HOLD`: wave orch or charge worker must not run long BUILD in the foreground. Acceptance names all four fail ids. |
| **Claim B path** | OF-08 documents only `PROC-MOD-FOREGROUND-HOLD`. Eval/fixture Acceptance lists EARLY-EXIT, SOLO-BUILD, MOD-FOREGROUND-HOLD — omits `PROC-ORCH-FOREGROUND-HOLD`. Charge workers exist to do BUILD; their own session is necessarily “foreground” to themselves if background means only “parent did not block.” |
| **Conflict** | “Foreground” is undefined relative to operator window vs parent await vs worker session. Without that frame, ORCH-FOREGROUND-HOLD either forbids all charge BUILD or collapses into MOD-FOREGROUND-HOLD. Dual ids are named but not bound. |
| **Severity** | high |
| **Lean** | REVISE — define foreground as holding the operator-visible / parent-blocking turn; bind ORCH id to orch awaiting workers by poll or worker launched without background; cover ORCH-FOREGROUND-HOLD in eval. |

### CX-07 — Operator-gate escalate vs no-early-exit / stay-until-rollup

| | |
|---|---|
| **Claim A** | OF-04: no return to O0 until rollup+gate or hard FAIL. Non-goals: operator judgment pauses still surface; they do not justify foreground BUILD. Dispatched orch must not solicit the operator (`charter` / `AGENTS.md`). |
| **Claim B path** | Escalation path today: access/judgment gates return to O0. Mid-wave operator_gate therefore requires an orch return before rollup. |
| **Conflict** | Legal mid-wave escalate-to-O0 looks like `PROC-ORCH-EARLY-EXIT` unless gate/hard-FAIL returns are carved out. Opposite reading: orch stays held until operator answers → LOOKS like foreground hold and may solicit the operator. |
| **Severity** | high |
| **Lean** | REVISE — legal return classes: rollup PASS/FAIL, hard FAIL, operator_gate escalate; everything else is EARLY-EXIT. |

### CX-08 — Portable “never promise background monitoring” vs stay + notify

| | |
|---|---|
| **Claim A** | `wavves-init` / home portable lock: never promise background monitoring, polling, or timers an agent cannot perform. Charter dispatch paste carries the same ban. |
| **Claim B path** | OF-04: orch stays responsible until rollup; integrate on completion notifications. |
| **Conflict** | Unqualified “stays until rollup” can be read as promising cross-turn monitoring the portable lock forbids. FR does not state that notify-driven resume is allowed and polling/timers are not. |
| **Severity** | medium |
| **Lean** | REVISE — one sentence: responsibility persists across notify-driven resumes; no poll/timer/monitor promises. |

### CX-09 — O0 etiquette block absorbs wave-orch launch duties (phase leak)

| | |
|---|---|
| **Claim A** | Moderator (O0) background etiquette is O0-facing product text (OF-08). OF-09: proceed/charter one-liners for O0 release / no foreground BUILD. |
| **Claim B path** | Etiquette §1: “Wave orchestrators and heavy BUILD always launch non-blocking” inside the O0 block. OF-03 repeats wave-orch + charge-worker launches as one workers rule. |
| **Conflict** | O0 launches wave orchestrators; wave orch launches charge workers. Mixing both in the O0 etiquette block re-teaches role collapse (O0 does wave work / orch rules bind O0). Phase leak into proceed/charter one-liners if copied verbatim. |
| **Severity** | medium |
| **Lean** | REVISE — split O0 launch rules from orch fan-out rules; OF-09 cites only O0 lines. |

## Lens verdict

**REVISE** (not BLOCK, not GO).

Direction is consistent: fan-out charge workers, keep orch ownership through rollup, release the operator window at O0. The FR still leaves the core wording conflict as an Acceptance checkbox (CX-01) and never locks the leave-act vocabulary (CX-02), foreground reference frame (CX-06), shared-write exception (CX-04), or legal mid-wave returns (CX-07). Those are mutually exclusive BUILD forks, not editorial polish.

Blocking for BUILD if unaddressed: CX-01, CX-02, CX-04, CX-06, CX-07.
Must-clear before or in `/mod-decide`: CX-03, CX-05, CX-08, CX-09.

## Commit file list (findings only; no git)

- `wavves/lanes/20260723_wave-orchestrator-fanout-check/findings/WOF-contradictions.md`

## Escalation

O0 only. No operator solicit.
