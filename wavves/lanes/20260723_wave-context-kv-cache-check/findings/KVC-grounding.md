# KVC-W1a — grounding

```yaml
lens: grounding
wave_id: KVC-W1a
model: cursor-grok-4.5-high-fast
tip: de75b4c4118c78dcc0164fdaa916bbc53f99225f
artifact: feature-requests/20260723_wave-context-kv-cache.md
verdict_lean: REVISE
escalation: O0 only via orch
git: none performed
```

## Verdict lean (this lens)

**REVISE.** Core wired seams exist and match the cited paths: WOF checkpoint /
`PROC-ORCH-NO-RESUME-CONTRACT`, PAS stale-queue / standing remasure, and
mod-rotate hydrate-from-files against an empty `wavves/rotations/` (RTH-W1e R2).
HF and RTH are correctly labeled analogy / illustration. Tip pin is consistent
across KVC lane docs + registry (HEAD remasure cited from orch launch; this
charge ran no git).

Blocking grounding issue for decide: open call **WOF-BIND** still asks whether
to land inside WOF BUILD, but WOF FR + WOFB are already SHIPPED. Problem #1 also
overstates WOF as lacking a durable resume contract when live charter/AGENTS
already mandate the checkpoint. Rotate empty-disk claim remains fully grounded.

## Claims vs evidence

| claim | evidence_path | match |
|---|---|---|
| Artifact exists; status `ready-for-mod-check` | `feature-requests/20260723_wave-context-kv-cache.md` | yes |
| README FR row same status | `feature-requests/README.md` (FR-20260723-wave-context-kv-cache) | yes |
| KVC lane chartered; tip `de75b4c…` | `wavves/registry.yml` KVC; `waveset.md`; `dispatch-w1.md`; `findings/KVC-W1-launch.md` tip_remeasured | yes (cross-doc; no git this charge) |
| INDEX lists KVC active lane | `wavves/INDEX.md` `active_lanes` KVC | yes |
| INDEX `feature_requests.open` lists this FR | `wavves/INDEX.md` `feature_requests.open` | **no** (absent; see GAP-KVC-G3) |
| WOF leave-act + checkpoint + `PROC-ORCH-NO-RESUME-CONTRACT` | WOF FR leave-acts / resume; live `skills/charter/SKILL.md` Leave-acts; `wavves/AGENTS.md` §2 | yes |
| WOF FR land status | WOF FR Status **SHIPPED**; WOFB GATE; registry WOF/WOFB completed | yes (SHIPPED) |
| PAS fail ids `PROC-PROCEED-STALE-QUEUE`, `PROC-PROCEED-CHAT-INVENTORY` | PAS FR fail table; live `skills/wavves/playbooks/proceed.md` | yes |
| Standing file is program cache home `wavves/standing/…` | PAS FR PS-02; dir + `wavves/standing/20260723_all-queued-lanes.md` on disk | yes (path real) |
| mod-rotate hydrates from rotation files / newest exemplar | `skills/mod-rotate/SKILL.md` (variant A; “newest existing file”) | yes |
| init §4–5 identity + rotation contract | `skills/wavves-init/SKILL.md` §4–5; live `wavves/AGENTS.md` §4–5 | yes |
| `wavves/rotations/` empty; INDEX `current_rotation: none` | remasured disk; `wavves/INDEX.md` | yes |
| RTH-W1e R2 empty-rotations cite | `lanes/20260723_mod-rotate-theory-research/findings/RTH-adversarial.md` §R2; `RTH-SYNTHESIS.md` fact row | yes (illustration lane) |
| HF blog = external analogy only | FR Inspiration line; waveset Grounding seams | yes (labeled) |
| Ban transformer-KV / RotatE isomorphism | FR Non-goals + fail id `PROC-KV-ISOMORPHISM-CLAIM` | yes (text present) |
| Out of scope PUO / IPB / MDA / voice | FR Wired FRs / Non-goals | yes |
| Open call WOF-BIND: “part of WOF BUILD vs after WOF” | WOF FR SHIPPED; WOFB completed | **stale** (GAP-KVC-G1) |
| Problem #1: WOF yields without checkpoint → invent past / chat resume | live charter already requires checkpoint; fail id shipped | **partial** (GAP-KVC-G2) |
| Proposed eval `evals/check_wave_context_kv_cache.py` | path absent today | n/a (sketch, not claimed live) |
| Proposed `wavves/rotations/_template.md` | absent; open call ROTATION-TEMPLATE | n/a (open call) |
| KV-06 docs home README or `EXECUTION_WIRING` | `README.md` tracking; `skills/charter/EXECUTION_WIRING.md` exists | yes (optional home real) |

