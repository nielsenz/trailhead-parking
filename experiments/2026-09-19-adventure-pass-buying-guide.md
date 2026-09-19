# Adventure Pass buying guide — September 19, 2026

Status: deployed and verified on September 19, 2026.

## Bet and scope

People already find `/adventure-pass/` through purchase-intent searches. Named sellers by approach route, accurate physical/digital distinctions, direct purchase links and seven contextual inbound links should make the existing page more useful and improve discovery for those searches.

Change the existing guide title, description, opening answer, seller sections and matching FAQs. Retain the canonical URL. Add section IDs through the shared detail template. Retarget existing related links on Heart Rock, Heaps Peak, Cougar Crest, Pine Knot, Humber Park, East Fork and Icehouse Canyon. Do not change those trailheads’ factual copy or the newer batch 6/7/8 cohort pages.

Primary-source research and caveats: `../docs/adventure-pass-buying-sources-2026-09-19.md`.

## Baseline

Google Search Console, August 18–September 16, 2026 inclusive (30 days), pulled September 19 before deployment. Canonical non-www Adventure Pass page: **69 clicks / 3,909 impressions / 1.765% CTR / average position 7.84**. The www URL separately has 0 clicks / 3 impressions; exclude it from this baseline denominator.

Visible query/page rows restricted to the canonical page and case-insensitive query substrings `buy`, `rei`, `big 5`, `big5`, `purchase`, `near me`, `online`: **35 rows / 5 clicks / 324 impressions**. This is a reproducible visible-query subset, not all purchase demand; GSC withholds some query text.

| Query | Clicks | Impressions | Average position |
|---|---:|---:|---:|
| where to buy adventure pass | 3 | 50 | 8.96 |
| rei adventure pass | 0 | 41 | 9.83 |
| big 5 adventure pass | 0 | 38 | 9.24 |
| does big 5 sell adventure passes | 0 | 30 | 6.27 |
| adventure pass big 5 | 0 | 24 | 9.83 |
| adventure pass big bear where to buy | 0 | 24 | 7.71 |

## Read plan

First 28 complete post-deploy days, assuming September 19 deployment: September 20–October 17. Read October 20 to allow GSC lag, against August 22–September 18 (28 days; repull that baseline then rather than comparing to the 30-day context above).

Primary metric: clicks from the same visible purchase-query filter; report impressions, CTR and impression-weighted position alongside clicks. Secondary: total canonical-page clicks and Tinylytics pageviews. Inspect the existing generic Adventure Pass query group for losses. A positive result is increased purchase-query clicks accompanied by stable or improved query visibility, without a material decline in generic-query performance; small counts remain inconclusive.

This is an observational before/after comparison. Seasonality, query mix and concurrent site changes prevent attributing all movement to this treatment. Outbound purchase conversions are not measured. No automated follow-up was scheduled.

## Release verification

- Clean release assembled from committed site/sitekit sources plus the scoped data/template changes; unrelated local edits excluded.
- `uv run build.py`: 83 indexable pages plus 404. All 79 Stay22 links retain the expected account. Amazon/Viator remain unconfigured with no rendered links, as before.
- Rendered audit: zero errors; existing 404 canonical warning only. All 33 local fragment links resolve; no duplicate IDs. Canonicals, JSON-LD and Tinylytics checked across 84 HTML files.
- Desktop and 390px mobile inspection: no horizontal overflow; jump links land on section headings. Seven trailhead records changed related links only.
- Sitekit template commit: `da2a5ee` (optional section IDs; no template fork).
- Netlify production deploy: `6aaf02c2367fc018789b4f39`.
- Deploy URL: https://6aaf02c2367fc018789b4f39--trailheadparking.netlify.app
- Production verification at `2026-09-19T21:47:16.479776+00:00`: all eight affected URLs returned HTTP 200 and matched the clean release byte-for-byte.
- Raw pre-deploy GSC context retained privately under `analytics-queries/out/adventure-pass-2026-09-19/`; do not publish those raw exports in the static site.

