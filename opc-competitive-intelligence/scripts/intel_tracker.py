#!/usr/bin/env python3
"""
Competitive Intelligence Tracker — CLI tool for indexing, querying, and
summarizing competitive landscape analyses.

Usage:
    python3 intel_tracker.py <intelligence_dir> [--index|--status|--threats|--signals|--compare A B] [--json|--human]

Exit codes:
    0 — Success (no critical threats)
    1 — Critical threats detected or error
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def find_landscapes(base_dir: str) -> list:
    """Discover all landscape directories containing metadata.json."""
    landscapes = []
    base = Path(base_dir)
    if not base.exists():
        return landscapes

    for entry in sorted(base.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            meta_path = entry / "metadata.json"
            if meta_path.exists():
                try:
                    with open(meta_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    data["_dir"] = str(entry)
                    data["_meta_path"] = str(meta_path)
                    landscapes.append(data)
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Warning: Could not read {meta_path}: {e}", file=sys.stderr)
    return landscapes


def build_index(base_dir: str) -> dict:
    """Build INDEX.json with summaries of all landscapes."""
    landscapes = find_landscapes(base_dir)
    index = {
        "generated_at": datetime.now().isoformat(),
        "total_landscapes": len(landscapes),
        "landscapes": [],
    }

    for ls in landscapes:
        competitors = ls.get("competitors", [])
        threat_counts = {}
        for c in competitors:
            tl = c.get("threat_level", "unknown")
            threat_counts[tl] = threat_counts.get(tl, 0) + 1

        tier_counts = {}
        for c in competitors:
            t = c.get("tier", "unknown")
            tier_counts[t] = tier_counts.get(t, 0) + 1

        signals = ls.get("signals", [])
        high_signals = [s for s in signals if s.get("severity") == "high"]

        entry = {
            "landscape_id": ls.get("landscape_id", "unknown"),
            "landscape_name": ls.get("landscape_name", "unnamed"),
            "product_description": ls.get("product_description", ""),
            "market_category": ls.get("market", {}).get("category", "unknown"),
            "market_stage": ls.get("market", {}).get("market_stage", "unknown"),
            "status": ls.get("status", "unknown"),
            "competitor_count": len(competitors),
            "threat_counts": threat_counts,
            "tier_counts": tier_counts,
            "signal_count": len(signals),
            "high_severity_signals": len(high_signals),
            "created_at": ls.get("created_at", "unknown"),
            "updated_at": ls.get("updated_at"),
        }

        positioning = ls.get("positioning")
        if positioning:
            entry["differentiation_type"] = positioning.get("differentiation_type")
            entry["wedge_strategy"] = positioning.get("wedge_strategy")

        index["landscapes"].append(entry)

    # Write INDEX.json
    index_path = Path(base_dir) / "INDEX.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return index


def get_status_summary(landscapes: list) -> dict:
    """Generate a status summary across all landscapes."""
    summary = {
        "total": len(landscapes),
        "by_status": {},
        "by_market_stage": {},
        "total_competitors": 0,
        "total_signals": 0,
        "landscapes": [],
    }

    for ls in landscapes:
        status = ls.get("status", "unknown")
        summary["by_status"][status] = summary["by_status"].get(status, 0) + 1

        market_stage = ls.get("market", {}).get("market_stage", "unknown")
        summary["by_market_stage"][market_stage] = summary["by_market_stage"].get(market_stage, 0) + 1

        competitors = ls.get("competitors", [])
        signals = ls.get("signals", [])
        summary["total_competitors"] += len(competitors)
        summary["total_signals"] += len(signals)

        direct_threats = [
            c for c in competitors
            if c.get("tier") == "direct" and c.get("threat_level") in ("critical", "high")
        ]

        summary["landscapes"].append({
            "name": ls.get("landscape_name", "unnamed"),
            "id": ls.get("landscape_id", "unknown"),
            "status": status,
            "category": ls.get("market", {}).get("category", "unknown"),
            "competitors": len(competitors),
            "high_threats": len(direct_threats),
            "signals": len(signals),
            "updated": ls.get("updated_at") or ls.get("created_at", "unknown"),
        })

    return summary


def get_threat_summary(landscapes: list) -> dict:
    """Generate a threat matrix summary across all landscapes."""
    summary = {
        "has_critical": False,
        "total_threats": 0,
        "by_level": {"critical": 0, "high": 0, "medium": 0, "low": 0, "none": 0},
        "critical_threats": [],
        "high_threats": [],
        "threat_matrix_entries": 0,
    }

    for ls in landscapes:
        for c in ls.get("competitors", []):
            tl = c.get("threat_level", "none")
            if tl in summary["by_level"]:
                summary["by_level"][tl] += 1
            summary["total_threats"] += 1

            if tl == "critical":
                summary["has_critical"] = True
                summary["critical_threats"].append({
                    "landscape": ls.get("landscape_name", "unnamed"),
                    "competitor": c.get("name", "unknown"),
                    "tier": c.get("tier", "unknown"),
                    "overlap": c.get("overlap_score"),
                    "moat": c.get("moat_type"),
                })
            elif tl == "high":
                summary["high_threats"].append({
                    "landscape": ls.get("landscape_name", "unnamed"),
                    "competitor": c.get("name", "unknown"),
                    "tier": c.get("tier", "unknown"),
                    "overlap": c.get("overlap_score"),
                })

        summary["threat_matrix_entries"] += len(ls.get("threat_matrix", []))

    return summary


def get_signal_summary(landscapes: list) -> dict:
    """Get recent signals sorted by severity."""
    all_signals = []

    for ls in landscapes:
        for s in ls.get("signals", []):
            s_copy = dict(s)
            s_copy["landscape"] = ls.get("landscape_name", "unnamed")
            all_signals.append(s_copy)

    severity_order = {"high": 0, "medium": 1, "low": 2}
    all_signals.sort(key=lambda s: (severity_order.get(s.get("severity", "low"), 3), s.get("date", "")),
                     reverse=False)
    # Sort: high first, then by date descending within severity
    all_signals.sort(key=lambda s: (severity_order.get(s.get("severity", "low"), 3), ""),)

    return {
        "total": len(all_signals),
        "by_severity": {
            "high": len([s for s in all_signals if s.get("severity") == "high"]),
            "medium": len([s for s in all_signals if s.get("severity") == "medium"]),
            "low": len([s for s in all_signals if s.get("severity") == "low"]),
        },
        "signals": all_signals,
    }


def compare_competitors(landscapes: list, name_a: str, name_b: str) -> dict:
    """Side-by-side comparison of two competitors."""
    comp_a = None
    comp_b = None
    landscape_name = None

    for ls in landscapes:
        for c in ls.get("competitors", []):
            name_lower = c.get("name", "").lower()
            id_lower = c.get("id", "").lower()
            if name_lower == name_a.lower() or id_lower == name_a.lower():
                comp_a = c
                landscape_name = ls.get("landscape_name")
            if name_lower == name_b.lower() or id_lower == name_b.lower():
                comp_b = c
                if not landscape_name:
                    landscape_name = ls.get("landscape_name")

    if not comp_a:
        return {"error": f"Competitor '{name_a}' not found"}
    if not comp_b:
        return {"error": f"Competitor '{name_b}' not found"}

    fields = [
        "tier", "threat_level", "stage", "positioning", "target_audience",
        "pricing_model", "pricing_range", "moat_type", "overlap_score",
    ]

    comparison = {
        "landscape": landscape_name,
        "competitor_a": comp_a.get("name"),
        "competitor_b": comp_b.get("name"),
        "dimensions": {},
    }

    for field in fields:
        comparison["dimensions"][field] = {
            "a": comp_a.get(field),
            "b": comp_b.get(field),
        }

    comparison["strengths"] = {
        "a": comp_a.get("strengths", []),
        "b": comp_b.get("strengths", []),
    }
    comparison["weaknesses"] = {
        "a": comp_a.get("weaknesses", []),
        "b": comp_b.get("weaknesses", []),
    }

    return comparison


# --- Formatters ---

def format_status_human(summary: dict) -> str:
    """Format status summary as human-readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("COMPETITIVE INTELLIGENCE — STATUS DASHBOARD")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Total landscapes: {summary['total']}")
    lines.append(f"Total competitors tracked: {summary['total_competitors']}")
    lines.append(f"Total signals: {summary['total_signals']}")
    lines.append("")

    if summary["by_status"]:
        lines.append("By status:")
        for status, count in sorted(summary["by_status"].items()):
            lines.append(f"  {status}: {count}")
        lines.append("")

    if summary["by_market_stage"]:
        lines.append("By market stage:")
        for stage, count in sorted(summary["by_market_stage"].items()):
            lines.append(f"  {stage}: {count}")
        lines.append("")

    if summary["landscapes"]:
        lines.append("-" * 60)
        lines.append(f"{'Name':<25} {'Category':<20} {'Comp':<5} {'Threats':<8} {'Signals':<8}")
        lines.append("-" * 60)
        for ls in summary["landscapes"]:
            lines.append(
                f"{ls['name']:<25} {ls['category']:<20} {ls['competitors']:<5} "
                f"{ls['high_threats']:<8} {ls['signals']:<8}"
            )
    lines.append("")
    return "\n".join(lines)


