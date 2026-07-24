# RTH-W1e — adversarial (overclaim / false isomorphism)

```text
lens: adversarial
tip: 7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67
model: cursor-grok-4.5-high-fast
read_only: yes
```

## Verdict for orch gate

**FAIL — honesty/overclaim would poison synthesis** if RTH-INT echoes
public/init prose as settled isomorphism, treats empty `rotations/` as live
term continuity, or collapses O0 into wave-orch/charge work.

W1e deliverable itself is complete (≥3 evidenced risks + bans below). Orch
must pause for O0 before RTH-INT per waveset GATED rule.

## Method

Read-only hunt across primary seams listed in `waveset.md` Grounding.
No skill edits. No git. No BUILD. Sibling W1 findings not authored here.

## Evidenced overclaim risks (≥3)

### R1 — DS borrowings stated as proven designs, not labeled analogy

**Risk:** Visitors and synthesizers treat Raft / StatefulSet / Erlang as
formal isomorphisms for `O0.R<N>`, though house text never implements Raft
election/log replication, StatefulSet controllers, or Erlang process links.

**Evidence:**

1. `skills/wavves-init/SKILL.md` §4 (lines 276–285):

> Each orchestrator instance carries a term identity `O0.R<N>`, where N is a
> monotonic rotation ordinal (1-indexed). The scheme borrows from three proven
> distributed-systems designs:
>
> - **Raft terms.** A monotonic generation integer carried on every message, so
>   stale-generation output is recognizable on sight.
> - **Kubernetes StatefulSet ordinals.** Stable identity = base name + ordinal,
>   with the ordinal labeled onto artifacts for filtering.
> - **Erlang incarnation numbers.** A successor is a new incarnation.
>   instructions addressed to a dead incarnation are history, not authority.

No "analogy" label. "Proven … designs" invites isomorphism.

2. `README.md` (lines 27–31):

> **Rotation with term identity.** When a thread gets heavy, the orchestrator
> hands off to a fresh one via a rotation file that assigns the successor a
> monotonic term identity (a design borrowed from Raft terms, Kubernetes
> StatefulSet ordinals and Erlang incarnation numbers), so stale instructions
> are recognizable and provenance survives.

