# RTH-W1b — Raft terms vs house `O0.R<N>`

Lane: `20260723_mod-rotate-theory-research`. Tip pin: `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67`.
Lens: Raft-term analogy. Verdict labels: **ANALOGY** or **ISOMORPHISM** only as stated.

## 1. What Raft terms are (external)

The following are well-known public facts about Raft consensus. They are
**not** quoted from a paper in this repo. Treat as external recall, not
house authority.

- Raft divides cluster time into **terms**, numbered by consecutive
  integers that increase over the cluster lifetime.
- A term typically begins with a **leader election**. At most one leader
  is elected for a given term (or the election fails and a new term
  starts).
- Servers carry a local `currentTerm`. RPCs (vote requests, log appends)
  include the sender's term. A server that sees a **higher** term updates
  its own term and steps down if it was leader.
- The term number is the primary way to detect **obsolete leaders** and
  to refuse or ignore messages from a prior generation.
- Log entries are also tagged with the term in which they were created.
  Safety of the replicated log depends on **majority quorums**, election
  restrictions, and commit rules, not on the term integer alone.

Raft's term is therefore a **generation counter inside a consensus
protocol**, coupled to election, vote majorities, and log replication.

## 2. What the house claims to borrow

| Source | Claim (paraphrase / short quote) | Label |
|---|---|---|
| `skills/wavves-init/SKILL.md` §4 | Scheme "borrows from three proven distributed-systems designs"; bullet **Raft terms**: "A monotonic generation integer carried on every message, so stale-generation output is recognizable on sight." | **ANALOGY** (stated borrow of generation fencing only) |
| `README.md` (core ideas, rotation bullet) | Rotation assigns "monotonic term identity (a design borrowed from Raft terms, …)" so "stale instructions are recognizable and provenance survives." | **ANALOGY** (visitor-facing) |
| `wavves/AGENTS.md` §4–5 | Live rule: `O0.R<N>` assigned by handoff; stale-term artifacts historical; newest rotation + AGENTS govern. Does **not** restate the Raft bullet. | House rule (implements the borrowed idea without re-citing Raft) |
| `skills/mod-rotate/SKILL.md` | Handoff assigns `O0.R<N+1>`; stamps; outgoing fences; concurrent-term git rules; newest rotation file governs dual claims. | House mechanics (uses term identity; no Raft protocol) |

wavves-init does **not** claim election, quorum, or log replication. The
borrowed surface it names is only: monotonic generation + stale
recognizability.

## 3. House rules that actually depend on monotonic `O0.R<N>`

These rules need a strictly increasing (or at least ordered) term ordinal.
They do **not** need Raft election or majority vote.

| House rule | Path | Depends on monotonic term? |
|---|---|---|
| Identity assigned by handoff, never self-chosen; successor block names `O0.R<N+1>` | `skills/wavves-init/SKILL.md` §4; `skills/mod-rotate/SKILL.md` variant A §0; `wavves/AGENTS.md` §4 | Yes: next term is outgoing N+1 |
| Stamp term on commits, step-log, charters; runner ids suffix `.R<N>` | `skills/wavves-init/SKILL.md` §4; `skills/mod-rotate/SKILL.md` | Yes: filterable generation label |
| Stale-term rule: older-term guidance is historical; newest term wins on conflict | `skills/wavves-init/SKILL.md` §4; `wavves/AGENTS.md` §4; `skills/mod-rotate/SKILL.md` (surviving predecessor conforms) | Yes: ordering of generations |
| Rotation filename `rotation-r<NN>-…` so lexical sort equals term order | `skills/wavves-init/SKILL.md` §4–5; `skills/mod-rotate/SKILL.md` | Yes: NN = outgoing term, zero-padded |
| Outgoing term fences itself after rotation commit/push; one paste, one successor | `skills/mod-rotate/SKILL.md` "Concurrent terms and git safety" | Yes: single active generation after handoff (by convention) |
| Dual claim of same term → newest rotation file governs, conflict logged | `skills/mod-rotate/SKILL.md` | Partial: file recency/name, not a Raft vote |
| Pickup ack states assigned identity and rotation file | `skills/wavves/playbooks/pickup.md`; rotation contract in init §5 | Yes: identity must match handoff |

