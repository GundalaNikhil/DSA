#!/usr/bin/env python3
"""
COMPREHENSIVE Test Case Generator for ALL Hashing Problems (HSH-002 through HSH-016)
Generates 30-40 test cases per problem following Universal Test Case Generation Prompt

Author: AI Assistant
Date: 2024
"""

import random
import string
import os
import sys
from typing import List, Tuple, Dict, Any, Set
from collections import defaultdict

# Hashing constants
MOD1 = 10**9 + 7
BASE1 = 313
MOD2 = 10**9 + 9
BASE2 = 317

def set_seed(seed=42):
    random.seed(seed)

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def compute_hash_single(s: str, base: int, mod: int) -> int:
    """Compute polynomial hash of string"""
    h = 0
    for c in s:
        h = (h * base + ord(c)) % mod
    return h

def compute_prefix_hashes_double(s: str) -> Tuple[List[int], List[int], List[int], List[int]]:
    """Compute prefix hashes and powers for double hashing"""
    n = len(s)
    h1, h2 = [0], [0]
    p1, p2 = [1], [1]
    
    for c in s:
        h1.append((h1[-1] * BASE1 + ord(c)) % MOD1)
        h2.append((h2[-1] * BASE2 + ord(c)) % MOD2)
        p1.append((p1[-1] * BASE1) % MOD1)
        p2.append((p2[-1] * BASE2) % MOD2)
    
    return h1, p1, h2, p2

def get_substring_hash_double(h1, p1, h2, p2, l, r):
    """Get double hash of substring s[l:r+1]"""
    length = r - l + 1
    hash1 = (h1[r+1] - h1[l] * p1[length]) % MOD1
    hash2 = (h2[r+1] - h2[l] * p2[length]) % MOD2
    return (hash1, hash2)

# ============================================================================
# HSH-002: Substring Equality Queries
# Input: string s, Q queries (l1, r1, l2, r2)
# Output: Q lines of "true" or "false"
# ============================================================================

def solve_hsh002(s: str, queries: List[Tuple[int, int, int, int]]) -> List[bool]:
    if not s:
        return [False] * len(queries)
    
    h1, p1, h2, p2 = compute_prefix_hashes_double(s)
    results = []
    
    for l1, r1, l2, r2 in queries:
        if r1 - l1 != r2 - l2:
            results.append(False)
            continue
        
        hash1_sub1, hash2_sub1 = get_substring_hash_double(h1, p1, h2, p2, l1, r1)
        hash1_sub2, hash2_sub2 = get_substring_hash_double(h1, p1, h2, p2, l2, r2)
        
        results.append(hash1_sub1 == hash1_sub2 and hash2_sub1 == hash2_sub2)
    
    return results

