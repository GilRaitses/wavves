# Proposed — mod-rotate / init analogy fences (RTH)

| Meta | |
|---|---|
| status | proposed (not installed) |
| source lane | `wavves/lanes/20260723_mod-rotate-theory-research/` |
| evidence | `findings/RTH-SYNTHESIS.md`, W1b/W1c/W1e |
| authority | moderator review + operator ask before any accept |

This draft does **not** edit `skills/mod-rotate/SKILL.md` or
`skills/wavves-init/SKILL.md`. It records candidate text only.

## Intent

Close honesty gaps without claiming protocol isomorphism:

1. Label the three DS borrowings as **analogy**.
2. Fence first rotation when `wavves/rotations/` is empty.
3. Disambiguate `/mod-rotate` from RotatE KG embedding.
4. Point durable resume at the context-cache FR (analogy only).

## Candidate delta A — wavves-init §4 (analogy labels)

Replace the "borrows from three proven distributed-systems designs" lead-in
with wording that forces the analogy label, for example:

> The scheme uses three **analogies** from distributed systems (not protocol
> isomorphisms). House fences are handoff files, stamps, and etiquette; there
> is no Raft election/quorum, no StatefulSet controller, and no Erlang
> distribution layer.
>
> - **Raft terms (analogy).** …
> - **Kubernetes StatefulSet ordinals (analogy).** …
> - **Erlang incarnation numbers (analogy).** …

Do not claim the identity scheme is fully "enforced in artifacts" while
INDEX may show bare `O0` and `current_rotation: none`. Prefer: "enforced in
artifacts when rotation files and INDEX stamps exist; bootstrap may be
prose-only until first rotate."

## Candidate delta B — mod-rotate first-rotation fence

After "Follow the section shape of the newest existing file in `rotations/`":

> If `rotations/` is empty (INDEX `current_rotation: none`), this is the
> **first** whole-orchestrator rotation. Do not invent section shape from
> chat. Write `rotation-r01-<YYYYMMDD>-<HHMM>.md` using the section order in
> this skill (Successor identity first, then Positions, Active background
> dispatches, Blocked items, Uncommitted local state, Operator-pending
> decisions, Active model policy, Provenance pointer), or from
> `wavves/rotations/_template.md` if that template has been landed. Outgoing
> term for bootstrap first rotate is the live bootstrap identity (AGENTS
> claims `O0.R1`); successor is `O0.R2`. Do not claim multi-term rotation
> history until at least one rotation file exists on disk.

Optional companion (separate land): add
`wavves/rotations/_template.md` — open call on FR-20260723
(ROTATION-TEMPLATE).

## Candidate delta C — RotatE disambiguation (mod-rotate frontmatter or When to use)

One line only:

> Name note: `/mod-rotate` is thread handoff with term identity. It is **not**
> RotatE (knowledge-graph embedding).

## Candidate delta D — README visitor bullet (if operator wants public align)

Keep the three names only if each is marked **analogy**, and do not assert
live provenance via rotation files while `current_rotation: none`. Prefer
pointing visitors at `wavves/AGENTS.md` + INDEX for current measured state.

## Related seam (pointer; not this install)

`feature-requests/20260723_wave-context-kv-cache.md` — durable checkpoint /
standing remasure / rotation hydration as a **context cache** analogy
(new notify/proceed/hydrate step = Q against cached K/V). **Not**
transformer KV isomorphism. **Not** RotatE. Bind first-rotation fence
(KV-03) when that FR is decided/BUILT.

## Accept bar (for O0 / operator later)

- [ ] Analogy labels present wherever Raft / StatefulSet / Erlang are named
- [ ] First-rotation empty-dir path spelled (template or skill prose)
- [ ] RotatE disambiguation present on mod-rotate surface
- [ ] No claim of Raft/StatefulSet/Erlang isomorphism
- [ ] No claim ROLE-COLLAPSE already closed (that is WOF BUILD, not this delta)
- [ ] Installed files changed only after operator ask; this file alone is not install

## Ban reminder

Obey RTH-adversarial "synthesis must NOT say" bans 1–10 when editing product
copy. Disk + INDEX win over marketing prose on conflict.
