#!/usr/bin/env python3
"""Update or verify every package version listed in .version-bump.json."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def resolve(value: object, field: str) -> object:
    for part in field.split("."):
        value = value[int(part)] if part.isdigit() else value[part]  # type: ignore[index]
    return value


def assign(value: object, field: str, replacement: str) -> None:
    parts = field.split(".")
    for part in parts[:-1]:
        value = value[int(part)] if part.isdigit() else value[part]  # type: ignore[index]
    last = parts[-1]
    value[int(last) if last.isdigit() else last] = replacement  # type: ignore[index]


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python scripts/bump-version.py <version>|--check")
    target = sys.argv[1]
    check = target == "--check"
    if not check and not re.fullmatch(r"\d+\.\d+\.\d+", target):
        raise SystemExit(f"not a semantic version: {target}")

    spec = json.loads((ROOT / ".version-bump.json").read_text(encoding="utf-8"))
    found: dict[str, str] = {}
    changed = 0
    for entry in spec["files"]:
        path = ROOT / entry["path"]
        data = json.loads(path.read_text(encoding="utf-8"))
        current = str(resolve(data, entry["field"]))
        found[f"{entry['path']} {entry['field']}"] = current
        if not check and current != target:
            assign(data, entry["field"], target)
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
            changed += 1

    width = max(map(len, found))
    for location, version in found.items():
        print(f"  {location:<{width}}  {version}")
    print()
    if check:
        versions = set(found.values())
        if len(versions) != 1:
            raise SystemExit(f"DISAGREEMENT across {len(versions)} versions: {sorted(versions)}")
        print(f"Every version agrees: {versions.pop()}")
    else:
        print(f"{changed} file(s) updated to {target}. Nothing is committed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
