# PTB-W1d — Adversarial discovery: BUILD footguns

**Lane:** `wavves/lanes/20260715_paragraph-tunnel-build/`  
**Role:** PTB-W1d (adversarial)  
**Date:** 2026-07-15 (America/New_York)  
**repo_state_verified_against:** `f2fb8ce144b68d820b0992f5075a2cbbf44673d2`  
**Scope:** Footguns and anti-patterns W2 must avoid. Findings only. No product edits. No git.

**Hydrated:** `waveset.md`, `decisions/LOCKED-DECISIONS.md`, FR
`feature-requests/20260715_paragraph-tunnel-gate.md`, PTG-LAND through
PTG-HASH, outbound copy lane-P2-TUNNEL + captures, `evals/run_fixtures.py` + README known
limitation, `skills/wavves/playbooks/check.md`.

---

## Ranked top 5 (severity order)

| rank | footgun | severity |
|:----:|---------|----------|
| 1 | Phase leak: mid-render tunnel wired as / into mod-check (Option B) | **BLOCK** |
| 2 | Overloading `run_fixtures.py` / lens-wording tripwire with tunnel cases | **BLOCK** |
| 3 | LLM-only acceptance without mechanical fixtures / checker | **BLOCK** |
| 4 | Auto-pass after fail-cap (or silent keep / second rewrite) | **BLOCK** |
| 5 | Fixtures that only cover outbound copy lane three-shop happy path (no FIXTURE/STANDIN) | **HIGH** |

---

## Footgun catalog (required coverage + adjacent)

### 1. Phase leak: mid-render tunnel ≠ mod-check (Option B struck)

| field | content |
|---|---|
| **Severity** | BLOCK |
| **What it looks like** | Playbook or WIRING note tells runners to invoke tunnel via `/mod-check`, extend `skills/mod-check/SKILL.md` lenses, or place tunnel inside check-wave STEPS. Or documents Option B as alternate path. |
| **Why it fails ACCEPT** | PTG-LAND struck B (phase leak). PTG-INVOKE struck C (invoke inside mod-check). ACCEPT criteria: mod-check SKILL.md untouched; order is render → tunnel → lint. `check.md` is pre-build GO/REVISE/BLOCK — wrong phase for mid-render outbound copy. |
| **W2 mitigation** | Ship only `skills/wavves/playbooks/paragraph-tunnel.md` + dispatch STEPS hook. Explicitly name: **not** mod-check; invoke after render, before prose_lint; field from waveset (`tunnel_field`). Do not edit mod-check. Leave INT gated for router only. |

### 2. Overloading `run_fixtures.py` / lens-wording tripwire with tunnel cases

| field | content |
|---|---|
| **Severity** | BLOCK |
| **What it looks like** | New dirs under `evals/fixtures/` that `run_fixtures.py` walks, expecting `lens_that_should_catch` / keyword match against mod-check SKILL; or patches to `run_fixtures.py` to "also handle" `paragraph-tunnel-*`. Claiming `python3 evals/run_fixtures.py` PASS = tunnel ACCEPT. |
| **Why it fails ACCEPT** | waveset: **Do not overload `run_fixtures.py` for tunnel cases.** Runner is a **lens-wording tripwire**, not judgment replay (README known limitation). Tunnel PASS/FAIL is fail_id matching on paragraph text — orthogonal to mod-check lens table. Mixing corpora makes false PASS/FAIL and corrupts SELF regression convention. |
| **W2 mitigation** | Separate runner: `evals/check_paragraph_tunnel.py`. Fixtures only under `evals/fixtures/paragraph-tunnel-*/`. Document in `evals/README.md` as **disjoint** from lens-wording runner. ACCEPT capture from tunnel checker only. |

### 3. LLM-only acceptance without mechanical fixtures

| field | content |
|---|---|
| **Severity** | BLOCK |
| **What it looks like** | ACCEPT = "Grok said the playbook looks good"; lane-local JSON narrative without runnable expected fail_ids; FR acceptance sketch treated as done (house FM class: unrunnable). |
| **Why it fails ACCEPT** | PTG-EVAL pick A: `paragraph-tunnel-*` + runner with expected fail_ids / PASS. ACCEPT item 1: `python3 evals/check_paragraph_tunnel.py` → PASS all fixtures; capture under `gate-captures/PTB-ACCEPT-tunnel.json`. Mechanical = zero network/LLM. |
| **W2 mitigation** | Stdlib checker + fixtures with `input.md` + `expected.md` (verdict + fail_ids). Captures cite measured runner stdout/JSON. Spot-check playbook separately; never substitute LLM self-grade for mechanical PASS. |

