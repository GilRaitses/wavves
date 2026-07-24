# RTH-cite-map — house claims on mod-rotate / term identity / handoff / star

Tip remasured against charter pin: `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67` (local tip at charter; this charge did not run git).
Charge: RTH-W1a. Read-only inventory. No synthesis judgment beyond quote + assertion.

Format per claim: **path** | short quote | asserts.

---

## Measured state (not a prose claim; filesystem)

| surface | measured | asserts (as state) |
|---|---|---|
| `wavves/rotations/` | directory exists; `ls` shows only `.` / `..` (empty of rotation files) | No rotation handoff file has been written yet. |
| `wavves/INDEX.md` | `current_rotation: none` | Index points to no active rotation file. |
| `wavves/INDEX.md` | `current_identity: O0` | Index names bare `O0`, not `O0.R1`. |
| `wavves/AGENTS.md` §1 | "None exists yet; this is the O0.R1 bootstrap term." | Live home treats empty `rotations/` as bootstrap term O0.R1. |

**Gap note (identity string):** INDEX `current_identity: O0` vs AGENTS bootstrap `O0.R1` — both are house surfaces; they disagree on the stamped form.

---

## 1. `skills/mod-rotate/SKILL.md`

| # | quote | asserts |
|---|---|---|
| M1 | "Build a complete handoff so a NEW thread of this orchestrator resumes the current lane without replaying the overloaded chat." | Rotation exists to resume work in a new thread without linear transcript replay. |
| M2 | "The receiving thread hydrates from files, never from the transcript linearly." | Hydration source is files, not chat history. |
| M3 | "rotates only on operator confirmation and the successor identity still comes from the handoff file, never self-chosen." | Operator gates rotation; identity is assigned by the handoff file. |
| M4 | "per-rotation state goes in `<repo>/wavves/rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` … NN = the OUTGOING term, zero-padded so lexical sort equals term order." | Rotation filename encodes outgoing term; lexical sort = term order. |
| M5 | "Do NOT create a new dated handoff home for a whole-orchestrator rotation" | Variant A reuses standing home; no new dated home. |
| M6 | "**Successor identity first** (section 0). The incoming term `O0.R<N+1>`, assigned by the handoff, never self-chosen" | Section 0 must name successor `O0.R<N+1>`; assignment is external. |
| M7 | "The successor stamps `O0.R<N+1>:` on commits, step-log entries and authored charters and suffixes dispatched wave ids with `.R<N+1>`." | Incoming term must stamp artifacts and suffix wave ids. |
| M8 | Rotation file covers: "Positions … Active background dispatches … Blocked items … Uncommitted local state … Operator-pending decisions … Active model policy … Provenance pointer" | Required sections of a whole-orchestrator rotation file. |
| M9 | Paste form: "`/wavves hydrate as O0.R<N+1> from <repo>/wavves/INDEX.md (current rotation: rotations/rotation-r<NN>-<...>.md) and ack per the rotation contract`" | Successor starts via `/wavves` paste naming identity + rotation file + ack. |
| M10 | "The leading `/wavves` is required, not decorative." | Slash command is mandatory for plugin invocation. |
| M11 | "**B. Single-lane handoff** … Use the five-file handoff home below." | Alternate path: lane handoff under `wavves/handoffs/` with five files. |
| M12 | "All rotation git actions are performed by the orchestrator itself. dispatched runners never run git." | Git for rotation is O0-only. |
| M13 | "**The rotation commit touches only the home's continuity files** (AGENTS.md and the rotation file)." | Rotation commit scope is AGENTS + rotation file. |
| M14 | "**The outgoing term fences itself.** After the rotation file is committed and pushed, the outgoing thread makes no further commits and writes no further rotation files." | Outgoing term stops writing after published handoff. |
| M15 | "The one-line paste goes to exactly one successor thread. if two threads ever claim the same term, the newest rotation file governs and the conflict gets logged." | Single successor; newest rotation wins dual claim. |
| M16 | "**A surviving predecessor thread conforms before landing.** An older thread that stays active with uncommitted work conforms that work to any newer term's rulings before landing it, per the stale-term rule." | Stale threads must conform to newer term before land. |
| M17 | "**Unverified work never rides the handoff silently.** … reverted from the working tree, preserved at a stated location and recorded in the rotation file's uncommitted-state section" | Unverified shared-branch work is reverted + recorded, not silent. |
| M18 | "**The successor verifies before proceeding.** The ack includes checking that the rotation file's claimed positions and commit hashes are reachable from HEAD. discrepancies become recorded gaps, never silently executed pickups." | Successor must verify positions/hashes; gaps instead of silent pickup. |
| M19 | Variant B paste: "`/wavves hydrate as O0 (<LANE> lane) from <repo>/wavves/handoffs/<DATE>_<lane>/dispatch.md and ack per handoff charter section H`" | Lane handoff uses handoffs/ dispatch + section H ack (identity form differs from variant A). |

