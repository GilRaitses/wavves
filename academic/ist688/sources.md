# What this reading is drawn from

Drafted 2026-11-06. Class reading for review. Not a lab submission and not the sold skill package.

## Included

- Public site text at https://wavves.aimez.ai/ as fetched that day. The same words are in `index.html` in this repo.
- Public listing text at https://www.agensi.io/skills/wavves as fetched that day.
- `README.md` in this repo. The version line there is 0.5.0.
- Plain claims on three listing images in this repo.
  - `assets/listing/gate-and-proof.png` for the kit name and the line about accepting work only when a recorded check shows it works.
  - `assets/listing/handoff-check.png` for the kit name and the line about a fresh thread checking a handoff and following a recovery playbook when a check fails.
  - `assets/listing/long-horizon-bundle.png` for the three kit names. The image says a fresh agent checks what the last one claimed, from files on disk. It also calls the kits one zip with three kit folders.

## Left out on purpose

- Example counts, sample paths and sample commit ids drawn on those listing images.
- The README paths `examples/usage.md`, `docs/public-copy-gates.md`, `docs/purpose-gates.md`, `skills/` and `evals/`. The README names them. They are not in this repository, so their contents are not restated. The fail-id list stays in the README for the same reason.
- https://www.agensi.io/skills/wavves-long-horizon-bundle returned 404 that day, so that page was not used. The bundle image in this repo is the source for those three kit names.
- Demo video file contents. The site says the control-surface sample files are invented.
- Secrets, key names and any `/set-key` command.
- Token totals, dollar savings and latency figures. The sources do not give them.
- The one-time price shown on the public listing. It is not a feature of the work.

## Limits copied from the sources

Scripts need Python 3 and no other packages. Pickup commit checks and the rotation history audit also need a local git binary. `/set-key` is built for macOS Terminal.app on the machine that holds the secret. `/layover` writes only its report. The README says a cloud agent stays single-repo and that `/layover` does not start one. The listing says sixty validation cases stay out of the sold package. That sixty is the size of a held-out set, not a score from a class run.
