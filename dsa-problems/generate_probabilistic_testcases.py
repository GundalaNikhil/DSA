#!/usr/bin/env python3
"""
Generate comprehensive test cases for Probabilistic problems (PRB-001 to PRB-016).
Target: 30-40 test cases per problem with proper distribution.
"""

import os
import yaml
import random
import math
from typing import List, Tuple, Dict, Any
from decimal import Decimal, getcontext

# Set high precision for calculations
getcontext().prec = 50

# Configuration
OUTPUT_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def str_representer(dumper, data):
    """Custom string representer that uses |- for multiline strings."""
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|-')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_representer)

def format_testcase_yaml(data: Dict[str, Any]) -> str:
    """Manually format YAML with |- syntax for multiline strings."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section in ['samples', 'public', 'hidden']:
        if section not in data or not data[section]:
            continue
        
        lines.append(f"{section}:")
        for case in data[section]:
            lines.append("- input: |-")
            for line in case['input'].split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            for line in case['output'].split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines) + '\n'

def write_yaml(filename: str, data: Dict[str, Any]):
    """Write test case data to YAML file with proper formatting."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(f"# filepath: {filepath}\n")
        f.write(format_testcase_yaml(data))
    print(f"✅ Generated {filename}")

# ===== PRB-001: Coin Flip Streak Probability =====
def generate_prb001():
    """Generate test cases for Coin Flip Streak Probability."""
    problem_id = "PRB-001"
    
    def solve(n, k):
        """DP solution: probability of at least one k-streak."""
        # dp[i][j] = probability of no k-streak in first i flips, current run j
        dp = [[0.0 for _ in range(k)] for _ in range(n + 1)]
        dp[0][0] = 1.0
        
        for i in range(n):
            for j in range(k):
                # Flip tails: run resets
                dp[i + 1][0] += dp[i][j] * 0.5
                # Flip heads: run increases (if not already k-1)
                if j + 1 < k:
                    dp[i + 1][j + 1] += dp[i][j] * 0.5
        
        prob_no_streak = sum(dp[n][j] for j in range(k))
        return 1.0 - prob_no_streak
    
    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}
    
    # Samples
    samples = [
        (3, 2),  # 0.375
        (5, 3),  # ~0.1875
        (10, 4) # ~0.0537
    ]
    for n, k in samples:
        result = solve(n, k)
        testcases["samples"].append({
            "input": f"{n} {k}",
            "output": f"{result:.6f}"
        })
    
    # Public
    public = [(4, 2), (6, 3), (8, 4), (10, 5), (15, 6)]
    for n, k in public:
        result = solve(n, k)
        testcases["public"].append({
            "input": f"{n} {k}",
            "output": f"{result:.6f}"
        })
    
    # Hidden
    hidden_cases = [
        (20, 5), (25, 6), (30, 7), (35, 8), (40, 9),
        (45, 10), (50, 11), (55, 12), (60, 13), (60, 15),
        (12, 3), (18, 4), (22, 5), (28, 6), (32, 7),
        (38, 8), (42, 9), (48, 10), (52, 11), (58, 12),
        (60, 20), (60, 30), (60, 1), (30, 15), (40, 20),
        (50, 25), (55, 27), (58, 29), (60, 60), (59, 59)
    ]
    for n, k in hidden_cases:
        result = solve(n, k)
        testcases["hidden"].append({
            "input": f"{n} {k}",
            "output": f"{result:.6f}"
        })
    
    write_yaml("PRB-001-coin-flip-streak-probability.yaml", testcases)

# ===== PRB-002: Expected Steps Random Walk 1D =====
def generate_prb002():
    """Generate test cases for Expected Steps Random Walk 1D."""
    problem_id = "PRB-002"
    
    def solve(a, b, p):
        """Expected steps to hit +a or -b in 1D random walk."""
        if abs(p - 0.5) < 1e-9:
            # Symmetric case
            return a * b
        else:
            # Asymmetric case: solve system of equations
            q = 1 - p
            r = q / p if p > 0 else 0
            
            if abs(r - 1) < 1e-9:
                return a * b
            
            denom = (r**a - 1) * (r**b - 1)
            if abs(denom) < 1e-9:
                return a * b
            
            numerator = (r**b - 1) * a + (r**a - 1) * b
            return numerator / (p - q) if abs(p - q) > 1e-9 else a * b
    
    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}
    
    # Samples
    samples = [(2, 1, 0.5), (3, 2, 0.5), (5, 5, 0.5)]
    for a, b, p in samples:
        result = solve(a, b, p)
        testcases["samples"].append({
            "input": f"{a} {b} {p:.6f}",
            "output": f"{result:.6f}"
        })
    
    # Public
    public = [(10, 5, 0.5), (20, 10, 0.5), (15, 15, 0.5), (25, 15, 0.6), (30, 20, 0.4)]
    for a, b, p in public:
        result = solve(a, b, p)
        testcases["public"].append({
            "input": f"{a} {b} {p:.6f}",
            "output": f"{result:.6f}"
        })
    
    # Hidden
    random.seed(42)
    for _ in range(30):
        a = random.randint(1, 200)
        b = random.randint(1, 200)
        p = random.uniform(0.1, 0.9)
        result = solve(a, b, p)
        testcases["hidden"].append({
            "input": f"{a} {b} {p:.6f}",
            "output": f"{result:.6f}"
        })
    
    write_yaml("PRB-002-expected-steps-random-walk-1d.yaml", testcases)

