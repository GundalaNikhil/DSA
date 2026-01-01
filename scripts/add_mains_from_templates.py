#!/usr/bin/env python3
"""
Append language-specific mains to solution files using problem markdown templates.
"""

import argparse
import glob
import re
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent

LANG_CONFIG = {
    "java": {"ext": "java", "tags": ["java"]},
    "cpp": {"ext": "cpp", "tags": ["cpp", "c++"]},
    "javascript": {"ext": "js", "tags": ["javascript", "js"]},
}


def extract_template_code(md_path, tags):
    text = Path(md_path).read_text()
    marker = text.find("Solution Template")
    if marker != -1:
        text = text[marker:]
    for tag in tags:
        pattern = rf"```{tag}\n(.*?)```"
        match = re.search(pattern, text, flags=re.S)
        if match:
            return match.group(1).strip() + "\n"
    return None


def strip_class_block(code, class_name):
    needle = f"class {class_name}"
    idx = code.find(needle)
    if idx == -1:
        return code
    start = code.find("{", idx)
    if start == -1:
        return code
    depth = 0
    end = None
    i = start
    while i < len(code):
        if code[i] == "{":
            depth += 1
        elif code[i] == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
        i += 1
    if end is None:
        return code
    j = end + 1
    if j < len(code) and code[j] == ";":
        j += 1
    return (code[:idx].rstrip() + "\n\n" + code[j:].lstrip()).strip() + "\n"


def split_java(code):
    package_line = None
    imports = []
    body = []
    for line in code.splitlines():
        stripped = line.strip()
        if stripped.startswith("package "):
            if package_line is None:
                package_line = stripped
        elif stripped.startswith("import "):
            imports.append(stripped)
        else:
            body.append(line)
    return package_line, imports, "\n".join(body).strip()


def split_cpp(code):
    includes = []
    using_lines = []
    body = []
    for line in code.splitlines():
        stripped = line.strip()
        if stripped.startswith("#include"):
            includes.append(stripped)
        elif stripped == "using namespace std;":
            using_lines.append(stripped)
        else:
            body.append(line)
    return includes, using_lines, "\n".join(body).strip()


def unique_lines(lines):
    seen = set()
    result = []
    for line in lines:
        key = line.strip()
        if not key or key in seen:
            continue
        seen.add(key)
        result.append(key)
    return result


def has_java_main(code):
    return bool(re.search(r"\bclass\s+Main\b", code) or re.search(r"\bstatic\s+void\s+main\b", code))


def has_cpp_main(code):
    return bool(re.search(r"\bint\s+main\s*\(", code))


def has_js_main(code):
    return "readFileSync(0" in code or "readline.createInterface" in code or "process.stdin" in code


def update_java(solution_path, template_code):
    solution_code = Path(solution_path).read_text()
    if has_java_main(solution_code):
        return False
    template_code = strip_class_block(template_code, "Solution")
    package_s, imports_s, body_s = split_java(solution_code)
    package_t, imports_t, body_t = split_java(template_code)
    package_line = package_s or package_t
    imports = unique_lines(imports_s + imports_t)
    parts = []
    if package_line:
        parts.append(package_line)
    if imports:
        parts.append("\n".join(imports))
    if body_s:
        parts.append(body_s)
    if body_t:
        parts.append(body_t)
    new_code = "\n\n".join(parts).strip() + "\n"
    Path(solution_path).write_text(new_code)
    return True


def update_cpp(solution_path, template_code):
    solution_code = Path(solution_path).read_text()
    if has_cpp_main(solution_code):
        return False
    template_code = strip_class_block(template_code, "Solution")
    includes_s, using_s, body_s = split_cpp(solution_code)
    includes_t, using_t, body_t = split_cpp(template_code)
    includes = unique_lines(includes_s + includes_t)
    use_using = bool(using_s or using_t)
    parts = []
    if includes:
        parts.append("\n".join(includes))
    if use_using:
        parts.append("using namespace std;")
    if body_s:
        parts.append(body_s)
    if body_t:
        parts.append(body_t)
    new_code = "\n\n".join(parts).strip() + "\n"
    Path(solution_path).write_text(new_code)
    return True


def update_js(solution_path, template_code):
    solution_code = Path(solution_path).read_text()
    if has_js_main(solution_code):
        return False
    template_code = strip_class_block(template_code, "Solution").strip()
    combined = solution_code.rstrip()
    if template_code:
        combined = combined + "\n\n" + template_code
    Path(solution_path).write_text(combined.rstrip() + "\n")
    return True


def extract_problem_id(md_path):
    stem = Path(md_path).stem
    parts = stem.split("-")
    if len(parts) >= 2 and parts[1].isdigit():
        return f"{parts[0]}-{parts[1]}"
    return None


def process_section(section):
    base_dir = ROOT_DIR / "dsa-problems" / section
    problems_dir = base_dir / "problems"
    solutions_dir = base_dir / "solutions"
    updated = []

    for md_path in sorted(problems_dir.glob("*.md")):
        if md_path.name == "README.md":
            continue
        problem_id = extract_problem_id(md_path)
        if not problem_id:
            continue
        for lang, config in LANG_CONFIG.items():
            pattern = str(solutions_dir / lang / f"{problem_id}*.{config['ext']}")
            files = glob.glob(pattern)
            if not files:
                continue
            template_code = extract_template_code(md_path, config["tags"])
            if not template_code:
                continue
            solution_path = files[0]
            if lang == "java":
                if update_java(solution_path, template_code):
                    updated.append(solution_path)
            elif lang == "cpp":
                if update_cpp(solution_path, template_code):
                    updated.append(solution_path)
            elif lang == "javascript":
                if update_js(solution_path, template_code):
                    updated.append(solution_path)
    return updated


def main():
    parser = argparse.ArgumentParser(description="Append mains to solutions from templates")
    parser.add_argument("sections", nargs="+", help="Sections to process (e.g., Stacks Strings StringsClassic)")
    args = parser.parse_args()

    total_updated = []
    for section in args.sections:
        total_updated.extend(process_section(section))

    print(f"Updated {len(total_updated)} files")


if __name__ == "__main__":
    main()
