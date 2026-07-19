# Proposed skill delta — paragraph-tunnel epistemic classes

- **Owning lane:** pax AVP / APPL (`20260718_apollo-voice-proof`,
  `20260715_apply-case-crack-asp-send`)
- **Findings / locks:**  
  `pax/.../APPL-EPISTEMIC-CLASSES.md`,  
  `pax/.../APPL-P2-TUNNEL.md` (2026-07-19 harden)
- **Failure mode:** Fluency / voice rewrite hides private→mutual conflation
  (EAST-style epistemic tracking error). Existing STACK/COMPARE/GLOSS/FIXTURE
  miss claim-class upgrades after voice.
- **Proposed trigger:** When paragraph-tunnel runs on cold outbound personalization
  paragraphs; also after any voice rewrite of the tunneled field.
- **Proposed instructions (delta only):**
  1. Tag each claim `OBSERVABLE|SHARED|PRIVATE|INFERRED`.
  2. Cold first-touch: only `OBSERVABLE`.
  3. Fail `PN-PRIVATE`, `PN-INFERRED`, `PN-EPISTEMIC-CONVERGE` (owner would
     correct a factual claim).
  4. Capture `gate-captures/<CODE>-pN-epistemic.json`.
  5. After voice: separate reviewer re-runs epistemic+converge; voice must not
     upgrade class.
- **Destination requested:** extend
  `skills/wavves/playbooks/paragraph-tunnel.md` **after AVP-ACCEPT** (not now).
- **Risks:** Over-tagging kills good OBSERVABLE “nice because” profiles; keep
  nice-because whitelist. Do not import EAST games or ToM branding.
- **Operator decision needed:** Promote after Apollo voice proof CLEARED.