# ===== PRB-003: Reservoir Sampling K Items =====
def generate_prb003():
    """Generate test cases for Reservoir Sampling."""
    problem_id = "PRB-003"
    
    def solve(n, k, seed):
        """Reservoir sampling algorithm with fixed seed."""
        random.seed(seed)
        stream = list(range(1, n + 1))
        reservoir = stream[:k]
        
        for i in range(k, n):
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = stream[i]
        
        return sorted(reservoir)
    
    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}
    
    # Samples
    samples = [(10, 3, 42), (20, 5, 123), (15, 4, 999)]
    for n, k, seed in samples:
        result = solve(n, k, seed)
        testcases["samples"].append({
            "input": f"{n} {k} {seed}",
            "output": " ".join(map(str, result))
        })
    
    # Public
    public = [(50, 10, 555), (100, 20, 777), (30, 5, 111), (75, 15, 222), (25, 8, 333)]
    for n, k, seed in public:
        result = solve(n, k, seed)
        testcases["public"].append({
            "input": f"{n} {k} {seed}",
            "output": " ".join(map(str, result))
        })
    
    # Hidden
    hidden_params = [
        (1000, 50, 1001), (5000, 100, 2002), (10000, 200, 3003),
        (50000, 500, 4004), (100000, 1000, 5005), (500000, 2500, 6006),
        (1000000, 5000, 7007), (250000, 1250, 8008), (750000, 3750, 9009),
        (200, 25, 1111), (300, 30, 2222), (400, 40, 3333),
        (500, 50, 4444), (600, 60, 5555), (700, 70, 6666),
        (800, 80, 7777), (900, 90, 8888), (150, 15, 9999),
        (350, 35, 1234), (450, 45, 5678), (550, 55, 9012),
        (650, 65, 3456), (750, 75, 7890), (850, 85, 2345),
        (950, 95, 6789), (175, 17, 1357), (275, 27, 2468),
        (375, 37, 1593), (475, 47, 7531), (575, 57, 9642)
    ]
    for n, k, seed in hidden_params:
        result = solve(n, k, seed)
        testcases["hidden"].append({
            "input": f"{n} {k} {seed}",
            "output": " ".join(map(str, result))
        })
    
    write_yaml("PRB-003-reservoir-sampling-k.yaml", testcases)

# ===== PRB-004: Monte Carlo Pi Estimation =====
def generate_prb004():
    """Generate test cases for Monte Carlo Pi estimation."""
    problem_id = "PRB-004"
    
    def solve(n, seed):
        """Monte Carlo estimation of pi."""
        random.seed(seed)
        inside = 0
        for _ in range(n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x*x + y*y <= 1:
                inside += 1
        estimate = 4.0 * inside / n
        # Error bound: 2 * sqrt(pi * (4 - pi) / n) for 95% confidence
        error = 2.0 * math.sqrt(math.pi * (4 - math.pi) / n)
        return estimate, error
    
    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}
    
    # Samples
    samples = [(1000, 42), (10000, 123), (5000, 999)]
    for n, seed in samples:
        est, err = solve(n, seed)
        testcases["samples"].append({
            "input": f"{n} {seed}",
            "output": f"{est:.6f} {err:.6f}"
        })
    
    # Public
    public = [(50000, 555), (100000, 777), (25000, 111), (75000, 222), (20000, 333)]
    for n, seed in public:
        est, err = solve(n, seed)
        testcases["public"].append({
            "input": f"{n} {seed}",
            "output": f"{est:.6f} {err:.6f}"
        })
    
    # Hidden
    hidden_params = [
        (200000, 1001), (500000, 2002), (1000000, 3003),
        (750000, 4004), (300000, 5005), (400000, 6006),
        (600000, 7007), (800000, 8008), (900000, 9009),
        (150000, 1111), (250000, 2222), (350000, 3333),
        (450000, 4444), (550000, 5555), (650000, 6666),
        (700000, 7777), (850000, 8888), (950000, 9999),
        (125000, 1234), (175000, 5678), (225000, 9012),
        (275000, 3456), (325000, 7890), (375000, 2345),
        (425000, 6789), (475000, 1357), (525000, 2468),
        (575000, 1593), (625000, 7531), (675000, 9642)
    ]
    for n, seed in hidden_params:
        est, err = solve(n, seed)
        testcases["hidden"].append({
            "input": f"{n} {seed}",
            "output": f"{est:.6f} {err:.6f}"
        })
    
    write_yaml("PRB-004-monte-carlo-pi.yaml", testcases)

