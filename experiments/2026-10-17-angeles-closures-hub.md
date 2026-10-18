# Angeles closures hub

**Status:** shipped October 17, 2026 (see Release).
**Page (new):** `/angeles-closures/`.
**Page (changed):** homepage (one intent card linking to it).
**Context:** October 17 network search-gap review.

## Bet

About 600 impressions in the review window went to Angeles closure searches
with no page built for them; they scattered across individual trailhead guides. Sedona's
`/closures/` page already earns clicks at positions 5–8 for the same pattern.
One page that lists each San Gabriel trailhead's status from the official
sources, quotes the Eaton Fire order and keeps the source contradictions
visible should rank for the cluster and send people on to the trailhead
guides.

## Sources checked October 17, 2026

- Angeles alerts index and the Eaton Fire Area Closure alert; signed Forest
  Order 05-01-26-04 (January 7, 2026–December 31, 2027) and its Exhibit B map.
- Williamson Rock order 05-01-24-04 and Rincon-Redbox order 05-01-26-13.
- USFS site pages: Chantry Flat, Switzer, East Fork, Icehouse Canyon (all "Site
  Open").
- L.A. County Parks, Eaton Canyon Natural Area: "closed until further notice
  due to the Eaton Fire".
- Caltrans road information for SR-2 and SR-39 (report of 9:49 PM).

## Contradictions found (not resolved on held pages)

The trailhead guides are under the `trailhead-batches-final` hold until
October 26, so these were recorded, not edited:

- `/trailheads/eaton-canyon/` attributes the natural area's closure to Forest
  Order 05-01-26-04 "through December 31, 2027". The natural area is county
  land; the county lists it closed with no end date. The canyon above it is in
  the federal order. Both say closed; the attribution and date are wrong.
- `/trailheads/mount-wilson-trail/` (checked August 1) says the lower trail
  reopened. The USFS Chantry Flat page now lists "Sierra Madre section of Mt
  Wilson Trail closed below Upper Winter Creek Trail", while the order's list
  and map leave the trail open. Needs a call to Sierra Madre or the district.
- The Eaton alert lists Millard Trail Camp as affected; the trailhead guides
  say Millard reopened in January 2026.

These are factual corrections that may precede the hold's read; if made,
record them as interventions in the relevant experiment.

## Changes

- `data/pages.json`: new standalone feature `angeles-closures` (WebPage, five
  sections, five FAQs consistent with the visible text, fact rows for the
  order, related official links).
- `templates/index.html`: "Angeles closures" intent card before Chantry Flat.

No trailhead guide or Adventure Pass page changed.

## How we'll know

- **Index check (November 17):** URL Inspection for `/angeles-closures/`.
- **First read (December 14):** final GSC November 13–December 10 and Bing for
  the same window: impressions, clicks and position for queries containing
  "closure", "closed" or "open" with Eaton, Echo Mountain, Mt. Lowe, Mt. Wilson
  or Angeles. Compare with the same query set on the trailhead guides over
  September 16–October 13 to see whether the hub adds demand or takes it.

Confounders: the held trailhead pages' own reads (October 26 and 31); any new
Forest Service order changes demand.

## Maintenance

Recheck the alerts page, Caltrans and each listed site before relying on this
page. December 31, 2026 ends two of the orders; look for replacements rather
than marking anything open. The Eaton order runs to December 31, 2027.

## Release

Commit `d7b5fd1` (Sitekit `11f7004`), deployed October 17, 2026 from a clean
tree (Netlify `6ad4535f9b39c447d66fb0b4`); audit 0 errors, 1 pre-existing
warning. Reviewed by two headless Codex passes (no blockers; the Vincent Gap
entry was reworded to say its own status was not rechecked). Browser-checked at
390 and 1280 px. Verified live: `/angeles-closures/` returns 200, the slashless
form 301s to it, the homepage card links to it, and it is in the sitemap. To
do: "Request indexing" in the GSC UI.

## Correction, October 17, 2026 (same day)

After this record was written, L.A. County Trails alert 4257
(trails.lacounty.gov) was read. It changes two of the three contradictions
above:

- **Eaton Canyon:** the county's trails alert does list the Eaton Canyon Trail
  and waterfall closed until December 31, 2027, so the date on the held page
  was supported. The error was the attribution to the forest order.
- **Mt. Wilson Trail:** the county lists it as reopened by Sierra Madre, so the
  conflict is now county (open) against the Forest Service's Chantry Flat page
  (closed below Upper Winter Creek). It is still unresolved.
- **Millard:** the county says Millard Canyon's trails are open and the
  campground is closed. That matches the Forest Service listing Millard Trail
  Camp as affected, so there is no contradiction.

All three held pages were corrected as an intervention, recorded in the
[September 4 review](2026-09-04-review.md). This hub was updated to cite the
county alert, report the Mt. Wilson conflict with the county's position, and
drop Millard from the contradictions.
