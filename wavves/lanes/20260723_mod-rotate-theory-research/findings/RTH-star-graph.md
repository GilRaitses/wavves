# RTH-W1d — hub/spoke work graph + state snapshot

Lane: `20260723_mod-rotate-theory-research`  
Charge: RTH-W1d  
Tip at charter: `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67`  
Lens: star-shaped dispatch graph; leave-acts; rotation as serialization  
Scope: research memo only. No skill edits. No RotatE claim.

**Locked distinction (state snapshot ≠ vector embedding):** In this lane, “state embedding” means a durable file snapshot that serializes the hub/spoke work graph (roles, edges, leave-acts, positions, pending dispatches) so a successor hydrates from repo state; it does not mean a learned vector embedding, knowledge-graph embedding, or RotatE-style complex-space embedding.

---

## 1. Hub/spoke topology (roles as nodes)

The live house and the revised WOF FR describe a **star**, not a mesh: one operator-facing hub, wave orchestrators as first-ring spokes, charge workers as second-ring leaves. Edges are dispatch/return/yield, not peer chat.

| node | product name (WOF rename) | live AGENTS name (§2) | job |
|---|---|---|---|
| hub | **O0 / moderator** | O0 (this thread) | charters lanes; dispatches **wave orchestrators** background; reconciles returns; lands git on ask; never poll-blocks |
| spoke (ring 1) | **wave orchestrator** | Dispatched orchestrators/runners | owns one wave; deploys charge workers; integrates; writes rollup/gate |
| leaf (ring 2) | **charge worker** | Wave subagents | one bounded disjoint charge; owns its findings file(s) |

### Edges (directed)

```text
operator
   │  (operator-facing only)
   ▼
  O0  ──────── O0_release_window ──► (ends mod turn; integrate on notify)
   │
   │  background Task (wave orch)
   ▼
 wave orchestrator
   │
   ├──── yield_awaiting_children ──► checkpoint on disk; responsibility persists
   ├──── return_to_O0 ─────────────► only with rollup|FAIL|operator_gate
   │
   │  background Task per charge id (default fan-out)
   ▼
 charge worker(s) ──► findings/<owned>.md (+ return file)
```

**Star properties (house rules, not formal graph theory isomorphism):**

- Leaves do not dispatch peers or solicit the operator; escalation returns toward O0 via the wave orch.
- The hub does not speak to leaves for critical-path BUILD (ROLE-COLLAPSE ban).
- Parallelism is fan-out from the wave orch hublet, not from O0.

### ROLE-COLLAPSE (forbidden cuts)

From `wavves/lanes/20260723_standing-fr-revise/waveset.md` and WOF fail id `PROC-ORCH-ROLE-COLLAPSE`:

| forbidden | why it collapses the star |
|---|---|
| O0 background-dispatches charge workers | hub skips ring-1; O0 acts as wave orch |
| O0 runs mid-wave fan-out or inline BUILD | hub becomes spoke+leaf |
| Wave orch revises FRs / executes charges itself | spoke absorbs leaves (`PROC-ORCH-SOLO-BUILD`) |
| Wave orch `return_to_O0` after launching only the first worker | LAUNCH-AND-EXIT; spoke abandons the star mid-wave |

SFR leave-act bind (operational illustration of the same star):

| act | who | when |
|---|---|---|
| `O0_release_window` | moderator | after orch is background-dispatched (not after charges) |
| `yield_awaiting_children` | orch | after all charges launched; return incomplete |
| `return_to_O0` | orch | only with rollup (or hard FAIL) |

---

## 2. Leave-acts (WOF locked vocabulary)

Source: `feature-requests/20260723_wave-orchestrator-fanout.md` § Leave-acts. Three acts. Do not collapse under “return” or “end turn.”

| act | who | meaning | legal when |
|---|---|---|---|
| `return_to_O0` | wave orchestrator | finished handoff to O0; wave no longer owned by orch Task | **only** when rollup+gate exists on disk, or hard FAIL artifact, or legal `operator_gate` escalate. Launching a child ≠ return authority. |
| `yield_awaiting_children` | wave orchestrator | ends the orch turn to await completion notifications; **responsibility persists** | allowed; **requires** checkpoint (`findings/<wave>-orch-checkpoint.md`) before yield. Not `return_to_O0`. Not a poll/timer promise. |
| `O0_release_window` | O0 / moderator | ends the operator-facing turn after charter + background deploy (+ AUTH/git land if that is the land) | always after deploy; integrate on notify. Distinct from orch leave-acts. |

