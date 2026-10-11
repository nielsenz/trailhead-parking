#!/usr/bin/env python3
"""Refresh data/usfs_fee_sites.json from the Forest Service recreation-site layer.

Pulls every day-use site in the four Adventure Pass forests and keeps the fee,
operator and status fields the /adventure-pass/where-needed/ page shows. The
output records the retrieval date; it is agency data as published, not a
TrailheadParking verification. Standard library only:

    uv run python scripts/usfs_fee_sites.py
"""
from __future__ import annotations

from datetime import date
import json
import math
from pathlib import Path
import re
import urllib.parse
import urllib.request

OUT = Path(__file__).resolve().parents[1] / 'data' / 'usfs_fee_sites.json'
LAYER = ('https://apps.fs.usda.gov/arcx/rest/services/EDW/'
         'EDW_RecInfraRecreationSites_02/MapServer/0')
FORESTS = {
    '0501': 'Angeles National Forest',
    '0502': 'Cleveland National Forest',
    '0507': 'Los Padres National Forest',
    '0512': 'San Bernardino National Forest',
}
# Popular trailheads are often recorded as picnic, interpretive or OHV sites,
# so filtering on TRAILHEAD alone misses Chantry Flat, Switzer and Heaps Peak.
DAY_USE_TYPES = {
    'TRAILHEAD', 'PICNIC SITE', 'DAY USE AREA', 'OHV STAGING AREA',
    'INTERPRETIVE SITE', 'OBSERVATION SITE', 'FISHING SITE',
    'INFO SITE/FEE STATION', 'INTERPRETIVE VISITOR CENTER (MINOR)',
}
# A concessionaire can run its own parking pass: Vincent Gap's Big Pines lot is
# listed as a standard amenity fee site with "Adventure Passes are Honored",
# yet the lot did not accept them when checked on August 2, 2026.
CONCESSION_OPERATORS = {'Concessionaire', 'ExplorUS'}
FIELDS = [
    'site_cn', 'managing_org', 'site_name', 'public_site_name', 'site_type',
    'fee_charged', 'fee_type', 'fee_description', 'operated_by',
    'seasonal_operational_status', 'restroom_availability', 'usda_portal_url',
    'latitude', 'longitude', 'edw_last_modify',
]


def fetch_sites():
    where = ' OR '.join(f"managing_org LIKE '{code}%'" for code in FORESTS)
    rows, offset = [], 0
    while True:
        query = urllib.parse.urlencode({
            'where': where, 'outFields': ','.join(FIELDS), 'returnGeometry': 'false',
            'orderByFields': 'objectid', 'resultOffset': offset,
            'resultRecordCount': 1000, 'f': 'json',
        })
        with urllib.request.urlopen(f'{LAYER}/query?{query}', timeout=180) as response:
            page = json.load(response)
        if 'error' in page:
            raise RuntimeError(page['error'])
        rows += [feature['attributes'] for feature in page['features']]
        if not page.get('exceededTransferLimit'):
            return rows
        offset += len(page['features'])


def clean_name(row):
    name = (row['public_site_name'] or row['site_name'] or '').strip()
    if name.isupper():
        name = name.title()
    # INFRA title-cases apostrophes ("Children'S") and abbreviations ("Cg", "Ohv").
    name = re.sub(r"'S\b", "'s", name)
    name = re.sub(r'\b(Ohv|Dua|Pg)\b', lambda m: m.group(1).upper(), name)
    return re.sub(r'\bCg\b', 'Campground', name)