### 4. Auto-pass after fail-cap (forbidden)

| field | content |
|---|---|
| **Severity** | BLOCK |
| **What it looks like** | Playbook says after loop 1 still FAIL: keep original, mark PASS, raise cap to 2, or soft-warn and continue to preview/send. Omits `post_cap: escalate`. |
| **Why it fails ACCEPT** | PTG-FAIL-CAP pick A: escalate operator REVISE; no auto-pass; no second rewrite. Preview/send blocked until revise. Spot-check ACCEPT includes fail-cap escalate. |
| **W2 mitigation** | Playbook hard rule: after one rewrite + re-adversarial still FAIL → `post_cap: escalate`, block CLEARED preview. Capture schema requires escalate field. No "best effort keep." |

### 5. Creating `/paragraph-tunnel` slash skill directory (deferred)

| field | content |
|---|---|
| **Severity** | HIGH |
| **What it looks like** | `skills/paragraph-tunnel/` or `/paragraph-tunnel` skill scaffold in W2 "for completeness" / A+C. |
| **Why it fails ACCEPT** | PTG-LAND: defer A until C proves out. ACCEPT item 3: confirm **no** `/paragraph-tunnel` skill directory created. |
| **W2 mitigation** | Playbook + evals only. Non-goal note in playbook: slash skill deferred. W2a may leave WIRING note for INT (router row), not a new skill package. |

### 6. Embedding `landing_commit_hash` inside artifact that lands in same commit (PTG-HASH / self-ref loop)

| field | content |
|---|---|
| **Severity** | HIGH |
| **What it looks like** | FR or ACCEPT capture sets `repo_state_verified_against` = hash of commit that will contain the artifact; single field labeled as both evidence and landing; playbook examples teach embedding own landing hash. |
| **Why it fails ACCEPT** | PTG-HASH: split `evidence_verified_against` (pre-landing) vs `landing_commit_hash`; never equate. House self-ref hash rule. FR currently conflates evidence label with a landing-style hash — W2d must patch, not repeat. |
| **W2 mitigation** | W2d: FR fields split. Artifacts record `repo_state_verified_against` / `evidence_verified_against` of state **evaluated**. Landing hash only in O0 completion report, never self-embedded in same commit payload. |

### 7. Collapsing judge + freeze into one capture

| field | content |
|---|---|
| **Severity** | HIGH |
| **What it looks like** | Single JSON with rewrite + inline "PASS" and freeze note; rewrite agent claims PASS without separate re-adversarial; no sibling checksum / opener-close hash verify. |
| **Why it fails ACCEPT** | PTG-JUDGE pick A: separate re-adversarial capture + sibling freeze checksum. Same model allowed; **same capture / inline PASS** struck. outbound copy lane live pattern: adversarial JSON then rewrite JSON with `re_adversarial` + frozen opener/close — product must keep separation. |
| **W2 mitigation** | Playbook: Gate 1 capture, Gate 2 rewrite capture, mandatory re-adversarial step, freeze checksum on siblings. Document two capture filenames. Checker may assert schema presence of freeze + re-adversarial fields where fixtures cover rewrite path. |

### 8. Using Claude/Composer for tunnel gates (Grok lock)

| field | content |
|---|---|
| **Severity** | HIGH |
| **What it looks like** | Playbook "recommended_model" lists Claude/Composer; dispatch "or equivalent high-reasoning"; W2 runners launched without `model: cursor-grok-4.5-high-fast`. |
| **Why it fails ACCEPT** | PTG-MODEL pick A: Grok only for adversarial + rewrite. waveset `model_enforcement`: no Claude/Composer fallback. Spot-check ACCEPT includes Grok model lock. |
| **W2 mitigation** | Hard-code `cursor-grok-4.5-high-fast` in playbook + any STEPS snippet. State forbidden fallbacks explicitly. |

### 9. Touching mod-check SKILL.md or router before INT gate

