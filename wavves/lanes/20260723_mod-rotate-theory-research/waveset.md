# RTH — mod-rotate theory research

| Meta | |
|---|---|
| lane code | RTH |
| owner | O0 (moderator); dispatched orch RTH-W1 |
| type | research / read-only |
| `repo_state_verified_against` | `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67` (local `main` tip at charter) |
| `proof_required` | n/a — research memo + citation map; no visitor/product Proof surface |
| proof rationale | outputs are findings and a synthesis memo, not a product demo |

## Intent

Operator: deeper research into the applied graph / distributed-systems theory
behind **mod-rotate** (after clarifying that was not RotatE KG embedding).
Produce a grounded map of what the house already claims, what the analogies
actually buy, where they break, and what (if anything) should become a
docs/skill delta — without installing skills or chartering BUILD.

## Grounding (verified paths)

| seam | path | role |
|---|---|---|
| rotate skill | `skills/mod-rotate/SKILL.md` | handoff mechanics, variants A/B, git fencing |
| rotate playbook | `skills/wavves/playbooks/rotate.md` | router steps |
| pickup | `skills/wavves/playbooks/pickup.md` | successor ack / identity |
| identity source | `skills/wavves-init/SKILL.md` §4–5 | Raft / StatefulSet / Erlang borrow; rotation contract |
| standing home | `wavves/AGENTS.md` §4–5 | live term + rotation contract |
| public claim | `README.md` (rotation + term identity) | visitor-facing analogy statement |
| fan-out leave-acts | `feature-requests/20260723_wave-orchestrator-fanout.md` | hub/spoke leave-acts (revised-after-WOF) |
| SFR role split | `wavves/lanes/20260723_standing-fr-revise/waveset.md` | moderator ≠ orch (ROLE-COLLAPSE) |
| rotations dir | `wavves/rotations/` | currently empty / none in INDEX |

Root constraint: house prose names three DS borrowings and a star-shaped
dispatch graph, but has no research memo separating **isomorphism** from
**analogy**, nor a citation map tying each rotation rule to a named pattern.

## Locked decisions (do NOT reopen)

1. This lane is **research only**. No edits to `skills/mod-rotate/SKILL.md`,
   `skills/wavves-init/SKILL.md`, or installed router skills.
2. Skill deltas land only as `wavves/skills/proposed/` drafts if warranted;
   moderator reviews before any accept path.
3. Do not claim RotatE / complex-space KG embedding applies to mod-rotate.
4. Analogies must be labeled **analogy** unless a rule is shown to match a
   cited formal property (term monotonicity, stale-generation fencing, etc.).
5. Foreign repos (pax, etc.) are illustration only; remasureable pins required.
6. Model for judgment lenses: `cursor-grok-4.5-high-fast`. No Claude/Composer
   fallback for RTH waves.
7. Git ban for orch and runners. O0 lands commits only on operator ask.
8. ROLE-COLLAPSE ban: O0 dispatches **only** the wave orchestrator; orch
   deploys charge workers; orch writes rollup/synthesis integrate.

## Wave structure

### RTH-W1 — discovery (parallel, read-only)

Five charges; each owns one findings file:

| id | lens | owns |
|---|---|---|
| RTH-W1a | cite-map | `findings/RTH-cite-map.md` — every house claim about rotation identity / handoff / star, with path+quote |
| RTH-W1b | Raft-term | `findings/RTH-raft-terms.md` — what Raft terms are; what wavves copies; mismatches; failure modes if misapplied |
| RTH-W1c | ordinal-incarnation | `findings/RTH-ordinal-incarnation.md` — StatefulSet ordinals + Erlang incarnations vs O0.R\<N\> / runner suffixes |
| RTH-W1d | star-graph | `findings/RTH-star-graph.md` — hub/spoke + leave-acts + state-snapshot “embedding” as graph serialization (not ML embedding) |
| RTH-W1e | adversarial | `findings/RTH-adversarial.md` — overclaim, false isomorphism, missing fences, empty rotations/, ROLE-COLLAPSE |

### RTH-INT — synthesis (single serialized editor, after W1)

One editor writes `findings/RTH-SYNTHESIS.md`:
- one-page operator brief
- analogy vs isomorphism table
- recommended docs/skill proposed deltas (optional files under
  `wavves/skills/proposed/` only if evidence supports)
- open calls for `/mod-decide` if any prose change is recommended

GATED: orch pauses for O0 approval before RTH-INT if W1e returns FAIL on
honesty/overclaim that would poison synthesis.

### RTH-ACCEPT — research accept (GATED)

Independent of synthesis author. Runnable bar (no product Proof):
- All five W1 files exist and cite remasureable paths
- Synthesis does not assert RotatE or silent skill edits
- Capture `gate-captures/RTH-ACCEPT.md` with checklist PASS/FAIL

Remediation loop cap: 2.

## Acceptance criteria

1. Cite-map covers mod-rotate, wavves-init §4–5, AGENTS §4–5, README rotation
   blurb, pickup ack, and WOF leave-acts (or explicit gap).
2. Each borrowed pattern has: **buys**, **breaks**, **house rule that depends
   on it**.
3. Star-graph note defines state snapshot ≠ vector embedding in one locked
   sentence.
4. Adversarial lens lists at least three overclaim risks with evidence.
5. No installed skill mutation; commit file list for O0 only.

## Gated waves

- RTH-INT: gated if adversarial FAIL; else orch may run INT then pause before ACCEPT
- RTH-ACCEPT: always gated on O0 before claiming lane complete

## Model routing

| role | recommended_model_tier | reason | expected_context | expected_file_reads | cost_caveat |
|---|---|---|---|---|---|
| lane orch RTH-W1 | high-reasoning | fan-out + integrate | lane home + five returns | waveset, charges, returns | keep to lane |
| RTH-W1a cite-map | fast | inventory + quotes | skills + README | ≤15 files | quote-bound |
| RTH-W1b Raft | high-reasoning | analogy judgment | init §4 + external recall labeled | ≤10 | no fake cites |
| RTH-W1c ordinal | high-reasoning | analogy judgment | init §4 + mod-rotate | ≤10 | no fake cites |
| RTH-W1d star-graph | high-reasoning | graph framing + WOF | mod-rotate + WOF FR + SFR waveset | ≤12 | |
| RTH-W1e adversarial | high-reasoning | overclaim hunt | all of above | ≤20 | |
| RTH-INT | high-reasoning | synthesis | five findings | findings/* | |
| RTH-ACCEPT | high-reasoning | independent check | synthesis + findings | gate checklist | |

Concrete slug when environment allows: `cursor-grok-4.5-high-fast`.

## Escalation (operator-protection)

Dispatched orch answers to O0 only. No direct operator solicitation.
Escalate: skill-edit temptation, need to invent external paper cites without
fetch, conflict with locked “research only”, empty rotations/ blocking claims
of live term history.