def fee_category(row):
    """Classify only what the record supports; contradictory records stay contradictory.

    Seen in the data: fee_charged N alongside "$5 per vehicle per day" or a
    standard amenity fee type (Upper Bear Creek), and fee_charged Y alongside
    "No fees are required for this site" (Morgan Trailhead).
    """
    description = (row['fee_description'] or '').lower()
    # Summit OHV's whole description is "Adventure Pass", with fee_charged N.
    lists_fee = ('$' in description or 'pass' in description
                 or row['fee_type'] is not None)
    says_free = 'no fee' in description
    if row['fee_charged'] not in ('Y', 'N'):
        return 'conflicting'
    if row['fee_charged'] == 'N':
        return 'conflicting' if lists_fee else 'no_fee'
    if says_free:
        return 'conflicting'
    if row['operated_by'] in CONCESSION_OPERATORS:
        return 'concession'
    if row['fee_type'] == 'STANDARD AMENITY FEE':
        return 'adventure_pass'
    if row['fee_type']:
        return 'other_fee'  # e.g. special recreation permit, expanded amenity fee
    return 'fee_unspecified'


def absolute_url(url):
    """Some INFRA portal links omit the scheme ("www.fs.usda.gov/...")."""
    if not url:
        return None
    url = url.strip()
    return url if re.match(r'^https?://', url) else 'https://' + url.lstrip('/')


def normalize(row):
    return {
        'id': row['site_cn'],
        'name': clean_name(row),
        'forest': FORESTS[row['managing_org'][:4]],
        'site_type': row['site_type'].title().replace('Ohv', 'OHV'),
        'fee_category': fee_category(row),
        'fee_type': row['fee_type'].capitalize() if row['fee_type'] else None,
        'fee_description': ' '.join((row['fee_description'] or '').split()) or None,
        'operated_by': row['operated_by'],
        'listed_closed': row['seasonal_operational_status'] == 'CLOSED',
        'restrooms': row['restroom_availability'],
        'official_url': absolute_url(row['usda_portal_url']),
        'lat': round(row['latitude'], 5),
        'lon': round(row['longitude'], 5),
    }


def km(a, b):
    lat1, lon1, lat2, lon2 = map(math.radians, (a['lat'], a['lon'], b['lat'], b['lon']))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 12742 * math.asin(math.sqrt(h))


GENERIC_WORDS = {'picnic', 'area', 'site', 'park', 'trailhead', 'day', 'use', 'the'}


def name_key(name):
    """'Switzer Park Picnic' -> 'switzer'; generic words and plurals drop out."""
    words = re.sub(r"[^a-z ]", '', name.lower().replace("'s", '')).split()
    return ' '.join(w.rstrip('s') for w in words if w not in GENERIC_WORDS)


def completeness(site):
    return sum(site[k] is not None for k in ('official_url', 'restrooms', 'fee_description'))


def dedupe(sites):
    """Collapse duplicate INFRA records for one place.

    Only records with the same distinctive name, type, fee classification and
    closed flag within 500 m merge. Fuzzy name matching merged distinct
    neighbours (West Fork Picnic Site and West Fork Fishing Access), so it is
    not used. The October 2026 pull had no such duplicates; this is a guard.
    """
    kept = []
    for site in sorted(sites, key=lambda s: -completeness(s)):
        duplicate = any(
            name_key(other['name']) == name_key(site['name'])
            and all(other[k] == site[k] for k in
                    ('forest', 'site_type', 'fee_category', 'listed_closed'))
            and km(other, site) < 0.5
            for other in kept
        )
        if not duplicate:
            kept.append(site)
    return sorted(kept, key=lambda s: (s['forest'], s['name']))


def main():
    rows = [r for r in fetch_sites() if r['site_type'] in DAY_USE_TYPES and r['latitude']]
    sites = dedupe([normalize(r) for r in rows])
    payload = {
        'source': 'USDA Forest Service, Recreation Sites (INFRA), EDW_RecInfraRecreationSites_02',
        'source_url': LAYER,
        'retrieved': date.today().isoformat(),
        'sites': sites,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n')
    counts = {}
    for site in sites:
        counts[site['fee_category']] = counts.get(site['fee_category'], 0) + 1
    print(f'{len(rows)} day-use records -> {len(sites)} sites after dedupe: {counts}')


if __name__ == '__main__':
    main()
