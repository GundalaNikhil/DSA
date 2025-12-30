#!/usr/bin/env python3
"""Analyze QUE-005 testcase pattern"""
import yaml
from collections import deque

def analyze(n, k, arr, expected):
    """Try different hypotheses"""
    # Hypothesis: reverse first k and rotate
    queue = deque(arr)
    stack = []

    for _ in range(min(k, len(arr))):
        if queue:
            stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(len(arr) - k):
        if queue:
            queue.append(queue.popleft())

    reversed_first_k_rotated = list(queue)

    # Hypothesis: sum of some elements
    sum_first_k = sum(arr[:k])
    sum_last_k = sum(arr[-k:] if k <= len(arr) else arr)

    # Hypothesis: k-th element
    kth_elem = arr[k] if k < len(arr) else -1

    # Hypothesis: sum of first k in reverse
    rev_arr = arr[:k][::-1] if k <= len(arr) else arr[::-1]
    sum_rev = sum(rev_arr)

    # Hypothesis: element at position that depends on k
    # Let's check various modulo operations
    candidates = []

    if sum_first_k == expected:
        candidates.append(f"sum_first_{k}")
    if sum_last_k == expected:
        candidates.append(f"sum_last_{k}")
    if kth_elem == expected:
        candidates.append(f"arr[{k}]")
    if sum_rev == expected:
        candidates.append(f"sum(reversed_first_{k})")

    # Check if any element of result matches
    if expected in reversed_first_k_rotated:
        idx = reversed_first_k_rotated.index(expected)
        candidates.append(f"result[{idx}]_from_reverse_rotate")

    # Specific computation
    val = (arr[k] if k < len(arr) else arr[-1]) + sum(arr[:k]) % 100
    if val == expected:
        candidates.append(f"arr[k] + sum_first_k % 100")

    print(f"n={n}, k={k}, expected={expected}")
    print(f"  sum_first_{k}: {sum_first_k}")
    print(f"  sum_last_{k}: {sum_last_k}")
    print(f"  arr[{k}]: {kth_elem}")
    if candidates:
        print(f"  ✓ MATCH: {candidates}")
    else:
        print(f"  ✗ No match")
    print()

# Load testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-005-lab-printer-reversal.yaml', 'r') as f:
    data = yaml.safe_load(f)

print("Analyzing QUE-005 patterns...")
print("=" * 60)

# Analyze samples
for test in data['samples']:
    lines = test['input'].strip().split('\n')
    parts = lines[0].split()
    n, k = int(parts[0]), int(parts[1])
    arr = list(map(int, lines[1].split()))
    expected = int(test['output'])
    analyze(n, k, arr, expected)
