#!/usr/bin/env python3
"""
Test verification script for Probabilistic problems.
Tests generated test cases against editorial reference solutions.
"""

import yaml
import math
import random
import numpy as np
from typing import List, Tuple, Dict

# PRB-001: Coin Flip Streak Probability
def prb001_solve(n, k):
    """DP solution: probability of at least one k-streak."""
    dp = [0.0] * (n + 1)
    
    # Base cases
    for i in range(k):
        dp[i] = 2 ** i if i <= n else 0
    
    if k <= n:
        dp[k] = 2 ** k - 1
    
    # Recurrence: dp[i] = 2*dp[i-1] - dp[i-k-1]
    for i in range(k + 1, n + 1):
        if i - k - 1 >= 0:
            dp[i] = 2 * dp[i-1] - dp[i-k-1]
        else:
            dp[i] = 2 * dp[i-1]
    
    prob_no_streak = dp[n] / (2 ** n)
    return 1.0 - prob_no_streak

# PRB-002: Expected Steps Random Walk 1D
def prb002_solve(a, b, p):
    """Expected steps to hit +a or -b in 1D random walk."""
    if abs(p - 0.5) < 1e-9:
        # Symmetric case: E = a * b
        return float(a * b)
    
    q = 1 - p
    r = q / p if p > 0 else 1
    
    if abs(r - 1) < 1e-9:
        return float(a * b)
    
    # Gambler's ruin expected duration formula:
    # E_0 = (b/(q-p)) * (1 - r^a) / (1 - r^(a+b)) - a/(q-p)
    # Simplified: E = 1/(q-p) * [b*(1-r^a)/(1-r^(a+b)) - a]
    
    if abs(1 - r**(a + b)) < 1e-15:
        return float(a * b)
    
    term1 = b * (1 - r**a) / (1 - r**(a + b))
    result = (term1 - a) / (q - p)
    
    return result

# PRB-003: Reservoir Sampling
def prb003_solve(n, k, seed):
    """Reservoir sampling algorithm with fixed seed."""
    random.seed(seed)
    stream = list(range(1, n + 1))
    reservoir = stream[:k]
    
    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    
    return sorted(reservoir)

# PRB-004: Monte Carlo Pi
def prb004_solve(n, seed):
    """Monte Carlo estimation of pi."""
    random.seed(seed)
    inside = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y <= 1:
            inside += 1
    estimate = 4.0 * inside / n
    error = 2.0 * math.sqrt(math.pi * (4 - math.pi) / n)
    return estimate, error

# PRB-005: Bloom Filter FPR
def prb005_solve(m, k, n):
    """False positive probability of Bloom filter."""
    exponent = -k * n / m
    fpr = (1 - math.exp(exponent)) ** k
    return fpr

# PRB-007: Skip List Expected Height
def prb007_solve(n, p):
    """Expected height of skip list."""
    if p >= 1 or p <= 0:
        return 1.0
    if n <= 1:
        return 1.0
    # Expected max level L where n * p^L ≈ 1
    # L ≈ ln(n) / ln(1/p) = log_{1/p}(n)
    return math.log(n) / math.log(1/p)

# PRB-008: Quickselect Expected Comparisons
def prb008_solve(n, k):
    """Expected comparisons for randomized quickselect."""
    return 2.0 * (n + max(k, n - k + 1))

# PRB-009: Treap Expected Depth
def prb009_solve(n):
    """Expected depth in a treap (harmonic number)."""
    if n == 0:
        return 0.0
    return sum(1.0 / i for i in range(1, n + 1))

# PRB-011: Coupon Collector
def prb011_solve(n):
    """Expected draws to collect all n coupons."""
    harmonic = sum(1.0 / i for i in range(1, n + 1))
    return n * harmonic

# PRB-012: Poisson Approximation
def prb012_solve(n, p, k):
    """Poisson approximation of binomial probability."""
    lambda_param = n * p
    
    # Exact binomial
    from math import comb
    exact = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    
    # Poisson approximation
    approx = (lambda_param ** k) * math.exp(-lambda_param) / math.factorial(k)
    
    error = abs(exact - approx)
    
    return approx, exact, error

