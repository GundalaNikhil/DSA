#!/usr/bin/env python3
"""Regenerate QUE-005 testcases with fixed solution"""
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

# Process all testcases
new_data = {
    'problem_id': data.get('problem_id', ''),
    'samples': [],
    'public': [],
    'hidden': []
}

for section in ['samples', 'public', 'hidden']:
    if section not in data:
        continue

    for idx, test in enumerate(data[section]):
        input_str = test['input']
        output, success = run_solution(solution_path, input_str)

        print(f"{section}[{idx}]: {output[:30] if output else 'EMPTY'}...")

        new_data[section].append({
            'input': input_str,
            'output': output
        })

# Save regenerated testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-005-lab-printer-reversal.yaml', 'w') as f:
    yaml.dump(new_data, f, default_flow_style=False, sort_keys=False)

print("\n✓ Regenerated QUE-005 testcases")
