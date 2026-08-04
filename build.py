#!/usr/bin/env python3
"""Site config for trailheadparking.com.

All build machinery lives in the shared `sitekit` package (../sitekit); this
file is configuration only. Templates in ./templates/ override sitekit's
defaults by filename — base.html, index.html and 404.html are site-specific,
hub/detail/filter/_macros are inherited.
"""

from datetime import date
from pathlib import Path

from sitekit import AffiliateProgram, Site, build

CURRENT_YEAR = date.today().year

# --- Affiliate programs ------------------------------------------------------
# Declared here rather than hand-built in the CTA function, so an unset id
# drops the CTA instead of shipping a link that earns nothing. Stay22's
# publisher id is public and shared across the network, with the environment
# able to override it; Viator stays disabled until its private account value is
# supplied. Amazon is wired but renders no block on trailhead pages — a gear
# search doesn't answer a parking question. It is available to any item that
# names it in `affiliate_ctas`.

AFFILIATES = {
    "stay22": AffiliateProgram(
        key="stay22",
        label="Stay22",
        url_template=(
            "https://www.stay22.com/allez/roam"
            "?aid={id}&address={target}&campaign=trailheadparking_stays"
        ),
        env="STAY22_AID",
        default_id="bigbearmapcom",
        disclosure="We earn a commission on lodging bookings.",
    ),
    "viator": AffiliateProgram(
        key="viator",
        label="Viator",
        url_template="https://www.viator.com/searchResults/all?text={target}&pid={id}",
        env="VIATOR_PID",
        disclosure="We earn a commission on Viator bookings.",
    ),
    "amazon": AffiliateProgram(
        key="amazon",
        label="Amazon",
        url_template="https://www.amazon.com/s?k={target}&tag={id}",
        env="AMAZON_ASSOC_TAG",
        disclosure="As an Amazon Associate we earn from qualifying purchases.",
    ),
}


def contextual_affiliate_ctas(section, item):
    """Lodging and tours, offered only after the page answers the parking question.

    Returns a list; a program with no partner id contributes nothing rather
    than rendering a link that earns nothing.
    """
    if section != "trailheads":
        return []

    ctas = []

    stay22 = AFFILIATES["stay22"]
    if stay22.configured:
        destination = item.get("address") or f"{item['name']}, {item.get('region', '')}"
        ctas.append({
            "heading": "Staying near the trailhead?",
            "body": "Compare nearby lodging after checking the access plan; mountain and park entrances can be much farther from a room than the map first suggests.",
            "label": "Compare nearby stays",
            "url": stay22.url(destination),
        })

    # Tours are worth offering where an outfitter can solve the access problem
    # the page just described — a shuttle or guided trip sidesteps the lot
    # entirely. Keyed off region so the search lands on the park, not the lot.
    viator = AFFILIATES["viator"]
    region = item.get("region")
    if viator.configured and region:
        ctas.append({
            "heading": f"Guided trips in {region}",
            "body": "If the lot fills before you can reach it, a guided trip or tour shuttle starts somewhere else entirely — often the simplest way around a capacity gate.",
            "label": f"See {region} tours",
            "url": viator.url(f"{region} tours"),
        })

    return ctas

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
    affiliate_programs=AFFILIATES,
    extra_globals={"contextual_affiliate_cta": contextual_affiliate_ctas},
)


if __name__ == "__main__":
    build(SITE)
