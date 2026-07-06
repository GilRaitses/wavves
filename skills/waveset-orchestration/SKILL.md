---
name: waveset-orchestration
description: >-
  Charter a waveset and dispatch it to a background or fresh orchestrator that
  runs waves of parallel subagents and reports back to the central orchestrator
  (O0) without blocking it. Use when the operator asks to charter a waveset,
  dispatch or launch a background orchestrator, run waves of parallel
  subagents, spin up parallel lanes, or delegate a multi-wave campaign while
  the main thread stays available. Produces a lane home (WAVESET_CHARTER,
  ORCHESTRATOR_DISPATCH_PROMPT, README), a waves-registry entry, and a
  background-orchestrator dispatch. Also covers the execution wiring every
  runner needs at run time, described in EXECUTION_WIRING.md.
---

# Waveset Orchestration

Delegated, multi-wave parallel execution under a central orchestrator. The
central orchestrator (**O0**, the operator-facing thread) does NOT execute
lane work itself. It **charters** a waveset, **dispatches** it to a
sub-orchestrator (a background subagent or a fresh thread), and that
sub-orchestrator runs **waves of parallel subagents** and **reports back to
O0**.

This complements two sibling skills in this plugin:

- `orchestrator-rotation` hands the whole orchestrator (or one lane) to a
  fresh thread when the current one is overloaded.
- `orchestrator-home` establishes the standing home file a fresh orchestrator
  instance hydrates from.

**Execution layer inside runners.** If an execution-discipline plugin (for
example pstack) is installed, code-heavy waves may be dispatched to its agents
or told to follow one of its named playbooks, and code-diff adversarial gates
may use its review commands as the evaluator panel. That layering has one
rule. Execution discipline governs HOW a runner writes code; the charter and
lane system stay the program authority (operator gates, honesty locks,
findings contract, commit protocol) and win on any conflict. In particular, a
plugin's never-block-on-the-human stance yields to operator-gated steps, and
its session-pickup or pause playbooks are superseded at orchestrator level by
the rotation contract.

## The three roles (do not collapse)

| Role | Who | Does | Does NOT |
|---|---|---|---|
| **O0 / central orchestrator** | the operator-facing thread | charters, dispatches, reconciles returns, holds the map | execute lane work; mutate code directly; block waiting on a dispatch |
| **Dispatched orchestrator** | a background subagent OR a fresh thread | runs the waves, gates, reports to O0 | solicit the human operator directly (see escalation catch) |
| **Parallel subagents** | the wave members | one bounded, disjoint task each | touch another agent's files; cross wave boundaries |

The point is that **O0 stays unblocked**. Dispatch to the background, keep
working or end the turn, and receive the completion notification. Never sit
and poll a dispatch.

## When to use

The operator says any of "charter a waveset", "dispatch / launch a
(background) orchestrator", "run waves of parallel subagents", "spin up N
parallel lanes", "deep waves of 5+ subagents", or "have a subagent do X and
stay available to me".

## Workflow

```
- [ ] 1. Name the lane: short code (2-4 caps) + kebab label + date (operator's timezone)
- [ ] 2. Capture repo state: branch + origin/main hash (repo_state_verified_against)
- [ ] 3. Ground the charter: read the real seams/data the lane touches; cite real paths (verify with file search)
- [ ] 4. Write the lane home: WAVESET_CHARTER.md + ORCHESTRATOR_DISPATCH_PROMPT.md + README.md
- [ ] 5. Register the lane in the waves registry (lane code, waves, status, one-paragraph note)
- [ ] 6. Commit + push the charter (if the repo's protocol requires it)
- [ ] 7. Dispatch: background subagent (run_in_background) OR emit the fresh-thread one-liner
- [ ] 8. Continue other work / end the turn. Do NOT poll. Reconcile on the completion notification.
- [ ] 9. At execution time, run adversarial/acceptance gates as RUNNABLE harnesses; capture evidence to gate_captures/. See EXECUTION_WIRING.md.
```

### Step 1, lane naming

- Home directory convention `<repo>/.cca/catalogue/O0/<YYYYMMDD>_<lane-label>/`
  (any stable per-lane directory works; keep one convention per repo).
- A short uppercase lane code (for example `API`, `PERF`) used in the registry
  and in every wave id (`PERF-W1`, `PERF-INT`, `PERF-ACCEPT`).

### Step 3, grounding (non-negotiable)

A charter that is not grounded in the real files wastes a whole dispatch. Read
the actual convergence file, data sources, and prior-lane artifacts. State the
**root cause / real constraint** in the charter, not a guess. Verify every
cited path exists before citing it.

### Step 4, the lane home files

**WAVESET_CHARTER.md** is the authority doc. Sections, in order.

- Lane code, owner, type (execution vs research/read-only),
  `repo_state_verified_against` (the main-branch hash BEFORE this pass; never
  embed this file's own landing commit, which would create a self-referential
  hash loop).
