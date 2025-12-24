#!/usr/bin/env python3
"""
Verify Recursion test cases against editorial reference solutions - Part 2.
Tests REC-007, REC-011, REC-013, REC-014, REC-016 (verifiable problems).
Notes: REC-008, 009, 010, 012, 015 need manual review due to complexity.
"""

from collections import defaultdict, deque
import itertools

def load_yaml_testcases(filepath):
    """Load test cases from YAML file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
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
# REC-007: Campus Lights Placement - Editorial Solution
# ============================================================================

def find_light_placements_editorial(n, k, d):
    """Find all ways to place k lights with distance >= d."""
    results = []
    
    def backtrack(start, chosen):
        if len(chosen) == k:
            results.append(chosen[:])
            return
        
        if start >= n:
            return
        
        # Calculate if we have enough positions left
        needed = k - len(chosen)
        # We need at least (needed-1)*d + 1 positions
        if start + (needed - 1) * d >= n and needed > 1:
            return
        
        for pos in range(start, n):
            if not chosen or pos - chosen[-1] >= d:
                chosen.append(pos)
                backtrack(pos + 1, chosen)
                chosen.pop()
    
    backtrack(0, [])
    return results if results else None

def verify_rec007(filepath):
    """Verify REC-007 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-007: Campus Lights Placement")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            parts = case['input'].strip().split()
            n, k, d = int(parts[0]), int(parts[1]), int(parts[2])
            
            expected_output = case['output'].strip()
            actual_result = find_light_placements_editorial(n, k, d)
            
            if expected_output == "NONE":
                if actual_result is None:
                    passed += 1
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED: Expected NONE, got result")
            else:
                expected_lines = sorted(expected_output.split('\n'))
                if actual_result:
                    actual_lines = sorted([' '.join(map(str, r)) for r in actual_result])
                    if expected_lines == actual_lines:
                        passed += 1
                    else:
                        failed += 1
                        print(f"❌ Case {i} FAILED:")
                        print(f"   Input: n={n}, k={k}, d={d}")
                        print(f"   Expected count: {len(expected_lines)}")
                        print(f"   Actual count: {len(actual_lines)}")
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED: Expected result, got NONE")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-011: Campus Course Ordering - Editorial Solution (Topological Sort)
# ============================================================================

def topological_sort_editorial(n, edges):
    """Topological sort using Kahn's algorithm."""
    adj = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != n:
        return None  # Cycle detected
    
    return result

def verify_rec011(filepath):
    """Verify REC-011 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-011: Campus Course Ordering (Topological Sort)")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            lines = case['input'].strip().split('\n')
            first_line = lines[0].split()
            n, m = int(first_line[0]), int(first_line[1])
            
            edges = []
            for j in range(1, len(lines)):
                if lines[j].strip():
                    u, v = map(int, lines[j].split())
                    edges.append((u, v))
            
            expected_output = case['output'].strip()
            actual_result = topological_sort_editorial(n, edges)
            
            if expected_output == "IMPOSSIBLE":
                if actual_result is None:
                    passed += 1
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED: Expected IMPOSSIBLE, got valid ordering")
            else:
                if actual_result:
                    # Verify it's a valid topological ordering
                    position = {node: idx for idx, node in enumerate(actual_result)}
                    valid = True
                    for u, v in edges:
                        if position[u] >= position[v]:
                            valid = False
                            break
                    
                    if valid and len(actual_result) == n:
                        passed += 1
                    else:
                        failed += 1
                        print(f"❌ Case {i} FAILED: Invalid topological ordering")
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED: Expected valid ordering, got IMPOSSIBLE")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-013: Palindrome Partition Min Count - Editorial Solution
# ============================================================================

def is_palindrome(s):
    return s == s[::-1]

def min_palindrome_partition_editorial(s, L):
    """Find minimum palindrome partition with max length L."""
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    partition = [None] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(max(0, i - L), i):
            substr = s[j:i]
            if is_palindrome(substr) and dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1
                partition[i] = j
    
    if dp[n] == float('inf'):
        return None
    
    # Reconstruct one valid partition
    result = []
    i = n
    while i > 0:
        j = partition[i]
        result.append(s[j:i])
        i = j
    
    return ' '.join(reversed(result))

def verify_rec013(filepath):
    """Verify REC-013 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-013: Palindrome Partition Min Count")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            lines = case['input'].strip().split('\n')
            s = lines[0]
            L = int(lines[1])
            
            expected_output = case['output'].strip()
            actual_result = min_palindrome_partition_editorial(s, L)
            
            if expected_output == "NONE":
                if actual_result is None:
                    passed += 1
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED: Expected NONE")
            else:
                if actual_result:
                    # Verify the partition is valid
                    parts = actual_result.split()
                    expected_parts = expected_output.split()
                    
                    # Check same number of parts
                    if len(parts) == len(expected_parts):
                        # Verify all parts are palindromes and reconstruct s
                        reconstructed = ''.join(parts)
                        all_palindromes = all(is_palindrome(p) and len(p) <= L for p in parts)
                        
                        if reconstructed == s and all_palindromes:
                            passed += 1
                        else:
                            failed += 1
                            print(f"❌ Case {i} FAILED: Invalid partition")
                    else:
                        failed += 1
                        print(f"❌ Case {i} FAILED: Wrong partition count")
                else:
                    failed += 1
                    print(f"❌ Case {i} FAILED: Expected valid partition, got NONE")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# REC-014: Target Sum Limited Negations - Editorial Solution
