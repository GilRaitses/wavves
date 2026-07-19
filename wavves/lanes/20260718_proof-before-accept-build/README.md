# PBB — proof-before-accept-build

Build the proof-before-accept product surface locked by PBA mod-decide.
No `/proof-gate` slash skill.

| field | value |
|---|---|
| code | PBB |
| label | proof-before-accept-build |
| owner | O0 |
| type | execution |
| status | w1-w2-complete; pause before INT |
| depends_on | PBA |
| home | `wavves/lanes/20260718_proof-before-accept-build/` |
| repo_state_verified_against | `517dd85190cf93cf744434338dec4b1eb1d859c5` |
| active_dispatch | `dispatch-w1.md` |
| proof_required | n/a (plugin-meta method lane) |

## Start

Hydrate `dispatch-w1.md`. Run W1+W2. Pause before gated INT/ACCEPT.
All subagents: **Grok only** (`cursor-grok-4.5-high-fast`).
