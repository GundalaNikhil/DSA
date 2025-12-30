#!/usr/bin/env python3

import os
import sys
import yaml
import subprocess
from pathlib import Path

SOLUTIONS_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/solutions/python"
TESTCASES_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases"

def load_testcase(problem_id):
    """Load testcase YAML"""
    testcase_files = list(Path(TESTCASES_DIR).glob(f"{problem_id}-*.yaml"))
    if not testcase_files:
        return None

    testcase_path = str(testcase_files[0])
    try:
        with open(testcase_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except:
        return None

def test_solution(problem_id):
    """Test solution by running it with stdin/stdout"""
    # Find solution file
    solutions = list(Path(SOLUTIONS_DIR).glob(f"{problem_id}-*.py"))
    if not solutions:
        return {"status": "NO_FILE", "passed": 0, "total": 0}

    solution_path = str(solutions[0])

    # Load testcases
    testcase = load_testcase(problem_id)
    if not testcase:
        return {"status": "NO_TESTCASE", "passed": 0, "total": 0}

    # Get hidden tests
    test_cases = testcase.get('hidden', [])
    if not test_cases:
        test_cases = testcase.get('public', [])

    if not test_cases:
        return {"status": "NO_TESTS", "passed": 0, "total": 0}

    passed = 0
    failed = []

    for idx, test_case in enumerate(test_cases):
        try:
            input_str = test_case.get('input', '')
            expected_str = test_case.get('output', '')

            # Run solution with input
            result = subprocess.run(
                ['python3', solution_path],
                input=input_str,
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode != 0:
                failed.append({
                    "index": idx,
                    "error": f"Non-zero exit: {result.stderr[:100]}"
                })
                continue

            output = result.stdout.strip()
            expected = expected_str.strip()

            # Exact string comparison
            if output == expected:
                passed += 1
            else:
                # Try line-by-line comparison for multi-line output
                output_lines = output.split('\n')
                expected_lines = expected.split('\n')

                if len(output_lines) != len(expected_lines):
                    failed.append({
                        "index": idx,
                        "input": input_str[:50],
                        "expected": expected,
                        "got": output
                    })
                    continue

                # Compare each line
                match = True
                for out_line, exp_line in zip(output_lines, expected_lines):
                    out_parts = out_line.split()
                    exp_parts = exp_line.split()

                    if len(out_parts) != len(exp_parts):
                        match = False
                        break

                    # Try numeric comparison if possible
                    for out_part, exp_part in zip(out_parts, exp_parts):
                        try:
                            out_float = float(out_part)
                            exp_float = float(exp_part)
                            if abs(out_float - exp_float) > 0.001 * max(abs(exp_float), 1):
                                match = False
                                break
                        except:
                            if out_part != exp_part:
                                match = False
                                break

                    if not match:
                        break

                if match:
                    passed += 1
                else:
                    failed.append({
                        "index": idx,
                        "input": input_str[:50],
                        "expected": expected,
                        "got": output
                    })

        except subprocess.TimeoutExpired:
            failed.append({
                "index": idx,
                "error": "Timeout"
            })
        except Exception as e:
            failed.append({
                "index": idx,
                "error": str(e)[:100]
            })

    total = len(test_cases)
    return {
        "status": "OK",
        "passed": passed,
        "total": total,
        "success": passed == total,
        "failures": failed if failed else None
    }

def main():
    print("="*60)
    print("Testing Queues Solutions (stdin/stdout)")
    print("="*60 + "\n")

    results = {}
    for i in range(1, 17):
        problem_id = f"QUE-{i:03d}"
        print(f"Testing {problem_id}...", end=" ", flush=True)

        result = test_solution(problem_id)
        results[problem_id] = result

        if result['status'] == 'OK':
            if result['success']:
                print(f"✓ PASSED ({result['passed']}/{result['total']})")
            else:
                print(f"✗ FAILED ({result['passed']}/{result['total']})")
        else:
            print(f"✗ {result['status']}")

    # Summary
    print("\n" + "="*60)
    print("COMPREHENSIVE TEST REPORT")
    print("="*60)

    total_passed = 0
    total_tests = 0
    failures = {}

    for problem_id, result in sorted(results.items()):
        if result['status'] == 'OK':
            total_passed += result['passed']
            total_tests += result['total']
            if not result['success']:
                failures[problem_id] = result['failures']

            status = "✓ PASS" if result['success'] else "✗ FAIL"
            print(f"{problem_id}: {status} ({result['passed']}/{result['total']})")
        else:
            print(f"{problem_id}: {result['status']}")

    print("="*60)
    if total_tests > 0:
        print(f"Success Rate: {total_passed}/{total_tests} = {100*total_passed/total_tests:.1f}%")
    print("="*60)

    if failures:
        print("\nFAILURES DETAILS (First 2 per problem):")
        print("="*60)
        for problem_id, failure_list in sorted(failures.items()):
            print(f"\n{problem_id}:")
            for failure in failure_list[:2]:
                print(f"  Test #{failure['index']}:")
                if 'error' in failure:
                    print(f"    Error: {failure['error']}")
                else:
                    print(f"    Expected: {failure.get('expected', 'N/A')[:80]}")
                    print(f"    Got: {failure.get('got', 'N/A')[:80]}")

if __name__ == "__main__":
    main()
