#!/usr/bin/env python3
"""Find which QUE-005 testcases pass"""
import subprocess
import yaml

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
        if result.returncode == 0:
            return result.stdout.strip(), True
        return "", False
    except:
        return "", False

# Load testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-005-lab-printer-reversal.yaml', 'r') as f:
    data = yaml.safe_load(f)

solution_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/solutions/python/QUE-005-lab-printer-reversal.py'

print("Finding passing testcases for QUE-005...")
passing = []
failing = []

for section in ['samples', 'public', 'hidden']:
    if section not in data:
        continue

    for idx, test in enumerate(data[section][:10]):  # First 10 of each
        input_str = test['input']
        expected_output = test['output']

        actual_output, success = run_solution(solution_path, input_str)

        if success and actual_output == expected_output:
            passing.append((section, idx, input_str[:50], expected_output))
        else:
            failing.append((section, idx, input_str[:50], expected_output, actual_output if success else "ERROR"))

print(f"\nPASSING ({len(passing)}):")
for section, idx, inp, exp in passing:
    print(f"  {section}[{idx}]: {inp}... → {exp}")

print(f"\nFAILING ({len(failing)}):")
for section, idx, inp, exp, act in failing[:5]:
    print(f"  {section}[{idx}]: {inp}... → expected {exp}, got {act}")
