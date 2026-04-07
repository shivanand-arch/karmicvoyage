"""
Trakstar Hire API client — fetch openings, candidates, and resume files.
Supports both API key auth and cookie-based auth.
Includes rate-limit handling with exponential backoff.
"""

import time
import requests


MAX_RETRIES = 5
BASE_DELAY = 2  # seconds


def _request_with_retry(session, method, url, **kwargs):
    """Make an HTTP request with automatic retry on 429 rate limits."""
    for attempt in range(MAX_RETRIES):
        r = session.request(method, url, **kwargs)
        if r.status_code == 429:
            retry_after = int(r.headers.get("Retry-After", BASE_DELAY * (2 ** attempt)))
            time.sleep(retry_after)
            continue
        r.raise_for_status()
        return r
    # Final attempt — let it raise if it fails
    r = session.request(method, url, **kwargs)
    r.raise_for_status()
    return r


def create_session(subdomain, api_key=None, cookie=None):
    """Create an authenticated requests session for Trakstar."""
    base = f"https://{subdomain}.hire.trakstar.com"
    s = requests.Session()
    if api_key:
        s.auth = (api_key, "")
    elif cookie:
        for item in cookie.split(";"):
            if "=" in item:
                k, v = item.strip().split("=", 1)
                s.cookies.set(k, v)
    return s, base


def fetch_openings(session, base):
    """Fetch all job openings with pagination."""
    openings = []
    offset = 0
    while True:
        r = _request_with_retry(session, "GET", f"{base}/api/v1/openings/",
                                params={"limit": 50, "offset": offset})
        batch = r.json().get("objects", [])
        if not batch:
            break
        openings.extend(batch)
        offset += 50
        time.sleep(0.3)  # gentle pacing
    return openings


def fetch_candidates(session, base, opening_id, order="desc"):
    """Fetch all candidates for an opening with pagination and rate-limit handling."""
    cands = []
    offset = 0
    while True:
        params = {
            "openings": opening_id,
            "limit": 20,
            "offset": offset,
            "orderBy": "date_created",
            "order": order,
        }
        r = _request_with_retry(session, "GET", f"{base}/api/v2/candidate_filter/",
                                params=params)
        batch = r.json().get("objects", [])
        if not batch:
            break
        cands.extend(batch)
        offset += 20
        time.sleep(0.5)  # pace to avoid 429s
    return cands


def deduplicate(cands):
    """Remove duplicate candidates by email."""
    unique = {}
    for c in cands:
        email = (c.get("email") or "").lower()
        key = email if email else c["id"]
        if key not in unique:
            unique[key] = c
    return list(unique.values())


def get_unique_stages(cands):
    """Extract unique pipeline stage names from candidates."""
    stages = set()
    for c in cands:
        name = (c.get("current_stage") or {}).get("name", "")
        if not name:
            name = c.get("stage") or ""
        if name:
            stages.add(name)
    return sorted(stages)


def fetch_resume_bytes(session, base, candidate_id):
    """
    Fetch resume file for a single candidate.
    Returns (filename, bytes) or (None, None) if no resume.
    """
    r = _request_with_retry(session, "GET", f"{base}/api/v1/candidates/{candidate_id}/")
    d = r.json()
    res = d.get("resume")
    if not res:
        return None, None
    url = base + res["location"] + "?redirect=true"
    filename = res.get("filename", "resume.pdf")
    data = _request_with_retry(session, "GET", url).content
    time.sleep(0.3)  # pace resume downloads
    return filename, data
