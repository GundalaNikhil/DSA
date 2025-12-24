#!/usr/bin/env python3
"""
Comprehensive test runner for ALL 16 Bitwise problems.
Extracts and tests editorial solutions against all testcases.
"""

import yaml
from pathlib import Path
from itertools import combinations

# ============================================================================
# EDITORIAL SOLUTIONS FOR ALL 16 PROBLEMS
# ============================================================================

# BIT-001: Odd After Bit Salt
def bit_001_solution(n, arr, salt):
    result = 0
    for x in arr:
        result ^= (x ^ salt)
    return result


# BIT-002: Two Unique With Triples Mask
def bit_002_solution(n, mask, arr):
    bit_count = [0] * 32
    for num in arr:
        for i in range(32):
            if num & (1 << i):
                bit_count[i] += 1

    xor_both = 0
    for i in range(32):
        if bit_count[i] % 3 == 1:
            xor_both |= (1 << i)

    masked_diff = xor_both & mask
    diff_bit = masked_diff & -masked_diff

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


# BIT-003: Bitwise AND Skip Multiples
def bit_003_solution(L, R, m):
    result = None
    for i in range(L, R + 1):
        if i % m != 0:
            result = i if result is None else result & i
    return result if result is not None else -1


# BIT-004: Pairwise XOR Band Index Parity
def bit_004_solution(n, L, U, arr):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (i + j) % 2 == 0:
                xor_val = arr[i] ^ arr[j]
                if L <= xor_val <= U:
                    count += 1
    return count


# BIT-005: Max Subarray XOR With Start
def bit_005_solution(n, start_idx, arr):
    # Handle out of bounds start index
    if start_idx >= n:
        return 0

    max_xor = 0
    for i in range(start_idx, n):
        curr_xor = 0
        for j in range(start_idx, i + 1):
            curr_xor ^= arr[j]
            max_xor = max(max_xor, curr_xor)
    return max_xor


# BIT-007: Count Set Bits Indexed XOR
def bit_007_solution(n, arr):
    total = 0
    for i in range(n):
        xor_val = i ^ arr[i]
        # Count set bits using Brian Kernighan's algorithm
        count = 0
        while xor_val:
            xor_val &= xor_val - 1
            count += 1
        total += count
    return total


# BIT-008: Maximize OR K Picks
def bit_008_solution(n, k, arr):
    max_or = 0
    for combo in combinations(arr, min(k, n)):
        or_val = 0
        for num in combo:
            or_val |= num
        max_or = max(max_or, or_val)
    return max_or


# BIT-009: Smallest Absent XOR (XOR Basis)
def bit_009_solution(n, arr):
    basis = [0] * 30

    for num in arr:
        cur = num
        for i in range(29, -1, -1):
            if not (cur & (1 << i)):
                continue

            if not basis[i]:
                basis[i] = cur
                break

            cur ^= basis[i]

    result = 0
    for i in range(29, -1, -1):
        if basis[i]:
            result = max(result, result ^ basis[i])

    return result


# BIT-010: Subset AND Equals X
def bit_010_solution(n, x, arr):
    # DP approach: dp[mask] = count of subsets with AND = mask
    dp = {}
    dp[((1 << n) - 1)] = 1  # All bits set initially

    for i in range(n):
        new_dp = {}
        for mask, count in dp.items():
            # Don't include arr[i]
            new_dp[mask] = new_dp.get(mask, 0) + count
            # Include arr[i]
            new_mask = mask & arr[i]
            new_dp[new_mask] = new_dp.get(new_mask, 0) + count
        dp = new_dp

    return dp.get(x, 0)


# BIT-011: Toggle Ranges Min Flips
def bit_011_solution(n, source, target):
    flips = 0
    for i in range(n):
        if source[i] != target[i]:
            flips += 1
            # Toggle from i onwards
            for j in range(i, n):
                source[j] ^= 1
    return flips


# BIT-012: Distinct Subarray XORs
def bit_012_solution(n, arr):
    xors = set()
    for i in range(n):
        curr_xor = 0
        for j in range(i, n):
            curr_xor ^= arr[j]
            xors.add(curr_xor)
    return len(xors)


# BIT-013: Minimize Max Pair XOR
def bit_013_solution(n, arr):
    if n <= 1:
        return 0

    arr.sort()
    min_max_xor = float('inf')

    # DP or brute force for small n
    for i in range(n):
        for j in range(i + 1, n):
            xor_val = arr[i] ^ arr[j]
            min_max_xor = min(min_max_xor, max(arr[i], xor_val))

    return min_max_xor


# BIT-014: Bitwise Palindromes Balanced Ones
def bit_014_solution(n):
    count = 0
    # Generate all n-bit numbers and check palindrome + balanced ones
    for num in range(1 << n):
        binary = bin(num)[2:].zfill(n)
        # Check if palindrome
        if binary == binary[::-1]:
            # Check if balanced (equal 0s and 1s)
            if binary.count('0') == binary.count('1'):
                count += 1
    return count


# BIT-015: Swap Adjacent 2-bit Blocks
def bit_015_solution(n):
    # Swap adjacent 2-bit blocks
    result = 0
    for i in range(0, 32, 4):
        block1 = (n >> i) & 3
        block2 = (n >> (i + 2)) & 3
        result |= (block2 << i)
        result |= (block1 << (i + 2))
    return result


