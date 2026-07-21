#!/usr/bin/env python3
"""Static site builder for trailheadparking.com.

JSON data (GeoJSON FeatureCollections in data/) -> Jinja2 templates -> dist/.
Deploy: netlify deploy --prod --dir=dist. No framework, no server.

Sister codebase to ~/projects/sites/lake-arrowhead (same conventions):
directory-style URLs only, self-referencing canonicals on the non-www host,
sitemap generated from the pages actually built.
"""

import json
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
DIST_DIR = BASE_DIR / "dist"

BASE_URL = "https://trailheadparking.com"
SITE_NAME = "TrailheadParking.com"
CURRENT_YEAR = date.today().year

# Map center for hub maps. Coverage now spans Southern California, so the hub
# map sits between the San Gabriels and San Diego rather than on the SBNF front
# range; detail-page maps are per-item and unaffected.
AREA_CENTER = [33.85, -117.20]
AREA_ZOOM = 8

# Hub cards and the region nav are grouped in this order; a region not listed
# here still renders, after the known ones. Keep coarse enough that a region
# holds several trailheads as coverage fills in.
REGION_ORDER = [
    "San Bernardino Mountains",
    "San Gabriel Mountains",
    "San Jacinto Mountains",
    "San Diego County",
]

# --- Section configuration ---------------------------------------------------
# Each section = one GeoJSON file in data/, one hub page, one detail page per
# feature. `fact_rows` maps property keys -> labels for the quick-facts table,
# in display order; rows with missing values are skipped.

