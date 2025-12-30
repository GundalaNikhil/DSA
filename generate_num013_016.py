#!/usr/bin/env python3
import yaml
import random
import math
import os

def solve_num013(n, k):
    MOD = 1000000007
    if k < 0 or k > n: return "0"
    
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
        
    invFact = [1] * (n + 1)
    invFact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, 1, -1):
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
        
    nCr = fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    vowels = pow(5, k, MOD)
    consonants = pow(21, n - k, MOD)
    return str(nCr * vowels % MOD * consonants % MOD)

def solve_num014(n, L, points):
    if n <= 1: return str(n)
    point_counts = {}
    for p in points:
        point_counts[p] = point_counts.get(p, 0) + 1
    unique_pts = list(point_counts.keys())
    counts = [point_counts[p] for p in unique_pts]
    m_len = len(unique_pts)
    max_pts = max(counts)
    
    for i in range(m_len):
        slope_map = {}
        x1, y1 = unique_pts[i]
        for j in range(m_len):
            if i == j: continue
            x2, y2 = unique_pts[j]
            dx = x2 - x1
            dy = y2 - y1
            dist = math.sqrt(dx*dx + dy*dy)
            if dist > L + 1e-9: continue
            g = math.gcd(abs(dx), abs(dy))
            slope = (dx // g, dy // g)
            slope_map[slope] = slope_map.get(slope, 0) + counts[j]
        for count in slope_map.values():
            max_pts = max(max_pts, counts[i] + count)
    return str(max_pts)

def solve_num015(a_list, m_list):
    def extended_gcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1; y = x1 - (a // b) * y1
        return g, x, y

    cur_a = 0; cur_m = 1
    for i in range(len(a_list)):
        A = a_list[i]; M = m_list[i]
        rhs = (A - cur_a) % M
        g, x, y = extended_gcd(cur_m, M)
        if rhs % g != 0: return "NO"
        inv = x % (M // g)
        k = (rhs // g) * inv % (M // g)
        new_m = cur_m * (M // g)
        cur_a = (cur_a + k * cur_m) % new_m
        cur_m = new_m
    return str(cur_a)

def solve_num016(n, k):
    MOD = 1000000007
    if k > n: return "0"
    C = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    ans = 0
    for i in range(k + 1):
        term = (C[k][i] * pow(k - i, n, MOD)) % MOD
        if i % 2 == 1: ans = (ans - term + MOD) % MOD
        else: ans = (ans + term) % MOD
    return str(ans)

def generate_num013():
    test_cases = {'problem_id': 'NUM_COUNT_STRINGS_EXACT_VOWELS__6940', 'samples': [], 'public': [], 'hidden': []} # ID is dummy
    test_cases['samples'].append({'input': "1 1", 'output': "5"})
    for _ in range(3):
        n = random.randint(1, 100)
        k = random.randint(0, n)
        test_cases['public'].append({'input': f"{n} {k}", 'output': solve_num013(n, k)})
    for _ in range(35):
        n = random.randint(100, 10**5) # Increased range
        k = random.randint(0, n)
        test_cases['hidden'].append({'input': f"{n} {k}", 'output': solve_num013(n, k)})
    with open('dsa-problems/NumberTheory/testcases/NUM-013-count-strings-exact-vowels.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num014():
    test_cases = {'problem_id': 'NUM_MAXIMUM_POINTS_LINE_SEGMENT_LIMIT__2831', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "3 2\n0 0\n1 1\n2 2", 'output': "2"})
    for _ in range(3):
        n = random.randint(2, 20)
        L = random.randint(1, 10)
        points = [(random.randint(0, 5), random.randint(0, 5)) for _ in range(n)]
        inp_str = f"{n} {L}\n" + "\n".join(f"{x} {y}" for x, y in points)
        test_cases['public'].append({'input': inp_str, 'output': solve_num014(n, L, points)})
    for _ in range(35):
        n = random.randint(20, 100) # O(N^2) solution
        L = random.randint(1, 20)
        # Create collinear points intentionally for better test quality
        points = []
        slope = (random.randint(1, 3), random.randint(1, 3))
        start = (random.randint(0, 10), random.randint(0, 10))
        for k in range(n // 2):
             points.append((start[0] + k*slope[0], start[1] + k*slope[1]))
        for k in range(n - n // 2):
             points.append((random.randint(0, 50), random.randint(0, 50)))
        random.shuffle(points)
        inp_str = f"{n} {L}\n" + "\n".join(f"{x} {y}" for x, y in points)
        test_cases['hidden'].append({'input': inp_str, 'output': solve_num014(n, L, points)})
    with open('dsa-problems/NumberTheory/testcases/NUM-014-maximum-points-line-segment-limit.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num015():
    test_cases = {'problem_id': 'NUM_CRT_EXISTENCE_VALUE__4592', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "2\n2 3\n3 5", 'output': "8"})
    for _ in range(3):
        k = random.randint(2, 5)
        a_list = []; m_list = []
        for _ in range(k):
             m_list.append(random.randint(2, 20))
             a_list.append(random.randint(0, m_list[-1]-1))
        # Create inputs as list of numbers: k, a1, m1, a2, m2, ...
        input_parts = [str(k)]
        for i in range(k):
            input_parts.append(str(a_list[i]))
            input_parts.append(str(m_list[i]))
        test_cases['public'].append({'input': " ".join(input_parts), 'output': solve_num015(a_list, m_list)})
    for _ in range(35):
        k = random.randint(5, 15)
        a_list = []; m_list = []
        # Ensure some cases are solvable by making moduli pairwise coprime sometimes, or random
        is_solvable = random.choice([True, False])
        if is_solvable:
             primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
             random.shuffle(primes)
             for i in range(k):
                 m = primes[i] if i < len(primes) else random.randint(50, 100)
                 m_list.append(m)
                 a_list.append(random.randint(0, m-1))
        else:
             for _ in range(k):
                 m_list.append(random.randint(2, 50))
                 a_list.append(random.randint(0, m_list[-1]-1))

        input_parts = [str(k)]
        for i in range(k):
            input_parts.append(str(a_list[i]))
            input_parts.append(str(m_list[i]))
        test_cases['hidden'].append({'input': " ".join(input_parts), 'output': solve_num015(a_list, m_list)})
    with open('dsa-problems/NumberTheory/testcases/NUM-015-crt-existence-value.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

def generate_num016():
    test_cases = {'problem_id': 'NUM_COUNT_SURJECTIVE_FUNCTIONS__1820', 'samples': [], 'public': [], 'hidden': []}
    test_cases['samples'].append({'input': "4 3", 'output': "36"})
    for _ in range(3):
        n = random.randint(5, 20)
        k = random.randint(1, n)
        test_cases['public'].append({'input': f"{n} {k}", 'output': solve_num016(n, k)})
    for _ in range(35):
        n = random.randint(20, 1000)
        k = random.randint(1, min(n, 1000))
        test_cases['hidden'].append({'input': f"{n} {k}", 'output': solve_num016(n, k)})
    with open('dsa-problems/NumberTheory/testcases/NUM-016-count-surjective-functions.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False)

if __name__ == "__main__":
    random.seed(42)
    generate_num013()
    generate_num014()
    generate_num015()
    generate_num016()
    print("Generated NUM-013 to NUM-016")
