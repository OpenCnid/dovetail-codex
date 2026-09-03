#!/usr/bin/env python3
"""Validate Dovetail's Codex-native package and prompt surfaces."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "better-skill-creator",
    "hypershot-protocol",
    "judge-composition",
    "prompt-engineering",
    "self-play",
    "spark-steering",
    "subagent-composition",
    "upsum",
}
EXPLICIT_ONLY = {"spark-steering", "upsum"}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: invalid or unreadable JSON: {exc}")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data, text


def yaml_scalar(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1).strip().strip('"\'') if match else None


def main() -> int:
    manifest = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if manifest.get("name") != "dovetail-codex":
        fail("plugin name must be dovetail-codex")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail("plugin version must be strict semantic versioning")
    if manifest.get("skills") != "./skills/":
        fail("plugin manifest must declare the native ./skills/ root")
    unsupported = {"hooks", "apps", "mcpServers"} & manifest.keys()
    if unsupported:
        fail(f"undeclared companion components present: {sorted(unsupported)}")

    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    entries = marketplace.get("plugins", [])
    if len(entries) != 1 or entries[0].get("name") != manifest["name"]:
        fail("marketplace must contain exactly the manifest plugin")
    source = entries[0].get("source", {})
    if source.get("source") != "url" or not source.get("url", "").endswith(
        "/OpenCnid/dovetail-codex.git"
    ):
        fail("marketplace must publish the repository-root URL plugin")
    policy = entries[0].get("policy", {})
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        fail("marketplace entry must declare installation and authentication policy")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "codex plugin add dovetail-codex@opencnid" not in readme:
        fail("README must document the current Codex plugin add command")

    skill_dirs = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if skill_dirs != EXPECTED_SKILLS:
        fail(
            f"skill inventory mismatch: missing={sorted(EXPECTED_SKILLS - skill_dirs)} "
            f"extra={sorted(skill_dirs - EXPECTED_SKILLS)}"
        )

    for name in sorted(EXPECTED_SKILLS):
        skill_path = ROOT / "skills" / name / "SKILL.md"
        data, skill_text = frontmatter(skill_path)
        if data.get("name") != name:
            fail(f"{name}: frontmatter name must match directory")
        description = data.get("description", "")
        if not description or len(description) > 240:
            fail(f"{name}: description must be 1..240 characters")
        if len(skill_text.encode("utf-8")) > 20_000:
            fail(f"{name}: SKILL.md exceeds the 20 KB prompt budget")
        if "disable-model-invocation" in skill_text:
            fail(f"{name}: use agents/openai.yaml invocation policy")
        stale_markers = (".claude-plugin", "CLAUDE_CONFIG_DIR", "~/.claude", "claude -p")
        if any(marker in skill_text for marker in stale_markers):
            fail(f"{name}: active skill body contains a legacy runtime marker")

        metadata_path = ROOT / "skills" / name / "agents" / "openai.yaml"
        metadata = metadata_path.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            if yaml_scalar(metadata, field) is None:
                fail(f"{name}: agents/openai.yaml missing {field}")
        short_description = yaml_scalar(metadata, "short_description") or ""
        if not 25 <= len(short_description) <= 64:
            fail(f"{name}: short_description must be 25..64 characters")
        prompt = yaml_scalar(metadata, "default_prompt") or ""
        if f"${name}" not in prompt:
            fail(f"{name}: default_prompt must mention ${name}")
        implicit = yaml_scalar(metadata, "allow_implicit_invocation")
        expected = "false" if name in EXPLICIT_ONLY else "true"
        if implicit != expected:
            fail(f"{name}: allow_implicit_invocation must be {expected}")

    agents = (ROOT / "AGENTS.md").read_bytes()
    if len(agents) > 32 * 1024:
        fail("root AGENTS.md exceeds the default combined Codex budget")

    print(
        f"OK: {manifest['name']} {manifest['version']}; "
        f"{len(EXPECTED_SKILLS)} native skills; AGENTS.md {len(agents)} bytes"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
