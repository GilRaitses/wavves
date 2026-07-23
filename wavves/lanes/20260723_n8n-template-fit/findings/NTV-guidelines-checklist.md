# NTV guidelines checklist — mandatory vs optional publish gates

charge: NTV-W1b
lane: `wavves/lanes/20260723_n8n-template-fit/`
tip_base: `de75b4c4118c78dcc0164fdaa916bbc53f99225f`
mode: research / decide-prep (no workflow JSON, no submit)

## Sources

| ID | Path or URL |
|----|-------------|
| G | `wavves/lanes/20260723_n8n-template-fit/references/guidelines-excerpt.md` (working authority; Notion may be empty shell) |
| E | https://n8n.io/workflows/4817-composestitch-separate-images-together-using-n8n-and-gemini-ai-image-editing/ |
| M | `wavves/lanes/20260723_n8n-template-fit/references/submit-template-modal.png` |

Locked context for this lane: first submit pricing is Free (paid needs ≥3 high-quality templates first). Sticky notes treated as mandatory for later BUILD.

## Gate checklist

| # | Gate | Class | Notes | Cite |
|---|------|-------|-------|------|
| 1 | Sticky notes: yellow sticky with full description | **mandatory** | Guidelines TLDR and Workflow section. Locked assumption for later BUILD. | G |
| 2 | Sticky notes: white/neutral stickies for steps | **mandatory** | Pair with yellow full-description sticky. | G |
| 3 | Embed media in stickies (images, etc.) | optional/encouraged | Allowed when it clarifies steps. | G |
| 4 | Loom walkthrough | optional/encouraged | Explicitly encouraged, not required. | G |
| 5 | Rename all nodes | **mandatory** | No default/generic node names left in the graph. | G |
| 6 | No hardcoded API keys in HTTP (or other) nodes | **mandatory** | Credentials must not sit inline in the workflow. | G |
| 7 | Use credentials (n8n credential store), not inline secrets | **mandatory** | Same Workflow security theme as keys. | G |
| 8 | Strip personal IDs | **mandatory** | Remove account-specific or operator-personal identifiers before publish. | G |
| 9 | Set Fields (or equivalent) for configurable values | **mandatory** | Config surface for users, not buried literals. | G; E shows Edit Fields (Set) in stack |
| 10 | Original work; no steal/repost of others' workflows | **mandatory** | Repost/steal is a ban-level failure. Fill library gaps. | G |
| 11 | High quality, practical, broad appeal with actionable specificity | **mandatory** (quality bar) | Success traits for review acceptance, not a form field. | G |
| 12 | SEO title form: Action verb + thing + to/on/in/from + where; sentence case | **mandatory** | Example title matches pattern: Compose/Stitch separate images together using n8n & Gemini AI image editing. | G; E |
| 13 | No spammy emoji in titles | **mandatory** | Guidelines ban spammy emoji titles. | G |
| 14 | Description ~200 words | **mandatory** (target) | Guidelines ask for about 200 words of clear English. | G |
| 15 | Description sections: Who's it for; How it works; How to set up; Requirements; How to customize | **mandatory** | Guidelines section names. Map to example labels below. | G |
| 16 | Example section shape: intro; Good to know; How it works; How to use; Requirements; Customising | **mandatory** (shape reference) | Published high-quality example. Intro covers use/who; Good to know is extras; How to use ≈ How to set up; Customising ≈ How to customize. Prefer matching this live shape when drafting. | E; G Example shape reference |
| 17 | Clear English Markdown; no HTML tags | **mandatory** | Description page rules. | G |
| 18 | Community nodes: self-hosted disclaimer + workflow image at top | **mandatory if** community nodes used; else N/A | Only when the template depends on community nodes. | G |
| 19 | Pricing: Free on first submit | **mandatory** (lane lock) | Modal offers Free. Paid eligibility only after ≥3 high-quality templates. This FR locks first submit to Free. | M; G Payment; lane lock |
| 20 | Paid eligibility (≥3 high-quality templates first) | optional later; **blocked for first submit** | Creator must deliver and keep paid templates accessible; failure may ban. Out of scope until Free templates qualify. | G |
| 21 | Submit UX: upload Workflow JSON | **mandatory** at submit | Modal drop zone: drag/drop or browse Workflow JSON. | M |
| 22 | Submit UX: agree to Terms and submission guidelines | **mandatory** at submit | Checkbox required before Submit for AI review. | M |
| 23 | Review path: AI check then human review | **mandatory** process | Modal copy: AI check before human review; button Submit for AI review. | M |
| 24 | Read guidelines before submit | **mandatory** process | Modal instructs reading guidelines; links to them. | M |
| 25 | Assume new n8n user; plug-and-play where possible | optional/encouraged (strong) | Workflow authoring guidance. Raises acceptance odds. | G |
| 26 | Look like published high-quality examples | optional/encouraged (strong) | TLDR success bar; use example 4817 as shape reference. | G; E |

## Section name map (guidelines → example 4817)

| Guidelines (G) | Example page (E) | Role |
|----------------|------------------|------|
| (opening / Who's it for) | Intro paragraph under title | Who and what the template does |
| (not named; extras) | Good to know | Cost, geo limits, caveats |
| How it works | How it works | Step narrative of the graph |
| How to set up | How to use | How a user runs or adapts triggers |
| Requirements | Requirements | Accounts, services, deps |
| How to customize | Customising this workflow | Extension ideas |

## Decide-prep notes (not BUILD)

- Sticky notes (yellow + step stickies) are **mandatory** for any later BUILD charge.
- First publish path is Free only; do not plan paid submit UX until ≥3 high-quality templates exist.
- Do not clone example workflow JSON; use E only for description section shape and quality bar.
- Community-node disclaimer is conditional; N/A if the wavves template uses only built-in or official nodes.