## Named gaps

### GAP-KVC-G1 — Open call WOF-BIND presupposes unlanded WOF BUILD
- **Severity:** medium (blocking for honest decide wording)
- **Evidence:** FR open call #2 asks WOF BUILD vs separate CTX-KV after WOF.
  WOF FR Status is SHIPPED; WOFB `findings/WOFB-GATE.md` completed; registry
  WOF/WOFB `completed`.
- **Fix lean:** Rewrite WOF-BIND to pick among (a) thin patch on shipped WOF
  seams + CTX-KV evals/docs, (b) separate CTX-KV BUILD after remasure, or
  (c) docs/evals-only bind. Drop “part of WOF BUILD.”

### GAP-KVC-G2 — Problem #1 overstates WOF as cache-less
- **Severity:** low-medium
- **Evidence:** Live `skills/charter/SKILL.md` Leave-acts and `wavves/AGENTS.md`
  already require `findings/<wave>-orch-checkpoint.md` and name
  `PROC-ORCH-NO-RESUME-CONTRACT`. FR still correctly *binds* to that fail id
  (KV-01 / `PROC-KV-YIELD-NO-CACHE`), but the problem intro lists WOF as an
  equally “open” invent-past surface beside empty rotations.
- **Fix lean:** Frame WOF as shipped resume contract needing shared
  vocabulary / schema / evals bind; keep rotate empty-disk and PAS remasure
  as the stronger live gaps.

### GAP-KVC-G3 — INDEX open FR list omits this artifact
- **Severity:** low
- **Evidence:** `feature-requests/README.md` lists the FR
  `ready-for-mod-check` and KVC is in `active_lanes` / registry, but
  `wavves/INDEX.md` `feature_requests.open` has no
  `FR-20260723-wave-context-kv-cache` row (WOF/PAS/PUO/IPB only under open).
- **Fix lean:** O0 inventory remasure when landing check; not a false path
  inside the FR body.

## Non-blocking nits

- NIT-1: `feature-requests/README.md` WOF row still says `revised-after-WOF`
  while WOF FR body + INDEX open row say shipped. Remasure before Next BUILD
  charter (FR Next already says remasure WOF/PAS land status).
- NIT-2: On-disk standing file
  `wavves/standing/20260723_all-queued-lanes.md` pins tip `26ad2d2…` and
  pre-decide PAS rows; supports the FR’s stale-queue risk as live illustration,
  not a wrong cite in the FR.
- NIT-3: RTH tip `7aecdfb…` ≠ KVC tip `de75b4c…`. Treat RTH as illustration
  only (waveset already does).

## Foreign / analogy labels

| pointer | label |
|---|---|
| Hugging Face KV Caching blog | external analogy only |
| `RTH-SYNTHESIS.md` / RTH-W1e R2 | illustration / research memo |
| Transformer KV tensors / RotatE | banned isomorphism (FR Non-goals) |

## No-git statement

This charge performed **no git** commands. Tip consistency is from lane
artifacts + registry + orch `KVC-W1-launch.md` remasure row. Disk remasure
covered `wavves/rotations/` (empty), INDEX identity/rotation fields, registry
KVC, README FR row, live charter leave-act text, PAS proceed playbook fail
ids, and RTH cite paths.
