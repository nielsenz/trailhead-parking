#!/usr/bin/env python3
"""Site config for trailheadparking.com.

All build machinery lives in the shared `sitekit` package (../sitekit); this
file is configuration only. Templates in ./templates/ override sitekit's
defaults by filename — base.html, index.html and 404.html are site-specific,
hub/detail/filter/_macros are inherited.
"""

import os
from datetime import date
from pathlib import Path
from urllib.parse import urlencode

from sitekit import Site, build

CURRENT_YEAR = date.today().year
STAY22_AID = os.environ.get("STAY22_AID", "bigbearmapcom")


def contextual_stay22_cta(section, item):
    """Offer nearby lodging only after the page answers the parking question."""
    if section != "trailheads":
        return None
    destination = item.get("address") or f"{item['name']}, {item.get('region', '')}"
    query = urlencode({
        "aid": STAY22_AID,
        "address": destination,
        "campaign": "trailheadparking_stays",
    })
    return {
        "heading": "Staying near the trailhead?",
        "body": "Compare nearby lodging after checking the access plan; mountain and park entrances can be much farther from a room than the map first suggests.",
        "label": "Compare nearby stays",
        "url": f"https://www.stay22.com/allez/roam?{query}",
    }

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
    "Mount Whitney",
    "Yosemite National Park",
    "Grand Canyon National Park",
    "Acadia National Park",
    "Kauai — Haena & Napali Coast",
    "Santa Monica Mountains",
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
        "meta_description": "Trailhead parking across Southern California and major national parks. How many cars each lot fits, when it fills, what pass or permit you need, and what to do when it's full.",
        "hub_intro": (
            "The hike is rarely the hard part — the lot is. Each guide below covers one "
            "trailhead: how many cars actually fit, when it fills on a weekend, what goes on the "
            "dash, the tow/citation risk of getting creative, and the realistic plan B. Pass rules "
            "change completely between regions — the <a href=\"/adventure-pass/\">Adventure Pass</a> "
            "covers most national-forest trailheads in the San Bernardinos and San Gabriels, but "
            "buys nothing at San Diego's state, county and city lots, and nothing in national or "
            "state parks where an entrance pass, shuttle, permit or timed reservation controls "
            "the approach."
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
        "hub_sections": [
            {
                "heading": "The one rule that saves your morning: get there early",
                "body": "Across every trailhead on this site, in every region, the single biggest predictor of a good day is arrival time. Popular Southern California lots — Heart Rock, Icehouse Canyon, Cedar Creek Falls, Potato Chip Rock — routinely <strong>fill between 7 and 9am on weekends</strong>. National-park and state-park sites add another kind of gate: a shuttle, a day-use ticket, a timed-entry reservation or a reservation-only parking slot. If a lot has a hard cap and a tow or citation risk on the shoulder, showing up at 10am doesn't mean a long walk — it means turning around. Each guide below gives the specific fill time we could verify, plus the realistic Plan B when it's already full."
            },
            {
                "heading": "Which pass or permit you actually need (they're not the same thing)",
                "body": "The most expensive mistakes here aren't parking tickets — they're driving hours to a trailhead with the wrong pass, or none. The rules change completely by region:\n\n<strong>Southern California national forests</strong> (San Bernardino, San Gabriel, San Jacinto ranges) mostly use the <a href=\"/adventure-pass/\">Adventure Pass</a> — $5/day or $30/year on the dash, or an America the Beautiful pass. <strong>San Diego County</strong> is a patchwork: Cedar Creek Falls needs a $6 Recreation.gov <em>permit</em> (not a parking pass), while Torrey Pines is a state reserve and Potato Chip Rock's Lake Poway lot is a city park — none of them honor an Adventure Pass. <strong>National parks</strong> use entrance passes plus their own systems: Yosemite manages Valley parking and shuttles, Grand Canyon routes hikers from designated lots to trailheads, and Acadia adds a Cadillac vehicle reservation. Hāʻena State Park requires advance entry and parking reservations for nonresidents.\n\nA permit is not a parking pass, an entrance fee is not an Adventure Pass, and a reservation is not a guarantee of a space. Every guide below states exactly which one that specific lot requires."
            },
            {
                "heading": "How we cover parking — and how facts stay current",
                "body": "This site covers the parking situation, not the trail's scenery: how many cars fit, when the lot fills, what goes on the dash, the tow and citation risk of getting creative, and the realistic overflow plan. Coverage spans four Southern California ranges plus national parks from Rocky Mountain and Glacier to Yosemite, Zion and the Grand Canyon, where entrance systems, shuttles and reservation rules can matter as much as the lot itself.\n\nMountain and desert access rules change with the seasons, so every page carries a <strong>\"facts last verified\"</strong> date, and the perishable ones — road closures, heat-advisory closures, permit systems — get re-checked against the official source on a recurring pass. When something changes, we fix the page rather than defend it. More on the method is on the <a href=\"/about/\">about page</a>."
            },
        ],
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
    extra_globals={"contextual_affiliate_cta": contextual_stay22_cta},
)


if __name__ == "__main__":
    build(SITE)
