# Glossary

Wavves terms stay as the sources spell them. The sentence after each term is the ordinary class meaning.

**moderator.** The thread a person talks in. Waves go out from it and grades come back. The README also names this operator-facing thread O0.

**moderator term.** A fresh thread that takes over a heavy one. Term ids look like `r02`. The new term starts without the old transcript.

**playbook.** The named route `/wavves` picks from a short request. The README lists bootstrap, charter-lane, check, decide, layover, paragraph-tunnel, proof-before-accept, rotate, kick, pickup, proceed and shrug.

**lane.** One stream of work with its own folder. One bounded stretch, with its own charter and its own finish checks.

**wave.** One round of parallel work inside a lane. The moderator numbers waves from W1 up in `waveset.md`.

**waveset.md.** The lane file. The README calls this charter an alignment packet. It holds scope, grounded facts, locked decisions, file boundaries and acceptance checks.

**alignment packet.** The written directive for one lane. Another process can read it without a person restating the chat.

**standing home.** The `wavves/` folder. A fresh term hydrates from these files and not from a transcript. `INDEX.md` is the fast pickup page.

**registry.yml.** The map of chartered lanes and their status.

**dispatch file.** The per-wave paste block. The README names `dispatch-wN.md`.

**orchestration agent.** The background runner of a wave. The README also calls this task the wave orchestrator. It fans out charge workers and writes the rollup and the gate.

**charge worker.** One background task for one bounded piece of the wave. The README says it does not commit and does not ask the operator questions. The listing calls the same role a runner on the execution layer.

**gate-captures.** JSON and a log for a gate, on disk beside the lane. The README says a hand-written summary is not a gate capture.

**/remeasure.** Turns a done claim into a gate with a claim and a check someone else can rerun. The grade comes from someone other than the author. The listing says the bundled script rejects self-grading, missing fields and placeholder evidence.

**disk gate.** The README rule that a lane advances after a runnable check writes pass or block evidence under `gate-captures`. Failed gates stay failed. Remediation loops are capped. The sources do not give that cap as a number.

**proof-before-accept.** A named proof job on a product lane. The README says a process-only accept cannot clear when proof is required.

**paragraph tunnel.** A mid-render structural gate for one outbound field. The README says it is not a voice copy.

**/mod-check.** A read-only review wave against a written plan. The README verdict words are GO, REVISE and BLOCK, with recommended actions.

**/mod-decide.** Locks open product calls one at a time and writes decision files. The README says locks then sync to the waveset, the dispatch file and the registry so a later wave does not reopen them. That sync is the authority propagation the README names.

**/mod-rotate.** Writes a rotation file and hands the thread to the next term. Older rotation files never change. The next term can audit the chain.

**rotation history audit.** Reads rotation files in order. Gaps in the numbering and breaks in the chain of terms get an ERROR line. The same run flags deleted rotation files, claimed commits missing from git and claimed paths missing from disk.

**pickup check.** Tests the rotation file against local git and against paths on disk. It also checks the JSON work registry. A fix row for a script message sits in five recovery playbooks.

**hydrate.** The fresh term reads the home and starts from those files. Nothing is carried over in the context window.

**/mod-kick.** A move to another machine. The README says the term publishes an allowlist and a short paste. It is not a substitute for rotate or for pickup.

**/layover.** A read-only audit of sibling repos in a multi-root workspace. It writes one report and does not change those repos.

**/shrug.** Carries out recommended actions. The README says a bare shrug stays on the narrow AUTH-10 proceed path. A closed phrase widens it. The listed phrases are all still standing, queue all standing and move, plus proceed all standing.

**model routing table.** A table inside each waveset. It records a recommended model tier for the lane orchestrator and for each wave. The README calls it a cost-control surface and not a measured savings claim.

**gate-and-proof.** Name on a listing image in this repo. The line on the image is to accept work only when a recorded check shows it works. The live site describes that job as `/remeasure`.

**handoff-check.** Name on a listing image in this repo. The line on the image is that a fresh thread checks each handoff and follows a recovery playbook when a check fails. The live site describes that job as the pickup check.

**rotation-audit.** Name on a listing image in this repo for the history audit. The image groups these three names as checks a fresh agent runs from files on disk.

The README also names a self-check loop for proposed skill edits, a set of orchestration fail ids and mechanical prose checks. The checker files and the two docs it points to are not in this repository, so this reading does not restate those id lists.