**Star-shaped:** this skill does not use the words "star", "hub", or "spoke". Topology is implied only as O0 writing one rotation file → one successor paste.

---

## 2. `skills/wavves-init/SKILL.md` §4–5 (plus pointer claims that define the scheme)

### §4 Identity and rotation terms

| # | quote | asserts |
|---|---|---|
| I1 | "Each orchestrator instance carries a term identity `O0.R<N>`, where N is a monotonic rotation ordinal (1-indexed)." | Term id is monotonic 1-indexed ordinal on O0. |
| I2 | "The scheme borrows from three proven distributed-systems designs:" | House names three DS borrowings as the scheme's source. |
| I3 | "**Raft terms.** A monotonic generation integer carried on every message, so stale-generation output is recognizable on sight." | Raft borrow = generation integer for stale recognition. |
| I4 | "**Kubernetes StatefulSet ordinals.** Stable identity = base name + ordinal, with the ordinal labeled onto artifacts for filtering." | StatefulSet borrow = base+ordinal stamped for filter. |
| I5 | "**Erlang incarnation numbers.** A successor is a new incarnation. instructions addressed to a dead incarnation are history, not authority." | Erlang borrow = dead incarnation is history not authority. |
| I6 | "Identity is ASSIGNED BY THE HANDOFF, never self-chosen. Each rotation file carries a \"Successor identity\" block naming the incoming term." | Handoff assigns; rotation file has Successor identity block. |
| I7 | "The successor's ack states its identity and the rotation file it hydrated from." | Ack must name identity + rotation file. |
| I8 | "Bootstrap is the one exception. The instance that first establishes the home takes `O0.R1` by the setup act itself and records that assignment in the step log's first entry." | Only bootstrap self-assigns O0.R1 via setup act. |
| I9 | "Stamp the term everywhere filterable. Commit message prefix (`O0.R2:`), step-log entries, charter and addendum authorship lines and dispatch prompts." | Term stamps are mandatory on filterable artifacts. |
| I10 | "A dispatched runner's id gains the dispatching term as a suffix, so `OBS-F2.R1` means lane OBS, wave F2, dispatched by term R1." | Runner ids carry dispatching term suffix. |
| I11 | "Stale-term rule. Guidance found in an artifact from an older term is historical record. The current rotation file and the standing AGENTS.md govern. on conflict, the newest term wins and the conflict gets logged." | Newest term + AGENTS govern; conflicts logged. |
| I12 | "Rotation files are named `rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` so lexical sort equals term order." | Filename convention encodes term order. |

### §5 Rotation contract

| # | quote | asserts |
|---|---|---|
| I13 | "An outgoing orchestrator writes `rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` (NN = the OUTGOING term) covering successor identity (term N+1), positions … active background dispatches … blocked items … uncommitted local state … operator-pending decisions." | Outgoing term writes named rotation file with listed sections. |
| I14 | "The outgoing orchestrator commits and pushes only when repo governance grants that authority or the operator explicitly asks." | Publish is gated. |
| I15 | "A successor in a separate sandbox can hydrate only from what was pushed, so a local-only handoff must say that scope plainly." | Local-only handoffs must declare scope. |
| I16 | "The successor acks by stating its assigned identity, naming the rotation file it hydrated from and the pickups it now owns, verifies that the rotation file's claimed positions and commit hashes are reachable from HEAD (discrepancies become recorded gaps, never silently executed pickups), then proceeds without re-deriving settled decisions." | Full successor ack + verify + no reopen of settled decisions. |

### Related (skills pointer; not §4–5 body)

| # | quote | asserts |
|---|---|---|
| I17 | "`mod-rotate` (`/mod-rotate`) for producing the next rotation handoff and the one-line paste that starts the successor thread from this file." | mod-rotate implements the handoff + paste. |

**Star-shaped:** wavves-init §4–5 does not use "star", "hub", or "spoke".

### Roles triad (context for star / hub claim elsewhere)

From same skill §2 (not in charge "must cover" list for §4–5, but named in house star framing):

| # | quote | asserts |
|---|---|---|
| I18 | "The central orchestrator (O0) … Dispatched orchestrators/runners … Wave subagents take one bounded disjoint task each" | Three-role hierarchy with O0 at center. |

