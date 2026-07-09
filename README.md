# wavves

Version: `0.0.0`.

Route durable multi-agent work through a moderator layer, with alignment
packets, check records and handoff files saved beside the work.

wavves is a free Cursor plugin for managed distributed sessions. Four skills
help a single operator prepare bounded work, dispatch parallel runners and
rotate overloaded threads while the shared record lives in files instead of
chat history.

The core ideas:

- **Alignment packets.** Each lane gets a home directory with scope, grounded
  facts, locked decisions, file boundaries and acceptance checks.
- **Bounded waves.** A dispatched sub-orchestrator runs focused waves of
  parallel subagents with strict file ownership while the operator-facing
  thread stays small.
- **Check records.** Acceptance comes from a measured check captured to disk
  by an independent evaluator. Failed gates are reported as failed, with
  capped remediation loops.
- **Rotation with term identity.** When a thread gets heavy, the orchestrator
  hands off to a fresh one via a rotation file that assigns the successor a
  monotonic term identity (a design borrowed from Raft terms, Kubernetes
  StatefulSet ordinals and Erlang incarnation numbers), so stale instructions
  are recognizable and provenance survives.
- **A standing home.** Any fresh instance hydrates from files (an index, a home
  contract, a rotations directory, a registry, a step log), never from
  transcripts.
- **Model routing.** Charters record recommended model tiers for the
  sub-orchestrator and each wave, so expensive reasoning is reserved for work
  that needs it and scan-heavy or mechanical work can run on faster models.

wavves is a community plugin by aimez and is not affiliated with or endorsed
by Cursor.

## Installation

From the Cursor plugin marketplace after listing:

```
/add-plugin wavves
```

Or install locally by copying this directory to:

```
~/.cursor/plugins/local/wavves/
```

Copy the plugin contents, not the `.git` directory. A release directory or a
plain copy of `.cursor-plugin/`, `skills/`, `examples/`, `README.md` and
`LICENSE` is the safest local install path.

## Safety defaults

wavves writes its own working records under `wavves/` by default. An
existing root `AGENTS.md` is treated as repo governance and is not overwritten.
Setup and lane preparation do not commit, push, deploy or mutate external
services unless the operator explicitly asks for that action or the repo
governance says wavves owns those writes.

## Usage

Type `/wavves` at the start of a task. It reads your request, checks the home,
picks a playbook and runs the leaf skill. Like `/poteto-mode` in pstack.

### just use `/wavves`

| playbook | for |
|:---------|:----|
| bootstrap | first time in repo, repair home, no `wavves/` yet |
| charter-lane | bounded work: bug fix, audit, refactor, flaky CI, overnight lane |
| rotate | hand off to a fresh moderator thread |
| pickup | resume from rotation paste, "where are we", reconcile active lanes |

### What wavves tracks

| Piece | Where it lives | What it is |
|:------|:---------------|:-----------|
| **Moderator (O0)** | the operator-facing thread | charters lanes, dispatches background work, reconciles returns |
| **Home** | `<repo>/wavves/` | standing hydration contract that outlives any one chat |
| **Lane** | `wavves/lanes/<date>_<label>/` | one bounded workstream with its own charter and findings |
| **Charter** | `lanes/.../waveset.md` | alignment packet: scope, locked decisions, waves, gates |
| **Registry** | `wavves/registry.yml` | map of every chartered lane and its status |
| **Rotation** | `wavves/rotations/` | handoff files with term identity (`O0.R1`, `O0.R2`, ...) |
| **Gates** | `lanes/.../gate-captures/` | runnable checks with JSON + log evidence on disk |

Fresh instances hydrate from the home files, never from chat transcripts.

### Skills

| skill | use it when |
|:------|:------------|
| `/wavves` | default entry. routes to bootstrap, charter, rotate or pickup |
| `/wavve` | you only need home setup |
| `/charter` | you only need a new lane chartered |
| `/mod-rotate` | you only need rotation |

Most operators type `/wavves` plus the task. Reach for the leaf skills when you
know exactly which step you need.

### examples

```text
default:           /wavves set up in this repo, then audit our README for drift.
                   read-only, no commits.
bug fix:           /wavves our checkout webhook sometimes creates duplicate
                   invoices. reproduce, fix and verify with gate captures.
flaky ci:          /wavves three integration tests flake on main. fix root causes
                   and prove stability.
overnight:         /wavves i'm stepping away. land the auth hardening lane with
                   captured gates. no deploy without my approval.
rotate:            /wavves rotate this thread. write a handoff for active lanes.
pickup:            /wavves hydrate from the rotation paste and tell me what's active.
setup only:        /wavve set up wavves in this repo. do not commit.
charter only:      /charter migrate every callsite to the async config store.
rotate only:       /mod-rotate token velocity is too high. give me the one-line paste.
```

