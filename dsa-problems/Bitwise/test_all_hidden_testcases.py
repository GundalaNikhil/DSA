#!/usr/bin/env python3
"""
Comprehensive test runner for all Bitwise hidden testcases against editorial solutions.
"""

import yaml
from pathlib import Path
from collections import defaultdict

# ============================================================================
# EDITORIAL SOLUTIONS EXTRACTED FROM MARKDOWN FILES
# ============================================================================

def bit_001_solution(n, arr, salt):
    """BIT-001: Odd After Bit Salt"""
    result = 0
    for x in arr:
        result ^= (x ^ salt)
    return result


def bit_002_solution(n, mask, arr):
    """BIT-002: Two Unique With Triples Mask"""
    # Phase 1: Get XOR of both uniques
    bit_count = [0] * 32

    for num in arr:
        for i in range(32):
            if num & (1 << i):
                bit_count[i] += 1

    xor_both = 0
    for i in range(32):
        if bit_count[i] % 3 == 1:
            xor_both |= (1 << i)

    # Phase 2: Find differentiating bit
    masked_diff = xor_both & mask
    diff_bit = masked_diff & -masked_diff

    # Phase 3: Partition and find both
    bit_count_0 = [0] * 32
    bit_count_1 = [0] * 32

    for num in arr:
        for i in range(32):
            if num & (1 << i):
                if num & diff_bit:
                    bit_count_1[i] += 1
                else:
                    bit_count_0[i] += 1

    unique1, unique2 = 0, 0
    for i in range(32):
        if bit_count_0[i] % 3 == 1:
            unique1 |= (1 << i)
        if bit_count_1[i] % 3 == 1:
            unique2 |= (1 << i)

    return sorted([unique1, unique2])


def bit_003_solution(L, R, m):
    """BIT-003: Bitwise AND Skip Multiples"""
    result = None
    for i in range(L, R + 1):
        if i % m != 0:
            if result is None:
                result = i
            else:
                result &= i
    return result if result is not None else -1


def bit_004_solution(n, L, U, arr):
    """BIT-004: Pairwise XOR Band Index Parity"""
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (i + j) % 2 == 0:
                xor_val = arr[i] ^ arr[j]
                if L <= xor_val <= U:
                    count += 1
    return count


def bit_005_solution(n, start_xor, arr):
    """BIT-005: Max Subarray XOR With Start"""
    max_xor = 0
    for i in range(start_xor, n):
        curr_xor = 0
        for j in range(start_xor, i + 1):
            curr_xor ^= arr[j]
            max_xor = max(max_xor, curr_xor)
    return max_xor


def bit_008_solution(n, k, arr):
    """BIT-008: Maximize OR K Picks"""
    from itertools import combinations
    max_or = 0
    for combo in combinations(arr, min(k, n)):
        or_val = 0
        for num in combo:
            or_val |= num
        max_or = max(max_or, or_val)
    return max_or


def bit_016_solution(n, K, arr):
    """BIT-016: Max OR Subarray LEQ K"""
    if not arr or n == 0:
        return 0

    max_len = 0
    bit_count = [0] * 30
    L = 0

    def compute_or():
        result = 0
        for i in range(30):
            if bit_count[i] > 0:
                result |= (1 << i)
        return result

    for R in range(len(arr)):
        for i in range(30):
            if arr[R] & (1 << i):
                bit_count[i] += 1

        while L <= R and compute_or() > K:
            for i in range(30):
                if arr[L] & (1 << i):
                    bit_count[i] -= 1
            L += 1

        max_len = max(max_len, R - L + 1)

    return max_len


# ============================================================================
# INPUT PARSING
# ============================================================================

def parse_input(input_str, problem_id):
    """Parse input string based on problem format"""
    lines = [line.strip() for line in input_str.strip().split('\n') if line.strip()]

    if problem_id == 'BIT-001':
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        salt = int(lines[2])
        return (n, arr, salt)

    elif problem_id == 'BIT-002':
        parts = lines[0].split()
        n, mask = int(parts[0]), int(parts[1])
        arr = list(map(int, lines[1].split()))
        return (n, mask, arr)

    elif problem_id == 'BIT-003':
        parts = lines[0].split()
        L, R, m = int(parts[0]), int(parts[1]), int(parts[2])
        return (L, R, m)

    elif problem_id == 'BIT-004':
        params = lines[0].split()
        n, L, U = int(params[0]), int(params[1]), int(params[2])
        arr = list(map(int, lines[1].split()))
        return (n, L, U, arr)

    elif problem_id == 'BIT-008':
        parts = lines[0].split()
        n, k = int(parts[0]), int(parts[1])
        arr = list(map(int, lines[1].split()))
        return (n, k, arr)

    elif problem_id == 'BIT-016':
        parts = lines[0].split()
        n, K = int(parts[0]), int(parts[1])
        arr = list(map(int, lines[1].split()))
        return (n, K, arr)

    return ()


# ============================================================================
# TEST RUNNER
# ============================================================================

def test_all_hidden_testcases():
    """Test all hidden testcases against editorial solutions"""

    testcase_dir = Path('dsa-problems/Bitwise/testcases')

    solutions_map = {
        'BIT-001': bit_001_solution,
        'BIT-002': bit_002_solution,
        'BIT-003': bit_003_solution,
        'BIT-004': bit_004_solution,
        'BIT-005': bit_005_solution,
        'BIT-008': bit_008_solution,
        'BIT-016': bit_016_solution,
    }

    results = {}
    total_passed = 0
    total_tests = 0

    print("\n" + "=" * 80)
    print("BITWISE HIDDEN TESTCASE VERIFICATION")
    print("=" * 80)

    for problem_id in sorted(solutions_map.keys()):
        solution_func = solutions_map[problem_id]
        files = list(testcase_dir.glob(f'{problem_id}-*.yaml'))

        if not files:
            continue

        with open(files[0], 'r') as f:
            data = yaml.safe_load(f)

        hidden_tests = data.get('hidden', [])
        passed = 0
        failed = 0
        errors = []

        for idx, test in enumerate(hidden_tests):
            total_tests += 1
            try:
                input_str = test.get('input', '')
                expected = str(test.get('output', '')).strip()

                parsed_input = parse_input(input_str, problem_id)
                if not parsed_input:
                    failed += 1
                    continue

                actual = solution_func(*parsed_input)

                # Format output
                if isinstance(actual, list):
                    actual_str = ' '.join(map(str, actual))
                else:
                    actual_str = str(actual)

                if actual_str == expected:
                    passed += 1
                    total_passed += 1
                else:
                    failed += 1
                    if len(errors) < 2:
                        errors.append(
                            f"  Test {idx}: Expected '{expected}', Got '{actual_str}'"
                        )
            except Exception as e:
                failed += 1
                if len(errors) < 2:
                    errors.append(f"  Test {idx}: {type(e).__name__}: {str(e)[:60]}")

        total = len(hidden_tests)
        pct = (passed / total * 100) if total > 0 else 0
        status = "✅ PASS" if failed == 0 else "❌ FAIL"

        results[problem_id] = {
            'passed': passed,
            'total': total,
            'errors': errors
        }

        print(f"\n{problem_id}: {passed}/{total} ({pct:.1f}%) {status}")
        for error in errors:
            print(error)

    print("\n" + "=" * 80)
    print(f"TOTAL: {total_passed}/{total_tests} ({total_passed/total_tests*100:.1f}%)")
    print("=" * 80 + "\n")

    return results


if __name__ == '__main__':
    test_all_hidden_testcases()
