---
name: orchestrator-home
description: >-
  Establish and maintain a standing home file for a central orchestrator so
  ANY fresh instance (rotation, replay, or recovery) hydrates from files
  instead of chat transcripts. Use when setting up the moderator layer for
  managed distributed sessions, when an orchestrator needs a durable hydration
  entry point, or when defining term identity and rotation rules for successive
  orchestrator instances. Produces <repo>/.cca/catalogue/O0/AGENTS.md (the
  standing contract), a rotations/ directory, a waves registry and a step log.
---

# Orchestrator Home

A standing hydration contract that outlives any single chat thread. The home
is a directory (convention `<repo>/.cca/catalogue/O0/`) whose `AGENTS.md` is
the entry point every fresh orchestrator instance reads first. Per-rotation
state lives in `rotations/`; the standing file only points.

Write the home ONCE per repo, then let rotations reuse it. Do not restate its
contents in every rotation file.

## What the standing AGENTS.md contains

Use this template, adapted to the repo. Every section below earns its place
by preventing a specific fresh-instance failure.

### 1. Hydration stack (read in this order)

1. The repo's own governance doc (surfaces, write policy, commit protocol,
   naming rules) if one exists. When none exists, the default policy applies
   until the operator supplies one. Writes stay confined to the home
   directory, lane homes, and the registry; commits land on the default
   branch with descriptive messages; everything else is read-only.
2. `rotations/` in the home directory. Rotation handoffs, one file per
   rotation, datestamped. THE NEWEST FILE IS THE CURRENT POSITION, naming
   active dispatches, pending pickups, blocked items, and uncommitted state.
3. The waves registry (`<repo>/.cca/waves.registry.yml` or equivalent). Every
   chartered lane, status, and home path. The registry note per lane is the
   compressed authority; the lane home's WAVESET_CHARTER.md is the full
   authority.
4. The lane homes named by the current rotation file.
5. `STEP_LOG.md` in the home directory, the orchestrator's synthesis trace
   (append, never rewrite).

State explicitly that agents hydrate from these files and never read chat
transcripts linearly. Transcripts are for keyword search only, and only when a
rotation file cites one.

### 2. The three roles (never collapse)

- The central orchestrator (O0) is operator-facing. It charters lanes,
  dispatches sub-orchestrators in the background, reconciles returns, and
  handles commits per the repo protocol. It never executes lane work inline
  when a dispatch fits, and never blocks polling a dispatch. Reconciling is
  verification. Before landing a return it spot-checks the evidence, and it
  refreshes derived outputs against canonical inputs that moved during the
  dispatch, recording the refresh.
- Dispatched orchestrators/runners run waves, write findings incrementally
  into their lane home, never run git write operations, and never solicit the
  operator directly (escalation returns to O0).
- Wave subagents take one bounded disjoint task each, with no shared-file
  collisions.

### 3. Etiquette locks (carried into every charter and dispatch)

The list has two kinds of entries. Portable locks travel as written and are
the mandatory core of the contract; trimming them at setup gutters the home,
because each one encodes a failure someone hit in real work. House bindings
are the slots the installing house fills in concretely (hosts, stores,
styles); any values shown for them are examples, never defaults.

Portable locks.

- Honesty. Modeled-not-measured labeling, no reassurance bias, failed gates
  reported as failed, evidence transcribed not asserted. Visual claims
  require looking at the rendered output before claiming done. Missing or
  unresolved artifacts are recorded explicitly, never inferred or
  fabricated; unprocessable items get gap entries with reasons, and count
  shrinkage is stated plainly.
- Anomalies. Check the actual values against baselines before calling a
  warning benign; a warning that recurs across runs is systematic until
  proven otherwise; state the worst-case interpretation first; say plainly
  when you do not know, and require a citable source before calling a
  behavior expected or safe. Never promise background monitoring, polling,
  or timers an agent cannot perform.
