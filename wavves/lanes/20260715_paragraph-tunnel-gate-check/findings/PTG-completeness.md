# PTG-W1c — completeness lens

- **Date:** 2026-07-15 (America/New_York)
- **Lane:** PTG (`20260715_paragraph-tunnel-gate-check`)
- **Lens:** completeness (missing AC, unowned edges, silent assumptions, rollback / non-goals, open calls BUILD needs)
- **Artifact:** `feature-requests/20260715_paragraph-tunnel-gate.md`
- **repo_state_verified_against:** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` (wavves_build `main`)
- **Evidence read:** outbound copy lane P2-TUNNEL decision, gate-captures p2-adversarial and p2-rewrite JSON; wavves surfaces `skills/mod-check/SKILL.md`, `skills/mod-decide/SKILL.md`, `skills/charter/SKILL.md`, `skills/charter/EXECUTION_WIRING.md`, `evals/README.md`, `docs/purpose-gates.md`, `docs/public-copy-gates.md`, `feature-requests/README.md`, `skills/wavves/playbooks/`
- **model_enforcement:** Grok only (cursor-grok-4.5-high-fast)
- **statement:** read-only; no git; no code edits outside this findings file

## Lens lean: REVISE

FR is strong enough for `/mod-decide` on landing shape, but incomplete as a BUILD-ready product sketch. Named gaps below must land as locked open calls (or FR patches) before `/charter`. Not BLOCK: problem, vocabulary, order relative to lint, worked example, and thin non-goals already exist. Not GO: invoker, model tier, eval shape, fail-after-cap, and gate-family relation are unowned.

---

## Named gaps

### G-LANDING — Landing option A|B|C not locked

**What is missing:** FR proposes A (skill), B (mod-check lens), C (playbook + eval) and defers pick to `/mod-decide`. Lean A or C; B alone rejected as too late. No pick, no hybrid rule (A+C), no implications table for BUILD file list.

**Blocks plan?** Yes for BUILD charter. Does not block finishing this mod-check if verdict routes to mod-decide with this call first.

---

### G-INVOKE — Who invokes, when, on what STEPS surface

**What is missing:** Sketch says "invoked from dispatch STEPS" (option A) without: which template family (outbound ASP/outbound-copy-style vs any render lane), which role runs the gate (dispatch runner vs O0), whether tunnel is mandatory before CLEARED preview or opt-in per charter Step, and how a lane names the tunneled field (default p2 vs arbitrary field path).

**Blocks plan?** Yes for BUILD wiring. Silent assumption today: every consumer has a "render → preview" mid-pipeline like outbound copy.

---

### G-MODEL — Model tier for adversarial + rewrite unset

**What is missing:** No recommended tier for Gate 1 (adversarial) or Gate 2 (rewrite). Charter skill defaults adversarial/acceptance to `high-reasoning`; FR never binds that. No cost caveat (two LLM calls per draft + re-adversarial).

**Blocks plan?** Yes for dispatch prompts and cost discipline. Does not block mod-decide on landing alone.

---

### G-EVAL — Eval fixture structure underspecified vs repo `evals/`

**What is missing:** Acceptance sketch item 1 says "stacked / gloss / compare FAIL; one-fact PASS" but does not own:

- home (`evals/fixtures/<case>/` vs lane-local vs skill-adjacent)
- layout (`input.md` + `expected.md` like current corpus, or JSON captures like outbound copy)
- pass metric / runnable command (contrast `python3 evals/run_fixtures.py`, which is lens-wording tripwire only, not LLM judgment)
- whether tunnel evals need a real replay harness (evals/README already calls this a known gap for mod-check fixtures)

Outbound copy captures prove a JSON shape that works; FR does not freeze that schema as the product fixture contract.

**Blocks plan?** Yes for acceptance wave. Non-blocking for check→decide if listed as open call "fixture home + schema."

---

### G-AC-THIN — Acceptance sketch not runnable

**What is missing beyond the four bullets:**

| missing AC | why it matters |
|---|---|
| Re-adversarial after rewrite is mandatory | Outbound copy does it (`re_adversarial`); FR loop cap 1 implies rewrite then stop without naming re-check PASS |
| Sibling-freeze verify method | "without touching frozen siblings" has no hash/diff/capture field |
| Capture required before CLEARED/preview | Order stated; hard fail if capture absent not stated |
| Closed vocabulary as allow-list | "lane may extend" with no merge/version rule |
| PN-* vs evidence P2-* id mapping | Product renames P2→PN; no compat/migration note for consumers reading outbound copy captures |

**Blocks plan?** Partially. Re-adversarial + freeze verify + capture-hard-fail should be AC before BUILD; id rename is non-blocking documentation.

---

### G-FAIL-CAP — Fail-after-remediation-cap unowned

**What is missing:** Loop cap 1 is set. Behavior when rewrite still FAILs is absent: block preview, escalate to operator REVISE, keep last draft, or hard-stop outbound. Charter EXECUTION_WIRING requires escalate at cap, not silent loop.

**Blocks plan?** Yes for safe mid-render use. Blocks GO for BUILD until decide/lock.

---

### G-ROLLBACK — No disable / rollback surface

**What is missing:** No way to turn the tunnel off per lane, no "ship bad skill → remove STEPS line / proposed→withdrawn" rollback, no non-goal that tunnel failure must not auto-send (auto-send is non-goal; disable path is not). Non-goals list three items only.

**Blocks plan?** Soft-block for charter escalation text. Non-blocking for mod-decide if added as decide call or FR patch under Non-goals / Rollback.

---

### G-GATE-FAMILY — Relation to prose_lint / purpose-gates / public-copy-gates incomplete

**What is present:** Order "after render, before prose_lint / ASP-F-style preview"; non-goal "not replacing" those three.

**What is missing (positive contract):**

- Whether tunnel PASS still requires `check_public_copy.py` / purpose-gates / project `prose_lint` (assume yes; not written)
- Overlap risk: purpose-gates PG2 rewards causal multi-sentence synthesis on marketing surfaces; tunnel PN-MULTI/PN-STACK punish multi-claim paragraphs on outbound email — scope boundary (email body field vs landing/README) not stated
- `prose_lint` / `check_gates` are not first-class wavves_build skills; they are consumer-lane tools. FR treats them as ambient without citing install path
- ASP-F is outbound-copy-specific; "ASP-F-style preview" has no generic wavves name/owner

**Blocks plan?** Yes for correct integration narrative. Does not block check if elevated to open call "gate-family matrix."

---

### G-OPEN-CALLS — Open calls list incomplete for BUILD

FR explicitly opens landing (A/B/C). Completeness requires these additional decide/BUILD calls (not inventing product forks beyond what the sketch leaves silent):

1. **Landing** — A, C, or A+C (B alone already rejected in prose)
2. **Invoker contract** — who / when / field selector
3. **Model tiers** — adversarial vs rewrite (likely both high-reasoning)
4. **Eval home + schema** — freeze outbound-copy-like JSON vs `evals/fixtures` markdown pair; name pass command
5. **Fail-after-cap policy** — escalate vs block preview
6. **Gate-family matrix** — tunnel ⊅ replace lint/purpose/public-copy; scope = named outbound field only
7. **Skill lifecycle** — if A: proposed → moderator → operator → accepted path owned (wavves-init); FR never mentions promotion
8. **Rollback/disable** — STEPS flag or skill withdrawal

Missing (1)–(6) block BUILD. (7)–(8) block clean charter handoff.

---

### G-ASSUME — Silent assumptions (document or lock)

| assumption | risk if wrong |
|---|---|
| Tunneled unit is always one sentence | Lanes needing two-sentence facts inherit PN-MULTI false fails |
| Vocabulary is storefront/outreach-shaped | Reuse on non-shop copy misfires (PN-FIXTURE, PN-COMPARE) |
| Adversarial judgment is LLM-only | No mechanical fallback; cost and nondeterminism unowned |
| Consumer dispatch has render step | Skill with nowhere to hang |
| Worked example = acceptance corpus | Three shops are narrative evidence, not frozen fixtures in wavves_build |

**Blocks plan?** Assumptions block BUILD quality if unstated; non-blocking for mod-check if listed under Locked decisions / Non-goals.

---

### G-NONGOALS-THIN — Non-goals gaps

Present: no replace lint family; no auto-send; no whole-email rewrite.

Absent:

- Not a mod-check Wave-1 lens (reinforces B rejection)
- Not a substitute for `evals/check_public_copy.py` or purpose-gates on landing/README
- Not required on lanes without outbound rendered paragraphs
- Not expanding fail vocabulary without lane charter amend
- Not claiming mechanical determinism

**Blocks plan?** No, if patched into FR or decide packet. Completeness flag only.

---

## Covered adequately (for this lens)

- Problem statement vs lint-pass wandering prose
- Closed fail-id vocabulary (copy-adjacent defaults)
- Remediation loop cap stated (value 1)
- Capture naming pattern `<CODE>-pN-adversarial|rewrite.json`
- Order relative to prose_lint / preview (directionally)
- Worked example grounded in live outbound copy captures
- Explicit deferral of landing to `/mod-decide`
- Ship path: chartered lane + operator accept; no install from feature-requests/
- Thin non-goals skeleton exists

---

## Completeness bullets for O0

1. Lock landing (A / C / A+C) before BUILD; keep B-alone rejected.
2. Own invoker: who, when, field selector, mandatory vs opt-in.
3. Bind model tiers for adversarial + rewrite; note dual-call cost.
4. Freeze eval home/schema/pass metric; do not treat outbound copy narrative table as the fixture corpus.
5. Add AC: re-adversarial after rewrite, sibling-freeze verify, capture-before-preview hard fail, fail-after-cap escalate.
6. Write gate-family matrix vs prose_lint / purpose-gates / public-copy-gates (complement, scoped field).
7. Add rollback/disable + skill-promotion path if option A.
8. Expand non-goals so ACCEPT cannot silently widen to mod-check lenses or landing-page purpose-gates.

## Explicit non-actions

- No `PTG-verdict.md` (O0)
- No FR rewrite
- No BUILD plan
- No git
