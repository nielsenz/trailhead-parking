# trailheadparking.com

Verified parking intel for hiking trailheads — lot sizes, fill times, pass
rules, enforcement reality, and the realistic plan B. Sister site to
[bigbearmap.com](https://bigbearmap.com) and
[lakearrowheadmap.com](https://lakearrowheadmap.com), but unlike them it's a
**horizontal** play: organized around the question ("where do I park?"), not a
destination, so it can grow across ranges.

**Coverage (July 2026):** San Bernardino National Forest — Lake Arrowhead/
Crestline/Running Springs (6 trailheads), Big Bear (Castle Rock, Cougar Crest,
Discovery Center, Pine Knot), Idyllwild (Humber Park/Devil's Slide), and
Forest Falls (Vivian Creek/San Gorgonio), plus the Adventure Pass explainer.
16 pages.

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

## Roadmap (researched July 2026)

Build in regional batches — one ranger district at a time reuses the same
pass system, sources, and phone calls:

1. ~~**Batch 1 — rest of SBNF:**~~ ✅ Built 2026-07-18 — Humber Park/Devil's
   Slide (Idyllwild) and Vivian Creek/Falls Picnic Area (Forest Falls), both
   deep-researched against live USFS/SGWA sources. Open items: no official
   space counts exist for either lot (pages deliberately don't state one);
   Ernie Maxwell permit status has one contradictory USFS webpage (brochure
   says no permit — confirm at (909) 382-2921 if challenged).
2. **Batch 2 — Angeles NF / San Gabriels:** Bridge to Nowhere/East Fork,
   Chantry Flats (verify post-Eaton-fire access first), Switzer Falls,
   Icehouse Canyon/Mt. Baldy. Largest audience (LA metro).
3. **Batch 3 — San Diego:** Cedar Creek Falls (permit ≠ parking confusion is
   the content), Three Sisters Falls (confirm fire-closure status first),
   Potato Chip Rock.
- **Watch list:** Eaton Canyon and Echo Mountain — closed through Dec 31,
  2027 (Eaton Fire); build pages when reopening is announced, ahead of the
  demand spike.
- **Hold on national expansion** — the big national parking-pain spots (Zion,
  Maroon Bells, Haena) already have official reservation/shuttle systems;
  regional depth beats national thin coverage.

## Analytics

Tinylytics (embed in `templates/base.html`). Register the domain in Google
Search Console **and Bing Webmaster Tools** (AI assistants lean on Bing's
index, and FAQ-schema pages are what they cite).
