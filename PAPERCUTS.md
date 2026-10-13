# Papercuts

Small frictions logged in the moment — dead-end tool calls, misleading errors,
undocumented setup steps, flaky commands. Not blocking on their own; together
they show where this repo needs sanding down. Append-only, newest at the bottom.

2026-08-05T05:29:42.027Z - claude-opus-5 - znielsen

Chased a 'broken link' dashboard report for myscenicdrives.com/national-parks/passes/adventure-pass; the URL was already fixed in data/pages.json on Aug 2 (f2b575b) and no live page in the network links to it. The checker re-checks the dead destination URL rather than re-crawling the source page, so fixed links stay listed until you manually hit 'Recheck all broken links' or delete the row. Worth noting so the next person doesn't grep the repo for a URL that isn't there.

2026-09-19T21:38:22.912Z - gpt-6-astra - znielsen

Initial Trailhead Parking read combined too many docs and truncated output; the site also has no local CLAUDE.md, so use workspace CLAUDE.md and focused reads.

2026-09-19T21:38:35.127Z - gpt-6-astra - znielsen

Sitekit templates live under src/sitekit/templates, not sitekit/templates; corrected the lookup before choosing an anchor implementation.

2026-09-19T21:38:48.073Z - gpt-6-astra - znielsen

The Forest Service Adventure Pass landing page returns HTTP 403 through the web reader; use indexed official pages and direct fetches to verify vendor and pass details.

2026-09-19T21:44:07.928Z - gpt-6-astra - znielsen

Body-level jump anchors landed below their headings on mobile; added optional section IDs in the shared detail template so deep links keep the heading visible. A cross-repository git diff also needs git -C ../sitekit rather than a sibling file path.

2026-09-19T21:46:39.195Z - gpt-6-astra - znielsen

One mobile browser click on the Big Bear jump link left the hash unchanged after viewport changes; re-reading its href and clicking again confirmed the correct #big-bear destination.

2026-09-19T21:50:00.775Z - gpt-6-astra - znielsen

The experiment index still showed overdue first-read dates despite a September 4 checkpoint, and README said Batch 8 was undeployed; synchronized the current summaries with the dated experiment records.

2026-09-30T21:56:55.410Z - gpt-6.1-sol - znielsen

The guessed Icehouse Canyon trailhead URL returned 404. The existing Icehouse Canyon Saddle page is accessible and supplies the current permit and winter-skill guidance.

2026-10-10T05:25:52.550Z - claude-opus-5-5 - znielsen

Testing built pages locally (python -m http.server on dist/) logs a console 404 for the Tinylytics embed script on every page, so browser tests that assert 'no console errors' must ignore tinylytics.app.

2026-10-10T15:11:30.608Z - claude-opus-5-5 - znielsen

Running a second read-only codex exec review in the background: it hung on 'Reading additional input from stdin...' and never reviewed anything; redirect stdin from /dev/null (or pass the prompt via '-') when running codex exec non-interactively.
