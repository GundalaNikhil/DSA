#!/usr/bin/env python3
"""
Test script for Stacks module solutions against YAML test cases.
"""

import yaml
import subprocess
import sys
from pathlib import Path

def load_test_cases(problem_id):
    """Load test cases from YAML file."""
    yaml_path = f"dsa-problems/Stacks/testcases/{problem_id}-*.yaml"
    import glob
    files = glob.glob(yaml_path)
    if not files:
        print(f"  No test cases found for {problem_id}")
        return None

    with open(files[0], 'r') as f:
        return yaml.safe_load(f)

def run_test(solution_path, test_input):
    """Run solution and return output."""
    try:
        result = subprocess.run(
            ['python3', solution_path],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {str(e)}"

def test_problem(problem_id, solution_path):
    """Test a single problem."""
    test_cases = load_test_cases(problem_id)
    if not test_cases:
        return None

    passed = 0
    total = 0

    for category in ['samples', 'public', 'hidden']:
        if category not in test_cases:
            continue

        for i, test_case in enumerate(test_cases[category]):
            total += 1
            test_input = test_case['input'].strip()
            expected = test_case['output'].strip()

            actual = run_test(solution_path, test_input)

            if actual == expected:
                passed += 1
            else:
                print(f"  {problem_id} {category}[{i}] FAIL")
                if len(actual) < 100 and len(expected) < 100:
                    print(f"    Expected: {expected}")
                    print(f"    Got:      {actual}")

    return passed, total

def main():
    """Test all Stacks solutions."""
    results = {}
    total_passed = 0
    total_tests = 0

    for problem_num in range(1, 17):
        problem_id = f"STK-{problem_num:03d}"
        solution_path = f"dsa-problems/Stacks/solutions/python/{problem_id}-*.py"

        import glob
        files = glob.glob(solution_path)
        if not files:
            print(f"{problem_id}: Solution file not found")
            continue

        solution_path = files[0]
        print(f"Testing {problem_id}...", end=" ")

        result = test_problem(problem_id, solution_path)
        if result:
            passed, total = result
            results[problem_id] = (passed, total)
            total_passed += passed
            total_tests += total
            pct = int(100 * passed / total) if total > 0 else 0
            status = "✓" if passed == total else "✗"
            print(f"{status} {passed}/{total} ({pct}%)")
        else:
            print("SKIP")

    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)

    for problem_id in sorted(results.keys()):
        passed, total = results[problem_id]
        pct = int(100 * passed / total) if total > 0 else 0
        status = "✓" if passed == total else "✗"
        print(f"{problem_id}: {status} {passed:3d}/{total:3d} ({pct:3d}%)")

    total_pct = int(100 * total_passed / total_tests) if total_tests > 0 else 0
    print("-"*50)
    print(f"TOTAL: {total_passed}/{total_tests} ({total_pct}%)")
    print("="*50)

if __name__ == "__main__":
    main()
