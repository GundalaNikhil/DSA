#!/usr/bin/env python3
"""
Verification script for GraphsBasics problems (GRB-001 to GRB-016).
Tests solutions across Python, Java, C++, and JavaScript.
"""

import subprocess
import sys
import os
import yaml
import argparse
import time
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent / "dsa-problems" / "GraphsBasics"
SOLUTIONS_DIR = BASE_DIR / "solutions"
TESTCASES_DIR = BASE_DIR / "testcases"

# Language configurations
LANG_CONFIG = {
    "python": {
        "ext": "py",
        "compile": None,
        "run": lambda file: ["python3", file]
    },
    "java": {
        "ext": "java",
        "compile": lambda file: ["javac", file],
        "run": lambda file: ["java", "-cp", os.path.dirname(file), "Main"]
    },
    "cpp": {
        "ext": "cpp",
        "compile": lambda file: ["g++", "-std=c++17", "-O2", file, "-o", file.replace(".cpp", ".out")],
        "run": lambda file: [file.replace(".cpp", ".out")]
    },
    "javascript": {
        "ext": "js",
        "compile": None,
        "run": lambda file: ["node", file]
    }
}

def load_testcases(problem_id):
    """Load test cases from YAML file."""
    import glob
    pattern = str(TESTCASES_DIR / f"{problem_id}*.yaml")
    files = glob.glob(pattern)
    
    # Prefer non-NEW files
    files = [f for f in files if '-NEW' not in f]
    if not files:
        # Fallback to NEW files if no regular ones exist
        files = glob.glob(pattern)
    
    if not files:
        return []
    
    with open(files[0], 'r') as f:
        data = yaml.safe_load(f)
    
    testcases = []
    if 'samples' in data:
        testcases.extend(data['samples'])
    if 'public' in data:
        testcases.extend(data['public'])
    if 'visible' in data:
        testcases.extend(data['visible'])
    if 'hidden' in data:
        testcases.extend(data['hidden'])
    
    # Clean testcases
    cleaned = []
    for t in testcases:
        inp = str(t.get('input', '')).strip()
        out = str(t.get('output', '')).strip()
        cleaned.append({'input': inp, 'output': out})
    
    return cleaned


def run_test(solution_file, input_data, expected_output, timeout=5):
    """Run a single test case."""
    lang = None
    for l, config in LANG_CONFIG.items():
        if solution_file.endswith(f".{config['ext']}"):
            lang = l
            break
    
    if not lang:
        return False, "Unknown language", 0
    
    config = LANG_CONFIG[lang]
    
    # Compile if needed
    if config['compile']:
        try:
            compile_result = subprocess.run(
                config['compile'](solution_file),
                capture_output=True,
                text=True,
                timeout=10
            )
            if compile_result.returncode != 0:
                return False, f"Compilation failed for {solution_file}:\n{compile_result.stderr}", 0
        except subprocess.TimeoutExpired:
            return False, "Compilation timeout", 0
        except Exception as e:
            return False, f"Compilation error: {str(e)}", 0
    
    # Run test
    try:
        start_time = time.time()
        result = subprocess.run(
            config['run'](solution_file),
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            error_msg = result.stderr if result.stderr else result.stdout
            return False, f"Runtime Error: {error_msg[:200]}", elapsed
        
        actual_output = result.stdout.strip()
        expected = expected_output.strip()
        
        if actual_output == expected:
            return True, None, elapsed
        else:
            return False, f"WA\nExpected:\n{expected[:100]}\nGot:\n{actual_output[:100]}", elapsed
            
    except subprocess.TimeoutExpired:
        return False, "Time Limit Exceeded", timeout
    except Exception as e:
        return False, f"Runtime Error: {str(e)}", 0

def verify_problem(problem_id, languages=None):
    """Verify a single problem across specified languages."""
    if languages is None:
        languages = ["python", "java", "cpp", "javascript"]
    
    testcases = load_testcases(problem_id)
    if not testcases:
        print(f"No test cases found for {problem_id}")
        return
    
    print(f"Verifying {problem_id} ({len(testcases)} tests)...")
    
    for lang in languages:
        import glob
        config = LANG_CONFIG[lang]
        pattern = str(SOLUTIONS_DIR / lang / f"{problem_id}*.{config['ext']}")
        files = glob.glob(pattern)
        
        if not files:
            print(f"[{lang}] Solution file not found")
            continue
        
        solution_file = files[0]
        print(f"[{lang}] Testing {os.path.basename(solution_file)}")
        
        passed = 0
        failed_early = False
        
        for i, test in enumerate(testcases, 1):
            input_data = test.get('input', '')
            expected_output = test.get('output', '')
            
            success, error, elapsed = run_test(str(solution_file), input_data, expected_output)
            
            if success:
                passed += 1
            else:
                print(f"  Test {i}: FAIL ({elapsed:.3f}s) -> {error[:150]}...")
                if passed < 5:  # Stop early if multiple early failures
                    failed_early = True
                if i >= 7 and not success:  # Stop after 7 failures
                    print(f"  ...stopping validation for this language.")
                    break
        
        print(f"[{lang}] Result: {passed}/{len(testcases)} passed.")

def main():
    parser = argparse.ArgumentParser(description='Verify GraphsBasics solutions')
    parser.add_argument('problem', nargs='?', help='Problem ID (e.g., GRB-001) or "all"')
    parser.add_argument('--langs', nargs='+', choices=['python', 'java', 'cpp', 'javascript'],
                       help='Languages to test', default=['python', 'java', 'cpp', 'javascript'])
    
    args = parser.parse_args()
    
    if args.problem and args.problem != 'all':
        verify_problem(args.problem, args.langs)
    else:
        # Verify all problems GRB-001 to GRB-016
        for i in range(1, 17):
            problem_id = f"GRB-{i:03d}"
            verify_problem(problem_id, args.langs)
            print()

if __name__ == "__main__":
    main()
