#!/usr/bin/env python3
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
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    return data

def run_solution(solution_file, input_data):
    try:
        result = subprocess.run(
            ['python3', solution_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip(), result.stderr
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:
        return None, str(e)

def test_solution(problem_id, solution_file, test_cases_file):
    print(f"\n{BLUE}Testing: {problem_id}{RESET}")
    
    test_data = load_test_cases(test_cases_file)
    results = {
        'samples': {'passed': 0, 'failed': 0, 'failures': []},
        'public': {'passed': 0, 'failed': 0, 'failures': []},
        'hidden': {'passed': 0, 'failed': 0, 'failures': []}
    }
    
    for category in ['samples', 'public', 'hidden']:
        if category not in test_data or not test_data[category]:
            continue
            
        for idx, test_case in enumerate(test_data[category], 1):
            input_data = test_case['input']
            expected_output = str(test_case['output']).strip()
            
            actual_output, error = run_solution(solution_file, input_data)
            
            if error and error != "":
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data, 'expected': expected_output, 'got': f"ERROR: {error}"
                })
            elif actual_output is None:
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data, 'expected': expected_output, 'got': "TIMEOUT"
                })
            elif actual_output.strip() == expected_output:
                results[category]['passed'] += 1
            else:
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data, 'expected': expected_output, 'got': actual_output
                })
    
    return results

def main():
    base_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Greedy")
    solutions_dir = base_dir / "solutions" / "python"
    testcases_dir = base_dir / "testcases"
    
    solution_files = sorted(solutions_dir.glob("GRD-*.py"))
    
    overall_results = {}
    all_passed = True
    
    for solution_file in solution_files:
        problem_id = solution_file.stem
        test_cases_file = testcases_dir / f"{problem_id}.yaml"
        if not test_cases_file.exists():
            continue
        
        results = test_solution(problem_id, str(solution_file), str(test_cases_file))
        overall_results[problem_id] = results
        
        for category in ['samples', 'public', 'hidden']:
            if results[category]['failed'] > 0:
                all_passed = False
                print(f"  {category.upper()}: {RED}{results[category]['passed']}/{results[category]['passed']+results[category]['failed']} PASSED{RESET}")
            else:
                passed_count = results[category]['passed']
                if passed_count > 0:
                    print(f"  {category.upper()}: {GREEN}{passed_count}/{passed_count} PASSED{RESET}")

    print(f"\n{BLUE}{'='*80}{RESET}\n{BLUE}FINAL SUMMARY{RESET}\n{BLUE}{'='*80}{RESET}")
    for pid, res in overall_results.items():
        total_p = sum(res[c]['passed'] for c in res)
        total_f = sum(res[c]['failed'] for c in res)
        status = f"{GREEN}PASS{RESET}" if total_f == 0 else f"{RED}FAIL{RESET}"
        print(f"{pid}: {status} ({total_p}/{total_p+total_f})")
    
    if all_passed:
        print(f"\n{GREEN}✓ ALL GREEDY PROBLEMS PASSED!{RESET}")
    else:
        print(f"\n{RED}✗ Some problems failed. Starting debugging phase...{RESET}")

if __name__ == "__main__":
    main()
