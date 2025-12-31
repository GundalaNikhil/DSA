#!/usr/bin/env python3
"""
Regenerate TreesDP test cases from current solutions.
Takes existing test case inputs and regenerates outputs from solutions.
"""

import yaml
import subprocess
import glob
from pathlib import Path

def run_solution(problem_id, input_data):
    """Run solution and get output."""
    solution_files = glob.glob(f"dsa-problems/TreesDP/solutions/python/{problem_id}-*.py")
    if not solution_files:
        return None

    try:
        result = subprocess.run(
            ['python3', solution_files[0]],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return None

def regenerate_test_cases(problem_id):
    """Regenerate test cases for a problem using current solution."""
    yaml_files = glob.glob(f"dsa-problems/TreesDP/testcases/{problem_id}-*.yaml")
    if not yaml_files:
        print(f"{problem_id}: No test case file found")
        return False

    yaml_path = yaml_files[0]

    try:
        with open(yaml_path, 'r') as f:
            test_data = yaml.safe_load(f)
    except:
        print(f"{problem_id}: Failed to load YAML")
        return False

    updated_tests = {'samples': [], 'public': [], 'hidden': []}

    for category in ['samples', 'public', 'hidden']:
        if category not in test_data:
            continue

        for test_case in test_data[category]:
            input_str = test_case['input'].strip()
            output = run_solution(problem_id, input_str)

            if output:
                updated_tests[category].append({
                    'input': input_str,
                    'output': output
                })

    # Write back
    test_data['samples'] = updated_tests['samples']
    test_data['public'] = updated_tests['public']
    test_data['hidden'] = updated_tests['hidden']

    with open(yaml_path, 'w') as f:
        yaml.dump(test_data, f, default_flow_style=False, sort_keys=False,
                 allow_unicode=True, width=float('inf'))

    total_tests = sum(len(v) for v in updated_tests.values())
    print(f"{problem_id}: ✓ Regenerated {total_tests} test cases")
    return True

def main():
    print("Regenerating TreesDP test cases from current solutions...")
    print("="*60)

    successful = 0
    for problem_num in range(1, 17):
        problem_id = f"TDP-{problem_num:03d}"
        if regenerate_test_cases(problem_id):
            successful += 1

    print("="*60)
    print(f"Successfully regenerated {successful}/16 problem test cases")

if __name__ == '__main__':
    main()
