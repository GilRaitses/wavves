---
name: charter
description: >-
  Charter a bounded lane and dispatch waves of parallel subagents to a
  background orchestrator that reports back to the moderator (O0). Use for
  /charter, wavesets, parallel lanes, background orchestrators and multi-wave
  work while the operator thread stays available. Produces a lane home
  (waveset.md, dispatch.md, README.md), a registry entry and runnable gate
  guidance in EXECUTION_WIRING.md.
disable-model-invocation: true
---

# Charter

Delegated, multi-wave parallel execution under a central orchestrator. The
central orchestrator (**O0**, the operator-facing thread) does NOT execute
lane work itself. O0 **charters** a waveset, **dispatches** it to a
sub-orchestrator (a background subagent or a fresh thread) and that
sub-orchestrator runs **waves of parallel subagents** and **reports back to
O0**.

The skill complements sibling skills in this plugin:

- `wavves` (`/wavves`) is the default entry and routes to the playbooks below.
- `mod-check` (`/mod-check`) is the read-only adversarial sanity-check
  wave for a landed spec or plan before implementation.
- `mod-decide` (`/mod-decide`) locks open product/design calls after a check
  return and produces the Locked decisions paste for this charter.
- `mod-rotate` (`/mod-rotate`) hands the whole moderator (or one lane) to a
  fresh thread when the current one is overloaded.
- `wavves-init` (`/wavves-init`) establishes the standing home a fresh moderator
  instance hydrates from.

If the operator asks to BUILD while named forks are still open, stop and
route to **`/mod-decide`** (or ask them to paste locks) before writing
`waveset.md`.

**Execution layer inside runners.** If an execution-discipline plugin (for
example pstack) is installed, code-heavy waves may be dispatched to its agents
or told to follow one of its named playbooks and code-diff adversarial gates
may use its review commands as the evaluator panel. The layering has one
rule. Execution discipline governs HOW a runner writes code. The charter and
lane system stay the program authority (operator gates, honesty locks,
findings contract, commit protocol) and win on any conflict. In particular, a
plugin's never-block-on-the-human stance yields to operator-gated steps and
its session-pickup or pause playbooks are superseded at orchestrator level by
the rotation contract.

## The three roles (do not collapse)

| Role | Who | Does | Does NOT |
|---|---|---|---|
| **O0 / central orchestrator** | the operator-facing thread | charters, dispatches, reconciles returns, holds the map | execute lane work. mutate code directly. block waiting on a dispatch |
| **Dispatched orchestrator** | a background subagent OR a fresh thread | runs the waves, gates, reports to O0 | solicit the human operator directly (see escalation catch) |
| **Parallel subagents** | the wave members | one bounded, disjoint task each | touch another agent's files. cross wave boundaries |

The point is that **O0 stays unblocked**. Dispatch to the background, keep
working or end the turn and receive the return notice. Never sit and poll a
dispatch.

## When to use

The operator says any of "charter a waveset", "dispatch / launch a
(background) orchestrator", "run waves of parallel subagents", "spin up N
parallel lanes", "deep waves of 5+ subagents" or "have a subagent do X and
stay available to me".

## Workflow

```
- [ ] 1. Name the lane: short code (2-4 caps) + kebab label + date (operator's timezone)
- [ ] 2. Capture repo state: branch + origin/main hash (repo_state_verified_against)
- [ ] 3. Ground the charter: read the real seams/data the lane touches; cite real paths (verify with file search)
- [ ] 4. Choose model tiers for the lane orchestrator and each wave; record reason and cost discipline
- [ ] 5. Write the lane home: waveset.md + dispatch.md + README.md
- [ ] 6. Register the lane in the waves registry (lane code, waves, status, one-paragraph note)
- [ ] 7. Add any project-skill needs as proposal targets, never installed skills
- [ ] 8. Return a commit plan for the charter. Commit and push only when the repo governance or operator explicitly authorizes it.
- [ ] 9. Dispatch: background subagent (run_in_background) OR emit the fresh-thread one-liner. First verify no other active term owns the lane (see "Git ownership and dispatch concurrency")
- [ ] 10. Continue other work / end the turn. Do NOT poll. Reconcile on the return notice per "Reconciliation duties".
- [ ] 11. At execution time, run adversarial/acceptance gates as RUNNABLE harnesses; capture evidence to gate-captures/. See EXECUTION_WIRING.md.
```

