# Batch 7 — San Bernardino + San Gabriel

**Deployed** 2026-08-02 (`39bc356`) · **3 pages** · site now has **51
trailheads and 55 pages**

The three pages were pulled from `origin/main`, reviewed for plain, specific
copy, built, checked for internal links, and deployed to
[trailheadparking.com](https://trailheadparking.com). The production pages and
all three new routes returned HTTP 200 after deploy.

## What shipped

| Page | The parking question |
|---|---|
| `/trailheads/grays-peak/` | Is the trail open, and which pass can I use? The bald-eagle closure controls the season; parking takes a $5 day pass, Adventure Pass, or America the Beautiful pass. |
| `/trailheads/san-bernardino-peak/` | What do I need before driving the rough road? Parking takes an Adventure Pass, the hike needs a free reserved wilderness permit, and the lot holds about 20 cars. |
| `/trailheads/devils-punchbowl/` | Is this a forest fee site? No — the county lot is free, but it is closed Mondays, has seasonal hours, and holds roughly 30–40 cars. |

## The bet

Local trailhead searches do not need a famous destination or a large parking
lot to be useful. They need a clear answer to the decision that comes before
the hike: can I go today, what do I need to bring or reserve, and will there
be somewhere to leave the car?

These pages test three different constraints in one nearby cluster:

- a seasonal wildlife closure at Grays Peak;
- a permit-and-parking combination at San Bernardino Peak; and
- a free county lot with a weekly closure and limited capacity at Devil's
  Punchbowl.

The prediction is that concrete restrictions will bring in higher-intent
traffic than generic trail descriptions. The copy pass after the origin pull
was part of the test: if the pages earn trust, the useful details should do the
work without padded or promotional language.

## What would make this look right

1. **At 30 days:** all three pages are indexed and receive impressions for
   parking, permit, closure, or hours queries.
2. **At 90 days:** each page attracts its own intent — Grays Peak closure and
   parking, San Bernardino Peak permit and parking, and Devil's Punchbowl
   hours and free parking — rather than only broad trail-name searches.
3. **Against the older local pages:** the new pages show a stronger share of
   queries containing `parking`, `permit`, `pass`, `hours`, or `closed`.

**Falsifier:** if the pages receive only broad hike queries and none of the
constraint-specific searches, then the details are useful on-page but are not
the discovery hook. The next batch should choose topics by demand first and
treat parking constraints as supporting content.

### Check-backs

- **2026-09-01** — 30-day indexing and impressions read.
- **2026-11-01** — 90-day query mix and comparison with the older local pages.

## Shipping record

- Origin pull: `8fd7ae5` added the three trailheads.
- Editorial cleanup: `39bc356` tightened the new copy after the anti-AI-slop
  review.
- Validation: 55 generated pages; 0 unresolved internal references.
- Production: Netlify deploy at [trailheadparking.com](https://trailheadparking.com).
