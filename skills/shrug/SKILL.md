---
name: shrug
description: >-
  Thin discoverable alias for emoji shrug (¯\_(ツ)_/¯). Bare /shrug → AUTH-10
  proceed (recommended_actions only). /shrug + a closed all-standing phrase →
  proceed-all-standing. Never widen bare /shrug. Execution lives in
  skills/wavves/playbooks/proceed.md.
disable-model-invocation: true
---

# shrug

Discoverable leaf for the standing shrug alias. **Does not** own proceed
logic. Read and follow `skills/wavves/playbooks/proceed.md`.

## Route (closed)

| utterance | route |
|---|---|
| `/shrug` alone | AUTH-10 proceed (`recommended_actions` only) |
| `¯\_(ツ)_/¯` alone | same |
| `/shrug` or shrug + one closed all-standing phrase below | **proceed-all-standing** |

Closed all-standing phrases (same utterance; no fuzzy widen):

- `all still standing`
- `queue all standing and move`
- `proceed all standing`
- `/wavves proceed all standing`

## Non-negotiables

1. **Bare never widens.** Bare `/shrug` or bare `¯\_(ツ)_/¯` is AUTH-10 only.
   Fail id if widened: `PROC-PROCEED-SHRUG-WIDEN`.
2. **No playbook body here.** Inventory, standing persist, move rules, and
   return card live only in `playbooks/proceed.md`.
3. **No wider surface than proceed routing.** Do not invent alternate queues,
   scopes, or unlock paths from this leaf.
