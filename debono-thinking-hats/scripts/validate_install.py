#!/usr/bin/env python3
"""
validate_install.py — Post-install validator for De Bono Six Thinking Hats.

This script cannot call Zo tools directly. It prints verification
instructions and checks what it can from the filesystem (placeholder
cleanup in persona source files). Run after the installer completes.

Usage:
    python3 Skills/debono-thinking-hats/scripts/validate_install.py
"""

import json
import os
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
PERSONAS_DIR = SKILL_ROOT / "assets" / "personas"
ROUTING_CONTRACT = SKILL_ROOT / "assets" / "routing-contract.md"
SEQUENCES_FILE = SKILL_ROOT / "assets" / "sequences.md"
WALKTHROUGH_FILE = SKILL_ROOT / "assets" / "WALKTHROUGH.prompt.md"
MODE_CATALOG_FILE = SKILL_ROOT / "assets" / "mode-catalog.md"
USE_CASES_FILE = SKILL_ROOT / "assets" / "use-cases.md"
IMAGES_DIR = SKILL_ROOT / "assets" / "images"
EXPECTED_IMAGES = [
    "debono3-blue-hat.png",
    "debono3-white-hat.png",
    "debono3-red-hat.png",
    "debono3-yellow-hat.png",
    "debono3-black-hat.png",
    "debono3-green-hat.png",
]

EXPECTED_HATS = {
    "blue": {
        "persona_name": "Thinking Hat: Blue (Facilitator)",
        "file": "blue-hat-facilitator.md",
    },
    "white": {
        "persona_name": "Thinking Hat: White (Analyst)",
        "file": "white-hat-analyst.md",
    },
    "red": {
        "persona_name": "Thinking Hat: Red (Intuition)",
        "file": "red-hat-intuition.md",
    },
    "yellow": {
        "persona_name": "Thinking Hat: Yellow (Optimist)",
        "file": "yellow-hat-optimist.md",
    },
    "black": {
        "persona_name": "Thinking Hat: Black (Critical Judge)",
        "file": "black-hat-judge.md",
    },
    "green": {
        "persona_name": "Thinking Hat: Green (Creative)",
        "file": "green-hat-creative.md",
    },
}

PLACEHOLDER_RE = re.compile(r"\{PERSONA_ID:\w+\}")


def check_mark(passed: bool) -> str:
    return "✅ PASS" if passed else "❌ FAIL"


def validate_source_files() -> list[dict]:
    results = []
    for color, spec in EXPECTED_HATS.items():
        filepath = PERSONAS_DIR / spec["file"]
        entry = {
            "color": color,
            "file": str(filepath.relative_to(SKILL_ROOT)),
            "exists": filepath.exists(),
            "placeholder_count": 0,
        }
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            placeholders = PLACEHOLDER_RE.findall(content)
            entry["placeholder_count"] = len(placeholders)
        results.append(entry)
    return results


def validate_support_files() -> dict:
    return {
        "routing_contract_exists": ROUTING_CONTRACT.exists(),
        "sequences_file_exists": SEQUENCES_FILE.exists(),
        "walkthrough_file_exists": WALKTHROUGH_FILE.exists(),
        "mode_catalog_exists": MODE_CATALOG_FILE.exists(),
        "use_cases_exists": USE_CASES_FILE.exists(),
    }


def validate_images() -> list[dict]:
    results = []
    for name in EXPECTED_IMAGES:
        path = IMAGES_DIR / name
        results.append({"name": name, "exists": path.exists()})
    return results


def main():
    print("=" * 60)
    print("  De Bono Six Thinking Hats — Installation Validator")
    print("=" * 60)
    print()

    all_passed = True

    # --- Check 1: Source persona files ---
    print("── Check 1: Persona Source Files (Templates) ──")
    source_results = validate_source_files()
    for r in source_results:
        exists_ok = r["exists"]
        if not exists_ok:
            all_passed = False

        status = check_mark(exists_ok)
        print(f"  {r['color']:8s} file present: {status}  ({r['file']})")
        if exists_ok and r["placeholder_count"] > 0:
            print(f"           placeholders:  ℹ️  INFO  ({r['placeholder_count']} in template — normal, resolved at install time)")
    print()

    # --- Check 2: Support files ---
    print("── Check 2: Support Files ──")
    support = validate_support_files()
    for label, present in support.items():
        nice_label = label.replace("_", " ").replace(" exists", "")
        status = check_mark(present)
        if not present:
            all_passed = False
        print(f"  {nice_label}: {status}")
    print()

    # --- Check 3: Packaged image assets ---
    print("── Check 3: Packaged Image Assets ──")
    image_results = validate_images()
    for r in image_results:
        status = check_mark(r["exists"])
        if not r["exists"]:
            all_passed = False
        print(f"  {r['name']}: {status}")
    print()

    # --- Check 4: Zo Personas (Manual Verification Required) ---
    print("── Check 4: Zo Personas (Manual Verification Required) ──")
    print()
    print("  The validator cannot query Zo personas directly.")
    print("  Please verify the following yourself:")
    print()
    print("  1. Open Personas: /?t=settings&s=ai&d=personas")
    print("  2. Confirm these 6 personas exist:")
    for color, spec in EXPECTED_HATS.items():
        print(f"     • {spec['persona_name']}")
    print()
    print("  3. Open any hat persona and check that its Routing & Handoff")
    print("     section contains REAL UUIDs, NOT placeholders like")
    print("     {PERSONA_ID:blue_hat}.")
    print("     (Note: the source files on disk keep placeholders as")
    print("     templates. Only the LIVE personas should have resolved IDs.)")
    print()

    # --- Check 4: Manual rule verification ---
    print("── Check 4: Zo Routing Rule (Manual Verification Required) ──")
    print()
    print("  1. Open Rules: /?t=settings&s=ai&d=rules")
    print('  2. Confirm a rule exists with condition containing "Thinking Hat"')
    print("  3. The rule instruction should reference:")
    print("     Skills/debono-thinking-hats/assets/routing-contract.md")
    print()

    # --- Summary ---
    print("=" * 60)
    automated_ok = all_passed
    if automated_ok:
        print("  Automated checks: ✅ ALL PASSED")
    else:
        print("  Automated checks: ❌ SOME FAILED (see above)")
    print("  Manual checks:    ⏳ Verify personas and rule per instructions above")
    print("=" * 60)

    sys.exit(0 if automated_ok else 1)


if __name__ == "__main__":
    main()
