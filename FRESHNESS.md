# Trailhead Parking freshness audit

This file is the issue-body template for `.github/workflows/freshness-reminder.yml`.
The workflow declares Mondays at 15:00 UTC and opens an issue only when no open
`freshness` issue exists. It does not run these checks, build or deploy.

- Recheck closures, passes, permits, reservation rules and seasonal access. Do not fill unsupported lot counts, fill times or overflow rules by guessing.
- Check seller sources and purchase links when reviewing Adventure Pass guidance; a listed vendor does not establish stock or opening hours.
- Keep regional and famous/local cohorts stable until their recorded reads. Annotate factual changes and changed supporting links.
- Build with `uv run build.py`, inspect warnings and run the shared HTML audit from the README. Check directions and official-source controls where changed.
- Read due experiment/source records and the local `analytics-queries/travel_ops`
  queue. Record findings and interventions in the appropriate source/experiment
  files; source acknowledgments and queue completion do not update site data.
- Check existing links and disclosures where affected. Earnings reporting is
  excluded from this maintenance pass.

Close the issue only when its editorial/release checks are complete; otherwise
leave it open with remaining work. Follow the README's clean-release procedure
when changes need publishing. Closing this issue does not complete a task in the
local queue, and completing a local task does not close this issue.
