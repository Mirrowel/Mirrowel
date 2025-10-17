import os
import sys
import json
import requests
from typing import List, Tuple

GITHUB_API = "https://api.github.com"

def parse_repos(raw: str) -> List[str]:
    if not raw:
        return []
    # Allow spaces, newlines, or commas
    parts = []
    for token in raw.replace(",", " ").split():
        token = token.strip()
        if token:
            parts.append(token)
    return parts

def gh_get(url: str, token: str, params=None) -> requests.Response:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "release-downloads-badge"
    }
    r = requests.get(url, headers=headers, params=params or {}, timeout=45)
    if r.status_code == 404:
        # Treat as empty; return a synthetic empty response
        class Dummy:
            def json(self): return []
            status_code = 404
            def raise_for_status(self): pass
        return Dummy()  # type: ignore
    r.raise_for_status()
    return r

def repo_total_downloads(owner: str, repo: str, include_prereleases: bool, token: str) -> int:
    total = 0
    page = 1
    while True:
        resp = gh_get(f"{GITHUB_API}/repos/{owner}/{repo}/releases", token, params={"per_page": 100, "page": page})
        releases = resp.json()
        if not releases:
            break
        for rel in releases:
            if not include_prereleases and rel.get("prerelease"):
                continue
            for asset in rel.get("assets", []):
                cnt = asset.get("download_count")
                if isinstance(cnt, int):
                    total += cnt
                else:
                    try:
                        total += int(cnt or 0)
                    except Exception:
                        pass
        page += 1
    return total

def compute_totals(repos: List[str], include_prereleases: bool, token: str) -> Tuple[int, dict]:
    grand_total = 0
    per_repo = {}
    for full in repos:
        if "/" not in full:
            print(f"Skipping invalid repo ref: {full}", file=sys.stderr)
            continue
        owner, repo = full.split("/", 1)
        try:
            total = repo_total_downloads(owner, repo, include_prereleases, token)
        except requests.HTTPError as e:
            print(f"HTTP error for {full}: {e}", file=sys.stderr)
            total = 0
        except requests.RequestException as e:
            print(f"Network error for {full}: {e}", file=sys.stderr)
            total = 0
        per_repo[full] = total
        grand_total += total
    return grand_total, per_repo

def write_repo_badge_json(path: str, label: str, message: str, color: str) -> None:
    data = {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color,
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def publish_gist(gist_id: str, filename: str, content: str, token: str) -> None:
    url = f"{GITHUB_API}/gists/{gist_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "release-downloads-badge"
    }
    body = {"files": {filename: {"content": content}}}
    r = requests.patch(url, headers=headers, json=body, timeout=45)
    r.raise_for_status()

def main() -> int:
    repos = parse_repos(os.environ.get("REPOS", ""))
    if not repos:
        print("REPOS is empty; nothing to compute.", file=sys.stderr)
        return 1

    include_prereleases = os.environ.get("INCLUDE_PRERELEASES", "false").lower() == "true"
    gh_token = os.environ.get("GITHUB_TOKEN") or ""
    if not gh_token:
        print("GITHUB_TOKEN not set.", file=sys.stderr)
        return 1

    # Outputs
    repo_badge_enabled = os.environ.get("REPO_BADGE_ENABLED", "true").lower() == "true"
    badge_path = os.environ.get("BADGE_JSON_PATH", "badges/downloads-total.json")
    badge_label = os.environ.get("BADGE_LABEL", "release downloads")
    badge_color = os.environ.get("BADGE_COLOR", "blue")

    gist_badge_enabled = os.environ.get("GIST_BADGE_ENABLED", "false").lower() == "true"
    gist_id = os.environ.get("GIST_ID", "").strip()
    gist_filename = os.environ.get("GIST_FILENAME", "downloads-total.json").strip()
    gist_token = os.environ.get("GIST_TOKEN", "").strip()

    grand_total, per_repo = compute_totals(repos, include_prereleases, gh_token)

    print("Per-repo downloads:")
    for k, v in per_repo.items():
        print(f"- {k}: {v}")
    print(f"Grand total: {grand_total}")

    # Prepare Shields endpoint JSON string
    endpoint_json_str = json.dumps({
        "schemaVersion": 1,
        "label": badge_label,
        "message": f"{grand_total:,}",
        "color": badge_color,
    }, ensure_ascii=False)

    # Write to repo (Option B)
    if repo_badge_enabled:
        write_repo_badge_json(badge_path, badge_label, f"{grand_total:,}", badge_color)
        print(f"Wrote repo badge JSON to: {badge_path}")

    # Publish to Gist (Option E)
    if gist_badge_enabled:
        if not gist_id:
            print("GIST_BADGE_ENABLED is true but GIST_ID is empty.", file=sys.stderr)
            return 1
        if not gist_token:
            print("GIST_BADGE_ENABLED is true but GIST_TOKEN is empty.", file=sys.stderr)
            return 1
        publish_gist(gist_id, gist_filename, endpoint_json_str, gist_token)
        print(f"Updated Gist {gist_id} file: {gist_filename}")

    return 0

if __name__ == "__main__":
    sys.exit(main())