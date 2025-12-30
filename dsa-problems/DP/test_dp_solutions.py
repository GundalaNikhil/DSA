#!/usr/bin/env python3
"""
Test runner for DP Python solutions against hidden test cases
"""
import yaml
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

def load_test_cases(yaml_file):
    """Load test cases from a YAML file"""
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    all_tests = []

    # Add sample tests
    if 'samples' in data:
        for test in data['samples']:
            all_tests.append(('sample', test))

    # Add public tests
    if 'public' in data:
        for test in data['public']:
            all_tests.append(('public', test))

    # Add hidden tests
    if 'hidden' in data:
        for test in data['hidden']:
            all_tests.append(('hidden', test))

    return all_tests

def run_solution(python_file, test_input):
    """Run a Python solution with given input"""
    try:
        # Don't strip the test_input as it may have significant whitespace
        result = subprocess.run(
            ['python3', str(python_file)],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return None, -1
    except Exception as e:
        return str(e), -1

def test_solution(solution_file, test_cases):
    """Test a single solution against all test cases"""
    results = {
        'sample': {'passed': 0, 'failed': 0, 'failures': []},
        'public': {'passed': 0, 'failed': 0, 'failures': []},
        'hidden': {'passed': 0, 'failed': 0, 'failures': []}
    }

    for test_type, test in test_cases:
        # Don't strip input - preserve significant whitespace
        test_input = test['input'].rstrip('\n')
        expected_output = test['output'].strip()

        actual_output, returncode = run_solution(solution_file, test_input)

        if returncode != 0:
            results[test_type]['failed'] += 1
            results[test_type]['failures'].append({
                'input': test_input,
                'expected': expected_output,
                'actual': f'Error (code {returncode})',
                'full_output': actual_output
            })
        elif actual_output == expected_output:
            results[test_type]['passed'] += 1
        else:
            results[test_type]['failed'] += 1
            results[test_type]['failures'].append({
                'input': test_input,
                'expected': expected_output,
                'actual': actual_output
            })

    return results

def main():
    solutions_dir = Path('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/DP/solutions/python')
    testcases_dir = Path('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/DP/testcases')

    # Get all solution files
    solution_files = sorted(solutions_dir.glob('*.py'))

    overall_results = defaultdict(lambda: {'passed': 0, 'failed': 0, 'solutions_failed': []})

    print("=" * 80)
    print("DP SOLUTIONS TEST REPORT")
    print("=" * 80)

    for solution_file in solution_files:
        problem_id = solution_file.stem
        testcase_file = testcases_dir / f"{problem_id}.yaml"

        if not testcase_file.exists():
            print(f"\n⚠️  SKIP: {problem_id} (no test cases found)")
            continue

        # Load test cases
        test_cases = load_test_cases(testcase_file)

        # Run tests
        results = test_solution(solution_file, test_cases)

        # Print results
        total_sample = results['sample']['passed'] + results['sample']['failed']
        total_public = results['public']['passed'] + results['public']['failed']
        total_hidden = results['hidden']['passed'] + results['hidden']['failed']

        all_passed = all(
            results[t]['failed'] == 0
            for t in ['sample', 'public', 'hidden']
        )

        status = "✅ PASS" if all_passed else "❌ FAIL"

        print(f"\n{status} {problem_id}")
        print(f"    Sample: {results['sample']['passed']}/{total_sample}")
        print(f"    Public: {results['public']['passed']}/{total_public}")
        print(f"    Hidden: {results['hidden']['passed']}/{total_hidden}")

        # Show failures
        for test_type in ['sample', 'public', 'hidden']:
            if results[test_type]['failures']:
                print(f"\n    {test_type.upper()} FAILURES:")
                for i, failure in enumerate(results[test_type]['failures'][:3], 1):  # Show first 3
                    print(f"      Test {i}:")
                    print(f"        Input: {failure['input'][:100]}")
                    print(f"        Expected: {failure['expected'][:100]}")
                    print(f"        Got: {failure['actual'][:100]}")
                if len(results[test_type]['failures']) > 3:
                    print(f"      ... and {len(results[test_type]['failures']) - 3} more failures")

        # Track overall stats
        for test_type in ['sample', 'public', 'hidden']:
            overall_results[test_type]['passed'] += results[test_type]['passed']
            overall_results[test_type]['failed'] += results[test_type]['failed']
            if results[test_type]['failed'] > 0:
                overall_results[test_type]['solutions_failed'].append(problem_id)

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for test_type in ['sample', 'public', 'hidden']:
        stats = overall_results[test_type]
        total = stats['passed'] + stats['failed']
        pct = (stats['passed'] / total * 100) if total > 0 else 0
        print(f"\n{test_type.upper()}: {stats['passed']}/{total} ({pct:.1f}%)")
        if stats['solutions_failed']:
            print(f"  Failed solutions: {', '.join(stats['solutions_failed'][:5])}", end='')
            if len(stats['solutions_failed']) > 5:
                print(f" ... and {len(stats['solutions_failed']) - 5} more")
            else:
                print()

if __name__ == '__main__':
    main()
