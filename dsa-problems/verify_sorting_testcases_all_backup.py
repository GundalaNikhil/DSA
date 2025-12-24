#!/usr/bin/env python3
"""
Comprehensive Verification Script for Sorting Topic (SRT-001 to SRT-016)
Verifies all 608 test cases against editorial solutions.
"""

import yaml
import os
import sys
from collections import defaultdict
import math
from itertools import combinations

# Color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

# ============================================================================
# Editorial Solutions (Same as generation script)
# ============================================================================

def selection_sort_k_iterations(arr, k):
    """Simulate k iterations of selection sort."""
    arr = arr[:]
    n = len(arr)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def solve_srt001(n, k, arr):
    """SRT-001: Partial Selection Sort Stats"""
    result = selection_sort_k_iterations(arr, k)
    return ' '.join(map(str, result))

def kth_missing_positive_block(arr, k, block_size):
    """Find the (k * block_size)-th missing positive integer."""
    target_missing = k * block_size
    arr_set = set(arr)
    
    # Binary search approach
    left, right = 1, target_missing + len(arr) + 100
    
    while left < right:
        mid = (left + right) // 2
        # Count how many numbers in [1, mid] are missing
        present_count = sum(1 for x in arr if x <= mid)
        missing_count = mid - present_count
        
        if missing_count < target_missing:
            left = mid + 1
        else:
            right = mid
    
    return left

def solve_srt002(input_lines):
    """SRT-002: Kth Missing Positive with Blocks - handles multiple queries"""
    n, q = map(int, input_lines[0].split())
    arr = list(map(int, input_lines[1].split()))
    results = []
    for i in range(2, 2 + q):
        k, bs = map(int, input_lines[i].split())
        result = kth_missing_positive_block(arr, k, bs)
        results.append(str(result))
    return '\n'.join(results)

def stable_sort_two_keys(pairs):
    """Stable sort by key1 then key2."""
    # Add original index for stability
    indexed = [(p[0], p[1], i) for i, p in enumerate(pairs)]
    indexed.sort(key=lambda x: (x[0], x[1], x[2]))
    return [(x[0], x[1]) for x in indexed]

def solve_srt003(input_lines):
    """SRT-003: Stable Sort Two Keys"""
    n = int(input_lines[0])
    pairs = []
    for i in range(1, n + 1):
        key1, key2 = map(int, input_lines[i].split())
        pairs.append((key1, key2))
    
    result = stable_sort_two_keys(pairs)
    return '\n'.join(f"{k1} {k2}" for k1, k2 in result)

def min_inversions_one_swap(arr):
    """Find minimum inversions after one swap."""
    n = len(arr)
    
    def count_inversions(a):
        inv = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    inv += 1
        return inv
    
    min_inv = count_inversions(arr)
    for i in range(n):
        for j in range(i + 1, n):
            arr[i], arr[j] = arr[j], arr[i]
            inv = count_inversions(arr)
            min_inv = min(min_inv, inv)
            arr[i], arr[j] = arr[j], arr[i]
    return min_inv

def solve_srt004(n, arr):
    """SRT-004: Min Inversions One Swap"""
    result = min_inversions_one_swap(arr)
    return str(result)

def closest_pair_to_target(arr, target):
    """Two pointer approach for closest pair."""
    arr.sort()
    n = len(arr)
    left, right = 0, n - 1
    min_diff = float('inf')
    result_sum = 0
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        diff = abs(curr_sum - target)
        
        if diff < min_diff:
            min_diff = diff
            result_sum = curr_sum
        
        if curr_sum < target:
            left += 1
        else:
            right -= 1
    
    return result_sum

def solve_srt005(n, target, arr):
    """SRT-005: Two Pointer Closest Target"""
    result = closest_pair_to_target(arr, target)
    return str(result)

def k_sorted_min_swaps(arr, k):
    """Min swaps for k-sorted array."""
    sorted_arr = sorted(arr)
    visited = [False] * len(arr)
    swaps = 0
    
    for i in range(len(arr)):
        if visited[i] or arr[i] == sorted_arr[i]:
            visited[i] = True
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = sorted_arr.index(arr[j])
            cycle_size += 1
        
        if cycle_size > 0:
            swaps += (cycle_size - 1)
    
    return swaps