def generate_hsh002_tests():
    tests = {'problem_id': 'HSH-002', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("banana", [(1, 3, 3, 5), (0, 1, 2, 3)]),
        ("abcabc", [(0, 2, 3, 5)]),
        ("test", [(0, 0, 1, 1)])
    ]
    
    # Public (5)
    public = [
        ("a", [(0, 0, 0, 0)]),
        ("aa", [(0, 0, 1, 1)]),
        ("hello", [(0, 1, 3, 4)]),
        ("programming", [(0, 6, 3, 9)]),
        ("abcd", [(0, 1, 2, 3)])
    ]
    
    # Hidden (27): Edge(5) + Boundary(5) + Normal(8) + Special(5) + Stress(4)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("aaaaaaa", [(0, 2, 3, 5), (1, 3, 2, 4)]),
        ("ababababab", [(0, 3, 2, 5), (0, 1, 4, 5)]),
        ("x", [(0, 0, 0, 0)]),
        ("complete", [(0, 7, 0, 7)]),
        ("abcdefghijk", [(0, 4, 5, 9)])
    ]
    
    # Boundary (5)
    hidden += [
        ("ab", [(0, 0, 1, 1), (0, 1, 0, 1)]),
        ("x" * 1000, [(0, 499, 500, 999), (0, 99, 100, 199)]),
        ("testing", [(i % 7, i % 7, (i+1) % 7, (i+1) % 7) for i in range(50)]),
        ("a" * 50 + "b" * 50, [(0, 49, 0, 49), (50, 99, 50, 99), (0, 49, 50, 99)]),
        ("z", [(0, 0, 0, 0)])
    ]
    
    # Normal (8)
    hidden += [
        ("algorithm", [(0, 2, 7, 9), (3, 5, 4, 6)]),
        ("datastructure", [(0, 3, 10, 13), (5, 8, 5, 8)]),
        ("hashing", [(0, 3, 4, 7)]),
        ("rollinghash", [(0, 6, 4, 10)]),
        ("substring", [(0, 2, 6, 8)]),
        ("queries", [(0, 1, 5, 6), (2, 3, 4, 5)]),
        ("comparison", [(0, 3, 6, 9)]),
        ("verification", [(0, 5, 6, 11)])
    ]
    
    # Special (5)
    hidden += [
        ("racecar", [(0, 2, 4, 6), (1, 5, 1, 5)]),
        ("abcabcabc", [(0, 2, 3, 5), (3, 5, 6, 8)]),
        ("overlap", [(0, 3, 2, 5), (1, 4, 3, 6)]),
        ("xyzxyz", [(0, 2, 3, 5)]),
        ("pattern" * 10, [(0, 6, 7, 13), (14, 20, 21, 27)])
    ]
    
    # Stress (4)
    set_seed(100)
    hidden += [
        ("abcdef" * 100, [(i*6, i*6+5, (i+50)*6, (i+50)*6+5) for i in range(20)]),
        (''.join(random.choice(string.ascii_lowercase) for _ in range(500)), 
         [(random.randint(0, 400), min(random.randint(0, 450), 499),
           random.randint(0, 400), min(random.randint(0, 450), 499)) 
          for _ in range(30)]),
        ("z" * 800, [(i*10, min(i*10+50, 799), (i+20)*10, min((i+20)*10+50, 799)) for i in range(25)]),
        ("test" * 250, [(i*20, i*20+19, (i+50)*20, (i+50)*20+19) for i in range(30)])
    ]
    
    # Process all test cases
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s, queries in category_list:
            # Normalize queries
            normalized_queries = []
            for q in queries:
                l1, r1, l2, r2 = q
                l1 = max(0, min(l1, len(s) - 1))
                r1 = max(l1, min(r1, len(s) - 1))
                l2 = max(0, min(l2, len(s) - 1))
                r2 = max(l2, min(r2, len(s) - 1))
                normalized_queries.append((l1, r1, l2, r2))
            
            result = solve_hsh002(s, normalized_queries)
            input_str = f"{s}\n{len(normalized_queries)}\n"
            for q in normalized_queries:
                input_str += f"{q[0]} {q[1]} {q[2]} {q[3]}\n"
            output_str = "\n".join("true" if r else "false" for r in result)
            tests[category_name].append({'input': input_str.strip(), 'output': output_str})
    
    return tests

# ============================================================================
# HSH-003: Longest Common Substring
# Input: Two strings a and b
# Output: Single integer (length of LCS)
# ============================================================================

