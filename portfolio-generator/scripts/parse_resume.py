#!/usr/bin/env python3
"""
Resume parser for the Portfolio Generator skill.
Extracts structured profile data from resume files (PDF, DOCX, TXT, MD).

Usage:
    python3 parse_resume.py <file_path> [--output json|text] [--dry-run]

Output:
    JSON object with extracted profile fields, printed to stdout.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def log(msg: str) -> None:
    """Log with timestamp to stderr."""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", file=sys.stderr)


def read_file_content(file_path: Path) -> str:
    """Read file content, converting from PDF/DOCX if needed."""
    suffix = file_path.suffix.lower()

    if suffix in (".txt", ".md", ".text"):
        log(f"Reading plain text: {file_path}")
        return file_path.read_text(encoding="utf-8", errors="replace")

    elif suffix == ".pdf":
        log(f"Converting PDF to text: {file_path}")
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", str(file_path), "-"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout
            log("pdftotext failed, trying pandoc...")
        except (FileNotFoundError, subprocess.TimeoutExpired):
            log("pdftotext not available, trying pandoc...")

        try:
            result = subprocess.run(
                ["pandoc", str(file_path), "-t", "plain", "--wrap=none"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                return result.stdout
        except (FileNotFoundError, subprocess.TimeoutExpired):
            log("pandoc also failed")

        log("ERROR: Could not extract text from PDF")
        sys.exit(1)

    elif suffix in (".docx", ".doc"):
        log(f"Converting DOCX to text: {file_path}")
        try:
            result = subprocess.run(
                ["pandoc", str(file_path), "-t", "plain", "--wrap=none"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                return result.stdout
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        log("ERROR: Could not extract text from DOCX")
        sys.exit(1)

    else:
        log(f"Attempting to read as plain text: {file_path}")
        return file_path.read_text(encoding="utf-8", errors="replace")


def extract_sections(text: str) -> dict:
    """
    Extract resume sections from raw text.

    Returns a dict with raw section text. The actual semantic parsing
    (understanding what each section means) is done by Zo/LLM, not this script.
    This script handles the mechanical extraction only.
    """
    lines = text.strip().split("\n")
    sections = {
        "raw_text": text,
        "line_count": len(lines),
        "char_count": len(text),
        "sections_detected": [],
    }

    section_headers = [
        "experience", "work experience", "professional experience", "employment",
        "education", "academic", "degrees",
        "skills", "technical skills", "core competencies", "proficiencies",
        "certifications", "certificates", "licenses",
        "projects", "key projects", "selected projects",
        "publications", "papers", "research",
        "awards", "honors", "achievements",
        "summary", "professional summary", "objective", "profile",
        "volunteer", "community", "leadership",
        "languages", "interests",
        "contact", "references",
    ]

    current_section = "header"
    section_content: dict[str, list[str]] = {"header": []}

    for line in lines:
        stripped = line.strip().lower()
        clean = stripped.rstrip(":").strip()

        is_header = False
        matched_section = None
        for header in section_headers:
            if clean == header or (len(clean) < 40 and header in clean):
                is_header = True
                matched_section = header
                break

        if is_header and matched_section:
            current_section = matched_section
            if current_section not in section_content:
                section_content[current_section] = []
                sections["sections_detected"].append(current_section)
        else:
            if current_section not in section_content:
                section_content[current_section] = []
            section_content[current_section].append(line)

    sections["section_content"] = {
        k: "\n".join(v).strip()
        for k, v in section_content.items()
        if v and "\n".join(v).strip()
    }

    return sections


def format_output(sections: dict, fmt: str) -> str:
    """Format the extracted sections for output."""
    if fmt == "json":
        return json.dumps(sections, indent=2)
    else:
        output = []
        output.append(f"Resume Analysis ({sections['line_count']} lines, {sections['char_count']} chars)")
        output.append(f"Sections detected: {', '.join(sections['sections_detected']) or 'none (unstructured)'}")
        output.append("")
        for name, content in sections.get("section_content", {}).items():
            output.append(f"--- {name.upper()} ---")
            output.append(content[:500] + ("..." if len(content) > 500 else ""))
            output.append("")
        return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Parse resume files into structured sections for the Portfolio Generator."
    )
    parser.add_argument("file_path", help="Path to the resume file (PDF, DOCX, TXT, MD)")
    parser.add_argument("--output", choices=["json", "text"], default="json", help="Output format")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be parsed without processing")
    args = parser.parse_args()

    file_path = Path(args.file_path)

    if not file_path.exists():
        log(f"ERROR: File not found: {file_path}")
        sys.exit(1)

    if args.dry_run:
        log(f"DRY RUN: Would parse {file_path} ({file_path.stat().st_size} bytes, type: {file_path.suffix})")
        print(json.dumps({"dry_run": True, "file": str(file_path), "size": file_path.stat().st_size}))
        sys.exit(0)

    log(f"Parsing resume: {file_path}")
    content = read_file_content(file_path)

    if not content.strip():
        log("ERROR: No text content extracted from file")
        sys.exit(1)

    log(f"Extracted {len(content)} characters")
    sections = extract_sections(content)
    print(format_output(sections, args.output))
    log("Done")


if __name__ == "__main__":
    main()