- Completions. Never trust a completion that arrives implausibly fast or
  with implausibly low output volume; verify throughput and output counts
  against expectations, and when a defect invalidated earlier output,
  re-run the full pass and overwrite the poisoned artifacts. Record mid-run
  defects, their fixes, and their cost in the findings even when fully
  remediated.
- Reporting. Report the full result distribution alongside any gate
  statistic; scope headline claims to the measured sample size and
  conditions; state the unit, resolution, and quality limits of derived
  metrics where quoted, and label cross-domain analogies as analogies.
  Claims in derived documents trace to findings files, quotations verbatim;
  mechanisms, attributions, timings, and scopes are never invented or
  shifted. Returns carry only the requested fields, with no added
  restructuring.
- Adversarial gates. Independent evaluator with no authorship of the work
  under review, runnable checks, evidence to the lane home `gate_captures/`,
  capped remediation loops, then escalate. Verdicts carry named failures; a
  pass may carry a named deployment-blocking condition that must clear
  before any deploy escalation.
- Prose gates for operator-facing writing, whatever house style the operator
  enforces.
- Git. Runners never commit; the orchestrator commits per the repo protocol
  and treats the work as incomplete until the push is verified. Local-only
  or staged-only state is never completion; no feature branches unless
  explicitly authorized; no delayed batching for file-changing passes.
  Artifacts never embed their own landing commit (a self-referential hash
  loop); report the landing commit in the completion message instead.
  Runner findings end with an explicit commit file list for the
  orchestrator, exclusions stated (bulky derived artifacts stay out when a
  durable store holds the canonical copy), plus a plain no-git statement.
- Git concurrency. Record the dispatch base commit; if HEAD moves
  mid-dispatch, report both hashes, reconcile the edits onto the new HEAD,
  and point evaluators at the new HEAD. Never land commits on a branch a
  dispatched agent is actively editing (freeze or coordinate). A
  remote-rejected push resolves by fetch, then rebase with autostash, then
  push, never force-push; before rebasing, confirm no other active agent
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
  to shared repo state before cross-actor use; an unpublished artifact is
  local-only and never crosses actors. An actor reading an artifact landed
  by another actor first syncs to the commit that landed it. Dispatch
  prompts declare whether outputs are local-only or shared review
  artifacts. Live repo state governs over any cached or bundled copy.
- Judgment calls that belong to the operator are NEVER inferred by agents.
  Operator-gated actions (attestation, gated mutations, destructive steps)
  always pause for the operator; any never-block-on-the-human execution
  principle yields to this pause. Machine proposals are visually distinct,
  labeled with source and confidence, never auto-attest, and never count
  toward operator progress. When rebuilding a tool the operator is actively
  using, preserve the operator's in-progress working state and verify with
  a real transcript that saved state and operator deletions survive before
  shipping the replacement.
- Escalations. At an access, credential, or permission boundary, transcribe
  the block evidence, record concrete resolution options, and stop; never
  fight the boundary. A deploy or merge escalation includes a rollback
  procedure, a live monitoring plan, and an honest caveat list of unrun
  checks with sequencing options.
- Outbound deliverables. Before anything leaves the house, leak-scan the
  full set for IP addresses, bucket and key names, credentials, internal
  hostnames, absolute paths, internal ids, commit hashes, and
  operator-private facts; record reviewed non-findings as well as hits.
- Design honesty. Measure any assumed external-system parameter before
  fixing design or campaign parameters on it; when the measurement
  disagrees, adjust the design and report the real number.
- Execution plugins and imported playbooks layer under the charter system,
  never instead of it; a plugin never overrides a charter lock, and on
  conflict the charter wins.
- Remote execution. Never inline complex commands over a remote shell
  (nested quoting, heredocs, multi-line logic); write a local script, copy
  it to the host, execute it simply. Keep remote commands short and
  predictable with timeouts, verify reachability with a quick test before
  real work, and after a remote timeout never retry the same approach.
