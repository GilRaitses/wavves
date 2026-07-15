# PTB-W1b — eval harness design (corrected vocab)

- **Wave:** PTB-W1b
- **Date:** 2026-07-15 (America/New_York)
- **Lane:** `wavves/lanes/20260715_paragraph-tunnel-build/`
- **Target:** `evals/check_paragraph_tunnel.py` + `evals/fixtures/paragraph-tunnel-*/`
- **Lock:** PTG-EVAL; mechanical stdlib only; do **not** overload `run_fixtures.py`
- **Vocab authority:** `findings/PTB-vocab-port.md` (no BECAUSE/EXPLAIN)

---

## 1. Fixture layout

```text
evals/fixtures/paragraph-tunnel-<slug>/
  input.md      # tunneled paragraph text (body only, or labeled field)
  expected.md   # schema below
```

Naming prefix `paragraph-tunnel-` is mandatory so the tunnel checker can
discover cases without walking the lens-wording corpus.

## 2. expected.md schema

```text
expected_verdict: PASS | FAIL
fail_ids: []                    # JSON-like list; empty on PASS
# optional:
require_one_sentence: true      # default true
ground_truth: ...               # only for FALSEFACT fixtures
forbidden_claims: ...           # optional FALSEFACT helper
```

`fail_ids` is an unordered set. Checker PASS means detected set equals
expected set (and verdict matches).

## 3. Mechanical detection (tripwire, not LLM judgment)

| id | heuristic |
|---|---|
| PN-MULTI | sentence count > 1 (split on `.!?` followed by space/end) |
| PN-GLOSS | `personality of` / `part of how` (case-insensitive) |
| PN-COMPARE | `than the` / `compared to` / `unlike` / `quieter than` / `destination food` |
| PN-STACK | ≥2 distinct claim signals (place/scene token + gloss and/or type restatement and/or `come together` with additional claim) |
| PN-FIXTURE | ≥2 of {glass, planter, awning, curb} and no place-type noun (shop/bar/florist/bagel/cafe/restaurant) |
| STANDIN | `stand-in` / `stand in` / `fair stand-in` / `kind of place` / `fair example` / category `looked like a` |
| RESEARCH-META | `early research` / `research phase` / `part I care about` / `for my research` |
| FALSEFACT | only if `ground_truth` or `forbidden_claims` present and contradicted |

**Whitelist:** presence of `nice because` / `because it is` must **never**
alone produce a fail id. Checker must not define BECAUSE/EXPLAIN detectors.

Known limitation (document in README): mechanical tripwire ≠ live Grok
adversarial judgment.

## 4. Minimum fixture set (W2c)

| slug | expected_verdict | fail_ids |
|---|---|---|
| `paragraph-tunnel-one-fact-pass` | PASS | `[]` |
| `paragraph-tunnel-nice-because-pass` | PASS | `[]` (proves whitelist) |
| `paragraph-tunnel-stack-gloss-fail` | FAIL | PN-STACK, PN-GLOSS, PN-MULTI |
| `paragraph-tunnel-compare-fail` | FAIL | PN-COMPARE, PN-MULTI |
| `paragraph-tunnel-fixture-fail` | FAIL | PN-FIXTURE |
| `paragraph-tunnel-standin-fail` | FAIL | STANDIN |

## 5. CLI contract

```bash
python3 evals/check_paragraph_tunnel.py
```

- Exit 0: every fixture matches expected
- Exit non-zero: any mismatch or load error
- Stdout: per-fixture PASS/FAIL + detected vs expected fail_ids
- Stdlib only; no network; no LLM

## 6. Explicit non-goals

- Do **not** modify `evals/run_fixtures.py`
- Do **not** require `lens_that_should_catch` fields
- Do **not** feed tunnel fixtures into the lens-wording tripwire
