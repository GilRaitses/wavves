# NTVB-W1a return — Charge Research A

```yaml
charge: NTVB-W1a
git_actions_by_runner: none
commit_file_list:
  - pack/01-charge-research-a.json
  - findings/NTVB-W1a-return.md
status: done
node_names:
  - Sub-workflow Entry
  - Propagate Locks And Topic
  - Research Agent A
  - Chat Model Credential Slot
  - Charge Return Parser
  - Emit Charge Return
  - Charge A Note
credential_placeholders:
  - openAiApi.id=PLACEHOLDER name="LangChain Chat Model"
schema_notes: >
  Importable sub-workflow JSON. Trigger defines topic/locks/charge_role/proof_job/research_brief.
  Set propagates locks + topic + charge_id=A. Agent v2.2 with hasOutputParser; lmChatOpenAi v1.2
  wired via ai_languageModel (NTV-LLM=C stub; importer may swap provider node). Structured parser
  schema: findings_summary, sources_claims[], status. Final Set emits parent-merge fields.
  Validated python3 -m json.tool EXIT 0. No secrets/paths. Sticky placeholder only; STICKIES.md canonical.
```

## Graph

1. **Sub-workflow Entry** (`executeWorkflowTrigger` 1.1) — parent call entry with typed inputs
2. **Propagate Locks And Topic** (`set` 3.4) — Set Fields for locks, topic, role, proof_job, charge_id
3. **Research Agent A** (`@n8n/n8n-nodes-langchain.agent` 2.2) — define prompt + system message; output parser on
4. **Chat Model Credential Slot** (`lmChatOpenAi` 1.2) — credential placeholder only
5. **Charge Return Parser** (`outputParserStructured` 1.3) — charge return schema
6. **Emit Charge Return** (`set` 3.4) — normalized merge payload for parent
7. **Charge A Note** — optional sticky; W1c owns canonical STICKIES.md

## Locks honored

- NTV-JOB=A, NTV-PACK=B, NTV-LLM=C, NTV-V0-SCOPE=A
- Free template; no Cursor/wavves slash skills in prompts
- Original graph; not copied from 4817 / 7504 / 7158 / 8578

## Proof

- `python3 -m json.tool pack/01-charge-research-a.json` → EXIT 0
- Leak scan: no `sk-`, no `/Users/`, no personal emails, no API keys
