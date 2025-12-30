#!/usr/bin/env python3
import os
import yaml
import subprocess

def run_test(solution_file, testcase_file):
    """Run sample and public tests only"""
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
                failed_tests.append({'index': idx, 'error': str(e)[:50]})

        accuracy = (passed / total_tests * 100) if total_tests > 0 else 0
        return accuracy, passed, total_tests, failed_tests

    except Exception as e:
        return None, 0, 0, [{'error': f'Error: {str(e)[:50]}'}]

def main():
    solutions_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/solutions/python"
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases"

    solution_files = sorted([f for f in os.listdir(solutions_dir) if f.endswith('.py')])

    print("\n" + "="*100)
    print("SEGMENTTREE - SAMPLES & PUBLIC TEST VALIDATION")
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
            for fail in failed[:1]:
                if 'error' in fail:
                    print(f"     Test {fail.get('index', '?')}: {fail['error']}")
                else:
                    print(f"     Test {fail.get('index', '?')}: Mismatch")

    # Summary
    print("\n" + "="*100)
    print("SUMMARY")
    print("="*100)

    print(f"\n✓ Problems with 100% accuracy: {problem_passed}/{len(all_results)}")
    print(f"✓ Total tests passed: {total_passed}/{total_tests} ({(total_passed/total_tests*100):.2f}%)")

    print("\nResults:")
    for r in all_results:
        status = "✓" if r['accuracy'] == 100.0 else "✗"
        print(f"{status} {r['file']:55} {r['passed']:2}/{r['total']:2} ({r['accuracy']:6.2f}%)")

    print("\n" + "="*100)
    if problem_passed == len(all_results):
        print("✅ ALL PROBLEMS PASS SAMPLES & PUBLIC TESTS!")
    else:
        print(f"⚠️  {len(all_results) - problem_passed} problems need fixing")
    print("="*100 + "\n")

if __name__ == "__main__":
    main()
