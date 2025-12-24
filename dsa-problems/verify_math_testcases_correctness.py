#!/usr/bin/env python3
"""
Verify Math Advanced test cases against reference solutions.
This tests a sample of test cases to ensure correctness.
"""

import os
import yaml
import sys

TESTCASES_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases"

# Import reference solutions from generation scripts
sys.path.insert(0, "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems")

def test_mth001_sample():
    """Test MTH-001: Polynomial Multiplication FFT"""
    MOD = 1000000007
    
    def solve(A, B):
        n = len(A)
        m = len(B)
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i+j] = (res[i+j] + A[i] * B[j]) % MOD
        return res
    
    # Load test cases
    filepath = os.path.join(TESTCASES_DIR, "MTH-001-polynomial-multiplication-fft.yaml")
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    
    # Test first sample: [1,2] * [3,4] = [3,10,8]
    sample = data['samples'][0]
    lines = sample['input'].strip().split('\n')
    A = list(map(int, lines[1].split()))
    B = list(map(int, lines[2].split()))
    expected = list(map(int, sample['output'].strip().split()))
    result = solve(A, B)
    
    if result == expected:
        return True, f"✅ MTH-001 Sample 1: PASS"
    else:
        return False, f"❌ MTH-001 Sample 1: FAIL - Expected {expected}, got {result}"

def test_mth005_sample():
    """Test MTH-005: Lagrange Interpolation"""
    MOD = 1000000007
    
    def modinv(a, m=MOD):
        return pow(a, m-2, m)
    
    def solve(points, x):
        n = len(points)
        result = 0
        for i in range(n):
            xi, yi = points[i]
            term = yi
            for j in range(n):
                if i != j:
                    xj, _ = points[j]
                    term = term * (x - xj) % MOD
                    term = term * modinv((xi - xj) % MOD) % MOD
            result = (result + term) % MOD
        return result
    
    # Load test cases
    filepath = os.path.join(TESTCASES_DIR, "MTH-005-lagrange-interpolation-mod.yaml")
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    
    # Test first sample: 2 points, query at x=2
    sample = data['samples'][0]
    lines = sample['input'].strip().split('\n')
    n, x = map(int, lines[0].split())
    points = []
    for i in range(1, n+1):
        xi, yi = map(int, lines[i].split())
        points.append((xi, yi))
    expected = int(sample['output'].strip())
    result = solve(points, x)
    
    if result == expected:
        return True, f"✅ MTH-005 Sample 1: PASS"
    else:
        return False, f"❌ MTH-005 Sample 1: FAIL - Expected {expected}, got {result}"

def test_mth006_sample():
    """Test MTH-006: Determinant Gaussian"""
    MOD = 1000000007
    
    def solve(matrix):
        n = len(matrix)
        mat = [row[:] for row in matrix]  # Copy
        det = 1
        
        for i in range(n):
            # Find pivot
            pivot = i
            for j in range(i+1, n):
                if abs(mat[j][i]) > abs(mat[pivot][i]):
                    pivot = j
            
            if mat[pivot][i] == 0:
                return 0
            
            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                det = (-det) % MOD
            
            det = (det * mat[i][i]) % MOD
            inv = pow(mat[i][i], MOD-2, MOD)
            
            for j in range(i, n):
                mat[i][j] = (mat[i][j] * inv) % MOD
            
            for j in range(i+1, n):
                factor = mat[j][i]
                for k in range(i, n):
                    mat[j][k] = (mat[j][k] - factor * mat[i][k]) % MOD
        
        return det
    
    # Load test cases
    filepath = os.path.join(TESTCASES_DIR, "MTH-006-determinant-gaussian.yaml")
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    
    # Test first sample
    sample = data['samples'][0]
    lines = sample['input'].strip().split('\n')
    n = int(lines[0])
    matrix = []
    for i in range(1, n+1):
        row = list(map(int, lines[i].split()))
        matrix.append(row)
    expected = int(sample['output'].strip())
    result = solve(matrix)
    
    if result == expected:
        return True, f"✅ MTH-006 Sample 1: PASS"
    else:
        return False, f"❌ MTH-006 Sample 1: FAIL - Expected {expected}, got {result}"

def test_mth009_sample():
    """Test MTH-009: Subset Convolution"""
    MOD = 1000000007
    
    def solve(A, B, op):
        n_len = len(A)
        C = [0] * n_len
        for i in range(n_len):
            for j in range(n_len):
                if op == 1:  # OR
                    k = i | j
                else:  # AND
                    k = i & j
                C[k] = (C[k] + A[i] * B[j]) % MOD
        return C
    
    # Load test cases
    filepath = os.path.join(TESTCASES_DIR, "MTH-009-subset-convolution-and-or.yaml")
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    
    # Test first sample
    sample = data['samples'][0]
    lines = sample['input'].strip().split('\n')
    n, op = map(int, lines[0].split())
    A = list(map(int, lines[1].split()))
    B = list(map(int, lines[2].split()))
    expected = list(map(int, sample['output'].strip().split()))
    result = solve(A, B, op)
    
    if result == expected:
        return True, f"✅ MTH-009 Sample 1: PASS"
    else:
        return False, f"❌ MTH-009 Sample 1: FAIL - Expected {expected}, got {result}"

def main():
    """Run all test verifications."""
    print("=" * 70)
    print("MATH ADVANCED TEST CASE VERIFICATION")
    print("=" * 70)
    print()
    
    tests = [
        test_mth001_sample,
        test_mth005_sample,
        test_mth006_sample,
        test_mth009_sample,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            success, message = test_func()
            print(message)
            if success:
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ {test_func.__name__}: ERROR - {e}")
            failed += 1
    
    print()
    print("=" * 70)
    print(f"VERIFICATION SUMMARY")
    print("=" * 70)
    print(f"Passed: {passed}/{passed+failed}")
    print(f"Failed: {failed}/{passed+failed}")
    
    if failed == 0:
        print()
        print("✅ ALL TESTS PASSED - Test cases are correct!")
    else:
        print()
        print("⚠️  Some tests failed - review test case generation")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
