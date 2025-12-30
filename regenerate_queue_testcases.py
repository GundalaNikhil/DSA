#!/usr/bin/env python3
"""Regenerate testcases for Queue problems after fixes"""
import subprocess
import yaml
import os
from pathlib import Path

def run_solution(solution_path, test_input):
    """Run solution and get output"""
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
        return None, False

base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues"

# Problems that were just fixed
problems = [
    ("QUE-008", "QUE-008-corridor-window-second-minimum"),
    ("QUE-011", "QUE-011-event-registration-merge"),
    ("QUE-012", "QUE-012-bus-loop-one-skip"),
    ("QUE-013", "QUE-013-task-stream-rate-limit"),
    ("QUE-015", "QUE-015-festival-lantern-spread"),
    ("QUE-016", "QUE-016-assembly-line-buffer-swap"),
]

for prob_id, prob_name in problems:
    solution_path = f"{base_path}/solutions/python/{prob_name}.py"
    testcase_path = f"{base_path}/testcases/{prob_name}.yaml"

    if not os.path.exists(solution_path):
        print(f"❌ {prob_id}: Solution not found")
        continue

    if not os.path.exists(testcase_path):
        print(f"❌ {prob_id}: Testcase not found")
        continue

    # Load testcases
    with open(testcase_path, 'r') as f:
        data = yaml.safe_load(f)

    # Regenerate all outputs
    new_data = {'problem_id': data.get('problem_id', ''), 'samples': [], 'public': [], 'hidden': []}

    total = 0
    fixed = 0

    for section in ['samples', 'public', 'hidden']:
        if section not in data:
            continue

        for test in data[section]:
            total += 1
            input_str = test['input']
            output, success = run_solution(solution_path, input_str)

            if output is None:
                # Solution crashed, keep empty
                new_data[section].append({'input': input_str, 'output': ''})
            else:
                # Got output from solution
                if output == '':
                    # Still empty
                    new_data[section].append({'input': input_str, 'output': ''})
                else:
                    # Got actual output
                    fixed += 1
                    new_data[section].append({'input': input_str, 'output': output})

    # Save regenerated testcases
    with open(testcase_path, 'w') as f:
        yaml.dump(new_data, f, default_flow_style=False, sort_keys=False)

    print(f"✅ {prob_id}: Regenerated {total} tests, fixed {fixed} empty outputs")

print("\n✅ Done regenerating testcases!")
