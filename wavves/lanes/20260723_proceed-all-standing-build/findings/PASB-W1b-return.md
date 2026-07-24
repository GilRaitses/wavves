# PASB-W1b return — thin `/shrug` leaf

```yaml
charge: PASB-W1b
role: charge_worker
owns: skills/shrug/SKILL.md
git: none
tip_expected: de75b4c4118c78dcc0164fdaa916bbc53f99225f
status: complete
```

## Path created

| path | action |
|---|---|
| `skills/shrug/SKILL.md` | created (dir + thin leaf) |

Frontmatter: `name: shrug`, `disable-model-invocation: true` (style matched to
`skills/set-key/SKILL.md`). Body routes only; execution points to
`skills/wavves/playbooks/proceed.md`. No playbook duplication.

## Trigger table (leaf)

| phrase | route |
|---|---|
| `/shrug` alone | AUTH-10 proceed (`recommended_actions`) |
| `¯\_(ツ)_/¯` alone | AUTH-10 proceed (`recommended_actions`) |
| `/shrug` or shrug + `all still standing` | proceed-all-standing |
| `/shrug` or shrug + `queue all standing and move` | proceed-all-standing |
| `/shrug` or shrug + `proceed all standing` | proceed-all-standing |
| `/shrug` or shrug + `/wavves proceed all standing` | proceed-all-standing |

Locks honored: bare `/shrug` never widens (`PROC-PROCEED-SHRUG-WIDEN`); no
wider body than proceed routing; COMMIT-AUTH-GRAIN / SCOPE-FALLBACK not
owned by this leaf (playbook).

## Residual risks

| id | risk | owner |
|---|---|---|
| R1 | Leaf ships before W1a lands mode fork in `proceed.md`; bare route works today, all-standing needs W1a body | PASB-W1a / INT |
| R2 | Router leaf table / README may not yet list `/shrug` until W1d | PASB-W1d / INT |
| R3 | Evals for bare-shrug non-widen not owned here | PASB-W1c |

## Untouched (per charge)

`skills/wavves/playbooks/proceed.md`, `skills/wavves/SKILL.md`, `evals/`,
`README.md`, `examples/`.