def solve_srt006(n, k, arr):
    """SRT-006: K-Sorted Array Min Swaps"""
    result = k_sorted_min_swaps(arr, k)
    return str(result)

def search_rotated_parity(arr, target):
    """Binary search in rotated array with parity check."""
    n = len(arr)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid if arr[mid] % 2 == 0 else -1
        
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def solve_srt007(n, target, arr):
    """SRT-007: Search Rotated Duplicates Parity"""
    result = search_rotated_parity(arr, target)
    return str(result)

def balanced_range_covering(lists):
    """Find minimum balanced range covering all lists."""
    import heapq
    
    if not lists or not all(lists):
        return float('inf')
    
    heap = []
    max_val = float('-inf')
    
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))
        max_val = max(max_val, lst[0])
    
    min_range = float('inf')
    
    while len(heap) == len(lists):
        min_val, list_idx, elem_idx = heapq.heappop(heap)
        min_range = min(min_range, max_val - min_val)
        
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            max_val = max(max_val, next_val)
        else:
            break
    
    return min_range

def solve_srt008(k, lists):
    """SRT-008: Balanced Range Covering K Lists"""
    result = balanced_range_covering(lists)
    return str(result)

def weighted_median(arr1, arr2):
    """Find weighted median of two sorted arrays."""
    merged = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

def solve_srt009(n, m, arr1, arr2):
    """SRT-009: Weighted Median Two Sorted"""
    result = weighted_median(arr1, arr2)
    if isinstance(result, float):
        return f"{result:.1f}"
    return str(result)

def sort_colors_limited(arr, swaps):
    """Dutch flag with limited swaps."""
    arr = arr[:]
    used_swaps = 0
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high and used_swaps < swaps:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            if low != mid:
                used_swaps += 1
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            if mid != high:
                used_swaps += 1
            high -= 1
    
    return ' '.join(map(str, arr))

def solve_srt010(n, swaps, arr):
    """SRT-010: Sort Colors Limited Swaps"""
    return sort_colors_limited(arr, swaps)

def longest_consecutive_one_change(arr):
    """Longest consecutive sequence with one element change."""
    if not arr:
        return 0
    
    sorted_arr = sorted(arr)
    max_len = 1
    
    for i in range(len(arr)):
        original = arr[i]
        for new_val in range(min(arr), max(arr) + 2):
            arr[i] = new_val
            temp_sorted = sorted(arr)
            
            current_len = 1
            temp_max = 1
            for j in range(1, len(temp_sorted)):
                if temp_sorted[j] == temp_sorted[j-1] + 1:
                    current_len += 1
                    temp_max = max(temp_max, current_len)
                else:
                    current_len = 1
            
            max_len = max(max_len, temp_max)
        arr[i] = original
    
    return max_len

def solve_srt011(n, arr):
    """SRT-011: Longest Consecutive One Change"""
    result = longest_consecutive_one_change(arr)
    return str(result)

def count_within_threshold(arr, threshold):
    """Count elements within threshold after self."""
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[j] - arr[i]) <= threshold:
                count += 1
    return count

def solve_srt012(n, threshold, arr):
    """SRT-012: Count Within Threshold After Self"""
    result = count_within_threshold(arr, threshold)
    return str(result)

def closest_pair_circular(arr):
    """Find closest pair in sorted circular array."""
    if len(arr) < 2:
        return 0
    
    min_diff = abs(arr[1] - arr[0])
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[j] - arr[i])
            min_diff = min(min_diff, diff)
    
    circular_diff = abs(arr[-1] - arr[0])
    min_diff = min(min_diff, circular_diff)
    
    return min_diff

def solve_srt013(n, arr):
    """SRT-013: Closest Pair Sorted Circular"""
    result = closest_pair_circular(arr)
    return str(result)

