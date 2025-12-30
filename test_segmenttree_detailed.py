#!/usr/bin/env python3
import os
import yaml
import subprocess
from collections import defaultdict

def run_detailed_test(solution_file, testcase_file):
    """Run tests and return detailed results"""
    try:
        with open(testcase_file, 'r') as f:
            testcases_obj = yaml.safe_load(f)

        test_cases = []
        if 'samples' in testcases_obj:
            test_cases.extend(testcases_obj['samples'])
        if 'public' in testcases_obj:
            test_cases.extend(testcases_obj['public'])

        if not test_cases:
            return None, 0, 0, []

        total_tests = len(test_cases)
        passed = 0
        failed_tests = []

        for idx, test in enumerate(test_cases):
            try:
                input_data = test.get('input', '')
                expected_output = test.get('output', '')

                result = subprocess.run(
                    ['python3', solution_file],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                actual_output = result.stdout.strip()
                expected_output_str = str(expected_output).strip() if expected_output else ""

                if actual_output == expected_output_str:
                    passed += 1
                else:
                    failed_tests.append({
                        'index': idx,
                        'expected': expected_output_str[:50],
                        'actual': actual_output[:50]
                    })
            except subprocess.TimeoutExpired:
                failed_tests.append({'index': idx, 'error': 'Timeout'})
            except Exception as e:
                failed_tests.append({'index': idx, 'error': str(e)})

        accuracy = (passed / total_tests * 100) if total_tests > 0 else 0
        return accuracy, passed, total_tests, failed_tests

    except Exception as e:
        return None, 0, 0, []

def main():
    solutions_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/solutions/python"
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases"

    solution_files = sorted([f for f in os.listdir(solutions_dir) if f.endswith('.py')])

    print("\n" + "="*100)
    print("DETAILED SEGMENTTREE VALIDATION")
    print("="*100)

    all_results = []
    total_passed = 0
    total_tests = 0

    for sol_file in solution_files:
        problem_id = sol_file.split('-')[0] + '-' + sol_file.split('-')[1]

        testcase_file = None
        for f in os.listdir(testcases_dir):
            if f.startswith(problem_id) and f.endswith('.yaml'):
                testcase_file = os.path.join(testcases_dir, f)
                break

        if not testcase_file:
            print(f"\n❌ {sol_file}: Testcase file not found")
            continue

        solution_path = os.path.join(solutions_dir, sol_file)
        accuracy, passed, total, failed = run_detailed_test(solution_path, testcase_file)

        if accuracy is None:
            print(f"\n❌ {sol_file}: Error loading test cases")
            continue

        all_results.append({
            'file': sol_file,
            'accuracy': accuracy,
            'passed': passed,
            'total': total,
            'failed': failed
        })
        total_passed += passed
        total_tests += total

        status = "✓" if accuracy == 100.0 else "✗"
        print(f"\n{status} {sol_file}")
        print(f"   Tests: {passed}/{total} passed ({accuracy:.1f}%)")
        if failed:
            print(f"   Failed: {len(failed)} test(s)")
            for fail in failed[:1]:
                print(f"     - Test {fail.get('index', '?')}: {fail.get('error', 'Mismatch')}")

    # Final Summary
    print("\n" + "="*100)
    print("FINAL SUMMARY")
    print("="*100)

    passed_100 = sum(1 for r in all_results if r['accuracy'] == 100.0)
    print(f"\n✓ Problems with 100% accuracy: {passed_100}/{len(all_results)}")
    print(f"✓ Total tests passed: {total_passed}/{total_tests}")
    print(f"✓ Overall accuracy: {(total_passed/total_tests*100):.2f}%")

    # Detailed breakdown
    print("\nProblem-wise Results:")
    for r in all_results:
        status = "✓" if r['accuracy'] == 100.0 else "✗"
        print(f"  {status} {r['file']:55} {r['passed']:3}/{r['total']:3} ({r['accuracy']:6.2f}%)")

    print("\n" + "="*100)
    if passed_100 == len(all_results):
        print("✅ ALL SEGMENTTREE PROBLEMS ARE 100% ACCURATE!")
    print("="*100 + "\n")

if __name__ == "__main__":
    main()
