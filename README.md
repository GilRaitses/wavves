# wavves

Route durable multi-agent work through a moderator layer, with alignment
packets, check records and handoff files saved beside the work.

wavves is a free Cursor plugin for managed distributed sessions. Its three
skills help a single operator prepare bounded work, dispatch parallel runners
and rotate overloaded threads while the shared record lives in files instead
of chat history.

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
- **A standing home.** Any fresh instance hydrates from files (a home
  contract, a rotations directory, a waves registry, a step log), never from
  transcripts.

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

wavves writes its own working records under `.cca/` by default. An
existing root `AGENTS.md` is treated as repo governance and is not overwritten.
Setup and lane preparation do not commit, push, deploy or mutate external
services unless the operator explicitly asks for that action or the repo
governance says wavves owns those writes.

## Quickstart

1. **Set up the home** (once per repo). Ask your agent to follow the
   `orchestrator-home` skill. The skill creates `<repo>/.cca/catalogue/O0/`
   with a standing `AGENTS.md` hydration contract, a `rotations/` directory,
   a waves registry and a step log.
2. **Prepare your first lane.** Ask for a waveset, such as "set up a waveset
   to fix the checkout flow's reliability". The `waveset-orchestration` skill
   writes the lane home, alignment packet, dispatch prompt and README, then
   registers the lane and dispatches a background sub-orchestrator.
3. **Let gates gate.** Adversarial and acceptance waves run as executable
   checks with evidence captured to the lane home `gate_captures/`. Approve
   gated waves (integration, deployment) explicitly when the orchestrator
   asks.
4. **Rotate when heavy.** When the thread slows down or context runs long,
   ask to rotate. The `orchestrator-rotation` skill writes a rotation file
   that assigns the successor's term identity and emits a one-line paste to
   start the fresh thread.

Safe first prompt:

```
Set up wavves in this repo, then prepare a read-only waveset to audit my README. Do not commit.
```

## Components

### Skills

| Skill | Description |
|:------|:------------|
| `waveset-orchestration` | Build a lane alignment packet and dispatch a sub-orchestrator that runs waves of parallel subagents behind runnable gates. Includes EXECUTION_WIRING.md and a generic transition-gap probe script. |
| `orchestrator-rotation` | Hand the orchestrator or one lane to a fresh thread with full hydration, assigned term identity and a one-line paste. |
| `orchestrator-home` | Establish the standing home file, registry and rotation contract a fresh instance hydrates from. |

## Worked example

[examples/friend-worked-example.md](examples/friend-worked-example.md) walks
through one real installation (building friend, a city-scale evidence model)
with three lanes and the first rotation, quoting the real findings files.
The example is not a default. The skills contain no paths from it.

## Read more

The launch article and companion whitepaper are omitted here until public URLs
exist.

## License

MIT