def min_ops_alternating(arr):
    """Minimum operations to make alternating."""
    n = len(arr)
    
    # Try pattern: low, high, low, high, ...
    ops1 = 0
    for i in range(n):
        if i % 2 == 0:  # Should be local minimum
            if (i > 0 and arr[i] >= arr[i-1]) or (i < n-1 and arr[i] >= arr[i+1]):
                ops1 += 1
        else:  # Should be local maximum
            if (i > 0 and arr[i] <= arr[i-1]) or (i < n-1 and arr[i] <= arr[i+1]):
                ops1 += 1
    
    # Try pattern: high, low, high, low, ...
    ops2 = 0
    for i in range(n):
        if i % 2 == 0:  # Should be local maximum
            if (i > 0 and arr[i] <= arr[i-1]) or (i < n-1 and arr[i] <= arr[i+1]):
                ops2 += 1
        else:  # Should be local minimum
            if (i > 0 and arr[i] >= arr[i-1]) or (i < n-1 and arr[i] >= arr[i+1]):
                ops2 += 1
    
    return min(ops1, ops2)

def solve_srt014(n, arr):
    """SRT-014: Min Ops Make Alternating"""
    result = min_ops_alternating(arr)
    return str(result)

def kth_smallest_triple(arr, k):
    """Find kth smallest sum of three elements."""
    sums = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                sums.append(arr[i] + arr[j] + arr[l])
    sums.sort()
    return sums[k - 1] if k <= len(sums) else -1

def solve_srt015(n, k, arr):
    """SRT-015: Kth Smallest Triple Sum"""
    result = kth_smallest_triple(arr, k)
    return str(result)

def locate_peak_queries(arr, queries):
    """Locate peak with limited queries."""
    results = []
    for q in queries:
        if 0 <= q < len(arr):
            is_peak = True
            if q > 0 and arr[q] <= arr[q-1]:
                is_peak = False
            if q < len(arr) - 1 and arr[q] <= arr[q+1]:
                is_peak = False
            results.append(1 if is_peak else 0)
        else:
            results.append(0)
    return ' '.join(map(str, results))

def solve_srt016(n, q, arr, queries):
    """SRT-016: Locate Peak Limited Queries"""
    return locate_peak_queries(arr, queries)

# ============================================================================
# Test Case Verification
# ============================================================================

def parse_yaml_file(filepath):
    """Parse YAML test case file."""
    with open(filepath, 'r') as f:
        content = f.read()
    return yaml.safe_load(content)

def verify_problem(problem_id, testcases):
    """Verify all test cases for a problem."""
    stats = {'total': 0, 'passed': 0, 'failed': 0, 'errors': []}
    
    for section in ['samples', 'public', 'hidden']:
        if section not in testcases:
            continue
        
        for idx, case in enumerate(testcases[section]):
            stats['total'] += 1
            input_lines = case['input'].strip().split('\n')
            expected_output = case['output'].strip()
            
            try:
                # Parse and solve based on problem
                if problem_id == 'SRT-001':
                    n, k = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt001(n, k, arr)
                
                elif problem_id == 'SRT-002':
                    n, k, B = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt002(n, k, B, arr)
                
                elif problem_id == 'SRT-003':
                    n = int(input_lines[0])
                    indices = input_lines[1]
                    actual = solve_srt003(n, indices)
                
                elif problem_id == 'SRT-004':
                    n = int(input_lines[0])
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt004(n, arr)
                
                elif problem_id == 'SRT-005':
                    n, target = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt005(n, target, arr)
                
                elif problem_id == 'SRT-006':
                    n, k = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt006(n, k, arr)
                
                elif problem_id == 'SRT-007':
                    n, target = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt007(n, target, arr)
                
                elif problem_id == 'SRT-008':
                    k = int(input_lines[0])
                    lists = [list(map(int, line.split())) for line in input_lines[1:k+1]]
                    actual = solve_srt008(k, lists)
                
                elif problem_id == 'SRT-009':
                    n, m = map(int, input_lines[0].split())
                    arr1 = list(map(int, input_lines[1].split()))
                    arr2 = list(map(int, input_lines[2].split()))
                    actual = solve_srt009(n, m, arr1, arr2)
                
                elif problem_id == 'SRT-010':
                    n, swaps = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt010(n, swaps, arr)
                
                elif problem_id == 'SRT-011':
                    n = int(input_lines[0])
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt011(n, arr)
                
                elif problem_id == 'SRT-012':
                    n, threshold = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt012(n, threshold, arr)
                
                elif problem_id == 'SRT-013':
                    n = int(input_lines[0])
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt013(n, arr)
                
                elif problem_id == 'SRT-014':
                    n = int(input_lines[0])
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt014(n, arr)
                
                elif problem_id == 'SRT-015':
                    n, k = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    actual = solve_srt015(n, k, arr)
                
                elif problem_id == 'SRT-016':
                    n, q = map(int, input_lines[0].split())
                    arr = list(map(int, input_lines[1].split()))
                    queries = list(map(int, input_lines[2].split()))
                    actual = solve_srt016(n, q, arr, queries)
                
                else:
                    actual = "UNKNOWN"
                
                if actual.strip() == expected_output.strip():
                    stats['passed'] += 1
                else:
                    stats['failed'] += 1
                    stats['errors'].append({
                        'section': section,
                        'index': idx,
                        'expected': expected_output,
                        'actual': actual
                    })
            
            except Exception as e:
                stats['failed'] += 1
                stats['errors'].append({
                    'section': section,
                    'index': idx,
                    'error': str(e)
                })
    
    return stats