# ===== PRB-005: Bloom Filter False Positive Rate =====
def generate_prb005():
    """Generate test cases for Bloom Filter FPR."""
    problem_id = "PRB-005"
    
    def solve(m, k, n):
        """False positive probability of Bloom filter."""
        # FPR = (1 - e^(-kn/m))^k
        exponent = -k * n / m
        fpr = (1 - math.exp(exponent)) ** k
        return fpr
    
    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}
    
    # Samples
    samples = [(1000, 3, 100), (5000, 5, 500), (10000, 7, 1000)]
    for m, k, n in samples:
        result = solve(m, k, n)
        testcases["samples"].append({
            "input": f"{m} {k} {n}",
            "output": f"{result:.6f}"
        })
    
    # Public
    public = [(20000, 10, 2000), (50000, 8, 5000), (100000, 12, 10000), 
              (15000, 6, 1500), (30000, 9, 3000)]
    for m, k, n in public:
        result = solve(m, k, n)
        testcases["public"].append({
            "input": f"{m} {k} {n}",
            "output": f"{result:.6f}"
        })
    
    # Hidden
    random.seed(42)
    for _ in range(30):
        m = random.randint(1000, 1000000)
        n = random.randint(100, m // 2)
        k = random.randint(1, 20)
        result = solve(m, k, n)
        testcases["hidden"].append({
            "input": f"{m} {k} {n}",
            "output": f"{result:.6f}"
        })
    
    write_yaml("PRB-005-bloom-filter-fpr.yaml", testcases)

# ===== PRB-011: Coupon Collector Expected Trials =====
def generate_prb011():
    """Generate test cases for Coupon Collector problem."""
    problem_id = "PRB-011"
    
    def solve(n):
        """Expected draws to collect all n coupons."""
        # E = n * H_n where H_n is nth harmonic number
        harmonic = sum(1.0 / i for i in range(1, n + 1))
        return n * harmonic
    
    testcases = {"problem_id": problem_id, "samples": [], "public": [], "hidden": []}
    
    # Samples
    samples = [3, 5, 10]
    for n in samples:
        result = solve(n)
        testcases["samples"].append({
            "input": f"{n}",
            "output": f"{result:.6f}"
        })
    
    # Public
    public = [15, 20, 25, 50, 100]
    for n in public:
        result = solve(n)
        testcases["public"].append({
            "input": f"{n}",
            "output": f"{result:.6f}"
        })
    
    # Hidden
    hidden_vals = [
        200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000,
        150000, 200000, 300000, 400000, 500000, 600000, 700000,
        800000, 900000, 1000000, 75000, 125000, 175000, 225000,
        275000, 325000, 375000, 425000, 475000, 550000, 999999
    ]
    for n in hidden_vals:
        result = solve(n)
        testcases["hidden"].append({
            "input": f"{n}",
            "output": f"{result:.6f}"
        })
    
    write_yaml("PRB-011-coupon-collector-expected.yaml", testcases)

def main():
    """Generate all Probabilistic test cases."""
    print("=" * 70)
    print("GENERATING PROBABILISTIC TEST CASES (PRB-001 to PRB-016)")
    print("=" * 70)
    
    # Generate test cases for implemented problems
    generate_prb001()  # Coin Flip Streak
    generate_prb002()  # Random Walk 1D
    generate_prb003()  # Reservoir Sampling
    generate_prb004()  # Monte Carlo Pi
    generate_prb005()  # Bloom Filter
    generate_prb011()  # Coupon Collector
    
    print("=" * 70)
    print("✅ Generated 6 problem test cases")
    print("⚠️  Remaining 10 problems require more complex implementations")
    print("=" * 70)

if __name__ == "__main__":
    main()