- New non-central orchestrators make their first write a hydration
  checkpoint in their actor-main step log, then sync and push, before any
  substantive write.

House bindings (fill in per repo).

- Infrastructure safety locks specific to the repo. Name the untouchable
  hosts, the verify-before-terminate rules, the fresh-state-before-lifecycle
  rules, and the run-scoped tagging rules (tag at launch, terminate only
  against a tag-verified list). Write them concretely for your environment.
- Timezone for all dates and times unless an artifact states otherwise.
- The repo's prose style, naming rules, and any separately gated surfaces
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
- **Erlang incarnation numbers.** A successor is a new incarnation;
  instructions addressed to a dead incarnation are history, not authority.

Rules:

- Identity is ASSIGNED BY THE HANDOFF, never self-chosen. Each rotation file
  carries a "Successor identity" block naming the incoming term. The
  successor's ack states its identity and the rotation file it hydrated from.
  Bootstrap is the one exception. The instance that first establishes the
  home takes `O0.R1` by the setup act itself and records that assignment in
  the step log's first entry; every later identity comes from a handoff.
- Stamp the term everywhere filterable. Commit message prefix (`O0.R2:`),
  step-log entries, charter and addendum authorship lines, and dispatch
  prompts. A dispatched runner's id gains the dispatching term as a suffix,
  so `OBS-F2.R1` means lane OBS, wave F2, dispatched by term R1. Runner
  completions reconcile under whichever term is current, but the suffix
  preserves who chartered what.
- Stale-term rule. Guidance found in an artifact from an older term is
  historical record. The current rotation file and the standing AGENTS.md
  govern; on conflict, the newest term wins and the conflict gets logged.
- Rotation files are named `ROTATION_R<NN>_<YYYYMMDD>_<HHMM>.md` so lexical
  sort equals term order.

### 5. Rotation contract

An outgoing orchestrator writes
`rotations/ROTATION_R<NN>_<YYYYMMDD>_<HHMM>.md` (NN = the OUTGOING term)
covering successor identity (term N+1), positions (what landed, with commit
hashes), active background dispatches (agent purpose, lane home, findings
file, expected deliverables, pickup actions on completion), blocked items
with what unblocks them, uncommitted local state per repo, and
operator-pending decisions. Then it commits and pushes this home before the
term ends, following the repo protocol where one exists and the default
policy where none does; a successor in a separate sandbox can hydrate only
from what was pushed. The successor acks by stating its assigned identity,
naming the rotation file it hydrated from, and the pickups it now owns,
verifies that the rotation file's claimed positions and commit hashes are
reachable from HEAD (discrepancies become recorded gaps, never silently
executed pickups), then proceeds without re-deriving settled decisions.

### 6. Skills that implement the system

Point to the sibling skills so a fresh instance knows the machinery:

- `waveset-orchestration` for chartering and dispatching lanes.
- `orchestrator-rotation` for producing the next rotation handoff and the
  one-line paste that starts the successor thread from this file.

## Setup workflow (first time in a repo)

```
- [ ] 1. Create <repo>/.cca/catalogue/O0/ and rotations/ inside it
- [ ] 2. Write AGENTS.md from the template above, adapted to the repo's
        governance, protocol, and infrastructure locks
- [ ] 3. Create <repo>/.cca/waves.registry.yml with an empty active map
- [ ] 4. Create STEP_LOG.md with a first entry recording the setup and the
        bootstrap identity assignment (O0.R1)
- [ ] 5. Commit per the repo protocol, or per the default policy in section 1
        when the repo has none
```

## Quality bar

- A fresh instance reading only the hydration stack can state the current
  position, the active dispatches, and the locked decisions without asking
  the operator anything that is already written down.
- Every etiquette lock traces to a real failure mode, not a hypothetical.
- The identity scheme is enforced in artifacts (stamps, suffixes, file
  names), beyond being described in prose.