def solve_hsh003(a: str, b: str) -> int:
    if not a or not b:
        return 0
    
    def has_common_substring(length: int) -> bool:
        if length == 0:
            return True
        if length > len(a) or length > len(b):
            return False
        
        # Hash all substrings of length in a
        hashes_a = set()
        hash_val = 0
        pow_val = pow(BASE1, length, MOD1)
        
        for i in range(len(a)):
            if i < length:
                hash_val = (hash_val * BASE1 + ord(a[i])) % MOD1
            else:
                hash_val = (hash_val * BASE1 + ord(a[i])) % MOD1
                hash_val = (hash_val - ord(a[i - length]) * pow_val) % MOD1
            
            if i >= length - 1:
                hashes_a.add(hash_val)
        
        # Check substrings in b
        hash_val = 0
        for i in range(len(b)):
            if i < length:
                hash_val = (hash_val * BASE1 + ord(b[i])) % MOD1
            else:
                hash_val = (hash_val * BASE1 + ord(b[i])) % MOD1
                hash_val = (hash_val - ord(b[i - length]) * pow_val) % MOD1
            
            if i >= length - 1 and hash_val in hashes_a:
                return True
        
        return False
    
    # Binary search
    left, right = 0, min(len(a), len(b))
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if has_common_substring(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def generate_hsh003_tests():
    tests = {'problem_id': 'HSH-003', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("abcde", "cdef"),
        ("abc", "xyz"),
        ("hello", "world")
    ]
    
    # Public (5)
    public = [
        ("a", "a"),
        ("test", "best"),
        ("algorithm", "logarithm"),
        ("abcdef", "defghi"),
        ("programming", "gaming")
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("aaaa", "aaaa"),
        ("abababab", "babababa"),
        ("x", "y"),
        ("abcdefghij", "jihgfedcba"),
        ("single", "double")
    ]
    
    # Boundary (5)
    hidden += [
        ("a", "b"),
        ("ab", "ba"),
        ("a" * 1000, "a" * 1000),
        ("x" * 500 + "y" * 500, "y" * 500 + "x" * 500),
        ("test", "t")
    ]
    
    # Normal (8)
    hidden += [
        ("hashing", "ashing"),
        ("substring", "string"),
        ("binary", "unary"),
        ("search", "research"),
        ("common", "uncommon"),
        ("prefix", "suffix"),
        ("rolling", "polling"),
        ("longest", "strongest")
    ]
    
    # Special (5)
    hidden += [
        ("racecar", "carrace"),
        ("abcabc", "cabcab"),
        ("xyz" * 50, "zyx" * 50),
        ("pattern" * 10, "pattern" * 10),
        ("abcdefg", "gfedcba")
    ]
    
    # Stress (4)
    set_seed(101)
    hidden += [
        ("a" * 1000, "a" * 800),
        (''.join(random.choice("abc") for _ in range(500)), 
         ''.join(random.choice("abc") for _ in range(500))),
        ("test" * 200, "best" * 200),
        ("algorithm" * 50, "logarithm" * 50)
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for a, b in category_list:
            result = solve_hsh003(a, b)
            input_str = f"{a}\n{b}"
            output_str = str(result)
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-004: Palindrome Substring Queries  
# Input: string s, Q queries (l, r)
# Output: Q lines of "true" or "false" (whether s[l:r+1] is palindrome)
# ============================================================================

def solve_hsh004(s: str, queries: List[Tuple[int, int]]) -> List[bool]:
    """Check if each substring is a palindrome using hashing"""
    n = len(s)
    h1_fwd, p1_fwd, h2_fwd, p2_fwd = compute_prefix_hashes_double(s)
    
    # Reverse string for backward hash
    s_rev = s[::-1]
    h1_bwd, p1_bwd, h2_bwd, p2_bwd = compute_prefix_hashes_double(s_rev)
    
    results = []
    for l, r in queries:
        # Forward hash of s[l:r+1]
        hash1_fwd, hash2_fwd = get_substring_hash_double(h1_fwd, p1_fwd, h2_fwd, p2_fwd, l, r)
        
        # Backward hash (reversed indices)
        l_rev = n - 1 - r
        r_rev = n - 1 - l
        hash1_bwd, hash2_bwd = get_substring_hash_double(h1_bwd, p1_bwd, h2_bwd, p2_bwd, l_rev, r_rev)
        
        results.append(hash1_fwd == hash1_bwd and hash2_fwd == hash2_bwd)
    
    return results

def generate_hsh004_tests():
    tests = {'problem_id': 'HSH-004', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("racecar", [(0, 6), (0, 3)]),
        ("abcba", [(0, 4), (1, 3)]),
        ("test", [(0, 3)])
    ]
    
    # Public (5)
    public = [
        ("a", [(0, 0)]),
        ("aa", [(0, 1)]),
        ("aba", [(0, 2), (1, 1)]),
        ("abba", [(0, 3), (1, 2)]),
        ("noon", [(0, 3), (1, 2)])
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("x", [(0, 0)]),
        ("aaaaaa", [(0, 5), (1, 4), (2, 3)]),
        ("abcdefg", [(0, 0), (3, 3)]),
        ("abcdcba", [(0, 6)]),
        ("madamimadam", [(0, 10), (5, 6)])
    ]
    
    # Boundary (5)
    hidden += [
        ("ab", [(0, 0), (1, 1), (0, 1)]),
        ("a" * 1000, [(0, 999), (100, 200)]),
        ("racecar" * 100, [(i*7, i*7+6) for i in range(20)]),
        ("test", [(i, i) for i in range(4)]),
        ("abcba" * 50, [(0, 4), (250, 254)])
    ]
    
    # Normal (8)
    hidden += [
        ("level", [(0, 4)]),
        ("civic", [(0, 4)]),
        ("radar", [(0, 4)]),
        ("deified", [(0, 6)]),
        ("rotator", [(0, 6)]),
        ("malayalam", [(0, 8)]),
        ("noon", [(0, 3)]),
        ("stats", [(0, 4)])
    ]
    
    # Special (5)
    hidden += [
        ("aabbaa", [(0, 5), (1, 4)]),
        ("abcdcba", [(0, 6), (1, 5), (2, 4)]),
        ("xyzyx", [(0, 4)]),
        ("a" + "b" * 50 + "a", [(0, 51)]),
        ("racecar" + "civic", [(0, 6), (7, 11)])
    ]
    
    # Stress (4)
    set_seed(102)
    palindrome1000 = "a" * 500 + "b" * 500
    hidden += [
        (palindrome1000, [(i*100, i*100+99) for i in range(9)]),
        ("racecar" * 150, [(i*35, i*35+6) for i in range(30)]),
        (''.join(random.choice("ab") for _ in range(500)), [(i*50, i*50+49) for i in range(10)]),
        ("aba" * 300, [(i*15, i*15+2) for i in range(50)])
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s, queries in category_list:
            normalized_queries = [(max(0, min(l, len(s)-1)), max(0, min(r, len(s)-1))) for l, r in queries]
            result = solve_hsh004(s, normalized_queries)
            input_str = f"{s}\n{len(normalized_queries)}\n"
            for l, r in normalized_queries:
                input_str += f"{l} {r}\n"
            output_str = "\n".join("true" if r else "false" for r in result)
            tests[category_name].append({'input': input_str.strip(), 'output': output_str})
    
    return tests

# ============================================================================
# HSH-005: Count Distinct Substrings
# Input: string s
# Output: Single integer (count of distinct substrings including empty string)
# ============================================================================

def solve_hsh005(s: str) -> int:
    """Count distinct substrings using hashing"""
    n = len(s)
    hashes = set()
    hashes.add((0, 0))  # Empty string
    
    # For each starting position
    for i in range(n):
        hash1 = 0
        hash2 = 0
        # For each ending position
        for j in range(i, n):
            hash1 = (hash1 * BASE1 + ord(s[j])) % MOD1
            hash2 = (hash2 * BASE2 + ord(s[j])) % MOD2
            hashes.add((hash1, hash2))
    
    return len(hashes)

def generate_hsh005_tests():
    tests = {'problem_id': 'HSH-005', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = ["abc", "aaa", "ab"]
    
    # Public (5)
    public = ["a", "aa", "abcd", "test", "hello"]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += ["x", "aaaa", "abcdefg", "zzz", "zzzzzz"]
    
    # Boundary (5)
    hidden += ["ab", "a" * 100, "abcdefghij", "test" * 25, "z"]
    
    # Normal (8)
    hidden += ["algorithm", "hashing", "substring", "distinct", "count", "rolling", "polynomial", "string"]
    
    # Special (5)
    hidden += ["abcabc", "ababab", "aabbcc", "racecar", "pattern" * 5]
    
    # Stress (4)
    set_seed(103)
    hidden += [
        "a" * 200,
        ''.join(random.choice("abc") for _ in range(200)),
        "test" * 50,
        "abcdefghij" * 20
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s in category_list:
            result = solve_hsh005(s)
            input_str = s
            output_str = str(result)
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-006: Minimal Rotation
# Input: string s
# Output: Starting index of lexicographically smallest rotation
# ============================================================================

def solve_hsh006(s: str) -> str:
    """Find minimal rotation - return the rotated string itself"""
    if not s:
        return s
    
    n = len(s)
    
    # Find lexicographically smallest rotation
    min_rotation = s
    for i in range(1, n):
        rotation = s[i:] + s[:i]
        if rotation < min_rotation:
            min_rotation = rotation
    
    return min_rotation

def generate_hsh006_tests():
    tests = {'problem_id': 'HSH-006', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = ["bcaab", "abc", "aaa"]
    
    # Public (5)
    public = ["a", "ba", "dcba", "test", "hello"]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += ["x", "aaaa", "zzzzz", "abcdefg", "zyxwvu"]
    
    # Boundary (5)
    hidden += ["ab", "ba", "a" * 100, "abcabc", "z"]
    
    # Normal (8)
    hidden += ["rotation", "minimal", "lexicographic", "string", "hash", "algorithm", "circular", "pattern"]
    
    # Special (5)
    hidden += ["abcabc", "aabaaab", "ababab", "racecar", "banana"]
    
    # Stress (4)
    set_seed(104)
    hidden += [
        "a" * 300,
        ''.join(random.choice("abc") for _ in range(200)),
        "test" * 60,
        "abcdefghij" * 25
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s in category_list:
            result = solve_hsh006(s)
            input_str = s
            output_str = result
            tests[category_name].append({'input': input_str, 'output': output_str})
    
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
        ('002', 'substring-equality-queries', generate_hsh002_tests),
        ('003', 'lcs-hash-two-strings', generate_hsh003_tests),
        ('004', 'palindrome-substring-queries', generate_hsh004_tests),
        ('005', 'count-distinct-substrings-hash', generate_hsh005_tests),
        ('006', 'minimal-rotation-hash', generate_hsh006_tests),
    ]
    
    print("=" * 70)
    print("COMPREHENSIVE HASHING TEST CASE GENERATOR")
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
    print("GENERATION COMPLETE!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Test HSH-002 through HSH-006 with ./test_python.sh")
    print("2. Implement generators for HSH-007 through HSH-016")
    print("3. Verify 100% pass rate for all problems")

if __name__ == "__main__":
    main()
