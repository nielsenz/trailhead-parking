# trailheadparking.com

Verified parking intel for hiking trailheads — lot sizes, fill times, pass
rules, enforcement reality, and the realistic plan B. Sister site to
[bigbearmap.com](https://bigbearmap.com) and
[lakearrowheadmap.com](https://lakearrowheadmap.com), but unlike them it's a
**horizontal** play: organized around the question ("where do I park?"), not a
destination, so it can grow across ranges.

**Coverage (July 2026):** five regions, 25 trailheads, 29 pages.

- **San Bernardino Mountains (11)** — Lake Arrowhead/Crestline/Running Springs
  (6), Big Bear (Castle Rock, Cougar Crest, Discovery Center, Pine Knot),
  Forest Falls (Vivian Creek/San Gorgonio).
- **San Gabriel Mountains (4)** — East Fork/Bridge to Nowhere, Chantry Flat,
  Switzer Falls, Icehouse Canyon.
- **San Jacinto Mountains (1)** — Humber Park/Devil's Slide.
- **San Diego County (4)** — Cedar Creek Falls, Three Sisters Falls, Potato
  Chip Rock/Mt. Woodson, Torrey Pines.
- **Zion National Park, Utah (5)** — Zion Visitor Center (the master parking
  page), Angels Landing, Temple of Sinawava/The Narrows, Canyon Overlook,
  Kolob Canyons.

Plus the Adventure Pass explainer and About.

## Parking content ownership (network policy)

**This site owns the deep trailhead-parking answer for the whole network.** The
geo sites (bigbearmap, lakearrowheadmap) keep destination parking (village
lots, ski resorts, beaches) and short parking summaries on trail pages, and
link here for the full trailhead-parking treatment. This prevents two of our
own domains from competing on the same "X trailhead parking" SERP.

- Big Bear trailhead lots (Castle Rock, Cougar Crest, Discovery Center, Pine
  Knot) were ported from `big-bear-maps/data/parking.json` in July 2026.
  bigbearmap keeps its village/resort/beach parking pages.
- lakearrowheadmap's Heart Rock parking page already defers here; its other
  parking pages (Village, Snow Valley, Lake Gregory) are destination parking
  and stay put.

## Architecture

Same pure-static pattern as lake-arrowhead (no Flask — that's a Big Bear
lesson, not a pattern):

```
JSON data  →  build.py (Jinja2)  →  dist/  →  Netlify
```

- `data/trailheads.json` — GeoJSON FeatureCollection, one feature per
  trailhead. Rich schema: `quick_answer`, `badges`, fact-table fields (`fee`,
  `lot_size`, `fill_time`, `overflow`, `tow_risk`, …), `sections`, `faq`
  (renders on-page FAQ + `FAQPage` JSON-LD — the AI-referral play), `related`,
  and a `verified` date stamped when facts were last checked.
- `data/pages.json` — standalone pages (Adventure Pass explainer, About).
- `templates/` — base/index/hub/detail/filter + `_macros.html` (Leaflet map,
  badges, JSON-LD emission).
- `build.py` writes directory-style URLs, `sitemap.xml`, `robots.txt`,
  `_redirects` (www → non-www 301), and `404.html`.

## Build & deploy

```bash
uv run --with 'jinja2>=3.1' build.py          # renders into dist/
python3 -m http.server -d dist 8000            # local preview
netlify deploy --prod --dir=dist               # ship it
```

## Editorial rules

- Every fact checked against an official source (USFS, county, operator) and
  date-stamped via `verified`. Perishable facts get re-checked on a recurring
  pass; when wrong, fix the page, don't defend it.
- No pay-for-placement, ever (promised on /about/). Affiliate links (lodging,
  gear) are allowed — they're links, not placement — kept disclosed and
  editorially independent.
- Every detail page answers above the fold: how many cars, when it fills, what
  pass, what enforcement looks like, what the real plan B is. No filler.

## Regions

Every trailhead feature carries a `region` string. `build.py` groups the hub's
cards under region headings in `REGION_ORDER` (with a jump nav above them);
anything with an unknown or missing region falls into a trailing "Elsewhere"
group so the mistake is visible on the page rather than silent. Adding a region
= add the string to the features and to `REGION_ORDER`.

Because coverage is no longer one forest — or one state — pass rules can't be
assumed: the Adventure Pass covers the Angeles, Cleveland, Los Padres and San
Bernardino national forests, and nothing else. San Diego's lots are state
(Torrey Pines) and city (Lake Poway); Zion is NPS, with a $35 vehicle entrance
fee. The /adventure-pass/ page says so explicitly, and so does each affected
trailhead page — our readers arrive from the forest pages and will assume the
pass travels with them.

## Roadmap (researched July 2026)

Build in regional batches — one ranger district at a time reuses the same
pass system, sources, and phone calls:

1. ~~**Batch 1 — rest of SBNF:**~~ ✅ Built 2026-07-18 — Humber Park/Devil's
   Slide (Idyllwild) and Vivian Creek/Falls Picnic Area (Forest Falls), both
   deep-researched against live USFS/SGWA sources. No official space counts
   exist for either lot, so the pages deliberately don't state one.
2. ~~**Batch 2 — Angeles NF / San Gabriels:**~~ ✅ Built 2026-07-20 — East
   Fork, Chantry Flat, Switzer Falls, Icehouse Canyon.
3. ~~**Batch 3 — San Diego:**~~ ✅ Built 2026-07-20 — Cedar Creek Falls, Three
   Sisters Falls, Potato Chip Rock, Torrey Pines.
4. ~~**Batch 4 — Zion National Park:**~~ ✅ Built 2026-07-21 — Visitor Center,
   Angels Landing, Temple of Sinawava, Canyon Overlook, Kolob Canyons. First
   non-California region, and the first batch where the agency published
   enough to state hard numbers on every page.
5. **Next — the rest of the NPS shuttle/permit belt**, on the same logic:
   Bryce, Arches (timed entry), Rocky Mountain NP (timed entry), Haena/Kalalau.
   All publish their rules in detail. Then **Eastern San Gabriels / Angeles
   Crest depth** (Mt. Baldy Village, Sturtevant, Mt. Wilson via Sierra Madre
   once the upper trail reopens) and **Santa Monicas / Malibu** (Sandstone
   Peak, Escondido Falls).

**Reversed 2026-07-21: national parks are in scope where the data is.** The
earlier call was to hold, on the reasoning that the big parking-pain spots
(Zion, Maroon Bells, Haena) "already have official reservation/shuttle
systems." That reasoning was backwards. A shuttle system doesn't answer the
parking question, it *is* the parking question — "where do I park for Angels
Landing?" has a genuinely non-obvious answer, and it's the same permit-is-not-
a-parking-pass pattern that Cedar Creek Falls already handles well.

The practical argument is stronger still: batches 2 and 3 kept running into
sources that publish nothing. Seven of those eight pages couldn't state a lot
capacity because no official count exists. NPS publishes capacities, shuttle
schedules, permit mechanics and seasonal driving rules — the Zion batch landed
concrete, sourced numbers on every page. **Prefer regions by whether the agency
publishes real data, not by distance from the San Bernardinos.**

Still holding on: thin coverage of anywhere we can't source properly.

### Open items

Unresolved facts, contradictions between official sources, and perishable
claims are tracked in **[docs/todos.md](docs/todos.md)**, dated as logged.
Check that file before trusting a page's more specific claims — especially
**Cedar Creek Falls**, which is closed under an open-ended heat order, and
**Chantry Flat**, whose road can shut on any given day.

Batch 1's carried-over item (Ernie Maxwell permit status) lives there too.

## Analytics

Tinylytics (embed in `templates/base.html`). Register the domain in Google
Search Console **and Bing Webmaster Tools** (AI assistants lean on Bing's
index, and FAQ-schema pages are what they cite).
