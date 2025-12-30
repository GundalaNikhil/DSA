#!/usr/bin/env python3
import yaml
import random
import math
import os

def solve_num005(n, p):
    # product of all integers in [1..n] that are NOT divisible by p, modulo p
    if n >= p:
        res = pow(p-1, n // p, p)
        for i in range(1, (n % p) + 1):
            res = (res * i) % p
        return str(res)
    else:
        res = 1
        for i in range(1, n + 1):
            res = (res * i) % p
        return str(res)

def solve_num006(N, queries):
    f = [0] * (N + 1)
    for i in range(2, N + 1):
        if f[i] == 0:
            for j in range(i, N + 1, i):
                f[j] += 1
    pref = [0] * (N + 1)
    for i in range(1, N + 1):
        pref[i] = pref[i-1] + f[i]
    res = []
    for l, r in queries:
        res.append(str(pref[r] - pref[l-1]))
    return "\n".join(res)

def solve_num007(n, q, MOD, a, queries):
    def get_lcm(slice):
        if not slice: return 0
        powers = {}
        for x in slice:
            d = 2
            temp = x
            while d * d <= temp:
                if temp % d == 0:
                    cnt = 0
                    while temp % d == 0:
                        cnt += 1
                        temp //= d
                    powers[d] = max(powers.get(d, 0), cnt)
                d += 1
            if temp > 1:
                powers[temp] = max(powers.get(temp, 0), 1)
        res = 1
        for p, exp in powers.items():
            res = (res * pow(p, exp, MOD)) % MOD
        return res
    
    ans = []
    for l, r in queries:
        ans.append(str(get_lcm(a[l:r+1])))
    return "\n".join(ans)

def solve_num008(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return str(math.gcd(dx, dy) + 1)

def generate_num005():
    test_cases = {'problem_id': 'NUM_FACTORIALS_MISSING_PRIMES__2941', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "6 5", 'output': "4"})
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 999983, 1000003]
    for _ in range(3):
        p = random.choice(primes)
        n = random.randint(1, 100)
        test_cases['public'].append({'input': f"{n} {p}", 'output': solve_num005(n, p)})
    for _ in range(35):
        p = random.choice(primes)
        n = random.randint(100, 10**12)
        test_cases['hidden'].append({'input': f"{n} {p}", 'output': solve_num005(n, p)})
    with open('dsa-problems/NumberTheory/testcases/NUM-005-factorials-missing-primes.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num006():
    test_cases = {'problem_id': 'NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "6 1\n2 5", 'output': "4"})
    for _ in range(3):
        N = random.randint(10, 100)
        q = random.randint(1, 3)
        queries = []
        for _ in range(q):
            l = random.randint(1, N)
            r = random.randint(l, N)
            queries.append([l, r])
        test_cases['public'].append({'input': f"{N} {q}\n" + "\n".join(f"{l} {r}" for l, r in queries), 'output': solve_num006(N, queries)})
    for _ in range(35):
        N = random.randint(1000, 10000)
        q = random.randint(10, 50)
        queries = []
        for _ in range(q):
            l = random.randint(1, N)
            r = random.randint(l, N)
            queries.append([l, r])
        test_cases['hidden'].append({'input': f"{N} {q}\n" + "\n".join(f"{l} {r}" for l, r in queries), 'output': solve_num006(N, queries)})
    with open('dsa-problems/NumberTheory/testcases/NUM-006-distinct-prime-factors-prefix.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num007():
    test_cases = {'problem_id': 'NUM_LCM_OF_RANGES__8402', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "3 1 1000000007\n2 6 3\n0 1", 'output': "6"})
    for _ in range(3):
        n = random.randint(5, 10); q = random.randint(1, 3); mod = 1000000007
        a = [random.randint(1, 100) for _ in range(n)]
        queries = []
        for _ in range(q):
            l = random.randint(0, n-1)
            r = min(l + random.randint(0, 5), n-1)
            queries.append([l, r])
        test_cases['public'].append({'input': f"{n} {q} {mod}\n" + " ".join(map(str, a)) + "\n" + "\n".join(f"{l} {r}" for l, r in queries), 'output': solve_num007(n, q, mod, a, queries)})
    for _ in range(35):
        n = random.randint(100, 500); q = random.randint(10, 50); mod = random.randint(10**7, 10**9)
        a = [random.randint(1, 10**6) for _ in range(n)]
        queries = []
        for _ in range(q):
            l = random.randint(0, n-1)
            r = min(l + random.randint(0, 20), n-1)
            queries.append([l, r])
        test_cases['hidden'].append({'input': f"{n} {q} {mod}\n" + " ".join(map(str, a)) + "\n" + "\n".join(f"{l} {r}" for l, r in queries), 'output': solve_num007(n, q, mod, a, queries)})
    with open('dsa-problems/NumberTheory/testcases/NUM-007-lcm-of-ranges.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num008():
    test_cases = {'problem_id': 'NUM_LATTICE_POINTS_ON_SEGMENT__6330', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "0 0 6 4", 'output': "3"})
    for _ in range(3):
        x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
        x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
        test_cases['public'].append({'input': f"{x1} {y1} {x2} {y2}", 'output': solve_num008(x1, y1, x2, y2)})
    for _ in range(35):
        x1, y1 = random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)
        x2, y2 = random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)
        test_cases['hidden'].append({'input': f"{x1} {y1} {x2} {y2}", 'output': solve_num008(x1, y1, x2, y2)})
    with open('dsa-problems/NumberTheory/testcases/NUM-008-lattice-points-on-segment.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

if __name__ == "__main__":
    random.seed(42)
    generate_num005()
    generate_num006()
    generate_num007()
    generate_num008()
    print("Generated NUM-005 to NUM-008")
