# Public copy gates

Mechanical checks for README, landing page and other outbound plugin prose.
These gates are **universal** (any project can use them). They ship with the
plugin at `evals/check_public_copy.py`.

wavves-specific **purpose** gates (capture story, moderator framing) live in
`docs/purpose-gates.md` and stay manual review.

## Automated hard fail

| ID | Rule |
|---|---|
| AFFIRM | No contrast hedges in the AFFIRM class (see fenced list below) |
| DASH | No em dash, en dash or spaced double hyphen in prose |
| FILLER | No smug/filler devices (see fenced list below) |
| OXFORD | No serial comma; no clause joiners of the OXFORD class (see fence) |
| NO_LONGER | No banned tense hedge of the NO_LONGER class (see fence) |

Banned substrings (fenced so this doc does not trip the checker):

```
rather than
instead of
actually
perhaps
it's not just
no longer
, and
```

## Automated review (warn)

| ID | Rule |
|---|---|
| LEAD | First sentence under a heading (or hero copy) should be at least 15 words |

## Not included (project-specific)

These live in the separate `prose-gates` repo for publisher surfaces and are
**not** run by the plugin checker:

- Lowercase internal product-repo naming (NAME)
- Internal token leakage (moderator identity tokens, private exhibit names)
- Colon ban on full HTML UI pages (too many structural false positives)
- Application/resume artifact presets

## Remedies (OXFORD)

Split the list or drop the serial comma. Prefer two sentences when a clause
joiner would otherwise trip OXFORD.

## Usage

From the plugin root:

```bash
python3 evals/check_public_copy.py
python3 evals/check_public_copy.py path/to/file.md
python3 evals/check_public_copy.py --fix index.html
```

Default scan (no paths): `index.html`, `README.md`, `docs/`, `examples/`.

Purpose gates (PG1 through PG11) are still read aloud before shipping hero or
article copy. The script does not judge synthesis or ontology.
