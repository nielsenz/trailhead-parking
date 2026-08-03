# Experiments

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
| 2026-07-28 | [Batch 6 — Rocky Mountain, Glacier, Yosemite](2026-07-28-batch-6-national-parks.md) | Three marquee parks at once; absence-of-reservation as the hook | ⏳ open — first read ~Aug 27 |
| 2026-08-02 | [Batch 7 — San Bernardino + San Gabriel](2026-08-02-batch-7-san-bernardino-san-gabriel.md) | Practical constraints — closures, permits, and small lots — can carry local trailhead search demand | ⏳ open — first read ~Sep 1 |
| 2026-08-02 built / 2026-08-03 deployed | [Batch 8 — Famous vs local trailheads](2026-08-02-batch-8-famous-vs-local.md) | A recognizable trail name may earn discovery; a smaller local cluster may earn more parking-specific visits | ⏳ open — first read Sep 2 |

Batches 1–5 shipped before this log existed. Their reasoning is compressed into
the roadmap in [../README.md](../README.md); it isn't worth reconstructing them
retroactively, since the point of the format is writing the bet down *first*.
