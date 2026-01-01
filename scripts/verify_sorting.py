#!/usr/bin/env python3
"""
Verification script for Sorting problems (SRT-001 to SRT-016).
Wraps C++/Java/JS solutions with template mains from problem markdown.
"""

import argparse
import glob
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path

import yaml


BASE_DIR = Path(__file__).parent.parent / "dsa-problems" / "Sorting"
SOLUTIONS_DIR = BASE_DIR / "solutions"
TESTCASES_DIR = BASE_DIR / "testcases"
PROBLEMS_DIR = BASE_DIR / "problems"

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


def load_testcases(problem_id):
    pattern = str(TESTCASES_DIR / f"{problem_id}*.yaml")
    files = glob.glob(pattern)
    files = [f for f in files if "-NEW" not in f]
    if not files:
        files = glob.glob(pattern)
    if not files:
        return []
    with open(files[0], "r") as f:
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


def find_problem_md(problem_id):
    pattern = str(PROBLEMS_DIR / f"{problem_id}*.md")
    files = glob.glob(pattern)
    return files[0] if files else None


def extract_template_code(md_path, lang_tag):
    with open(md_path, "r") as f:
        text = f.read()
    pattern = rf"```{lang_tag}\n(.*?)```"
    match = re.search(pattern, text, flags=re.S)
    if not match:
        return None
    return match.group(1).strip() + "\n"


def has_java_main(code):
    return bool(re.search(r"\bclass\s+Main\b", code) or re.search(r"\bstatic\s+void\s+main\b", code))


def has_cpp_main(code):
    return bool(re.search(r"\bint\s+main\s*\(", code))


def has_js_main(code):
    return "readFileSync(0" in code or "readline.createInterface" in code or "process.stdin" in code


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


def build_java_combined(solution_path, template_code):
    with open(solution_path, "r") as f:
        solution_code = f.read()
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
    with open(solution_path, "r") as f:
        solution_code = f.read()
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
    with open(solution_path, "r") as f:
        solution_code = f.read().strip()
    template_code = strip_class_block(template_code, "Solution").strip()
    parts = []
    if solution_code:
        parts.append(solution_code)
    if template_code:
        parts.append(template_code)
    return "\n\n".join(parts).strip() + "\n"


def prepare_solution(problem_id, lang, temp_dir):
    config = LANG_CONFIG[lang]
    pattern = str(SOLUTIONS_DIR / lang / f"{problem_id}*.{config['ext']}")
    files = glob.glob(pattern)
    if not files:
        return None
    solution_path = files[0]
    with open(solution_path, "r") as f:
        solution_code = f.read()

    if lang == "python":
        return {"run": config["run"](solution_path), "compile": None, "workdir": None}

    if lang == "java" and has_java_main(solution_code):
        out_file = Path(temp_dir) / Path(solution_path).name
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

    md_path = find_problem_md(problem_id)
    if not md_path:
        return None
    lang_tag = "java" if lang == "java" else "cpp" if lang == "cpp" else "javascript"
    template_code = extract_template_code(md_path, lang_tag)
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


def verify_problem(problem_id, languages=None):
    if languages is None:
        languages = ["python", "java", "cpp", "javascript"]

    testcases = load_testcases(problem_id)
    if not testcases:
        print(f"No test cases found for {problem_id}")
        return

    print(f"Verifying {problem_id} ({len(testcases)} tests)...")
    for lang in languages:
        with tempfile.TemporaryDirectory() as temp_dir:
            prepared = prepare_solution(problem_id, lang, temp_dir)
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


def main():
    parser = argparse.ArgumentParser(description="Verify Sorting solutions")
    parser.add_argument("problem", nargs="?", help='Problem ID (e.g., SRT-001) or "all"')
    parser.add_argument(
        "--langs",
        nargs="+",
        choices=["python", "java", "cpp", "javascript"],
        default=["python", "java", "cpp", "javascript"],
        help="Languages to test",
    )
    args = parser.parse_args()

    if args.problem and args.problem != "all":
        verify_problem(args.problem, args.langs)
    else:
        for i in range(1, 17):
            problem_id = f"SRT-{i:03d}"
            verify_problem(problem_id, args.langs)
            print()


if __name__ == "__main__":
    main()