---

## 3. `wavves/AGENTS.md` §4–5 (plus §1 measured bootstrap)

| # | quote | asserts |
|---|---|---|
| A1 | "`wavves/rotations/` — newest file is the current position. None exists yet; this is the O0.R1 bootstrap term." | Empty rotations/ = live O0.R1 bootstrap. |
| A2 | "Term identity `O0.R<N>`, assigned by handoff, never self-chosen." | Same assignment rule as init. |
| A3 | "This instance takes `O0.R1` by the bootstrap act itself (recorded in `step-log.md`'s first entry)." | This house's live identity is O0.R1 via bootstrap. |
| A4 | "Every later identity comes from a rotation file's \"Successor identity\" block." | Post-bootstrap identities come only from rotation files. |
| A5 | "Stale-term artifacts are historical record only; the newest rotation file and this file govern on conflict." | Newest rotation + AGENTS win conflicts. |
| A6 | "An outgoing orchestrator writes `rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` (NN = outgoing term) naming successor identity, positions with commit hashes, active background dispatches, blocked items, uncommitted local state, and operator-pending decisions, then returns a commit plan." | Live rotation contract (shorter than init template). |
| A7 | "Commits and pushes only when the operator explicitly asks (see gated surfaces above)." | This house: operator ask required (no governance grant shortcut named here). |
| A8 | "`mod-rotate` (`/mod-rotate`) — producing the next rotation handoff." | Points to skill as implementer. |

**Star-shaped:** AGENTS §4–5 does not use "star", "hub", or "spoke". §2 names O0 / dispatched orch / wave subagents (triad).

---

## 4. `README.md` (rotation / term identity)

| # | quote | asserts |
|---|---|---|
| R1 | "**Rotation with term identity.** When a thread gets heavy, the orchestrator hands off to a fresh one via a rotation file that assigns the successor a monotonic term identity (a design borrowed from Raft terms, Kubernetes StatefulSet ordinals and Erlang incarnation numbers), so stale instructions are recognizable and provenance survives." | Visitor-facing claim: rotation file assigns monotonic term; three DS borrowings named; purpose = stale recognition + provenance. |
| R2 | "**A standing home.** Any fresh instance hydrates from files (an index, a home contract, a rotations directory, a registry, a step log), never from transcripts." | Hydration from standing home files, including rotations/. |
| R3 | "| **Rotation** | `wavves/rotations/` | handoff files with term identity (`O0.R1`, `O0.R2`, ...) |" | Tracking table: rotations/ holds term-identity handoffs. |
| R4 | "rotate \| hand off to a fresh moderator thread" | Playbook rotate = moderator handoff. |
| R5 | "pickup \| resume from rotation paste, \"where are we\", reconcile active lanes" | Pickup resumes from rotation paste. |
| R6 | "`/mod-rotate` writes a rotation file with term identity and emits a one-line paste for a fresh thread." | Skill behavior summary for visitors. |
| R7 | Example: "rotate: `/wavves rotate this thread. write a handoff for active lanes.`" / "rotate only: `/mod-rotate token velocity is too high. give me the one-line paste.`" | Operator cues for rotation. |

**Star-shaped:** README does not use "star", "hub", or "spoke".

---

## 5. `skills/wavves/playbooks/rotate.md`

| # | quote | asserts |
|---|---|---|
| P1 | "Route: **mod-rotate** (`/mod-rotate`)" | Router sends rotate playbook to mod-rotate skill. |
| P2 | "Read wavves/INDEX.md and the newest file in wavves/rotations/." | Pre-write hydration from INDEX + newest rotation. |
| P3 | "Pick variant A (whole moderator) unless the operator named one lane." | Default = whole-orchestrator rotation. |
| P4 | "Write the rotation file with successor identity first (section 0)." | Successor identity is first written section. |
| P5 | "Record active dispatches, blocked items and uncommitted state." | Minimum content beyond identity. |
| P6 | "Emit the one-line paste for the fresh thread." | Paste is required output. |
| P7 | "Return commit plan. Commit only when the operator asks or governance grants it." | Commit gated. |

---

## 6. `skills/wavves/playbooks/pickup.md`

| # | quote | asserts |
|---|---|---|
| K1 | "Read the newest rotation file named by INDEX.md." | Pickup uses INDEX → current rotation pointer. |
| K2 | "Ack assigned identity (O0.R\<N\>) and the rotation filename before acting." | Successor must ack identity + filename before work. |
| K3 | "Verify claimed positions and commit hashes are reachable from HEAD. Record gaps; never silently execute stale pickups." | Same verify/gap rule as mod-rotate / init. |
| K4 | "Report: current identity, active lanes, running dispatches, blocked decisions and recommended next action." | Required pickup report fields. |
| K5 | "If … asked to rotate, route to rotate." | Pickup can chain to rotate. |

