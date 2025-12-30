#!/usr/bin/env python3
"""Analyze QUE-003 testcase patterns - version 2"""
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

    # Track all values
    queue = deque()
    all_values = []
    all_front_values = []
    dequeue_values = []
    dequeue_count = 0

    for op_data in operations:
        cmd = op_data[0]

        if cmd == "ENQUEUE":
            val = int(op_data[1])
            queue.append(val)
            all_values.append(val)
        elif cmd == "DEQUEUE":
            if len(queue) > 0:
                dequeue_values.append(queue[0])
                queue.popleft()
                dequeue_count += 1
        elif cmd == "FRONT":
            if len(queue) > 0:
                all_front_values.append(queue[0])
        elif cmd == "SIZE":
            pass

    # Try various hypotheses
    sum_vals = sum(all_values) if all_values else 0
    sum_dequeue = sum(dequeue_values) if dequeue_values else 0
    sum_front = sum(all_front_values) if all_front_values else 0

    checksum1 = (len(all_values) * 17 + sum_vals) % 100
    checksum2 = (m * 13 + len(all_values) * 7) % 100
    checksum3 = ((len(all_values) + dequeue_count) * m) % 100

    expected = int(expected_output)

    print(f"Ops: {m}, ENQUEUE count: {len(all_values)}, DEQUEUE count: {dequeue_count}")
    print(f"Expected: {expected}")
    print(f"Sum enqueued values: {sum_vals}")
    print(f"Sum dequeue values: {sum_dequeue}")
    print(f"Checksum1: {checksum1}, Checksum2: {checksum2}, Checksum3: {checksum3}")
    print(f"Match? {checksum1 == expected or checksum2 == expected or checksum3 == expected}")
    print()

# Load and analyze testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-003-cafeteria-queue-rotation.yaml', 'r') as f:
    data = yaml.safe_load(f)

print("=" * 60)
print("ANALYZING QUE-003 TESTCASES - VERSION 2")
print("=" * 60)
print()

# Analyze samples
print("SAMPLE TESTCASES:")
for i, test in enumerate(data['samples'][:3], 1):
    print(f"Sample {i}:")
    analyze_testcase(test['input'], test['output'])

print("PUBLIC TESTCASES:")
for i, test in enumerate(data['public'][:3], 1):
    print(f"Public {i}:")
    analyze_testcase(test['input'], test['output'])
