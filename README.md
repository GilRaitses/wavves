# wavves

Version: `0.4.1`.

Route durable multi-agent work through a moderator layer, with alignment
packets, disk gate captures and handoff files saved beside the work.

wavves is a free Cursor plugin for managed distributed sessions. Skills help
a single operator prepare bounded work, dispatch parallel runners and rotate
overloaded threads while the shared record lives in files on disk.

The core ideas:

- **Alignment packets.** Each lane gets a home directory with scope, grounded
  facts, locked decisions, file boundaries and acceptance checks.
- **Bounded waves.** O0 background-dispatches a **wave orchestrator** that
  fans out **charge workers** (one Task per charge) with strict file
  ownership while the operator-facing thread stays small.
- **Disk gate captures.** A lane advances after a runnable harness writes
  pass or block evidence under `gate-captures/`, graded by someone who did
  not author the work under review. Failed gates are reported as failed,
  with capped remediation loops.
- **Proof-before-accept.** Product lanes declare a named proof job;
  process-only ACCEPT cannot clear when `proof_required: yes`.
- **Paragraph tunnel.** Mid-render structural gate for one outbound field
  (adversarial + capped rewrite + mechanical fixtures), not a voice-clone.
- **Rotation with term identity.** When a thread gets heavy, the orchestrator
  hands off to a fresh one via a rotation file that assigns the successor a
  monotonic term identity (`O0.R<N>`). The naming uses **analogies** to Raft
  terms, Kubernetes StatefulSet ordinals and Erlang incarnation numbers (not
  protocol isomorphisms): house fences are handoff files, stamps and etiquette.
- **A standing home.** Any fresh instance hydrates from files (an index, a home
  contract, a rotations directory, a registry, a step log), never from
  transcripts.
- **Authority propagation.** After mod-decide, locks sync to `waveset.md`,
  `dispatch-w{N}.md` and the registry so W2+ runners do not re-litigate
  settled decisions. Scoped mod-check verdicts (`blocks_w2`…`blocks_w5`) and
  `/wavves proceed` execute ordered recommended actions.

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
| check | adversarial sanity-check of a landed spec or plan before build |
| decide | lock open product/design calls after a check return, before BUILD |
| layover | preflight a multi-repo desktop workspace (audit report; cloud stays per-repo) |
| paragraph-tunnel | mid-render structural gate for a named outbound paragraph |
| proof-before-accept | named proof job + host/blank-canvas checks before ACCEPT |
| rotate | hand off to a fresh moderator thread |
| pickup | resume from rotation paste, "where are we"; mandatory yield vs `return_to_O0` remasure |
| proceed | execute `recommended_actions` from a verdict (`proceed as recommended`); all-standing mode on closed phrases only |
| shrug | `/shrug` alias for emoji shrug; bare → AUTH-10 proceed; with closed all-standing phrase → proceed-all-standing |

### What wavves tracks

| Piece | Where it lives | What it is |
|:------|:---------------|:-----------|
| **O0** | the operator-facing thread | charters lanes, background-dispatches wave orchestrators, reconciles on notify, lands git; then `O0_release_window` |
| **wave orchestrator** | background Task under O0 | fans out charge workers; integrates; writes rollup+gate (or hard FAIL / operator_gate). No early `return_to_O0`. Yield requires `findings/<wave>-orch-checkpoint.md`; O0 same-turn remasures and resumes yield (not fail-remediation-only) |
| **charge worker** | one background Task per charge id | one bounded disjoint task; never git; never solicit the operator |
| **Home** | `<repo>/wavves/` | standing hydration contract that outlives any one chat |
| **Lane** | `wavves/lanes/<date>_<label>/` | one bounded workstream with its own charter and findings |
| **Charter** | `lanes/.../waveset.md` | alignment packet: scope, locked decisions, waves, gates |
| **Dispatch** | `lanes/.../dispatch-w{N}.md` | per-wave paste block; `active_dispatch` in registry |
| **Registry** | `wavves/registry.yml` | map of every chartered lane and its status |
| **Rotation** | `wavves/rotations/` | handoff files with term identity (`O0.R1`, `O0.R2`, ...) |
| **Gates** | `lanes/.../gate-captures/` | runnable checks with JSON + log evidence on disk |

Orchestration fail ids (skill text; append to `wavves/failure_log.yml` only
when observed in a real run): `PROC-ORCH-EARLY-EXIT`,
`PROC-ORCH-LAUNCH-AND-EXIT`, `PROC-ORCH-NO-RESUME-CONTRACT`,
`PROC-ORCH-SOLO-BUILD`, `PROC-ORCH-ROLE-COLLAPSE`, `PROC-ORCH-DEP-OVERCLAIM`,
`PROC-ORCH-FOREGROUND-HOLD`, `PROC-MOD-FOREGROUND-HOLD`,
`PROC-MOD-PROGRESS-THEATER`. Checker:
`python3 evals/check_wave_orchestrator_fanout.py`. Canonical Roles:
`skills/charter/SKILL.md`.