- **Intent** (the operator's framing; use verbatim wording when given).
- **Grounding** (the real seams/data with exact paths, and the verified root
  cause).
- **Locked decisions (do NOT reopen)**. The highest-value section; every fact
  an unprimed agent would get wrong.
- **Wave structure** (discovery, build, integrate, accept; see below).
- **Acceptance criteria** (hard, checkable, no reassurance bias).
- **Escalation (operator-protection catch)**, described below.

**ORCHESTRATOR_DISPATCH_PROMPT.md** is a fenced paste block that declares the
role (this lane's orchestrator); lists hydration files in order (files, never
the transcript linearly); restates locked decisions inline; names active waves
and which are GATED; states the execution order for this dispatch (which waves
run now vs pause for O0 approval); carries the escalation catch; mandates
validation (typecheck/lint, no conflicting dev servers) and the repo's
commit/push protocol; instructs runners to BACKGROUND any long computation and
keep working instead of blocking on it (EXECUTION_WIRING.md Rule 1b);
**mandates that adversarial/acceptance gates are RUN, not asserted, with
captured evidence under `gate_captures/`, per EXECUTION_WIRING.md**; and
demands a return contract. Add a "more context" table mapping each likely need
to a file.

**README.md** is 8-15 lines. What the lane is, the file list, how to start it,
current status.

### Step 5, registry entry

Append to `<repo>/.cca/waves.registry.yml` (or your repo's equivalent) under
the active map:

```yaml
  <CODE>:
    label: <kebab-label>
    home: <lane home path>
    waves: [<CODE>-A, <CODE>-B, ..., <CODE>-INT, <CODE>-ACCEPT]
    status: chartered   # -> in-progress -> completed
    note: <one paragraph: intent, locked decisions, root cause, wave split, gates>
```

## Wave structure (default shape; a lane may refine)

1. **Wave 1, discovery** (parallel, read-only findings). N subagents, each
   owning ONE `findings/<CODE>-<TOPIC>.md`. Include an **adversarial** member
   that hunts regressions and bad assumptions.
2. **Wave 2, build** (parallel, NEW files preferred). Each agent owns disjoint
   new files plus a WIRING doc. Typecheck/lint clean. No conflicting build or
   dev-server processes in parallel.
3. **Wave 3, integration** (SINGLE serialized editor). Edits the shared
   convergence file. Pull/rebase first. GATED on O0 approval.
4. **Wave 4, acceptance** (verify on the real target, for example real
   hardware or the deployed platform, not a software fallback). Honest verdict
   plus evidence. GATED.

**Waves can repeat.** Re-capture, re-run, or re-open a wave when acceptance
fails; the charter and registry stay the authority across repeats.

**Long captures and serial test suites inside a wave.** A serial multi-minute
test or capture run fired in a blocking call hangs the dispatched
orchestrator's own session. When a wave does capture, shard by scenario to
disjoint subagents or background processes (one scenario, one output directory
each), size the blocking window above the slowest single unit rather than the
serial sum, and keep timing-sensitive measurement serial on an isolated host,
because concurrent contexts corrupt the numbers.

**File-ownership discipline** is what makes parallelism safe. Disjoint scopes,
a single editor on any convergence file, and serialized integration **across**
lanes that share that file.

## Execution wiring (runnable gates + evidence), invoked at run time

A charter is not done when files are written, and a wave with an adversarial
gate is only credible when the gate is **run** and its evidence captured. Full
detail and a copy-paste probe live in
**[EXECUTION_WIRING.md](EXECUTION_WIRING.md)**. The five rules in brief.

1. **One long-blocking command for any measured transition.** A probe started
   with `&`/`nohup` in one tool call is reaped when that call returns. Run
   probe-start, trigger, wait-for-completion, read-results inside ONE command.
2. **Gates are runnable; evidence is captured.** Define the pass metric BEFORE
   the run; write the JSON summary and log to the lane home `gate_captures/`;
   the verdict cites measured numbers, never a claim.
3. **Read-only grounding vs operator-gated mutation.** Research touches
   infrastructure read-only. Any mutation is operator-gated and only runs in a
   later wave with approval.
4. **Record the decision durably.** If the repo keeps decision records, write
   one naming the decision, the measured evidence, and what it supersedes.
5. **Harness shape.** Dependency-free, polls a liveness endpoint and a real
   user endpoint at a fixed cadence, records the max contiguous window where
   the real call fails while liveness is up. Generic probe included at
   `scripts/transition_gap_probe.py`.

## The escalation catch (operator-protection), REQUIRED

Every dispatch must instruct the dispatched orchestrator that **it answers to
the dispatching O0, not the human operator**. When a decision, trade-off,
locked-decision conflict, regression, or sign-off on a gated, destructive, or
scope-expanding step is needed, the runner pauses and returns the question to
the dispatching O0 in its summary. It does NOT solicit the human operator
directly. Gated waves require O0 approval.

This is the safeguard that lets O0 remain the single operator-facing surface
while work runs in the background.

## Dispatch mechanics

- **Background orchestrator.** Launch a subagent with run-in-background,
  prompt = the dispatch block (or "hydrate from
  ORCHESTRATOR_DISPATCH_PROMPT.md"). State the execution order (for example
  run W1+W2, then pause for O0 approval before gated W3/W4) and the return
  contract. Then continue or end the turn; reconcile on completion.
- **Fresh thread.** Use `orchestrator-rotation` to emit the one-line paste the
  operator drops into a new thread.

## Origin note (why this is a named pattern)

It emerged organically. A rotation dispatch file carried a
message-to-the-operator above the prompt block, which led the receiving agent
to launch a background orchestrator that then successfully launched parallel
subagents. That was the first waveset it happened on; it is now a consistent,
deliberate pattern, formalized here.

## Quality bar

- Charter grounded in real, verified paths; root cause stated, not guessed.
- Locked decisions let an unprimed agent avoid every known footgun.
- Escalation catch present in every dispatch.
- O0 never blocks on a dispatch; it reconciles on the completion notification.
- No time-bombs; state conditions, not deadlines.
