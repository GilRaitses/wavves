# Public asset checklist (wavves)

Companion to `docs/public-asset-brief.yaml` (nano-banana packet).

## Surfaces

| Surface | URL / path | Needs |
|---|---|---|
| Cursor marketplace | plugin listing | clean `assets/wavves-logo.svg` + 1024 PNG tile |
| GitHub Pages site | https://wavves.aimez.ai/ (`index.html`) | favicon pack, apple-touch, OG 1200×630 |
| GitHub repo social | GilRaitses/wavves | same OG image |
| Plugin install | `.cursor-plugin/plugin.json` → `logo` | SVG path (already wired; file bloated) |
| README / crosslinks | README, aimez mentions | horizontal lockup + wordmark |

## Already on disk

| file | status |
|---|---|
| `assets/wavves-logo.svg` | exists, ~1MB — remake as true vector |
| `assets/wavves-logo.png` | exists, 1200×1200 |
| `index.html` | **no** `<img>`, favicon, or `og:image` wired yet |

## P0 generate

1. Clean SVG logo (`<200KB`)
2. Marketplace PNG 1024 / 512 / 256
3. Favicon pack (ico + 16/32 + 192/512)
4. OG card 1200×630

## P1

5. Apple touch 180
6. Horizontal lockup SVG
7. Wordmark SVG

## P2 (optional)

8. Hero atmosphere 1600×900 (site is CSS-only today)

## After delivery

Wire tags in `index.html`, replace bloated SVG, push, remasure Pages
(single `github-pages` artifact), rsync local plugin mirror.
