# RTH-W1c — StatefulSet ordinals + Erlang incarnations vs wavves identity

| Meta | |
|---|---|
| charge | RTH-W1c |
| tip | `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67` |
| model | cursor-grok-4.5-high-fast |
| scope | read-only map; no skill edits |

Label key: **isomorphism** = a named formal property that the house rule
implements with the same force (recognizable generation, reject-stale, or
stable compound name). **analogy** = useful teaching borrow without a
runtime or protocol that enforces the foreign property.

External facts below are well-known public properties of Kubernetes
StatefulSets and Erlang/OTP distribution. They are marked **external**.
No paper quotes are invented; no primary-source fetch was done this charge.

---

## 1. House claims (remasureable)

### 1.1 Identity scheme and three borrows

`skills/wavves-init/SKILL.md` §4:

> Each orchestrator instance carries a term identity `O0.R<N>`, where N is a
> monotonic rotation ordinal (1-indexed). The scheme borrows from three proven
> distributed-systems designs:
>
> - **Raft terms.** ...
> - **Kubernetes StatefulSet ordinals.** Stable identity = base name + ordinal,
>   with the ordinal labeled onto artifacts for filtering.
> - **Erlang incarnation numbers.** A successor is a new incarnation.
>   instructions addressed to a dead incarnation are history, not authority.

Rules in the same section (paraphrase with quotes where binding):

- Identity is **ASSIGNED BY THE HANDOFF**, never self-chosen; rotation file
  carries a "Successor identity" block; bootstrap exception takes `O0.R1`.
- Stamp the term everywhere filterable; runner id gains dispatching term as
  suffix: `OBS-F2.R1` means lane OBS, wave F2, dispatched by term R1.
- **Stale-term rule:** older-term guidance is historical; current rotation
  file + standing `AGENTS.md` govern; newest term wins; conflict logged.
- Rotation filenames `rotation-r<NN>-...` so lexical sort equals term order.

### 1.2 Live standing contract

`wavves/AGENTS.md` §4–5 compresses the same identity and handoff contract
without restating the StatefulSet/Erlang names. Binding lines:

> Term identity `O0.R<N>`, assigned by handoff, never self-chosen. ...
> Stale-term artifacts are historical record only; the newest rotation file
> and this file govern on conflict.

### 1.3 mod-rotate mechanics

`skills/mod-rotate/SKILL.md` variant A:

- Section 0 assigns successor `O0.R<N+1>` (never self-chosen).
- Successor stamps `O0.R<N+1>:` and suffixes wave ids with `.R<N+1>`.
- Outgoing term **fences itself** after rotation commit/push; one paste to
  one successor; if two threads claim the same term, newest rotation file
  governs.
- Surviving predecessor conforms uncommitted work to newer rulings before
  landing (stale-term rule).
- Successor ack verifies claimed positions/hashes; gaps recorded, not
  silently executed.

### 1.4 Pickup ack

`skills/wavves/playbooks/pickup.md`:

> Ack assigned identity (O0.R\<N\>) and the rotation filename before acting.

### 1.5 Public claim

`README.md`:

> Rotation with term identity. ... monotonic term identity (a design borrowed
> from Raft terms, Kubernetes StatefulSet ordinals and Erlang incarnation
> numbers), so stale instructions are recognizable and provenance survives.

---

## 2. External: Kubernetes StatefulSet ordinals

**Source class:** external / well-known Kubernetes API behavior (not fetched
this charge).

Well-known properties:

1. Pod identity is compound: `<statefulset-name>-<ordinal>` (ordinal usually
   `0 .. replicas-1`).
2. Ordinal is **stable across pod restart** for that slot: same name, same
   sticky identity (DNS, PVC binding conventions).
3. Controllers use ordinals for **ordered** scale/update (peer slots in one
   set), not as a single-leader generation counter.
4. Filtering and addressing by ordinal is a first-class operational habit
   (logs, services, PVCs keyed by the compound name).

What StatefulSet ordinals are **not**:

- Not a global "generation of the whole cluster authority" counter.
- Not a protocol that rejects RPCs stamped with an older ordinal when a
  newer peer exists (peers of different ordinals are concurrent members).

---

## 3. External: Erlang incarnation / creation numbers

**Source class:** external / well-known Erlang/OTP distribution behavior
(not fetched this charge).

Well-known properties (node creation + process identity recycling):

1. A node name can outlive a VM process; when the node restarts, distribution
   uses a **creation** (incarnation) counter so peers treat the new node as
   a new incarnation of that name.
2. Process ids can be recycled; monitors/links and stale references are meant
   so signals for a **dead** process/incarnation are not delivered as live
   authority to a new inhabitant of a recycled id.