**Fail binds (edge misuse):**

- Illegal `return_to_O0` → `PROC-ORCH-EARLY-EXIT` / `PROC-ORCH-LAUNCH-AND-EXIT`
- Yield without checkpoint → `PROC-ORCH-NO-RESUME-CONTRACT`
- Busy-wait / poll instead of yield → `PROC-ORCH-FOREGROUND-HOLD`
- O0 holds the mod chat → `PROC-MOD-FOREGROUND-HOLD` / `PROC-MOD-PROGRESS-THEATER`

**Foreground frame (locked):** holding the operator-visible or parent-blocking turn. A charge worker’s own Task doing its one charge is not orch foreground-hold.

Leave-acts are the labeled edge types on the star. Rotation (next section) serializes which of those edges are open at handoff time.

---

## 3. Variant A vs B cuts (what the star truncates)

Source: `skills/mod-rotate/SKILL.md` § Two variants. The cut is **which subgraph is handed off**, not a change of role names.

| | **Variant A — whole-orchestrator rotation** | **Variant B — single-lane handoff** |
|---|---|---|
| When | Common case: moderator/O0 thread overloaded | One lane leaves an overloaded thread; main orchestrator continues |
| Artifact home | `<repo>/wavves/rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` | `<repo>/wavves/handoffs/<YYYYMMDD>_<lane>/` (five files) |
| Standing contract | Reuse `wavves/AGENTS.md`; do **not** restate etiquette locks per rotation | Lane packet carries locked decisions (handoff.md §B) for the fresh lane thread |
| Successor identity | `O0.R<N+1>` in rotation file section 0; assigned by handoff, never self-chosen | Fresh thread hydrates as O0 for that **lane** paste (`/wavves hydrate as O0 (<LANE> lane) from .../dispatch.md`) |
| What moves | Entire hub state: positions, **all** active background dispatches, blocked items, uncommitted state, operator-pending decisions, model policy | One lane’s purpose, locks, registry slice, primer, dispatch table, gates, uncommitted flags |
| What stays | Standing home (INDEX, AGENTS, registry, step-log) | Main orchestrator thread continues for other lanes |
| Git default | Commit plan; publish only on ask / governance | Same: no commit/push unless operator asks |
| Paste shape | `/wavves hydrate as O0.R<N+1> from .../INDEX.md (current rotation: rotations/...)` | `/wavves hydrate as O0 (<LANE> lane) from .../handoffs/.../dispatch.md` |

**Cut intuition:**

- **A** re-roots the hub node (new term incarnation of O0) while preserving the spoke inventory in one rotation snapshot.
- **B** severs one spoke (lane) into a new handoff home; the hub keeps the rest of the star.

Playbook default (`skills/wavves/playbooks/rotate.md`): pick A unless the operator named one lane.

---

## 4. Rotation file as graph serialization (“state embedding”)

### What is serialized

Per `skills/mod-rotate/SKILL.md` (variant A) and `skills/wavves-init/SKILL.md` §5 / live `wavves/AGENTS.md` §5, the rotation file is an ordered dump of hub state:

0. Successor identity (`O0.R<N+1>`)
1. Positions (landed work + commit hashes)
2. Active background dispatches (purpose, lane home, findings file, PICKUP actions, model tier)
3. Blocked items + unblock conditions
4. Uncommitted local state per repo
5. Operator-pending decisions
6. Active model policy / deviations
7. Provenance pointer (transcript path; keyword search only)

Variant B’s five-file packet is the same idea at lane grain: `handoff.md` authority + `hydration.md` read order + `step-log.md` + `dispatch.md` paste + `README.md`.

### Why call it a snapshot (not ML)

- Hydration is **file read order** (`INDEX.md` → newest rotation → active lanes → …), never linear transcript replay (`wavves-init` pointer model; AGENTS §1).
- The newest rotation file is the **current position** of the star (open spoke Tasks, blocked edges, uncommitted nodes).
- Successor ack verifies claimed commit hashes are reachable from HEAD; discrepancies become recorded gaps (`mod-rotate` Concurrent terms).
- Outgoing term fences itself after the rotation file is published: no further commits or rotation files from that thread.

