# trailheadparking.com

Verified parking intel for hiking trailheads — lot sizes, fill times, pass
rules, enforcement reality, and the realistic plan B. Sister site to
[bigbearmap.com](https://bigbearmap.com) and
[lakearrowheadmap.com](https://lakearrowheadmap.com), but unlike them it's a
**horizontal** play: organized around the question ("where do I park?"), not a
destination, so it can grow across ranges.

**Coverage (July 2026):** four Southern California regions, 20 trailheads,
24 pages.

- **San Bernardino Mountains (11)** — Lake Arrowhead/Crestline/Running Springs
  (6), Big Bear (Castle Rock, Cougar Crest, Discovery Center, Pine Knot),
  Forest Falls (Vivian Creek/San Gorgonio).
- **San Gabriel Mountains (4)** — East Fork/Bridge to Nowhere, Chantry Flat,
  Switzer Falls, Icehouse Canyon.
- **San Jacinto Mountains (1)** — Humber Park/Devil's Slide.
- **San Diego County (4)** — Cedar Creek Falls, Three Sisters Falls, Potato
  Chip Rock/Mt. Woodson, Torrey Pines.

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

Because coverage is no longer one forest, pass rules can't be assumed: the
Adventure Pass covers the Angeles, Cleveland, Los Padres and San Bernardino
national forests, and nothing else. San Diego's lots are state (Torrey Pines)
and city (Lake Poway) — the /adventure-pass/ page now says so explicitly, and
so does each affected trailhead page.

## Roadmap (researched July 2026)

Build in regional batches — one ranger district at a time reuses the same
pass system, sources, and phone calls:

1. ~~**Batch 1 — rest of SBNF:**~~ ✅ Built 2026-07-18 — Humber Park/Devil's
   Slide (Idyllwild) and Vivian Creek/Falls Picnic Area (Forest Falls), both
   deep-researched against live USFS/SGWA sources. Open items: no official
   space counts exist for either lot (pages deliberately don't state one);
   Ernie Maxwell permit status has one contradictory USFS webpage (brochure
   says no permit — confirm at (909) 382-2921 if challenged).
2. ~~**Batch 2 — Angeles NF / San Gabriels:**~~ ✅ Built 2026-07-20 — East
   Fork, Chantry Flat, Switzer Falls, Icehouse Canyon.
3. ~~**Batch 3 — San Diego:**~~ ✅ Built 2026-07-20 — Cedar Creek Falls, Three
   Sisters Falls, Potato Chip Rock, Torrey Pines.
4. **Next — Eastern San Gabriels / Angeles Crest depth** (Mt. Baldy Village,
   Sturtevant, Mt. Wilson via Sierra Madre once the upper trail reopens), then
   **Santa Monicas / Malibu** (Sandstone Peak, Escondido Falls — county and
   state lots, a different fee world again).

### Open items from batches 2 & 3 — re-check before trusting

These were flagged during research and are deliberately hedged in the copy
rather than stated flatly. Fix the page when one resolves.

- **Cedar Creek Falls is closed.** Forest Order #02-26-14 (San Diego River
  Gorge / Cedar Creek Falls), effective July 14 2026, still posted with **no
  end date** as of the July 20 check — verified directly against the Cleveland
  NF alerts page. The page leads with the closure. **Re-check first**; this is
  the most perishable fact on the site.
- **Chantry Flat road status is volatile** — open as of July 2026 (verified
  against the USFS page), but the road is managed by three entities and USFS
  says it "may be closed to vehicles for safety reasons at any time." The page
  tells readers to call (818) 899-1900 the morning of.
- **East Fork wilderness permit contradiction** — the USFS trail page says
  required, the USFS parking page says "encouraged but strictly voluntary."
  Both live. Page presents both and says self-register anyway. Settle at
  (626) 335-1251.
- **Cucamonga Wilderness permit routing** — SBNF page routes via SGWA online,
  secondary sources say Lytle Creek Ranger Station. Page presents both.
- **Switzer gate hours conflict** — USFS says day use 6am–10pm, tchester.org
  says the lower spur gate closes 6pm. Page notes both.
- **Three Sisters' 80-vehicle capacity** comes from the National Forest
  Foundation project description (design capacity), not a post-build USFS
  count — attributed inline. Its coordinates predate the trailhead rebuild and
  could be off slightly; worth a satellite check.
- **Torrey Pines South Beach fee** — two official CA State Parks pages
  disagree ($12–$20 vs. $12–$25). Page covers both with "up to $25 at peak."
- **No official capacity exists for any of the four San Gabriel lots**, so
  none of those pages states a number.
- **Watch list:** Eaton Canyon and Echo Mountain — closed through Dec 31, 2027
  (Eaton Fire Area Closure 05-01-26-04, which also covers Mt. Wilson Toll
  Road, Idlehour, Castle Canyon, Sam Merrill and Mt. Lowe). Build pages when
  reopening is announced, ahead of the demand spike.
- **Hold on national expansion** — the big national parking-pain spots (Zion,
  Maroon Bells, Haena) already have official reservation/shuttle systems;
  regional depth beats national thin coverage.

## Analytics

Tinylytics (embed in `templates/base.html`). Register the domain in Google
Search Console **and Bing Webmaster Tools** (AI assistants lean on Bing's
index, and FAQ-schema pages are what they cite).
