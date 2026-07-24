# FR-20260723 — n8n template fit (wavves → publishable workflow)

status: build-accept-pass
lane: `wavves/lanes/20260723_n8n-template-fit/`
build_lane: `wavves/lanes/20260723_n8n-template-build/`
code: NTV
build_code: NTVB

## Intent (operator)

Charter the n8n version of wavves. Decide what it needs to be to fit the
n8n template library, and what to remove. Submission UX shows Free pricing,
workflow JSON upload, AI check then human review, mandatory guideline
agreement.

## Why this FR exists

There is **no** n8n workflow JSON, sticky-note pack, or template description
in `wavves_build` today (repo search: zero `n8n` hits). The Cursor plugin
(skills, standing home, mod-check/decide/rotate, charter fan-out) is not a
drop-in template. Shipping without a keep/remove matrix risks a low-effort
or Cursor-only submission that fails review.

## External authority (operator-pasted + linked)

- Guidelines:
  https://n8n.notion.site/Template-submission-guidelines-9959894476734da3b402c90b124b1f77
- Example description shape:
  https://n8n.io/workflows/4817-composestitch-separate-images-together-using-n8n-and-gemini-ai-image-editing/
- Submit modal capture (local):
  `assets` under Cursor project (Free pricing, "Submit for AI review")

Mandatory themes from guidelines (operator paste): sticky notes (yellow
explainer + step stickies), renamed nodes, no hardcoded API keys, strip
personal IDs, Set Fields for config, original work, SEO title form
(`Action verb` + object + to/on/in/from + where), ~200-word description
with Who/How/Setup/Requirements/Customize, Free until 3 high-quality
templates for paid eligibility.

## Success for this FR (not BUILD yet)

1. Inventory of wavves core ideas that could map into n8n.
2. Checklist of publish gates from guidelines + example.
3. Library gap note (existing multi-agent/orchestrator templates).
4. KEEP / ADAPT / REMOVE matrix with evidence.
5. Named open forks for `/mod-decide` before any workflow JSON BUILD.

## Out of scope for NTV discovery

- Building or submitting the workflow JSON
- Paid-template commerce
- Editing installed Cursor skills to "become n8n"
