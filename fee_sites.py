"""Context for /adventure-pass/where-needed/: USFS day-use sites plus our guides.

data/usfs_fee_sites.json is refreshed by scripts/usfs_fee_sites.py. A guide's
verified fee answer is shown beside a site only when the guide covers that same
place (see same_place); the two can disagree (Vincent Gap), and the guide is the
checked one. Other guides within NEARBY_KM are linked without their fee answer:
proximity alone put the free Discovery Center lot next to the concession-run
Meadows Edge Picnic.
"""

import json
import math
from pathlib import Path
import re

DATA = Path(__file__).parent / "data"
NEARBY_KM = 0.5
SAME_PLACE_KM = 0.3
COLOCATED_KM = 0.05
# Words shared by unrelated places; a match needs a distinctive word in common.
GENERIC_WORDS = {
    "picnic", "area", "site", "park", "parking", "lot", "trailhead", "trail",
    "day", "use", "the", "via", "mt", "mount", "falls", "canyon", "creek", "peak",
    "lake", "big", "san", "national", "forest", "ohv", "staging",
}
FOREST_ORDER = [
    "Angeles National Forest",
    "San Bernardino National Forest",
    "Cleveland National Forest",
    "Los Padres National Forest",
]
# Wording stays inside what the agency record supports; see the page's
# "How to read this list" section for the caveats behind each label.
CATEGORIES = {
    "adventure_pass": {"label": "Adventure Pass site", "tone": "warn"},
    "concession": {"label": "Concession fee — pass acceptance varies", "tone": "bad"},
    "conflicting": {"label": "Records conflict — check first", "tone": "bad"},
    "other_fee": {"label": "Other fee type", "tone": "info"},
    "fee_unspecified": {"label": "Fee listed — type not stated", "tone": "info"},
    "no_fee": {"label": "No fee listed", "tone": "good"},
}


def _km(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 12742 * math.asin(math.sqrt(h))


def _words(name):
    words = re.sub(r"[^a-z ]", " ", (name or "").lower().replace("'s", "")).split()
    return {w.rstrip("s") for w in words if w not in GENERIC_WORDS and len(w) > 2}


def same_place(site, guide, distance):
    """Co-located, or close with a distinctive name word in common."""
    if distance <= COLOCATED_KM:
        return True
    return distance <= SAME_PLACE_KM and bool(_words(site["name"]) & _words(guide["name"]))


def _guides():
    features = json.loads((DATA / "trailheads.json").read_text())["features"]
    return [
        {
            "slug": f["properties"]["slug"],
            "name": f["properties"]["name"],
            "fee": f["properties"].get("fee"),
            "verified": f["properties"].get("verified"),
            "lon": f["geometry"]["coordinates"][0],
            "lat": f["geometry"]["coordinates"][1],
        }
        for f in features
        if f.get("geometry")
    ]


def fee_sites():
    path = DATA / "usfs_fee_sites.json"
    if not path.exists():
        return None
    payload = json.loads(path.read_text())
    guides = _guides()
    forests = {name: [] for name in FOREST_ORDER}
    counts = {key: 0 for key in CATEGORIES}
    for site in payload["sites"]:
        nearby = sorted(
            (pair for pair in ((_km(site["lat"], site["lon"], g["lat"], g["lon"]), g)
                               for g in guides) if pair[0] <= NEARBY_KM),
            key=lambda pair: pair[0],
        )
        same = [g for d, g in nearby if same_place(site, g, d)]
        site = dict(site, category=CATEGORIES[site["fee_category"]],
                    guide=same[0] if same else None,
                    nearby_guide=None if same or not nearby else nearby[0][1])
        forests.setdefault(site["forest"], []).append(site)
        counts[site["fee_category"]] += 1
    return {
        "source": payload["source"],
        "source_url": payload["source_url"],
        "retrieved": payload["retrieved"],
        "total": len(payload["sites"]),
        "counts": counts,
        "categories": CATEGORIES,
        "forests": [(name, sites) for name, sites in forests.items() if sites],
        "markers": [
            {"id": s["id"], "name": s["name"], "lat": s["lat"], "lon": s["lon"],
             "category": s["fee_category"], "label": CATEGORIES[s["fee_category"]]["label"]}
            for s in payload["sites"]
        ],
    }
