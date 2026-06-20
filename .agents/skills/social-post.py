#!/usr/bin/env python3
"""
Zernio Social Media Posting Skill
Posts content to Jhonnatan's connected social media accounts via Zernio API.

Usage:
  python3 social-post.py --content "Your post text" [--platforms all|instagram|facebook] [--schedule "2026-06-21T09:00:00"]

Connected Accounts:
  facebook  → JF Web Studios     (ID: 6a36309f5f7d1751ab18ef8e)
  instagram → jhonnatan_ferrebus_ (ID: 6a3630655f7d1751ab18ee24)
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime

ZERNIO_API_KEY = os.environ.get("ZERNIO_API_KEY", "")
BASE_URL = "https://zernio.com/api/v1"
TIMEZONE = "America/Chicago"

ACCOUNTS = {
    "facebook": {
        "id": "6a36309f5f7d1751ab18ef8e",
        "name": "JF Web Studios (Facebook)",
        "platform": "facebook"
    },
    "instagram": {
        "id": "6a3630655f7d1751ab18ee24",
        "name": "jhonnatan_ferrebus_ (Instagram)",
        "platform": "instagram"
    }
}

def post_to_zernio(content, platforms_list, schedule_time=None, publish_now=True):
    if not ZERNIO_API_KEY:
        print("ERROR: ZERNIO_API_KEY not set")
        sys.exit(1)

    selected = []
    for p in platforms_list:
        if p in ACCOUNTS:
            selected.append({
                "platform": ACCOUNTS[p]["platform"],
                "accountId": ACCOUNTS[p]["id"]
            })

    if not selected:
        print("ERROR: No valid platforms selected")
        sys.exit(1)

    payload = {
        "content": content,
        "platforms": selected,
        "timezone": TIMEZONE
    }

    if schedule_time:
        payload["scheduledFor"] = schedule_time
        payload["publishNow"] = False
    else:
        payload["publishNow"] = publish_now

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/posts",
        data=data,
        headers={
            "Authorization": f"Bearer {ZERNIO_API_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            post = result.get("post", {})
            print(f"✅ Posted successfully!")
            print(f"Post ID: {post.get('_id', 'N/A')}")
            print(f"Status: {post.get('status', 'N/A')}")
            if schedule_time:
                print(f"Scheduled for: {schedule_time} CT")
            platforms_posted = [p["platform"] for p in selected]
            print(f"Platforms: {', '.join(platforms_posted)}")
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"❌ Error {e.code}: {body}")
        sys.exit(1)

def list_accounts():
    req = urllib.request.Request(
        f"{BASE_URL}/accounts",
        headers={"Authorization": f"Bearer {ZERNIO_API_KEY}"},
        method="GET"
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        accounts = result.get("accounts", [])
        print(f"Connected accounts ({len(accounts)}):")
        for a in accounts:
            print(f"  {a['platform']}: {a['displayName']} (ID: {a['_id']})")

def main():
    parser = argparse.ArgumentParser(description="Post to social media via Zernio")
    parser.add_argument("--content", type=str, help="Post content/caption")
    parser.add_argument("--platforms", type=str, default="all",
                        help="Platforms: all, instagram, facebook (comma-separated)")
    parser.add_argument("--schedule", type=str, default=None,
                        help="Schedule datetime ISO format e.g. 2026-06-21T09:00:00")
    parser.add_argument("--list-accounts", action="store_true",
                        help="List connected accounts")
    parser.add_argument("--draft", action="store_true",
                        help="Save as draft only")

    args = parser.parse_args()

    if args.list_accounts:
        list_accounts()
        return

    if not args.content:
        print("ERROR: --content is required")
        parser.print_help()
        sys.exit(1)

    if args.platforms == "all":
        platforms = list(ACCOUNTS.keys())
    else:
        platforms = [p.strip() for p in args.platforms.split(",")]

    publish_now = not args.draft and not args.schedule

    post_to_zernio(
        content=args.content,
        platforms_list=platforms,
        schedule_time=args.schedule,
        publish_now=publish_now
    )

if __name__ == "__main__":
    main()
