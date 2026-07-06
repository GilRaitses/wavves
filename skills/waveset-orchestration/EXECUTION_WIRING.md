# Execution wiring: runnable gates, harnesses, evidence

The charter and dispatch docs describe *what* a waveset will do. This
describes *how* the runner executes the gates, meaning the shell writing and
wiring that turns an adversarial or acceptance wave from an assertion into
measured evidence. Invoke this whenever a wave has a gate to run, a transition
to measure, or a decision to record.

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
for i in $(seq 1 24); do                  # poll the event to completion
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

## Rule 1b, long COMPUTATIONS run in the background; keep working

Rule 1 is for measured transitions (a probe must survive across an event). It
is NOT a license to sit blocking on every long process. For a plain long
computation (batch data processing, extraction, inference, render, large
fetch) with no concurrent probe to keep alive:

- Launch it as a BACKGROUND shell, do a one-shot smoke check that it started,
  then move on to any other work in your scope while it runs. Reconcile when
  the completion notification arrives.
- Never announce "this benchmarks at ~3 minutes, so I'll run it now" and then
  hold the session blocked for 10. Benchmarks underestimate; a blocked runner
  starves the whole wave.
- Only block when the result truly gates every remaining action you could
  take, and even then prefer finishing sibling tasks first, then awaiting.
- Orchestrators, put this instruction in every runner dispatch prompt. A
  runner that serializes on long processes defeats the point of parallel
  waves.

## Rule 2, gates are runnable; evidence is captured

- Define the pass metric BEFORE the run (for example "max gap while liveness
  up = 0", "p95 first-token < 1.5s", "zero 5xx during rollover"). No
  reassurance bias.
- Write the JSON summary and log to the lane home `gate_captures/`.
- The verdict in the step log cites the measured numbers and the capture path,
  never a claim. If the metric is not met, the gate FAILS and the wave
  repeats.

## Rule 3, read-only grounding vs operator-gated mutation

- Research and discovery touch infrastructure READ-ONLY only (describe, get,
  list, metric reads, log reads). Change nothing.
- Any mutation (deploy, scale, teardown, DNS, secret write) is OPERATOR-GATED
  and runs only in a later wave with explicit approval. State in the charter
  which CLI calls are read-only grounding and which one is the gated mutation,
  so an unprimed runner cannot accidentally mutate production during research.

## Rule 4, record the decision durably

A completed waveset that made a real decision records it so it survives the
chat thread. If the repo keeps structured decision records, write one that
names the decision, the measured evidence (gate numbers plus the capture
path), the adversarial verdict, cost deltas, deferred items, and what it
supersedes. If the repo has no decision store, a dated decision file in the
lane home is the minimum.

## Rule 5, measurement harness shape

A probe is dependency-free (stdlib only), polls a LIVENESS endpoint and a REAL
USER endpoint at a fixed cadence, and records the max contiguous window where
the real call returns non-2xx while liveness stays 2xx. That window is the
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
  --out gate_captures/gap.json
```

Pass = `max_gap_while_live_up_ms == 0`. The script also logs each GAP
open/close and a sparse mutating call (for example a create) when
`--mutate-path` is given.

## Checklist for a gate-running wave

```
- [ ] Pass metric defined before the run (hard, checkable)
- [ ] Harness written/selected; dependency-free; emits JSON to gate_captures/
- [ ] Measured transition runs as ONE long-blocking command (probe survives)
- [ ] Mutation (if any) was operator-gated and approved; research stayed read-only
- [ ] Verdict cites measured numbers + capture path (not a claim)
- [ ] Decision recorded durably (Rule 4)
- [ ] Step log + registry status updated; committed/pushed per the repo protocol
```
