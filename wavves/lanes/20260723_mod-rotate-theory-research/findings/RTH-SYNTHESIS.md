# RTH-SYNTHESIS — mod-rotate theory (operator brief)

| Meta | |
|---|---|
| role | wave_orchestrator / INT editor (RTH-INT) |
| moderator | O0 |
| tip | `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67` |
| authority | `decisions/RTH-INT-UNLOCK.md` + W1e bans (W1e remains **FAIL**) |
| scope | research memo only; no installed skill edits; no git; no BUILD; no ACCEPT |

## One-page operator brief

**What mod-rotate is.** A file handoff so a fresh thread resumes from repo
state. Variant A writes `wavves/rotations/rotation-r<NN>-….md` and assigns
successor `O0.R<N+1>`. Variant B hands one lane via a five-file packet.
Identity is assigned by the handoff (never self-chosen); older-term output
is historical when a newer rotation + `AGENTS.md` govern.

**What the DS names buy (analogy only).** Raft terms, StatefulSet ordinals,
and Erlang incarnations are teaching borrows for a monotonic generation
label, a filterable compound name, and succession/stale-authority doctrine.
None of them is implemented as a protocol here: no election, no quorum, no
replica set, no runtime reject-stale wire. House fences are etiquette +
handoff file + stamps when those artifacts exist.

**What the star buys (analogy only).** Moderator (O0) → wave orchestrator →
charge workers is a hub/spoke work graph for dispatch and leave-acts
(`return_to_O0`, `yield_awaiting_children`, `O0_release_window` in the
revised WOF FR). That is process framing, not graph algorithms. A rotation
file is a durable **snapshot** of that work graph for hydration. It is not
a vector embedding, knowledge-graph embedding, or RotatE (disambiguation
only: `/mod-rotate` is **not** RotatE KG embedding).

**Honesty constraint from W1e (still FAIL).** Shipped README/wavves-init
name the three borrows without the word **analogy**, and visitor copy can
read as live continuity. Disk + INDEX win: this home has no rotation file
yet. ROLE-COLLAPSE locks live in SFR/WOF research/FR text; they are **not**
already closed in shipped AGENTS/README. Charge findings were authored by
charge workers, not by O0.

**Related seam (pointer only).** Durable resume across yield / proceed /
hydrate is sketched as a **context cache** analogy in
`feature-requests/20260723_wave-context-kv-cache.md`. That FR is analogy to
transformer KV caching (new step = Q against cached K/V); it is **not**
transformer KV isomorphism and not RotatE.

## Analogy vs isomorphism

Default cell = **analogy**. No row claims protocol isomorphism.

| Pattern | House surface | Label | Buys | Breaks | House rule that depends |
|---|---|---|---|---|---|
| Raft terms | `O0.R<N>` generation stamp | **analogy** | stale recognizability when stamps exist | no election, majority, or log replication | stale-term rule; successor `N+1`; `rotation-r<NN>` sort |
| StatefulSet ordinals | compound `O0` + `R<N>`; runner `.R*` | **analogy** | filterable compound name; stamp habit | not concurrent peer replicas | stamp on commits/charters; runner provenance suffix |
| Erlang incarnations | succession; stale = history | **analogy** | new term = new incarnation of the role | no runtime drop of wrong-term messages | handoff-assigned identity; pickup ack; outgoing fence |
| Hub/spoke (star) | O0 → wave orch → charges | **analogy** | clear fan-out ownership; leave-act edges | no graph ops / adjacency algorithms | ROLE-COLLAPSE ban (FR/SFR); orch integrates before `return_to_O0` |
| Rotation "state embedding" | rotation / handoff files | **analogy** (snapshot) | successor hydrates from files | not ML/KG/vector embedding | variant A/B serialization; hydrate-from-files rule |

## Fact row (disk + INDEX win)

Remeasured at INT write time:

| Fact | Measured |
|---|---|
| `wavves/rotations/` | empty (zero files) |
| `wavves/INDEX.md` `current_rotation` | `none` |
| `wavves/INDEX.md` `current_identity` | `O0` (bare; no `.R1`) |
| AGENTS / step-log bootstrap claim | prose claims `O0.R1` bootstrap with no rotation file yet |
| Identity string drift | INDEX `O0` vs AGENTS `O0.R1` — both house surfaces; they disagree |

Do not treat README continuity language as measured for this home while the
table above holds.

## Optional proposed deltas

Draft only (not installed). Paths:

- `wavves/skills/proposed/20260723_mod-rotate-analogy-fences.md`

Covers: analogy labels on the three borrows; first-rotation template fence
when `rotations/` is empty; RotatE disambiguation line; pointer to
FR-20260723 context-cache seam. Moderator reviews before any accept path.

## Open calls (for `/mod-decide` if prose change is wanted)

1. **ANALOGY-LABEL** — add explicit **analogy** wording to wavves-init §4
   and/or README rotation bullet (proposed draft only until accepted).
2. **FIRST-ROTATION** — ship `_template` under `rotations/` vs skill-only
   first-write prose (also open on FR-20260723 CACHE / ROTATION-TEMPLATE).
3. **INDEX-IDENTITY** — align INDEX `current_identity` to `O0.R1` during
   bootstrap, or document bare `O0` as intentional until first rotate.
4. **ROLE-COPY** — land WOF leave-acts + rename into AGENTS/README via the
   WOF BUILD path (not claimed done here).

## Sources (W1; not re-authored)

- `findings/RTH-cite-map.md` (PASS)
- `findings/RTH-raft-terms.md` (PASS)
- `findings/RTH-ordinal-incarnation.md` (PASS)
- `findings/RTH-star-graph.md` (PASS)
- `findings/RTH-adversarial.md` (FAIL honesty gate; bans obeyed)
- `findings/RTH-W1-rollup.md`

## Ban compliance (W1e § synthesis must NOT say)

Obeyed bans 1–10: no Raft/StatefulSet/Erlang isomorphism; **analogy** used
when naming borrows; no live continuity claim against empty `rotations/`;
no "fully enforced in artifacts" while INDEX shows `O0`; hub/spoke framed
as analogy not graph theory; RotatE only as "not RotatE"; ROLE-COLLAPSE not
claimed closed in shipped product text; O0 not described as RTH-W1 wave
orch; no silent skill edits asserted; disk+INDEX win over README on conflict.

## Next (for O0)

- Reconcile this synthesis.
- **RTH-ACCEPT** remains gated until O0 unlocks it.
- No git from orch. Commit file list for O0 only (below).

```text
wavves/lanes/20260723_mod-rotate-theory-research/findings/RTH-SYNTHESIS.md
wavves/skills/proposed/20260723_mod-rotate-analogy-fences.md
```