3. The operational slogan matching the house prose: a successor is a new
   incarnation; mail addressed to the dead incarnation is history.

What Erlang incarnations are **not** (for this map):

- Not an operator-authored handoff document that *assigns* the next
  identity string before the successor starts.
- Not the same object as a StatefulSet peer ordinal (incarnation fences
  generations of one name; ordinals name concurrent slots).

---

## 4. Mapping table

| Foreign property | House surface | Fit label | Notes |
|---|---|---|---|
| Compound name `base-ordinal` | `O0.R<N>` | **analogy** (strong for naming) | Base role `O0` + ordinal `R<N>`. Filters and stamps match the "stable identity string" habit. |
| Ordinal labeled on artifacts | Commit prefix `O0.R2:`, step-log, charters, dispatch prompts | **analogy** → partial **isomorphism** of *filterability* | Same operational buy: grep/filter by generation. No kube controller enforces it. |
| Concurrent peer slots `0..N-1` | Multiple live `O0.R*` threads | **breaks** if treated as isomorphic | House design is successive authority of one moderator role. Concurrent terms are a conflict to fence (`mod-rotate` newest-file rule), not a replica set. |
| Ordered scale by ordinal | Rotation file NN lexical sort | **analogy** (weak) | Lexical sort = term order is a filesystem convenience, not StatefulSet ordered rollout. |
| Sticky PVC / restart same slot | Fresh chat thread hydrates same role from files | **analogy** (weak) | Continuity is file hydration + assigned id, not volume sticky identity. |
| Node/process creation increments | Successor term `O0.R<N+1>` | **analogy** (strong for succession) | New term = new incarnation of the moderator role. |
| Stale mail to dead incarnation discarded | Stale-term rule; older artifacts = history | **analogy**; **not isomorphism** | House relies on agent etiquette + newest rotation/`AGENTS.md` governance. No runtime drops wrong-term "messages". |
| Runtime-enforced reject-stale | Outgoing fence; predecessor conforms; ack-before-act | **house rules that *simulate* the buy** | Closest local substitutes for Erlang's kernel fence. Still process discipline, not a distribution layer. |
| Identity assigned by supervisor/handoff | "Successor identity" block; pickup ack | **analogy** (handoff) | Supervisor restart ≠ operator paste, but both forbid self-chosen identity. |
| Runner suffix `.R1` on `OBS-F2` | Provenance: who chartered | **house invention** using ordinal stamp | Not a StatefulSet peer id among runners; not an Erlang pid. It stamps **dispatching term** onto a wave id. |

### 4.1 O0.R\<N\> specifically

- **N as StatefulSet ordinal:** **analogy.** Shape match (`name + ordinal`)
  and filter habit. Semantic mismatch: N indexes **successive moderator
  generations**, not concurrent peer pods in a set.
- **N as Erlang incarnation:** **stronger analogy** for succession and
  stale-authority. Still not isomorphic: no creation field in a wire
  protocol; authority switch is a markdown rotation file + human paste.

### 4.2 Runner suffixes (e.g. OBS-F2.R1)

From init §4: `OBS-F2.R1` = lane OBS, wave F2, dispatched by term R1.
Returns reconcile under the **current** term; suffix preserves charter
provenance.

| Borrow | Fit |
|---|---|
| StatefulSet "label ordinal onto artifact" | **analogy** — stamp for filtering |
| Erlang incarnation on the runner itself | **breaks** if over-read — the runner is not a new incarnation of OBS-F2; the suffix records the **parent term** that dispatched it |
| Stale-term rule | Dependent: a return stamped `.R1` may land under `O0.R2`; content is reconciled under current governance, not under R1's authority |

### 4.3 Stale-term rule

House text (init §4 / AGENTS §4): older-term guidance is historical; newest
rotation + AGENTS govern; conflict logged.

| Borrow | Fit |
|---|---|
| Erlang "dead incarnation is history" | **analogy** (primary borrow named in init) |
| Raft stale-term rejection | Parallel borrow (owned by RTH-W1b); not re-litigated here |
| StatefulSet ordinals | **breaks** as the primary model — peer ordinals do not mean "older ordinal is invalid authority" |

### 4.4 Successor-assigned identity

House: handoff assigns `O0.R<N+1>`; successor ack states identity + rotation
file; never self-chosen (bootstrap exception for R1).

| Borrow | Fit |
|---|---|
| Erlang successor = new incarnation | **analogy** for "new inhabitant, old mail not authority" |
| StatefulSet controller allocates ordinal | **analogy** (weak) — controller assigns pod ordinals; house assigns via human-operated rotation file |
| Self-chosen identity ban | **house rule** depending on the incarnation borrow's teaching intent |

