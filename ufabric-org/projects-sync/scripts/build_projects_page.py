#!/usr/bin/env python3
"""Build content/projects.md from uFabric project markdown reports."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sources",
        default="ufabric-org/projects-sync/sources.md",
        help="Path to Markdown table with project report sources.",
    )
    parser.add_argument(
        "--output",
        default="content/projects.md",
        help="Output markdown page path.",
    )
    parser.add_argument(
        "--timeout",
        default=20,
        type=int,
        help="Network timeout in seconds.",
    )
    return parser.parse_args()


def request_headers(token: str | None) -> dict[str, str]:
    headers = {
        "User-Agent": "ufabric-projects-sync/1.0",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_text(url: str, timeout: int, token: str | None) -> str:
    req = urllib.request.Request(url, headers=request_headers(token))
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8")


def fetch_json(url: str, timeout: int, token: str | None) -> Any:
    return json.loads(fetch_text(url, timeout=timeout, token=token))


def get_last_commit_date(repo: str, report_path: str, branch: str, timeout: int, token: str | None) -> str | None:
    query = urllib.parse.urlencode(
        {
            "path": report_path,
            "sha": branch,
            "per_page": 1,
        }
    )
    url = f"https://api.github.com/repos/{repo}/commits?{query}"
    data = fetch_json(url, timeout=timeout, token=token)
    if not isinstance(data, list) or not data:
        return None

    first = data[0]
    return (
        first.get("commit", {})
        .get("author", {})
        .get("date")
    )


def build_raw_url(repo: str, branch: str, report_path: str) -> str:
    parts = [urllib.parse.quote(part) for part in report_path.split("/")]
    encoded_path = "/".join(parts)
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{encoded_path}"


def trim_h1(markdown: str) -> str:
    lines = markdown.strip().splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).strip()
    return "\n".join(lines).strip()


def shift_headings(markdown: str, levels: int = 1) -> str:
    shifted: list[str] = []
    for line in markdown.splitlines():
        if line.startswith("#"):
            prefix = len(line) - len(line.lstrip("#"))
            if prefix > 0 and len(line) > prefix and line[prefix] == " ":
                shifted.append("#" * min(prefix + levels, 6) + line[prefix:])
                continue
        shifted.append(line)
    return "\n".join(shifted)


def docsify_route(path: str) -> str:
    cleaned = path.strip().lstrip("./")
    return f"#/{cleaned}"


def read_sources(path: Path) -> list[dict[str, Any]]:
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    table_lines = [line for line in lines if line.startswith("|") and line.endswith("|")]
    if len(table_lines) < 3:
        raise ValueError("sources markdown must include a table with header, separator and at least one row")

    header = [part.strip() for part in table_lines[0].split("|")[1:-1]]
    if not header:
        raise ValueError("sources table header is empty")
    expected_prefix = ["name", "repo", "branch", "report_path"]
    if header[:4] != expected_prefix:
        raise ValueError("sources table must start with columns: name, repo, branch, report_path")

    sources: list[dict[str, Any]] = []
    for row in table_lines[2:]:
        cols = [part.strip() for part in row.split("|")[1:-1]]
        if len(cols) != len(header):
            raise ValueError("sources table row has unexpected number of columns")
        item: dict[str, Any] = {}
        for key, value in zip(header, cols):
            item[key] = value
        sources.append(item)

    if not sources:
        raise ValueError("sources table has no rows")
    return sources


def validate_source(item: dict[str, Any]) -> None:
    for key in ("name", "repo", "branch", "report_path"):
        if key not in item or not isinstance(item[key], str) or not item[key].strip():
            raise ValueError(f"source entry must include non-empty '{key}'")
    if "local_path" in item and not isinstance(item["local_path"], str):
        raise ValueError("optional 'local_path' must be a string when present")
    if "visibility" in item and not isinstance(item["visibility"], str):
        raise ValueError("optional 'visibility' must be a string when present")
    visibility = item.get("visibility", "").strip().lower() or "public"
    if visibility not in {"public", "private"}:
        raise ValueError("optional 'visibility' must be 'public' or 'private'")


def get_local_last_commit_date(path: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", path],
            check=False,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def build_page(sources: list[dict[str, Any]], timeout: int, token: str | None) -> str:
    lines: list[str] = []
    lines.append("# Projects")
    lines.append("")
    lines.append("This page aggregates public markdown progress reports from uFabric projects.")
    lines.append("")
    lines.append("Source registry: `ufabric-org/projects-sync/sources.md`")
    lines.append("")
    lines.append("Sync operations docs: [`ufabric-org/projects-sync/README.md`](#/ufabric-org/projects-sync/README.md)")
    lines.append("")
    lines.append("New project setup: [`ufabric-org/projects-sync/NEW_PROJECT_SETUP.md`](#/ufabric-org/projects-sync/NEW_PROJECT_SETUP.md)")
    lines.append("")
    lines.append("To join this page, publish a report file and add your repo entry to the source registry.")
    lines.append("")

    for source in sorted(sources, key=lambda x: x["name"].lower()):
        validate_source(source)
        name = source["name"].strip()
        repo = source["repo"].strip()
        branch = source["branch"].strip()
        report_path = source["report_path"].strip()
        local_path = source.get("local_path", "").strip()
        visibility = source.get("visibility", "").strip().lower() or "public"
        repo_url = f"https://github.com/{repo}"
        raw_url = build_raw_url(repo=repo, branch=branch, report_path=report_path)

        lines.append(f"## {name}")
        lines.append("")
        if visibility == "private":
            lines.append(f"- Repository: private source (`{repo}`)")
        else:
            lines.append(f"- Repository: [{repo}]({repo_url})")
        lines.append(f"- Branch: `{branch}`")
        lines.append(f"- Visibility: `{visibility}`")
        if local_path and Path(local_path).exists():
            link = docsify_route(local_path)
            lines.append(f"- Report file: local snapshot [`{local_path}`]({link})")
        else:
            lines.append(f"- Report file: [`{report_path}`]({raw_url})")

        last_commit_date = None
        if visibility == "public":
            try:
                last_commit_date = get_last_commit_date(
                    repo=repo,
                    report_path=report_path,
                    branch=branch,
                    timeout=timeout,
                    token=token,
                )
            except Exception:
                last_commit_date = None

        if last_commit_date:
            lines.append(f"- Last report commit (UTC): `{last_commit_date}`")
        elif local_path and Path(local_path).exists():
            local_commit = get_local_last_commit_date(local_path)
            if local_commit:
                lines.append(f"- Last report commit (UTC): `{local_commit}`")
            else:
                lines.append("- Last report commit (UTC): `unavailable`")
        else:
            lines.append("- Last report commit (UTC): `unavailable`")
        lines.append("")

        # Local path wins when present so this repo can preview uncommitted report edits.
        if local_path and Path(local_path).exists():
            local_content = Path(local_path).read_text(encoding="utf-8")
            local_body = shift_headings(trim_h1(local_content), levels=1)
            if local_body:
                lines.append(local_body)
            else:
                lines.append("> Local report file is empty.")
        elif visibility == "private":
            lines.append("> Private project report is not publicly accessible.")
        else:
            try:
                report_content = fetch_text(raw_url, timeout=timeout, token=token)
                report_body = shift_headings(trim_h1(report_content), levels=1)
                if report_body:
                    lines.append(report_body)
                else:
                    lines.append("> Report file is reachable but empty.")
            except urllib.error.HTTPError as exc:
                lines.append(f"> Could not load report (`HTTP {exc.code}`).")
            except urllib.error.URLError as exc:
                lines.append(f"> Could not load report (`{exc.reason}`).")
            except Exception as exc:
                lines.append(f"> Could not load report (`{exc}`).")

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    sources_path = Path(args.sources)
    output_path = Path(args.output)

    try:
        sources = read_sources(sources_path)
    except Exception as exc:
        print(f"error: failed reading sources file '{sources_path}': {exc}", file=sys.stderr)
        return 1

    token = os.getenv("GITHUB_TOKEN")
    try:
        page = build_page(
            sources=sources,
            timeout=args.timeout,
            token=token,
        )
    except Exception as exc:
        print(f"error: failed building projects page: {exc}", file=sys.stderr)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(page, encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
