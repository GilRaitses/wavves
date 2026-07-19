# PBB-W1b — eval-harness-design

```yaml
lens: eval-harness
wave: PBB-W1b
repo_state_verified_against: 517dd85190cf93cf744434338dec4b1eb1d859c5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Verdict (this lens)

Ship `evals/check_proof_before_accept.py` as a **stdlib mechanical tripwire**
on charter/ACCEPT fixture text (paragraph-tunnel shape). Do **not** overload
`evals/run_fixtures.py` or `paragraph-tunnel-*` fixtures (PBA-adversarial FM-3).

## Checker contract

| field | value |
|---|---|
| command | `python3 evals/check_proof_before_accept.py` |
| discovery | only `evals/fixtures/proof-before-accept-*/` |
| deps | stdlib; no network; no LLM |
| input | `input.md` (waveset/ACCEPT snippet) |
| expected | `expected.md` with `expected_verdict` + `fail_ids` |

## Mechanical detection rules (fixture-static)

Parse `input.md` for YAML-ish / keyed fields:

1. **`proof_required`** — must be present as `yes|no|n/a` when fixture claims
   a waveset meta block. Missing on a fixture labeled product/visitor →
   treat as process leak for FAIL cases.
2. **PROC-PASS-NO-PROOF** when `proof_required: yes` and ANY of:
   - `proof_job` missing or empty
   - ACCEPT criteria list has process/shell-only markers
     (`LAND-C`, `honesty`, `e2e shell`, `HEAD match`) and **no** named
     proof harness token (`check_proof_before_accept`, `proof_job`,
     `host_height`, `primary product host`, `gate-captures/.*proof`)
3. **PROC-NO-VISUAL** when `proof_required: yes` and
   `visual_accept: yes` (or visual_accept omitted while proof_required yes
   and no `visual_accept: no` + rationale) and no harness command string
   matching `evals/check_proof_before_accept.py` or a
   `proof_harness:` / `dom_harness:` field.
4. **Opt-out rationale** — if `proof_required: yes` and
   (`proof_reference: none` or `visual_accept: no`) without a non-empty
   `rationale:` / `*_rationale:` field → emit `PROC-PASS-NO-PROOF`
   (schema fail; PBA-OPTOUT). Does not waive `proof_job`.

Review-only ids (`PROC-CHROME-THRASH`, `PROC-DEBT-AS-DONE`,
`PROC-BLANK-CANVAS`) are **never auto-emitted** by the mechanical script.
Fixtures may document them in comments; expected.md must not require the
script to detect them.

## Minimum fixtures (W2b)

| dir | expected |
|---|---|
| `proof-before-accept-proc-pass-no-proof-fail` | FAIL `[PROC-PASS-NO-PROOF]` |
| `proof-before-accept-with-proof-pass` | PASS `[]` (all four fields + harness) |
| `proof-before-accept-optout-no-rationale-fail` | FAIL `[PROC-PASS-NO-PROOF]` |
| `proof-before-accept-no-visual-fail` | FAIL `[PROC-NO-VISUAL]` |

## Live DOM/host rule (docs in EXECUTION_WIRING, not this script)

Named harness for product ACCEPT (documented in W2c draft):

```bash
# example binding — product host geometry
python3 <lane-or-repo>/scripts/proof_host_probe.py \
  --url "$PROOF_URL" --selector "$PROOF_HOST_SELECTOR" \
  --out gate-captures/<CODE>-ACCEPT-proof-host.json
```

Pass metric: primary product host `clientHeight > 0` and not blank-canvas
class while chrome may PASS. Screenshot optional.

## README

Add a **disjoint** section under `evals/README.md` (mirror paragraph-tunnel
section). Do not claim LLM replay.

## W2b ownership

`evals/check_proof_before_accept.py` + fixtures + README section (W2d shares
README edit — serialize: W2b owns checker+fixtures; W2d appends README
section after W2b lands, or single editor owns README in W2d).

## Commit file list

- `wavves/lanes/20260718_proof-before-accept-build/findings/PBB-eval-harness.md`

No git. Escalation to O0 only.
