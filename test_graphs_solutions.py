#!/usr/bin/env python3
"""
Comprehensive test script for all Graphs Python solutions.
Tests against samples, public, and hidden test cases.
"""

import os
import sys
import yaml
import subprocess
from pathlib import Path

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def load_test_cases(yaml_file):
    """Load test cases from YAML file."""
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    return data

def run_solution(solution_file, input_data):
    """Run a Python solution with given input and return output."""
    try:
        result = subprocess.run(
            ['python3', solution_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip(), result.stderr
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:
        return None, str(e)

def test_solution(problem_id, solution_file, test_cases_file):
    """Test a solution against all test cases."""
    print(f"\n{BLUE}{'='*80}{RESET}")
    print(f"{BLUE}Testing: {problem_id}{RESET}")
    print(f"{BLUE}{'='*80}{RESET}")
    
    # Load test cases
    test_data = load_test_cases(test_cases_file)
    
    results = {
        'samples': {'passed': 0, 'failed': 0, 'failures': []},
        'public': {'passed': 0, 'failed': 0, 'failures': []},
        'hidden': {'passed': 0, 'failed': 0, 'failures': []}
    }
    
    # Test each category
    for category in ['samples', 'public', 'hidden']:
        if category not in test_data or not test_data[category]:
            continue
            
        print(f"\n{YELLOW}Testing {category.upper()}:{RESET}")
        
        for idx, test_case in enumerate(test_data[category], 1):
            input_data = test_case['input']
            expected_output = test_case['output'].strip()
            
            actual_output, error = run_solution(solution_file, input_data)
            
            if error and error != "":
                print(f"  Test {idx}: {RED}ERROR{RESET}")
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx,
                    'input': input_data,
                    'expected': expected_output,
                    'got': f"ERROR: {error}",
                    'error': error
                })
            elif actual_output is None:
                print(f"  Test {idx}: {RED}TIMEOUT{RESET}")
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx,
                    'input': input_data,
                    'expected': expected_output,
                    'got': "TIMEOUT"
                })
            elif actual_output.strip() == expected_output:
                print(f"  Test {idx}: {GREEN}PASS{RESET}")
                results[category]['passed'] += 1
            else:
                print(f"  Test {idx}: {RED}FAIL{RESET}")
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx,
                    'input': input_data,
                    'expected': expected_output,
                    'got': actual_output
                })
    
    return results

def main():
    """Main function to test all Graphs solutions."""
    base_dir = Path(__file__).parent / "dsa-problems" / "Graphs"
    solutions_dir = base_dir / "solutions" / "python"
    testcases_dir = base_dir / "testcases"
    
    # Get all Python solutions
    solution_files = sorted(solutions_dir.glob("GRP-*.py"))
    
    if not solution_files:
        print(f"{RED}No solution files found!{RESET}")
        return
    
    print(f"{BLUE}Found {len(solution_files)} Graphs solutions to test{RESET}")
    
    overall_results = {}
    all_passed = True
    
    for solution_file in solution_files:
        problem_id = solution_file.stem
        test_cases_file = testcases_dir / f"{problem_id}.yaml"
        
        if not test_cases_file.exists():
            print(f"{YELLOW}Warning: No test cases found for {problem_id}{RESET}")
            continue
        
        results = test_solution(problem_id, str(solution_file), str(test_cases_file))
        overall_results[problem_id] = results
        
        # Check if all tests passed
        for category in ['samples', 'public', 'hidden']:
            if results[category]['failed'] > 0:
                all_passed = False
    
    # Print summary
    print(f"\n{BLUE}{'='*80}{RESET}")
    print(f"{BLUE}SUMMARY{RESET}")
    print(f"{BLUE}{'='*80}{RESET}")
    
    for problem_id, results in overall_results.items():
        samples_total = results['samples']['passed'] + results['samples']['failed']
        public_total = results['public']['passed'] + results['public']['failed']
        hidden_total = results['hidden']['passed'] + results['hidden']['failed']
        
        samples_status = f"{results['samples']['passed']}/{samples_total}" if samples_total > 0 else "N/A"
        public_status = f"{results['public']['passed']}/{public_total}" if public_total > 0 else "N/A"
        hidden_status = f"{results['hidden']['passed']}/{hidden_total}" if hidden_total > 0 else "N/A"
        
        all_tests_passed = (
            results['samples']['failed'] == 0 and
            results['public']['failed'] == 0 and
            results['hidden']['failed'] == 0
        )
        
        status_color = GREEN if all_tests_passed else RED
        status_symbol = "✓" if all_tests_passed else "✗"
        
        print(f"\n{status_color}{status_symbol} {problem_id}{RESET}")
        print(f"  Samples: {samples_status} | Public: {public_status} | Hidden: {hidden_status}")
        
        # Show failures if any
        for category in ['samples', 'public', 'hidden']:
            if results[category]['failures']:
                print(f"\n  {RED}{category.upper()} FAILURES:{RESET}")
                for failure in results[category]['failures']:
                    print(f"    Test {failure['test_num']}:")
                    print(f"      Input: {failure['input'][:100]}...")
                    print(f"      Expected: {failure['expected'][:100]}")
                    print(f"      Got: {failure['got'][:100]}")
    
    print(f"\n{BLUE}{'='*80}{RESET}")
    if all_passed:
        print(f"{GREEN}✓ ALL TESTS PASSED! 100% SUCCESS!{RESET}")
    else:
        print(f"{RED}✗ Some tests failed. Please review the failures above.{RESET}")
    print(f"{BLUE}{'='*80}{RESET}")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