# ============================================================================

def can_reach_target_editorial(arr, k, target):
    """Check if target is reachable by negating at most k elements."""
    n = len(arr)
    
    # Try all combinations of negations
    for mask in range(1 << n):
        if bin(mask).count('1') > k:
            continue
        
        temp_sum = sum(arr[i] if not (mask & (1 << i)) else -arr[i] for i in range(n))
        if temp_sum == target:
            return "YES"
    
    return "NO"

def verify_rec014(filepath):
    """Verify REC-014 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-014: Target Sum Limited Negations")
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
            
            expected = case['output'].strip()
            actual = can_reach_target_editorial(arr, k, target)
            
            if actual == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: arr={arr}, k={k}, target={target}")
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
# REC-016: Lexicographic Gray Code - Editorial Solution
# ============================================================================

def gray_code_editorial(n):
    """Generate n-bit Gray code."""
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1']
    
    prev = gray_code_editorial(n - 1)
    result = []
    
    # Add 0 prefix to first half
    for code in prev:
        result.append('0' + code)
    
    # Add 1 prefix to reversed second half
    for code in reversed(prev):
        result.append('1' + code)
    
    return result

def verify_rec016(filepath):
    """Verify REC-016 test cases."""
    print("\n" + "="*80)
    print("VERIFYING REC-016: Lexicographic Gray Code")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            n = int(case['input'].strip())
            expected_lines = case['output'].strip().split('\n')
            
            actual_result = gray_code_editorial(n)
            
            if actual_result == expected_lines:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: n={n}")
                print(f"   Expected count: {len(expected_lines)}")
                print(f"   Actual count: {len(actual_result)}")
                if len(expected_lines) <= 8:
                    print(f"   Expected: {expected_lines}")
                    print(f"   Actual: {actual_result}")
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
    """Run verifications for selected Part 2 problems."""
    print("="*80)
    print("RECURSION TEST CASE VERIFICATION (Part 2: Selected Problems)")
    print("="*80)
    print("\nVerifying: REC-007, REC-011, REC-013, REC-014, REC-016")
    print("Skipped (need manual review): REC-008, REC-009, REC-010, REC-012, REC-015")
    print("="*80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Recursion/testcases"
    
    results = {}
    
    # REC-007
    rec007_path = f"{base_path}/REC-007-campus-lights-placement.yaml"
    results['REC-007'] = verify_rec007(rec007_path)
    
    # REC-011
    rec011_path = f"{base_path}/REC-011-campus-course-ordering.yaml"
    results['REC-011'] = verify_rec011(rec011_path)
    
    # REC-013
    rec013_path = f"{base_path}/REC-013-palindrome-partition-min-count.yaml"
    results['REC-013'] = verify_rec013(rec013_path)
    
    # REC-014
    rec014_path = f"{base_path}/REC-014-target-sum-limited-negations.yaml"
    results['REC-014'] = verify_rec014(rec014_path)
    
    # REC-016
    rec016_path = f"{base_path}/REC-016-lexicographic-gray-code.yaml"
    results['REC-016'] = verify_rec016(rec016_path)
    
    # Summary
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY (Part 2 - Selected Problems)")
    print("="*80)
    
    all_passed = all(results.values())
    
    for problem, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{problem}: {status}")
    
    print("\n" + "="*80)
    if all_passed:
        print("🎉 ALL VERIFIED PROBLEMS PASSED!")
        print("✅ Verified: REC-007, REC-011, REC-013, REC-014, REC-016")
        print("⚠️  Note: REC-008, 009, 010, 012, 015 need manual editorial review")
    else:
        print("⚠️ Some verifications failed. Please review the errors above.")
    print("="*80)


if __name__ == "__main__":
    main()
