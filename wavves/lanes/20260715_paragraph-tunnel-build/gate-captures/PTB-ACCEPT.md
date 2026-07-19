# PTB-ACCEPT — gate capture

lane: PTB (paragraph-tunnel-build)
gate: PTB-ACCEPT
date: 2026-07-18 (America/New_York)
evaluator: O0 (independent of PTB-W1/W2 authorship; no authorship of
`skills/wavves/playbooks/paragraph-tunnel.md` or
`evals/check_paragraph_tunnel.py` under review)
repo_state_verified_against: `af0c0788cb2dbb865cbce6721fcdcbf6642b11d4`
INT unlock: operator "lets complete them" (2026-07-18)

## Pass metric (stated before the run)

1. `python3 evals/check_paragraph_tunnel.py` → PASS all fixtures; JSON under
   `gate-captures/PTB-ACCEPT-tunnel.json`
2. Playbook documents: order render → tunnel → lint; fail-cap escalate;
   Grok model lock; judge/freeze rules
3. No `/paragraph-tunnel` skill directory
4. `skills/mod-check/SKILL.md` untouched

## (1) Mechanical checker — measured

```
PASS  paragraph-tunnel-compare-fail: verdict=FAIL fail_ids=['PN-COMPARE', 'PN-MULTI']
PASS  paragraph-tunnel-fixture-fail: verdict=FAIL fail_ids=['PN-FIXTURE']
PASS  paragraph-tunnel-nice-because-pass: verdict=PASS fail_ids=[]
PASS  paragraph-tunnel-one-fact-pass: verdict=PASS fail_ids=[]
PASS  paragraph-tunnel-stack-gloss-fail: verdict=FAIL fail_ids=['PN-GLOSS', 'PN-MULTI', 'PN-STACK']
PASS  paragraph-tunnel-standin-fail: verdict=FAIL fail_ids=['STANDIN']

summary: pass=6 fail=0 total=6
EXIT:0
```

Capture: `gate-captures/PTB-ACCEPT-tunnel.json`

## (2) Playbook spot-check — measured against file

| lock | evidence in `skills/wavves/playbooks/paragraph-tunnel.md` | result |
|---|---|---|
| order render → tunnel → lint | line: "render → tunnel (adversarial → optional rewrite) → prose_lint" | PASS |
| fail-cap escalate | step 8: `post_cap: escalate`, operator REVISE, no auto-pass | PASS |
| Grok model lock | "MUST use `model: cursor-grok-4.5-high-fast`" | PASS |
| judge / freeze | steps 3, 7: freeze checksums + separate re-adversarial | PASS |

## (3) No slash skill directory

`skills/paragraph-tunnel` does not exist (`test ! -d` → NO_SLASH_OK).

## (4) mod-check untouched

`git hash-object skills/mod-check/SKILL.md` =
`616fb7027ee1d60298662ce8b35a268a3168d7bf` (no local diff vs HEAD).

## INT wiring (gated, operator unlocked)

`skills/wavves/SKILL.md` now lists playbook `paragraph-tunnel` →
`playbooks/paragraph-tunnel.md` (router table + playbook list). Leaf =
dispatch STEPS; no slash skill in v0.

## Scope (what ACCEPT measured)

Mid-render structural tunnel only: closed fail vocab, sibling freeze,
rewrite cap → operator REVISE, mechanical fixtures. Not a voice-clone or
mailbox-scale humanizer. Operator HITL overturns (e.g. nice-because
whitelist) stay in the lock files. Slash skill deferred (LAND=C).

## Verdict

**PASS.** PTB ACCEPT criteria met.
