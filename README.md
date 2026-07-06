# wavves

Run agent campaigns overnight and trust the morning report, because
acceptance is a measured check with its evidence saved to disk.

wavves is charter-driven orchestration for long-running, multi-agent work. It
is a set of three skills that let a single operator run parallel campaigns of
AI agents while state survives context limits, chat threads stay out of the
critical path, and claims arrive with evidence on disk.

The core ideas:

- **Charters, not chat.** Every campaign (a "lane") gets a home directory
  with a charter that carries the operator's intent, the grounded facts, and
  the locked decisions an unprimed agent would get wrong.
- **Waves of parallel subagents.** A dispatched sub-orchestrator runs bounded
  waves (discovery, build, integrate, accept) with strict file-ownership
  discipline, while the operator-facing thread stays unblocked.
- **Runnable adversarial gates.** Acceptance is a measured number captured to
  disk by an independent evaluator, never an assertion. Failed gates are
  reported as failed, with capped remediation loops.
- **Rotation with term identity.** When a thread gets heavy, the orchestrator
  hands off to a fresh one via a rotation file that assigns the successor a
  monotonic term identity (a design borrowed from Raft terms, Kubernetes
  StatefulSet ordinals, and Erlang incarnation numbers), so stale instructions
  are recognizable and provenance survives.
- **A standing home.** Any fresh instance hydrates from files (a home
  contract, a rotations directory, a waves registry, a step log), never from
  transcripts.

wavves is a community plugin by aimez. It is not affiliated with or endorsed
by Cursor.

## Installation

From the Cursor plugin marketplace (once listed):

```
/add-plugin wavves
```

Or install locally by copying this directory to:

```
~/.cursor/plugins/local/wavves/
```

## Quickstart

1. **Set up the home** (once per repo). Ask your agent to follow the
   `orchestrator-home` skill. It creates `<repo>/.cca/catalogue/O0/` with a
   standing `AGENTS.md` hydration contract, a `rotations/` directory, a waves
   registry, and a step log.
2. **Charter your first lane.** Ask for a waveset (for example "charter a
   waveset to fix the checkout flow's reliability"). The
   `waveset-orchestration` skill writes the lane home (charter, dispatch
   prompt, README), registers the lane, and dispatches a background
   sub-orchestrator that runs the waves and reports back.
3. **Let gates gate.** Adversarial and acceptance waves run as executable
   checks with evidence captured to the lane home `gate_captures/`. Approve
   gated waves (integration, deployment) explicitly when the orchestrator
   asks.
4. **Rotate when heavy.** When the thread slows down or context runs long,
   ask to rotate. The `orchestrator-rotation` skill writes a rotation file
   that assigns the successor's term identity and emits a one-line paste to
   start the fresh thread.

## Components

### Skills

| Skill | Description |
|:------|:------------|
| `waveset-orchestration` | Charter a lane and dispatch a sub-orchestrator that runs waves of parallel subagents behind runnable gates. Includes EXECUTION_WIRING.md (how gates are run at execution time) and a generic transition-gap probe script. |
| `orchestrator-rotation` | Hand the orchestrator (or one lane) to a fresh thread with full hydration, assigned term identity, and a one-line paste. |
| `orchestrator-home` | Establish the standing home file, registry, and rotation contract a fresh instance hydrates from. |

## Worked example

[examples/friend-worked-example.md](examples/friend-worked-example.md) walks
through one real installation (building friend, a city-scale evidence model)
with three campaigns and the first rotation, quoting the real findings files.
It is an example, not a default; the skills contain no paths from it.

## Read more

- Launch article on aimez, the story of one night's campaigns under these
  contracts, including a caught false completion.
  [ARTICLE LINK PLACEHOLDER, added at publish time]
- Whitepaper, the method written up with its distributed-systems grounding,
  full evidence tables, and stated limits.
  [WHITEPAPER LINK PLACEHOLDER, added at publish time]

## License

MIT
