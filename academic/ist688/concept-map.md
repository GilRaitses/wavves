# Class ideas and wavves features

The class phrases below are not renamed product terms. Charts of the file home and of the two sourced orders are in the PDF.

## Three ways the class already described the work

| Class description | Wavves term | Where it shows up |
|:------------------|:------------|:------------------|
| A short request into a context store | `/wavves` and the standing home | The class phrase is context store. The product files are the home and `waveset.md`. The request itself stays short. |
| One bounded stretch of work with a clear finish line | lane, wave and gate | Charter one lane. Number waves from W1 up. Finish checks are the gates and the acceptance checks in the charter. |
| Freeze traces and check them, instead of summarizing the chat | rotation file, `gate-captures`, pickup check, rotation history audit | Older rotation files never change. A later term checks files, commits and paths. A hand-written summary is not a capture. |

## Class ideas and the feature that does the job

| Class idea | Wavves term or function | What the sources say |
|:-----------|:------------------------|:---------------------|
| Chatbots, prompts and prompt methods. A short request in ordinary language. | `/wavves` and a playbook | The entry takes the request, checks the home and runs one playbook. The published examples are short tasks. |
| Conversation memory and a conversation buffer that keeps recent turns. | No buffer control in these sources | The sources do not describe a buffer of recent turns or a setting that shrinks what the next request sends. Older work sits in files. `/mod-rotate` starts a new term. |
| Context window, token count and cost. A smaller model and a flagship model. | Listing FAQ and the model routing table | The next term carries nothing forward in the context window. Each waveset records a tier per role. The README publishes no token counts and no savings figure. It does not name a flagship model. |
| Context window bloat. Long work fills the window and raises token cost and wait time. | lane, wave, standing home, `/mod-rotate` | Long work is chartered as waves with state on disk. A heavy thread is handed to the next term. These sources do not publish a token cost or a wait time. |
| Context rot. Recaps lose detail, constraints and error notes. | `/remeasure`, pickup check, rotation history audit | A later term checks JSON, logs, claimed commits and claimed paths. A hand-written summary is not a gate capture. |
| Agents do not need a bigger window or endless recaps for large work. | hydrate from the home | The listing says the next term hydrates from files with nothing carried over in the context window. The README says fresh instances never hydrate from transcripts. |
| Lasting state lives in files another process can read. | `wavves/` home | `INDEX.md`, the lane waveset, `gate-captures`, rotation files and, in the README, `registry.yml`. |
| One bounded stretch with a clear finish line. | lane, wave and gate | A lane is one folder. A wave is one round from W1 up. Gates record pass or block. Failed gates are reported as failed. |
| Write results out as artifacts and later check those files. | `gate-captures` and `/remeasure` | JSON and a log land on disk. Someone other than the author grades the capture. The command that made the capture is named so another person can rerun it. |
| Separate workers are optional. Artifacts and written directives are required so another process can pick up the work. | waveset, dispatch file, rotation file, runners | The charter, the dispatch and the rotation file are the written record a new term reads. The sources also describe runners for the wave. They do not call those runners optional. |
| Model comparison and evaluation on quality, cost and latency. A later check against recorded evidence, not a self-score. | grade on the capture and the model routing table | The listing rejects a self-grade. Cost is the tier table. The README says that table is not a measured savings claim. These sources do not report a latency figure. |
| Retrieval, embeddings and a vector database. Streamlit apps that host the student tools. | No matching feature in these sources | These sources do not describe embeddings, a vector database or a Streamlit app. The store a later step reads is the `wavves/` folder. Streamlit is how this class hosts its own tools. |

## Model tiers recorded before a wave

The README says each `waveset.md` includes this table. It calls the table a cost-control surface and not a measured savings claim.

| Role | Model tier | Reason in the README |
|:-----|:-----------|:---------------------|
| lane orchestrator | high-reasoning | cross-file planning and gate design |
| discovery runners | fast | broad search, summaries, inventory |
| build runners | balanced | bounded edits with local validation |
| adversarial gate | high-reasoning | defect finding and risk judgment |
| acceptance gate | high-reasoning | final verification and caveat review |

The README says to record runner count, expected file reads, expected gate cost and model tier before execution. A later pass can compare those tiers with token or billing records only when the environment exposes them. Discovery runners are the role whose stated reason includes summaries. Gate evidence is a separate record.
