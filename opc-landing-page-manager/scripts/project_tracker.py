#!/usr/bin/env python3
"""
Landing page project tracker for opc-landing-page-manager.

Manages the project index, tracks versions, and provides project status.

Usage:
    python3 project_tracker.py [pages_dir]
    python3 project_tracker.py --index [pages_dir]
    python3 project_tracker.py --status [pages_dir]
    python3 project_tracker.py --list [pages_dir]
    python3 project_tracker.py --versions PROJECT_ID [pages_dir]
    python3 project_tracker.py --json [pages_dir]

Options:
    --index         Rebuild INDEX.json from project directories
    --status        Show status summary of all projects
    --list          List all projects (one per line)
    --versions ID   Show version history for a project
    --json          Output as JSON instead of human-readable
    pages_dir       Path to landing-pages directory (default: ./landing-pages)

Exit codes:
    0   Success
    1   Error

Dependencies: Python 3.8+ stdlib only
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path


def find_projects(pages_dir: Path) -> list:
    """Find all project directories containing metadata.json."""
    projects = []
    if not pages_dir.is_dir():
        return projects

    for d in sorted(pages_dir.iterdir()):
        if not d.is_dir():
            continue
        if d.name.startswith('.') or d.name == 'INDEX.json':
            continue

        meta_path = d / 'metadata.json'
        if meta_path.is_file():
            try:
                with open(meta_path, 'r') as f:
                    meta = json.load(f)
                meta['_dir'] = str(d)
                projects.append(meta)
            except (json.JSONDecodeError, OSError) as e:
                print(f"Warning: Could not read {meta_path}: {e}", file=sys.stderr)
        else:
            # Check for versioned subdirectories
            for vd in sorted(d.iterdir()):
                if vd.is_dir() and (vd / 'metadata.json').is_file():
                    try:
                        with open(vd / 'metadata.json', 'r') as f:
                            meta = json.load(f)
                        meta['_dir'] = str(vd)
                        projects.append(meta)
                    except (json.JSONDecodeError, OSError) as e:
                        print(f"Warning: Could not read {vd / 'metadata.json'}: {e}",
                              file=sys.stderr)

    return projects


def build_index(pages_dir: Path) -> dict:
    """Build INDEX.json from all project metadata."""
    projects = find_projects(pages_dir)

    # Deduplicate: keep latest version per project_id
    latest = {}
    for p in projects:
        pid = p.get('project_id', '')
        version = p.get('version', 1)
        if pid not in latest or version > latest[pid].get('version', 1):
            latest[pid] = p

    index = {
        "generated_at": date.today().isoformat(),
        "total_projects": len(latest),
        "projects": []
    }

    status_counts = {}
    for pid in sorted(latest.keys()):
        p = latest[pid]
        status = p.get('status', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1

        entry = {
            "project_id": pid,
            "product_name": p.get('product_name', ''),
            "status": status,
            "version": p.get('version', 1),
            "created_at": p.get('created_at', ''),
            "updated_at": p.get('updated_at', ''),
            "conversion_goal": p.get('strategy', {}).get('conversion_goal', ''),
            "product_type": p.get('strategy', {}).get('product_type', ''),
            "directory": p.get('_dir', '')
        }

        # Include variant count
        variants = p.get('variants', [])
        if variants:
            entry["variant_count"] = len(variants)

        index["projects"].append(entry)

    index["status_summary"] = status_counts

    # Write INDEX.json
    index_path = pages_dir / 'INDEX.json'
    # Remove _dir from projects before writing
    for proj in index["projects"]:
        proj.pop('_dir', None)

    with open(index_path, 'w') as f:
        json.dump(index, f, indent=2)

    return index


def get_status_summary(pages_dir: Path) -> dict:
    """Get a status summary of all projects."""
    projects = find_projects(pages_dir)

    # Deduplicate by project_id
    latest = {}
    for p in projects:
        pid = p.get('project_id', '')
        version = p.get('version', 1)
        if pid not in latest or version > latest[pid].get('version', 1):
            latest[pid] = p

    summary = {
        "total": len(latest),
        "by_status": {},
        "projects": []
    }

    for pid in sorted(latest.keys()):
        p = latest[pid]
        status = p.get('status', 'unknown')
        summary["by_status"][status] = summary["by_status"].get(status, 0) + 1
        summary["projects"].append({
            "project_id": pid,
            "product_name": p.get('product_name', ''),
            "status": status,
            "version": p.get('version', 1),
            "updated_at": p.get('updated_at', p.get('created_at', ''))
        })

    return summary


def get_versions(pages_dir: Path, project_id: str) -> list:
    """Get all versions of a project."""
    projects = find_projects(pages_dir)
    versions = [p for p in projects if p.get('project_id') == project_id]
    versions.sort(key=lambda x: x.get('version', 1))
    return versions


def format_status_human(summary: dict) -> str:
    """Format status summary for human reading."""
    lines = []
    lines.append(f"Landing Page Projects: {summary['total']} total")
    lines.append("")

    if summary["by_status"]:
        lines.append("By Status:")
        status_order = ["strategy", "copy", "design", "build", "review", "published", "archived"]
        for status in status_order:
            count = summary["by_status"].get(status, 0)
            if count > 0:
                lines.append(f"  {status}: {count}")

    lines.append("")
    lines.append("Projects:")
    for p in summary["projects"]:
        version_str = f"v{p['version']}" if p.get('version', 1) > 1 else ""
        updated = f" (updated {p['updated_at']})" if p.get('updated_at') else ""
        lines.append(
            f"  [{p['status']:10s}] {p['product_name']}"
            f" {version_str}{updated}"
        )

    return "\n".join(lines)


def format_versions_human(versions: list, project_id: str) -> str:
    """Format version history for human reading."""
    if not versions:
        return f"No versions found for project: {project_id}"

    lines = [f"Version history for: {project_id}", ""]
    for v in versions:
        status = v.get('status', 'unknown')
        created = v.get('created_at', '')
        updated = v.get('updated_at', '')
        directory = v.get('_dir', '')
        lines.append(
            f"  v{v.get('version', 1):3d}  [{status:10s}]  "
            f"created: {created}  updated: {updated}"
        )
        if directory:
            lines.append(f"         dir: {directory}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Landing page project tracker."
    )
    parser.add_argument(
        'pages_dir',
        nargs='?',
        default='./landing-pages',
        help='Path to landing-pages directory (default: ./landing-pages)'
    )
    parser.add_argument(
        '--index',
        action='store_true',
        help='Rebuild INDEX.json from project directories'
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help='Show status summary of all projects'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List all projects (one per line)'
    )
    parser.add_argument(
        '--versions',
        metavar='PROJECT_ID',
        help='Show version history for a project'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()
    pages_dir = Path(args.pages_dir)

    if not pages_dir.is_dir():
        if args.json:
            print(json.dumps({"error": f"Directory not found: {pages_dir}"}))
        else:
            print(f"Directory not found: {pages_dir}", file=sys.stderr)
            print("No landing page projects found. Create your first project to get started.")
        sys.exit(0)

    try:
        if args.index:
            index = build_index(pages_dir)
            if args.json:
                print(json.dumps(index, indent=2))
            else:
                print(f"Index rebuilt: {index['total_projects']} projects indexed.")

        elif args.versions:
            versions = get_versions(pages_dir, args.versions)
            if args.json:
                # Remove _dir for clean output
                clean = [{k: v for k, v in v_item.items() if k != '_dir'}
                         for v_item in versions]
                print(json.dumps(clean, indent=2))
            else:
                print(format_versions_human(versions, args.versions))

        elif args.list:
            projects = find_projects(pages_dir)
            # Deduplicate
            seen = {}
            for p in projects:
                pid = p.get('project_id', '')
                version = p.get('version', 1)
                if pid not in seen or version > seen[pid].get('version', 1):
                    seen[pid] = p

            if args.json:
                result = [{"project_id": pid, "product_name": p.get('product_name', '')}
                          for pid, p in sorted(seen.items())]
                print(json.dumps(result, indent=2))
            else:
                for pid in sorted(seen.keys()):
                    print(f"{pid}  {seen[pid].get('product_name', '')}")

        else:
            # Default: status summary
            summary = get_status_summary(pages_dir)
            if args.json:
                print(json.dumps(summary, indent=2))
            else:
                print(format_status_human(summary))

    except Exception as e:
        if args.json:
            print(json.dumps({"error": str(e)}))
        else:
            print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
