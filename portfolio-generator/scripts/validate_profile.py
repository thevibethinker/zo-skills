#!/usr/bin/env python3
"""
Profile data validator for the Portfolio Generator skill.
Validates that gathered profile data meets minimum requirements
before portfolio generation begins.

Usage:
    python3 validate_profile.py <json_file> [--strict] [--dry-run]
    echo '{"name":"..."}' | python3 validate_profile.py - 

Output:
    Validation report (JSON) with pass/fail status and any issues found.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def log(msg: str) -> None:
    """Log with timestamp to stderr."""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", file=sys.stderr)


REQUIRED_FIELDS = {
    "name": "Full name",
    "title": "Professional title or headline",
}

RECOMMENDED_FIELDS = {
    "summary": "Professional summary or about section",
    "experience": "Work experience entries",
    "skills": "Professional skills",
}

OPTIONAL_FIELDS = {
    "education": "Education history",
    "certifications": "Professional certifications",
    "projects": "Notable projects",
    "publications": "Publications or speaking engagements",
    "location": "Current location",
    "email": "Contact email",
    "linkedin_url": "LinkedIn profile URL",
    "photo_url": "Headshot photo URL or path",
    "links": "Additional links (website, GitHub, etc.)",
}


def validate_profile(data: dict, strict: bool = False) -> dict:
    """
    Validate profile data completeness and quality.
    
    Returns:
        dict with: valid (bool), score (int 0-100), issues (list), summary (str)
    """
    issues = []
    warnings = []
    score = 0

    for field, label in REQUIRED_FIELDS.items():
        value = data.get(field, "")
        if not value or (isinstance(value, str) and not value.strip()):
            issues.append(f"MISSING REQUIRED: {label} ({field})")
        else:
            score += 20

    for field, label in RECOMMENDED_FIELDS.items():
        value = data.get(field)
        if not value:
            warnings.append(f"MISSING RECOMMENDED: {label} ({field})")
        elif isinstance(value, list) and len(value) == 0:
            warnings.append(f"EMPTY: {label} ({field})")
        else:
            score += 15

    optional_count = 0
    for field in OPTIONAL_FIELDS:
        value = data.get(field)
        if value and (not isinstance(value, (list, str)) or (isinstance(value, str) and value.strip()) or (isinstance(value, list) and len(value) > 0)):
            optional_count += 1
    score += min(optional_count * 5, 15)

    name = data.get("name", "")
    if name and len(name.strip()) < 2:
        issues.append(f"NAME TOO SHORT: '{name}' — likely incomplete")
    if name and len(name.strip()) > 100:
        warnings.append(f"NAME UNUSUALLY LONG: {len(name)} chars — verify")

    summary = data.get("summary", "")
    if isinstance(summary, str) and summary:
        if len(summary) < 20:
            warnings.append("SUMMARY VERY SHORT: Consider expanding for a better bio")
        slop_phrases = [
            "passionate about leveraging",
            "synergies",
            "results-driven professional",
            "dynamic and motivated",
            "seeking opportunities",
        ]
        for phrase in slop_phrases:
            if phrase.lower() in summary.lower():
                warnings.append(f"SLOP DETECTED: '{phrase}' — consider more authentic language")

    experience = data.get("experience", [])
    if isinstance(experience, list):
        for i, exp in enumerate(experience):
            if isinstance(exp, dict):
                if not exp.get("title") and not exp.get("role"):
                    warnings.append(f"EXPERIENCE [{i}]: Missing job title")
                if not exp.get("company") and not exp.get("organization"):
                    warnings.append(f"EXPERIENCE [{i}]: Missing company name")

    valid = len(issues) == 0
    if strict:
        valid = valid and len(warnings) == 0

    section_count = sum(1 for f in list(REQUIRED_FIELDS) + list(RECOMMENDED_FIELDS) + list(OPTIONAL_FIELDS)
                        if data.get(f))

    result = {
        "valid": valid,
        "score": min(score, 100),
        "section_count": section_count,
        "issues": issues,
        "warnings": warnings,
        "summary": f"Profile {'VALID' if valid else 'INVALID'} — "
                   f"Score: {min(score, 100)}/100, "
                   f"{section_count} sections populated, "
                   f"{len(issues)} issues, {len(warnings)} warnings",
    }

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Validate portfolio profile data before generation."
    )
    parser.add_argument("json_file", help="Path to JSON profile data (or - for stdin)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--dry-run", action="store_true", help="Show validation rules without processing")
    args = parser.parse_args()

    if args.dry_run:
        rules = {
            "required": {k: v for k, v in REQUIRED_FIELDS.items()},
            "recommended": {k: v for k, v in RECOMMENDED_FIELDS.items()},
            "optional": {k: v for k, v in OPTIONAL_FIELDS.items()},
        }
        print(json.dumps(rules, indent=2))
        sys.exit(0)

    if args.json_file == "-":
        log("Reading profile data from stdin")
        raw = sys.stdin.read()
    else:
        path = Path(args.json_file)
        if not path.exists():
            log(f"ERROR: File not found: {path}")
            sys.exit(1)
        log(f"Reading profile data from: {path}")
        raw = path.read_text()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        log(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)

    result = validate_profile(data, strict=args.strict)
    print(json.dumps(result, indent=2))

    if not result["valid"]:
        log(f"VALIDATION FAILED: {result['summary']}")
        sys.exit(1)
    else:
        log(f"VALIDATION PASSED: {result['summary']}")
        sys.exit(0)


if __name__ == "__main__":
    main()
