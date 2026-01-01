#!/usr/bin/env python3
"""
Remove language-specific solution code blocks from editorials and
remove solution-template signatures from problems.
"""

import re
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent
LANG_TAGS = {"java", "python", "cpp", "c++", "javascript", "js"}


def strip_blocks(text, only_solution_template):
    lines = text.splitlines()
    output = []
    in_block = False
    in_solution = False
    solution_level = None

    for line in lines:
        if not in_block:
            if only_solution_template:
                heading = re.match(r"^(#+)\s+Solution Template\b", line)
                if heading:
                    in_solution = True
                    solution_level = len(heading.group(1))
                elif in_solution:
                    other_heading = re.match(r"^(#+)\s+", line)
                    if other_heading and len(other_heading.group(1)) <= solution_level:
                        in_solution = False

            fence = re.match(r"^```\s*([A-Za-z+]+)\s*$", line)
            if fence:
                lang = fence.group(1).lower()
                if lang in LANG_TAGS and (not only_solution_template or in_solution):
                    in_block = True
                    continue

            output.append(line)
        else:
            if line.strip().startswith("```"):
                in_block = False
            continue

    result = "\n".join(output)
    if text.endswith("\n"):
        result += "\n"
    return result


def process_files(files, only_solution_template):
    updated = 0
    for path in files:
        original = path.read_text()
        stripped = strip_blocks(original, only_solution_template)
        if stripped != original:
            path.write_text(stripped)
            updated += 1
    return updated


def main():
    editorials = []
    problems = []
    for section in (ROOT_DIR / "dsa-problems").iterdir():
        if not section.is_dir():
            continue
        editorials_dir = section / "editorials"
        problems_dir = section / "problems"
        if editorials_dir.exists():
            editorials.extend(
                p for p in editorials_dir.glob("*.md") if p.name != "README.md"
            )
        if problems_dir.exists():
            problems.extend(
                p for p in problems_dir.glob("*.md") if p.name != "README.md"
            )

    updated_editorials = process_files(editorials, only_solution_template=False)
    updated_problems = process_files(problems, only_solution_template=True)

    print(f"Updated editorials: {updated_editorials}")
    print(f"Updated problems: {updated_problems}")


if __name__ == "__main__":
    main()
