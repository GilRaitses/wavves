# Public copy gates

Mechanical checks for README, landing page and other outbound plugin prose.
These gates are **universal** (any project can use them). They ship with the
plugin at `evals/check_public_copy.py`.

wavves-specific **purpose** gates (capture story, moderator framing) live in
`docs/purpose-gates.md` and stay manual review.

## Automated hard fail

| ID | Rule |
|---|---|
| AFFIRM | No `rather than` or `instead of` |
| DASH | No em dash, en dash or spaced double hyphen in prose |
| FILLER | No smug/filler devices (`actually`, `perhaps`, `it's not just`, …) |
| OXFORD | No serial comma; no `, and` between clauses. Comma before `while` is allowed |
| NO_LONGER | No `no longer` |

## Automated review (warn)

| ID | Rule |
|---|---|
| LEAD | First sentence under a heading (or hero copy) should be at least 15 words |

## Not included (project-specific)

These live in the separate `prose-gates` repo for aimez surfaces and are
**not** run by the plugin checker:

- Lowercase `pax` / `magniphyq` naming (NAME)
- Internal token leakage (`O0`, `Central Casting`, …)
- Colon ban on full HTML UI pages (too many structural false positives)
- Application/resume artifact presets

## Remedies (OXFORD)

| Violation | Fix |
|---|---|
| `, X, and Y` | `, X and Y` |
| `, and` between clauses | `, while` when subordinate, or split into two sentences |

## Usage

From the plugin root:

```bash
python3 evals/check_public_copy.py
python3 evals/check_public_copy.py path/to/file.md
python3 evals/check_public_copy.py --fix index.html
```

Default scan (no paths): `index.html`, `README.md`, `docs/`, `examples/`.

Purpose gates (PG1–PG11) are still read aloud before shipping hero or article
copy. The script does not judge synthesis or ontology.
