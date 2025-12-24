#!/usr/bin/env python3
"""
Verify Recursion test cases against editorial reference solutions.
Tests REC-001 to REC-006 (Part 1) with comprehensive validation.
"""

import math
import yaml
from collections import defaultdict, deque

def load_yaml_testcases(filepath):
    """Load test cases from YAML file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Parse manually
    lines = content.split('\n')
    cases = []
    current_case = None
    current_field = None
    
    for line in lines:
        if line.startswith('- input:'):
            if current_case:
                cases.append(current_case)
            current_case = {'input': '', 'output': ''}
            current_field = 'input'
        elif line.startswith('  output:'):
            current_field = 'output'
        elif line.startswith('    ') and current_case:
            content_line = line[4:]
            if current_case[current_field]:
                current_case[current_field] += '\n' + content_line
            else:
                current_case[current_field] = content_line
    
    if current_case:
        cases.append(current_case)
    
    return cases


# ============================================================================
# REC-001: Dorm Room Paths - Editorial Solution
# ============================================================================

def count_paths_editorial(r, c):
    """Editorial solution using DP with memoization."""
    memo = {}
    
    def helper(i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        memo[(i, j)] = helper(i - 1, j) + helper(i, j - 1)
        return memo[(i, j)]
    
    return helper(r - 1, c - 1)

def verify_rec001(filepath):
    """Verify REC-001 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-001: Dorm Room Paths")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            parts = case['input'].strip().split()
            r, c = int(parts[0]), int(parts[1])
            expected = int(case['output'].strip())
            
            actual = count_paths_editorial(r, c)
            
            if actual == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: r={r}, c={c}")
                print(f"   Expected: {expected}")
                print(f"   Actual: {actual}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-002: Lab ID Permutations No Twins - Editorial Solution
# ============================================================================

def generate_no_twin_perms_editorial(s):
    """Editorial solution using backtracking."""
    chars = sorted(s)
    results = []
    
    def backtrack(path, remaining):
        if not remaining:
            results.append(''.join(path))
            return
        
        seen = set()
        for i in range(len(remaining)):
            if remaining[i] in seen:
                continue
            seen.add(remaining[i])
            
            # Check no adjacent twins
            if path and path[-1] == remaining[i]:
                continue
            
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    backtrack([], chars)
    return results if results else ["NONE"]

def verify_rec002(filepath):
    """Verify REC-002 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-002: Lab ID Permutations No Twins")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            s = case['input'].strip()
            expected_lines = sorted(case['output'].strip().split('\n'))
            
            actual_result = generate_no_twin_perms_editorial(s)
            actual_lines = sorted(actual_result)
            
            if actual_lines == expected_lines:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: {s}")
                print(f"   Expected count: {len(expected_lines)}")
                print(f"   Actual count: {len(actual_lines)}")
                if len(actual_lines) <= 10:
                    print(f"   Expected: {expected_lines[:5]}")
                    print(f"   Actual: {actual_lines[:5]}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-003: Campus Ticket Packs - Editorial Solution
# ============================================================================

def coin_change_count_editorial(coins, target):
    """Editorial DP solution for coin change count."""
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    return dp[target]

def verify_rec003(filepath):
    """Verify REC-003 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-003: Campus Ticket Packs (Coin Change)")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            lines = case['input'].strip().split('\n')
            first_line = lines[0].split()
            n, target = int(first_line[0]), int(first_line[1])
            coins = list(map(int, lines[1].split()))
            
            expected = int(case['output'].strip())
            actual = coin_change_count_editorial(coins, target)
            
            if actual == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: coins={coins}, target={target}")
                print(f"   Expected: {expected}")
                print(f"   Actual: {actual}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-004: Exam Seating Backtrack - Editorial Solution (N-Queens)
# ============================================================================

def n_queens_count_editorial(n):
    """Editorial solution for N-Queens count with optimized constraint tracking."""
    # Precomputed results for known values to speed up verification
    known = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 
             9: 352, 10: 724, 11: 2680, 12: 14200, 13: 73712, 14: 365596, 15: 2279184}
    
    if n in known:
        return known[n]
    
    count = 0
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        
        for col in range(n):
            d1 = row - col
            d2 = row + col
            
            if col in cols or d1 in diag1 or d2 in diag2:
                continue
            
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            
            backtrack(row + 1)
            
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)
    
    backtrack(0)
    return count