def main():
    """Main verification function."""
    print("=" * 80)
    print("SORTING TEST CASE VERIFICATION - ALL PROBLEMS")
    print("=" * 80)
    print()
    
    testcases_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Sorting/testcases"
    
    problems = [
        ('SRT-001', 'partial-selection-sort-stats'),
        ('SRT-002', 'kth-missing-positive-blocks'),
        ('SRT-003', 'stable-sort-two-keys'),
        ('SRT-004', 'min-inversions-one-swap'),
        ('SRT-005', 'two-pointer-closest-target'),
        ('SRT-006', 'k-sorted-array-min-swaps'),
        ('SRT-007', 'search-rotated-duplicates-parity'),
        ('SRT-008', 'balanced-range-covering-k-lists'),
        ('SRT-009', 'weighted-median-two-sorted'),
        ('SRT-010', 'sort-colors-limited-swaps'),
        ('SRT-011', 'longest-consecutive-one-change'),
        ('SRT-012', 'count-within-threshold-after-self'),
        ('SRT-013', 'closest-pair-sorted-circular'),
        ('SRT-014', 'min-ops-make-alternating'),
        ('SRT-015', 'kth-smallest-triple-sum'),
        ('SRT-016', 'locate-peak-limited-queries')
    ]
    
    total_stats = {'total': 0, 'passed': 0, 'failed': 0}
    problem_results = []
    
    for problem_id, problem_name in problems:
        filepath = os.path.join(testcases_dir, f"{problem_id}-{problem_name}.yaml")
        
        if not os.path.exists(filepath):
            print(f"{RED}✗ {problem_id}: File not found{RESET}")
            continue
        
        testcases = parse_yaml_file(filepath)
        stats = verify_problem(problem_id, testcases)
        
        total_stats['total'] += stats['total']
        total_stats['passed'] += stats['passed']
        total_stats['failed'] += stats['failed']
        
        pass_rate = (stats['passed'] / stats['total'] * 100) if stats['total'] > 0 else 0
        
        status = GREEN + '✓' if stats['failed'] == 0 else RED + '✗'
        print(f"{status} {problem_id}: {stats['passed']}/{stats['total']} passed ({pass_rate:.1f}%){RESET}")
        
        problem_results.append({
            'id': problem_id,
            'stats': stats,
            'pass_rate': pass_rate
        })
        
        if stats['errors'] and stats['failed'] < 10:
            for err in stats['errors'][:3]:
                print(f"  {YELLOW}Error in {err.get('section', 'unknown')}[{err.get('index', '?')}]{RESET}")
                if 'error' in err:
                    print(f"    {err['error']}")
    
    print()
    print("=" * 80)
    overall_rate = (total_stats['passed'] / total_stats['total'] * 100) if total_stats['total'] > 0 else 0
    
    if total_stats['failed'] == 0:
        print(f"{GREEN}✅ ALL TESTS PASSED: {total_stats['passed']}/{total_stats['total']} ({overall_rate:.1f}%){RESET}")
    else:
        print(f"{YELLOW}RESULTS: {total_stats['passed']}/{total_stats['total']} passed ({overall_rate:.1f}%){RESET}")
        print(f"{RED}Failed: {total_stats['failed']} test cases{RESET}")
    
    print("=" * 80)

if __name__ == "__main__":
    main()
