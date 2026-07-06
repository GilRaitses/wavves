---
name: orchestrator-home
description: >-
  Establish and maintain a standing home file for a central orchestrator so
  ANY fresh instance (rotation, replay, or recovery) hydrates from files
  instead of chat transcripts. Use when setting up charter-driven multi-agent
  work in a repo for the first time, when an orchestrator needs a durable
  hydration entry point, or when defining term identity and rotation rules for
  successive orchestrator instances. Produces <repo>/.cca/catalogue/O0/AGENTS.md
  (the standing contract), a rotations/ directory, a waves registry, and a
  step log.
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
   naming rules) if one exists.
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
  when a dispatch fits, and never blocks polling a dispatch.
- Dispatched orchestrators/runners run waves, write findings incrementally
  into their lane home, never run git write operations, and never solicit the
  operator directly (escalation returns to O0).
- Wave subagents take one bounded disjoint task each, with no shared-file
  collisions.

### 3. Etiquette locks (carried into every charter and dispatch)

Adapt this list to the repo; the pattern is that each lock encodes a failure
someone hit in real work.

- Honesty. Modeled-not-measured labeling, no reassurance bias, failed gates
  reported as failed, evidence transcribed not asserted. Visual claims
  require looking at the rendered output before claiming done.
- Adversarial gates. Independent evaluator, runnable checks, evidence to the
  lane home `gate_captures/`, capped remediation loops, then escalate.
- Prose gates for operator-facing writing, whatever house style the operator
  enforces.
- Git. Runners never commit; the orchestrator commits per the repo protocol.
  Artifacts never embed their own landing commit (a self-referential hash
  loop); report the landing commit in the completion message instead.
- Judgment calls that belong to the operator are NEVER inferred by agents.
- Infrastructure safety locks specific to the repo. Name the untouchable
  hosts, the verify-before-terminate rules, the fresh-state-before-lifecycle
  rules. Write them concretely for your environment.
- Timezone for all dates and times unless an artifact states otherwise.

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
operator-pending decisions. Then it commits and pushes this home if the repo
protocol allows. The successor acks by stating its assigned identity, naming
the rotation file it hydrated from, and the pickups it now owns, then
proceeds without re-deriving settled decisions.

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
- [ ] 4. Create STEP_LOG.md with a first entry recording the setup
- [ ] 5. Commit per the repo protocol
```

## Quality bar

- A fresh instance reading only the hydration stack can state the current
  position, the active dispatches, and the locked decisions without asking
  the operator anything that is already written down.
- Every etiquette lock traces to a real failure mode, not a hypothetical.
- The identity scheme is enforced in artifacts (stamps, suffixes, file
  names), beyond being described in prose.