**Analogy label (not isomorphism):** calling this a “state embedding” is house shorthand for “embed the work-graph state into durable files.” It is **analogy** to checkpoint/serialization, not a claim that mod-rotate implements knowledge-graph link prediction or RotatE.

### Relation to leave-acts

A legal rotation snapshot must record which leave-acts are in flight:

- Open `yield_awaiting_children` → listed under active background dispatches + checkpoint path if present.
- Completed `return_to_O0` for a wave → positions / landed rollup hashes, not still “active.”
- After deploy, O0 should have taken `O0_release_window`; if the mod thread is still holding, that is etiquette failure, not something a rotation file invents away.

---

## 5. Standing identity vs per-rotation snapshot

| layer | path | role in the star |
|---|---|---|
| Standing contract | `wavves/AGENTS.md` | role definitions, etiquette, rotation contract shape; reused across terms |
| Pickup map | `wavves/INDEX.md` | pointer to current identity + current rotation + active lanes |
| Per-term snapshot | `wavves/rotations/rotation-r*.md` | serialization of hub state for A |
| Lane packet | `wavves/handoffs/<date>_<lane>/` | serialization for B |
| Wave plan | lane `waveset.md` + `dispatch-*.md` | spoke authority for one wave |
| Charge leaves | `findings/*` owned per charge | leaf outputs |

Bootstrap gap (measured, not assumed empty forever): RTH waveset notes `wavves/rotations/` currently empty / none in INDEX; live home is O0.R1 bootstrap term (AGENTS §1 item 2, §4). Absence of a rotation file means no prior A-handoff snapshot yet; it does not erase the star topology defined by AGENTS §2 + WOF leave-acts.

---

## 6. Citation map (paths remasured this charge)

| claim | path |
|---|---|
| Three roles never collapse | `wavves/AGENTS.md` §2; `skills/wavves-init/SKILL.md` §2 |
| Rotation contract + file shape | `wavves/AGENTS.md` §5; `skills/wavves-init/SKILL.md` §5; `skills/mod-rotate/SKILL.md` variant A |
| Variants A/B | `skills/mod-rotate/SKILL.md` § Two variants |
| Leave-acts table | `feature-requests/20260723_wave-orchestrator-fanout.md` § Leave-acts |
| Role rename O0 / wave orch / charge worker | same FR § Role rename |
| ROLE-COLLAPSE + SFR leave-acts | `wavves/lanes/20260723_standing-fr-revise/waveset.md` |
| Star-shaped dispatch named as research subject | `wavves/lanes/20260723_mod-rotate-theory-research/waveset.md` Grounding / Root constraint |
| Rotate playbook default A | `skills/wavves/playbooks/rotate.md` |
| Visitor rotation blurb (term identity; no star vocabulary) | `README.md` “Rotation with term identity” |

---

## 7. Gaps (explicit)

1. **Product rename vs live AGENTS wording.** WOF locks product names “wave orchestrator” / “charge worker”; live `wavves/AGENTS.md` §2 still says “Dispatched orchestrators/runners” / “Wave subagents.” Topology is the same; vocabulary not yet BUILD-synced (FR status: revised-after-WOF, awaiting re-check or `/mod-decide`).
2. **Empty `rotations/`.** No live A-snapshot to remasure section shape against; skill text is the authority for required fields.
3. **“Star graph” is house framing.** Waveset root constraint states the house names a star-shaped dispatch graph; README visitor prose does not use hub/spoke vocabulary. Treat “star” as research formalization of existing role+dispatch rules, not a shipped theorem.
4. **No claim that leave-acts are already installed in `skills/charter/SKILL.md`.** They are locked in the WOF FR for BUILD; this memo cites the FR as the leave-act authority.

---

## 8. Non-claims

- Does **not** claim RotatE, TransE, or any KG embedding model applies to mod-rotate.
- Does **not** claim isomorphism to Raft/StatefulSet/Erlang (those are other charges); identity borrowings are out of scope except as consumers of the rotation snapshot.
- Does **not** edit skills or charter BUILD.
