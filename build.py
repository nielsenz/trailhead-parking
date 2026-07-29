#!/usr/bin/env python3
"""Site config for trailheadparking.com.

All build machinery lives in the shared `sitekit` package (../sitekit); this
file is configuration only. Templates in ./templates/ override sitekit's
defaults by filename — base.html, index.html and 404.html are site-specific,
hub/detail/filter/_macros are inherited.
"""

from datetime import date
from pathlib import Path

from sitekit import Site, build

CURRENT_YEAR = date.today().year

# Hub cards and the region nav are grouped in this order; a region not listed
# here still renders, after the known ones. Keep coarse enough that a region
# holds several trailheads as coverage fills in.
REGION_ORDER = [
    "San Bernardino Mountains",
    "San Gabriel Mountains",
    "San Jacinto Mountains",
    "San Diego County",
    "Zion National Park",
    "Bryce Canyon National Park",
    "Arches National Park",
    "Rocky Mountain National Park",
    "Glacier National Park",
    "Yosemite National Park",
]

# --- Section configuration ---------------------------------------------------
# Each section = one GeoJSON file in data/, one hub page, one detail page per
# feature. `fact_rows` maps property keys -> labels for the quick-facts table,
# in display order; rows with missing values are skipped.

SECTIONS = {
    "trailheads": {
        "nav_label": "Trailheads",
        "hub_title": f"Trailhead Parking, Honestly: Every Lot We Cover ({CURRENT_YEAR})",
        "meta_title": f"Trailhead Parking Guides: Lot Sizes, Fill Times & Passes ({CURRENT_YEAR})",
        "meta_description": "Trailhead parking across Southern California, Zion, Bryce Canyon and Arches. How many cars each lot fits, when it fills, what pass or permit you need, and what to do when it's full.",
        "hub_intro": (
            "The hike is rarely the hard part — the lot is. Each guide below covers one "
            "trailhead: how many cars actually fit, when it fills on a weekend, what goes on the "
            "dash, the tow/citation risk of getting creative, and the realistic plan B. Pass rules "
            "change completely between regions — the <a href=\"/adventure-pass/\">Adventure Pass</a> "
            "covers most national-forest trailheads in the San Bernardinos and San Gabriels, but "
            "buys nothing at San Diego's state, county and city lots, and nothing in the Utah "
            "national parks, where a shuttle, a permit lottery or a 1-hour posted limit decides "
            "where you park at all."
        ),
        "marker_emoji": "🅿️",
        "fact_rows": [
            ("trail_served", "Trail served"),
            ("fee", "Cost / pass"),
            ("lot_size", "Lot size"),
            ("fill_time", "When it fills"),
            ("overflow", "Overflow option"),
            ("tow_risk", "Tow / citation risk"),
            ("restrooms", "Restrooms"),
            ("road_access", "Road to the lot"),
            ("best_season", "Busy season"),
        ],
        "schema_type": "ParkingFacility",
    },
}

# --- Filter pages ------------------------------------------------------------
# None yet; same mechanism as lake-arrowhead when needed.

FILTERS = []

NAV = [
    ("/trailheads/", "Trailheads"),
    ("/adventure-pass/", "Adventure Pass"),
    ("/about/", "About"),
]

SITE = Site(
    base_dir=Path(__file__).parent,
    base_url="https://trailheadparking.com",
    site_name="TrailheadParking.com",
    nav=NAV,
    sections=SECTIONS,
    page_filters=FILTERS,
    # Coverage spans several states; hub maps fit their own markers, so this is
    # only the fallback for a section with no coordinates at all.
    area_center=(33.85, -117.20),
    area_zoom=8,
    group_by="region",
    group_order=REGION_ORDER,
    group_label="region",
    default_marker_emoji="🅿️",
)


if __name__ == "__main__":
    build(SITE)