### Step 1, lane naming

- Home directory convention `<repo>/wavves/lanes/<YYYYMMDD>_<lane-label>/`
  (any stable per-lane directory works. keep one convention per repo).
- A short uppercase lane code (for example `API`, `PERF`) used in the registry
  and in every wave id (`PERF-W1`, `PERF-INT`, `PERF-ACCEPT`).

### Step 3, grounding (non-negotiable)

A charter that is not grounded in the real files wastes a whole dispatch. Read
the actual convergence file, data sources and prior-lane artifacts. State the
**root cause / real constraint** in the charter, not a guess. Verify every
cited path exists before citing it.

### Step 4, the lane home files

Default lane layout:

```text
wavves/lanes/<YYYYMMDD>_<lane-label>/
  README.md
  waveset.md
  dispatch.md
  findings/
  gate-captures/
  decisions/
```

**waveset.md** is the authority doc. Sections, in order.

- Lane code, owner, type (execution vs research/read-only),
  `repo_state_verified_against` (the main-branch hash BEFORE this pass. never
  embed this file's own landing commit, which would create a self-referential
  hash loop).
- **Intent** (the operator's framing. use verbatim wording when given).
- **Grounding** (the real seams/data with exact paths and the verified root
  cause).
- **Locked decisions (do NOT reopen)**. The highest-value section. every fact
  an unprimed agent would get wrong. A lock protects settled decisions from
  churn, never from evidence. a locked decision contradicted by verified
  evidence is escalated to the orchestrator with the evidence, never silently
  defended or silently reopened.
- **Wave structure** (discovery, build, integrate, accept. see below).
- **Acceptance criteria** (hard, checkable, no reassurance bias).
- **Gated waves and operator involvement.** Name at charter time which waves are
  GATED and which mutations are operator-gated, so a lane that touches
  production carries its gates from birth.
- **Model routing and token discipline.** Include a table with `role`,
  `recommended_model_tier`, `reason`, `expected_context`, `expected_file_reads`
  and `cost_caveat`. Tier names are `fast`, `balanced` and `high-reasoning`
  unless the repo defines concrete model slugs. Use `high-reasoning` for
  architecture, integration, adversarial review and acceptance. Use `balanced`
  for bounded implementation with local validation. Use `fast` for inventory,
  search, formatting, link checks and mechanical scans.
- **Escalation (operator-protection catch)**, described below.

**dispatch.md** is a fenced paste block that declares the
role (this lane's orchestrator). lists hydration files in order (files, never
the transcript linearly). restates locked decisions inline. carries the
orchestrator home's etiquette locks (honesty, gates, git, prose) into the
dispatch. names active waves and which are GATED. states the execution order
for this dispatch (which waves run now vs pause for O0 approval). carries the
escalation catch. declares whether outputs are local-only or shared review
artifacts. mandates validation (typecheck/lint, no conflicting dev servers).
states the runner git ban (runners and wave subagents never run git write
operations. findings end with an explicit commit file list for the
orchestrator, exclusions stated, plus a plain statement that no git actions
were performed). instructs runners to BACKGROUND any long computation and
keep working instead of blocking on it (EXECUTION_WIRING.md Rule 1b). forbids
promising background monitoring the runner cannot perform. **mandates that
adversarial/acceptance gates are RUN, not asserted, with captured evidence
under `gate-captures/`, per EXECUTION_WIRING.md** and demands the return
contract below. The dispatch also carries the recommended model tier, the reason for
that tier and the expected context budget. Add a "more context" table mapping
each likely need to a file.

**Return contract (minimum fields).** Every dispatch return lists the waves run
with gate verdicts and capture paths, the commit file list for the orchestrator
(or an explicit statement that nothing needs committing), escalations and
operator-pending decisions, gap entries with reasons for anything promised but
not delivered and any mid-run defects found and fixed, with their cost.
Omissions are findings, never silences.

**README.md** is 8-15 lines. What the lane is, the file list, how to start it,
current status.

### Model routing table

Every `waveset.md` carries a table like this:

```text
role                  model tier        reason                         cost caveat
lane orchestrator     high-reasoning    cross-file plan and gates       highest-cost role, keep context bounded
discovery runners     fast              search and inventory            limit file reads, summarize paths
build runners         balanced          bounded edits plus checks       validate locally before return
adversarial gate      high-reasoning    risk and defect judgment        run after build artifacts exist
acceptance gate       high-reasoning    final verification              cite captures, do not re-read chat
```

When launching a subagent through an environment that exposes a `model`
argument, set that argument to the recommended model or model slug. When the
environment does not expose model selection, keep the recommendation in the
dispatch prompt and require the runner to report `model_enforcement:
not_available`.

Do not claim savings from this table unless a later accounting pass compares
planned tiers with actual token or billing records. The safe claim is that the
charter makes model selection auditable before execution and reserves expensive
models for judgment-heavy work.

### Project skill proposals

A lane may discover a repeated instruction that belongs in a project skill.
The lane does not install it. The lane drafts a proposal for the moderator:

```text
wavves/skills/proposed/<YYYYMMDD>_<skill-slug>.md
```

Minimum proposal fields:

- owning lane and findings file
- failure mode or repeated practice the skill addresses
- proposed trigger language
- proposed instructions
- destination requested: project file, repo rule, Cursor IDE skill or plugin
  update
- risks, review notes and operator decision needed
- regression-check field: for a proposal that edits an existing,
  already-installed skill file (as opposed to adding a wholly new one),
  state which `evals/fixtures/` cases the edit could plausibly affect and
  attach the output of `python3 evals/run_fixtures.py` run against the
  proposal applied to a scratch copy of the target file.

The moderator reviews the proposal, checks evidence and asks the operator
before saving it anywhere active. Accepted project-local skills may be copied
to `wavves/skills/accepted/`. Cursor IDE or plugin-level skills require a
separate operator-approved pass.

**Regression gate for edits to an installed skill file (added by lane
SELF, wavves-self-improvement).** A proposal that edits an already-shipped
`skills/*/SKILL.md` file is not promoted to `wavves/skills/accepted/`, and
is never applied directly to the installed file, until `evals/run_fixtures.py`
passes 3 consecutive times against the proposed edit. "Passes 3 consecutive
times" means: apply the proposed diff to a scratch copy of the target file,
point the runner at that scratch copy, run it 3 times in a row with no
intervening edit, and confirm zero FAILs across all 3 runs. A proposal that
adds a wholly new skill file, rather than editing an existing one, is
exempt from this gate (there is no existing detection surface to regress),
but is encouraged to add a fixture of its own to `evals/fixtures/` when it
introduces a new review lens or verdict rule.

### Step 5, registry entry

Append to `<repo>/wavves/registry.yml` (or your repo's equivalent) under
the active map:

```yaml
  <CODE>:
    label: <kebab-label>
    home: <lane home path>
    waves: [<CODE>-A, <CODE>-B, ..., <CODE>-INT, <CODE>-ACCEPT]
    status: chartered   # -> in-progress -> completed
    note: <one paragraph: intent, locked decisions, root cause, wave split, gates>
```

The registry is a convergence file. The chartering orchestrator is its single
editor. it syncs before appending and later status transitions are made only
by the orchestrator when it reconciles, never by dispatched runners.

## Wave structure (default shape. a lane may refine)

1. **Wave 1, discovery** (parallel, read-only findings). N subagents, each
   owning ONE `findings/<CODE>-<TOPIC>.md`. Include an **adversarial** member
   that hunts regressions and bad assumptions. Findings cite evidence, meaning
   real paths and transcribed output. a conclusion without its evidence does
   not satisfy the wave. If a wave member dies mid-wave, its findings file
   keeps its ownership. the orchestrator re-dispatches a replacement for that
   file rather than reassigning it to a sibling mid-flight.
2. **Wave 2, build** (parallel, NEW files preferred). Each agent owns disjoint
   new files plus a WIRING doc. Typecheck/lint clean. No conflicting build or
   dev-server processes in parallel. Code that could not be verified or
   qualified is reverted from the working tree before handoff, preserved at a
   stated location, with the revert and rationale recorded in the findings.
3. **Wave 3, integration** (SINGLE serialized editor). Edits the shared
   convergence file in the working tree only. The integration editor runs NO
   git commands. the orchestrator syncs the branch before dispatching this
   wave, freezes it for the duration and commits the handed-back tree
   afterward. GATED on O0 approval.
4. **Wave 4, acceptance** (verify on the real target, for example real
   hardware or the deployed platform, not a software fallback). Honest verdict
   plus evidence. GATED. The gate is graded by an evaluator with no authorship
   of the wave under review and the pass metric comes from the charter or
   from the orchestrator, never from the agent being judged.

**Waves can repeat, with a cap.** Re-capture, re-run or re-open a wave when
acceptance fails. the charter and registry stay the authority across repeats.
The charter fixes a remediation-loop cap (default 2 repeats per gate). When the
cap is reached, the runner stops looping and escalates to O0 with the named
failures. O0 decides whether to re-charter, descope or report the lane failed
upward. Verdicts carry named failures and a pass may still carry a named
deployment-blocking condition that must be cleared before any deploy
escalation.

**Long captures and serial test suites inside a wave.** A serial multi-minute
test or capture run fired in a blocking call hangs the dispatched
orchestrator's own session. When a wave does capture, shard by scenario to
disjoint subagents or background processes (one scenario, one output directory
each), size the blocking window above the slowest single unit rather than the
serial sum and keep timing-sensitive measurement serial on an isolated host,
because concurrent contexts corrupt the numbers.

**File-ownership discipline** is what makes parallelism safe. Disjoint scopes,
a single editor on any convergence file and serialized integration **across**
lanes that share that file. Wave members write findings incrementally into the
lane home as work proceeds, never holding results to the end.

## Git ownership and dispatch concurrency

- **The chartering orchestrator is the sole git actor for the lane.** Dispatched
  orchestrators, runners and wave subagents never run git state changes. Each
  runner ends its findings with an explicit commit file list for the
  orchestrator (including what to EXCLUDE, for example bulky derived artifacts
  whose canonical copy lives in durable storage) and states plainly that it
  performed no git actions.
- **Record the dispatch base commit.** The charter's
  `repo_state_verified_against` is the base every dispatched agent works from.
  If HEAD moves mid-dispatch, report the move with both hashes, reconcile the
  working edits onto the new HEAD and point downstream evaluators at the new
  HEAD, never the stale one.
- **Freeze a branch a dispatched agent is actively editing.** The orchestrator
  lands no commits on it for the duration of the dispatch or coordinates the
  commit explicitly.
- **Before dispatching a lane, verify no other active term or thread owns it**
  and record the check in the step log. Never double-dispatch.
- **Remote-rejected push** (a concurrent actor landed first). Fetch, then
  rebase with autostash, then push. Never force-push over the concurrent
  commit. Before rebasing, confirm no other active agent owns unstaged files
  in the working tree. if one does, coordinate before any git action.
- **No-protocol default.** In a repo with no stated commit protocol, the
  orchestrator writes lane-home artifacts and returns a commit plan. The
  orchestrator does not commit or push unless the operator explicitly asks.
  The orchestrator never invents git authority silently. The orchestrator records the
  default it applied.
- **Cross-actor artifacts.** An artifact meant for another actor is published
  to shared repo state before cross-actor use. an unpublished artifact is
  local-only and never crosses actors. An actor reading an artifact landed by
  another actor first syncs to the commit that landed it.

## Reconciliation duties (on the return notice)

Reconciling is verification, never transcription. Before reporting a lane
complete, the orchestrator

- opens the gate captures and spot-checks the returned summary against them.
- verifies any claimed commits are reachable from HEAD before treating the
  work as landed.
- distrusts a return that arrived implausibly fast or with implausibly low
  output volume, verifying throughput and output counts against expectations.
  when a defect invalidated earlier output, the pass re-runs in full and
  overwrites the poisoned artifacts.
- refreshes derived outputs against canonical inputs that moved during the
  dispatch and records the refresh.

## Execution wiring (runnable gates + evidence), invoked at run time

A charter is not done when files are written and a wave with an adversarial
gate is only credible when the gate is **run** and its evidence captured. Full
detail and a copy-paste probe live in
**[EXECUTION_WIRING.md](EXECUTION_WIRING.md)**. The five rules in brief.

1. **One long-blocking command for any measured transition.** A probe started
   with `&`/`nohup` in one tool call is reaped when that call returns. Run
   probe-start, trigger, wait-for-finish, read-results inside ONE command.
2. **Gates are runnable. evidence is captured.** Define the pass metric BEFORE
   the run. write the JSON summary and log to the lane home `gate-captures/`.
   the verdict cites measured numbers, never a claim.
3. **Read-only grounding vs operator-gated mutation.** Research touches
   infrastructure read-only. Any mutation is operator-gated and only runs in a
   later wave with approval.
4. **Record the decision durably.** If the repo keeps decision records, write
   one naming the decision, the measured evidence and what it supersedes.
5. **Harness shape.** Dependency-free, polls a liveness endpoint and a real
   user endpoint at a fixed cadence, records the max contiguous window where
   the real call fails while liveness is up. Generic probe included at
   `scripts/transition_gap_probe.py`.

## The escalation catch (operator-protection), REQUIRED

Every dispatch must instruct the dispatched orchestrator that **it answers to
the dispatching O0, not the human operator**. When a decision, trade-off,
locked-decision conflict, regression or sign-off on a gated, destructive or
scope-expanding step is needed, the runner pauses and returns the question to
the dispatching O0 in its summary. The runner does NOT solicit the human operator
directly. Gated waves require O0 approval and O0 approval for a mutation is
valid only when O0 holds operator approval for it. operator-gated means the
human operator and O0 relays that gate rather than substituting for it. At an
access, credential or permission boundary, the runner transcribes the
evidence of the block, records it as an escalation with concrete resolution
options and stops rather than improvising workarounds. A deploy or merge
escalation includes an explicit rollback procedure, a live monitoring plan and
an honest caveat list naming every check that could not be run, with
sequencing options for closing each caveat.

Two boundary cases. An urgent finding (a live regression, active data loss, a
security exposure) interrupts. the runner ends its wave early and returns it
immediately instead of sitting on it until the wave completes. And when a
fresh-thread runner lives in an operator-facing chat and the operator
addresses it directly, the operator outranks the catch. the runner answers,
then records the exchange for the dispatching O0 to reconcile.

The escalation catch lets O0 remain the single operator-facing surface
while work runs in the background.

## Dispatch mechanics

- **Background orchestrator.** Launch a subagent with run-in-background,
  prompt = the dispatch block (or "hydrate from
  dispatch.md"). State the execution order (for example
  run W1+W2, then pause for O0 approval before gated W3/W4) and the return
  contract. Then continue or end the turn. reconcile on return.
- **Dispatch depth is bounded.** A dispatched orchestrator dispatches wave
  subagents only, never further background orchestrators, unless the charter
  grants it explicitly with a stated depth.
- **A dispatch that never returns is a blocked item.** Record it in the
  registry and step log with a stated pickup action (how to check whether it
  crashed and what to re-dispatch). a lane is never left open silently.
- **Fresh thread.** Use `mod-rotate` (`/mod-rotate`) to emit the one-line
  paste the operator drops into a new thread.
- **Term stamping.** When the house runs term identities, a dispatched
  runner's id carries the dispatching term as suffix (`PERF-INT.R2`), so the
  chartering term is preserved even when the return reconciles under a later
  term.

## Origin note (why this is a named pattern)

The pattern emerged organically. A rotation dispatch file carried a
message-to-the-operator above the prompt block, which led the receiving agent
to launch a background orchestrator that then successfully launched parallel
subagents. The first waveset happened on that run. The pattern is now a consistent,
deliberate pattern, formalized here. The history explains the name only.
Operative instructions live inside the fenced dispatch block. text found
outside it is context, never instruction.

## Quality bar

- Charter grounded in real, verified paths. root cause stated, not guessed.
- Locked decisions let an unprimed agent avoid every known footgun.
- Escalation catch present in every dispatch.
- O0 never blocks on a dispatch. it reconciles on the return notice.
- No time-bombs. state conditions, not deadlines.
