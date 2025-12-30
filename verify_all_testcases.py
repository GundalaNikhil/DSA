#!/usr/bin/env python3
"""Verify all Queue testcases have non-empty outputs"""
import yaml
import os
from pathlib import Path

base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases"

issues = []

for yaml_file in sorted(Path(base_path).glob("QUE-*.yaml")):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    problem_id = yaml_file.stem

    # Check all sections
    for section in ['samples', 'public', 'hidden']:
        if section not in data:
            continue

        empty_count = 0
        total_count = len(data[section])

        for idx, test in enumerate(data[section]):
            output = test.get('output', '')
            if output == '' or output is None:
                empty_count += 1

        if empty_count > 0:
            issues.append({
                'problem': problem_id,
                'section': section,
                'empty': empty_count,
                'total': total_count
            })

print("TESTCASE OUTPUT VERIFICATION")
print("=" * 70)

if not issues:
    print("✅ ALL TESTCASES HAVE NON-EMPTY OUTPUTS")
else:
    print(f"❌ FOUND {len(issues)} SECTIONS WITH EMPTY OUTPUTS:\n")
    for issue in issues:
        print(f"  {issue['problem']}: {issue['section']} section has {issue['empty']}/{issue['total']} empty outputs")

print("\n" + "=" * 70)
print(f"Total sections with issues: {len(issues)}")