def format_threats_human(summary: dict) -> str:
    """Format threat summary as human-readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("THREAT MATRIX SUMMARY")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Total competitors assessed: {summary['total_threats']}")
    lines.append("")

    for level in ["critical", "high", "medium", "low", "none"]:
        count = summary["by_level"].get(level, 0)
        marker = " !!!" if level == "critical" and count > 0 else ""
        lines.append(f"  {level.upper()}: {count}{marker}")
    lines.append("")

    if summary["critical_threats"]:
        lines.append("!!! CRITICAL THREATS !!!")
        lines.append("-" * 40)
        for t in summary["critical_threats"]:
            lines.append(f"  [{t['landscape']}] {t['competitor']} (tier: {t['tier']}, overlap: {t['overlap']})")
        lines.append("")

    if summary["high_threats"]:
        lines.append("HIGH THREATS:")
        lines.append("-" * 40)
        for t in summary["high_threats"]:
            lines.append(f"  [{t['landscape']}] {t['competitor']} (tier: {t['tier']}, overlap: {t['overlap']})")
        lines.append("")

    return "\n".join(lines)


def format_signals_human(summary: dict) -> str:
    """Format signal summary as human-readable text."""
    lines = []
    lines.append("=" * 60)
    lines.append("INTELLIGENCE SIGNALS")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"Total signals: {summary['total']}")
    lines.append(f"  High: {summary['by_severity']['high']} | "
                 f"Medium: {summary['by_severity']['medium']} | "
                 f"Low: {summary['by_severity']['low']}")
    lines.append("")

    if summary["signals"]:
        lines.append("-" * 60)
        for s in summary["signals"]:
            sev = s.get("severity", "?").upper()
            date = s.get("date", "????-??-??")
            stype = s.get("signal_type", "unknown")
            desc = s.get("description", "")
            landscape = s.get("landscape", "")
            comp = s.get("competitor_id", "market")
            lines.append(f"  [{sev}] {date} — {stype} — {comp}")
            lines.append(f"         {desc}")
            if s.get("implication"):
                lines.append(f"         → {s['implication']}")
            if s.get("action_needed"):
                lines.append(f"         Action: {s['action_needed']}")
            lines.append("")

    return "\n".join(lines)


def format_compare_human(comparison: dict) -> str:
    """Format competitor comparison as human-readable text."""
    if "error" in comparison:
        return f"Error: {comparison['error']}"

    a_name = comparison["competitor_a"]
    b_name = comparison["competitor_b"]

    lines = []
    lines.append("=" * 60)
    lines.append(f"COMPARISON: {a_name} vs {b_name}")
    lines.append(f"Landscape: {comparison['landscape']}")
    lines.append("=" * 60)
    lines.append("")

    lines.append(f"{'Dimension':<20} {a_name:<20} {b_name:<20}")
    lines.append("-" * 60)
    for dim, vals in comparison["dimensions"].items():
        a_val = str(vals["a"]) if vals["a"] is not None else "—"
        b_val = str(vals["b"]) if vals["b"] is not None else "—"
        lines.append(f"{dim:<20} {a_val:<20} {b_val:<20}")
    lines.append("")

    lines.append(f"Strengths ({a_name}):")
    for s in comparison["strengths"]["a"]:
        lines.append(f"  + {s}")
    lines.append(f"Strengths ({b_name}):")
    for s in comparison["strengths"]["b"]:
        lines.append(f"  + {s}")
    lines.append("")

    lines.append(f"Weaknesses ({a_name}):")
    for w in comparison["weaknesses"]["a"]:
        lines.append(f"  - {w}")
    lines.append(f"Weaknesses ({b_name}):")
    for w in comparison["weaknesses"]["b"]:
        lines.append(f"  - {w}")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Competitive Intelligence Tracker — index, query, and summarize competitive landscapes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 intel_tracker.py intelligence/ --index
  python3 intel_tracker.py intelligence/ --status --human
  python3 intel_tracker.py intelligence/ --threats --json
  python3 intel_tracker.py intelligence/ --signals
  python3 intel_tracker.py intelligence/ --compare "Notion" "Coda"
        """,
    )

    parser.add_argument("intelligence_dir", help="Path to the intelligence directory")
    parser.add_argument("--index", action="store_true", help="Build/rebuild INDEX.json")
    parser.add_argument("--status", action="store_true", help="Show landscape status summary")
    parser.add_argument("--threats", action="store_true", help="Show threat matrix summary")
    parser.add_argument("--signals", action="store_true", help="Show recent intelligence signals")
    parser.add_argument("--compare", nargs=2, metavar=("A", "B"), help="Compare two competitors side-by-side")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--human", action="store_true", help="Output in human-readable format (default)")

    args = parser.parse_args()

    if not os.path.isdir(args.intelligence_dir):
        print(f"Error: Directory not found: {args.intelligence_dir}", file=sys.stderr)
        sys.exit(1)

    # Default to --status if no action specified
    if not any([args.index, args.status, args.threats, args.signals, args.compare]):
        args.status = True

    # Default to human output
    if not args.json:
        args.human = True

    has_critical = False

    if args.index:
        index = build_index(args.intelligence_dir)
        if args.json:
            print(json.dumps(index, indent=2, ensure_ascii=False))
        else:
            print(f"Index built: {index['total_landscapes']} landscapes indexed.")
            print(f"Written to: {os.path.join(args.intelligence_dir, 'INDEX.json')}")

    if args.status:
        landscapes = find_landscapes(args.intelligence_dir)
        summary = get_status_summary(landscapes)
        if args.json:
            print(json.dumps(summary, indent=2, ensure_ascii=False))
        else:
            print(format_status_human(summary))

    if args.threats:
        landscapes = find_landscapes(args.intelligence_dir)
        summary = get_threat_summary(landscapes)
        has_critical = summary["has_critical"]
        if args.json:
            print(json.dumps(summary, indent=2, ensure_ascii=False))
        else:
            print(format_threats_human(summary))

    if args.signals:
        landscapes = find_landscapes(args.intelligence_dir)
        summary = get_signal_summary(landscapes)
        if args.json:
            print(json.dumps(summary, indent=2, ensure_ascii=False))
        else:
            print(format_signals_human(summary))

    if args.compare:
        landscapes = find_landscapes(args.intelligence_dir)
        result = compare_competitors(landscapes, args.compare[0], args.compare[1])
        if "error" in result:
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_compare_human(result))

    sys.exit(1 if has_critical else 0)


if __name__ == "__main__":
    main()