Parenthetical "borrowed from" still asserts outcome ("so stale instructions
are recognizable") without labeling analogy vs isomorphism.

3. Contrast: live `wavves/AGENTS.md` §4 names term rules but **never** names
Raft, StatefulSet, or Erlang. Public README is louder than the standing
contract.

**Footgun:** Synthesis that says "wavves implements Raft terms" or "term
identity is isomorphic to Raft" is false. At most: naming/monotonicity
**analogy**, house-enforced by handoff file + stamps when those artifacts
exist.

### R2 — Empty `rotations/` vs claimed continuity / enforcement

**Risk:** Prose describes a working rotation continuity surface; on-disk home
has no rotation file, INDEX says `none`, and identity stamps disagree.

**Evidence:**

1. `wavves/rotations/` — directory exists, **zero files** (remasured this
   charge).

2. `wavves/INDEX.md` (lines 3–4):

> current_identity: O0
> current_rotation: none

3. `wavves/AGENTS.md` (lines 13–14, 105–106):

> `wavves/rotations/` — newest file is the current position. None exists
> yet; this is the O0.R1 bootstrap term.
>
> Term identity `O0.R<N>`, assigned by handoff, never self-chosen. This
> instance takes `O0.R1` by the bootstrap act itself

4. `wavves/step-log.md` first entry: identity `O0.R1` assigned; `rotations/`
   "empty, no rotation yet".

5. `skills/wavves-init/SKILL.md` Quality bar (lines 363–364):

> The identity scheme is enforced in artifacts (stamps, suffixes, file
> names), beyond being described in prose.

6. `skills/mod-rotate/SKILL.md` (line 56):

> Follow the section shape of the newest existing file in `rotations/`.

With an empty directory there is **no** newest file to follow; first
rotation has no in-dir template fence.

**Footgun:** Claiming "provenance survives via rotation files" or "scheme
enforced in artifacts" as a measured live property of this home is
overclaim. Bootstrap term exists in step-log/AGENTS prose; INDEX omits
`.R1`; no rotation handoff artifact yet.

### R3 — "Graph" / star framing without graph operations (false theory upgrade)

**Risk:** Research and lane copy frame mod-rotate as graph/DS **theory**;
shipped skills define file handoffs and role paste, not graph ops
(adjacency, traversal, cut, embedding algorithms).

**Evidence:**

1. Lane `waveset.md` Intent (lines 14–15):

> Operator: deeper research into the applied graph / distributed-systems theory
> behind **mod-rotate**

2. Lane `README.md` (lines 3–4):

> Deeper research into the distributed-systems and graph framing behind
> `/mod-rotate` (term identity, star handoff, state snapshot).

3. `waveset.md` Root constraint (lines 34–36):

> house prose names three DS borrowings and a star-shaped
> dispatch graph, but has no research memo separating **isomorphism** from
> **analogy**

4. Shipped `skills/mod-rotate/SKILL.md` — mechanics are variants A/B, five-file
   packet, one-line paste, git fencing. **No** graph vocabulary, no star,
   no adjacency, no serialization-as-embedding API.

5. WOF FR leave-acts (`feature-requests/20260723_wave-orchestrator-fanout.md`)
   define role acts (`return_to_O0`, `yield_awaiting_children`,
   `O0_release_window`) as process etiquette, not graph-theoretic primitives.

**Footgun:** Synthesis that upgrades hub/spoke dispatch to "graph theory" or
"state embedding" (ML/KG sense) without labeling analogy invents theory the
skills do not implement.

### R4 — RotatE name collision (KG embedding ≠ mod-rotate)

**Risk:** External readers (and agents) confuse `/mod-rotate` with RotatE
(complex-space knowledge-graph embedding). House already locked the ban in
this lane; public/skill surfaces do not warn.

**Evidence:**

1. `waveset.md` Locked decision 3:

> Do not claim RotatE / complex-space KG embedding applies to mod-rotate.

2. `waveset.md` Intent notes clarifying "that was not RotatE KG embedding".

3. `README.md` skill name `/mod-rotate` with no RotatE disambiguation.
   `skills/mod-rotate/SKILL.md` title/description: thread handoff only.

**Footgun:** Any synthesis sentence tying mod-rotate to RotatE scores,
relations, or complex embeddings is poison. Disambiguation belongs in
proposed docs if anything ships later; not as an isomorphism claim.

### R5 — ROLE-COLLAPSE still live in standing/public role prose

**Risk:** Fail id `PROC-ORCH-ROLE-COLLAPSE` is named in WOF revise, and SFR
locks the triad, but shipped AGENTS/README still invite O0-as-orch or
orch-as-solo-builder collapse.

**Evidence:**

1. SFR lock (`wavves/lanes/20260723_standing-fr-revise/waveset.md` lines
   17–21):

> ### Forbidden (ROLE-COLLAPSE)
>
> - O0 must **not** background-dispatch charge workers.
> - O0 must **not** act as wave orchestrator (no mid-wave fan-out from the moderator thread).
> - Orchestrator must **not** revise FRs itself (no charge collapse into orch).

2. WOF FR fail id (`feature-requests/20260723_wave-orchestrator-fanout.md`):

> `PROC-ORCH-ROLE-COLLAPSE` | charge-worker work done inside the wave-orchestrator Task (or O0) despite triad labels

3. Live `wavves/AGENTS.md` §2 still:

> - **O0 (this thread)** is operator-facing: charters lanes, dispatches
>   sub-orchestrators in the background, reconciles returns.
> - **Dispatched orchestrators/runners** run waves…
> - **Wave subagents** take one bounded disjoint task each…

No leave-act vocabulary. No "O0 dispatches only the wave orchestrator"
fence. Rename table (wave orchestrator / charge worker) not applied.

4. `README.md` (lines 16–18):

> **Bounded waves.** A dispatched sub-orchestrator runs focused waves of
> parallel subagents with strict file ownership while the operator-facing
> thread stays small.

Collapses orch and charges under one sentence; no ban on O0 doing charge
work.

**Footgun:** Synthesis that treats current AGENTS/README as already fixing
ROLE-COLLAPSE, or that describes O0 as the wave orchestrator for RTH, is
false relative to SFR/WOF locks and this charge's own ROLE (charge, not orch).

### R6 — Public README overclaim vs thin AGENTS (visitor vs house gap)

**Risk:** README markets a full continuity stack; AGENTS is thinner on
theory claims and honest about empty rotations, but INDEX/identity still
drift.

**Evidence (paired):**

| claim surface | quote / fact |
|---|---|
| README core idea | rotation file + term identity so "stale instructions are recognizable and provenance survives" + names three DS systems |
| README tracking | **Rotation** \| `wavves/rotations/` \| handoff files with term identity (`O0.R1`, `O0.R2`, ...) |
| AGENTS | admits "None exists yet"; does **not** list Raft/StatefulSet/Erlang |
| INDEX | `current_rotation: none`, `current_identity: O0` (not `O0.R1`) |
| disk | `rotations/` empty |

**Footgun:** Synthesis that cites README as authority for "we have rotation
history" or "AGENTS encodes the same DS isomorphisms as README" is wrong on
both counts.

### R7 — Missing first-rotation / bootstrap fences in mod-rotate skill text

**Risk:** Skill assumes a prior rotation shape and concurrent-term git
rules, but bootstrap first write has no `rotations/` exemplar; identity
theory lives only in wavves-init.

**Evidence:**

1. `skills/mod-rotate/SKILL.md` line 56: follow newest `rotations/` file
   (none exist).
2. Variant A paste assumes `current rotation: rotations/rotation-r<NN>-…`
   while live INDEX says `current_rotation: none`.
3. mod-rotate never restates analogy fences for Raft/StatefulSet/Erlang;
   a rotate-only operator never sees the "analogy" obligation locked in
   this research lane.

**Footgun:** First `/mod-rotate` run invents section shape from chat memory,
or imports DS isomorphism language from README without fences.

## Cross-check: what is *not* overclaim (fair house claims)

- Hand-assigned `O0.R<N>`, never self-chosen (mod-rotate + AGENTS + init).
- Outgoing term fences itself after commit/push (mod-rotate Concurrent terms).
- Runners never git; O0 commits on operator ask (AGENTS etiquette).
- Research lane locked: no RotatE, no installed skill edits, ROLE-COLLAPSE ban
  for this dispatch.

These are operational rules. They do not require graph theory or Raft
isomorphism.

## synthesis must NOT say

Concrete bans for RTH-INT (and any proposed skill/doc delta):

1. **MUST NOT** say mod-rotate "is" Raft, StatefulSet, or Erlang, or that
   `O0.R<N>` is isomorphic to Raft terms / election generations.
2. **MUST NOT** omit the word **analogy** when naming those three borrowings.
3. **MUST NOT** claim live rotation continuity, rotation history, or
   "provenance survives via rotation files" for this home while
   `current_rotation: none` and `wavves/rotations/` is empty.
4. **MUST NOT** claim the identity scheme is fully "enforced in artifacts"
   while INDEX shows `current_identity: O0` (no `.R1`) and no rotation file
   exists.
5. **MUST NOT** call house dispatch "graph theory" or claim graph algorithms /
   embeddings; at most hub/spoke **analogy** / work-graph framing with no
   graph ops.
6. **MUST NOT** mention RotatE as applicable, related, or inspirational to
   mod-rotate (disambiguation only: "not RotatE KG embedding").
7. **MUST NOT** say ROLE-COLLAPSE is already closed in shipped AGENTS/README;
   WOF remains revised-after-WOF; leave-acts and rename are not live product
   text.
8. **MUST NOT** describe O0 as the wave orchestrator for RTH-W1, or treat
   charge findings as authored by O0/orch.
9. **MUST NOT** assert silent or already-applied edits to
   `skills/mod-rotate/SKILL.md` or `skills/wavves-init/SKILL.md`.
10. **MUST NOT** upgrade README visitor copy over AGENTS/INDEX disk state when
    they conflict; disk + INDEX win for "what is current."

## Recommended synthesis posture

- Table: **analogy vs isomorphism** with default cell = analogy for all three
  DS borrowings and for star/hub-spoke.
- Fact row: `rotations/` empty; bootstrap term claimed in AGENTS/step-log;
  INDEX identity string drifts (`O0` vs `O0.R1`).
- Optional proposed deltas only under `wavves/skills/proposed/`, and only if
  they add analogy labels + first-rotation template fence + RotatE
  disambiguation — never as "we implemented Raft."

## Commit file list (for O0 only; this charge runs no git)

- `wavves/lanes/20260723_mod-rotate-theory-research/findings/RTH-adversarial.md`
- `wavves/lanes/20260723_mod-rotate-theory-research/findings/RTH-W1e-return.md`

Exclusions: no skill edits, no README/AGENTS/INDEX edits, no BUILD.
