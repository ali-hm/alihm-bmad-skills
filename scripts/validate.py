#!/usr/bin/env python3
"""Validate package structure and release metadata without changing files."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

try:
    import yaml
except ImportError:
    raise SystemExit("Install validation dependencies: python -m pip install -r requirements-dev.txt")

SKILLS = {
    "bmad-sdlc", "bmad-guided-build",
    "change-intake-governance", "decision-governance",
}
VERSION = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"


def validate(root: Path, release: bool = False, tag: str | None = None) -> list[str]:
    """Return all discovered package errors; never execute skill instructions."""
    errors = []
    required = (
        "README.md", "LICENSE", "CHANGELOG.md", "plugin.json",
        "requirements-dev.txt", "docs/compatibility.md", "docs/releasing.md",
        "docs/project-instructions.md", ".github/workflows/validate.yml",
    )
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing package file: {name}")
    try:
        manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("manifest must be an object")
    except (OSError, ValueError) as exc:
        return errors + [f"Invalid plugin.json: {exc}"]

    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(VERSION, version):
        errors.append("plugin.json version must be major.minor.patch")
    if manifest.get("name") != "alihm-bmad-skills":
        errors.append("Unexpected plugin name")
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("Unexpected portable plugin schema")
    if manifest.get("license") != "MIT":
        errors.append("Plugin license must match the approved MIT license")
    if tag is not None and tag != f"v{version}":
        errors.append(f"Tag {tag!r} does not match bundle version {version!r}")

    root_license = (root / "LICENSE").read_bytes() if (root / "LICENSE").is_file() else None
    entries = list((root / "skills").glob("*/SKILL.md"))
    if {entry.parent.name for entry in entries} != SKILLS:
        errors.append("skills/ must contain exactly the four companion skill entrypoints")
    for entry in entries:
        label = entry.relative_to(root).as_posix()
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            errors.append(f"{label}: missing YAML frontmatter")
            continue
        try:
            data = yaml.safe_load(match[1])
            if not isinstance(data, dict):
                raise ValueError("frontmatter must be a mapping")
        except (yaml.YAMLError, ValueError) as exc:
            errors.append(f"{label}: {exc}")
            continue
        name = data.get("name")
        if name != entry.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(name)) or len(str(name)) > 64:
            errors.append(f"{label}: invalid or mismatched skill name")
        description = data.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{label}: description must contain 1-1024 characters")
        allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
        if data.keys() - allowed:
            errors.append(f"{label}: unsupported frontmatter fields {sorted(data.keys() - allowed)}")
        metadata = data.get("metadata")
        if not isinstance(metadata, dict) or metadata.get("version") != version:
            errors.append(f"{label}: metadata.version must equal {version}")
        elif not all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()):
            errors.append(f"{label}: metadata keys and values must be strings")
        if data.get("license") != "MIT":
            errors.append(f"{label}: license must be MIT")
        license_file = entry.parent / "LICENSE"
        if not license_file.is_file() or license_file.read_bytes() != root_license:
            errors.append(f"{label}: include the root MIT license for standalone installations")
        ui_file = entry.parent / "agents/openai.yaml"
        try:
            ui = yaml.safe_load(ui_file.read_text(encoding="utf-8"))
            interface = ui["interface"]
            if not all(isinstance(interface.get(field), str) and interface[field].strip()
                       for field in ("display_name", "short_description", "default_prompt")):
                raise ValueError("UI strings must be non-empty")
            if not 25 <= len(interface["short_description"]) <= 64:
                raise ValueError("UI short_description must contain 25-64 characters")
            if f"${name}" not in interface["default_prompt"]:
                raise ValueError("default_prompt must name this skill")
            if ui.get("policy", {}).get("allow_implicit_invocation", True) is not True:
                raise ValueError("implicit invocation must remain enabled")
        except (OSError, yaml.YAMLError, KeyError, TypeError, AttributeError, ValueError) as exc:
            errors.append(f"{label}: invalid agents/openai.yaml: {exc}")

    markdown = [root / "README.md", root / "CHANGELOG.md"]
    markdown += list((root / "docs").rglob("*.md")) + list((root / "skills").rglob("*.md"))
    for path in markdown:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        fence = None
        for line in text.splitlines():
            marker = re.match(r"^\s*([`~]{3,})", line)
            if marker:
                token = marker[1]
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                continue
            if fence is not None:
                continue
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", line):
                target = target.strip().split(' "', 1)[0].strip("<>")
                parsed = urlparse(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                destination = (path.parent / unquote(parsed.path)).resolve()
                if not destination.is_relative_to(root.resolve()) or not destination.exists():
                    errors.append(f"{path.relative_to(root)}: invalid local reference {target}")
        if fence is not None:
            errors.append(f"{path.relative_to(root)}: unclosed code fence")

    readme = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").is_file() else ""
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8") if (root / "CHANGELOG.md").is_file() else ""
    if f"**Bundle version: {version}." not in readme:
        errors.append("README bundle version does not match plugin.json")
    if f"## [{version}] - " not in changelog:
        errors.append("CHANGELOG.md is missing the current version entry")
    if release:
        if "YOUR_GITHUB_USER" in readme:
            errors.append("Replace YOUR_GITHUB_USER in README.md before publication")
        repository = manifest.get("repository", "")
        if not isinstance(repository, str) or not re.fullmatch(r"https://github\.com/[^/\s]+/alihm-bmad-skills", repository):
            errors.append("Set plugin.json repository to the real HTTPS GitHub repository URL")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true", help="Also require final publication identity")
    parser.add_argument("--tag", help="Check that a tag equals v<bundle version>")
    args = parser.parse_args()
    errors = validate(Path(__file__).resolve().parents[1], args.release, args.tag)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: four skills, MIT licenses, UI metadata, versions, and local references")
    print("Package checks only; live BMad execution and directory publication are unverified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