def test_problem(problem_id, yaml_file, solver_func, tolerance=1e-4):
    """Test a single problem's test cases against reference solution."""
    print(f"\n{'='*70}")
    print(f"Testing {problem_id}")
    print(f"{'='*70}")
    
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    total_tests = 0
    passed_tests = 0
    failed_tests = []
    
    for section in ['samples', 'public', 'hidden']:
        if section not in data:
            continue
        
        for idx, test in enumerate(data[section]):
            total_tests += 1
            input_lines = test['input'].strip().split('\n')
            expected_output = test['output'].strip()
            
            try:
                # Parse input based on problem
                if problem_id == 'PRB-001':
                    n, k = map(int, input_lines[0].split())
                    result = solver_func(n, k)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-002':
                    parts = input_lines[0].split()
                    a, b = int(parts[0]), int(parts[1])
                    p = float(parts[2])
                    result = solver_func(a, b, p)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-003':
                    n, k, seed = map(int, input_lines[0].split())
                    result = solver_func(n, k, seed)
                    actual_output = " ".join(map(str, result))
                    
                elif problem_id == 'PRB-004':
                    n, seed = map(int, input_lines[0].split())
                    est, err = solver_func(n, seed)
                    actual_output = f"{est:.6f} {err:.6f}"
                    
                elif problem_id == 'PRB-005':
                    m, k, n = map(int, input_lines[0].split())
                    result = solver_func(m, k, n)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-007':
                    parts = input_lines[0].split()
                    n = int(parts[0])
                    p = float(parts[1])
                    result = solver_func(n, p)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-008':
                    n, k = map(int, input_lines[0].split())
                    result = solver_func(n, k)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-009':
                    n = int(input_lines[0])
                    result = solver_func(n)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-011':
                    n = int(input_lines[0])
                    result = solver_func(n)
                    actual_output = f"{result:.6f}"
                    
                elif problem_id == 'PRB-012':
                    parts = input_lines[0].split()
                    n = int(parts[0])
                    p = float(parts[1])
                    k = int(parts[2])
                    approx, exact, error = solver_func(n, p, k)
                    actual_output = f"{approx:.9f} {exact:.9f} {error:.9f}"
                
                else:
                    continue
                
                # Compare outputs
                if actual_output == expected_output:
                    passed_tests += 1
                else:
                    # Check if difference is within tolerance for floats
                    try:
                        expected_vals = list(map(float, expected_output.split()))
                        actual_vals = list(map(float, actual_output.split()))
                        
                        if len(expected_vals) == len(actual_vals):
                            all_close = all(abs(e - a) < tolerance for e, a in zip(expected_vals, actual_vals))
                            if all_close:
                                passed_tests += 1
                            else:
                                failed_tests.append({
                                    'section': section,
                                    'index': idx,
                                    'input': input_lines[0],
                                    'expected': expected_output,
                                    'actual': actual_output
                                })
                        else:
                            failed_tests.append({
                                'section': section,
                                'index': idx,
                                'input': input_lines[0],
                                'expected': expected_output,
                                'actual': actual_output
                            })
                    except:
                        failed_tests.append({
                            'section': section,
                            'index': idx,
                            'input': input_lines[0],
                            'expected': expected_output,
                            'actual': actual_output
                        })
                        
            except Exception as e:
                failed_tests.append({
                    'section': section,
                    'index': idx,
                    'input': input_lines[0] if input_lines else 'N/A',
                    'error': str(e)
                })
    
    # Print results
    pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    print(f"\n📊 Results:")
    print(f"   Total Tests: {total_tests}")
    print(f"   Passed: {passed_tests} ✅")
    print(f"   Failed: {len(failed_tests)} ❌")
    print(f"   Pass Rate: {pass_rate:.1f}%")
    
    if failed_tests and len(failed_tests) <= 5:
        print(f"\n❌ Failed Tests:")
        for fail in failed_tests[:5]:
            print(f"   [{fail.get('section', 'N/A')}-{fail.get('index', 'N/A')}] Input: {fail.get('input', 'N/A')}")
            if 'error' in fail:
                print(f"      Error: {fail['error']}")
            else:
                print(f"      Expected: {fail.get('expected', 'N/A')}")
                print(f"      Actual: {fail.get('actual', 'N/A')}")
    
    return passed_tests, total_tests

def main():
    """Test all Probabilistic problems."""
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases"
    
    problems = [
        ('PRB-001', f'{base_path}/PRB-001-coin-flip-streak-probability.yaml', prb001_solve),
        ('PRB-002', f'{base_path}/PRB-002-expected-steps-random-walk-1d.yaml', prb002_solve),
        ('PRB-003', f'{base_path}/PRB-003-reservoir-sampling-k.yaml', prb003_solve),
        ('PRB-004', f'{base_path}/PRB-004-monte-carlo-pi.yaml', prb004_solve),
        ('PRB-005', f'{base_path}/PRB-005-bloom-filter-fpr.yaml', prb005_solve),
        ('PRB-007', f'{base_path}/PRB-007-skip-list-expected-height.yaml', prb007_solve),
        ('PRB-008', f'{base_path}/PRB-008-quickselect-expected-comparisons.yaml', prb008_solve),
        ('PRB-009', f'{base_path}/PRB-009-treap-priority-invariants.yaml', prb009_solve),
        ('PRB-011', f'{base_path}/PRB-011-coupon-collector-expected.yaml', prb011_solve),
        ('PRB-012', f'{base_path}/PRB-012-poisson-approx-binomial.yaml', prb012_solve),
    ]
    
    print("=" * 70)
    print("PROBABILISTIC TEST CASE VERIFICATION")
    print("=" * 70)
    
    total_passed = 0
    total_tests = 0
    
    for problem_id, yaml_file, solver in problems:
        passed, total = test_problem(problem_id, yaml_file, solver)
        total_passed += passed
        total_tests += total
    
    print(f"\n{'='*70}")
    print(f"OVERALL RESULTS")
    print(f"{'='*70}")
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {total_passed} ✅")
    print(f"Failed: {total_tests - total_passed} ❌")
    print(f"Overall Pass Rate: {(total_passed/total_tests*100):.1f}%")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