Fresh instances hydrate from the home files, never from chat transcripts.

### Skills

| skill | use it when |
|:------|:------------|
| `/wavves` | default entry. routes to bootstrap, charter, check, decide, layover, set-key, rotate, pickup, proceed or shrug |
| `/wavves-init` | you only need home setup |
| `/charter` | you only need a new lane chartered |
| `/mod-check` | you only need an adversarial spec/plan sanity-check wave |
| `/mod-decide` | you only need to lock open calls before a BUILD charter |
| `/layover` | you only need the workspace preflight audit |
| `/set-key` | open Terminal.app paste helper for a server-only env secret |
| `/shrug` | alias for emoji shrug; bare → AUTH-10 proceed; with closed all-standing phrase → proceed-all-standing |
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
spec check:        /mod-check review docs/superpowers/specs/2026-07-08-example.md
                   before we write the implementation plan. adversarial parallel
                   wave. read-only. landing_commit_hash <hash>.
decide:            /mod-decide navigate open calls from the check return.
                   one decision at a time. write decisions/*.md. no BUILD yet.
                   Mid-queue: answer Pick: … only. Do not re-slash each time.
layover:           /wavves preflight ~/my.code-workspace. read-only audit;
                   I will open one cloud agent myself afterward.
rotate:            /wavves rotate this thread. write a handoff for active lanes.
pickup:            /wavves hydrate from the rotation paste and tell me what's active.
proceed:           /wavves proceed as recommended after mod-check or mod-decide return.
all-standing:      /wavves proceed all standing
                   (or: all still standing / queue all standing and move)
shrug:             /shrug
                   (bare → AUTH-10 proceed; add a closed all-standing phrase to widen)
setup only:        /wavves-init set up wavves in this repo. Do not commit.
charter only:      /charter migrate every callsite to the async config store.
check only:        /mod-check the landed spec. GO / REVISE / BLOCK with named gaps.
decide only:       /mod-decide lock the open calls. emit Locked decisions paste.
layover only:      /layover audit ~/my.code-workspace. report untracked,
                   unpushed and stashed state per sibling repo.
set-key only:      /set-key open Terminal.app paste helper for klosr
                   GOOGLE_MAPS_API_KEY (never put the secret in chat).
rotate only:       /mod-rotate token velocity is too high. give me the one-line paste.
```

Spec → BUILD lifecycle (`/mod-check` → `/mod-decide` → `/charter`) plus four
worked examples: [examples/usage.md](examples/usage.md).

### What each skill does

1. **`/wavves`** matches a playbook, reads the leaf skill and executes. If the
   home is missing, bootstrap runs first.
2. **`/wavves-init`** creates `<repo>/wavves/` with `INDEX.md`, `AGENTS.md`,
   `registry.yml`, `step-log.md` and `rotations/`.
3. **`/charter`** writes the lane home, registers the lane and dispatches a
   background **wave orchestrator** with runnable gates in `gate-captures/`.
   Multi-repo lanes declare a `repos` table and commit plan; each dispatch
   carries an authority precedence block.
4. **`/mod-check`** charters a read-only adversarial wave against a landed
   spec or plan and returns a scoped verdict (`GO` / `REVISE` / `BLOCK`,
   `blocks_w2`…`blocks_w5`) with `recommended_actions`.
5. **`/mod-decide`** walks open product/design calls one at a time, writes
   `decisions/*.md`, syncs authority surfaces on completion and emits a
   Locked decisions paste for BUILD.
6. **`/layover`** reads a bespoke multi-root `.code-workspace` file (or an
   explicit folder list) and writes a read-only audit of every sibling
   repo's remotes, branch sync state, uncommitted changes, untracked files
   and stashes. Audit-only: one report file, never mutates an audited repo.
   Does not start cloud agents or autoconfigure wavves elsewhere.
7. **`/set-key`** opens Terminal.app with a paste-and-return helper that
   writes a server-only env secret (default klosr `GOOGLE_MAPS_API_KEY`).
   Never echoes the secret; remasures set/nchars only; reject leaves the
   env file unchanged.
8. **`/shrug`** is a thin alias for emoji shrug. Bare `/shrug` → AUTH-10
   proceed; with a closed all-standing phrase → proceed-all-standing.
9. **`/mod-rotate`** writes a rotation file with term identity and emits a
   one-line paste for a fresh thread.

`/wavves proceed` executes ordered `recommended_actions` from a verdict
(commit, dispatch, operator gates). Closed all-standing phrases
(`all still standing`, `queue all standing and move`, `proceed all standing`,
`/wavves proceed all standing`) route to proceed-all-standing. Bare shrug or
bare `/shrug` stays AUTH-10 proceed only. On orch
`yield_awaiting_children`, pickup / O0 same-turn remasures disk and resumes
(or treats rollup+gate as `return_to_O0`); fail-remediation-only is for true
fails.

`/wavves` pairs well with Cursor's `/loop` for long lanes with captured gates
on disk beside the lane home.

## Project layout

Default new-repo layout:

```text
wavves/
  INDEX.md
  AGENTS.md
  registry.yml
  step-log.md
  failure_log.yml
  rotations/
    rotation-r01-YYYYMMDD-HHMM.md
  lanes/
    YYYYMMDD_lane-label/
      waveset.md
      dispatch.md          # W1 or historical
      dispatch-w{N}.md     # active wave dispatch
      README.md
      findings/
      gate-captures/
      decisions/
  layovers/
    <workspace-name>-YYYYMMDD.md
  skills/
    proposed/
    accepted/
evals/
  run_fixtures.py
  fixtures/
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

## Public copy gates

Universal outbound prose rules ship with the plugin (AFFIRM, DASH, FILLER,
OXFORD, NO_LONGER). wavves story rules are manual (`docs/purpose-gates.md`).

```bash
python3 evals/check_public_copy.py
```

See `docs/public-copy-gates.md`. Project-specific rules (internal naming
tokens, colon ban on full UI pages) stay in the separate `prose-gates` repo.

## Self-improvement loop

Lane orchestrators can propose edits to installed skill files. Any such edit
is gated: `evals/run_fixtures.py` must pass 3 consecutive times before the
moderator applies it live. Confirmed regressions append to `wavves/failure_log.yml`.

## Workspace preflight (`/layover`)

`/layover` audits every sibling repo in a bespoke `.code-workspace` and writes
one report under `wavves/layovers/`. It never mutates an audited repo.

**Known boundary:** Cursor cloud agents remain single-repo. `/layover` does
not start a cloud agent. It does not make cloud multi-root. It does not
autoconfigure wavves in another thread. After the report, open one cloud
agent on the chosen repo and hydrate wavves there by hand.

## Paragraph tunnel and proof-before-accept

- Playbook: `skills/wavves/playbooks/paragraph-tunnel.md`  
  Checker: `python3 evals/check_paragraph_tunnel.py`
- Playbook: `skills/wavves/playbooks/proof-before-accept.md`  
  Checker: `python3 evals/check_proof_before_accept.py`  
  Host probe: `python3 skills/charter/scripts/proof_host_probe.py --self-check`

## Components

### Skills

| Skill | Description |
|:------|:------------|
| `wavves` (`/wavves`) | Main entry. Routes to bootstrap, charter, check, decide, layover, rotate, pickup or proceed. |
| `wavves-init` (`/wavves-init`) | Bootstrap the standing home a fresh moderator hydrates from. |
| `charter` (`/charter`) | Charter a lane and dispatch waves behind runnable gates. Multi-repo profile, `dispatch-w{N}.md`, authority precedence. |
| `mod-check` (`/mod-check`) | Adversarial parallel sanity-check of a landed spec or plan. Scoped verdict + `recommended_actions`. |
| `mod-decide` (`/mod-decide`) | Lock open product/design calls; authority sync on complete; emit Locked decisions for BUILD. |
| `layover` (`/layover`) | Read-only multi-repo workspace preflight audit. Does not configure cloud agents. |
| `set-key` (`/set-key`) | Terminal.app paste helper for a server-only env secret. Never agent-shells the secret. |
| `shrug` (`/shrug`) | Thin alias for emoji shrug. Bare → AUTH-10 proceed; with closed all-standing phrase → proceed-all-standing. |
| `mod-rotate` (`/mod-rotate`) | Hand the moderator or one lane to a fresh thread. |

## Examples on disk

[examples/usage.md](examples/usage.md) has the spec → BUILD lifecycle
(`/mod-check` → `/mod-decide` → `/charter`), quick-reference prompts, and
four worked walkthroughs plus a `/layover` preflight audit example.
The paths and metrics in those examples are fictional. The skills ship no
hard-coded paths from any particular project.

## Read more

- [docs/public-copy-gates.md](docs/public-copy-gates.md): universal mechanical rules (`evals/check_public_copy.py`)
- [docs/purpose-gates.md](docs/purpose-gates.md): wavves story fidelity (manual)

The launch article and companion whitepaper are omitted here until public URLs
exist.

## License

MIT
