#!/usr/bin/env python3

import os
import yaml
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

# Configuration
SORTING_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting"
SOLUTIONS_DIR = f"{SORTING_DIR}/solutions/python"
TESTCASES_DIR = f"{SORTING_DIR}/testcases"

def load_test_cases(problem_id):
    """Load test cases for a problem"""
    test_file = f"{TESTCASES_DIR}/{problem_id}.yaml"
    if not os.path.exists(test_file):
        return None

    with open(test_file, 'r') as f:
        data = yaml.safe_load(f)

    return data

def run_solution(solution_file, test_input):
    """Run a solution with given input and return output"""
    try:
        result = subprocess.run(
            ['python3', solution_file],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip(), result.returncode, result.stderr
    except subprocess.TimeoutExpired:
        return None, -1, "Timeout"
    except Exception as e:
        return None, -1, str(e)

def test_solution(problem_id, solution_file):
    """Test a single solution against all test cases"""
    test_data = load_test_cases(problem_id)
    if not test_data:
        return None, "No test data found"

    results = {
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Test samples
    if 'samples' in test_data:
        for idx, test_case in enumerate(test_data['samples']):
            input_data = test_case.get('input', '').strip()
            expected_output = test_case.get('output', '').strip()

            actual_output, returncode, error = run_solution(solution_file, input_data)

            if actual_output is None:
                results['samples'].append({
                    'index': idx,
                    'passed': False,
                    'error': error
                })
            else:
                passed = actual_output == expected_output
                results['samples'].append({
                    'index': idx,
                    'passed': passed,
                    'expected': expected_output,
                    'actual': actual_output
                })

    # Test public
    if 'public' in test_data:
        for idx, test_case in enumerate(test_data['public']):
            input_data = test_case.get('input', '').strip()
            expected_output = test_case.get('output', '').strip()

            actual_output, returncode, error = run_solution(solution_file, input_data)

            if actual_output is None:
                results['public'].append({
                    'index': idx,
                    'passed': False,
                    'error': error
                })
            else:
                passed = actual_output == expected_output
                results['public'].append({
                    'index': idx,
                    'passed': passed,
                    'expected': expected_output,
                    'actual': actual_output
                })

    # Test hidden
    if 'hidden' in test_data:
        for idx, test_case in enumerate(test_data['hidden']):
            input_data = test_case.get('input', '').strip()
            expected_output = test_case.get('output', '').strip()

            actual_output, returncode, error = run_solution(solution_file, input_data)

            if actual_output is None:
                results['hidden'].append({
                    'index': idx,
                    'passed': False,
                    'error': error
                })
            else:
                passed = actual_output == expected_output
                results['hidden'].append({
                    'index': idx,
                    'passed': passed,
                    'expected': expected_output,
                    'actual': actual_output
                })

    return results, None

def main():
    """Main test runner"""
    solutions = sorted([f for f in os.listdir(SOLUTIONS_DIR) if f.endswith('.py')])

    print("=" * 80)
    print("SORTING PROBLEMS - PYTHON SOLUTIONS TEST REPORT")
    print("=" * 80)
    print()

    summary = defaultdict(lambda: {'total': 0, 'passed': 0, 'failed': 0})
    all_passed = True

    for solution_file in solutions:
        problem_id = solution_file.replace('.py', '')
        solution_path = f"{SOLUTIONS_DIR}/{solution_file}"

        results, error = test_solution(problem_id, solution_path)

        if error:
            print(f"FAIL {problem_id}: {error}")
            all_passed = False
            continue

        # Summarize results
        sample_passed = sum(1 for r in results['samples'] if r.get('passed', False))
        public_passed = sum(1 for r in results['public'] if r.get('passed', False))
        hidden_passed = sum(1 for r in results['hidden'] if r.get('passed', False))

        sample_total = len(results['samples'])
        public_total = len(results['public'])
        hidden_total = len(results['hidden'])

        total = sample_total + public_total + hidden_total
        passed = sample_passed + public_passed + hidden_passed
        failed = total - passed

        summary['overall']['total'] += total
        summary['overall']['passed'] += passed
        summary['overall']['failed'] += failed

        status = "PASS" if failed == 0 else "FAIL"
        print(f"{status} {problem_id}")
        print(f"   Samples: {sample_passed}/{sample_total} | Public: {public_passed}/{public_total} | Hidden: {hidden_passed}/{hidden_total}")

        if failed > 0:
            all_passed = False
            # Show first failure
            for test_type in ['samples', 'public', 'hidden']:
                for test in results[test_type]:
                    if not test.get('passed', False):
                        print(f"   First failure in {test_type}[{test['index']}]:")
                        if 'error' in test:
                            print(f"     Error: {test['error']}")
                        else:
                            print(f"     Expected: {test.get('expected', '')[:80]}")
                            print(f"     Got:      {test.get('actual', '')[:80]}")
                        break
                if not all_passed and failed > 0:
                    break
        print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total test cases: {summary['overall']['total']}")
    print(f"Passed: {summary['overall']['passed']}")
    print(f"Failed: {summary['overall']['failed']}")
    print(f"Success Rate: {100 * summary['overall']['passed'] / summary['overall']['total']:.1f}%")
    print()

    if all_passed:
        print("ALL TESTS PASSED - 100% ACCURACY!")
        return 0
    else:
        print("SOME TESTS FAILED - NEEDS FIXES")
        return 1

if __name__ == "__main__":
    sys.exit(main())
