#!/usr/bin/env python3
"""Analyze QUE-003 testcase patterns"""
from collections import deque
import yaml

def analyze_testcase(input_str, expected_output):
    """Analyze a single testcase"""
    lines = input_str.strip().split('\n')
    m = int(lines[0])
    operations = []

    for i in range(1, len(lines)):
        parts = lines[i].split()
        operations.append(parts)

    # Try hypothesis 1: Sum of SIZE operation results
    queue = deque()
    total_size = 0
    size_count = 0

    for op_data in operations:
        cmd = op_data[0]

        if cmd == "ENQUEUE":
            queue.append(int(op_data[1]))
        elif cmd == "DEQUEUE":
            if len(queue) > 0:
                queue.popleft()
        elif cmd == "SIZE":
            total_size += len(queue)
            size_count += 1
        elif cmd == "FRONT":
            pass

    print(f"Operations: {m}")
    print(f"Expected output: {expected_output}")
    print(f"Hypothesis 1 (sum of SIZE): {total_size} (SIZE count: {size_count})")
    print(f"Average SIZE: {total_size // size_count if size_count > 0 else 0}")
    print(f"Max queue size seen: {len(queue)}")
    print()

# Load and analyze testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-003-cafeteria-queue-rotation.yaml', 'r') as f:
    data = yaml.safe_load(f)

print("=" * 60)
print("ANALYZING QUE-003 TESTCASES")
print("=" * 60)
print()

# Analyze samples
print("SAMPLE TESTCASES:")
for i, test in enumerate(data['samples'][:3], 1):
    print(f"Sample {i}:")
    analyze_testcase(test['input'], test['output'])

print("\nPUBLIC TESTCASES:")
for i, test in enumerate(data['public'][:3], 1):
    print(f"Public {i}:")
    analyze_testcase(test['input'], test['output'])

print("\nHIDDEN TESTCASES (first 3):")
for i, test in enumerate(data['hidden'][:3], 1):
    print(f"Hidden {i}:")
    analyze_testcase(test['input'], test['output'])
