# Coordinate parallel research agents to a proof-gated accept in n8n

**Pricing:** Free

Run a bounded wave of parallel research agents, merge returns, and hold accept until a named proof check writes pass or block evidence to an n8n Data Table. Originality wedge: **governed wave accept** (alignment packet, parent-plus-two-charges role triad, independent gate evidence). Not another CEO-style orchestrator demo.

## Who's it for

Operators who need parallel AI research with a hard accept gate, not a one-shot chat merge that always succeeds.

## How it works

Set topic, locks, and `proof_job` on the parent. Fan out two **embedded** charge workflows in parallel via Execute Workflow (parameter/JSON). Merge, run **Proof Merge Complete**, write a Data Table pass or block row, then emit rollup only on pass.

## How to set up

1. Import this **single** workflow JSON.
2. Create Data Table `wavves_proof_gate` with columns listed in the Proof + Data Table sticky.
3. Attach a chat-model credential on each embedded charge **Chat Model Credential Slot** (default OpenAI-compatible node; swap for other providers).
4. Edit Set Fields and run **Start Wave Run** once.

## Requirements

n8n with LangChain / AI Agent nodes; one chat-model credential (you choose the provider); n8n Data Tables for proof rows. No community-node dependency for v0.

## How to customize

Swap charge prompts, change the proof check, add a Wait for human lock approval, or extend Data Table columns. Keep proof-before-accept intact. Modular repo files `01`/`02`/`03` are optional source form, not required for this upload.
