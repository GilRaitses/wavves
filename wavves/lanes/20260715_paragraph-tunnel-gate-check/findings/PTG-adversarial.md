# PTG-W1d — adversarial lens

**Lens:** adversarial (failure modes, unsafe defaults, happy-path-only, unrunnable gates, rewrite gaming, narrow fail vocab, single-loop-cap)  
**Artifact:** `feature-requests/20260715_paragraph-tunnel-gate.md`  
**Evidence:** pax APPL-P2-TUNNEL live run under  
`/Users/gilraitses/pax/wavves/lanes/20260715_apply-case-crack-asp-send/`  
**repo_state_verified_against (check lane):** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2`  
**Date:** 2026-07-15 (America/New_York)  
**Model lock:** Grok  

## Lens lean

**REVISE**

Not BLOCK: the live tunnel pattern worked once under operator clearance and the problem statement is real. Not GO: acceptance is a sketch without a harness, the closed fail vocab undershoots documented APPL/ASP REVISE bans, rewrite is self-graded under loop cap 1 with no post-cap path, and defaults assume the APPL email anatomy happy path.

---

## Named failure modes

### FM-1 — Acceptance sketch is not a runnable gate

**Class:** gates that can't actually run  

**Claim in FR:** Acceptance sketch §1–4 ("Eval fixture: stacked / gloss / compare inputs FAIL; one-fact inputs PASS"; rewrite clears fail ids; dispatch order; no install from folder).  

**Evidence:**
- FR labels this "Acceptance sketch (for future charter)" — no command, no fixture path, no runner, no pass metric, no invoker.
- `wavves_build/evals/` has `run_fixtures.py` and other fixtures; **no** paragraph-tunnel / PN-* fixture exists (glob over `evals/` + `*paragraph*tunnel*` → FR only).
- Live "proof" is agent JSON captures (`APPL-p2-adversarial.json`, `APPL-p2-rewrite.json`), not a harness an independent agent can re-run.
- Maps directly to the house fixture class `evals/fixtures/unrunnable-gate-narrowed-adversarial-lens/` ("acceptance test suite" with zero runnable detail → REVISE).

**Risk:** Charter/build can ship "PASS" against prose acceptance while nothing machine-checkable exists. Product FR looks acceptance-ready; it is not.

---

### FM-2 — Happy-path-only live corpus; PN-FIXTURE never fires

**Class:** works on happy path only  

**Evidence:**
- Adversarial capture has exactly three hand-shaped cases: high already PASS; mid triggers EXPLAIN/STACK/BECAUSE/GLOSS/MULTI; low triggers COMPARE/MULTI (`APPL-p2-adversarial.json`).
- **P2-FIXTURE / PN-FIXTURE never appears** in live fail_ids, despite being in the default vocabulary and heavily banned in ASP-ASK + facade weave ("awning/glass as the only characterizing content", planters/curb glass).
- High Apollo line was already tunnel-compliant; it does not stress the gate.
- Mid rewrite PASS and low rewrite PASS after one compression each (`APPL-p2-rewrite.json` `re_adversarial`).

**Risk:** Vocabulary and loop look complete because the only FAIL inputs were the ones the vocab was written from. Fixture-inventory and stand-in modes from earlier ASP drafts are untested.

---

### FM-3 — Closed fail vocab misses documented APPL/ASP REVISE modes

**Class:** over-narrow fail vocabulary  

**Documented second-line bans outside PN-*/P2-* table:**

| REVISE / ban source | Mode | In FR default vocab? |
|---|---|---|
| ASP-ASK-research-call.md | "looked like a fair stand-in" | **No** |
| ASP-ASK | "early research phase" / "the part I care about most" / "how those …" | **No** |
| facade-weave-v0.md | "looked like a fair stand-in"; research-meta bleed into P2 | **No** |
| ASP-ASK + APPLY intent | Wrong / invented place fact (truthfulness vs Places/CASE) | **No** |
| tone-branch-examples.md (prior pack) | Soft category stand-in without owner-recognizable fact | Only weakly via STACK/FIXTURE; no dedicated id |
| Operator REVISE history (APPL-W1-RECONCILE) | Close/ask anatomy changes | Correctly out of tunnel scope — but shows most REVISE cycles were **not** P2-vocab failures |

**Evidence:** ASP-ASK explicitly lists stand-in + research-meta bans for the second line; FR problem statement cites "wandering paragraph" from APPL cycles, then freezes a copy-adjacent seven-id set that omits those bans. Live mid/low FAILs are only the synonym-rich "nice because / personality / compare" cluster the table already names.

**Risk:** Agent PASS on a one-sentence stand-in ("X looked like a fair stand-in for a Midtown florist") or research-meta leak, or a fluent false fact, because none of those ids exist. "Lane may extend" is optional — unsafe default is ship closed vocab as-is.

---

### FM-4 — Rewrite-loop gaming under self-graded re-adversarial

**Class:** rewrite loop gaming / unsafe default (same agent attack→rewrite→judge)  

**Evidence:**
- FR: FAIL → rewrite only that paragraph to clear every fail id; loop cap 1; then captures before CLEARED.
- Live rewrite capture records `cleared_fail_ids` then `re_adversarial` PASS with **empty notes and no re-stated p2 under the re-check** (`APPL-p2-rewrite.json`). Same wave owns Gate 1, Gate 2, and re-check.
- Mid `after`: "Ardesia Wine Bar's patio frontage opens into evening sidewalk life on a west 50s Hell's Kitchen block." Still packs **frontage scene + sidewalk life + block geography** in one sentence — STACK was "cleared" by joining claims, not by reducing to one fact. Operator later CLEARED (`APPL-ACCEPT.md`), so product-acceptable ≠ vocab-strict.
- Gaming paths the FR does not block:
  - MULTI → one sentence via semicolon / relative clause while keeping STACK content.
  - BECAUSE/EXPLAIN → synonym swap ("notable for", "known for") without PN-BECAUSE lexemes.
  - GLOSS → paraphrase without "personality of" / "part of how".
  - COMPARE → delete second sentence; leave comparative adjective in the first.
  - List `cleared_fail_ids` without proving independent re-attack.

**Risk:** Cap-1 + self-grade = optimize for id clearance, not owner-recognizable single fact. Tunnel becomes a capture ritual.

---

### FM-5 — Single-loop-cap (1) with no post-cap behavior

**Class:** single-loop-cap risk / unsafe default vs charter norm  

**Evidence:**
- FR + APPL-P2-TUNNEL: remediation loop cap **1** (one rewrite, re-run Gate 1).
- House charter default remediation cap is **2** with escalate-to-O0 on exhaustion (`skills/charter/SKILL.md`).
- FR never states: if re-adversarial still FAIL after the one rewrite → escalate? block preview? operator REVISE? leave FAIL and proceed to lint?
- APPL waveset acceptance: "P2 adversarial PASS (or FAIL→rewrite→PASS)" — assumes the happy transition; no FAIL residual path.
- Mid live case cleared **five** fail ids in one rewrite — worked once; does not prove cap-1 is enough when rewrite introduces FIXTURE or a new STACK shape.

**Risk:** At cap, runner either (a) ships FAIL silently past tunnel into lint/preview, or (b) stalls with no escalation contract. Cap-1 is stricter than house default without compensating escalate rule.

---

### FM-6 — Unsafe defaults: paragraph-2 email anatomy + agent-only gate

**Class:** unsafe defaults  

**Evidence:**
- FR default scope: "named paragraph / field (default: body paragraph 2)". Assumes APPL storefront email shape (opener / profile / close). Options A/C as skill/playbook would export that default into non-email or multi-profile bodies.
- Order: render → tunnel → lint → preview. Tunnel PASS does not check truthfulness against Places/CASE; lint does not check PN-* modes (`APPL-prose.json` passed drafts that still needed P2 tunnel — correct ordering, but tunnel remains non-scripted judgment).
- No requirement for disjoint evaluator (charter rule: gate graded by evaluator with no authorship of the wave). Live run collapses author/attacker/rewriter/judge.

**Risk:** Reuse outside APPL inherits P2 index and judgment-only enforcement; false confidence relative to prose_lint (which is actually runnable).

---

### FM-7 — Evidence provenance drift for "live run validates FR"

**Class:** works on happy path only / grounding bleed into adversarial trust  

**Evidence:**
- FR cites pax evidence hash `21b1d7cf06557a19ee042d6fde00d60a7ed8e759` (matches `APPL-ACCEPT.md`).
- Tunnel decision + both P2 captures cite `079f4c4cacb961996b23e66bd7749b4e243708f8`.
- Product FR treats one three-shop clearance as reusable pattern proof.

**Risk:** Not a blocker alone, but packaging "live run" as validation without a harness means the only regression oracle is narrative. Hash split shows captures and clearance are not one frozen evidence pin.

---

## What the live run does prove (bounded)

- A scoped adversarial vocabulary can catch the specific mid/low wandering profiles that prose_lint missed (`APPL-prose.json` OK vs `APPL-p2-adversarial.json` FAIL).
- Sibling freeze + one rewrite can produce operator-CLEARED one-liners (`APPL-ACCEPT.md`).
- That is existence proof for the **problem** and a **manual pattern**, not acceptance for a reusable wavves skill/playbook.

## Gaps that must land before GO (for this lens)

1. Runnable eval fixture path + command + pass metric (or explicitly defer acceptance and strip "acceptance sketch" language that reads like a gate).
2. Extend default fail vocab (or required lane-extension checklist) to cover ASP-ASK stand-in / research-meta / false-fact modes; add a FIXTURE-positive fixture.
3. Define post-cap-1 behavior (escalate to O0 with named residual fail ids; do not proceed to CLEARED preview).
4. Separate re-adversarial authorship from rewrite (or require scripted/fixture checks for MULTI/COMPARE/BECAUSE lexemes at minimum).
5. Default field selector must be charter-required, not silent "paragraph 2".

## Lens verdict

**REVISE** — ship-as-reusable-gate is premature; problem and manual APPL pattern are real.
