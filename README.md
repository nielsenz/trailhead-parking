# TrailheadParking.com

A guide to practical trailhead access: parking, passes, reservations, official
restrictions and documented alternatives. Coverage spans Southern California
and several national-park regions. The current inventory lives in
`data/trailheads.json`; region ordering lives in `build.py`.

This site owns detailed per-trailhead parking answers for the whole network.
Destination sites retain village/resort/beach parking and short trail summaries
that link here. Preserve the distinction when expanding either site.

## Build and release

Sitekit renders GeoJSON and this site's configuration to static HTML. Python
3.12+, `uv` and the sibling `../sitekit/` checkout are required.

```sh
uv sync
uv run build.py
uv run --project ../sitekit sitekit-audit dist \
  --base-url https://trailheadparking.com --require-tinylytics --require-robots
uv run python -m http.server -d dist 8000
```

Read build warnings and inspect changed pages before deploying committed,
reviewed sources with `netlify deploy --prod --dir=dist` from this linked repo.
The build generates directory-style canonicals, sitemap, robots and redirects.
Never edit `dist/` directly.

## Content structure

- `data/trailheads.json`: GeoJSON features with stable slugs, region, quick
  answers, badges, fact fields, sections, FAQ, related links and verification date.
- `data/pages.json`: explicit standalone paths, including Adventure Pass and About.
- `build.py`: section configuration and `REGION_ORDER`.
- `templates/`: local base/home/404 templates; hubs, details and macros inherit Sitekit.
- `static/planning-events.js`: selected official-source/directions click tracking.

A new region needs the exact region string on its features and in `REGION_ORDER`.
Missing regions fall into “Elsewhere”; unlisted region names sort after configured
ones. Inspect the built hub so grouping errors are visible before release.

## Editorial contract

Every practical claim needs its responsible agency/operator source and actual
verification date. Answer capacity, fill time, overflow and enforcement only when
supported; uncertainty is better than a plausible number. Correct wrong claims
and document the intervention rather than defending an old page.

Do not assume a parking pass covers entry reservations, wilderness permits or
other agencies. National-park access systems and shuttle policies vary by place
and year. The old README's detailed 2026 fees and seasonal rules are now historical
[expansion notes](docs/archive/2026-07-expansion-notes.md); current claims belong in
source-checked data, not duplicate prose in an operating guide.

[docs/todos.md](docs/todos.md) preserves unresolved source contradictions,
unpublished numbers and dated research. Check the relevant entry before replacing
an unknown value. Dates in that file identify the evidence's age, not a current
access determination. There is no paid placement; preserve editorial independence
and existing affiliate disclosures.

## Shipped work and protected reads

The [September 19 Adventure Pass guide](experiments/2026-09-19-adventure-pass-buying-guide.md)
adds officially listed sellers and buying guidance to the existing URL. Seller
records do not establish live stock or hours. Seven trailhead pages link to heading
IDs in the guide; keep those IDs stable. Its first outcome read is October 20,
using the exact windows and purchase-query definition in the experiment.

The [September 30 release](experiments/2026-09-30-autumn-access-refresh.md)
updates Chantry Flats, Icehouse Canyon and East Fork, with official-source and
directions events. The Adventure Pass treatment was retained; changed supporting
pages are a confound to record. The three-page read is October 31.

Earlier famous/local and regional batches retain their own cohorts and gates.
Use [experiments/README.md](experiments/README.md) and the
[shared queue](../../analytics-queries/travel_ops/README.md) before further edits.
The queue's older-batch hold is initially conservative; narrow it only after
reconstructing the original URL cohorts. A passing review date never ends a hold.

## Maintenance and measurement

Tinylytics is embedded in the local base template; GSC is available through
`../../analytics-queries/`. Save raw exports privately and put necessary aggregate
findings in experiment records. Query rows omit private searches, and a visitor
leaving after getting an answer can be a successful visit.

The selected `directions.click` and `planning.official` events start with their
recorded deployment. Transport checks are not proof of dashboard ingestion,
physical visits or outcomes. No counts should be backfilled.

[FRESHNESS.md](FRESHNESS.md) is used by the weekly GitHub issue workflow. It does
not fetch sources or deploy. The local monitor can be run daily and its search
queue refreshed weekly; it has no installed background schedule. Existing Stay22
links remain on detail pages, but earnings work is excluded from the queue.
