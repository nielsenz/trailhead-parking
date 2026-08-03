# Batch 6 — Rocky Mountain, Glacier, Yosemite

**Deployed** 2026-07-28 (`fb41dc1`) · **15 pages** · site goes 35 → 50
trailheads, 39 → 54 pages · all facts verified against nps.gov on 2026-07-28

---

## What shipped

**Rocky Mountain National Park**

| Page | The gate |
|---|---|
| `/trailheads/rmnp-timed-entry/` | Master. Two permits, different hours, different end dates |
| `/trailheads/bear-lake/` | Full by 9 a.m. — NPS's own number |
| `/trailheads/glacier-gorge/` | Fills before Bear Lake; NPS gives it no clock time |
| `/trailheads/alpine-visitor-center/` | Trail Ridge Road, seasonal |
| `/trailheads/longs-peak/` | Full by 5–6 a.m.; 2:30 a.m. arrivals for a 3 a.m. start |

**Glacier National Park**

| Page | The gate |
|---|---|
| `/trailheads/glacier-vehicle-reservations/` | Master. **No vehicle reservation in 2026** |
| `/trailheads/logan-pass/` | Fills by sunrise; 3-hour limit enforced 24/7, Jul 1 – Sep 7 |
| `/trailheads/avalanche-creek/` | Shuttle no longer stops here |
| `/trailheads/many-glacier/` | 339 spaces — the only capacity NPS publishes in the park |
| `/trailheads/st-mary-falls/` | Shuttle no longer stops here either |

**Yosemite National Park**

| Page | The gate |
|---|---|
| `/trailheads/yosemite-reservations/` | Master. **No reservation in 2026**, nothing replaced it |
| `/trailheads/yosemite-valley-parking/` | The whole gate. Full by 8 a.m. |
| `/trailheads/glacier-point/` | Seasonal road, no published count |
| `/trailheads/cathedral-lakes/` | Trailhead moved to the Tuolumne VC lot in 2022 |
| `/trailheads/mist-trail/` | No trailhead lot exists; you park at Curry Village |

---

## The bet

**Three parks in one deploy instead of one.** Every batch before this took a
region at a time. This one took three, on the theory that the marginal cost of
park two and three is small once you're inside the NPS source pattern — same
site structure, same fee page layout, same news-release cadence — while the
demand is not remotely marginal. Yosemite alone is a bigger search market than
batches 1–3 combined.

**The hook is an absence.** Batch 5 turned up something that looked like a
one-off: Arches had quietly dropped timed entry for 2026. It wasn't a one-off.
Glacier dropped its vehicle reservation too — first season since 2020 — and
Yosemite announced the same on Feb 18, 2026. Three of the six parks on the site
now gate on nothing but the parking lot.

That's the whole thesis of this batch. **When a reservation system disappears,
the internet doesn't update.** Every guide, every listicle, every forum answer
still tells you to set an alarm for the recreation.gov drop. The searcher's real
question quietly changes from *how do I get a reservation* to *how early do I
have to physically be there*, and that second question is the one this site was
built to answer. A park dropping its reservation isn't a gap in our coverage —
it's the moment our page becomes the correct answer and everyone else's goes
stale.

**Corollary, which is the actual reason to build all three at once:** RMNP is
the control. It still gates entry, with two permits people routinely mix up. So
the cluster carries both states of the same variable — two parks where the
answer is "just show up at 5 a.m." and one where showing up at 5 a.m. gets you
turned around without a permit. Publishing them together makes the contrast
legible, and gives the master pages something to link against.

### Why these three, in this order

- **Yosemite** — largest demand, and the cleanest version of the thesis: no
  reservation, no ticketed replacement, so the answer is *entirely* parking.
- **Glacier** — the most under-served. NPS replaced the reservation with a $1
  ticketed Logan Pass shuttle whose six-stop route silently dropped Avalanche
  Creek, St. Mary Falls and Many Glacier. Nobody has written that down as a
  service cut. Two of our pages state plainly that there's no shuttle fallback.
- **Rocky Mountain** — the control, and the highest-value confusion to resolve:
  two permits, 5 a.m. vs 9 a.m. windows, Oct 18 vs Oct 12 end dates.

