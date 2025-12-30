#!/usr/bin/env python3
"""Final comprehensive testcase regeneration"""
import subprocess
import yaml
import os
from pathlib import Path

def run_solution(solution_path, test_input):
    """Run solution safely"""
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

problems = [
    ("QUE-001", "QUE-001-campus-service-line"),
    ("QUE-002", "QUE-002-circular-shuttle-buffer-overwrite"),
    ("QUE-003", "QUE-003-cafeteria-queue-rotation"),
    ("QUE-004", "QUE-004-hallway-interleave"),
    ("QUE-005", "QUE-005-lab-printer-reversal"),
    ("QUE-006", "QUE-006-ticket-window-distinct-prefix"),
    ("QUE-007", "QUE-007-lab-window-instability"),
    ("QUE-008", "QUE-008-corridor-window-second-minimum"),
    ("QUE-009", "QUE-009-customer-service-queue", "QUE-009-battery-lab-first-negative"),
    ("QUE-010", "QUE-010-shuttle-seat-assignment"),
    ("QUE-011", "QUE-011-event-registration-merge"),
    ("QUE-012", "QUE-012-bus-loop-one-skip"),
    ("QUE-013", "QUE-013-task-stream-rate-limit"),
    ("QUE-014", "QUE-014-deque-balance-rearrange"),
    ("QUE-015", "QUE-015-festival-lantern-spread"),
    ("QUE-016", "QUE-016-assembly-line-buffer-swap"),
]

print("=" * 70)
print("FINAL COMPREHENSIVE QUEUE TESTCASE REGENERATION")
print("=" * 70)

success_count = 0

for prob_spec in problems:
    if len(prob_spec) == 2:
        prob_id, name = prob_spec
        sol_name = name
        test_name = name
    else:
        prob_id, sol_name, test_name = prob_spec

    solution_path = f"{base_path}/solutions/python/{sol_name}.py"
    testcase_path = f"{base_path}/testcases/{test_name}.yaml"

    if not os.path.exists(solution_path) or not os.path.exists(testcase_path):
        print(f"❌ {prob_id}: Files missing")
        continue

    # Load original testcases
    with open(testcase_path, 'r') as f:
        original_data = yaml.safe_load(f)

    # Regenerate
    new_data = {
        'problem_id': original_data.get('problem_id', ''),
        'samples': [],
        'public': [],
        'hidden': []
    }

    total = 0
    empty = 0
    failed = 0

    for section in ['samples', 'public', 'hidden']:
        if section not in original_data:
            continue

        for test in original_data[section]:
            total += 1
            input_str = test['input']
            output, success = run_solution(solution_path, input_str)

            if not success or output is None:
                output = ""
                failed += 1
            elif output == "":
                empty += 1

            new_data[section].append({
                'input': input_str,
                'output': output
            })

    # Save regenerated testcases
    with open(testcase_path, 'w') as f:
        yaml.dump(new_data, f, default_flow_style=False, sort_keys=False)

    if failed == 0 and empty == 0:
        print(f"✅ {prob_id}: {total} tests regenerated (0 failures, 0 empty)")
        success_count += 1
    else:
        print(f"⚠️  {prob_id}: {total} tests ({failed} failures, {empty} empty)")

print("\n" + "=" * 70)
print(f"Successfully regenerated: {success_count}/16 problems")
print("=" * 70)
