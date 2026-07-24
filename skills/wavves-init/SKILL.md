---
name: wavves-init
description: >-
  Bootstrap and maintain the wavves home so any fresh moderator (O0) hydrates
  from files instead of chat. Use for /wavves-init, first-time repo setup,
  repairing the standing home, or defining term identity and rotation rules.
  Produces <repo>/wavves/INDEX.md, AGENTS.md, registry.yml, step-log.md and
  rotations/.
disable-model-invocation: true
---

# wavves-init

A standing hydration contract that outlives any single chat thread. The home
is a directory (convention `<repo>/wavves/`) whose `INDEX.md` is the fast
entry point every fresh orchestrator instance reads first. `AGENTS.md` holds
the stable contract. Per-rotation state lives in `rotations/`. the standing
files only point.

Default tree:

```text
wavves/
  INDEX.md
  AGENTS.md
  registry.yml
  step-log.md
  rotations/
    rotation-r01-YYYYMMDD-HHMM.md
  lanes/
    YYYYMMDD_lane-label/
      README.md
      waveset.md
      dispatch.md
      findings/
      gate-captures/
      decisions/
  skills/
    proposed/
      README.md
    accepted/
      README.md
```

Pointer model:

```text
INDEX.md -> current rotation -> active lanes -> lane README -> waveset.md
         -> blocked decisions -> operator questions
         -> proposed skills -> moderator review -> operator approval
```

Write the home ONCE per repo, then let rotations reuse it. Do not restate its
contents in every rotation file.

If the home already exists, adopt it. Read the existing `INDEX.md`,
`AGENTS.md`, `step-log.md`, registry and rotations directory before writing.
Do not overwrite those files. Add only missing owned files and report any
conflict as a setup gap for the operator.

## What the standing AGENTS.md contains

Use this template, adapted to the repo. Every section below earns its place
by preventing a specific fresh-instance failure.

### 1. Hydration stack (read in this order)

1. The repo's own governance doc (surfaces, write policy, commit protocol,
   naming rules) if one exists. When none exists, setup writes stay confined
   to the home directory, lane homes and the registry. No commit or push
   happens unless the operator explicitly requests it.
2. `INDEX.md` in the home directory. The small, current pickup map with the
   active rotation file, active lanes, blocked decisions and next files to
   read. Keep this file short enough for quick grounding.
3. `rotations/` in the home directory. Rotation handoffs, one file per
   rotation, datestamped. THE NEWEST FILE IS THE CURRENT POSITION, naming
   active dispatches, pending pickups, blocked items and uncommitted state.
4. The waves registry (`<repo>/wavves/registry.yml` or equivalent). Every
   chartered lane, status and home path. The registry note per lane is the
   compressed authority. the lane home's `waveset.md` is the full
   authority.
5. The lane homes named by the current rotation file.
6. `step-log.md` in the home directory, the orchestrator's synthesis trace
   (append, never rewrite).
7. `skills/proposed/` and `skills/accepted/` in the home directory. Proposed
   project skills are evidence-backed drafts from lane orchestrators. Accepted
   skills are operator-approved project instructions, not automatic IDE
   installs.

State explicitly that agents hydrate from these files and never read chat
transcripts linearly. Transcripts are for keyword search only and only when a
rotation file cites one.

### 1a. INDEX.md shape

`INDEX.md` is the file optimized for fast indexing and grounding. Keep it
short and current:

```text
# wavves index

current_identity: O0.R<N>
current_rotation: rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md

active_lanes:
  - code: <CODE>
    home: lanes/<YYYYMMDD>_<lane-label>/
    status: <chartered|in-progress|blocked|accepted>
    next_read: lanes/<YYYYMMDD>_<lane-label>/README.md

blocked_decisions:
  - <operator decision needed>

project_skills:
  proposed: skills/proposed/
  accepted: skills/accepted/

model_policy:
  default: record recommendation before dispatch
  high_reasoning: integration, adversarial review, acceptance, architecture
  balanced: bounded implementation with local validation
  fast: inventory, search, formatting, link checks, mechanical scans
```

Do not copy long findings, logs or transcripts into `INDEX.md`. Point to them.

### 2. The three roles (never collapse)

- **O0** is operator-facing: charters lanes, background-dispatches **wave
  orchestrators**, reconciles on notify, lands commits per repo protocol.
  Never executes charge work inline when a dispatch fits. Never polls.
  After deploy: `O0_release_window`. On orch notify, follow the
  **yield vs return reconcile branch** (pickup playbook + etiquette below).
