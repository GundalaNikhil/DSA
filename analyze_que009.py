#!/usr/bin/env python3
"""Analyze QUE-009 testcase pattern"""
import yaml

def analyze_array(arr, expected):
    """Try different hypotheses"""
    # Find first negative
    first_neg = None
    for val in arr:
        if val < 0:
            first_neg = val
            break

    # Find first negative index
    first_neg_idx = -1
    for i, val in enumerate(arr):
        if val < 0:
            first_neg_idx = i
            break

    # Sum of negatives
    sum_neg = sum(x for x in arr if x < 0)

    # Count negatives
    count_neg = sum(1 for x in arr if x < 0)

    # Min value
    min_val = min(arr)

    # Max value
    max_val = max(arr)

    print(f"Array length: {len(arr)}, Expected: {expected}")
    print(f"  First negative: {first_neg} (idx: {first_neg_idx})")
    print(f"  Sum of negatives: {sum_neg}")
    print(f"  Count negatives: {count_neg}")
    print(f"  Min: {min_val}, Max: {max_val}")

    # Check matches
    candidates = []
    if first_neg == expected:
        candidates.append("first_negative")
    if first_neg_idx == expected:
        candidates.append("first_negative_index")
    if sum_neg == expected:
        candidates.append("sum_negatives")
    if count_neg == expected:
        candidates.append("count_negatives")
    if min_val == expected:
        candidates.append("min_value")
    if max_val == expected:
        candidates.append("max_value")

    if candidates:
        print(f"  ✓ MATCH: {candidates}")
    else:
        print(f"  ✗ No match")
    print()

# Load testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-009-battery-lab-first-negative.yaml', 'r') as f:
    data = yaml.safe_load(f)

print("Analyzing QUE-009 patterns...")
print("=" * 60)

# Analyze samples
for test in data['samples'][:3]:
    lines = test['input'].strip().split('\n')
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    expected = int(test['output'])
    analyze_array(arr, expected)

print("\nPublic testcases:")
for test in data['public'][:2]:
    lines = test['input'].strip().split('\n')
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    expected = int(test['output'])
    analyze_array(arr, expected)
