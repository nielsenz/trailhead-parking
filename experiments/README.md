# Experiments

## How to use this record

This index was reconciled October 4, 2026. Dated files preserve original
hypotheses, measurements and later interventions; read the latest review before
using an older checkpoint. A passed date does not establish completion.

The [shared work queue](../../../analytics-queries/travel_ops/README.md) tracks
selected current reviews and protected edits. Its registry is not an exhaustive
copy of this history. Keep unresolved records here and reconcile dates/holds
when a review is recorded. No local background schedule is installed; the site's
GitHub freshness issue reminder is separate. Historical affiliate records remain
for attribution context; earnings reviews are outside the current work queue.

Why a batch was built the way it was, and what would prove it right or wrong.

`docs/todos.md` tracks facts that might be *wrong*. This tracks bets that might
be *misjudged* — the region choice, the cluster shape, the page mix. A batch can
be flawless on facts and still be the wrong five pages to build.

One file per batch, named `YYYY-MM-DD-<slug>.md`, dated by deploy. Each one
states the bet before the results exist, so the record can't be quietly
rewritten once traffic comes in. **Fill in the results section from the actual
numbers, including when they're bad** — a batch that didn't work is the only way
the next region choice gets better.

## Log

| Built / deployed | Batch | Bet | Verdict |
|---|---|---|---|
| 2026-07-28 | [Batch 6 — Rocky Mountain, Glacier, Yosemite](2026-07-28-batch-6-national-parks.md) | Three marquee parks at once; absence-of-reservation as the hook | Read recorded November 20, 2026 in the [September 4 review](2026-09-04-review.md); `trailhead-batches-final` completed |
| 2026-08-02 | [Batch 7 — San Bernardino + San Gabriel](2026-08-02-batch-7-san-bernardino-san-gabriel.md) | Practical constraints — closures, permits, and small lots — can carry local trailhead search demand | Read recorded November 20, 2026 in the [September 4 review](2026-09-04-review.md); `trailhead-batches-final` completed |
| 2026-08-02 built / 2026-08-03 deployed | [Batch 8 — Famous vs local trailheads](2026-08-02-batch-8-famous-vs-local.md) | A recognizable trail name may earn discovery; a smaller local cluster may earn more parking-specific visits | Read recorded November 20, 2026 in the [September 4 review](2026-09-04-review.md); `trailhead-batches-final` completed |
| 2026-08-03 | [Stay22 lodging links](2026-08-03-stay22-affiliate-links.md) | A disclosed nearby-stays link can serve overnight trail users without changing parking recommendations | Unmeasured — awaiting campaign attribution data |
| 2026-09-19 | [Adventure Pass buying guide](2026-09-19-adventure-pass-buying-guide.md) | Verified sellers by route and clear purchase options can grow purchase-query clicks on the existing guide | ⏳ open — first outcome read October 20 |

## Next Adventure Pass read

**October 20, 2026 (manual):** compare September 20–October 17 against
August 22–September 18. Use the fixed purchase-query filter in the
[experiment](2026-09-19-adventure-pass-buying-guide.md), then check total-page
performance and generic queries for losses. The deployed update has passed
technical verification; traffic impact is still pending. Seller checks and
source records are linked from the experiment. The shared queue now records this read; it is not an installed reminder.

Batches 1–5 shipped before this log existed. Their reasoning is compressed into
the [archived July expansion notes](../docs/archive/2026-07-expansion-notes.md); it isn't worth reconstructing them
retroactively, since the point of the format is writing the bet down *first*.

## September 4 review

See [the dated review](2026-09-04-review.md) for completed checkpoints, explicit closures, measurement gaps, and protected changes. This dated review supersedes stale next-check labels above without rewriting the original hypotheses.


## September 30 autumn access release

[Chantry, Icehouse and East Fork](2026-09-30-autumn-access-refresh.md) are deployed
with dated access guidance and new official-source/directions events. The
Adventure Pass main content is unchanged. Its **October 20** read must note
that two supporting inbound pages changed September 30.

**October 31 (manual):** compare the three guides over October 1–28 against
September 2–29 using final GSC. Prior growth is baseline, not a release outcome.
The shared queue records the read; dated source research remains in
[maintenance notes](../docs/todos.md).

## October 17 Angeles closures hub

[`/angeles-closures/`](2026-10-17-angeles-closures-hub.md) lists each San Gabriel
trailhead's status under the Eaton Fire order and the other Angeles closures,
checked October 17. It records three contradictions on held trailhead guides
(Eaton Canyon, Mt. Wilson Trail, Millard) without editing them. Index check
November 17; first read December 14.

## October 25 click-attribution deploy

Stay22 CTA links on all trailhead pages now carry Tinylytics click events
(`affiliate.stay22`, value `cta:<slug>` or `contextual:<slug>:trailheads`),
via Sitekit `538200d` and build.py `605e0fb`. No visible content changed on
any page, including the held `/trailheads/*` cohorts, but the deploy
(Netlify `6ade8560e23c9244b8fc54b4`) restamped `<lastmod>` on all 85 sitemap
URLs to October 25 (Sitekit behavior). Click events start accruing from this
date; earlier Stay22 clicks on this site are unattributed.

## November 5 Stay22 checkpoint

Stay22 has been live on this site since August 3, 2026 ([record](2026-08-03-stay22-affiliate-links.md)). Tinylytics `affiliate.stay22` click events since October 25; earlier clicks are unattributed. Links only, no map iframe.

Baseline, from the owner's Stay22 dashboard for October 5 to November 5 (all six
sites combined; the dashboard view does not split by site): 11 loads, 6 views,
4 interactions, 29 clicks, 0 transactions. Lifetime earnings are one $3.34
commission (October 1). Loads and views count only the map iframe; plain links
register clicks without a load.

Next read 2026-12-05 (30 days): Stay22 Hub by campaign for this site against the
baseline above. Clicks are not bookings.
