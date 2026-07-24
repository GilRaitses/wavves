# NTVB-W1b return

```yaml
charge: NTVB-W1b
git_actions_by_runner: none
commit_file_list:
  - pack/02-charge-research-b.json
  - findings/NTVB-W1b-return.md
status: done
node_names:
  - Execute Sub-workflow Trigger
  - Lock Wave Packet Fields
  - Adversarial Research Agent
  - Generic Chat Model
  - Structure Charge Return
credential_placeholders:
  - openAiApi / PLACEHOLDER_LLM_CREDENTIAL ("OpenAI API (attach your credential)")
role_split_vs_A: Charge A cite-maps supportive evidence; Charge B runs the adversarial lens for counter-claims, gaps, and accept-blocking risks.
schema_notes: Importable export (name/nodes/connections/active:false/settings). Trigger typeVersion 1.1; Set 3.4; Agent 1.7; lmChatOpenAi 1.2 with ai_languageModel edge. Locks NTV-JOB=A, NTV-PACK=B, NTV-LLM=C, NTV-V0-SCOPE=A, Free, cursor_residue=REMOVE. Merge fields charge_id, charge_role, charge_lens, topic, packet_id, findings, gaps_risks, status. No secrets, no /Users/ paths, no graph copy from 4817/7504/7158/8578.
```

## Artifact

- `pack/02-charge-research-b.json` — Charge Research B sub-workflow for parent Execute Workflow fan-out.

## Validation

- `python3 -m json.tool pack/02-charge-research-b.json` → EXIT 0 (run by charge before return).
