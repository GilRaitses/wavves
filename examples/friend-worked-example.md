# Worked example: building friend with wavves

The document describes one real installation of the wavves system, used
while building **friend**, a city-scale evidence model of Manhattan served
at friend.aimez.ai. The installation is a WORKED EXAMPLE, not a default.
Nothing in the packaged skills points at these paths. You will create your own home,
registry and lane names. Numbers below are quoted from lane findings files
as of 2026-07-06.

## The home

The standing home lives at `<repo>/wavves/`:

```
wavves/
  INDEX.md                       # fast pickup map for fresh agents
  AGENTS.md                      # standing hydration contract (orchestrator-home)
  registry.yml                   # every lane, status, one-paragraph note
  step-log.md                    # synthesis trace, append-only
  rotations/
    rotation-r01-20260705-2340.md  # first rotation handoff (R1 outgoing, R2 assigned)
  lanes/
    20260705_friend-perf-reliability/   # one lane home per bounded workstream
    20260705_thermal-bake-refresh/
    20260704_camera-observability-ext/
```

The repo's own root `AGENTS.md` carries the governance the home defers to
(write policy, commit protocol, naming rules). The home's etiquette locks
include repo-specific infrastructure safety rules, for example an
untouchable-hosts list and a verify-results-before-terminate rule for cloud
instances, written after a real incident in which a batch-compute instance
was terminated while its simulation was still running.

## Lane 1: friend performance and reliability (FPR)

The friend web viewer had an unbounded crash-to-fallback path and an
unsplit caching policy. The lane ran waves W1 through W8 (findings files
`FPR-W1-*.md` ... `FPR-W8-ADV.md`, 48 files) on a shared scaffold branch,
with two adversarial waves (W6 and W8). The W8 findings record their
evaluator as fresh, with no authorship of the waves it judged.

Measured outcomes quoted from `FPR-W8-EVIDENCE.md` and `FPR-W8-ADV.md`:

- Dead-path fallback bounded at 14.8 s against a 60 s ceiling, versus
  "72 s/unbounded pre-remediation".
- Deployed cache headers matched the policy table on the real platform,
  "12/12".
- Warm reload served "152/152 asset+thermal requests ... from cache, 0.00 MB
  transfer", with "console errors/rejections: 0".
- The second adversarial review advanced all seven surfaces with
  "Remediation loops consumed: 0 of 2 per lane". The final diff was 10
  files, +637/-50.

The one coverage gap (an auth-provisioned preview environment) was reported
as a gap and escalated to the operator rather than papered over.

## Lane 2: a data-freshness audit that found nothing to refresh (TBR)

A thermal 3D artifact was suspected stale. The runner's freshness scan found
no upstream input newer than the existing bake and said so plainly in
`TBR-P1.md` ("FINDING (honest): no upstream input changed since the Jun 24
bake. There is nothing to re-bake at the raster level."). The lane pivoted to
embedding provenance (a `generated_at` timestamp plus sha256 hashes of all 65
inputs) into the artifact instead, an additive change of +6,072 bytes. The
adversarial evaluator independently re-hashed four inputs and reproduced the
manifest hash. The gate passed on loop 1 of the 2-loop cap (`TBR-ADV.md`).

## Lane 3: camera observability for friend (OBS)

One lane built a 356-camera annotation deck and ran a cloud detection pass.
Quoted from `OBS-F1-P1.md`:

- 45 on-demand instances processed 341 cameras, 127,404 frames. Per-shard
  runtime 249-319 s (mean 286 s). Wall clock about 32 minutes including
  remediations. Rough cost about $4.
- Two worker defects were caught mid-run and recorded honestly. A missing
  system library killed the first worker start. A too-narrow frame-name
  regex "silently dropping the burst frames" made the first pass end
  "absurdly fast (224 frames/shard)". The runner refused to accept the fast
  signal, fixed the regex and re-ran end to end. The findings note the first
  signal "was false and would have shipped a ~0.2% detection pass if it had
  been trusted".

A sibling wave (`OBS-F2-P1.md`) trained a segmentation model on 43
operator-labeled cameras. All six (period, class) cells passed the 0.5
median-IoU ship gate (macro median 0.660). The findings state the
distribution caveat plainly, "crosswalk is bimodal in both periods. 4 of 10
held-out cameras land under 0.35 day and 4 under 0.35 night (including one
0.00 ...)".

## The rotation

After these lanes, the thread rotated. The outgoing instance wrote
`rotations/rotation-r01-20260705-2340.md`, whose section 0 assigns the
successor identity ("You are **O0.R2**. Ack with that identity and this
file's name before acting."), lists landed positions with commit hashes,
records the background dispatch still running at handoff with pickup
instructions (plus one finished and reconciled before the rotation) and
lists blocked items with what unblocks them. The rotation contract requires
the successor to ack its assigned identity and the rotation file it
hydrated from before acting.

## What to copy

Copy the shapes, not the paths. One standing home, one registry and one lane
home per bounded workstream, findings written incrementally, adversarial gates run by
fresh evaluators with capped loops, rotation files that assign successor
identity. The lane names, cloud vendors and gate metrics above are specific
to this installation and are not defaults of the plugin.
