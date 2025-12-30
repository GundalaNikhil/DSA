#!/usr/bin/env python3
import yaml
import random
import math
import os

def solve_num009(a, m, e):
    ans = 1
    for char in e:
        d = int(char)
        ans = pow(ans, 10, m)
        term = pow(a, d, m)
        ans = (ans * term) % m
    return str(ans)

def solve_num010(L, R):
    MOD = 1000000007
    sigma = [0] * (R + 1)
    for i in range(1, R + 1):
        for j in range(i, R + 1, i):
            sigma[j] += i
    total = 0
    for i in range(L, R + 1):
        total = (total + sigma[i]) % MOD
    return str(total)

def solve_num011(n, jumps):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for jump in jumps:
            if i >= jump:
                dp[i] = (dp[i] + dp[i - jump]) % MOD
    return str(dp[n])

def solve_num012(x):
    s = str(x)
    n = len(s)
    min_prod = float('inf')
    found = False
    for i in range(1, n):
        a = int(s[:i])
        b = int(s[i:])
        prod = a * b
        if prod > 0:
            min_prod = min(min_prod, prod)
            found = True
    return str(min_prod) if found else "0" # Handle case where no split yields prod > 0 if any

def generate_num009():
    test_cases = {'problem_id': 'NUM_MODULAR_EXPONENT_DIGIT_STREAM__1122', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "3 11 10", 'output': "1"})
    for _ in range(3):
        a = random.randint(2, 100)
        m = random.randint(2, 100)
        e = str(random.randint(1, 100))
        test_cases['public'].append({'input': f"{a} {m} {e}", 'output': solve_num009(a, m, e)})
    for _ in range(35):
        a = random.randint(2, 10**9)
        m = random.randint(2, 10**9)
        len_e = random.randint(10, 100)
        e = "".join([str(random.randint(0, 9)) for _ in range(len_e)])
        # avoid leading zero unless single digit 0, though e usually > 0
        if e[0] == '0': e = '1' + e[1:] 
        test_cases['hidden'].append({'input': f"{a} {m} {e}", 'output': solve_num009(a, m, e)})
    with open('dsa-problems/NumberTheory/testcases/NUM-009-modular-exponent-digit-stream.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num010():
    test_cases = {'problem_id': 'NUM_SUM_DIVISORS_RANGE__5591', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "3 5", 'output': "17"})
    for _ in range(3):
        L = random.randint(1, 50)
        R = random.randint(L, 100)
        test_cases['public'].append({'input': f"{L} {R}", 'output': solve_num010(L, R)})
    for _ in range(35):
        L = random.randint(1, 1000)
        R = random.randint(L, min(L + 5000, 20000)) # Limit R for performance of O(R log R) reference solution
        test_cases['hidden'].append({'input': f"{L} {R}", 'output': solve_num010(L, R)})
    with open('dsa-problems/NumberTheory/testcases/NUM-010-sum-divisors-range.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num011():
    test_cases = {'problem_id': 'NUM_WAYS_CLIMB_JUMP_SET__7782', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "5 2 1 2", 'output': "8"})
    for _ in range(3):
        n = random.randint(5, 20)
        m = random.randint(1, 3)
        jumps = sorted(list(set([random.randint(1, 5) for _ in range(m)])))
        m = len(jumps)
        test_cases['public'].append({'input': f"{n} {m} " + " ".join(map(str, jumps)), 'output': solve_num011(n, jumps)})
    for _ in range(35):
        n = random.randint(20, 1000)
        m = random.randint(1, 5)
        jumps = sorted(list(set([random.randint(1, 10) for _ in range(m)])))
        m = len(jumps)
        test_cases['hidden'].append({'input': f"{n} {m} " + " ".join(map(str, jumps)), 'output': solve_num011(n, jumps)})
    with open('dsa-problems/NumberTheory/testcases/NUM-011-ways-climb-jump-set.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num012():
    test_cases = {'problem_id': 'NUM_MINIMAL_SPLIT_EQUAL_PRODUCT__9931', 'samples': [], 'public': [], 'hidden': []} # ID is dummy
    test_cases['samples'].append({'input': "123", 'output': "23"})
    for _ in range(3):
        x = random.randint(10, 1000)
        test_cases['public'].append({'input': f"{x}", 'output': solve_num012(x)})
    for _ in range(35):
        x = random.randint(100, 10**9)
        test_cases['hidden'].append({'input': f"{x}", 'output': solve_num012(x)})
    with open('dsa-problems/NumberTheory/testcases/NUM-012-minimal-split-equal-product.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

if __name__ == "__main__":
    random.seed(42)
    generate_num009()
    generate_num010()
    generate_num011()
    generate_num012()
    print("Generated NUM-009 to NUM-012")
