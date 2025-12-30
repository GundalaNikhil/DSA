#!/usr/bin/env python3
import os
import yaml
import sys
import subprocess
from pathlib import Path
from collections import defaultdict

def run_test(solution_file, testcase_file):
    """Run a single test case against a solution"""
    try:
        with open(testcase_file, 'r') as f:
            testcases_obj = yaml.safe_load(f)

        if not testcases_obj:
            return None, "No test cases found"

        # Extract test cases from samples and public
        test_cases = []
        if 'samples' in testcases_obj:
            test_cases.extend(testcases_obj['samples'])
        if 'public' in testcases_obj:
            test_cases.extend(testcases_obj['public'])

        if not test_cases:
            return None, "No test cases found in samples or public"

        total_tests = len(test_cases)
        passed = 0
        failed_tests = []

        for idx, test in enumerate(test_cases):
            try:
                input_data = test.get('input', '')
                expected_output = test.get('output', '')

                # Run the solution
                result = subprocess.run(
                    ['python3', solution_file],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5
                )

                actual_output = result.stdout.strip()
                expected_output_str = str(expected_output).strip() if expected_output else ""

                if actual_output == expected_output_str:
                    passed += 1
                else:
                    failed_tests.append({
                        'index': idx,
                        'input': input_data[:50] if len(input_data) > 50 else input_data,
                        'expected': expected_output_str[:100],
                        'actual': actual_output[:100]
                    })
            except subprocess.TimeoutExpired:
                failed_tests.append({
                    'index': idx,
                    'error': 'Timeout'
                })
            except Exception as e:
                failed_tests.append({
                    'index': idx,
                    'error': str(e)
                })

        accuracy = (passed / total_tests * 100) if total_tests > 0 else 0
        return accuracy, failed_tests

    except Exception as e:
        return None, f"Error loading test cases: {str(e)}"

def main():
    solutions_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/solutions/python"
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases"

    results = {}

    # Get all solution files
    solution_files = sorted([f for f in os.listdir(solutions_dir) if f.endswith('.py')])

    print("=" * 80)
    print("SEGMENTTREE SOLUTIONS TEST REPORT")
    print("=" * 80)

    for sol_file in solution_files:
        problem_id = sol_file.split('-')[0] + '-' + sol_file.split('-')[1]

        # Find the matching testcase file
        testcase_file = None
        for f in os.listdir(testcases_dir):
            if f.startswith(problem_id) and f.endswith('.yaml'):
                testcase_file = os.path.join(testcases_dir, f)
                break

        if not testcase_file:
            results[sol_file] = {'accuracy': None, 'error': 'Testcase file not found'}
            print(f"\n{sol_file}: ❌ Testcase not found")
            continue

        solution_path = os.path.join(solutions_dir, sol_file)
        print(f"\n{sol_file}")

        accuracy, failures = run_test(solution_path, testcase_file)

        if accuracy is None:
            print(f"  ❌ ERROR: {failures}")
            results[sol_file] = {'accuracy': None, 'error': failures}
        else:
            status = "✓" if accuracy == 100.0 else "✗"
            print(f"  {status} Accuracy: {accuracy:.2f}% ({len([f for f in failures if 'index' in f])}/{len(failures) + int(accuracy * len(failures) / 100)} failed)")
            if failures:
                print(f"    Failed Tests:")
                for fail in failures[:3]:  # Show first 3 failures
                    if 'error' in fail:
                        print(f"      Test {fail.get('index', '?')}: {fail['error']}")
                    else:
                        print(f"      Test {fail.get('index', '?')}: Expected '{fail.get('expected', '')[:50]}' got '{fail.get('actual', '')[:50]}'")
            results[sol_file] = {'accuracy': accuracy, 'failures': failures}

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    passed_count = sum(1 for r in results.values() if r.get('accuracy') == 100.0)
    total_count = len([r for r in results.values() if r.get('accuracy') is not None])

    print(f"\nProblems with 100% accuracy: {passed_count}/{total_count}")
    print("\nDetailed Results:")

    for sol_file in sorted(results.keys()):
        r = results[sol_file]
        if r.get('accuracy') is not None:
            status = "✓" if r['accuracy'] == 100.0 else "✗"
            print(f"{status} {sol_file}: {r['accuracy']:.2f}%")
        else:
            print(f"✗ {sol_file}: ERROR - {r.get('error', 'Unknown')}")

if __name__ == "__main__":
    main()
