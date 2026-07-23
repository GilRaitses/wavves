# WOF-W1d — adversarial lens

```yaml
lens: adversarial
wave: WOF-W1d
artifact: feature-requests/20260723_wave-orchestrator-fanout.md
repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Lens verdict (this lens only)

**REVISE**

The FR names the real burns (`PROC-ORCH-SOLO-BUILD`, `PROC-ORCH-EARLY-EXIT`,
foreground holds at O0 and wave). As written, BUILD can ship role prose + a
dispatch paste + a soft fixture and still leave W29-class stalls open: there
is no durable stay-alive / resume contract for the wave orchestrator, OF-04
can be read as launch-and-exit-on-notify, OF-07 cannot catch early exit after
fan-out, and Acceptance omits `PROC-ORCH-FOREGROUND-HOLD` from the eval list.

O0 owns the lane verdict. This file does not grade sibling lenses.

## Proposed fail ids (map)

| id | Covers | Operable in FR as written? |
|---|---|---|
| `PROC-ORCH-SOLO-BUILD` | wave agent executes multiple charge ids itself | Partial. Named; "when independent" loophole; no detector |
| `PROC-ORCH-EARLY-EXIT` | return to O0 before critical path + rollup | Partial. Named; OF-04 notify wording can excuse it |
| `PROC-ORCH-FOREGROUND-HOLD` | wave orch / charge worker long BUILD in foreground | Named in Problem; missing from Acceptance eval list |
| `PROC-MOD-FOREGROUND-HOLD` | O0 inline BUILD / await / session hold | Partial. Six-point etiquette; no detector shape |

### Missing fail ids (needed before BUILD ACCEPT)

| id | Why |
|---|---|
| `PROC-ORCH-LAUNCH-AND-EXIT` | Fan-out of N background workers then immediate return to O0 before integrate/rollup (fake fan-out; W29 generalized) |
| `PROC-ORCH-ROLE-COLLAPSE` | Charge-worker work done inside the wave-orchestrator Task (or O0); roles named but collapsed in practice |
| `PROC-ORCH-DEP-OVERCLAIM` | False shared-write / dependency claims used to serialize a+b+c+d under the non-goal |
| `PROC-ORCH-NO-RESUME-CONTRACT` | Early exit or session end with no durable checkpoint (charge table state, pending worker ids, next integrate step) so O0 cannot resume without inventing |
| `PROC-MOD-PROGRESS-THEATER` | O0 narrates / "checks shortly" / holds chat with status prose instead of release + reconcile-on-notify |

Keep `PROC-ORCH-EARLY-EXIT` for any return before rollup+gate.
`PROC-ORCH-LAUNCH-AND-EXIT` is the specific fake-fan-out subtype the ≥2-workers
sketch will miss. Do not collapse them.

## Blocking failure modes

### FM-1 — Fake fan-out: launch children, return PASS-ish

**Class:** launch-and-exit / originating W29 fail re-encoded  
**Severity:** blocking  
**Fail ids:** `PROC-ORCH-EARLY-EXIT`, `PROC-ORCH-LAUNCH-AND-EXIT` (missing)

OF-03/OF-04 require background launches and "must not return until
rollup+gate," then say "Integrate on completion notifications; no
busy-poll." An agent can:

1. Background-deploy a (or a‖b‖c)
2. End the orchestrator turn immediately ("awaiting notify; no poll")
3. Return a PASS-ish summary to O0

That matches half of OF-04 and reproduces the stall unless O0 notices.
Acceptance asks to resolve conflict with "no empty mid-dispatch return"
(PHF parked; originating-mod note) but no OF row writes the resolution
text. BUILD can check the box with a vague sentence.

**Concrete BUILD footgun:** Dispatch table `a → (b‖c) → d`. Orchestrator
launches a,b,c as background Tasks, returns "workers deployed; integrate
on notify." d never runs. O0 sees a return and lands or moves on. Wave
stalls. OF-07 "≥2 parallel workers after first PASS" greens.

**Required revise:** Hard rule: wave orchestrator return to O0 is only legal
when rollup+gate (or hard FAIL) exists on disk. Launching child ≠ return
authority. If the host forces the orch Task to yield, write a resume
contract artifact before any return (see FM-2). Fixture: synthetic return
after N launches and before rollup file →
`PROC-ORCH-LAUNCH-AND-EXIT` / `PROC-ORCH-EARLY-EXIT`.

### FM-2 — No stay-alive / resume mechanism (unsafe default: prose only)

**Class:** unsafe default / happy-path host assumption  
**Severity:** blocking  
**Fail ids:** `PROC-ORCH-NO-RESUME-CONTRACT` (missing), `PROC-ORCH-EARLY-EXIT`

FR never states how the orchestrator "stays responsible" under
background+no-poll:

- Foreground-await children → `PROC-ORCH-FOREGROUND-HOLD`
- End turn after launch → `PROC-ORCH-EARLY-EXIT` (W29)
- Remain as integration surface until notify, then rollup, then return →
  needs explicit product text
- Checkpoint + O0 background-resume → etiquette point 5 mentions resume
  but no artifact schema

Without a mechanism, agents pick end-turn. Moderator etiquette point 5
("O0 may background-resume") has nothing durable to resume from.

**Concrete BUILD footgun:** Skill says "do not return until rollup." Host
completes the orch turn after Tool fan-out. No
`findings/*-orch-checkpoint.md` with pending charges / worker ids / next
step. O0 cannot resume; invents a new solo runner.

**Required revise:** Lock one v0 mechanism in the FR (mod-decide ok):
(A) orch Task remains open as integrate-on-notify surface until rollup, or
(B) mandatory checkpoint artifact + fail if return without rollup or
checkpoint. Name `PROC-ORCH-NO-RESUME-CONTRACT`. Etiquette point 5 binds
to that artifact path.

### FM-3 — Charge worker collapses into orchestrator (role theater)

**Class:** role collapse / solo builder under new labels  
**Severity:** blocking  
**Fail ids:** `PROC-ORCH-SOLO-BUILD`, `PROC-ORCH-ROLE-COLLAPSE` (missing)

OF-01 renames the stack O0 → wave orchestrator → charge worker. Charter
and wavves-init still use O0 / "Dispatched orchestrators/runners" / "Wave
subagents" and already say "never collapse." Observed fail was a single
`generalPurpose` runner doing the whole wave inline. FR does not require
a return contract mapping `charge_id → worker_agent_id` (or equivalent
disk evidence of distinct workers).

Charter also: "Dispatch depth is bounded… never further background
orchestrators, unless the charter grants it." BUILD may treat charge-worker
Tasks as forbidden depth and keep work inside the wave orch, or paste
`role: wave_orchestrator` while executing charges locally.

**Concrete BUILD footgun:** Dispatch says `role: wave_orchestrator` and
"Do not execute charges yourself." Orch writes all four findings files
itself, returns rollup. Labels pass OF-05; fan-out never happened.

**Required revise:** Return contract minimum: per charge id, worker id (or
explicit `serialized_reason` citing real shared-write dep). Missing map →
`PROC-ORCH-ROLE-COLLAPSE` / `PROC-ORCH-SOLO-BUILD`. Clarify charter depth
text: charge workers are the allowed wave members, not nested O0-class
orchestrators.

### FM-4 — Dependency overclaim serializes the wave (unsafe non-goal)

**Class:** unsafe default / happy-path-only fan-out  
**Severity:** blocking  
**Fail ids:** `PROC-ORCH-DEP-OVERCLAIM` (missing), `PROC-ORCH-SOLO-BUILD`

OF-02 fans out "when independent." Non-goal: no max parallelism when
charges share one write target. Default reading: when unsure, serialize.
Agent claims "shared lane home" or "shared registry" and runs a+b+c+d in
one worker. Fan-out rule never fires.

**Concrete BUILD footgun:** Mod-check-shaped table W1a‖W1b‖W1c‖W1d with
disjoint findings paths. Orch serializes "to avoid collisions on
findings/." OF-07 solo-BUILD fixture greens only if it requires four
distinct worker ids; a keyword fixture will not.

**Required revise:** Default is fan-out. Serialization requires a stated
shared write path that actually collides (same file, not same directory).
Fixture: four disjoint outputs → must show ≥2 concurrent workers (or four
worker ids); serialize without colliding path →
`PROC-ORCH-DEP-OVERCLAIM`.

### FM-5 — Eval cannot catch early exit (unrunnable / theater gate)

**Class:** gate that can't run / process-PASS  
**Severity:** blocking  

OF-07: "fake 3-charge dispatch → assert ≥2 parallel workers after first
PASS; assert no early orchestrator return; assert no solo multi-charge
BUILD." Acceptance lists eval for EARLY-EXIT, SOLO-BUILD,
MOD-FOREGROUND-HOLD. Gaps:

- No named harness (`evals/check_wave_orchestrator_fanout.py` or equal)
- If fixtures go through `evals/run_fixtures.py`, PASS is lens-keyword
  survival only (evals/README known limitation); cannot see early exit
- "≥2 parallel workers after first PASS" does not fail
  launch-all-then-exit-before-rollup (FM-1)
- No synthetic trace schema (launch log, return timestamp, rollup path
  mtime / existence)
- `PROC-ORCH-FOREGROUND-HOLD` absent from Acceptance eval list
- No stated mechanical emit for `PROC-MOD-FOREGROUND-HOLD` (session hold
  is behavioral; needs a review-only label or a trace fixture)

**Concrete BUILD footgun:** Three markdown fixtures under `evals/fixtures/`
with keywords `early exit`, `solo`, `foreground`. `run_fixtures.py` PASS.
Live orch still returns after launching W29a.

**Required revise:** Disjoint mechanical checker over synthetic orch traces
(same pattern as `check_proof_before_accept.py` / `check_paragraph_tunnel.py`).
Minimum emit: `PROC-ORCH-EARLY-EXIT`, `PROC-ORCH-LAUNCH-AND-EXIT`,
`PROC-ORCH-SOLO-BUILD`. Trace fields: charges launched, workers ids,
rollup_path present|absent, orch_returned_before_rollup bool.
Foreground holds may be review-only if labeled; do not claim mechanical
coverage you cannot run. BUILD ACCEPT requires checker PASS, not docs-only.

### FM-6 — O0 foreground theater / silent re-do of charge work

**Class:** moderator session hold / progress theater  
**Severity:** blocking  
**Fail ids:** `PROC-MOD-FOREGROUND-HOLD`, `PROC-MOD-PROGRESS-THEATER` (missing)

OF-08 six points are correct doctrine and match charter "never poll."
Still missing:

- What counts as holding (AwaitShell / blocking Task / inline BUILD diffs
  in O0 thread / "I'll check again shortly")
- Ban on O0 re-executing charge work when orch return is thin (etiquette
  point 4 says do not re-do; no fail id when violated)
- Fresh-thread dispatch (charter alternative to `run_in_background`) as
  operator-facing window hold
- Detector for "Say what shipped" becoming live progress theater

**Concrete BUILD footgun:** O0 pastes wave into mod thread "to watch it,"
or background-launches then polls with status paragraphs. Etiquette block
exists in README; behavior unchanged. Orch early-exits; O0 "helps" by
running charge d inline → role collapse + mod foreground hold.

**Required revise:** Closed ban list for O0 during active dispatch.
Fresh-thread runner that is operator-facing counts as
`PROC-MOD-FOREGROUND-HOLD` unless the paste is explicitly a non-mod window
and O0 has released. Point 4 violation → named fail (or fold into
`PROC-MOD-FOREGROUND-HOLD` with examples). Fixture: O0 transcript with
blocking await / inline BUILD after dispatch → FAIL.

### FM-7 — Wording conflict left as checkbox (reintroduces foreground or exit)

**Class:** unresolved product fork / ACCEPT theater  
**Severity:** blocking  

Acceptance: "Resolve wording conflict with 'no empty mid-dispatch return'
without reintroducing foreground holds." Feature sketch has no OF row for
the reconciled sentence. Older PHF option A was "no return until
RECONCILE+GATE." New doctrine is background workers + orch responsibility.
If BUILD copies PHF A literally into charter without the resume/integrate
path, agents foreground-hold. If BUILD copies only "integrate on notify,"
agents early-exit (FM-1).

**Concrete BUILD footgun:** One line added to charter: "orchestrator owns
completion." No definition of completion artifact. Agents interpret as
either sit-and-wait or launch-and-leave.

**Required revise:** Add OF-10 (or fold into OF-04) with the exact
replacement sentence pair: (1) workers always background; (2) orch returns
to O0 only when rollup+gate|FAIL on disk; (3) yield requires checkpoint.
Strike "empty mid-dispatch return" ambiguity by defining empty = return
without rollup/checkpoint.

## Non-blocking failure modes

### FM-8 — Critical-path example only (partial failure / gate pause)

**Severity:** non-blocking  

Example `a → (b‖c) → d` has no rule for b FAIL while c PASSes, or operator
gate between c and d. Orch may return partial as PASS or hold foreground
for the gate.

**Revise ask:** Return contract: per-charge verdict; wave status
`PASS|FAIL|PARTIAL|GATED`; gates escalate to O0 without O0 foreground BUILD.

### FM-9 — Home AGENTS / README role table drift

**Severity:** non-blocking  

OF-06/OF-08 patch wavves-init template + README + skill. Charter skill
role table still says "Dispatched orchestrator" / "Parallel subagents."
Three surfaces can disagree after BUILD.

**Revise ask:** Explicit patch list includes `skills/charter/SKILL.md`
three-roles table and dispatch-depth sentence, not only wavves + init.

### FM-10 — Foreign pax bind as accidental hard dep

**Severity:** non-blocking (waveset says illustration only)  

Evidence pointers cite pax `OPERATOR_ORCHESTRATION.md` and
`dispatch-w29.md`. If BUILD copies those paths into portable skill text as
required hydration, consumer repos break.

**Revise ask:** Portable examples use synthetic charge ids; pax paths stay
in FR evidence only.

### FM-11 — Eval lists MOD hold but not ORCH hold

**Severity:** non-blocking (subset of FM-5)  

Acceptance eval bullet omits `PROC-ORCH-FOREGROUND-HOLD` despite Problem
naming it. BUILD may ship three fixtures and skip orch foreground.

**Revise ask:** All four Problem fail ids in Acceptance; mark which are
mechanical vs review-only.

## What would change REVISE → GO (this lens)

1. Define stay-alive vs checkpoint resume; ban return without
   rollup|FAIL|checkpoint (`PROC-ORCH-NO-RESUME-CONTRACT`,
   `PROC-ORCH-LAUNCH-AND-EXIT`).
2. OF-04 wording that cannot be read as launch-and-exit-on-notify.
3. Return contract: charge_id → worker_id or proven serialize reason
   (`PROC-ORCH-ROLE-COLLAPSE`, `PROC-ORCH-DEP-OVERCLAIM`).
4. Mechanical orch-trace checker; OF-07 asserts that catch early exit after
   fan-out, not only ≥2 workers.
5. Closed O0 hold/theater ban; fresh-thread called out
   (`PROC-MOD-PROGRESS-THEATER` or folded examples).
6. OF row that resolves empty mid-dispatch vs background without
   foreground hold.
7. Acceptance eval includes `PROC-ORCH-FOREGROUND-HOLD` (mechanical or
   explicit review-only).

## Out of scope for this lens

- Grounding of foreign pax pins (WOF-W1a)
- Internal FR contradictions (WOF-W1b)
- Completeness inventory (WOF-W1c)
- Implementation plan or code

## Commit file list (orchestrator only)

- `wavves/lanes/20260723_wave-orchestrator-fanout-check/findings/WOF-adversarial.md` (this file)

No git. Escalation to O0 only.