| field | content |
|---|---|
| **Severity** | HIGH (BLOCK if done in W2) |
| **What it looks like** | W2 edits `skills/mod-check/SKILL.md`, or W2 (not INT) edits `skills/wavves/SKILL.md` route table / playbook list. Parallel editors on shared files. |
| **Why it fails ACCEPT** | waveset: INT is **SINGLE editor**, **GATED** — wire router only after O0 approval. ACCEPT: mod-check untouched. W2: NEW files preferred. |
| **W2 mitigation** | W2a–c: new playbook, new checker, new fixture dirs. W2d: FR + evals README only. WIRING note in findings for INT; do not apply router patch in W2. Never open mod-check. |

### 10. Fixtures that only cover outbound copy lane three-shop happy path without FIXTURE/STANDIN

| field | content |
|---|---|
| **Severity** | HIGH |
| **What it looks like** | Corpus = Apollo PASS + Ardesia stack/gloss FAIL + Scotts compare FAIL only. No `PN-FIXTURE` / STANDIN fail cases. Or fixtures that FAIL solely for "nice because". |
| **Why it fails ACCEPT** | PTG-EVAL / PTG-VOCAB: at least one PN-FIXTURE and STANDIN case. PTG-NICE-BECAUSE: nice-because allowed. |
| **W2 mitigation** | one-fact PASS; nice-because PASS; stack/gloss FAIL (no BECAUSE id); compare FAIL; **FIXTURE FAIL**; **STANDIN FAIL**. |

---

## Additional anti-patterns (secondary; still ACCEPT-relevant)

| # | anti-pattern | severity | ACCEPT failure mode | W2 mitigation |
|---|--------------|----------|---------------------|---------------|
| A | Checker that greps prose_lint banned phrases only | MED | Misses wandering-paragraph class (FR problem statement) | Fail_id rules on structure: MULTI, STACK, GLOSS, COMPARE, FIXTURE, STANDIN (never BECAUSE/EXPLAIN) |
| A2 | Reintroducing PN-BECAUSE / PN-EXPLAIN or failing "nice because" | BLOCK | PTG-NICE-BECAUSE / outbound copy lane-NICE-BECAUSE-ALLOWED: struck; operator overturn | Whitelist nice-because in playbook + checker; no BECAUSE/EXPLAIN fixtures-as-fail |
| B | Freeze that rewrites opener/close "for coherence" | HIGH | PTG-JUDGE sibling freeze; outbound copy lane opener/close frozen | Checksum/hash siblings; rewrite tunnel field only |
| C | Treating mechanical PASS as proof live Grok judgment matches | MED | Known-limitation class: mechanical ≠ full judgment | Document gap in README; ACCEPT = mechanical + playbook spot-check, not fake replay |
| D | Default `tunnel_field` omitted / optional on CLEARED-preview outbound | MED | PTG-INVOKE: hard-fail if skipped on CLEARED-preview outbound | Playbook: require named field; hard-fail skip |
| E | Reopening locked PTG picks in playbook "options" | MED | LOCKED-DECISIONS: do not reopen | State locks as binding; no A/B/C menu in product surface |

---

## Phase-leak cross-check (`check.md`)

`skills/wavves/playbooks/check.md` routes **mod-check**: lane home, adversarial parallel wave, GO|REVISE|BLOCK, pre-build / pre-plan. Paragraph tunnel is **mid-render outbound** (after render, before prose_lint). Wiring tunnel into check playbook or mod-check skill is exactly Option B phase leak. W2 must keep surfaces disjoint.

---

## W2 do / don't (one screen)

**Do**

- New playbook `paragraph-tunnel.md` (invoke order, vocab, fail-cap, judge/freeze, Grok)
- New `evals/check_paragraph_tunnel.py` (stdlib, no LLM)
- Fixtures `paragraph-tunnel-*` including FIXTURE + STANDIN fails
- FR hash split (W2d); README section disjoint from `run_fixtures.py`
- WIRING note only for later INT router row

**Don't**

- Touch mod-check SKILL.md or router in W2
- Create `/paragraph-tunnel` skill dir
- Extend or feed `run_fixtures.py`
- Auto-pass / silent keep after fail-cap
- Single capture for rewrite+judge+freeze
- Claude/Composer for tunnel gates
- Self-embed landing commit hash in landing artifact
- Happy-path-only outbound copy lane three-shop fixtures

---

## Verdict for O0

W2 is safe if it treats PTG locks as hard constraints and keeps the tunnel **product surface** (playbook + mechanical eval) **out of** the mod-check / lens-wording eval plane. Highest-probability ACCEPT failures: phase leak into check, overloaded `run_fixtures.py`, and missing FIXTURE/STANDIN mechanical cases while claiming LLM review sufficient.