- **wave orchestrator** (background Task) fans out **charge workers**,
  integrates, writes rollup+gate. Must not `return_to_O0` before those
  artifacts (or hard FAIL / operator_gate). Must not solo-serialize
  independent charges. Yield requires checkpoint.
- **charge worker** takes one bounded disjoint task each; no shared-file
  collisions; never git; never solicit the operator (escalate to O0 via
  orch).

**Moderator (O0) background etiquette** (canonical; densify/set-key link here):

1. Dispatch wave orchestrators background.
2. `O0_release_window` after charter + deploy (+ AUTH/git if that is the land).
3. No poll / “check again shortly.”
4. Reconcile then land on notify; do not re-do charge work in O0.
5. **Yield resume is normal pickup (not fail remediation).** On any orch
   return notice whose leave-act is `yield_awaiting_children`, O0 MUST in
   the **same turn** remeasure `findings/<wave>-orch-checkpoint.md` and
   the named child outs on disk. If children are COMPLETE and the next
   integrate/ACCEPT charge is due, Task-resume the orch (or re-dispatch
   from the checkpoint). Do **not** step-log-and-park. If rollup+gate
   (or hard FAIL / legal operator_gate) is already on disk at that
   remeasure, treat as `return_to_O0` and land the orch `commit_file_list`
   per repo protocol — do not wait for a second notify. Nested charge-worker
   Task completions may not surface as O0 notices; disk remasure is the
   authority. **Fail remediation only** applies when resuming after a true
   fail / illegal early exit / poisoned wave — not to mid-wave yield.
6. Brief note of what was backgrounded; progress theater is a fail
   (`PROC-MOD-PROGRESS-THEATER`). Inline BUILD / foreground await →
   `PROC-MOD-FOREGROUND-HOLD`.

### 3. Etiquette locks (carried into every charter and dispatch)

The list has two kinds of entries. Portable locks travel as written and are
the mandatory core of the contract. trimming them at setup gutters the home,
because each one encodes a failure someone hit in real work. House bindings
are the slots the installing house fills in concretely (hosts, stores,
styles). any values shown for them are examples, never defaults.

Portable locks.

- Honesty. Modeled-not-measured labeling, no reassurance bias, failed gates
  reported as failed, evidence transcribed not asserted. Visual claims
  require looking at the rendered output before claiming done. Missing or
  unresolved artifacts are recorded explicitly, never inferred or
  fabricated. unprocessable items get gap entries with reasons and count
  shrinkage is stated plainly.
- Anomalies. Check the actual values against baselines before calling a
  warning benign. a warning that recurs across runs is systematic until
  proven otherwise. state the worst-case interpretation first. say plainly
  when you do not know and require a citable source before calling a
  behavior expected or safe. Never promise background monitoring, polling or
  timers an agent cannot perform.
- Returns. Never trust a return that arrives implausibly fast or
  with implausibly low output volume. verify throughput and output counts
  against expectations and when a defect invalidated earlier output,
  re-run the full pass and overwrite the poisoned artifacts. Record mid-run
  defects, their fixes and their cost in the findings even when fully
  remediated.
- Reporting. Report the full result distribution alongside any gate
  statistic. scope headline claims to the measured sample size and
  conditions. state the unit, resolution and quality limits of derived
  metrics where quoted and label cross-domain analogies as analogies.
  Claims in derived documents trace to findings files, quotations verbatim.
  mechanisms, attributions, timings and scopes are never invented or
  shifted. Returns carry only the requested fields, with no added
  restructuring.
- Adversarial gates. Independent evaluator with no authorship of the work
  under review, runnable checks, evidence to the lane home `gate-captures/`,
  capped remediation loops, then escalate. Verdicts carry named failures. a
  pass may carry a named deployment-blocking condition that must clear
  before any deploy escalation.
- Prose gates for operator-facing writing, whatever house style the operator
  enforces.
- Git. Runners never commit. the orchestrator commits per the repo protocol
  and treats the work as incomplete until the push is verified. Local-only
  or staged-only state is never a finished state. no feature branches unless
  explicitly authorized. no delayed batching for file-changing passes.
  Artifacts never embed their own landing commit (a self-referential hash
  loop). report the landing commit in the final message instead.
  Runner findings end with an explicit commit file list for the
  orchestrator, exclusions stated (bulky derived artifacts stay out when a
  durable store holds the canonical copy), plus a plain no-git statement.
