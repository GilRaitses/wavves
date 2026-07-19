# Purpose gates

Purpose gates are pass-or-fail checks for wavves public copy (landing page,
README lead, outbound articles). They judge whether prose states the product
point, not whether mechanics lint clean.

**Mechanical style (universal):** `python3 evals/check_public_copy.py` (see
`docs/public-copy-gates.md`).

**Story fidelity (wavves-specific):** this file (PG1 through PG11).

Surfaces in scope:

- `index.html` hero and above-the-fold copy
- `README.md` opening paragraphs
- Published publisher articles and whitepaper excerpts that describe wavves

## Hard fail

| ID | Rule | Why |
|---|---|---|
| PG1 | Lead with capture and durable alignment, not release-note mechanics | AUTH sync, `dispatch-w{N}.md`, scoped verdicts and `/wavves proceed` support the story; they do not headline it |
| PG2 | Synthesize causally; no stacked one-fact-per-sentence propositions | Each sentence must earn the next through cause, consequence or answer |
| PG3 | Do not open with adopted ontology | Do not presuppose fleet taxonomy, moderator-layer vocabulary or architecture the reader has not yet felt as a problem |
| PG4 | Do not open with inventory list buildup | Do not enumerate scope fields before the reader knows why the list matters |
| PG5 | Every sentence at least 15 words | Short leads read as fragments on marketing surfaces |
| PG6 | No Oxford commas | See `docs/public-copy-gates.md` (OXFORD); `evals/check_public_copy.py` |
| PG7 | No banned tense hedge of the NO_LONGER class | State where things are or what fails, affirmatively |
| PG8 | No contrast hedges of the AFFIRM class | Same affirmative rule as prose gate G1 on these surfaces |

Banned substrings for PG7/PG8 (fenced):

```
no longer
rather than
instead of
```

## Review (human)

| ID | Rule | Why |
|---|---|---|
| PG9 | Alignment packet before runners deploy | Capture precedes dispatch |
| PG10 | Successor hydrates from `wavves/` files | Files carry the record; chat does not |
| PG11 | Runnable check evidence on disk | Acceptance is measured, not asserted in chat |

## Usage

Read the surface aloud. Hard-fail any row that triggers. For landing hero
edits, check PG1 through PG8 before push.

Automated substring check for PG7, PG8 and PG6 (OXFORD) on hero copy:

```bash
python3 evals/check_public_copy.py index.html
```

Zero hard-fail on AFFIRM, NO_LONGER and OXFORD for hero. See `docs/public-copy-gates.md`
for the full universal set.

## Remedies

Serial comma fixes: see `docs/public-copy-gates.md` (also applied by
`python3 evals/check_public_copy.py --fix`).