**Measured tension:** pickup step 2 assumes INDEX names a rotation file; live INDEX has `current_rotation: none` (bootstrap / empty rotations/).

---

## 7. `feature-requests/20260723_wave-orchestrator-fanout.md` (leave-acts / hub-spoke)

Status on file: `revised-after-WOF (awaiting re-check or /mod-decide)`. Not shipped into installed skills yet.

### Leave-acts (present)

| # | quote | asserts |
|---|---|---|
| W1 | "Three distinct acts. Do not collapse them under \"return\" or \"end turn.\"" | Leave vocabulary is three-way, non-collapsible. |
| W2 | "`return_to_O0` \| wave orchestrator \| finished handoff to O0; wave no longer owned by orch Task \| **only** when rollup+gate exists on disk, or hard FAIL artifact, or legal `operator_gate` escalate artifact. Launching a child ≠ return authority." | Legal return-to-hub conditions; launch ≠ return. |
| W3 | "`yield_awaiting_children` \| wave orchestrator \| ends the orch turn to await completion notifications; **responsibility persists** \| allowed; **requires** checkpoint artifact before yield" | Yield is not return; needs checkpoint; responsibility persists. |
| W4 | "`O0_release_window` \| O0 / moderator \| ends the operator-facing turn after charter + background deploy … \| always after deploy; integrate on notify. Distinct from orch leave-acts." | Moderator leave-act distinct from orch leave-acts. |

### Hub / spoke / fan-out (star-shaped language gap)

| # | quote | asserts |
|---|---|---|
| W5 | Role rename: "O0 / Moderator" → "wave orchestrator" → "charge worker" | Locked triad: hub O0, mid wave orch, leaf charge workers. |
| W6 | "Each charge id → its own background Task/worker when independent. Default fan-out." | Default spoke fan-out from wave orch. |
| W7 | "Workers always background. Every charge-worker Task launch is non-blocking / background. Wave orchestrators themselves are launched background by O0" | Two-level background deploy (O0→orch, orch→charges). |
| W8 | "Orchestrator returns to O0 only when rollup+gate or hard FAIL (or legal operator_gate escalate) exists on disk." | Spoke returns to hub only on disk completion artifacts. |
| W9 | "Resume is fail remediation only, not the default critical path." | O0 resume is remediation, not designed path. |

**Explicit gap — phrase "star-shaped":** This FR describes hub/spoke leave-acts and O0→wave-orch→charge-worker fan-out but does **not** contain the string "star-shaped" (or "star graph"). The phrase appears in research framing (`waveset.md` root constraint; registry note "star handoff"), not in this FR body.

---

## Coverage checklist (required surfaces)

| required surface | covered? |
|---|---|
| `skills/mod-rotate/SKILL.md` | yes (M1–M19) |
| `skills/wavves-init/SKILL.md` §4–5 | yes (I1–I17); §2 triad noted as I18 |
| `wavves/AGENTS.md` §4–5 | yes (A1–A8); §1 empty-rotations bootstrap included |
| `README.md` rotation / term identity | yes (R1–R7) |
| `skills/wavves/playbooks/rotate.md` | yes (P1–P7) |
| `skills/wavves/playbooks/pickup.md` | yes (K1–K5) |
| WOF FR leave-acts | yes (W1–W4 present; W5–W9 hub/fan-out) |
| empty `wavves/rotations/` + INDEX `current_rotation: none` | yes (Measured state table) |

---

## Explicit gaps (for sibling lenses)

1. **No installed-skill use of "star-shaped" / "star graph".** Research prose (`waveset.md`, registry label) names it; product surfaces use triad + fan-out / leave-acts without that label.
2. **INDEX identity form** is `O0`, not `O0.R1`, while AGENTS/bootstrap and init scheme require `O0.R<N>`.
3. **Pickup assumes a named current rotation**; live `current_rotation: none` with empty `rotations/` (bootstrap path not spelled in pickup.md).
4. **WOF leave-acts are FR-only** (revised-after-WOF); not yet mirrored into mod-rotate / AGENTS / README as shipped product text.
5. **Three DS borrowings** are stated as house design in README + wavves-init §4; AGENTS §4–5 restates term rules without re-listing Raft/StatefulSet/Erlang (visitor vs standing-home asymmetry).