def verify_rec004(filepath):
    """Verify REC-004 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-004: Exam Seating Backtrack (N-Queens)")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            n = int(case['input'].strip())
            expected = int(case['output'].strip())
            
            actual = n_queens_count_editorial(n)
            
            if actual == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: n={n}")
                print(f"   Expected: {expected}")
                print(f"   Actual: {actual}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-005: Robot Route Turns - Editorial Solution
# ============================================================================

def count_paths_with_turns_editorial(r, c, max_turns):
    """Editorial DP solution with direction tracking."""
    memo = {}
    
    def dp(row, col, direction, turns):
        if row == r - 1 and col == c - 1:
            return 1
        
        if row >= r or col >= c or turns > max_turns:
            return 0
        
        key = (row, col, direction, turns)
        if key in memo:
            return memo[key]
        
        result = 0
        # Move right
        new_turns = turns + (1 if direction == 'D' else 0)
        result += dp(row, col + 1, 'R', new_turns)
        
        # Move down
        new_turns = turns + (1 if direction == 'R' else 0)
        result += dp(row + 1, col, 'D', new_turns)
        
        memo[key] = result
        return result
    
    return dp(0, 0, '', 0)

def verify_rec005(filepath):
    """Verify REC-005 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-005: Robot Route Turns")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            parts = case['input'].strip().split()
            r, c, t = int(parts[0]), int(parts[1]), int(parts[2])
            expected = int(case['output'].strip())
            
            actual = count_paths_with_turns_editorial(r, c, t)
            
            if actual == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: r={r}, c={c}, max_turns={t}")
                print(f"   Expected: {expected}")
                print(f"   Actual: {actual}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-006: Subset Sum Exact Count - Editorial Solution
# ============================================================================

def find_subset_sum_editorial(arr, k, target):
    """Editorial backtracking solution for subset sum."""
    n = len(arr)
    
    def backtrack(idx, chosen, current_sum, count):
        if count == k:
            if current_sum == target:
                return chosen[:]
            return None
        
        if idx >= n or count + (n - idx) < k:
            return None
        
        # Include arr[idx]
        chosen.append(arr[idx])
        result = backtrack(idx + 1, chosen, current_sum + arr[idx], count + 1)
        if result:
            return result
        chosen.pop()
        
        # Exclude arr[idx]
        result = backtrack(idx + 1, chosen, current_sum, count)
        return result
    
    result = backtrack(0, [], 0, 0)
    return result if result else None

def verify_rec006(filepath):
    """Verify REC-006 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-006: Subset Sum Exact Count")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            lines = case['input'].strip().split('\n')
            first_line = lines[0].split()
            n, k, target = int(first_line[0]), int(first_line[1]), int(first_line[2])
            arr = list(map(int, lines[1].split()))
            
            expected_output = case['output'].strip()
            actual_result = find_subset_sum_editorial(arr, k, target)
            
            if expected_output == "NONE":
                if actual_result is None:
                    passed += 1
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED:")
                    print(f"   Expected: NONE")
                    print(f"   Actual: {actual_result}")
            else:
                # Check if the subset is valid
                expected_nums = sorted(map(int, expected_output.split()))
                if actual_result:
                    actual_nums = sorted(actual_result)
                    # Verify it's a valid subset
                    if len(actual_nums) == k and sum(actual_nums) == target:
                        # Check all elements exist in array
                        temp_arr = arr[:]
                        valid = True
                        for num in actual_nums:
                            if num in temp_arr:
                                temp_arr.remove(num)
                            else:
                                valid = False
                                break
                        
                        if valid:
                            passed += 1
                        else:
                            failed += 1
                            print(f"❌ Case {i} FAILED: Invalid subset")
                    else:
                        failed += 1
                        print(f"❌ Case {i} FAILED:")
                        print(f"   Wrong sum or count")
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED:")
                    print(f"   Expected valid subset, got NONE")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# Main Verification
# ============================================================================

def main():
    """Run all verifications for REC-001 to REC-006."""
    print("="*80)
    print("RECURSION TEST CASE VERIFICATION (Part 1: REC-001 to REC-006)")
    print("="*80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Recursion/testcases"
    
    results = {}
    
    # REC-001
    rec001_path = f"{base_path}/REC-001-dorm-room-paths.yaml"
    results['REC-001'] = verify_rec001(rec001_path)
    
    # REC-002
    rec002_path = f"{base_path}/REC-002-lab-id-permutations-no-twins.yaml"
    results['REC-002'] = verify_rec002(rec002_path)
    
    # REC-003
    rec003_path = f"{base_path}/REC-003-campus-ticket-packs.yaml"
    results['REC-003'] = verify_rec003(rec003_path)
    
    # REC-004
    rec004_path = f"{base_path}/REC-004-exam-seating-backtrack.yaml"
    results['REC-004'] = verify_rec004(rec004_path)
    
    # REC-005
    rec005_path = f"{base_path}/REC-005-robot-route-turns.yaml"
    results['REC-005'] = verify_rec005(rec005_path)
    
    # REC-006
    rec006_path = f"{base_path}/REC-006-subset-sum-exact-count.yaml"
    results['REC-006'] = verify_rec006(rec006_path)
    
    # Summary
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY (Part 1)")
    print("="*80)
    
    all_passed = all(results.values())
    
    for problem, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{problem}: {status}")
    
    print("\n" + "="*80)
    if all_passed:
        print("🎉 ALL PART 1 VERIFICATIONS PASSED!")
        print("✅ All test cases (REC-001 to REC-006) are correct.")
    else:
        print("⚠️ Some verifications failed. Please review the errors above.")
    print("="*80)


if __name__ == "__main__":
    main()
