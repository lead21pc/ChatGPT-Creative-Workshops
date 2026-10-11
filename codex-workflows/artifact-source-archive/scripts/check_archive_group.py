#!/usr/bin/env python3
"""Read-only layout checker for one confirmed artifact replacement group."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


ARCHIVE_NAME = "source_archive"


def _absolute(path: str) -> Path:
    return Path(os.path.abspath(os.path.expanduser(path)))


def _resolved(path: str) -> Path:
    return _absolute(path).resolve(strict=False)


def _within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _is_link_or_junction(path: Path) -> bool:
    if path.is_symlink():
        return True
    is_junction = getattr(os.path, "isjunction", None)
    return bool(is_junction and is_junction(path))


def _first_link_or_junction(path: Path) -> Path | None:
    for candidate in (path, *path.parents):
        if _is_link_or_junction(candidate):
            return candidate
    return None


def _matching_children(directory: Path) -> list[Path]:
    return [child for child in directory.iterdir() if child.name.casefold() == ARCHIVE_NAME]


def _ancestor_directories(source: Path, artifact_root: Path) -> list[Path]:
    directories: list[Path] = []
    current = source.parent
    while True:
        directories.append(current)
        if current == artifact_root:
            return directories
        current = current.parent


def check(task_root_arg: str, artifact_root_arg: str, source_args: list[str]) -> tuple[dict[str, object], int]:
    task_root_input = _absolute(task_root_arg)
    artifact_root_input = _absolute(artifact_root_arg)
    source_inputs = [_absolute(value) for value in source_args]
    task_root = _resolved(task_root_arg)
    artifact_root = _resolved(artifact_root_arg)
    sources = [_resolved(value) for value in source_args]
    problems: list[str] = []

    for label, input_path in (
        ("task root", task_root_input),
        ("artifact root", artifact_root_input),
        *(("source", source) for source in source_inputs),
    ):
        boundary = _first_link_or_junction(input_path)
        if boundary is not None:
            problems.append(f"{label} path crosses a symlink or junction: {boundary}")

    if not task_root.is_dir():
        problems.append("task root does not exist or is not a directory")
    if not artifact_root.is_dir():
        problems.append("artifact root does not exist or is not a directory")
    if task_root.is_dir() and not _within(artifact_root, task_root):
        problems.append("artifact root is outside task root")
    for source in sources:
        if not source.is_file():
            problems.append(f"source is missing or not a regular file: {source}")
            continue
        if not _within(source, artifact_root):
            problems.append(f"source is outside artifact root: {source}")
            continue
        relative_parts = source.relative_to(artifact_root).parts[:-1]
        if any(part.casefold() == ARCHIVE_NAME for part in relative_parts):
            problems.append(f"source is already inside an archive: {source}")

    archive_candidates: dict[str, Path] = {}
    if artifact_root.is_dir():
        try:
            for source in sources:
                if not _within(source, artifact_root):
                    continue
                for directory in _ancestor_directories(source, artifact_root):
                    for candidate in _matching_children(directory):
                        archive_candidates[str(candidate).casefold()] = candidate
        except OSError as exc:
            problems.append(f"cannot inspect archive layout: {exc}")

    try:
        root_matches = _matching_children(artifact_root) if artifact_root.is_dir() else []
    except OSError as exc:
        root_matches = []
        problems.append(f"cannot inspect artifact root: {exc}")
    if len(root_matches) > 1:
        problems.append("multiple case-insensitive source_archive entries exist at artifact root")
    elif root_matches and not root_matches[0].is_dir():
        problems.append("a non-directory entry occupies source_archive at artifact root")

    nested_candidates = [candidate for candidate in archive_candidates.values() if candidate.parent != artifact_root]
    if nested_candidates:
        rendered = ", ".join(str(path) for path in sorted(nested_candidates, key=str))
        problems.append(f"nested archive candidates would fragment the group: {rendered}")

    if problems:
        payload: dict[str, object] = {
            "status": "BLOCKED",
            "task_root": str(task_root),
            "artifact_root": str(artifact_root),
            "sources": [str(source) for source in sources],
            "problems": problems,
        }
        return payload, 2

    if root_matches:
        status = "PASS_SHARED"
        destination = root_matches[0]
    else:
        status = "PASS_CREATE_ONE"
        destination = artifact_root / ARCHIVE_NAME

    payload = {
        "status": status,
        "task_root": str(task_root),
        "artifact_root": str(artifact_root),
        "sources": [str(source) for source in sources],
        "archive_destination": str(destination),
    }
    return payload, 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", required=True)
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--source", action="append", required=True)
    args = parser.parse_args()
    payload, exit_code = check(args.task_root, args.artifact_root, args.source)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