SECTIONS = {
    "trailheads": {
        "nav_label": "Trailheads",
        "hub_title": f"Southern California Trailhead Parking: Every Lot, Honestly ({CURRENT_YEAR})",
        "meta_title": f"Southern California Trailhead Parking: Lot Sizes, Fill Times & Passes ({CURRENT_YEAR})",
        "meta_description": "Trailhead parking across Southern California — the San Bernardinos, San Gabriels, San Jacintos and San Diego County. How many cars each lot fits, when it fills, what pass you need, and what to do when it's full.",
        "hub_intro": (
            "The hike is rarely the hard part out here — the lot is. Each guide below covers one "
            "trailhead: how many cars actually fit, when it fills on a weekend, what goes on the "
            "dash, the tow/citation risk of getting creative, and the realistic plan B. Pass rules "
            "vary by range — the <a href=\"/adventure-pass/\">Adventure Pass</a> covers most "
            "national-forest trailheads in the San Bernardinos and San Gabriels, but not the "
            "state, county and city lots in San Diego."
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


def load_section(name):
    """Load a GeoJSON FeatureCollection into a list of item dicts."""
    path = DATA_DIR / f"{name}.json"
    if not path.exists():
        return []
    fc = json.loads(path.read_text())
    items = []
    for feature in fc["features"]:
        item = dict(feature["properties"])
        geometry = feature.get("geometry")
        item["coordinates"] = geometry["coordinates"] if geometry else None  # [lon, lat]
        items.append(item)
    return items


def group_by_region(items):
    """Group hub items into [(region, [items]), ...] in REGION_ORDER.

    Items without a `region` fall into a trailing "Elsewhere" group so a
    missing field shows up on the page instead of silently dropping a card.
    """
    buckets = {}
    for item in items:
        buckets.setdefault(item.get("region") or "Elsewhere", []).append(item)
    known = [(r, buckets.pop(r)) for r in REGION_ORDER if r in buckets]
    return known + sorted(buckets.items())


def fact_value(value):
    """Render a property value for the facts table."""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return str(value)


def build_facts(item, fact_rows):
    facts = []
    for key, label in fact_rows:
        if key in item and item[key] is not None and item[key] != "":
            facts.append({"label": label, "value": fact_value(item[key])})
    return facts


def paragraphs(text):
    """Split double-newline text into paragraphs (data may embed inline HTML)."""
    if not text:
        return []
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def slugify(text):
    """Region name -> anchor id."""
    import re

    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


def strip_tags(text):
    """Drop inline HTML from FAQ answers for JSON-LD text fields."""
    import re

    return re.sub(r"<[^>]+>", "", text or "")


def breadcrumb_block(trail):
    """BreadcrumbList JSON-LD from a [(name, url), ...] trail ending at this page."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": url}
            for i, (name, url) in enumerate(trail, 1)
        ],
    }


def schema_blocks(item, schema_type, canonical, trail=None):
    """JSON-LD for a detail page: Place-ish entity + FAQPage + breadcrumbs."""
    blocks = []
    place = {
        "@context": "https://schema.org",
        # Items can override the section default (e.g. guide pages are WebPage,
        # not a Place subtype).
        "@type": item.get("schema_type", schema_type),
        "name": item["name"],
        "description": strip_tags(
            item.get("meta_description") or item.get("card_summary") or ""
        ),
        "url": canonical,
    }
    if item.get("coordinates"):
        place["geo"] = {
            "@type": "GeoCoordinates",
            "latitude": item["coordinates"][1],
            "longitude": item["coordinates"][0],
        }
    if item.get("address"):
        place["address"] = item["address"]
    if item.get("phone"):
        place["telephone"] = item["phone"]
    blocks.append(place)

    if item.get("faq"):
        blocks.append(
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f["q"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": strip_tags(f["a"]),
                        },
                    }
                    for f in item["faq"]
                ],
            }
        )

    if trail:
        blocks.append(breadcrumb_block(trail))
    return blocks


def make_env():
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["paragraphs"] = paragraphs
    env.filters["slugify"] = slugify
    env.globals.update(
        site_name=SITE_NAME,
        base_url=BASE_URL,
        current_year=CURRENT_YEAR,
        nav=NAV,
        area_center=AREA_CENTER,
        area_zoom=AREA_ZOOM,
    )
    return env


class Builder:
    def __init__(self):
        self.env = make_env()
        self.pages = []  # (path, lastmod) for sitemap

    def emit(self, path, template, **context):
        """Render template to dist/<path>/index.html with canonical URL."""
        assert path.startswith("/") and path.endswith("/"), path
        canonical = BASE_URL + path
        html = self.env.get_template(template).render(
            canonical_url=canonical, path=path, **context
        )
        out = DIST_DIR / path.lstrip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        self.pages.append(path)

    def build(self):
        if DIST_DIR.exists():
            shutil.rmtree(DIST_DIR)
        DIST_DIR.mkdir()

        if STATIC_DIR.exists():
            shutil.copytree(STATIC_DIR, DIST_DIR / "static")

        sections = {name: load_section(name) for name in SECTIONS}

        # Home
        self.emit("/", "index.html", sections=sections)

        # Section hubs + detail pages
        for name, cfg in SECTIONS.items():
            items = sections[name]
            if not items:
                continue
            hub_items = [i for i in items if not i.get("hub_hidden")]
            self.emit(
                f"/{name}/",
                "hub.html",
                section=name,
                cfg=cfg,
                items=hub_items,
                groups=group_by_region(hub_items),
            )
            for item in items:
                path = f"/{name}/{item['slug']}/"
                trail = [
                    ("Home", BASE_URL + "/"),
                    (cfg["nav_label"], f"{BASE_URL}/{name}/"),
                    (item["name"], BASE_URL + path),
                ]
                self.emit(
                    path,
                    "detail.html",
                    section=name,
                    cfg=cfg,
                    item=item,
                    facts=build_facts(item, cfg["fact_rows"]),
                    jsonld=schema_blocks(item, cfg["schema_type"], BASE_URL + path, trail),
                )

        # Filter pages
        for f in FILTERS:
            items = [i for i in sections[f["section"]] if f["match"](i)]
            cfg = SECTIONS[f["section"]]
            self.emit(
                f"/{f['section']}/{f['slug']}/",
                "filter.html",
                section=f["section"],
                cfg=cfg,
                filter=f,
                items=items,
            )

        # Standalone pages (e.g. /adventure-pass/) — features in pages.json with
        # a `path` property; rendered with the detail template, no hub. An
        # optional `parent` ({label, href}) nests the page in breadcrumbs.
        for item in load_section("pages"):
            cfg = {
                "nav_label": item["name"],
                "marker_emoji": item.get("marker_emoji", "🅿️"),
                "fact_rows": [(r["key"], r["label"]) for r in item.get("fact_rows", [])],
                "schema_type": item.get("schema_type", "Place"),
            }
            trail = [("Home", BASE_URL + "/")]
            if item.get("parent"):
                trail.append((item["parent"]["label"], BASE_URL + item["parent"]["href"]))
            trail.append((item["name"], BASE_URL + item["path"]))
            self.emit(
                item["path"],
                "detail.html",
                section=None,
                cfg=cfg,
                item=item,
                facts=build_facts(item, cfg["fact_rows"]),
                jsonld=schema_blocks(item, cfg["schema_type"], BASE_URL + item["path"], trail),
            )

        self.write_infra()
        print(f"Built {len(self.pages)} pages -> {DIST_DIR}")
        for p in sorted(self.pages):
            print(f"  {p}")

    def write_infra(self):
        today = date.today().isoformat()
        urls = "\n".join(
            f"  <url><loc>{BASE_URL}{p}</loc><lastmod>{today}</lastmod></url>"
            for p in sorted(self.pages)
        )
        (DIST_DIR / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )
        (DIST_DIR / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n"
        )
        # Netlify _redirects: www -> non-www (forced 301)
        (DIST_DIR / "_redirects").write_text(
            "https://www.trailheadparking.com/* https://trailheadparking.com/:splat 301!\n"
        )
        html_404 = self.env.get_template("404.html").render(
            canonical_url=BASE_URL + "/404.html", path="/404.html"
        )
        (DIST_DIR / "404.html").write_text(html_404)


if __name__ == "__main__":
    Builder().build()
