#!/usr/bin/env python3
import yaml
import random
import math
import os

def solve_num001(n, q, a, queries):
    pref = [0] * n
    pref[0] = abs(a[0])
    for i in range(1, n):
        pref[i] = math.gcd(pref[i-1], abs(a[i]))
    res = []
    for r in queries:
        res.append(str(pref[r]))
    return "\n".join(res)

def solve_num002(n):
    if n < 2: return "0"
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return str(sum(phi[j] for j in range(2, n + 1)))

def solve_num003(q, queries):
    res = []
    for a, m in queries:
        res.append("true" if math.gcd(a, m) == 1 else "false")
    return "\n".join(res)

def solve_num004(x):
    def get_sum(n, b):
        s = 0
        temp = n
        while temp > 0:
            s += temp % b
            temp //= b
        return s
    
    min_sum = float('inf')
    best_b = 2
    for b in range(2, 37):
        curr_sum = get_sum(x, b)
        if curr_sum < min_sum:
            min_sum = curr_sum
            best_b = b
    return f"{best_b} {min_sum}"

def generate_num001():
    test_cases = {'problem_id': 'NUM_CLASSROOM_GCD_PREFIX_QUERIES__4821', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "3 3\n12 18 6\n0\n1\n2", 'output': "12\n6\n6"})
    for _ in range(3):
        n = random.randint(1, 10); q = random.randint(1, 5)
        a = [random.randint(-100, 100) for _ in range(n)]
        queries = [random.randint(0, n-1) for _ in range(q)]
        test_cases['public'].append({'input': f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(map(str, queries)), 'output': solve_num001(n, q, a, queries)})
    for _ in range(35):
        n = random.randint(100, 500); q = random.randint(10, 50)
        a = [random.randint(-10**9, 10**9) for _ in range(n)]
        queries = [random.randint(0, n-1) for _ in range(q)]
        test_cases['hidden'].append({'input': f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(map(str, queries)), 'output': solve_num001(n, q, a, queries)})
    with open('dsa-problems/NumberTheory/testcases/NUM-001-classroom-gcd-prefix-queries.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num002():
    test_cases = {'problem_id': 'NUM_COPRIME_PAIR_COUNT__7194', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "5", 'output': "9"})
    for _ in range(3):
        n = random.randint(2, 10)
        test_cases['public'].append({'input': str(n), 'output': solve_num002(n)})
    for _ in range(35):
        n = random.randint(10, 100000)
        test_cases['hidden'].append({'input': str(n), 'output': solve_num002(n)})
    with open('dsa-problems/NumberTheory/testcases/NUM-002-coprime-pair-count.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num003():
    test_cases = {'problem_id': 'NUM_MODULAR_INVERSE_EXISTENCE__3507', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "1\n4 7", 'output': "true"})
    for _ in range(3):
        q = random.randint(2, 5)
        queries = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(q)]
        test_cases['public'].append({'input': f"{q}\n" + "\n".join(f"{a} {m}" for a, m in queries), 'output': solve_num003(q, queries)})
    for _ in range(35):
        q = random.randint(10, 500)
        queries = [[random.randint(1, 10**9), random.randint(1, 10**9)] for _ in range(q)]
        test_cases['hidden'].append({'input': f"{q}\n" + "\n".join(f"{a} {m}" for a, m in queries), 'output': solve_num003(q, queries)})
    with open('dsa-problems/NumberTheory/testcases/NUM-003-modular-inverse-existence.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num004():
    test_cases = {'problem_id': 'NUM_MINIMAL_BASE_REPRESENTATION__6628', 'samples': [], 'public': [], 'hidden': []}
    # Corrected sample output to match solution logic and other test cases
    test_cases['samples'].append({'input': "31", 'output': "31 1"})
    for _ in range(3):
        x = random.randint(2, 100)
        test_cases['public'].append({'input': str(x), 'output': solve_num004(x)})
    for _ in range(35):
        x = random.randint(100, 10**12)
        test_cases['hidden'].append({'input': str(x), 'output': solve_num004(x)})
    with open('dsa-problems/NumberTheory/testcases/NUM-004-minimal-base-representation.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

if __name__ == "__main__":
    random.seed(42)
    generate_num001()
    generate_num002()
    generate_num003()
    generate_num004()
    print("Generated NUM-001 to NUM-004")
