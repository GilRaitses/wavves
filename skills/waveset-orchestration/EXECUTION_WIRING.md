# Execution wiring: runnable gates, harnesses, evidence

The charter and dispatch docs describe *what* a waveset will do. The execution
wiring describes *how* the runner executes the gates, meaning the shell writing and
wiring that turns an adversarial or acceptance wave from an assertion into
measured evidence. Invoke this whenever a wave has a gate to run, a transition
to measure or a decision to record.

## Rule 1, one long-blocking command for any measured transition

A process started with `&` or `nohup` from a tool-call shell is reaped when
that tool call returns. So if you start a probe in one call and trigger the
event in a later call, the probe is already dead and you measure nothing.
(Observed first hand. A `nohup` poller logged two lines and exited while a
deploy ran in a separate call.)

When you must MEASURE across an action (deploy, instance recycle, DB
migration, load test, cutover), run the whole sequence inside ONE command and
size the tool's blocking window above the probe duration so the call (and the
process tree) stays alive:

```bash
# start the probe in the background OF THIS command
python3 probe.py --base "$URL" --seconds 360 --out cap.json > cap.log 2>&1 &
PROBE=$!
sleep 6                                   # let the baseline settle
<trigger the event>                       # e.g. start the deployment
for i in $(seq 1 24); do                  # poll the event until finished
  sleep 15
  ST=$(<query deploy status>)
  echo "[$(date -u +%H:%M:%S)] $ST"
  case "$ST" in SUCCEEDED|FAILED|ROLLBACK_SUCCEEDED) break;; esac
done
wait $PROBE                               # let the probe finish its window
cat cap.json                              # read the measured summary
```

Set the blocking window to roughly `(probe seconds + slack) * 1000` ms. Do a
one-shot status check if you background the whole thing instead.

## Rule 1b, long COMPUTATIONS run in the background. keep working

Rule 1 is for measured transitions (a probe must survive across an event). The
rule is NOT a license to sit blocking on every long process. For a plain long
computation (batch data processing, extraction, inference, render, large
fetch) with no concurrent probe to keep alive:

- Launch it as a BACKGROUND shell, do a one-shot smoke check that it started,
  then move on to any other work in your scope while it runs. Reconcile when
  the return notice arrives.
- Never announce "this benchmarks at ~3 minutes, so I'll run it now" and then
  hold the session blocked for 10. Benchmarks underestimate. a blocked runner
  starves the whole wave.
- Only block when the result truly gates every remaining action you could
  take and even then prefer finishing sibling tasks first, then awaiting.
- Orchestrators, put this instruction in every runner dispatch prompt. A
  runner that serializes on long processes defeats the point of parallel
  waves.

## Rule 2, gates are runnable. evidence is captured

- Define the pass metric BEFORE the run (for example "max gap while liveness
  up = 0", "p95 first-token < 1.5s", "zero 5xx during rollover"). No
  reassurance bias.
- The pass metric comes from the charter or from the orchestrator, never from
  the agent whose work the gate judges and the gate is graded by an evaluator
  with no authorship of that work.
- Write the JSON summary and log to the lane home `gate-captures/`. A capture
  is the harness's own output. a hand-authored summary is fabrication and the
  verdict names the command that produced each capture so it can be
  reproduced.
- The verdict in the step log cites the measured numbers and the capture path,
  never a claim and reports the full result distribution alongside any gate
  statistic. headline claims stay scoped to the measured sample size and
  conditions. If the metric is not met, the gate FAILS with named failures and
  the wave repeats, within the charter's remediation-loop cap. at the cap,
  escalate to the orchestrator instead of looping.

Manual inspection path:

```text
wavves/lanes/<YYYYMMDD>_<lane-label>/
  gate-captures/
    <gate>.json
    <gate>.log
  findings/
    <gate-verdict>.md
```

Inspect the JSON first, then the log, then the verdict. The numbers in the
verdict must match the capture. If a capture is missing, hand-authored or
cannot be rerun from the named command, the gate is not accepted.

## Rule 3, read-only grounding vs operator-gated mutation

- Research and discovery touch infrastructure READ-ONLY only (describe, get,
  list, metric reads, log reads). Change nothing.
- Any mutation (deploy, scale, teardown, DNS, secret write) is OPERATOR-GATED
  and runs only in a later wave with explicit approval. State in the charter
  which CLI calls are read-only grounding and which one is the gated mutation,
  so an unprimed runner cannot accidentally mutate production during research.
- OPERATOR-GATED means the human operator. The runner requests approval
  through the dispatching orchestrator and the orchestrator relays approval
  it holds from the operator. the orchestrator's own judgment never
  substitutes for the operator gate.
- Never pass `--mutate-path` to the probe outside an approved mutation wave.
  The flag fires real POST calls. in research and discovery waves the probe
  runs read-only.

## Rule 4, record the decision durably

Some repos treat their decision store, system state or registry surfaces as
separately gated. Writing a gated surface requires the charter or dispatch
directive to authorize it explicitly. a runner whose directive is silent on
those surfaces hands the record content back to the orchestrator in its
findings instead of writing it.

A waveset that made a real decision records it so it survives the chat thread.
If the repo keeps structured decision records, write one that names the
decision, the measured evidence (gate numbers plus the capture path), the
adversarial verdict, cost deltas, deferred items and what it supersedes. If
the repo has no decision store, a dated decision file in the lane home is the
minimum.

## Rule 5, measurement harness shape

A probe is dependency-free (stdlib only), polls a LIVENESS endpoint and a REAL
USER endpoint at a fixed cadence and records the max contiguous window where
the real call returns non-2xx while liveness stays 2xx. The window is the
user-visible gap. Throttle quota-limited calls (for example a create that
counts against a daily cap). Emit a JSON summary the gate verdict can cite.

Generic, ready to copy and adapt at
**[scripts/transition_gap_probe.py](scripts/transition_gap_probe.py)**.

```bash
# measure the user-visible gap across a transition (liveness vs a real endpoint)
python3 scripts/transition_gap_probe.py \
  --base https://service.example \
  --live-path /health \
  --real-path /api/status \
  --seconds 360 --cadence-ms 500 \
  --out gate-captures/gap.json
```

Pass = `max_gap_while_live_up_ms == 0`. The script also logs each GAP
open/close and a sparse mutating call (for example a create) when
`--mutate-path` is given. `--mutate-path` is itself a mutation under Rule 3
and runs only in an approved mutation wave.

## Checklist for a gate-running wave

```
- [ ] Pass metric defined before the run (hard, checkable)
- [ ] Harness written/selected; dependency-free; emits JSON to gate-captures/
- [ ] Measured transition runs as ONE long-blocking command (probe survives)
- [ ] Mutation (if any) was operator-gated and approved; research stayed read-only
- [ ] Verdict cites measured numbers + capture path (not a claim)
- [ ] Decision recorded durably (Rule 4, gated surfaces only with explicit authorization)
- [ ] Step log (append-only, never rewrite prior entries) + registry status updated
- [ ] Findings end with the commit file list for the orchestrator (exclusions stated) and the no-git statement; the orchestrator commits/pushes per protocol
```
