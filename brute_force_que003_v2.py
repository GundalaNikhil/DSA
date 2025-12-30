#!/usr/bin/env python3
"""Brute force analysis for QUE-003 - extended hypotheses"""
from collections import deque
import yaml
import itertools

def analyze_test(input_str, expected_output):
    """Deeply analyze a single testcase"""
    lines = input_str.strip().split('\n')
    m = int(lines[0])
    operations = []

    for i in range(1, len(lines)):
        parts = lines[i].split()
        operations.append(parts)

    queue = deque()
    metrics = {}

    # Count each operation type
    metrics['ENQUEUE_count'] = sum(1 for op in operations if op[0] == 'ENQUEUE')
    metrics['DEQUEUE_count'] = sum(1 for op in operations if op[0] == 'DEQUEUE')
    metrics['FRONT_count'] = sum(1 for op in operations if op[0] == 'FRONT')
    metrics['SIZE_count'] = sum(1 for op in operations if op[0] == 'SIZE')
    metrics['total_ops'] = m

    # Simulate to get final state
    for op_data in operations:
        cmd = op_data[0]
        if cmd == "ENQUEUE":
            queue.append(int(op_data[1]))
        elif cmd == "DEQUEUE":
            if queue:
                queue.popleft()
        elif cmd == "FRONT":
            pass
        elif cmd == "SIZE":
            pass

    metrics['final_queue_size'] = len(queue)
    metrics['expected'] = int(expected_output)

    return metrics

def generate_formulas(m):
    """Generate candidate formulas from metrics"""
    formulas = []

    # Basic formulas
    for op_type in ['ENQUEUE_count', 'DEQUEUE_count', 'FRONT_count', 'SIZE_count']:
        for mod in [1, 10, 100]:
            formulas.append(f"({op_type} * {m}) % {mod}")
            formulas.append(f"({op_type} + {m}) % {mod}")

    return formulas

# Load testcases
with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-003-cafeteria-queue-rotation.yaml', 'r') as f:
    data = yaml.safe_load(f)

all_tests = data['samples'][:3] + data['public'][:3]

print("Searching for formula pattern...")
print("=" * 80)

for test in all_tests:
    metrics = analyze_test(test['input'], test['output'])

    m = metrics['total_ops']
    exp = metrics['expected']
    e_count = metrics['ENQUEUE_count']
    d_count = metrics['DEQUEUE_count']
    f_count = metrics['FRONT_count']
    s_count = metrics['SIZE_count']

    print(f"\nTest: m={m}, E={e_count}, D={d_count}, F={f_count}, S={s_count} => {exp}")

    # Try all combinations
    candidates = []

    # Two-term formulas
    for a, b in itertools.product([e_count, d_count, f_count, s_count, m], repeat=2):
        for op in ['+', '-', '*']:
            for mod in [100, 1000, 10000]:
                if op == '+':
                    result = (a + b) % mod
                elif op == '-':
                    result = (a - b) % mod
                else:  # *
                    result = (a * b) % mod

                if result == exp:
                    candidates.append(f"({a} {op} {b}) % {mod} = {result}")

    if candidates:
        print(f"  Candidates found: {len(candidates)}")
        for c in candidates[:3]:
            print(f"    {c}")
    else:
        print(f"  No match found")