**Buys (if analogy kept honest):** operators and agents can see which
generation wrote an artifact; stale threads can be demoted by rule without
replaying chat; rotation files sort into a generation sequence.

## 4. Borrowed pattern card — Raft terms

### Buys

- A short name for "this message/artifact is from generation N."
- A reason to reject or demote guidance stamped with an older `O0.R*` when
  a newer rotation exists.
- Lexical ordering of handoff files via `r<NN>`.

### Breaks (where the analogy fails)

| Raft property (external) | House reality | Consequence |
|---|---|---|
| Leader election per term | No election. Operator confirms rotate; outgoing writes successor identity. | Authority transfer is social/file handoff, not vote. |
| Majority quorum / RequestVote | Single operator, single moderator role; no peer vote. | No Raft safety proof transfers. |
| Log replication / AppendEntries | Shared truth is git + files under `wavves/`, not a Raft log. | "Term" does not commit entries across replicas. |
| Automatic step-down on higher term | Stale threads must **conform by etiquette**; nothing forces a hung chat to stop. | Fence is procedural, not protocol-enforced. |
| At most one leader per term (election invariant) | Dual claim possible; house resolves by "newest rotation file" + log | Conflict handling is house policy, not Raft. |
| Term on every RPC for cluster-wide sync | Stamps are convention on commits/prompts; not every message is an RPC. | Coverage depends on agents following stamp rules. |

### House rule that depends on it

The **stale-term rule** and **successor identity assignment**
(`wavves-init` §4, `AGENTS.md` §4, `mod-rotate` fencing) depend on
monotonic `O0.R<N>` as a generation label. They do **not** depend on Raft
election or quorum.

### Label

**ANALOGY**, not **ISOMORPHISM**.

Closest formal property that *is* shared: **monotonic generation
counter used to recognize stale authority**. That is a thin slice of Raft
terms. It is not an isomorphism to Raft consensus, leadership, or log
safety.

## 5. Failure modes if the analogy is misapplied

1. **False safety.** Believing `O0.R2` "wins" like a Raft leader after
   election. House win condition is "newest rotation file + AGENTS," not a
   majority. Two live chats can both act until etiquette fences land.
2. **Missing fence enforcement.** Expecting automatic step-down. Without
   outgoing fence + successor ack, older threads can still commit if the
   operator or tooling allows it (git rules try to prevent silent landings;
   they are not Raft).
3. **Term without handoff.** Self-chosen `O0.R*` breaks the only assignment
   path the house has. Raft servers also must not invent terms arbitrarily,
   but Raft couples increments to elections; the house couples them to a
   written rotation file.
4. **Empty `rotations/`.** Live house notes bootstrap O0.R1 with no
   rotation file yet (`wavves/AGENTS.md` §1 item 2). Term identity still
   exists; Raft-like "current term from log/election history" has no
   multi-term trail until first rotate.
5. **Overclaim in docs.** README/init "borrowed from Raft terms" read as
   "we run Raft." Correct reading: borrowed **generation-label idea** only.

## 6. Analogy vs isomorphism summary

| Property | Verdict |
|---|---|
| Monotonic generation integer | **ANALOGY** (useful; house implements via `O0.R<N>`) |
| Stale-generation recognizable on sight | **ANALOGY** (if stamps are applied) |
| Leader election | **not borrowed** |
| Majority vote / quorum safety | **not borrowed** |
| Log replication / commit index | **not borrowed** |
| Full Raft term semantics | **not isomorphism** |

## 7. Citation map (house paths only)

- Borrow claim: `skills/wavves-init/SKILL.md` §4 (Raft bullet).
- Public borrow claim: `README.md` rotation bullet (~lines 27–31).
- Live identity + stale rule: `wavves/AGENTS.md` §4–5.
- Handoff + concurrent-term fence: `skills/mod-rotate/SKILL.md`.
- Pickup ack: `skills/wavves/playbooks/pickup.md`.
- Lane framing: `wavves/lanes/20260723_mod-rotate-theory-research/waveset.md`.

External Raft facts: section 1; no paper quotes invented.
