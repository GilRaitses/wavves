# KVC-W1 — wave orchestrator dispatch

```yaml
authority_precedence:
  order:
    - path: waveset.md
      role: wave_plan
    - path: ../../../feature-requests/20260723_wave-context-kv-cache.md
      role: artifact_under_review
```

```text
ROLE: wave_orchestrator KVC-W1. Not moderator. Not charge author for lenses.
HOME: <repo>/wavves/lanes/20260723_wave-context-kv-cache-check/
ARTIFACT: <repo>/feature-requests/20260723_wave-context-kv-cache.md
TIP: de75b4c4118c78dcc0164fdaa916bbc53f99225f

MISSION:
1. Deploy four background charge workers (grounding/contradictions/completeness/adversarial).
2. Each writes ONLY its findings/KVC-*.md + return file.
3. No LAUNCH-AND-EXIT. Checkpoint if yield. Rollup then findings/KVC-verdict.md.
4. return_to_O0 with verdict path. No git. No BUILD. No skill edits.
MODEL: cursor-grok-4.5-high-fast
ESCALATION: to O0 only.
```
