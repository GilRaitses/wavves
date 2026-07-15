# FR-20260715 — Paragraph tunnel gate

- **Status:** locks-complete (awaiting BUILD charter)
- **Check lane:** `wavves/lanes/20260715_paragraph-tunnel-gate-check/`
- **Date:** 2026-07-15 (America/New_York)
- **Product surface:** wavves skills / charter gate templates / optional playbook
- **Source lane evidence:** pax APPL
  `wavves/lanes/20260715_apply-case-crack-asp-send/decisions/APPL-P2-TUNNEL.md`
  plus gate-captures `APPL-p2-adversarial.json`, `APPL-p2-rewrite.json`
- **repo_state_verified_against (evidence):** pax `21b1d7cf06557a19ee042d6fde00d60a7ed8e759`

## Problem

Prose lint and check_gates catch banned phrases. They do not catch a
**wandering paragraph** that still "passes" mechanically: stacked claims,
self-justification ("nice because"), meta gloss ("personality of the
location"), comparisons to other shop types, or two-sentence profiles when
the job is one recognizable place fact.

In APPL storefront outreach, opener and close stabilized early. Paragraph 2
(the storefront profile) ate most operator REVISE cycles. Lint kept passing.

## Feature sketch

Add a reusable **paragraph tunnel** pattern to wavves:

1. **Adversarial gate (scoped)** — attack only a named paragraph / field
   (default: body paragraph 2). Emit fail ids from a small closed vocabulary.
2. **Rewrite gate** — if FAIL, rewrite **only** that paragraph to clear every
   fail id. Freeze sibling paragraphs. Remediation loop cap: 1.
3. **Captures** — `gate-captures/<CODE>-pN-adversarial.json` and
   `<CODE>-pN-rewrite.json` before any operator CLEARED preview or outbound.
4. **Order** — after render, before prose_lint / ASP-F-style preview.

### Default fail vocabulary (copy-adjacent; lane may extend)

| id | fail condition |
|---|---|
| PN-EXPLAIN | Justifies why the subject is nice / interesting / a fit |
| PN-STACK | Two or more distinct claims in one paragraph |
| PN-COMPARE | Compares subject to other types or destinations |
| PN-BECAUSE | "nice because" / "because it is" frame |
| PN-GLOSS | Meta gloss ("personality of…", "part of how") |
| PN-FIXTURE | Fixture inventory as sole content |
| PN-MULTI | More than one sentence when tunnel requires one |

**PASS:** one sentence; one concrete fact the recipient would recognize; no
self-justification.

## Where it lands (proposed, not decided)

| option | meaning |
|---|---|
| A | New skill `/paragraph-tunnel` invoked from dispatch STEPS |
| B | Extension to `mod-check` adversarial lens + charter Step "tunneled field" |
| C | Playbook fragment under `skills/wavves/playbooks/` + eval fixture |

Open call for `/mod-decide` when chartered. Evidence so far favors **A or C**
as a reusable outbound-copy gate; **B** alone is too late (mod-check is
pre-build, this gate is mid-render).

## Worked example (live)

| tier | adversarial | rewrite |
|---|---|---|
| high Apollo | PASS | keep one-sentence sidewalk-line profile |
| mid Ardesia | FAIL (EXPLAIN/STACK/BECAUSE/GLOSS/MULTI) | one sentence: patio frontage → evening sidewalk life on west 50s Hell's Kitchen block |
| low Scotts | FAIL (COMPARE/MULTI) | drop food-shop comparison; one sentence Midtown florist on working commercial block |

## Acceptance sketch (for future charter)

1. Eval fixture: stacked / gloss / compare inputs FAIL; one-fact inputs PASS.
2. Rewrite pass clears fail ids without touching frozen sibling paragraphs.
3. Dispatch template documents order: render → tunnel → lint → preview.
4. No install from this folder; ship only via chartered lane + operator accept.

## Non-goals

- Replacing prose_lint / purpose-gates / public-copy-gates.
- Auto-sending outbound mail.
- Broad tone rewriting of whole emails.

## Operator note

Spawned from ASP/APPL clearance work. Treat as product FR for wavves, not as
an APPL residual.
