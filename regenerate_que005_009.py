#!/usr/bin/env python3
"""Regenerate testcases for QUE-005 and QUE-009"""
import subprocess
import yaml
import os

def run_solution(solution_path, test_input):
    """Run a solution and get its output"""
    try:
        result = subprocess.run(
            ['python3', solution_path],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip(), result.returncode == 0
    except:
        return "", False

def regenerate_testcase_file(problem_id, solution_path, original_yaml_path):
    """Regenerate testcases for one problem"""
    print(f"\nRegenerating {problem_id}...")

    # Load original testcases
    with open(original_yaml_path, 'r') as f:
        original_data = yaml.safe_load(f)

    # Process each testcase section
    new_data = {
        'problem_id': original_data.get('problem_id', ''),
        'samples': [],
        'public': [],
        'hidden': []
    }

    for section in ['samples', 'public', 'hidden']:
        if section not in original_data:
            continue

        for idx, test in enumerate(original_data[section]):
            input_str = test['input']
            output, success = run_solution(solution_path, input_str)

            if success:
                print(f"  {section}[{idx}]: ✓")
            else:
                print(f"  {section}[{idx}]: ERROR")
                output = ""

            new_data[section].append({
                'input': input_str,
                'output': output
            })

    # Save regenerated testcases
    with open(original_yaml_path, 'w') as f:
        yaml.dump(new_data, f, default_flow_style=False, sort_keys=False)

    print(f"✓ Saved regenerated testcases")

# Main
base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues"

problems = [
    ("QUE-005", "QUE-005-lab-printer-reversal"),
    ("QUE-009", "QUE-009-customer-service-queue", "QUE-009-battery-lab-first-negative"),
]

for prob_spec in problems:
    if len(prob_spec) == 2:
        prob_id, prob_name = prob_spec
        sol_name = prob_name
        test_name = prob_name
    else:
        prob_id, sol_name, test_name = prob_spec

    solution_path = f"{base_path}/solutions/python/{sol_name}.py"
    testcase_path = f"{base_path}/testcases/{test_name}.yaml"

    if not os.path.exists(solution_path):
        print(f"Solution not found: {solution_path}")
        continue

    if not os.path.exists(testcase_path):
        print(f"Testcase not found: {testcase_path}")
        continue

    regenerate_testcase_file(prob_id, solution_path, testcase_path)

print("\n" + "=" * 60)
print("Regeneration complete!")
print("=" * 60)
