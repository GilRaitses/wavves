# NTV — LLM

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_n8n-template-fit/`
- **repo_state_verified_against:** `de75b4c4118c78dcc0164fdaa916bbc53f99225f`
- **Question:** Default LLM credential surface for v0?
- **Options considered:**
  - A: OpenAI
  - B: Google Gemini
  - C: Generic LangChain chat model (importer picks)
- **Pick:** C
- **Rationale:** Operator bare shrug (AUTH-10 proceed as recommended). Lean was C.
- **Implications for BUILD:** Wire AI Agent / chat model nodes to a generic LangChain chat-model credential slot. Stickies: attach whichever provider credential the importer has. Do not hardcode API keys. Do not require a single vendor for the Free template to run.
