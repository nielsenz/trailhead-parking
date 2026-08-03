# trailheadparking.com

Verified parking intel for hiking trailheads — lot sizes, fill times, pass
rules, enforcement reality, and the realistic plan B. Sister site to
[bigbearmap.com](https://bigbearmap.com) and
[lakearrowheadmap.com](https://lakearrowheadmap.com), but unlike them it's a
**horizontal** play: organized around the question ("where do I park?"), not a
destination, so it can grow across ranges.

**Coverage (August 2026):** fifteen regions, 79 trailheads, 83 pages.

- **San Bernardino Mountains (15)** — Lake Arrowhead/Crestline/Running Springs,
  Big Bear, Forest Falls, Grays Peak, and San Bernardino Peak.
- **San Gabriel Mountains (10)** — East Fork/Bridge to Nowhere, Chantry Flat,
  Switzer Falls, Icehouse Canyon, and Devil's Punchbowl.
- **San Jacinto Mountains (4)** — Humber Park/Devil's Slide and Idyllwild-area
  trailheads.
- **San Diego County (7)** — Cedar Creek Falls, Three Sisters Falls, Potato
  Chip Rock/Mt. Woodson, Torrey Pines, and other county trailheads.
- **Zion National Park (5)** — Visitor Center (master parking page), Angels
  Landing, Temple of Sinawava/The Narrows, Canyon Overlook, Kolob Canyons.
- **Bryce Canyon National Park (5)** — Visitor Center (master), Sunset Point,
  Bryce Point, Fairyland Point, Mossy Cave.
- **Arches National Park (5)** — timed entry (master), Delicate Arch/Wolfe
  Ranch, Devils Garden, The Windows, Fiery Furnace.
- **Rocky Mountain National Park (5)** — timed entry (master), Bear Lake,
  Glacier Gorge, Alpine Visitor Center/Trail Ridge Road, Longs Peak.
- **Glacier National Park (5)** — entry & Going-to-the-Sun Road (master), Logan
  Pass, Avalanche Creek/Trail of the Cedars, Many Glacier, St. Mary Falls.
- **Mount Whitney (1)** — Whitney Portal.
- **Yosemite National Park (5)** — entry & reservations (master), Valley
  day-use parking, Glacier Point, Cathedral Lakes, Mist Trail/Happy Isles.
- **Grand Canyon National Park (2)** — Bright Angel and South Kaibab.
- **Acadia National Park (1)** — Cadillac Mountain.
- **Kauai — Haena & Napali Coast (1)** — Kalalau Trailhead.
- **Santa Monica Mountains (8)** — Sandstone Peak/Mishe Mokwa, Solstice Canyon,
  Circle X Ranch, Temescal Gateway, Zuma Canyon, Rocky Oaks, Rancho Sierra
  Vista/Satwiwa, and Paramount Ranch.

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

Pure static, with shared build machinery in the sibling `sitekit` package:

```
JSON data  →  build.py config  →  sitekit + Jinja2  →  dist/  →  Netlify
```

- `data/trailheads.json` — GeoJSON FeatureCollection, one feature per
  trailhead. Rich schema: `quick_answer`, `badges`, fact-table fields (`fee`,
  `lot_size`, `fill_time`, `overflow`, `tow_risk`, …), `sections`, `faq`
  (renders on-page FAQ + `FAQPage` JSON-LD — the AI-referral play), `related`,
  and a `verified` date stamped when facts were last checked.
- `data/pages.json` — standalone pages (Adventure Pass explainer, About).
- `templates/` — site-specific base, home and 404 templates. Hub, detail,
  filter and macro templates are inherited from `../sitekit`.
- `build.py` is site configuration only. `sitekit` writes directory-style
  URLs, `sitemap.xml`, `robots.txt`, `_redirects` and `404.html`.

## Build & deploy

```bash
uv run python build.py                        # renders into dist/
python3 -m http.server -d dist 8000            # local preview
netlify deploy --prod --dir=dist               # ship it
```

Disclosed Stay22 lodging links render on trailhead detail pages only. They use
campaign `trailheadparking_stays`; Stay22 Hub provides click and booking totals
without a custom browser event collector.

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
(Torrey Pines) and city (Lake Poway); the Utah parks are NPS, with per-park
entrance fees ($35 Zion and Bryce, $30 Arches). The /adventure-pass/ page says
so explicitly, and so does each affected trailhead page — our readers arrive
from the forest pages and will assume the pass travels with them.

One checkable contrast worth keeping accurate: the **$100 non-US-resident
surcharge** (effective Jan 1 2026) applies at Zion, Bryce, Rocky Mountain,
Glacier and Yosemite — but **not** at Arches, which isn't on the 11-park list.
It is waived by an annual or America the Beautiful pass, which is unusual for a
surcharge and is quoted verbatim from each park's fees page rather than
paraphrased.

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
5. ~~**Batch 5 — Bryce Canyon + Arches:**~~ ✅ Built 2026-07-21. Vindicated the
   data-availability rule: NPS publishes per-lot capacities for both parks, so
   9 of 10 pages state hard numbers. Two findings inverted their briefs —
   **Arches requires no timed-entry reservation in 2026** (NPS news release,
   Feb 18 2026), and **Bryce's Visitor Center lot is posted 1-hour**, with
   all-day parkers sent to the Shuttle Station lot in Bryce Canyon City.
6. ~~**Batch 6 — Rocky Mountain, Glacier, Yosemite:**~~ ✅ Built 2026-07-28.
   Three findings inverted their briefs, and two of them the same way:
   **Glacier requires no vehicle reservation in 2026** (first season since
   2020) and **Yosemite requires none either** (announced Feb 18, 2026). Only
   RMNP still gates entry — and it does it with *two* different permits people
   routinely confuse. Also corrected mid-build: a research claim that RMNP's
   Park & Ride lets you skip the corridor permit is wrong; NPS says the Bear
   Lake Road permit covers "all destinations on Bear Lake Road," and the
   Park & Ride is 5.2 miles up it.
7. ~~**Batch 7 — Southern California depth:**~~ ✅ Built through 2026-08-02 —
   sixteen additional trailheads across the San Bernardinos, San Gabriels,
   San Jacintos and San Diego County, finishing with Grays Peak, San Bernardino
   Peak and Devil's Punchbowl.
8. **Batch 8 — Famous vs local:** Built locally 2026-08-02, not yet deployed —
   seven famous-park pages and eight Santa Monica Mountains pages tagged with
   `experiment_cohort` so GSC and Tinylytics can compare discovery demand with
   parking-specific local demand after deployment.

### A note on the six park systems, because readers conflate them

Six genuinely different regimes, and the pages say so explicitly:

- **Zion** — shuttle is *mandatory* in season; you cannot drive the Scenic
  Drive Mar 7 – Nov 28.
- **Bryce** — shuttle is *free and optional*; you can drive to every viewpoint.
  NPS: "In no area of the park is riding the shuttle mandatory."
- **Arches** — no shuttle at all, and **no timed entry in 2026**. Parking is
  the only gate.
- **Rocky Mountain** — **two** timed entry permits with different hours and
  different end dates. Bear Lake Road is gated 5am–6pm; the rest of the park
  9am–2pm. Buying the wrong one is the batch's signature mistake.
- **Glacier** — **no vehicle reservation in 2026**, replaced by a *paid* $1
  ticketed Logan Pass shuttle and a **3-hour parking limit at Logan Pass**
  enforced 24/7, Jul 1 – Sep 7. The old free hop-on GTSR shuttle is gone, and
  its replacement's six-stop route no longer serves Avalanche Creek, St. Mary
  Falls or Many Glacier — a service cut that was never announced as one.
- **Yosemite** — **no reservation in 2026**, and nothing ticketed replaced it.
  The gate is entirely the Valley floor, which NPS says fills by 8am.

Readers arriving from the Zion pages assume the Zion rules travel. They don't.
The 2026 lesson across the newer parks is that a reservation system's absence
is now as newsworthy as its presence — three of the six have dropped theirs,
and every one of those decisions is re-made annually.

### Open items

Unresolved facts, contradictions between official sources, and perishable
claims are tracked in **[docs/todos.md](docs/todos.md)**, dated as logged.
Check that file before trusting a page's more specific claims — especially the
recurring heat closures at **Cedar Creek Falls** and **Chantry Flat**, whose
road can shut on any given day.

Batch 1's carried-over item (Ernie Maxwell permit status) lives there too.

### Why a batch was built

`docs/todos.md` tracks facts that might be wrong. **[experiments/](experiments/)**
tracks bets that might be misjudged — region choice, cluster shape, page mix —
written down before the traffic data exists, with the check-back dates that
would settle them. Starts with batch 6.

## Analytics

Tinylytics (embed in `templates/base.html`). Register the domain in Google
Search Console **and Bing Webmaster Tools** (AI assistants lean on Bing's
index, and FAQ-schema pages are what they cite).
