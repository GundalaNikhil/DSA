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
                pass
            
            if actual_output is None:
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data, 'expected': expected_output, 'got': "TIMEOUT"
                })
                continue
            
            # Custom validation for HSH-011
            if "HSH-011" in problem_id:
                try:
                    lines = actual_output.strip().split()
                    if len(lines) != 2:
                        raise ValueError("Output must contain exactly 2 strings")
                    s1, s2 = lines[0], lines[1]
                    
                    # Parse input
                    B, M, L = map(int, input_data.split())
                    
                    if len(s1) != L or len(s2) != L:
                         raise ValueError(f"Strings must be length {L}")
                    if s1 == s2:
                         raise ValueError("Strings must be distinct")
                         
                    # Verify Hash
                    h1 = 0
                    for char in s1:
                        h1 = (h1 * B + ord(char)) % M
                    
                    h2 = 0
                    for char in s2:
                        h2 = (h2 * B + ord(char)) % M
                        
                    if h1 != h2:
                        raise ValueError(f"Hashes do not match: {h1} != {h2}")
                        
                    # If we get here, it's a pass
                    results[category]['passed'] += 1
                    continue
                except Exception as e:
                     results[category]['failed'] += 1
                     results[category]['failures'].append({
                        'test_num': idx, 'input': input_data, 'expected': "Valid Collision", 'got': f"Invalid: {str(e)} Output: {actual_output}"
                     })
                     continue

            if actual_output.strip() == expected_output:
                results[category]['passed'] += 1
            else:
                results[category]['failed'] += 1
                results[category]['failures'].append({
                    'test_num': idx, 'input': input_data, 'expected': expected_output, 'got': actual_output
                })
    
    return results

def main():
    base_dir = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Hashing")
    solutions_dir = base_dir / "solutions" / "python"
    testcases_dir = base_dir / "testcases"
    
    solution_files = sorted(solutions_dir.glob("HSH-*.py"))
    
    overall_results = {}
    all_passed = True
    
    for solution_file in solution_files:
        problem_id = solution_file.stem
        # The solution file stems are like HSH-001-polynomial-hash-prefixes
        # The test case files should match this stem.
        test_cases_file = testcases_dir / f"{problem_id}.yaml"
        if not test_cases_file.exists():
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
                print(f"  {category.upper()}: {RED}{results[category]['passed']}/{total} PASSED{RESET}")
                # Print first failure
                if results[category]['failures']:
                    fail = results[category]['failures'][0]
                    print(f"    First Fail: Exp '{fail['expected']}' Got '{fail['got']}'")
            else:
                print(f"  {category.upper()}: {GREEN}{results[category]['passed']}/{total} PASSED{RESET}")

    print(f"\n{BLUE}{'='*80}{RESET}\n{BLUE}FINAL SUMMARY{RESET}\n{BLUE}{'='*80}{RESET}")
    for pid, res in overall_results.items():
        total_p = sum(res[c]['passed'] for c in res)
        total_f = sum(res[c]['failed'] for c in res)
        total = total_p + total_f
        status = f"{GREEN}PASS{RESET}" if total_f == 0 else f"{RED}FAIL{RESET}"
        print(f"{pid}: {status} ({total_p}/{total})")
    
    if all_passed:
        print(f"\n{GREEN}✓ ALL HASHING PROBLEMS PASSED!{RESET}")
    else:
        print(f"\n{RED}✗ Some problems failed. Starting debugging phase...{RESET}")

if __name__ == "__main__":
    main()
