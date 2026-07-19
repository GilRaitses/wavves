# FR-20260715 — Paragraph tunnel gate

- **Status:** shipped (ACCEPT PASS 2026-07-18)
- **Check lane:** `wavves/lanes/20260715_paragraph-tunnel-gate-check/`
- **Build lane:** `wavves/lanes/20260715_paragraph-tunnel-build/`
- **Date:** 2026-07-15 (America/New_York)
- **Product surface:** wavves skills / charter gate templates / playbook + evals
- **Source lane evidence:** originating outbound-copy lane with a mid-render
  paragraph gate (adversarial + capped rewrite captures under that lane home).
- **evidence_verified_against:** _(pin recorded in lane home at authoring; not
  a landing commit)_
- **landing_commit_hash:** _(O0 completion report only; never self-embed in this FR)_

## Problem

Prose lint and check_gates catch banned phrases. They do not catch a
**wandering paragraph** that still "passes" mechanically: stacked claims,
meta gloss ("personality of the location"), comparisons to other shop types,
or two-sentence profiles when the job is one recognizable place fact.

**Operator lock:** "nice because" is **allowed**. Do not treat it as a fail.
Do not emit `PN-BECAUSE`, `P2-BECAUSE`, `PN-EXPLAIN`, or `P2-EXPLAIN`.

In outbound storefront copy, opener and close stabilized early. The profile
paragraph ate most operator REVISE cycles. Lint kept passing.

## Feature sketch

Add a reusable **paragraph tunnel** pattern to wavves:

1. **Adversarial gate (scoped)** — attack only a named paragraph / field
   (default: body paragraph 2). Emit fail ids from a small closed vocabulary.
2. **Rewrite gate** — if FAIL, rewrite **only** that paragraph to clear every
   fail id. Freeze sibling paragraphs. Remediation loop cap: 1.
3. **Captures** — `gate-captures/<CODE>-pN-adversarial.json` and
   `<CODE>-pN-rewrite.json` before any operator CLEARED preview or outbound.
4. **Order** — after render, before prose_lint / CLEARED preview.

### Default fail vocabulary (copy-adjacent; lane may extend)

| id | fail condition |
|---|---|
| PN-STACK | Two or more distinct claims in one paragraph |
| PN-COMPARE | Compares subject to other types or destinations |
| PN-GLOSS | Meta gloss ("personality of…", "part of how") |
| PN-FIXTURE | Fixture inventory as sole content |
| PN-MULTI | More than one sentence when tunnel requires one |

Extensions: `STANDIN`, `RESEARCH-META`, `FALSEFACT`.

**ALLOWED:** "nice because" / "because it is" as a profile frame.

**PASS:** one sentence; one concrete fact the recipient would recognize;
no gloss / compare / fixture-only / multi-sentence.

## Where it lands (locked)

| option | meaning | status |
|---|---|---|
| A | New skill `/paragraph-tunnel` | deferred |
| B | Extension to `mod-check` | struck (phase leak) |
| C | Playbook under `skills/wavves/playbooks/` + eval fixtures | **locked** |

## Worked example (live)

| tier | adversarial | rewrite |
|---|---|---|
| high Apollo | PASS | keep one-sentence sidewalk-line profile |
| mid Ardesia | operator keeps "nice because" + patio/sidewalk (agent BECAUSE ban struck) | restore nice-because patio-first line; do not strip |
| low Scotts | FAIL (COMPARE/MULTI) | drop food-shop comparison; one sentence Midtown florist on working commercial block |

## Acceptance (BUILD)

1. `python3 evals/check_paragraph_tunnel.py` PASS on `paragraph-tunnel-*` fixtures
   (include FIXTURE + STANDIN fails; include nice-because PASS).
2. Rewrite pass clears fail ids without touching frozen sibling paragraphs.
3. Dispatch template documents order: render → tunnel → lint → preview.
4. No install from this folder; ship only via chartered lane + operator accept.

## Hash hygiene (PTG-HASH)

| field | meaning |
|---|---|
| `evidence_verified_against` | Commit/state the FR or capture **evaluated** (pre-landing) |
| `landing_commit_hash` | Commit that **lands** the artifact — report only in O0 completion; never embed inside the same artifact |

Do not equate the two. Do not set either field to the hash of the commit that
contains this FR.

## Non-goals

- Replacing prose_lint / purpose-gates / public-copy-gates.
- Auto-sending outbound mail.
- Broad tone rewriting of whole emails.
- Reintroducing BECAUSE/EXPLAIN fail ids without operator ask.
- Mailbox-scale voice-clone / SFT humanizer (different product).

## Operator note

Spawned from outbound-copy clearance work. Treat as product FR for wavves.
Product shape: judgment + structure for one named paragraph (HITL rules,
adversarial mid-render, mechanical checks), not voice transfer. Keep ACCEPT
on that surface.
