from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"

PLACEHOLDERS = {
    "{{FULL_NAME}}": "Kalpick Sharma",
    "{{ROLE}}": "Community Architect | Design Engineer | Web3 Enthusiast",
    "{{GITHUB_USERNAME}}": "Kalpick-Sharma",
    "{{PROFILE_BANNER}}": "assets/banner.svg",
    "{{STATS_IMAGE}}": "assets/stats.svg",
    "{{TECH_STACK_IMAGE}}": "assets/tech-stack.svg",
    "{{CONTRIBUTION_MAP_IMAGE}}": "assets/contribution-map.svg",
}


def update_last_updated(text: str) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    pattern = r"<!-- LAST_UPDATED:START -->.*?<!-- LAST_UPDATED:END -->"
    replacement = f"<!-- LAST_UPDATED:START -->{timestamp}<!-- LAST_UPDATED:END -->"
    return re.sub(pattern, replacement, text, count=1, flags=re.DOTALL)


def update_readme() -> None:
    text = README_PATH.read_text(encoding="utf-8")
    updated = text
    for key, value in PLACEHOLDERS.items():
        updated = updated.replace(key, value)
    updated = update_last_updated(updated)
    if updated != text:
        README_PATH.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
    print("README placeholders and timestamp updated successfully.")
