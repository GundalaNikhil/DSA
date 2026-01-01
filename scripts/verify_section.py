#!/usr/bin/env python3
"""
Verification script for a section's problems using their solution files.
Falls back to templates if a solution lacks a main.
"""

import argparse
import glob
import re
import subprocess
import tempfile
import time
from pathlib import Path

import yaml


ROOT_DIR = Path(__file__).parent.parent

LANG_CONFIG = {
    "python": {
        "ext": "py",
        "compile": None,
        "run": lambda file: ["python3", file],
    },
    "java": {
        "ext": "java",
        "compile": lambda file: ["javac", file],
        "run": lambda file, workdir: ["java", "-cp", workdir, "Main"],
    },
    "cpp": {
        "ext": "cpp",
        "compile": lambda file: ["g++", "-std=c++17", "-O2", file, "-o", file.replace(".cpp", ".out")],
        "run": lambda file: [file.replace(".cpp", ".out")],
    },
    "javascript": {
        "ext": "js",
        "compile": None,
        "run": lambda file: ["node", file],
    },
}


def load_testcases(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    testcases = []
    for key in ("samples", "public", "visible", "hidden"):
        if key in data:
            testcases.extend(data[key])
    cleaned = []
    for t in testcases:
        inp = str(t.get("input", "")).strip()
        out = str(t.get("output", "")).strip()
        cleaned.append({"input": inp, "output": out})
    return cleaned


def extract_problem_id(testcase_path):
    stem = Path(testcase_path).stem
    parts = stem.split("-")
    if len(parts) >= 2 and parts[1].isdigit():
        return f"{parts[0]}-{parts[1]}"
    return None


def find_problem_md(base_dir, problem_id):
    pattern = str(base_dir / "problems" / f"{problem_id}*.md")
    files = glob.glob(pattern)
    return files[0] if files else None


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


def build_java_combined(solution_path, template_code):
    solution_code = Path(solution_path).read_text()
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
    return "\n\n".join(parts).strip() + "\n"


def build_cpp_combined(solution_path, template_code):
    solution_code = Path(solution_path).read_text()
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
    return "\n\n".join(parts).strip() + "\n"


def build_js_combined(solution_path, template_code):
    solution_code = Path(solution_path).read_text().strip()
    template_code = strip_class_block(template_code, "Solution").strip()
    parts = []
    if solution_code:
        parts.append(solution_code)
    if template_code:
        parts.append(template_code)
    return "\n\n".join(parts).strip() + "\n"


def prepare_solution(base_dir, problem_id, lang, temp_dir):
    config = LANG_CONFIG[lang]
    pattern = str(base_dir / "solutions" / lang / f"{problem_id}*.{config['ext']}")
    files = glob.glob(pattern)
    if not files:
        return None
    solution_path = files[0]
    solution_code = Path(solution_path).read_text()

    if lang == "python":
        return {"run": config["run"](solution_path), "compile": None, "workdir": None}

    if lang == "java" and has_java_main(solution_code):
        out_file = Path(temp_dir) / "Main.java"
        out_file.write_text(solution_code)
        return {
            "run": config["run"](str(out_file), str(temp_dir)),
            "compile": config["compile"](str(out_file)),
            "workdir": str(temp_dir),
        }

    if lang == "cpp" and has_cpp_main(solution_code):
        out_file = Path(temp_dir) / Path(solution_path).name
        out_file.write_text(solution_code)
        return {
            "run": config["run"](str(out_file)),
            "compile": config["compile"](str(out_file)),
            "workdir": str(temp_dir),
        }

    if lang == "javascript" and has_js_main(solution_code):
        out_file = Path(temp_dir) / Path(solution_path).name
        out_file.write_text(solution_code)
        return {"run": config["run"](str(out_file)), "compile": None, "workdir": str(temp_dir)}

    md_path = find_problem_md(base_dir, problem_id)
    if not md_path:
        return None
    tags = ["java"] if lang == "java" else ["cpp", "c++"] if lang == "cpp" else ["javascript", "js"]
    template_code = extract_template_code(md_path, tags)
    if not template_code:
        return None

    if lang == "java":
        combined = build_java_combined(solution_path, template_code)
        out_file = Path(temp_dir) / "Main.java"
        out_file.write_text(combined)
        return {
            "run": config["run"](str(out_file), str(temp_dir)),
            "compile": config["compile"](str(out_file)),
            "workdir": str(temp_dir),
        }

    if lang == "cpp":
        combined = build_cpp_combined(solution_path, template_code)
        out_file = Path(temp_dir) / "main.cpp"
        out_file.write_text(combined)
        return {
            "run": config["run"](str(out_file)),
            "compile": config["compile"](str(out_file)),
            "workdir": str(temp_dir),
        }

    if lang == "javascript":
        combined = build_js_combined(solution_path, template_code)
        out_file = Path(temp_dir) / "main.js"
        out_file.write_text(combined)
        return {"run": config["run"](str(out_file)), "compile": None, "workdir": str(temp_dir)}

    return None


def run_test(run_cmd, input_data, expected_output, timeout=5, workdir=None):
    try:
        start_time = time.time()
        result = subprocess.run(
            run_cmd,
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=workdir,
        )
        elapsed = time.time() - start_time
        if result.returncode != 0:
            error_msg = result.stderr if result.stderr else result.stdout
            return False, f"Runtime Error: {error_msg[:200]}", elapsed
        actual_output = result.stdout.strip()
        expected = expected_output.strip()
        if actual_output == expected:
            return True, None, elapsed
        return False, f"WA\nExpected:\n{expected[:100]}\nGot:\n{actual_output[:100]}", elapsed
    except subprocess.TimeoutExpired:
        return False, "Time Limit Exceeded", timeout
    except Exception as e:
        return False, f"Runtime Error: {str(e)}", 0


def verify_section(section, languages):
    base_dir = ROOT_DIR / "dsa-problems" / section
    testcases_dir = base_dir / "testcases"
    testcase_files = sorted(p for p in testcases_dir.glob("*.yaml") if p.name != "README.md")

    for testcase_path in testcase_files:
        if "-NEW" in testcase_path.name:
            continue
        problem_id = extract_problem_id(testcase_path)
        if not problem_id:
            continue
        testcases = load_testcases(testcase_path)
        if not testcases:
            print(f"No test cases found for {problem_id}")
            continue

        print(f"Verifying {problem_id} ({len(testcases)} tests)...")
        for lang in languages:
            with tempfile.TemporaryDirectory() as temp_dir:
                prepared = prepare_solution(base_dir, problem_id, lang, temp_dir)
                if not prepared:
                    print(f"[{lang}] Solution/template not found")
                    continue

                compile_cmd = prepared["compile"]
                if compile_cmd:
                    try:
                        compile_result = subprocess.run(
                            compile_cmd,
                            capture_output=True,
                            text=True,
                            timeout=10,
                            cwd=prepared["workdir"],
                        )
                        if compile_result.returncode != 0:
                            print(f"[{lang}] Compilation failed:\n{compile_result.stderr}")
                            continue
                    except subprocess.TimeoutExpired:
                        print(f"[{lang}] Compilation timeout")
                        continue

                print(f"[{lang}] Testing {problem_id}")
                passed = 0
                for i, test in enumerate(testcases, 1):
                    success, error, elapsed = run_test(
                        prepared["run"],
                        test.get("input", ""),
                        test.get("output", ""),
                        workdir=prepared["workdir"],
                    )
                    if success:
                        passed += 1
                    else:
                        print(f"  Test {i}: FAIL ({elapsed:.3f}s) -> {error[:150]}...")
                        if i >= 7:
                            print("  ...stopping validation for this language.")
                            break
                print(f"[{lang}] Result: {passed}/{len(testcases)} passed.")
        print()


def main():
    parser = argparse.ArgumentParser(description="Verify section solutions")
    parser.add_argument("section", help="Section name (e.g., Stacks, Strings, StringsClassic)")
    parser.add_argument(
        "--langs",
        nargs="+",
        choices=["python", "java", "cpp", "javascript"],
        default=["python", "java", "cpp", "javascript"],
        help="Languages to test",
    )
    args = parser.parse_args()

    verify_section(args.section, args.langs)


if __name__ == "__main__":
    main()
