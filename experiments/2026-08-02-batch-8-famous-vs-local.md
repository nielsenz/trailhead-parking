# Batch 8 — Famous vs local trailheads

**Built** 2026-08-02 · **15 pages** · locally built from `main` at `39bc356`;
not deployed yet.

This batch creates two deliberately labeled cohorts in
`data/trailheads.json`. The `experiment_cohort` field is metadata for analysis;
it does not change the page template or URL.

## Cohorts

### Famous — 7 pages

- `/trailheads/mount-whitney-portal/`
- `/trailheads/yosemite-valley/`
- `/trailheads/glacier-point/`
- `/trailheads/bright-angel/`
- `/trailheads/south-kaibab/`
- `/trailheads/cadillac-mountain/`
- `/trailheads/kalalau-trailhead/`

### Less famous — 8 pages

- `/trailheads/sandstone-peak/`
- `/trailheads/solstice-canyon/`
- `/trailheads/circle-x-ranch/`
- `/trailheads/temescal-gateway/`
- `/trailheads/zuma-canyon/`
- `/trailheads/rocky-oaks/`
- `/trailheads/rancho-sierra-vista/`
- `/trailheads/paramount-ranch/`

## The bet

Famous names should have a larger pool of potential searches, but recognition
alone may not make someone click a parking page. The smaller Santa Monica
Mountains cluster has less name recognition and more specific local decisions:
which lot fills first, whether roadside parking is legal, whether a gate is
open, and where overflow is allowed.

The useful comparison is not total traffic — the cohorts have different page
counts — but the median page performance and the query mix each cohort earns.

## Measurement plan

After deployment, use the analytics queries work in
`/Users/znielsen/projects/sites/analytics-queries`:

1. In GSC, compare each cohort at 30 and 90 days for impressions, clicks, CTR,
   and average position. Group by landing-page path, then compare medians.
2. Bucket queries into `parking`, `trailhead`, `permit`, `reservation`,
   `shuttle`, `hours`, and `closed`. This shows whether recognition creates
   discovery or whether the parking question creates the click.
3. In Tinylytics, compare grouped path hits, unique page views, and entry-page
   behavior. Keep the famous and less-famous paths separate from the start.

The current environment has no GSC service-account credential or Tinylytics
API key, so this file records the test before results exist rather than claiming
a baseline.

## What would make it look right

- Famous pages earn more impressions and broader trail-name queries, while the
  local pages earn a comparable or better share of parking-specific clicks.
- At least one less-famous cluster page earns query demand beyond its trail
  name, especially for lot availability, hours, overflow, or access rules.
- The result holds on both GSC clicks and Tinylytics page views; one source by
  itself is not enough.

**Falsifier:** if the famous cohort gets impressions but neither cohort earns
parking-intent clicks, the new pages are not answering a discovery problem yet.
If only one local page gets traffic, the cluster is too broad and the next
batch should follow the query evidence rather than add more nearby pages.

### Check-backs

- **30 days after deployment** — indexing, impressions, and first query buckets.
- **90 days after deployment** — clicks, CTR, page-view comparison, and cohort
  verdict.
