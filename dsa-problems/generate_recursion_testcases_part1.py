#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Recursion Topic (REC-001 to REC-016)
Following the Universal Test Case Generation Prompt.
Target: 30-40 test cases per problem with proper YAML format.
"""

import random
import math
from itertools import permutations, combinations

def format_testcase_yaml(data):
    """Format test cases in proper YAML with |- syntax."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section_name in ['samples', 'public', 'hidden']:
        if section_name not in data or not data[section_name]:
            continue
        lines.append(f"{section_name}:")
        for case in data[section_name]:
            lines.append("- input: |-")
            for line in case['input'].strip().split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            for line in case['output'].strip().split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines)


# ============================================================================
# REC-001: Dorm Room Paths (Grid Paths)
# ============================================================================

def count_paths_grid(r, c):
    """Count paths in grid using combinatorics: C(r+c-2, r-1)"""
    if r == 1 or c == 1:
        return 1
    return math.comb(r + c - 2, r - 1)

def generate_rec001_cases():
    cases = {'problem_id': 'REC-001', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    for r, c in [(2, 3), (3, 3), (1, 5)]:
        result = count_paths_grid(r, c)
        cases['samples'].append({'input': f"{r} {c}", 'output': str(result)})
    
    # Public
    for r, c in [(1, 1), (2, 2), (3, 4), (4, 4), (5, 5)]:
        result = count_paths_grid(r, c)
        cases['public'].append({'input': f"{r} {c}", 'output': str(result)})
    
    # Hidden (30 cases)
    test_cases = [
        (1, 10), (10, 1), (6, 6), (7, 7), (8, 8),
        (10, 10), (12, 12), (15, 15), (20, 20), (25, 25),
        (5, 10), (10, 5), (8, 12), (12, 8), (15, 20),
        (20, 15), (7, 14), (14, 7), (9, 18), (18, 9),
        (6, 15), (15, 6), (11, 13), (13, 11), (16, 17),
        (17, 16), (19, 21), (21, 19), (22, 23), (23, 22)
    ]
    
    for r, c in test_cases:
        result = count_paths_grid(r, c)
        cases['hidden'].append({'input': f"{r} {c}", 'output': str(result)})
    
    return cases


# ============================================================================
# REC-002: Lab ID Permutations No Twins
# ============================================================================

def generate_no_twin_permutations(s):
    """Generate permutations with no adjacent duplicates."""
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
            
            if path and path[-1] == remaining[i]:
                continue
            
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    backtrack([], chars)
    return results if results else ["NONE"]

def generate_rec002_cases():
    cases = {'problem_id': 'REC-002', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    for s in ["aab", "aabb", "abc"]:
        result = generate_no_twin_permutations(s)
        cases['samples'].append({'input': s, 'output': '\n'.join(result)})
    
    # Public
    for s in ["a", "ab", "aaa", "abcd", "aaaa"]:
        result = generate_no_twin_permutations(s)
        cases['public'].append({'input': s, 'output': '\n'.join(result)})
    
    # Hidden (30 cases)
    test_strings = [
        "aa", "bb", "abab", "aabbcc", "aaabbb",
        "abcde", "aabbccd", "xyz", "abcc", "aabbc",
        "pqr", "aabbccdd", "abcabc", "xyyz", "aabbccddee",
        "mnop", "aaabbbc", "qrst", "aabbbccc", "defg",
        "aabbcc", "hijkl", "aaabbbccc", "uvwx", "aabbccdd",
        "yz", "aaaa", "bbbb", "abcdefgh", "aabbccddee"
    ]
    
    for s in test_strings:
        result = generate_no_twin_permutations(s)
        cases['hidden'].append({'input': s, 'output': '\n'.join(result)})
    
    return cases


# ============================================================================
# REC-003: Campus Ticket Packs (Coin Change Count)
# ============================================================================

def count_ways_coin_change(coins, target):
    """Count ways to make target using given coins (unbounded)."""
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    return dp[target]

def generate_rec003_cases():
    cases = {'problem_id': 'REC-003', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ([1, 2, 5], 5),
        ([2, 3, 5], 7),
        ([1, 5, 10], 12)
    ]
    
    for coins, target in sample_data:
        result = count_ways_coin_change(coins, target)
        inp = f"{len(coins)} {target}\n" + ' '.join(map(str, coins))
        cases['samples'].append({'input': inp, 'output': str(result)})
    
    # Public
    public_data = [
        ([1], 5),
        ([2], 4),
        ([1, 2], 3),
        ([1, 5], 10),
        ([2, 5, 10], 15)
    ]
    
    for coins, target in public_data:
        result = count_ways_coin_change(coins, target)
        inp = f"{len(coins)} {target}\n" + ' '.join(map(str, coins))
        cases['public'].append({'input': inp, 'output': str(result)})
    
    # Hidden (30 cases)
    hidden_data = []
    
    # Small coins, small target
    for _ in range(5):
        coins = sorted(random.sample(range(1, 6), random.randint(2, 4)))
        target = random.randint(5, 15)
        hidden_data.append((coins, target))
    
    # Medium coins, medium target
    for _ in range(10):
        coins = sorted(random.sample(range(1, 11), random.randint(3, 5)))
        target = random.randint(15, 30)
        hidden_data.append((coins, target))
    
    # Large coins, large target
    for _ in range(10):
        coins = sorted(random.sample(range(1, 21), random.randint(3, 6)))
        target = random.randint(30, 50)
        hidden_data.append((coins, target))
    
    # Edge cases
    hidden_data.extend([
        ([1], 50),
        ([1, 2, 5, 10, 20], 50),
        ([3, 5, 7], 15),
        ([2, 3, 7], 20),
        ([1, 10, 25], 30)
    ])
    
    for coins, target in hidden_data:
        result = count_ways_coin_change(coins, target)
        inp = f"{len(coins)} {target}\n" + ' '.join(map(str, coins))
        cases['hidden'].append({'input': inp, 'output': str(result)})
    
    return cases


# ============================================================================
# REC-004: Exam Seating Backtrack (N-Queens)
# ============================================================================

def solve_n_queens(n):
    """Solve N-Queens and return count of solutions."""
    count = 0
    
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def backtrack(row, board):
        nonlocal count
        if row == n:
            count += 1
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1
    
    backtrack(0, [-1] * n)
    return count

def generate_rec004_cases():
    cases = {'problem_id': 'REC-004', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    for n in [4, 5, 6]:
        result = solve_n_queens(n)
        cases['samples'].append({'input': str(n), 'output': str(result)})
    
    # Public
    for n in [1, 2, 3, 7, 8]:
        result = solve_n_queens(n)
        cases['public'].append({'input': str(n), 'output': str(result)})
    
    # Hidden (30 cases)
    hidden_ns = [9, 10, 11, 12, 13, 14] + list(range(1, 15)) + list(range(4, 15))
    
    for n in hidden_ns[:30]:
        result = solve_n_queens(n)
        cases['hidden'].append({'input': str(n), 'output': str(result)})
    
    return cases


# ============================================================================
# REC-005: Robot Route Turns (Grid with Turns Constraint)
# ============================================================================

def count_paths_with_max_turns(r, c, max_turns):
    """Count paths with at most max_turns direction changes."""
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

def generate_rec005_cases():
    cases = {'problem_id': 'REC-005', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    for r, c, t in [(3, 3, 2), (2, 4, 1), (4, 4, 3)]:
        result = count_paths_with_max_turns(r, c, t)
        cases['samples'].append({'input': f"{r} {c} {t}", 'output': str(result)})
    
    # Public
    for r, c, t in [(2, 2, 0), (2, 2, 1), (3, 3, 0), (3, 3, 1), (4, 4, 2)]:
        result = count_paths_with_max_turns(r, c, t)
        cases['public'].append({'input': f"{r} {c} {t}", 'output': str(result)})
    
    # Hidden (30 cases)
    hidden_data = [
        (5, 5, 2), (5, 5, 3), (5, 5, 4), (6, 6, 2), (6, 6, 3),
        (6, 6, 4), (7, 7, 3), (7, 7, 4), (8, 8, 3), (8, 8, 4),
        (3, 4, 1), (4, 3, 1), (3, 5, 2), (5, 3, 2), (4, 6, 2),
        (6, 4, 2), (5, 7, 3), (7, 5, 3), (6, 8, 3), (8, 6, 3),
        (10, 10, 5), (12, 12, 6), (9, 9, 4), (11, 11, 5), (10, 5, 3),
        (5, 10, 3), (8, 4, 2), (4, 8, 2), (7, 9, 4), (9, 7, 4)
    ]
    
    for r, c, t in hidden_data:
        result = count_paths_with_max_turns(r, c, t)
        cases['hidden'].append({'input': f"{r} {c} {t}", 'output': str(result)})
    
    return cases


# ============================================================================
# REC-006: Subset Sum Exact Count
# ============================================================================

def find_subset_sum(arr, k, target):
    """Find a subset of exactly k elements that sums to target."""
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

def generate_rec006_cases():
    cases = {'problem_id': 'REC-006', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples
    sample_data = [
        ([4, 1, 6, 2], 2, 7),
        ([1, 2, 3, 4, 5], 3, 9),
        ([10, 20, 30], 2, 50)
    ]
    
    for arr, k, target in sample_data:
        result = find_subset_sum(arr, k, target)
        inp = f"{len(arr)} {k} {target}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result)) if result else "NONE"
        cases['samples'].append({'input': inp, 'output': out})
    
    # Public (some with NONE)
    public_data = [
        ([1, 2, 3], 2, 5),
        ([1, 2, 3], 2, 10),  # NONE
        ([5, 10, 15, 20], 3, 45),
        ([1, 1, 1], 2, 2),
        ([2, 4, 6, 8], 2, 100)  # NONE
    ]
    
    for arr, k, target in public_data:
        result = find_subset_sum(arr, k, target)
        inp = f"{len(arr)} {k} {target}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result)) if result else "NONE"
        cases['public'].append({'input': inp, 'output': out})
    
    # Hidden (30 cases with mix of valid and NONE)
    random.seed(42)
    hidden_data = []
    
    for _ in range(20):
        n = random.randint(5, 15)
        arr = [random.randint(1, 50) for _ in range(n)]
        k = random.randint(2, min(n, 8))
        # Make some achievable
        if random.random() < 0.7:
            subset_indices = random.sample(range(n), k)
            target = sum(arr[i] for i in subset_indices)
        else:
            target = random.randint(1, 200)
        hidden_data.append((arr, k, target))
    
    # Add some guaranteed NONE cases
    for _ in range(10):
        n = random.randint(5, 10)
        arr = [random.randint(1, 20) for _ in range(n)]
        k = random.randint(2, min(n, 5))
        target = sum(arr) + 100  # Impossible
        hidden_data.append((arr, k, target))
    
    for arr, k, target in hidden_data:
        result = find_subset_sum(arr, k, target)
        inp = f"{len(arr)} {k} {target}\n" + ' '.join(map(str, arr))
        out = ' '.join(map(str, result)) if result else "NONE"
        cases['hidden'].append({'input': inp, 'output': out})
    
    return cases


# ============================================================================
# Main Generation (Part 1: REC-001 to REC-006)
# ============================================================================

def main():
    """Generate test cases for REC-001 to REC-006."""
    print("=" * 80)
    print("RECURSION TEST CASE GENERATION - PART 1 (REC-001 to REC-006)")
    print("=" * 80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Recursion/testcases"
    
    problems = [
        ("REC-001", "dorm-room-paths", generate_rec001_cases),
        ("REC-002", "lab-id-permutations-no-twins", generate_rec002_cases),
        ("REC-003", "campus-ticket-packs", generate_rec003_cases),
        ("REC-004", "exam-seating-backtrack", generate_rec004_cases),
        ("REC-005", "robot-route-turns", generate_rec005_cases),
        ("REC-006", "subset-sum-exact-count", generate_rec006_cases),
    ]
    
    total_cases = 0
    
    for prob_id, slug, generator_func in problems:
        print(f"\n[{prob_id}] Generating {slug}...")
        cases = generator_func()
        yaml_content = format_testcase_yaml(cases)
        
        output_path = f"{base_path}/{prob_id}-{slug}.yaml"
        with open(output_path, 'w') as f:
            f.write(yaml_content)
        
        count = len(cases['samples']) + len(cases['public']) + len(cases['hidden'])
        total_cases += count
        print(f"✅ {prob_id}: {count} test cases")
        print(f"   Samples: {len(cases['samples'])}, Public: {len(cases['public'])}, Hidden: {len(cases['hidden'])}")
    
    print("\n" + "=" * 80)
    print(f"✅ PART 1 COMPLETE: {total_cases} test cases generated")
    print("=" * 80)


if __name__ == "__main__":
    main()
