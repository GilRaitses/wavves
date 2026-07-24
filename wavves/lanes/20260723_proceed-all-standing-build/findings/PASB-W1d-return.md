# PASB-W1d return — router + docs for /shrug and all-standing

```text
charge: PASB-W1d
role: charge worker (not orch, not moderator)
model: cursor-grok-4.5-high-fast
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
status: done
```

## Paths touched

| path | change |
|:-----|:-------|
| `skills/wavves/SKILL.md` | description YAML; proceed routing row; leaf table `/shrug` |
| `README.md` | playbook table; Skills table; examples block; proceed prose; Components table |
| `examples/usage.md` | Skills table; playbooks proceed row; Quick reference; proceed prose |

Untouched (owned by other charges): `skills/wavves/playbooks/proceed.md`,
`skills/shrug/`, `evals/`.

## Rows / lines added

### `skills/wavves/SKILL.md`

- Description: `/shrug` in leaf list; `proceed-all-standing` in use-for list.
- Routing table proceed row: closed all-standing phrases listed; bare shrug /
  bare `/shrug` → AUTH-10 only.
- Playbook list: still **Proceed.** `playbooks/proceed.md` (no new playbook file).
- Leaf skills table: new `shrug` / `/shrug` row (bare → AUTH-10; + closed
  phrase → proceed-all-standing).

### `README.md`

- Usage playbook table: proceed row mentions all-standing on closed phrases;
  new `shrug` row.
- Skills table: `/shrug` row.
- examples block: `all-standing:` and `shrug:` trigger lines.
- Proceed prose after skill list: closed phrases → proceed-all-standing;
  bare shrug / bare `/shrug` non-widen.
- Components table: `shrug` (`/shrug`) row.

### `examples/usage.md`

- Skills table: `/shrug` row.
- Playbooks proceed row: all-standing closed phrases; bare `/shrug` AUTH-10.
- Quick reference: `all-standing:` and `shrug:` lines.
- After recommended_actions note: same non-widen + closed-phrase rule.

## Authority honored

- Bare shrug / bare `/shrug` never widen (LOCKED + `PROC-PROCEED-SHRUG-WIDEN`).
- Closed triggers only: `all still standing`, `queue all standing and move`,
  `proceed all standing`, `/wavves proceed all standing` (and shrug + one of those).
- No behavior invented beyond FR PS-06/PS-07/PS-08 + LOCKED-DECISIONS.
- No em dashes in new prose.

## Residual risks

1. **Leaf skill body not owned here.** Docs route to `/shrug`; actual
   `skills/shrug/SKILL.md` is another charge. Until that ships, slash may 404
   in install while router text already names it.
2. **Playbook body not owned here.** Router points at `proceed.md` for both
   AUTH-10 and all-standing; mode fork must land in that playbook (other charge).
3. **Table drift vs index/homepage.** `index.html` / marketplace copy not in
   this charge OWNS list; INT may need to reconcile if Acceptance docs bullet
   expects homepage listing too.
4. **Non-negotiables leaf list** in SKILL.md still names full leaves only
   (no shrug). Intentional: shrug is thin alias into proceed, not a separate
   playbook. Escalate if orch wants it named there too.
```
