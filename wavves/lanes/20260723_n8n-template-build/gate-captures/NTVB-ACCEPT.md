# NTVB-ACCEPT — gate capture

```yaml
lane: NTVB
gate: NTVB-ACCEPT
role: acceptance_evaluator
answers_to: O0
date: 2026-07-23 (America/New_York)
captured_at: 2026-07-23T14:02:13-04:00
tip_base: de75b4c4118c78dcc0164fdaa916bbc53f99225f
git_actions_by_runner: none
authored_pack: false
```

## Pass metric (stated before the run)

1. `python3 -m json.tool` on all three workflow JSON files → EXIT 0
2. Residue scan on `pack/`: no real secrets, emails, absolute home paths,
   `/wavves` install steps, or slash-skill requirements
3. Guidelines musts: stickies (parent or STICKIES.md); Set Fields; Free;
   SEO title in DESCRIPTION; no plagiarize claim against 4817 graph
4. proof_job path: Proof Merge Complete → IF Outcome Pass → Append
   Proof/Block Gate Row; GATE-TABLE-SCHEMA non-empty
5. Locks: PACK=B, GATE-STORE=B, LLM=C, V0=A (no term_id / paragraph-tunnel
   fields)

## (1) JSON validity — measured

```text
python3 -m json.tool pack/01-charge-research-a.json → EXIT 0
python3 -m json.tool pack/02-charge-research-b.json → EXIT 0
python3 -m json.tool pack/03-parent-orchestrator.json → EXIT 0
```

## (2) Residue scan — measured

Strict patterns (`sk-…`, `/Users/…`, emails, `/wavves`, `plugin.json` as
install requirement): **no hits**.

Instructional ban text only (allowed by dispatch):
- `term_id` / paragraph-tunnel named as out-of-scope in locks, prompts,
  GATE-TABLE-SCHEMA
- Cursor / slash-skill REMOVE notices in README and charge system messages

No hardcoded credential secret values; chat-model credential ids are
`PLACEHOLDER` / `PLACEHOLDER_LLM_CREDENTIAL`.

## (3) Guidelines musts — checklist

| must | evidence | result |
|---|---|---|
| Stickies | Parent embeds yellow overview (`color` 4) + 6 step stickies (`color` 2); `pack/STICKIES.md` canonical | PASS |
| Set Fields | Parent node `Set Fields — Topic Locks Proof` (`topic`, `locks`, `proof_job`, `wave_run_id`, …) | PASS |
| Free | DESCRIPTION + STICKIES + Set Fields locks: Pricing Free | PASS |
| SEO title | DESCRIPTION H1: `Coordinate parallel research agents to a proof-gated accept in n8n` (verb + thing + to + in) | PASS |
| Description sections | Who's it for / How it works / How to set up / Requirements / How to customize; ~221 words | PASS |
| No 4817 graph plagiarize claim | No 4817 / Composestitch / copy-graph language in pack/ | PASS |
| Credentials not inline | No `apiKey`/`token` secret values in workflow JSON | PASS |

## (4) proof_job path — measured

Parent workflow: `Parent Orchestrator — Proof-Gated Wave Accept`

```text
Start Wave Run
  → Set Fields — Topic Locks Proof
  → Execute Workflow — Charge A ‖ Execute Workflow — Charge B
  → Merge Charge Returns
  → Proof Merge Complete          (Code; proof_check_id=proof_merge_complete)
  → IF Outcome Pass               (outcome === "pass")
      → Append Proof Gate Row     (Data Table insert → wavves_proof_gate)
          → Emit Pass Rollup
      → Append Block Gate Row     (Data Table insert → wavves_proof_gate)
          → Emit Block Rollup
```

`pack/GATE-TABLE-SCHEMA.md`: non-empty (3738 bytes); columns include
`outcome`, `proof_check_id`, `proof_check_name`, `recorded_at`,
`wave_run_id`, `reason`, optional `merge_fingerprint`/`topic`; no
`term_id` column.

## (5) Locks — checklist

| lock | expected | pack evidence | result |
|---|---|---|---|
| NTV-PACK | B parent + Execute Workflow charges | Parent + `01`/`02` charge workflows; Execute Workflow A‖B | PASS |
| NTV-GATE-STORE | B Data Table | Append Proof/Block Gate Row → `wavves_proof_gate` | PASS |
| NTV-LLM | C generic LangChain chat-model credential | Placeholder credential slots on both charges; README/stickies say importer picks provider | PASS |
| NTV-V0-SCOPE | A no term_id / no paragraph-tunnel | No `term_id` assignment/column; bans stated as out-of-scope | PASS |
| Pricing | Free | DESCRIPTION / STICKIES / locks string | PASS |

## Named failures

None.

## Observations (non-blocking)

1. Charge chat-model nodes are `@n8n/n8n-nodes-langchain.lmChatOpenAi`
   with `openAiApi` credential type. Lock LLM=C is satisfied by
   placeholder credential + importer-swap docs; pack is OpenAI-node-first,
   not a hard fail.
2. Charge B has no sticky node; waveset allows charge placeholders when
   STICKIES.md / parent stickies are canonical.
3. Execute Workflow targets remain `PLACEHOLDER_CHARGE_*_WORKFLOW_ID`
   (documented importer step in README).

## Verdict

**PASS** — ACCEPT gate closed for return_to_O0. No pack rewrite by
evaluator. Git land and n8n.io submit remain O0 / operator-gated.