---

## 5. Buys / breaks / dependent house rules

### 5.1 StatefulSet ordinals

**Buys**

1. Stable, greppable compound identity (`O0` + `R<N>`).
2. Habit of stamping the ordinal on commits, logs, charters, and runner ids
   so provenance and filtering survive thread death.
3. Lexical rotation filenames that sort with term order (mild buy).

**Breaks**

1. Treating `O0.R1` and `O0.R2` as concurrent peer replicas (StatefulSet
   mental model). House wants one current moderator authority.
2. Expecting ordered peer rollout / sticky volumes / DNS per ordinal.
3. Expecting a controller to prevent two pods from claiming the same
   ordinal; house only has "newest rotation file governs" prose.

**Dependent house rules**

1. Stamp term on commits / step-log / charters / dispatch prompts
   (`wavves-init` §4).
2. Runner suffix `.R<N>` for dispatch provenance (`wavves-init` §4;
   `mod-rotate` successor stamp).
3. Rotation filename `rotation-r<NN>-...` lexical order (`wavves-init` §4;
   `mod-rotate` variant A).

### 5.2 Erlang incarnation numbers

**Buys**

1. Teaching frame for succession: new term = new incarnation of the role.
2. Stale instructions addressed to a prior term are history, not live
   authority (stale-term rule).
3. Justifies forbidding self-chosen identity and requiring handoff
   assignment + pickup ack.

**Breaks**

1. No runtime that drops wrong-incarnation messages. A stale thread can
   still write files or propose commits unless etiquette and git fences hold.
2. No automatic creation bump on crash; bump happens only when someone runs
   `/mod-rotate` (or bootstrap).
3. Process-id recycling hazards are not the house failure mode; the mode is
   **chat-thread overload / context death** with leftover agents still able
   to act.

**Dependent house rules**

1. Stale-term rule (init §4; AGENTS §4).
2. Successor identity assigned by handoff; never self-chosen (init §4;
   mod-rotate §0; pickup ack).
3. Outgoing fence after rotation; one paste → one successor; newest
   rotation wins on dual claim (`mod-rotate` concurrent-terms section).
4. Surviving predecessor conforms before landing (`mod-rotate`).
5. Bootstrap-only self-assignment of `O0.R1` recorded in step-log (init §4;
   AGENTS §4).

---

## 6. Analogy vs isomorphism verdict

| Claim in house prose | Verdict |
|---|---|
| "Stable identity = base name + ordinal" (StatefulSet) | **Analogy** for naming/filter stamps. Not an isomorphism to StatefulSet peer-slot semantics. |
| "Successor is a new incarnation; dead incarnation is history" (Erlang) | **Analogy** for authority succession + stale-term doctrine. Not an isomorphism to Erlang creation/monitor enforcement. |
| README "borrowed from ... StatefulSet ordinals and Erlang incarnation numbers" so stale instructions are recognizable | **Analogy** (honest as a design borrow). "Recognizable" is true for stamped ids; "rejected automatically" is **not** claimed by the skills and must not be inferred. |
| Filterable term stamps / runner suffixes | Local **isomorphism of filterability** (house property), inspired by ordinal labeling, not by kube API. |
| Stale-term governance by newest rotation + AGENTS | Local **house rule**, Erlang-colored. Enforcement = human/agent process + git etiquette, not distribution creation fields. |

**Locked sentence for synthesis:** StatefulSet ordinals buy the compound
filterable name; Erlang incarnations buy the succession/stale-authority
story; neither is a protocol isomorphism inside wavves, and concurrent
`O0.R*` peers must not be read as a StatefulSet replica set.

---

## 7. Gaps (charge-local)

1. No primary Kubernetes or Erlang doc fetch this charge; external rows are
   well-known-public only. Synthesis should not upgrade them to paper cites
   without a fetch.
2. Raft term mapping is out of scope here (RTH-W1b). Overlap noted only
   where stale-generation recognition is shared language.
3. `wavves/rotations/` is empty at tip (waveset grounding); live multi-term
   history is not remasureable yet. Ordinal/incarnation claims are from
   skill + AGENTS text, not from a landed R2 handoff artifact.
4. Variant B lane handoff paste uses `O0 (<LANE> lane)` without an `R<N>`
   stamp in the playbook line; interaction with term ordinals for lane-only
   handoffs is a minor doc seam (not blocking this map).

---

## 8. Commit file list (for O0 only)

This charge writes:

- `wavves/lanes/20260723_mod-rotate-theory-research/findings/RTH-ordinal-incarnation.md`
- `wavves/lanes/20260723_mod-rotate-theory-research/findings/RTH-W1c-return.md`

No git. No skill edits. No BUILD.
