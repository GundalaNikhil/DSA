#!/usr/bin/env python3
import os
import sys
import yaml
import subprocess
from pathlib import Path
import time

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
        start_time = time.time()
        result = subprocess.run(
            ['python3', solution_file],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        duration = time.time() - start_time
        return result.stdout.strip(), result.stderr, duration
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT", 5.0
    except Exception as e:
        return None, str(e), 0.0

def test_solution(problem_id, solution_file, test_cases_file):
    print(f"\n{BLUE}Testing: {problem_id}{RESET}")
    
    try:
        test_data = load_test_cases(test_cases_file)
    except Exception as e:
        print(f"{RED}Error loading YAML: {e}{RESET}")
        return {
            'samples': {'passed': 0, 'failed': 1, 'failures': [{'test_num': 0, 'input': '', 'expected': '', 'got': f'YAML Error: {e}'}]},
            'public': {'passed': 0, 'failed': 0, 'failures': []},
            'hidden': {'passed': 0, 'failed': 0, 'failures': []}
        }

    results = {
        'samples': {'passed': 0, 'failed': 0, 'failures': []},
        'public': {'passed': 0, 'failed': 0, 'failures': []},
        'hidden': {'passed': 0, 'failed': 0, 'failures': []}
    }
    
    for category in ['samples', 'public', 'hidden']:
        if category not in test_data or not test_data[category]:
            continue
            
        print(f"  Running {category} ({len(test_data[category])} tests)...", end='', flush=True)
            
        for idx, test_case in enumerate(test_data[category], 1):
            input_data = str(test_case['input'])
            expected_output = str(test_case['output']).strip()
            
            actual_output, error, duration = run_solution(solution_file, input_data)
            
            if error and error != "TIMEOUT" and error != "":
                pass
            
            if actual_output is None: # TIMEOUT
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data[:100] + "...", 'expected': expected_output[:100], 'got': "TIMEOUT"
                })
            elif actual_output.strip() == expected_output:
                results[category]['passed'] += 1
            else:
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data[:100] + "...", 'expected': expected_output[:100], 'got': actual_output[:100]
                })
        
        print(f" Done.")
    
    return results

def main():
    base_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced")
    solutions_dir = base_dir / "solutions" / "python"
    testcases_dir = base_dir / "testcases"
    
    solution_files = sorted(solutions_dir.glob("MTH-*.py"))
    
    if not solution_files:
        print(f"{RED}No solutions found in {solutions_dir}{RESET}")
        return

    overall_results = {}
    all_passed = True
    
    for solution_file in solution_files:
        problem_id = solution_file.stem
        # Look for corresponding yaml.
        test_cases_file = testcases_dir / f"{problem_id}.yaml"
        if not test_cases_file.exists():
            prefix = problem_id.split('-')[0] + '-' + problem_id.split('-')[1]
            candidates = list(testcases_dir.glob(f"{prefix}*.yaml"))
            if candidates:
                test_cases_file = candidates[0]
            else:
                print(f"{YELLOW}Warning: No test cases found for {problem_id}{RESET}")
                continue
        
        results = test_solution(problem_id, str(solution_file), str(test_cases_file))
        overall_results[problem_id] = results
        
        for category in ['samples', 'public', 'hidden']:
            total = results[category]['passed'] + results[category]['failed']
            if total == 0:
                continue
                
            if results[category]['failed'] > 0:
                all_passed = False
                print(f"    {category.upper()}: {RED}{results[category]['passed']}/{total} PASSED{RESET}")
                if results[category]['failures']:
                    fail = results[category]['failures'][0]
                    print(f"      First Fail: Exp '{fail['expected']}' Got '{fail['got']}'")
            else:
                print(f"    {category.upper()}: {GREEN}{results[category]['passed']}/{total} PASSED{RESET}")

    print(f"\n{BLUE}{'='*80}{RESET}\n{BLUE}FINAL SUMMARY{RESET}\n{BLUE}{'='*80}{RESET}")
    for pid, res in overall_results.items():
        total_p = sum(res[c]['passed'] for c in res)
        total_f = sum(res[c]['failed'] for c in res)
        total = total_p + total_f
        status = f"{GREEN}PASS{RESET}" if total_f == 0 else f"{RED}FAIL{RESET}"
        print(f"{pid}: {status} ({total_p}/{total})")
    
    if all_passed:
        print(f"\n{GREEN}✓ ALL MTH PROBLEMS PASSED!{RESET}")
    else:
        print(f"\n{RED}✗ Some problems failed. {RESET}")

if __name__ == "__main__":
    main()