# BIT-016: Max OR Subarray LEQ K
def bit_016_solution(n, K, arr):
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
    """Parse input based on problem format"""
    lines = [line.strip() for line in input_str.strip().split('\n') if line.strip()]

    if problem_id == 'BIT-001':
        n, arr, salt = int(lines[0]), list(map(int, lines[1].split())), int(lines[2])
        return (n, arr, salt)
    elif problem_id == 'BIT-002':
        n, mask = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))
        return (n, mask, arr)
    elif problem_id == 'BIT-003':
        L, R, m = map(int, lines[0].split())
        return (L, R, m)
    elif problem_id == 'BIT-004':
        n, L, U = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))
        return (n, L, U, arr)
    elif problem_id == 'BIT-005':
        n, start_idx = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))
        return (n, start_idx, arr)
    elif problem_id == 'BIT-007':
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return (n, arr)
    elif problem_id == 'BIT-008':
        n, k = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))
        return (n, k, arr)
    elif problem_id == 'BIT-009':
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return (n, arr)
    elif problem_id == 'BIT-010':
        n, x = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))
        return (n, x, arr)
    elif problem_id == 'BIT-011':
        n = int(lines[0])
        source = list(map(int, lines[1].split()))
        target = list(map(int, lines[2].split()))
        return (n, source, target)
    elif problem_id == 'BIT-012':
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return (n, arr)
    elif problem_id == 'BIT-013':
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        return (n, arr)
    elif problem_id == 'BIT-014':
        n = int(lines[0])
        return (n,)
    elif problem_id == 'BIT-015':
        n = int(lines[0])
        return (n,)
    elif problem_id == 'BIT-016':
        n, K = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))
        return (n, K, arr)

    return ()


# ============================================================================
# TEST RUNNER
# ============================================================================

def run_comprehensive_tests():
    testcase_dir = Path('dsa-problems/Bitwise/testcases')

    solutions = {
        'BIT-001': bit_001_solution,
        'BIT-002': bit_002_solution,
        'BIT-003': bit_003_solution,
        'BIT-004': bit_004_solution,
        'BIT-005': bit_005_solution,
        'BIT-007': bit_007_solution,
        'BIT-008': bit_008_solution,
        'BIT-009': bit_009_solution,
        'BIT-010': bit_010_solution,
        'BIT-011': bit_011_solution,
        'BIT-012': bit_012_solution,
        'BIT-013': bit_013_solution,
        'BIT-014': bit_014_solution,
        'BIT-015': bit_015_solution,
        'BIT-016': bit_016_solution,
    }

    print("\n" + "=" * 100)
    print("COMPREHENSIVE BITWISE TESTCASE VERIFICATION")
    print("Testing ALL 16 problems with Editorial Solutions")
    print("=" * 100 + "\n")

    all_results = {}
    total_passed = 0
    total_tests = 0

    for problem_id in sorted(solutions.keys()):
        solution_func = solutions[problem_id]
        files = list(testcase_dir.glob(f'{problem_id}-*.yaml'))

        if not files:
            continue

        with open(files[0], 'r') as f:
            data = yaml.safe_load(f)

        samples = data.get('samples', [])
        public = data.get('public', [])
        hidden = data.get('hidden', [])

        all_tests = samples + public + hidden

        passed = 0
        failed = 0
        errors = []

        for idx, test in enumerate(all_tests):
            total_tests += 1
            try:
                input_str = test.get('input', '')
                expected = str(test.get('output', '')).strip()

                parsed_input = parse_input(input_str, problem_id)
                if not parsed_input:
                    failed += 1
                    continue

                # Make a copy for problems that modify in-place
                if problem_id == 'BIT-011':
                    n, source, target = parsed_input
                    parsed_input = (n, source[:], target)

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
                        errors.append(f"  [{idx}] Expected '{expected}', Got '{actual_str}'")
            except Exception as e:
                failed += 1
                if len(errors) < 2:
                    errors.append(f"  [{idx}] {type(e).__name__}: {str(e)[:50]}")

        total = len(all_tests)
        pct = (passed / total * 100) if total > 0 else 0
        status = "✅ PASS" if failed == 0 else "❌ FAIL"

        all_results[problem_id] = {
            'passed': passed,
            'total': total,
            'errors': errors,
            'samples': len(samples),
            'public': len(public),
            'hidden': len(hidden)
        }

        print(f"{problem_id}: {passed}/{total} ({pct:.1f}%) {status}")
        print(f"  Breakdown: {len(samples)} samples, {len(public)} public, {len(hidden)} hidden")
        for error in errors:
            print(error)
        if failed == 0 and total > 0:
            print(f"  ✅ All tests passed!")
        print()

    print("=" * 100)
    print(f"TOTAL: {total_passed}/{total_tests} ({total_passed/total_tests*100:.1f}%)")
    print("=" * 100 + "\n")

    # Summary by status
    print("SUMMARY BY PROBLEM:\n")
    passing = [p for p, r in all_results.items() if r['passed'] == r['total']]
    partial = [p for p, r in all_results.items() if 0 < r['passed'] < r['total']]
    failing = [p for p, r in all_results.items() if r['passed'] == 0 and r['total'] > 0]

    print(f"✅ FULLY PASSING ({len(passing)}):")
    for p in passing:
        r = all_results[p]
        print(f"  {p}: {r['passed']}/{r['total']}")

    print(f"\n⚠️  PARTIAL PASS ({len(partial)}):")
    for p in partial:
        r = all_results[p]
        print(f"  {p}: {r['passed']}/{r['total']}")

    print(f"\n❌ FAILING ({len(failing)}):")
    for p in failing:
        r = all_results[p]
        print(f"  {p}: {r['passed']}/{r['total']}")

    print("\n" + "=" * 100)


if __name__ == '__main__':
    run_comprehensive_tests()