Four full worked examples (parallel feature build, flaky test stabilization,
a performance sprint and a migration that survives a mid-flight rotation):
[examples/usage.md](examples/usage.md).

### What each skill does

1. **`/wavves`** matches a playbook, reads the leaf skill and executes. If the
   home is missing, bootstrap runs first.
2. **`/wavve`** creates `<repo>/wavves/` with `INDEX.md`, `AGENTS.md`,
   `registry.yml`, `step-log.md` and `rotations/`.
3. **`/charter`** writes the lane home, registers the lane and dispatches a
   background sub-orchestrator with runnable gates in `gate-captures/`.
4. **`/mod-rotate`** writes a rotation file with term identity and emits a
   one-line paste for a fresh thread.

`/wavves` pairs well with Cursor's `/loop` for long lanes with captured gates
instead of chat memory.

## Project layout

Default new-repo layout:

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
      waveset.md
      dispatch.md
      README.md
      findings/
      gate-captures/
      decisions/
  skills/
    proposed/
    accepted/
```

`INDEX.md` is the fast pickup surface, pointing a fresh moderator to the
current rotation file, active lanes, blocked decisions and next files to read.
`AGENTS.md` is the stable contract. `registry.yml` is the lane map.
`step-log.md` is append-only. Lane files carry the detailed work.

## Moderator and skill flow

The moderator owns `wavves/INDEX.md`, `wavves/registry.yml` and
`wavves/step-log.md`. Lane orchestrators own their lane homes under
`wavves/lanes/` and return proposed project skills when a repeated local
practice appears.

Project skills are drafts first. A lane may write a proposal under
`wavves/skills/proposed/`, with the evidence and lane that justified it. The
moderator reviews the proposal and asks the operator before saving it as a
repo skill, Cursor IDE skill or plugin update. Runners never install skills
directly.

## Model and Cost Discipline

Each `waveset.md` includes a model routing table. The table records the
moderator's recommended model tier for the lane orchestrator and for each wave:

```text
role                  model tier        reason
lane orchestrator     high-reasoning    cross-file planning and gate design
discovery runners     fast              broad search, summaries, inventory
build runners         balanced          bounded edits with local validation
adversarial gate      high-reasoning    defect finding and risk judgment
acceptance gate       high-reasoning    final verification and caveat review
```

When the environment exposes a model parameter for subagents, the moderator
sets that parameter at dispatch time. If the environment does not expose one,
the dispatch prompt still carries the recommendation so the receiving agent can
report the mismatch.

The table is a cost-control surface, not a measured savings claim. Cost is
auditable when the charter records runner count, expected file reads, expected
gate cost and model tier before execution. A later accounting pass can compare planned
tiers with actual token or billing records when the environment exposes them.

## Manual harness inspection

Gate evidence lives beside the lane:

```text
wavves/lanes/YYYYMMDD_lane-label/
  gate-captures/
    <gate>.json
    <gate>.log
```

Inspect a gate by opening the JSON summary, reading the paired log and checking
the verdict in `findings/` against both files. A hand-written summary is not a
gate capture. The command that produced each capture should be named in the
finding so another operator can rerun it.

## Components

### Skills

| Skill | Description |
|:------|:------------|
| `wavves` (`/wavves`) | Main entry. Routes to bootstrap, charter, rotate or pickup playbooks. |
| `wavve` (`/wavve`) | Bootstrap the standing home a fresh moderator hydrates from. |
| `charter` (`/charter`) | Charter a lane and dispatch waves behind runnable gates. |
| `mod-rotate` (`/mod-rotate`) | Hand the moderator or one lane to a fresh thread. |

## Examples on disk

[examples/usage.md](examples/usage.md) has quick-reference prompts plus four
full worked walkthroughs, each demonstrating a different mechanic: parallel
file ownership on a feature build, measured before/after gates on a flaky
test fix, model routing on a performance sprint, and a rotation mid-migration
with a verified handoff. The paths and metrics in those examples are
fictional. The skills ship no hard-coded paths from any particular project.

## Read more

The launch article and companion whitepaper are omitted here until public URLs
exist.

## License

MIT