### The page mix, and why it's 1 master + 4 lots

Same shape as batches 4 and 5, kept deliberately. The master page takes the
system-level query (*do I need a reservation for X*) and the four lot pages take
the intent-heavy ones (*Bear Lake trailhead parking*). The master absorbs the
volume and the volatility; when a reservation policy flips in February, it's one
page that needs a rewrite instead of five.

---

## What this batch cost us, honestly

**The data-availability rule broke here.** Batch 4 chose Zion partly because NPS
published enough to state hard numbers, and batch 5 vindicated that — 9 of 10
pages carried real capacities. This batch got **one published capacity across
fifteen pages**: Many Glacier's 339 spaces. Everything else says NO PUBLISHED
COUNT and explains what's circulating instead (Logan Pass's "236 spaces" traces
to a social post; Longs Peak's "around 100 cars" to climbing forums; Glacier
Point's "around 200" to Conservancy material).

We shipped anyway, which is a change in policy worth naming: **demand overrode
data availability for the first time.** The compensating move was to make the
absence itself the content — every one of those pages names the number that
circulates and says why we won't repeat it. Whether that reads as authoritative
or as evasive is genuinely untested, and it's the main thing to watch.

The one capacity we did get came from a *construction update*, not a parking
page. That's a sourcing technique, not luck — worth trying first in the next
park that won't publish counts.

**Three pages are built on an absence that gets re-decided every year.** Glacier
and Yosemite could both reinstate reservations around Feb 2027, and if they do,
those master pages need rewrites rather than edits. Logged in
[`docs/todos.md`](../docs/todos.md) with 12 other open items from this batch.

---

## What would make this look right

Measured in Search Console and Bing Webmaster Tools, against the batch 4/5
pages as the in-house benchmark — same template, same build, published 5 weeks
earlier, so the comparison is close to clean.

1. **Impressions, not clicks, at 30 days.** These are competitive terms and
   nothing ranks in a month. What's diagnostic early is whether the *reservation
   master pages* pick up impressions on reservation-phrased queries. If
   "yosemite reservation 2026" style queries surface the master page, the
   absence-as-hook thesis is alive.
2. **Query mix at 90 days.** The signal to look for is queries that still
   presume a reservation exists landing on pages that say it doesn't. That gap
   is the whole bet. If instead the traffic is all plain "bear lake parking",
   the batch is working as ordinary lot coverage and the cluster reasoning added
   nothing — worth knowing before batch 7.
3. **Master vs lot split.** Batches 4–5 predict lot pages carry it. If the
   masters outperform here, the reservation-confusion read is right and the next
   batch should weight toward system-level pages (Haena, Acadia, Old Rag are all
   reservation-gated).
4. **AI citations.** Every page ships FAQPage JSON-LD, and stale-reservation
   questions are exactly the kind assistants get wrong from 2024 training data.
   Anecdotal, but check whether assistants cite these pages when asked about
   2026 Glacier or Yosemite reservations.

**Falsifier:** if at 90 days the three master pages haven't out-impressed the
Zion and Arches masters on reservation-phrased queries, then the absence wasn't
the hook — the demand was — and the three-park cluster was just three batches
run at once. That's not a failure, but it means the *reasoning* was decorative,
and batch 7 should pick regions on demand alone and stop building the contrast.

### Check-backs

- **2026-08-27** — 30-day read (impressions only).
- **2026-10-26** — 90-day read, verdict, update the log table in
  [README.md](README.md).
- **2026-10-XX** — settles the RMNP Oct 18/Oct 12 vs Oct 19/Oct 13 conflict by
  observation; see `docs/todos.md`.
- **2027-02** — the one that matters. Glacier, Yosemite and RMNP all re-announce
  around then. If either absence reverses, this experiment's premise reverses
  with it.

---

## Loose end

The commit message for `fb41dc1` says "nine of fifteen lots have no published
capacity." Counting the shipped data, it's fourteen of fifteen — one published
figure in the batch. The pages themselves are right; the commit message
undercounts. Noting it here because the number gets quoted.
