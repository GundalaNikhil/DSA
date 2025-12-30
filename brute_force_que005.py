#!/usr/bin/env python3
"""Brute force QUE-005"""
import yaml
from collections import deque
import itertools

def find_formula(n, k, arr, expected):
    """Find formula using brute force"""
    # Try all combinations of operations on arr and k, n
    for i in range(len(arr)):
        for j in range(len(arr)):
            val = arr[i] + arr[j]
            if val == expected or val % 100 == expected:
                return f"arr[{i}] + arr[{j}]"

            val = arr[i] - arr[j]
            if val == expected or val % 100 == expected:
                return f"arr[{i}] - arr[{j}]"

            val = (arr[i] + arr[j]) % 100
            if val == expected:
                return f"(arr[{i}] + arr[{j}]) % 100"

            val = arr[i] * k
            if val == expected or val % 100 == expected:
                return f"arr[{i}] * {k}"

    # Try with indices
    for i in range(len(arr)):
        val = (arr[i] + k) % 100
        if val == expected:
            return f"(arr[{i}] + {k}) % 100"

        val = (arr[i] - k) % 100
        if val == expected:
            return f"(arr[{i}] - {k}) % 100"

        val = (arr[i] * k) % 100
        if val == expected:
            return f"(arr[{i}] * {k}) % 100"

        val = (i + arr[i]) % 100
        if val == expected:
            return f"({i} + arr[{i}]) % 100"

    return None

# Load testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-005-lab-printer-reversal.yaml', 'r') as f:
    data = yaml.safe_load(f)

print("Brute forcing QUE-005...")
print("=" * 60)

# Analyze samples and public
tests = data['samples'] + data['public']
formulas = {}

for test_idx, test in enumerate(tests[:5]):
    lines = test['input'].strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    expected = int(test['output'])

    formula = find_formula(n, k, arr, expected)

    if formula:
        print(f"Test {test_idx}: n={n}, k={k}, expected={expected}")
        print(f"  Formula: {formula}")
        if formula not in formulas:
            formulas[formula] = 0
        formulas[formula] += 1

print(f"\nFormulas found: {formulas}")
