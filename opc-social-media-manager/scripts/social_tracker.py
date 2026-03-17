#!/usr/bin/env python3
"""
Social Media Tracker — CLI tool for indexing, querying, and summarizing
social media content, calendar, engagement, and performance data.

Usage:
    python3 social_tracker.py <social_dir> [--index|--status|--calendar|--backlog|--review|--engagement] [--json|--human]

Exit codes:
    0 — Success
    1 — Error or issues detected
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path


def find_profiles(base_dir: str) -> list:
    """Discover all brand profile directories containing metadata.json."""
    profiles = []
    base = Path(base_dir)
    if not base.exists():
        return profiles

    for entry in sorted(base.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            meta_path = entry / "metadata.json"
            if meta_path.exists():
                try:
                    with open(meta_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    data["_dir"] = str(entry)
                    data["_meta_path"] = str(meta_path)
                    profiles.append(data)
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Warning: Could not read {meta_path}: {e}", file=sys.stderr)
    return profiles


def build_index(base_dir: str) -> dict:
    """Build INDEX.json with summaries of all brand profiles."""
    profiles = find_profiles(base_dir)
    index = {
        "generated_at": datetime.now().isoformat(),
        "total_profiles": len(profiles),
        "profiles": [],
    }

    for p in profiles:
        content_items = p.get("content_items", [])
        topic_backlog = p.get("topic_backlog", [])
        reviews = p.get("reviews", [])

        status_counts = {}
        for item in content_items:
            s = item.get("status", "unknown")
            status_counts[s] = status_counts.get(s, 0) + 1

        platform_counts = {}
        for item in content_items:
            plat = item.get("platform", "unknown")
            platform_counts[plat] = platform_counts.get(plat, 0) + 1

        backlog_counts = {}
        for t in topic_backlog:
            s = t.get("status", "unknown")
            backlog_counts[s] = backlog_counts.get(s, 0) + 1

        entry = {
            "profile_id": p.get("profile_id", "unknown"),
            "brand_name": p.get("brand_name", "unnamed"),
            "status": p.get("status", "unknown"),
            "platforms_active": len([
                pl for pl in p.get("platform_strategy", {}).get("platforms", [])
                if pl.get("active")
            ]),
            "content_pillars": len(p.get("content_pillars", [])),
            "total_content_items": len(content_items),
            "content_by_status": status_counts,
            "content_by_platform": platform_counts,
            "backlog_size": len(topic_backlog),
            "backlog_by_status": backlog_counts,
            "reviews_count": len(reviews),
            "pending_replies": len([
                r for r in p.get("engagement", {}).get("reply_queue", [])
                if r.get("status") == "pending"
            ]),
            "created_at": p.get("created_at", "unknown"),
            "updated_at": p.get("updated_at"),
        }

        index["profiles"].append(entry)

    index_path = Path(base_dir) / "INDEX.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return index


def get_status_summary(profiles: list) -> dict:
    """Generate an overall status summary."""
    summary = {
        "total_profiles": len(profiles),
        "total_content_items": 0,
        "total_published": 0,
        "total_backlog": 0,
        "total_pending_replies": 0,
        "by_status": {},
        "profiles": [],
    }

    for p in profiles:
        status = p.get("status", "unknown")
        summary["by_status"][status] = summary["by_status"].get(status, 0) + 1

        content_items = p.get("content_items", [])
        published = [c for c in content_items if c.get("status") == "published"]
        backlog = p.get("topic_backlog", [])
        pending = [
            r for r in p.get("engagement", {}).get("reply_queue", [])
            if r.get("status") == "pending"
        ]

        summary["total_content_items"] += len(content_items)
        summary["total_published"] += len(published)
        summary["total_backlog"] += len(backlog)
        summary["total_pending_replies"] += len(pending)

        summary["profiles"].append({
            "name": p.get("brand_name", "unnamed"),
            "id": p.get("profile_id", "unknown"),
            "status": status,
            "published": len(published),
            "drafts": len([c for c in content_items if c.get("status") == "draft"]),
            "backlog": len(backlog),
            "pending_replies": len(pending),
            "updated": p.get("updated_at") or p.get("created_at", "unknown"),
        })

    return summary


def get_calendar_summary(profiles: list) -> dict:
    """Get calendar and scheduling status."""
    results = []

    for p in profiles:
        calendar = p.get("calendar", {})
        content_items = p.get("content_items", [])
        slots = calendar.get("weekly_slots", [])

        filled = len([s for s in slots if s.get("content_id")])
        total = len(slots)

        scheduled = [c for c in content_items if c.get("status") == "scheduled"]
        ready = [c for c in content_items if c.get("status") == "ready"]

        results.append({
            "brand": p.get("brand_name", "unnamed"),
            "current_week": calendar.get("current_week", "not set"),
            "slots_filled": filled,
            "slots_total": total,
            "fill_rate": round(filled / total * 100) if total > 0 else 0,
            "scheduled_count": len(scheduled),
            "ready_count": len(ready),
            "series": [
                {"name": s.get("name"), "frequency": s.get("frequency"), "episodes": s.get("episode_count", 0)}
                for s in calendar.get("series", [])
            ],
        })

    return {"calendars": results}


def get_backlog_summary(profiles: list) -> dict:
    """Get topic backlog status."""
    results = []

    for p in profiles:
        backlog = p.get("topic_backlog", [])

        by_priority = {"high": 0, "medium": 0, "low": 0}
        by_status = {"idea": 0, "planned": 0, "drafted": 0, "published": 0, "recycled": 0}
        by_pillar = {}

        for t in backlog:
            pri = t.get("priority", "medium")
            if pri in by_priority:
                by_priority[pri] += 1

            st = t.get("status", "idea")
            if st in by_status:
                by_status[st] += 1

            pillar = t.get("pillar_id", "unassigned")
            by_pillar[pillar] = by_pillar.get(pillar, 0) + 1

        high_pri_topics = [
            {"topic": t.get("topic"), "pillar": t.get("pillar_id"), "status": t.get("status")}
            for t in backlog
            if t.get("priority") == "high" and t.get("status") in ("idea", "planned")
        ]

        results.append({
            "brand": p.get("brand_name", "unnamed"),
            "total_topics": len(backlog),
            "by_priority": by_priority,
            "by_status": by_status,
            "by_pillar": by_pillar,
            "high_priority_ready": high_pri_topics[:10],
        })

    return {"backlogs": results}


def get_review_summary(profiles: list) -> dict:
    """Get latest content review data."""
    results = []

    for p in profiles:
        reviews = p.get("reviews", [])
        if not reviews:
            results.append({
                "brand": p.get("brand_name", "unnamed"),
                "has_reviews": False,
            })
            continue

        latest = reviews[-1]
        results.append({
            "brand": p.get("brand_name", "unnamed"),
            "has_reviews": True,
            "latest_week": latest.get("week"),
            "posts_published": latest.get("posts_published", 0),
            "total_impressions": latest.get("total_impressions"),
            "avg_engagement_rate": latest.get("avg_engagement_rate"),
            "effective_patterns": latest.get("effective_patterns", []),
            "ineffective_patterns": latest.get("ineffective_patterns", []),
            "recommendations": latest.get("next_week_recommendations", []),
        })

    return {"reviews": results}


def get_engagement_summary(profiles: list) -> dict:
    """Get engagement queue status."""
    results = []

    for p in profiles:
        engagement = p.get("engagement", {})
        queue = engagement.get("reply_queue", [])
        contacts = engagement.get("high_value_contacts", [])

        pending = [r for r in queue if r.get("status") == "pending"]
        by_priority = {"urgent": 0, "high": 0, "medium": 0, "low": 0}
        for r in pending:
            pri = r.get("priority", "medium")
            if pri in by_priority:
                by_priority[pri] += 1

        by_tier = {}
        for r in pending:
            tier = r.get("from_tier", "general")
            by_tier[tier] = by_tier.get(tier, 0) + 1

        content_opps = [
            r.get("content_opportunity")
            for r in queue
            if r.get("content_opportunity")
        ]

        results.append({
            "brand": p.get("brand_name", "unnamed"),
            "pending_total": len(pending),
            "by_priority": by_priority,
            "by_tier": by_tier,
            "high_value_contacts": len(contacts),
            "content_opportunities": content_opps[:5],
            "urgent_items": [
                {"from": r.get("from"), "type": r.get("type"), "platform": r.get("platform"), "context": r.get("context")}
                for r in pending if r.get("priority") == "urgent"
            ],
        })

    return {"engagement": results}


# --- Formatters ---

def format_status_human(summary: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("SOCIAL MEDIA MANAGER — STATUS DASHBOARD")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Total profiles: {summary['total_profiles']}")
    lines.append(f"Total published: {summary['total_published']}")
    lines.append(f"Total in backlog: {summary['total_backlog']}")
    lines.append(f"Pending replies: {summary['total_pending_replies']}")
    lines.append("")

    if summary["profiles"]:
        lines.append("-" * 60)
        lines.append(f"{'Brand':<20} {'Status':<10} {'Published':<10} {'Drafts':<8} {'Backlog':<8} {'Replies':<8}")
        lines.append("-" * 60)
        for p in summary["profiles"]:
            lines.append(
                f"{p['name']:<20} {p['status']:<10} {p['published']:<10} "
                f"{p['drafts']:<8} {p['backlog']:<8} {p['pending_replies']:<8}"
            )
    lines.append("")
    return "\n".join(lines)


def format_calendar_human(data: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("CONTENT CALENDAR STATUS")
    lines.append("=" * 60)

    for cal in data["calendars"]:
        lines.append("")
        lines.append(f"Brand: {cal['brand']}")
        lines.append(f"Week: {cal['current_week']}")
        lines.append(f"Slots filled: {cal['slots_filled']}/{cal['slots_total']} ({cal['fill_rate']}%)")
        lines.append(f"Scheduled: {cal['scheduled_count']} | Ready: {cal['ready_count']}")

        if cal["series"]:
            lines.append("Series:")
            for s in cal["series"]:
                lines.append(f"  - {s['name']} ({s['frequency']}, {s['episodes']} episodes)")
    lines.append("")
    return "\n".join(lines)


def format_backlog_human(data: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("TOPIC BACKLOG")
    lines.append("=" * 60)

    for bl in data["backlogs"]:
        lines.append("")
        lines.append(f"Brand: {bl['brand']}")
        lines.append(f"Total topics: {bl['total_topics']}")
        lines.append(f"  High: {bl['by_priority']['high']} | Medium: {bl['by_priority']['medium']} | Low: {bl['by_priority']['low']}")
        lines.append("")

        if bl["by_pillar"]:
            lines.append("By pillar:")
            for pillar, count in sorted(bl["by_pillar"].items()):
                lines.append(f"  {pillar}: {count}")
            lines.append("")

        if bl["high_priority_ready"]:
            lines.append("High priority (ready to draft):")
            for t in bl["high_priority_ready"]:
                lines.append(f"  - [{t['status']}] {t['topic']} ({t['pillar']})")

    lines.append("")
    return "\n".join(lines)


def format_review_human(data: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("CONTENT REVIEW — LATEST")
    lines.append("=" * 60)

    for r in data["reviews"]:
        lines.append("")
        lines.append(f"Brand: {r['brand']}")
        if not r["has_reviews"]:
            lines.append("  No reviews yet.")
            continue

        lines.append(f"Week: {r['latest_week']}")
        lines.append(f"Posts: {r['posts_published']} | Impressions: {r.get('total_impressions', 'N/A')} | Eng Rate: {r.get('avg_engagement_rate', 'N/A')}%")

        if r["effective_patterns"]:
            lines.append("What worked:")
            for p in r["effective_patterns"]:
                lines.append(f"  ✅ {p}")

        if r["ineffective_patterns"]:
            lines.append("What didn't work:")
            for p in r["ineffective_patterns"]:
                lines.append(f"  ❌ {p}")

        if r["recommendations"]:
            lines.append("Next week:")
            for rec in r["recommendations"]:
                lines.append(f"  → {rec}")

    lines.append("")
    return "\n".join(lines)


def format_engagement_human(data: dict) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("ENGAGEMENT QUEUE")
    lines.append("=" * 60)

    for e in data["engagement"]:
        lines.append("")
        lines.append(f"Brand: {e['brand']}")
        lines.append(f"Pending: {e['pending_total']}")
        lines.append(f"  Urgent: {e['by_priority']['urgent']} | High: {e['by_priority']['high']} | Medium: {e['by_priority']['medium']} | Low: {e['by_priority']['low']}")
        lines.append(f"High-value contacts: {e['high_value_contacts']}")

        if e["urgent_items"]:
            lines.append("")
            lines.append("!!! URGENT !!!")
            for item in e["urgent_items"]:
                lines.append(f"  [{item['platform']}] {item['from']} ({item['type']}): {item.get('context', '')[:60]}...")

        if e["content_opportunities"]:
            lines.append("")
            lines.append("Content opportunities from audience:")
            for opp in e["content_opportunities"]:
                lines.append(f"  💡 {opp}")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Social Media Tracker — index, query, and summarize social media content and engagement.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 social_tracker.py social/ --index
  python3 social_tracker.py social/ --status --human
  python3 social_tracker.py social/ --calendar
  python3 social_tracker.py social/ --backlog --json
  python3 social_tracker.py social/ --review
  python3 social_tracker.py social/ --engagement
        """,
    )

    parser.add_argument("social_dir", help="Path to the social media directory")
    parser.add_argument("--index", action="store_true", help="Build/rebuild INDEX.json")
    parser.add_argument("--status", action="store_true", help="Show overall status dashboard")
    parser.add_argument("--calendar", action="store_true", help="Show content calendar status")
    parser.add_argument("--backlog", action="store_true", help="Show topic backlog")
    parser.add_argument("--review", action="store_true", help="Show latest content review")
    parser.add_argument("--engagement", action="store_true", help="Show engagement queue")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--human", action="store_true", help="Output in human-readable format (default)")

    args = parser.parse_args()

    if not os.path.isdir(args.social_dir):
        print(f"Error: Directory not found: {args.social_dir}", file=sys.stderr)
        sys.exit(1)

    if not any([args.index, args.status, args.calendar, args.backlog, args.review, args.engagement]):
        args.status = True

    if not args.json:
        args.human = True

    if args.index:
        index = build_index(args.social_dir)
        if args.json:
            print(json.dumps(index, indent=2, ensure_ascii=False))
        else:
            print(f"Index built: {index['total_profiles']} profiles indexed.")
            print(f"Written to: {os.path.join(args.social_dir, 'INDEX.json')}")

    if args.status:
        profiles = find_profiles(args.social_dir)
        summary = get_status_summary(profiles)
        if args.json:
            print(json.dumps(summary, indent=2, ensure_ascii=False))
        else:
            print(format_status_human(summary))

    if args.calendar:
        profiles = find_profiles(args.social_dir)
        data = get_calendar_summary(profiles)
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(format_calendar_human(data))

    if args.backlog:
        profiles = find_profiles(args.social_dir)
        data = get_backlog_summary(profiles)
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(format_backlog_human(data))

    if args.review:
        profiles = find_profiles(args.social_dir)
        data = get_review_summary(profiles)
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(format_review_human(data))

    if args.engagement:
        profiles = find_profiles(args.social_dir)
        data = get_engagement_summary(profiles)
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(format_engagement_human(data))

    sys.exit(0)


if __name__ == "__main__":
    main()
