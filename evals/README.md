# evals/ — wavves fixture corpus

Repo-root, shippable feature of the wavves plugin itself, sibling to
`skills/`, `examples/`, `assets/`. Not lane-scoped working state. Written by
lane `SELF` (`wavves-self-improvement`), wave `SELF-W2a`; see
`wavves/lanes/20260709_wavves-self-improvement/waveset.md` for the full
charter.

## What this is

A held-out set of fixtures, each seeding one named defect that a `mod-check`
review (or `charter` grounding step) should catch. The corpus exists so a
future edit to `mod-check`'s lens set or `charter`'s grounding step can be
checked against a fixed baseline before it is trusted, instead of being
trusted on the strength of looking correct once. See
`wavves/lanes/20260709_wavves-self-improvement/findings/SELF-inventory.md`
for the gap this closes and
`wavves/lanes/20260709_wavves-self-improvement/findings/SELF-adversarial-case.md`
for the two concrete regression scenarios this corpus is built to catch.

## Layout

```text
evals/
  README.md                 (this file)
  run_fixtures.py            runner: PASS/FAIL per fixture
  fixtures/
    <case-name>/
      input.md                seeded-defect spec/plan snippet
      expected.md              named defect category, keywords, lens,
                                 expected verdict, gap a reviewer must name
```

## Fixture cases (3, at bootstrap)

1. `unrunnable-gate-narrowed-adversarial-lens` — seeds an acceptance gate
   described in prose but not runnable by an outside party (no command, no
   harness, no pass metric). Corresponds to
   `SELF-adversarial-case.md` Scenario 1. Lens: `adversarial`.
2. `plausible-path-softened-grounding` — seeds one nonexistent-but-plausible
   file citation (`skills/mod-review/SKILL.md`, following the real
   `mod-<verb>` naming convention but not actually present in this repo)
   inside an otherwise-real grounding section. Corresponds to
   `SELF-adversarial-case.md` Scenario 2. Lens: `grounding`.
3. `no-repeat-verification-on-promotion` — seeds a project-skill proposal
   that is promoted through today's real pipeline (moderator review,
   evidence check, operator ask) with no fixture-corpus run and no
   repeat-trial requirement, and whose proposed edit is itself the
   regression from fixture 1. Corresponds to `SELF-inventory.md` section 1.
   Lens: `completeness`.

Fixtures 1 and 2 are the two scenarios required by `SELF-W1b`. Fixture 3 is
the third case required by `SELF-W2a`, built from the `SELF-W1a` inventory
finding rather than repeating a `SELF-W1b` scenario.

## Running the corpus

```bash
python3 evals/run_fixtures.py
```

No dependencies beyond the Python 3 standard library. No network access, no
LLM call, no other repo state mutated.

## Public copy gates

`evals/check_public_copy.py` checks universal outbound prose rules (AFFIRM,
DASH, FILLER, OXFORD, NO_LONGER; LEAD length as review). It does not include
project-specific rules from the separate `prose-gates` repo (internal naming,
internal tokens, colon ban on full UI pages). See `docs/public-copy-gates.md`.

```bash
python3 evals/check_public_copy.py
python3 evals/check_public_copy.py --fix index.html
```

wavves-specific purpose gates (`docs/purpose-gates.md`) stay manual review.

## Known limitation, stated plainly (do not overstate this script)

`run_fixtures.py` is a **structured checklist verifier**, not a real
reviewer replay. It cannot invoke an LLM call from inside the script in a
way that reproduces true agent judgment against a fixture's `input.md`.
Concretely, the script:

- reads the CURRENT, live `skills/mod-check/SKILL.md` "Default parallel
  lenses" table,
- reads each fixture's `expected.md` for a declared `seeded_defect_category`,
  a `defect_keywords` list and a `lens_that_should_catch` name,
- checks whether the named lens's "hunts for" cell contains at least one of
  the declared keywords (case-insensitive substring match),
- reports PASS when the current lens wording plausibly still claims
  coverage of that defect category, FAIL when none of the keywords survive
  in the current wording.

A PASS means "the lens table's wording still nominally names this failure
mode." It does NOT mean "an agent given this fixture's `input.md` would
actually produce the `expected_verdict` and name the gap correctly." The
runner has no way to verify that without a real model call reproducing
agent judgment, and it does not attempt to fake one.

This is a known gap. A future wave should close it with a real replay
harness: dispatch an actual `mod-check`-style reviewer subagent against
each fixture's `input.md`, capture its verdict and named gaps, and compare
those against `expected.md` for a true pass/fail, rather than checking
keyword survival in the lens table's wording. Until that harness exists,
this script is a tripwire on lens-wording narrowing, not a test of review
quality.

## Paragraph tunnel fixtures (disjoint harness)

Separate from the lens-wording tripwire above. Product surface for the
paragraph-tunnel playbook (`skills/wavves/playbooks/paragraph-tunnel.md`).

```bash
python3 evals/check_paragraph_tunnel.py
```

- Discovers only `evals/fixtures/paragraph-tunnel-*/`
- Stdlib mechanical fail-id tripwire (no LLM, no network)
- Does **not** use or modify `run_fixtures.py`
- Whitelist: `"nice because"` / `"because it is"` never alone fail
- Closed vocab: `PN-STACK`, `PN-COMPARE`, `PN-GLOSS`, `PN-FIXTURE`, `PN-MULTI`,
  plus `STANDIN` / `RESEARCH-META` / `FALSEFACT` (no BECAUSE/EXPLAIN)

Known limitation: mechanical PASS ≠ live Grok adversarial judgment. ACCEPT
still requires playbook spot-check plus measured checker output.

## Proof-before-accept fixtures (disjoint harness)

Separate from the lens-wording tripwire and from paragraph-tunnel. Product
surface for the proof-before-accept playbook
(`skills/wavves/playbooks/proof-before-accept.md`).

```bash
python3 evals/check_proof_before_accept.py
```

- Discovers only `evals/fixtures/proof-before-accept-*/`
- Stdlib mechanical fail-id tripwire (no LLM, no network)
- Does **not** use or modify `run_fixtures.py` or `paragraph-tunnel-*`
- Mechanical vocab: `PROC-PASS-NO-PROOF`, `PROC-NO-VISUAL`
- Review/live ids (`PROC-CHROME-THRASH`, `PROC-DEBT-AS-DONE`,
  `PROC-BLANK-CANVAS`) are not emitted by this script
- Minimum cases: process-only ACCEPT → FAIL; full proof fields + harness →
  PASS; opt-out without rationale → FAIL; `visual_accept: yes` without
  harness → FAIL

Known limitation: mechanical PASS ≠ live DOM/host Proof ACCEPT. Product
lanes still need the named host-geometry harness and JSON capture under
`gate-captures/` per EXECUTION_WIRING Rule 2b (applied at INT).

## Repeated-trial verification (3 consecutive passes)

Per the SELF lane's locked decisions, a proposed skill edit affecting
`mod-check`'s lens set or `charter`'s grounding step is trusted only after
`run_fixtures.py` passes 3 consecutive times against the corpus, once the
patch drafts in `SELF-W2b` are reviewed and applied (`SELF-INT`, gated, not
run by this wave). This file documents the convention; `SELF-INT` performs
the actual repeat run against pre-patch and post-patch skill files.
