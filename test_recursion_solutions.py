#!/usr/bin/env python3
"""Test script for Recursion module solutions"""

import os
import sys
import yaml
import subprocess
import json
from pathlib import Path

RECURSION_DIR = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Recursion")
SOLUTIONS_DIR = RECURSION_DIR / "solutions" / "python"
TESTCASES_DIR = RECURSION_DIR / "testcases"

def load_testcases(testcase_file):
    """Load testcases from YAML file"""
    with open(testcase_file, 'r') as f:
        data = yaml.safe_load(f)

    if not data:
        return []

    # Collect all testcases from samples, public, and hidden
    all_testcases = []
    for section in ['samples', 'public', 'hidden']:
        if section in data:
            all_testcases.extend(data[section])

    return all_testcases

def run_solution(solution_file, test_input):
    """Run a solution with given input"""
    try:
        result = subprocess.run(
            ['python3', str(solution_file)],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT", -1
    except Exception as e:
        return None, str(e), -1

def find_file_by_pattern(directory, pattern):
    """Find file by pattern matching"""
    for file in directory.glob(f"{pattern}*.py" if "solution" in str(directory) else f"{pattern}*.yaml"):
        return file
    return None

def test_problem(problem_id):
    """Test a single problem"""
    solution_file = find_file_by_pattern(SOLUTIONS_DIR, problem_id)
    testcase_file = find_file_by_pattern(TESTCASES_DIR, problem_id)

    if not solution_file:
        return f"Solution not found for {problem_id}"

    if not testcase_file:
        return f"Testcases not found for {problem_id}"

    testcases = load_testcases(testcase_file)
    if not testcases:
        return f"No testcases found for {problem_id}"

    passed = 0
    failed = 0
    results = []

    for i, tc in enumerate(testcases, 1):
        if 'input' not in tc or 'output' not in tc:
            continue

        test_input = tc['input']
        expected_output = str(tc['output']).strip()

        actual_output, stderr, returncode = run_solution(solution_file, test_input)

        if actual_output is None:
            failed += 1
            results.append({
                'test': i,
                'status': 'ERROR',
                'error': stderr
            })
        elif actual_output == expected_output:
            passed += 1
            results.append({'test': i, 'status': 'PASS'})
        else:
            failed += 1
            results.append({
                'test': i,
                'status': 'FAIL',
                'expected': expected_output[:100],
                'actual': actual_output[:100]
            })

    return {
        'problem': problem_id,
        'passed': passed,
        'failed': failed,
        'total': passed + failed,
        'details': results
    }

def main():
    """Test all Recursion problems"""
    problems = sorted([
        f"REC-{i:03d}" for i in range(1, 17)
    ])

    all_results = []
    total_passed = 0
    total_failed = 0

    print("=" * 80)
    print("RECURSION MODULE TEST RESULTS")
    print("=" * 80)

    for problem_id in problems:
        result = test_problem(problem_id)

        if isinstance(result, str):
            print(f"\n{problem_id}: {result}")
        else:
            all_results.append(result)
            passed = result['passed']
            failed = result['failed']
            total = result['total']
            total_passed += passed
            total_failed += failed

            status = "✓ PASS" if failed == 0 else "✗ FAIL"
            print(f"{problem_id}: {status} ({passed}/{total})")

            if failed > 0 and failed <= 3:
                for detail in result['details']:
                    if detail['status'] != 'PASS':
                        print(f"  Test {detail['test']}: {detail['status']}")
                        if 'error' in detail:
                            print(f"    Error: {detail['error'][:100]}")
                        if 'expected' in detail:
                            print(f"    Expected: {detail['expected']}")
                            print(f"    Got: {detail['actual']}")

    print("\n" + "=" * 80)
    print(f"TOTAL: {total_passed}/{total_passed + total_failed} tests passed")
    print(f"Success Rate: {100 * total_passed / (total_passed + total_failed) if total_passed + total_failed > 0 else 0:.1f}%")
    print("=" * 80)

    return 0 if total_failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