- Git concurrency. Record the dispatch base commit. if HEAD moves
  mid-dispatch, report both hashes, reconcile the edits onto the new HEAD and
  point evaluators at the new HEAD. Never land commits on a branch a
  dispatched agent is actively editing (freeze or coordinate). A
  remote-rejected push resolves by fetch, then rebase with autostash, then
  push, never force-push. before rebasing, confirm no other active agent
  owns unstaged working-tree files. A divergent untracked local copy that
  blocks a pull resolves in favor of the tracked origin artifact, with the
  deletion logged. Verify claimed commits are reachable from HEAD before
  treating reported work as landed. Before dispatching a lane, verify no
  other active term owns it and record the check in the step log. An older
  thread holding uncommitted work conforms it to a newer term's rulings
  before landing. Unverified or unqualifiable code on a shared branch is
  reverted before handoff, preserved at a stated location, with the revert
  recorded.
- Cross-actor artifacts. An artifact meant for another actor is published
  to shared repo state before cross-actor use. an unpublished artifact is
  local-only and never crosses actors. An actor reading an artifact landed
  by another actor first syncs to the commit that landed it. Dispatch
  prompts declare whether outputs are local-only or shared review
  artifacts. Live repo state governs over any cached or bundled copy.
- Judgment calls that belong to the operator are NEVER inferred by agents.
  Operator-gated actions (attestation, gated mutations, destructive steps)
  always pause for the operator. any never-block-on-the-human execution
  principle yields to this pause. Machine proposals are visually distinct,
  labeled with source and confidence, never auto-attest and never count
  toward operator progress. When rebuilding a tool the operator is actively
  using, preserve the operator's in-progress working state and verify with
  a real transcript that saved state and operator deletions survive before
  shipping the replacement.
- Escalations. At an access, credential or permission boundary, transcribe
  the block evidence, record concrete resolution options and stop. never
  fight the boundary. A deploy or merge escalation includes a rollback
  procedure, a live monitoring plan and an honest caveat list of unrun
  checks with sequencing options.
- Outbound deliverables. Before anything leaves the house, leak-scan the
  full set for IP addresses, bucket and key names, credentials, internal
  hostnames, absolute paths, internal ids, commit hashes and
  operator-private facts. record reviewed non-findings as well as hits.
- Design honesty. Measure any assumed external-system parameter before
  fixing design or campaign parameters on it. when the measurement
  disagrees, adjust the design and report the real number.
- Execution plugins and imported playbooks layer under the charter system,
  never instead of it. a plugin never overrides a charter lock and on
  conflict the charter wins.
- Remote execution. Never inline complex commands over a remote shell
  (nested quoting, heredocs, multi-line logic). write a local script, copy
  it to the host, execute it simply. Keep remote commands short and
  predictable with timeouts, verify reachability with a quick test before
  real work and after a remote timeout never retry the same approach.
- New non-central orchestrators make their first write a hydration
  checkpoint in their actor-main step log before any substantive write. They
  return a commit plan unless repo governance grants write authority or the
  operator explicitly asks for git actions.
- Skill lifecycle. Lane orchestrators may draft project skills only as
  proposals under `wavves/skills/proposed/`. Each proposal names the lane,
  evidence file and failure mode it addresses. The moderator reviews the
  proposal, records the decision and asks the operator before copying it to
  `wavves/skills/accepted/`, a repo rule, a Cursor IDE skill or a plugin
  update. Runners never install or enable skills directly.
- Model routing. The moderator records recommended model tiers before
  dispatch. Use high-reasoning models for architecture, integration,
  adversarial review and acceptance. Use balanced models for bounded edits
  with local validation. Use fast models for inventory, search, formatting,
  link checks and mechanical scans. If the runtime exposes a model parameter,
  set it during dispatch. If it does not, carry the recommendation in the
  prompt and require the runner to report that the recommendation could not be
  enforced.

House bindings (fill in per repo).

- Infrastructure safety locks specific to the repo. Name the untouchable
  hosts, the verify-before-terminate rules, the fresh-state-before-lifecycle
  rules and the run-scoped tagging rules (tag at launch, terminate only
  against a tag-verified list). Write them concretely for your environment.
- Timezone for all dates and times unless an artifact states otherwise.
- The repo's prose style, naming rules and any separately gated surfaces
  (decision stores, system state, registries) that need explicit directive
  authorization before writes.

