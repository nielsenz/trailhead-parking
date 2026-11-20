# Adventure Pass buying guide — September 19, 2026

Status: deployed and verified on September 19, 2026.

## Bet and scope

People already find `/adventure-pass/` through purchase-intent searches. Named sellers by approach route, accurate physical/digital distinctions, direct purchase links and seven contextual inbound links should make the existing page more useful and improve discovery for those searches.

Updated the guide title, description, opening answer, seller sections and matching FAQs on the existing canonical URL. Added section IDs through the shared detail template and retargeted related links on Heart Rock, Heaps Peak, Cougar Crest, Pine Knot, Humber Park, East Fork and Icehouse Canyon. Those trailheads’ factual copy and the newer batch 6/7/8 cohort pages were unchanged.

Primary-source research and caveats: [source-check record](../docs/adventure-pass-buying-sources-2026-09-19.md), with the [nine selected vendor records](../docs/adventure-pass-vendors-2026-09-19.json).

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

First 28 complete days after the verified September 19 deployment: September 20–October 17. Read October 20 to allow GSC lag, against August 22–September 18 (28 days; repull that baseline then rather than comparing to the 30-day context above).

Primary metric: clicks from the same visible purchase-query filter; report impressions, CTR and impression-weighted position alongside clicks. Secondary: total canonical-page clicks and Tinylytics pageviews. For the generic-query guardrail, use visible queries containing `adventure pass` but none of the purchase-filter substrings, restricted to the same canonical page in both windows. Report its clicks, impressions and CTR for losses. A positive result is increased purchase-query clicks accompanied by stable or improved query visibility, without a material decline in generic-query performance; small counts remain inconclusive.

This is an observational before/after comparison. Seasonality, query mix and concurrent site changes prevent attributing all movement to this treatment. Outbound purchase conversions are not measured. No automated follow-up was scheduled.

## Results

**Recorded November 13, 2026; see the read at the end of this record.** Original plan: the release checks below establish that the change shipped;
they are not evidence of search lift. On October 20, record both windows’
purchase-query clicks, impressions, CTR and weighted position; total-page
clicks/impressions; generic-query guardrail; and Tinylytics pageviews. Record
whether data availability or low counts leave the result inconclusive, then
state whether to retain, revise or extend the experiment.

## Release verification

- Clean release assembled from committed site/sitekit sources plus the scoped data/template changes; unrelated local edits excluded.
- `uv run build.py`: 83 indexable pages plus 404. All 79 Stay22 links retain the expected account. Amazon/Viator remain unconfigured with no rendered links, as before.
- Rendered audit: zero errors; existing 404 canonical warning only. All 33 local fragment links resolve; no duplicate IDs. Canonicals, JSON-LD and Tinylytics checked across 84 HTML files.
- Desktop and 390px mobile inspection: no horizontal overflow; jump links land on section headings. Seven trailhead records changed related links only.
- Site content and research commit: `b075fc6`.
- Sitekit template commit: `da2a5ee` (optional section IDs; no template fork).
- Netlify production deploy: `6aaf02c2367fc018789b4f39`.
- Deploy URL: https://6aaf02c2367fc018789b4f39--trailheadparking.netlify.app
- Production verification at `2026-09-19T21:47:16.479776+00:00`: all eight affected URLs returned HTTP 200 and matched the clean release byte-for-byte.
- Raw pre-deploy GSC context retained privately under `analytics-queries/out/adventure-pass-2026-09-19/`; do not publish those raw exports in the static site.



## September 30 supporting-page annotation

The [autumn access refresh](2026-09-30-autumn-access-refresh.md) changed factual
access guidance on Icehouse Canyon and East Fork, which already link into this
guide; Chantry Flat was also refreshed. Adventure Pass's main content, title,
purchase-query filter and October 20 read remain unchanged. Account for the
supporting-page intervention when interpreting discovery and inbound traffic.
The new directions/source events exist only on those three trailhead pages;
they do not measure Adventure Pass purchases or seller conversions.

