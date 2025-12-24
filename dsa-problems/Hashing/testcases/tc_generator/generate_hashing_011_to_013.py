#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Hashing Problems HSH-011 through HSH-016
Part 3: Final set of hashing problems
"""

import random
import string
import os
from typing import List, Tuple, Dict, Any, Set
from collections import defaultdict, Counter
from itertools import product

# Hashing constants
MOD1 = 10**9 + 7
BASE1 = 313
MOD2 = 10**9 + 9
BASE2 = 317

def set_seed(seed=42):
    random.seed(seed)

# ============================================================================
# HSH-011: Rolling Hash Collision
# Input: Base B, Modulus M, Length L
# Output: Two distinct strings of length L with same hash
# ============================================================================

def solve_hsh011(B: int, M: int, L: int) -> Tuple[str, str]:
    """
    Find two distinct strings that hash to the same value
    Strategy: Use iterative generation with guaranteed collision finding
    """
    def compute_hash(s: str) -> int:
        h = 0
        for char in s:
            h = (h * B + ord(char)) % M
        return h
    
    seen = {}  # hash -> string
    
    # For small L (1-4), generate systematically
    if L <= 4:
        from itertools import product
        max_attempts = min(26**L, M * 3, 100000)
        count = 0
        
        for combo in product('abcdefghijklmnopqrstuvwxyz', repeat=L):
            s = ''.join(combo)
            h = compute_hash(s)
            if h in seen and seen[h] != s:
                return (seen[h], s)
            seen[h] = s
            
            count += 1
            if count >= max_attempts:
                break
    
    # For L >= 5, use random generation with birthday paradox
    # Expected collisions after sqrt(M) attempts
    import random
    random.seed(42 + B + M + L)  # Deterministic but varied
    
    max_attempts = min(int((M ** 0.5) * 5), 500000)  # 5 * sqrt(M) attempts
    
    for _ in range(max_attempts):
        s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(L))
        h = compute_hash(s)
        if h in seen and seen[h] != s:
            return (seen[h], s)
        seen[h] = s
    
    # If still no collision found, do a more targeted search
    # This handles edge cases where M is very large
    # Try variations on 'a' repeated
    base_str = 'a' * L
    for offset in range(1, min(26 ** min(L, 2), 1000)):
        # Generate string by treating offset as base-26 number
        s = list(base_str)
        temp_offset = offset
        for i in range(L - 1, -1, -1):
            s[i] = chr(ord('a') + temp_offset % 26)
            temp_offset //= 26
            if temp_offset == 0:
                break
        
        s_str = ''.join(s)
        h = compute_hash(s_str)
        if h in seen and seen[h] != s_str:
            return (seen[h], s_str)
        seen[h] = s_str
    
    # Ultimate fallback - should never reach here with valid parameters
    return ("a" * L, "b" * L)

def generate_hsh011_tests():
    tests = {'problem_id': 'HSH-011', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3) - Small examples  
    samples = [
        (31, 100, 2),
        (37, 1000, 3),
        (31, 10000, 3)
    ]
    
    # Public (5)
    public = [
        (31, 100, 2),
        (37, 500, 2),
        (31, 1000, 3),
        (37, 5000, 3),
        (31, 10000, 4)
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5) - Small parameters
    hidden += [
        (31, 10, 1),
        (2, 100, 2),
        (31, 50, 2),
        (37, 200, 2),
        (31, 1000, 3)
    ]
    
    # Boundary (5)
    hidden += [
        (31, 100, 3),
        (37, 500, 3),
        (31, 2000, 3),
        (37, 5000, 4),
        (31, 10000, 4)
    ]
    
    # Normal (8)
    hidden += [
        (31, 1000, 3),
        (37, 2000, 3),
        (313, 5000, 3),
        (31, 10000, 4),
        (37, 15000, 4),
        (31, 20000, 4),
        (37, 50000, 4),
        (31, 100000, 5)
    ]
    
    # Special (5)
    hidden += [
        (31, 10007, 4),
        (37, 100003, 4),
        (313, 50000, 4),
        (31, 200000, 5),
        (37, 500000, 5)
    ]
    
    # Stress (4) - Larger but still manageable
    hidden += [
        (31, 1000000, 5),
        (37, 2000000, 5),
        (313, 5000000, 5),
        (31, 10000000, 5)
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for B, M, L in category_list:
            s1, s2 = solve_hsh011(B, M, L)
            input_str = f"{B} {M} {L}"
            output_str = f"{s1}\n{s2}"
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-012: Subarray Hash Equality
# Input: Array of integers, Q queries with (l1, r1, l2, r2)
# Output: For each query, "true" or "false"
# ============================================================================

def solve_hsh012(arr: List[int], queries: List[Tuple[int, int, int, int]]) -> List[bool]:
    """Check if subarrays arr[l1:r1+1] == arr[l2:r2+1]"""
    n = len(arr)
    
    # Build prefix hashes
    h = [0]
    p = [1]
    
    hash_val = 0
    power_val = 1
    for num in arr:
        hash_val = (hash_val * BASE1 + num) % MOD1
        h.append(hash_val)
        power_val = (power_val * BASE1) % MOD1
        p.append(power_val)
    
    results = []
    for l1, r1, l2, r2 in queries:
        # Check lengths
        if r1 - l1 != r2 - l2:
            results.append(False)
            continue
        
        # Get hashes
        len_sub = r1 - l1 + 1
        hash1 = (h[r1+1] - h[l1] * p[len_sub]) % MOD1
        hash2 = (h[r2+1] - h[l2] * p[len_sub]) % MOD1
        
        results.append(hash1 == hash2)
    
    return results

def generate_hsh012_tests():
    tests = {'problem_id': 'HSH-012', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ([1, 2, 3, 1, 2, 3], [(0, 2, 3, 5)]),
        ([5, 5, 5, 5], [(0, 1, 2, 3)]),
        ([1, 2, 3, 4], [(0, 1, 2, 3)])
    ]
    
    # Public (5)
    public = [
        ([1], [(0, 0, 0, 0)]),
        ([1, 2], [(0, 0, 1, 1)]),
        ([1, 2, 3, 1, 2, 3], [(0, 2, 3, 5), (0, 1, 1, 2)]),
        ([5, 5, 5, 5, 5], [(0, 2, 2, 4)]),
        ([1, 2, 3, 4, 5], [(0, 1, 3, 4)])
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ([1], [(0, 0, 0, 0)]),
        ([1, 1, 1, 1], [(0, 3, 0, 3), (0, 1, 2, 3)]),
        ([1, 2, 3, 4, 5], [(0, 4, 0, 4)]),
        (list(range(1, 11)), [(0, 4, 5, 9)]),
        ([100] * 10, [(0, 4, 5, 9)])
    ]
    
    # Boundary (5)
    hidden += [
        ([1, 2], [(0, 0, 1, 1), (0, 1, 0, 1)]),
        ([1] * 100, [(0, 49, 50, 99)]),
        (list(range(50)), [(0, 24, 25, 49)]),
        ([1, 2, 3] * 30, [(0, 2, 3, 5), (6, 8, 9, 11)]),
        ([i % 10 for i in range(100)], [(0, 9, 10, 19), (20, 29, 30, 39)])
    ]
    
    # Normal (8)
    hidden += [
        ([1, 2, 3, 4, 5, 6, 7, 8], [(0, 3, 4, 7)]),
        ([10, 20, 30, 10, 20, 30], [(0, 2, 3, 5)]),
        ([5, 4, 3, 2, 1, 5, 4, 3, 2, 1], [(0, 4, 5, 9)]),
        ([1, 1, 2, 2, 3, 3], [(0, 1, 2, 3), (2, 3, 4, 5)]),
        ([100, 200, 300], [(0, 0, 1, 1), (1, 1, 2, 2)]),
        (list(range(1, 21)), [(0, 9, 10, 19)]),
        ([7, 8, 9, 7, 8, 9, 7, 8, 9], [(0, 2, 3, 5), (3, 5, 6, 8)]),
        ([11, 22, 33, 44, 55], [(0, 2, 2, 4)])
    ]
    
    # Special (5)
    hidden += [
        ([1, 2, 1, 2, 1, 2], [(0, 1, 2, 3), (2, 3, 4, 5)]),
        ([i * i for i in range(1, 11)], [(0, 4, 5, 9)]),
        ([1, 2, 3] * 20, [(0, 2, 3, 5), (6, 8, 9, 11), (30, 32, 33, 35)]),
        (list(range(25)) + list(range(25)), [(0, 24, 25, 49)]),
        ([10, 20, 30, 40, 50] * 5, [(0, 4, 5, 9), (10, 14, 15, 19)])
    ]
    
    # Stress (4)
    set_seed(112)
    hidden += [
        ([random.randint(1, 100) for _ in range(200)], 
         [(i*20, i*20+19, (i+5)*20, (i+5)*20+19) for i in range(3)]),
        ([1] * 300, [(0, 149, 150, 299)]),
        (list(range(1, 251)), [(0, 124, 125, 249)]),
        ([i % 50 for i in range(400)], [(0, 49, 50, 99), (100, 149, 150, 199)])
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for arr, queries in category_list:
            result = solve_hsh012(arr, queries)
            input_str = f"{len(arr)}\n"
            input_str += " ".join(map(str, arr)) + "\n"
            input_str += f"{len(queries)}\n"
            for q in queries:
                input_str += f"{q[0]} {q[1]} {q[2]} {q[3]}\n"
            output_str = "\n".join("true" if r else "false" for r in result)
            tests[category_name].append({'input': input_str.strip(), 'output': output_str})
    
    return tests

# ============================================================================
# HSH-013: 2D Rolling Hash  
# Input: Matrix A (N x M), Pattern B (P x Q)
# Output: "true" or "false" (whether B exists in A)
# ============================================================================

def solve_hsh013(A: List[List[int]], B: List[List[int]]) -> bool:
    """Check if pattern B exists as submatrix in A"""
    if not A or not B or not A[0] or not B[0]:
        return False
    
    N, M = len(A), len(A[0])
    P, Q = len(B), len(B[0])
    
    if P > N or Q > M:
        return False
    
    # Compute hash for pattern B
    hash_B = 0
    for i in range(P):
        for j in range(Q):
            hash_B = (hash_B * BASE1 + B[i][j]) % MOD1
    
    # Check all possible positions in A
    for i in range(N - P + 1):
        for j in range(M - Q + 1):
            # Compute hash for submatrix A[i:i+P][j:j+Q]
            hash_A = 0
            for di in range(P):
                for dj in range(Q):
                    hash_A = (hash_A * BASE1 + A[i+di][j+dj]) % MOD1
            
            if hash_A == hash_B:
                # Verify actual match
                match = True
                for di in range(P):
                    for dj in range(Q):
                        if A[i+di][j+dj] != B[di][dj]:
                            match = False
                            break
                    if not match:
                        break
                if match:
                    return True
    
    return False

def generate_hsh013_tests():
    tests = {'problem_id': 'HSH-013', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[5, 6], [8, 9]]),
        ([[1, 1, 1], [1, 1, 1]], [[1, 1]]),
        ([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    ]
    
    # Public (5)
    public = [
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[1]]),
        ([[1, 2, 3], [4, 5, 6]], [[2, 3], [5, 6]]),
        ([[5, 5, 5], [5, 5, 5], [5, 5, 5]], [[5, 5], [5, 5]]),
        ([[1, 2, 3, 4], [5, 6, 7, 8]], [[3, 4], [7, 8]])
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        ([[1, 1, 1]], [[1]]),
        ([[1], [2], [3]], [[2]]),
        ([[i for i in range(5)]], [[2, 3]])
    ]
    
    # Boundary (5)
    hidden += [
        ([[1, 2]], [[1, 2]]),
        ([[1] * 10 for _ in range(10)], [[1] * 5 for _ in range(5)]),
        ([[i % 10 for i in range(20)]], [[5, 6, 7]]),
        ([[1, 2, 3]] * 5, [[1, 2], [1, 2]]),
        ([[i + j for j in range(10)] for i in range(10)], [[5, 6], [6, 7]])
    ]
    
    # Normal (8)
    set_seed(113)
    hidden += [
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[6, 7], [10, 11]]),
        ([[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4]], [[1, 2], [1, 2]]),
        ([[i for i in range(1, 6)] for _ in range(4)], [[3, 4, 5], [3, 4, 5]]),
        ([[5, 5, 5, 5], [5, 5, 5, 5]], [[5]]),
        ([[10 * i + j for j in range(5)] for i in range(5)], [[11, 12], [21, 22]]),
        ([[random.randint(1, 10) for _ in range(6)] for _ in range(6)], [[1, 2], [3, 4]]),
        ([[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2]], [[1, 2], [3, 4]]),
        ([[i * j for j in range(5)] for i in range(5)], [[2, 4], [3, 6]])
    ]
    
    # Special (5)
    hidden += [
        ([[1, 2, 3] * 3 for _ in range(3)], [[1, 2, 3], [1, 2, 3]]),
        ([[i + j for j in range(8)] for i in range(8)], [[5, 6, 7], [6, 7, 8], [7, 8, 9]]),
        ([[1 if i == j else 0 for j in range(5)] for i in range(5)], [[1, 0], [0, 1]]),
        ([[5] * 10 for _ in range(10)], [[5] * 3 for _ in range(3)]),
        ([[i % 5 for i in range(10)] for _ in range(10)], [[0, 1], [0, 1]])
    ]
    
    # Stress (4)
    set_seed(113)
    large_matrix = [[random.randint(1, 5) for _ in range(20)] for _ in range(20)]
    pattern1 = [[large_matrix[5][5], large_matrix[5][6]], [large_matrix[6][5], large_matrix[6][6]]]
    hidden += [
        (large_matrix, pattern1),
        ([[1] * 30 for _ in range(30)], [[1] * 10 for _ in range(10)]),
        ([[i % 10 for i in range(25)] for _ in range(25)], [[5, 6, 7], [5, 6, 7]]),
        ([[i + j for j in range(20)] for i in range(20)], [[10, 11], [11, 12]])
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for A, B in category_list:
            result = solve_hsh013(A, B)
            N, M = len(A), len(A[0])
            P, Q = len(B), len(B[0])
            input_str = f"{N} {M}\n"
            for row in A:
                input_str += " ".join(map(str, row)) + "\n"
            input_str += f"{P} {Q}\n"
            for row in B:
                input_str += " ".join(map(str, row)) + "\n"
            output_str = "true" if result else "false"
            tests[category_name].append({'input': input_str.strip(), 'output': output_str})
    
    return tests

# ============================================================================
# YAML WRITER
# ============================================================================

def write_yaml(filename: str, data: Dict[str, Any]):
    """Write test cases to YAML with proper |- format"""
    with open(filename, 'w') as f:
        f.write(f"problem_id: {data['problem_id']}\n")
        
        for category in ['samples', 'public', 'hidden']:
            f.write(f"{category}:\n")
            for test in data[category]:
                f.write("  - input: |-\n")
                for line in test['input'].split('\n'):
                    f.write(f"      {line}\n")
                f.write("    output: |-\n")
                for line in test['output'].split('\n'):
                    f.write(f"      {line}\n")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    set_seed(42)
    
    output_dir = "Hashing/testcases"
    os.makedirs(output_dir, exist_ok=True)
    
    generators = [
        ('011', 'rolling-hash-collision', generate_hsh011_tests),
        ('012', 'subarray-hash-equality', generate_hsh012_tests),
        ('013', '2d-rolling-hash', generate_hsh013_tests),
    ]
    
    print("=" * 70)
    print("HASHING TEST GENERATOR - PART 3 (HSH-011 to HSH-013)")
    print("=" * 70)
    
    for num, slug, generator_func in generators:
        print(f"\n[HSH-{num}] Generating: {slug}...")
        try:
            tests = generator_func()
            filename = f"{output_dir}/HSH-{num}-{slug}.yaml"
            write_yaml(filename, tests)
            
            total = len(tests['samples']) + len(tests['public']) + len(tests['hidden'])
            print(f"  ✓ Generated {total} tests: {len(tests['samples'])} samples, " +
                  f"{len(tests['public'])} public, {len(tests['hidden'])} hidden")
            print(f"  ✓ Written to: {filename}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 70)
    print("PART 3 COMPLETE!")
    print("=" * 70)
    print("\nGenerated HSH-011 through HSH-013")
    print("Next: Create generator for HSH-014 through HSH-016")

if __name__ == "__main__":
    main()
