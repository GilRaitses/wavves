# KVC-W1d return

```yaml
wave_id: KVC-W1d
lens: adversarial
path: findings/KVC-adversarial.md
verdict_lean: REVISE
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
git: none
```

## FM ids

- FM-KVC-01 resume without checkpoint (chat as K/V)
- FM-KVC-02 proceed chat-inventory labeled as cache
- FM-KVC-03 empty rotations + hydrate claim (live disk)
- FM-KVC-04 isomorphism / RotatE vocabulary leak
- FM-KVC-05 fail-id alias / bind loopholes
- FM-KVC-06 open calls unlocked → BUILD unsafe
- FM-KVC-07 evals absent / soft gates
- FM-KVC-08 tip stale at resume
- FM-KVC-09 scope-poison BUILD footgun

## One line

REVISE: lock alias binds + CACHE-NAME / WOF-BIND / ROTATION-TEMPLATE before
any CTX-KV BUILD; empty `rotations/` + chat-as-cache are the live footguns.