## October 11 intervention: where-needed page launched before the read

`/adventure-pass/where-needed/` (USFS trailheads and day-use sites by fee
listing, site commit `36b99b8`) went live October 11 at the owner's request to
accelerate Trailhead Parking, inside the September 20–October 17 window. It is
in the sitemap and was submitted to IndexNow, but it is **not linked** from
`/adventure-pass/`, and the guide's content, title and purchase-query filter are
unchanged. On October 20, check whether the new URL earned impressions for
`adventure pass` queries (possible cannibalization) and report the guardrail
with and without October 11–17. Netlify production deploy:
`6acc52726b31277464893101`; production matched the build byte-for-byte.

## Read — performed November 13, 2026 (scheduled October 20)

Final GSC web data, canonical `/adventure-pass/`, September 20–October 17 against
August 22–September 18, both re-pulled.

| Metric | Clicks / impressions / CTR / position, pre → post |
|---|---|
| Purchase-query filter | 6 / 398 / 1.5% / 8.9 → 8 / 303 / 2.6% / 8.5 |
| Generic guardrail | 15 / 514 / 2.9% / 10.8 → 17 / 571 / 3.0% / 9.2 |
| Generic guardrail, post September 20–October 10 only | → 14 / 472 / 3.0% / 8.8 |
| Page total | 84 / 4,421 / 1.9% / 7.5 → 93 / 4,160 / 2.2% / 7.3 |

`/adventure-pass/where-needed/` had 41 impressions and 1 click in the post window and
one impression on an "adventure pass" query, so there is no sign of cannibalization.

**Outcome: inconclusive, leaning positive.** Purchase clicks rose from six to eight
on fewer impressions at a slightly better position, and the generic guardrail did
not decline with or without October 11–17. Two extra clicks is too few to call.
Tinylytics pageviews were not collected for this read. **Decision:** retain the
guide and close `adventure-pass-read`. Later context, outside this read: page clicks
were 117 in September 16–October 13 and 81 in October 14–November 10.

## November 20, 2026 annotation: guide now links to the where-needed page (not deployed)

Prepared at the owner's request after the November 20 search review. With the
read above closed, the "Price, coverage and which pass you need" section gains one
sentence linking to `/adventure-pass/where-needed/`, which the guide had not
linked since that page launched October 11. Title, headings, seller sections and
the purchase-query filter are unchanged. No other page changes.

Final GSC web data, October 21–November 17: `/adventure-pass/` 88 clicks / 4,481
impressions / 2.0% / position 7.1; `/adventure-pass/where-needed/` 0 / 84 / 0.0% /
9.7. URL Inspection on November 20: where-needed is "Submitted and indexed", last
crawled October 14.

The review also looked at the purchase near-misses ("where to buy adventure
pass" 121 impressions at 8.6, "rei adventure pass" 35 at 9.7, "near me" variants).
The guide already answers each of them in a named section, so no retargeting was
made. "cleveland national forest adventure pass" (25 impressions, 8.9) has no
seller section; adding one needs the Forest Service vendor list checked first and
was left undone.

This is an internal link, not a test with a read. Expect nothing measurable on
the guide; watch whether where-needed is recrawled and gains impressions. Local
build and `sitekit-audit` passed (0 errors, the standing `/404` warning).
Production deploy, deploy ID and date: pending owner approval.

### Release — November 20, 2026

The where-needed link was deployed to production on November 20, 2026 at about
1:37 PM Pacific from commit `afef239` (Netlify deploy `6b00bd7f531a2e051b89e47e`).
Before the deploy, all 85 built pages were compared with production: only
`/adventure-pass/` differed, by the one added sentence. Build and `sitekit-audit`
passed with 0 errors and the standing `/404` canonical warning. Verified live:
`/adventure-pass/` carries the link and `/adventure-pass/where-needed/` returns 200.
This supersedes "not deployed" in the annotation heading above.
