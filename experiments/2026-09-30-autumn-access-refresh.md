# Autumn access refresh — September 30, 2026

The user authorized refreshing Chantry Flat, Icehouse Canyon and East Fork,
tracking useful exits and deploying after validation. Existing URLs retained.
The Adventure Pass guide and its title/intro remain unchanged; the October 20
buying-guide experiment read remains in place. Its inbound cohort overlaps
Icehouse and East Fork, so annotate this supporting-page change in that read.

## Changes and sources

- Chantry: separate picnic-area status from road status; published 6am–8pm
  day-use schedule and exit deadline. Removed unsupported guaranteed fill-time,
  white-line parking legality and private-overflow-price claims. Its title now
  emphasizes gate hours, passes and road access. Source:
  https://www.fs.usda.gov/r05/angeles/recreation/chantry-flat-picnic-area
- Icehouse: retain the separate parking/wilderness distinction, clarify each
  forest's permit source and put the agency's winter mountaineering warning
  above the guide. Do not infer safe conditions from an open road or trail.
  https://www.fs.usda.gov/r05/angeles/recreation/icehouse-canyon-saddle-icehouse-canyon
  https://www.fs.usda.gov/r05/sanbernardino/recreation/cucamonga-wilderness
  The latter directs permit requests to https://www.sgwa.org/permits.
- East Fork: 24-hour parking is not a recommendation to cross water in darkness;
  agency cautions against crossings in rainy conditions. Existing official
  disagreement remains: trail page calls wilderness permits required, parking
  page calls them voluntary. Keep that visible rather than choosing a rule.
  https://www.fs.usda.gov/r05/angeles/recreation/east-fork-day-use-parking-trailhead
  https://www.fs.usda.gov/r05/angeles/recreation/trails/east-fork-trail
- Alerts checked: https://www.fs.usda.gov/r05/angeles/alerts.

Access notes record September 30 separately from unchanged underlying facts.
Chantry's rewritten guide carries the new verified date. Official text is a
source check, not live road monitoring; readers must check on their travel date.

## Measurement

Final GSC September 15–28 versus September 1–14:
Chantry 24 vs 12 clicks; Icehouse 18 vs 15; East Fork 12 vs 6. This momentum
predates the release and cannot be credited to it.

Track `directions.click` (value: slug) and `planning.official` (value:
slug + official URL path) only on these three pages. Enable Tinylytics events
and beacon mode. No historical event counts or conversion claims.

Read first 28 full days October 1–28 against September 2–29 on October 31,
using final GSC. Report page-level clicks, impressions, CTR and position; small
samples remain inconclusive. Review official access sources before winter
weather or when an agency changes an order. No automation scheduled.

## Validation

84 HTML pages and 242 JSON-LD blocks pass links/canonical/schema checks;
79/79 Stay22 links retain their account. Adventure Pass main content matches
baseline exactly. Browser checks at 390px and 1440px cover all three guides.
Directions and official-source clicks each emit one expected Tinylytics request
using the actual embed with collector calls intercepted locally. No claim of
analytics dashboard ingestion or bookings. Clean committed sources used for
release; unrelated working-tree notes excluded.

### Published result

- Site content: `5bc2947`; shared Sitekit: `d625203`.
- Production deploy: `6abd86f045a0d5aab4245b4b`, September 30, 2026.
- All three guides, Adventure Pass and the new tracking asset returned 200 and
  matched the clean build byte-for-byte. Only the three detail pages and their
  directory cards have changed main content; Adventure Pass remains unchanged.
- Both site releases passed 14 responsive page checks and eight click-transport
  checks in total. No runtime JavaScript errors in the tested pages.
