# NTV-W1c: library gap (multi-agent / orchestrator templates)

| Meta | |
|---|---|
| charge_id | NTV-W1c |
| tip_base | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| lens | originality competitors vs wavves-shaped gap |
| status | complete (≥2 public cites) |

## Repo constraint (charter)

At charter, this repo has **zero** `*n8n*` workflow JSON files. Any later BUILD is greenfield relative to this codebase, not a port of an existing graph here.

## Cited competitors / playbooks (public pages only)

### 1. Collaborative sales planning with multi-agent AI, Google Docs, and Slack

- **URL:** https://n8n.io/workflows/7504-collaborative-sales-planning-with-multi-agent-ai-google-docs-and-slack/
- **What it covers:** Free bootstrap for a CEO orchestrator that calls Marketing, Operations, and Finance tool agents once, merges their JSON/Markdown into a sales-season plan, then exports a Google Doc PDF and optionally shares to Slack. Teaches coordinator plus specialist role prompts and document handoff, not durable governance.

### 2. Beginner manager agent with sub-agent tools

- **URL:** https://n8n.io/workflows/7158-beginner-manager-agent-with-sub-agent-tools/
- **What it covers:** Manager Agent routes user input to Email or Data Agent Tool nodes, each with its own memory and OpenAI model. Focus is conversational routing and modular agent tools under `@n8n/n8n-nodes-langchain`, not wave ownership or accept gates.

### 3. Run multiple tasks in parallel with asynchronous processing and webhooks

- **URL:** https://n8n.io/workflows/8578-run-multiple-tasks-in-parallel-with-asynchronous-processing-and-webhooks/
- **What it covers:** Main Orchestrator plus Asynchronous Worker pattern: Execute Workflow with wait-for-completion off, Wait nodes, and webhook callbacks to collect parallel results. Covers fan-out/fan-in mechanics for long-running sub-workflows, not role triad or proof-before-accept.

### 4. Official playbook: Multi-agent systems (n8n Blog)

- **URL:** https://blog.n8n.io/multi-agent-systems/
- **What it covers:** Official tutorial on hierarchical multi-agent patterns in n8n (coordinator plus specialized sub-agents, workflows-as-tools, RAG sub-agent, sequential vs parallel handoff). Competes on "how to wire agents," not on locked decisions, independent graders, or term-identity rotation.

Related framing (same family, not counted as a separate workflow): https://blog.n8n.io/ai-agent-orchestration-frameworks/ compares orchestration frameworks and positions n8n for agent-to-agent sequential, parallel, and hierarchical delegation.

## What the library already saturates

Published templates and official posts already own:

1. **Prompt-role multi-agent demos** (CEO/departments, manager/email/data).
2. **LangChain agent + Agent Tool wiring** with memory and model per role.
3. **Async parallel sub-workflow fan-out** with Wait/webhook join.
4. **One-shot plan or reply outputs** (PDF, Slack, chat), then stop.

They do **not** publicly productize: alignment packets as first-class durable scope, hard O0 / wave-orch / charge separation with file (or artifact) ownership, independent disk/gate evidence before accept, proof-required accept branches, or rotation with monotonic term identity so stale runners are recognizable.

## Named originality gap

**Gap name: Governed wave accept (alignment + independent gates + proof), not another CEO-agent demo.**

A wavves-shaped template could differentiate **if** those ideas are later adapted to **n8n-native mechanisms** (sub-workflows, Execute Workflow, Wait/webhooks, credentials, Data Store / Sheets / Drive artifacts, sticky documentation), without cloning competitor graphs:

| wavves idea | Differentiating claim (n8n-native later) |
|---|---|
| Alignment packets | Structured brief + locked-decision fields (Set Fields / Data Store / Drive packet) that every charge sub-workflow must read; scope and acceptance written before agents run, not only in system prompts. |
| Role triad (O0 / wave orch / charge) | Three workflow layers with hard boundaries: operator-facing trigger (moderator), one orchestrator that only fans out and joins, charge sub-workflows that never rewrite locks or land "git." Collapse of orch into charge is a documented anti-pattern. |
| Bounded waves + ownership | Explicit charge IDs and disjoint write targets (artifact paths or record keys) so parallel workers cannot clobber each other; orch owns rollup only. |
| Disk gate captures | Separate evaluator path that writes pass/block evidence to a durable artifact under a gate folder or sheet; accept branch blocked until evidence exists; capped remediation, not silent retry. |
| Proof-before-accept | Named proof job field; process-only "looks done" cannot clear when proof is required. |
| Rotation / term identity | Handoff record with monotonic term id for the orchestrator execution lineage so resumed or replaced runs reject stale instructions. |

That package is the originality wedge against sales-CSO and manager-subagent templates, which stop at role prompts plus merge/share.

## Explicit non-copy rule

Existing multi-agent n8n templates and orchestrator-worker blogs are **competitors for originality**, not sources to copy. Do not import, regraph, or resell their node layouts, prompts, or sticky text. Research cites public titles and URLs only. Later BUILD (out of this charge) must invent a distinct use case and graph that carries only the wavves ideas that survive n8n product and review constraints.

## Escalate?

No. Search and fetch returned ≥2 template URLs plus an official blog playbook. No block for O0.