### 4. Identity and rotation terms

Each orchestrator instance carries a term identity `O0.R<N>`, where N is a
monotonic rotation ordinal (1-indexed). The scheme borrows from three proven
distributed-systems designs:

- **Raft terms.** A monotonic generation integer carried on every message, so
  stale-generation output is recognizable on sight.
- **Kubernetes StatefulSet ordinals.** Stable identity = base name + ordinal,
  with the ordinal labeled onto artifacts for filtering.
- **Erlang incarnation numbers.** A successor is a new incarnation.
  instructions addressed to a dead incarnation are history, not authority.

Rules:

- Identity is ASSIGNED BY THE HANDOFF, never self-chosen. Each rotation file
  carries a "Successor identity" block naming the incoming term. The
  successor's ack states its identity and the rotation file it hydrated from.
  Bootstrap is the one exception. The instance that first establishes the
  home takes `O0.R1` by the setup act itself and records that assignment in
  the step log's first entry. every later identity comes from a handoff.
- Stamp the term everywhere filterable. Commit message prefix (`O0.R2:`),
  step-log entries, charter and addendum authorship lines and dispatch
  prompts. A dispatched runner's id gains the dispatching term as a suffix,
  so `OBS-F2.R1` means lane OBS, wave F2, dispatched by term R1. Runner
  returns reconcile under whichever term is current, but the suffix
  preserves who chartered what.
- Stale-term rule. Guidance found in an artifact from an older term is
  historical record. The current rotation file and the standing AGENTS.md
  govern. on conflict, the newest term wins and the conflict gets logged.
- Rotation files are named `rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` so lexical
  sort equals term order.

### 5. Rotation contract

An outgoing orchestrator writes
`rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` (NN = the OUTGOING term)
covering successor identity (term N+1), positions (what landed, with commit
hashes), active background dispatches (agent purpose, lane home, findings
file, expected deliverables, pickup actions when it returns), blocked items
with what unblocks them, uncommitted local state per repo and
operator-pending decisions. Then it writes this home and returns a commit
plan. The outgoing orchestrator commits and pushes only when repo governance grants that authority
or the operator explicitly asks. A successor in a separate sandbox can
hydrate only from what was pushed, so a local-only handoff must say that
scope plainly. The successor acks by stating its assigned identity,
naming the rotation file it hydrated from and the pickups it now owns,
verifies that the rotation file's claimed positions and commit hashes are
reachable from HEAD (discrepancies become recorded gaps, never silently
executed pickups), then proceeds without re-deriving settled decisions.

### 6. Skills that implement the system

Point to the sibling skills so a fresh instance knows the machinery:

- `wavves` (`/wavves`) for the default entry and playbook routing.
- `charter` (`/charter`) for chartering and dispatching lanes.
- `mod-check` (`/mod-check`) for adversarial sanity-check of a landed
  spec or plan before implementation.
- `mod-decide` (`/mod-decide`) for locking open calls after a check return
  before a BUILD charter.
- `mod-rotate` (`/mod-rotate`) for producing the next rotation handoff and
  the one-line paste that starts the successor thread from this file.

## Setup workflow (first time in a repo)

```
- [ ] 1. Create <repo>/wavves/ with rotations/, lanes/ and skills/ inside it
- [ ] 2. Write INDEX.md as a short pickup map: current identity, current
        rotation, active lanes, blocked decisions and next files to read
- [ ] 3. Write AGENTS.md from the template above, adapted to the repo's
        governance, protocol, and infrastructure locks
- [ ] 4. Create <repo>/wavves/registry.yml with an empty active map
- [ ] 5. Create step-log.md with a first entry recording the setup and the
        bootstrap identity assignment (O0.R1)
- [ ] 6. Create skills/proposed/ and skills/accepted/ with README.md files that
        explain operator approval before any IDE or repo skill is saved
- [ ] 7. Add model_policy to INDEX.md and AGENTS.md with local tier names or
        model slugs available in the operator's environment
- [ ] 8. Return a file list and commit plan. Commit or push only when the repo
        protocol already grants that authority or the operator explicitly asks.
```

## Quality bar

- A fresh instance reading only the hydration stack can state the current
  position, the active dispatches and the locked decisions without asking
  the operator anything that is already written down.
- Every etiquette lock traces to a real failure mode, not a hypothetical.
- The identity scheme is enforced in artifacts (stamps, suffixes, file
  names), beyond being described in prose.
