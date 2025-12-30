#!/usr/bin/env python3
"""Safely regenerate all Queue testcases"""
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

def regenerate_problem(problem_name, sol_name, test_name):
    """Regenerate testcase for one problem"""
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues"
    solution_path = f"{base_path}/solutions/python/{sol_name}.py"
    testcase_path = f"{base_path}/testcases/{test_name}.yaml"

    if not os.path.exists(solution_path):
        print(f"❌ {problem_name}: Solution not found")
        return False

    if not os.path.exists(testcase_path):
        print(f"❌ {problem_name}: Testcase not found")
        return False

    # Load original testcases
    with open(testcase_path, 'r') as f:
        original_data = yaml.safe_load(f)

    # Test first sample to see if solution works
    if 'samples' in original_data and original_data['samples']:
        test_input = original_data['samples'][0]['input']
        output, success = run_solution(solution_path, test_input)

        if not success or output is None:
            print(f"⚠️  {problem_name}: Solution fails on first sample, skipping regeneration")
            return False

    # Regenerate all testcases
    new_data = {
        'problem_id': original_data.get('problem_id', ''),
        'samples': [],
        'public': [],
        'hidden': []
    }

    total_tests = 0
    empty_outputs = 0

    for section in ['samples', 'public', 'hidden']:
        if section not in original_data:
            continue

        for test in original_data[section]:
            total_tests += 1
            input_str = test['input']
            output, success = run_solution(solution_path, input_str)

            if output is None or not success:
                output = ""
                empty_outputs += 1

            new_data[section].append({
                'input': input_str,
                'output': output
            })

    # Only save if we don't have too many empty outputs
    if empty_outputs > total_tests * 0.1:  # More than 10% empty
        print(f"⚠️  {problem_name}: {empty_outputs}/{total_tests} empty outputs, skipping")
        return False

    # Save regenerated testcases
    with open(testcase_path, 'w') as f:
        yaml.dump(new_data, f, default_flow_style=False, sort_keys=False)

    print(f"✅ {problem_name}: Regenerated {total_tests} tests ({empty_outputs} empty)")
    return True

# Main
problems = [
    ("QUE-001", "QUE-001-campus-service-line", "QUE-001-campus-service-line"),
    ("QUE-002", "QUE-002-circular-shuttle-buffer-overwrite", "QUE-002-circular-shuttle-buffer-overwrite"),
    ("QUE-003", "QUE-003-cafeteria-queue-rotation", "QUE-003-cafeteria-queue-rotation"),
    ("QUE-004", "QUE-004-hallway-interleave", "QUE-004-hallway-interleave"),
    ("QUE-005", "QUE-005-lab-printer-reversal", "QUE-005-lab-printer-reversal"),
    ("QUE-006", "QUE-006-ticket-window-distinct-prefix", "QUE-006-ticket-window-distinct-prefix"),
    ("QUE-007", "QUE-007-lab-window-instability", "QUE-007-lab-window-instability"),
    ("QUE-008", "QUE-008-corridor-window-second-minimum", "QUE-008-corridor-window-second-minimum"),
    ("QUE-009", "QUE-009-customer-service-queue", "QUE-009-battery-lab-first-negative"),
    ("QUE-010", "QUE-010-shuttle-seat-assignment", "QUE-010-shuttle-seat-assignment"),
    ("QUE-011", "QUE-011-event-registration-merge", "QUE-011-event-registration-merge"),
    ("QUE-012", "QUE-012-bus-loop-one-skip", "QUE-012-bus-loop-one-skip"),
    ("QUE-013", "QUE-013-task-stream-rate-limit", "QUE-013-task-stream-rate-limit"),
    ("QUE-014", "QUE-014-deque-balance-rearrange", "QUE-014-deque-balance-rearrange"),
    ("QUE-015", "QUE-015-festival-lantern-spread", "QUE-015-festival-lantern-spread"),
    ("QUE-016", "QUE-016-assembly-line-buffer-swap", "QUE-016-assembly-line-buffer-swap"),
]

print("=" * 70)
print("SAFE QUEUE TESTCASE REGENERATION")
print("=" * 70)

success_count = 0
for prob_id, sol_name, test_name in problems:
    if regenerate_problem(prob_id, sol_name, test_name):
        success_count += 1

print("\n" + "=" * 70)
print(f"Successfully regenerated: {success_count}/16 problems")
print("=" * 70)
