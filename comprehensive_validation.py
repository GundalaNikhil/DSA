#!/usr/bin/env python3
"""
Comprehensive validation of all SegmentTree solutions against expanded test cases
Tests: samples + public only (not hidden, since hidden are generated/not validated)
"""

import os
import yaml
import subprocess
import sys

def run_test(solution_file, testcase_file):
    """Run samples and public tests only"""
    try:
        with open(testcase_file, 'r') as f:
            testcases_obj = yaml.safe_load(f)

        test_cases = []
        # Only test samples and public, not hidden
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
                        'expected': expected_output_str[:80],
                        'actual': actual_output[:80]
                    })
            except subprocess.TimeoutExpired:
                failed_tests.append({
                    'index': idx,
                    'error': 'Timeout',
                    'input_preview': input_data.split('\n')[0][:50]
                })
            except Exception as e:
                failed_tests.append({
                    'index': idx,
                    'error': str(e)[:80]
                })

        accuracy = (passed / total_tests * 100) if total_tests > 0 else 0
        return accuracy, passed, total_tests, failed_tests

    except Exception as e:
        return None, 0, 0, [{'error': f'Error: {str(e)[:80]}'}]

def main():
    solutions_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/solutions/python"
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases"

    solution_files = sorted([f for f in os.listdir(solutions_dir) if f.endswith('.py')])

    print("\n" + "="*100)
    print("COMPREHENSIVE SEGMENTTREE VALIDATION")
    print("Testing: Samples (2) + Public (3) = 5 tests per problem")
    print("="*100)

    all_results = []
    total_passed = 0
    total_tests = 0
    problem_passed = 0

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
        accuracy, passed, total, failed = run_test(solution_path, testcase_file)

        if accuracy is None:
            print(f"\n❌ {sol_file}: Error loading test cases")
            continue

        all_results.append({
            'file': sol_file,
            'problem_id': problem_id,
            'accuracy': accuracy,
            'passed': passed,
            'total': total,
            'failed': failed
        })
        total_passed += passed
        total_tests += total
        if accuracy == 100.0:
            problem_passed += 1

        status = "✓" if accuracy == 100.0 else "✗"
        print(f"\n{status} {sol_file}")
        print(f"   Tests: {passed}/{total} passed ({accuracy:.1f}%)")

        if failed:
            print(f"   Failed: {len(failed)} test(s)")
            for fail in failed[:2]:
                if 'error' in fail:
                    print(f"     Test {fail.get('index', '?')}: {fail['error']}")
                else:
                    print(f"     Test {fail.get('index', '?')}: Output mismatch")

    # Summary
    print("\n" + "="*100)
    print("COMPREHENSIVE VALIDATION SUMMARY")
    print("="*100)

    print(f"\n✓ Problems with 100% accuracy: {problem_passed}/{len(all_results)}")
    print(f"✓ Total tests passed: {total_passed}/{total_tests} ({(total_passed/total_tests*100):.2f}%)")

    print("\nDetailed Results:")
    print(f"{'Status':<7} {'Problem':<60} {'Pass Rate':<15}")
    print("-" * 82)

    for r in sorted(all_results, key=lambda x: -x['accuracy']):
        status = "✓" if r['accuracy'] == 100.0 else "✗"
        filename = r['file'][:58]
        print(f"{status:<7} {filename:<60} {r['passed']}/{r['total']} ({r['accuracy']:6.2f}%)")

    print("\n" + "="*100)
    if problem_passed == len(all_results):
        print("✅ ALL PROBLEMS PASS ALL SAMPLES & PUBLIC TESTS!")
        print("✅ SegmentTree test case generation and validation COMPLETE!")
    else:
        print(f"⚠️  {len(all_results) - problem_passed} problems have failures")
        print("\nFailed Problems:")
        for r in all_results:
            if r['accuracy'] < 100.0:
                print(f"  - {r['problem_id']}: {r['accuracy']:.1f}%")
    print("="*100 + "\n")

    return 0 if problem_passed == len(all_results) else 1

if __name__ == "__main__":
    sys.exit(main())
