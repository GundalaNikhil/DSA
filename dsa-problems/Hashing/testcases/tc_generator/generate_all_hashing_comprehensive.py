#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Hashing Problems HSH-002 through HSH-016
Generates 30-40 test cases per problem following the Universal Test Case Generation Prompt
"""

import random
import string
import yaml
import os
from typing import List, Tuple, Dict, Any

# Constants for hashing
MOD1 = 10**9 + 7
BASE1 = 313
MOD2 = 10**9 + 9
BASE2 = 317

def set_seed(seed=42):
    """Set random seed for reproducibility"""
    random.seed(seed)

# ============================================================================
# HELPER FUNCTIONS FOR COMPUTING EXPECTED OUTPUTS
# ============================================================================

def compute_prefix_hashes(s: str, base: int, mod: int) -> List[int]:
    """Compute prefix hashes for a string"""
    hashes = []
    current_hash = 0
    for char in s:
        current_hash = (current_hash * base + ord(char)) % mod
        hashes.append(current_hash)
    return hashes

def get_substring_hash(h: List[int], p: List[int], l: int, r: int, mod: int) -> int:
    """Get hash of substring s[l:r+1] using prefix hash array"""
    if l == 0:
        return h[r]
    length = r - l + 1
    return (h[r] - h[l-1] * p[length]) % mod

def compute_powers(length: int, base: int, mod: int) -> List[int]:
    """Compute powers of base mod mod"""
    powers = [1]
    for i in range(length):
        powers.append((powers[-1] * base) % mod)
    return powers

# ============================================================================
# HSH-002: Substring Equality Queries
# ============================================================================

def solve_hsh002(s: str, queries: List[Tuple[int, int, int, int]]) -> List[bool]:
    """
    Check if substrings s[l1:r1+1] == s[l2:r2+1] for each query
    Uses double hashing to minimize collisions
    """
    n = len(s)
    
    # Build prefix hashes for both hash functions
    h1 = [0]
    h2 = [0]
    p1 = compute_powers(n, BASE1, MOD1)
    p2 = compute_powers(n, BASE2, MOD2)
    
    hash1 = 0
    hash2 = 0
    for char in s:
        hash1 = (hash1 * BASE1 + ord(char)) % MOD1
        hash2 = (hash2 * BASE2 + ord(char)) % MOD2
        h1.append(hash1)
        h2.append(hash2)
    
    results = []
    for l1, r1, l2, r2 in queries:
        # Check lengths
        if r1 - l1 != r2 - l2:
            results.append(False)
            continue
        
        # Get hashes with both hash functions
        len_sub = r1 - l1 + 1
        hash1_sub1 = (h1[r1+1] - h1[l1] * p1[len_sub]) % MOD1
        hash1_sub2 = (h1[r2+1] - h1[l2] * p1[len_sub]) % MOD1
        
        hash2_sub1 = (h2[r1+1] - h2[l1] * p2[len_sub]) % MOD2
        hash2_sub2 = (h2[r2+1] - h2[l2] * p2[len_sub]) % MOD2
        
        # Both hashes must match
        results.append(hash1_sub1 == hash1_sub2 and hash2_sub1 == hash2_sub2)
    
    return results

def generate_hsh002_tests():
    """Generate comprehensive test cases for HSH-002"""
    tests = {
        'problem_id': 'HSH-002',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample tests (2-3)
    sample_cases = [
        ("banana", [(1, 3, 3, 5), (0, 1, 2, 3)]),  # "ana" == "ana", "ba" != "na"
        ("abcabc", [(0, 2, 3, 5)]),  # "abc" == "abc"
        ("test", [(0, 0, 1, 1), (0, 1, 2, 3)])  # "t" != "e", "te" == "st"
    ]
    
    for s, queries in sample_cases:
        result = solve_hsh002(s, queries)
        input_str = f"{s}\n{len(queries)}\n"
        for q in queries:
            input_str += f"{q[0]} {q[1]} {q[2]} {q[3]}\n"
        output_str = "\n".join("true" if r else "false" for r in result)
        tests['samples'].append({'input': input_str.strip(), 'output': output_str})
    
    # Public tests (3-5)
    public_cases = [
        ("a", [(0, 0, 0, 0)]),  # Single char equals itself
        ("aa", [(0, 0, 1, 1)]),  # Two same chars
        ("hello", [(0, 1, 3, 4), (1, 1, 2, 2)]),  # "he" != "lo", "e" != "l"
        ("programming", [(0, 6, 3, 9)]),  # "program" != "grammin"
        ("abcd", [(0, 1, 2, 3)])  # "ab" != "cd"
    ]
    
    for s, queries in public_cases:
        result = solve_hsh002(s, queries)
        input_str = f"{s}\n{len(queries)}\n"
        for q in queries:
            input_str += f"{q[0]} {q[1]} {q[2]} {q[3]}\n"
        output_str = "\n".join("true" if r else "false" for r in result)
        tests['public'].append({'input': input_str.strip(), 'output': output_str})
    
    # Hidden tests (20-30)
    # Edge cases (4-6)
    hidden_edge = [
        # All same character
        ("aaaaaaa", [(0, 2, 3, 5), (1, 3, 2, 4)]),
        # Alternating pattern
        ("ababababab", [(0, 3, 2, 5), (0, 1, 4, 5)]),
        # Empty substrings (length 0 edge)
        ("xyz", [(0, 0, 1, 1), (1, 1, 2, 2)]),
        # Full string comparison
        ("complete", [(0, 7, 0, 7)]),
        # Sequential alphabet
        ("abcdefghijk", [(0, 4, 5, 9)])
    ]
    
    # Boundary cases (4-6)
    hidden_boundary = [
        # Single character string
        ("x", [(0, 0, 0, 0)]),
        # Two character string
        ("ab", [(0, 0, 1, 1), (0, 1, 0, 1)]),
        # Maximum reasonable length string (large N)
        ("x" * 1000, [(0, 499, 500, 999), (0, 99, 100, 199)]),
        # Many queries (large Q)
        ("testing", [(i, i, (i+1) % 6, (i+1) % 6) for i in range(50)]),
        # Length 100 with various queries
        ("a" * 50 + "b" * 50, [(0, 49, 0, 49), (50, 99, 50, 99), (0, 49, 50, 99)])
    ]
    
    # Normal cases (4-8)
    hidden_normal = [
        ("algorithm", [(0, 2, 7, 9), (3, 5, 4, 6)]),
        ("datastructure", [(0, 3, 10, 13), (5, 8, 5, 8)]),
        ("hashing", [(0, 3, 4, 7)]),
        ("rollinghash", [(0, 6, 4, 10)]),
        ("substring", [(0, 2, 6, 8)]),
        ("queries", [(0, 1, 5, 6), (2, 3, 4, 5)]),
        ("comparison", [(0, 3, 6, 9), (4, 5, 7, 8)]),
        ("verification", [(0, 5, 6, 11)])
    ]
    
    # Special constraint cases (3-5)
    hidden_special = [
        # Palindrome
        ("racecar", [(0, 2, 4, 6), (1, 5, 1, 5)]),
        # Repeated patterns
        ("abcabcabc", [(0, 2, 3, 5), (3, 5, 6, 8)]),
        # Overlapping queries
        ("overlap", [(0, 3, 2, 5), (1, 4, 3, 6)]),
        # Non-overlapping identical segments
        ("xyzxyz", [(0, 2, 3, 5)])
    ]
    
    # Stress tests (3-4)
    hidden_stress = [
        # Large string with many queries
        ("abcdef" * 100, [(i*6, i*6+5, (i+50)*6, (i+50)*6+5) for i in range(20)]),
        # Random string length 500
        (''.join(random.choice(string.ascii_lowercase) for _ in range(500)), 
         [(random.randint(0, 400), random.randint(0, 400) + random.randint(0, 50),
           random.randint(0, 400), random.randint(0, 400) + random.randint(0, 50)) 
          for _ in range(30)]),
        # All same char, many queries
        ("z" * 800, [(i*10, i*10+50, (i+20)*10, (i+20)*10+50) for i in range(25)])
    ]
    
    # Process all hidden test categories
    for cases in [hidden_edge, hidden_boundary, hidden_normal, hidden_special, hidden_stress]:
        for s, queries in cases:
            # Normalize queries to ensure l <= r
            normalized_queries = []
            for q in queries:
                l1, r1, l2, r2 = q
                l1, r1 = min(l1, r1), max(l1, r1)
                l2, r2 = min(l2, r2), max(l2, r2)
                # Ensure indices are valid
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
            tests['hidden'].append({'input': input_str.strip(), 'output': output_str})
    
    return tests

# ============================================================================
# HSH-003: Longest Common Substring
# ============================================================================

def solve_hsh003(a: str, b: str) -> int:
    """
    Find length of longest common substring using binary search + hashing
    """
    if not a or not b:
        return 0
    
    def has_common_substring(length: int) -> bool:
        """Check if there's a common substring of given length"""
        if length == 0:
            return True
        
        # Hash all substrings of length 'length' in string a
        hashes_a = set()
        n = len(a)
        if length > n:
            return False
        
        # Compute hash for first window
        hash_val = 0
        for i in range(length):
            hash_val = (hash_val * BASE1 + ord(a[i])) % MOD1
        hashes_a.add(hash_val)
        
        # Rolling hash for remaining windows
        pow_val = pow(BASE1, length, MOD1)
        for i in range(length, n):
            hash_val = (hash_val * BASE1 + ord(a[i])) % MOD1
            hash_val = (hash_val - ord(a[i - length]) * pow_val) % MOD1
            hashes_a.add(hash_val)
        
        # Check substrings of b
        m = len(b)
        if length > m:
            return False
        
        hash_val = 0
        for i in range(length):
            hash_val = (hash_val * BASE1 + ord(b[i])) % MOD1
        if hash_val in hashes_a:
            return True
        
        for i in range(length, m):
            hash_val = (hash_val * BASE1 + ord(b[i])) % MOD1
            hash_val = (hash_val - ord(b[i - length]) * pow_val) % MOD1
            if hash_val in hashes_a:
                return True
        
        return False
    
    # Binary search on answer
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
    """Generate comprehensive test cases for HSH-003"""
    tests = {
        'problem_id': 'HSH-003',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample tests
    sample_cases = [
        ("abcde", "cdef"),  # "cde" = 3
        ("abc", "xyz"),  # no common = 0
        ("hello", "world")  # "o" or "l" = 1
    ]
    
    for a, b in sample_cases:
        result = solve_hsh003(a, b)
        input_str = f"{a}\n{b}"
        output_str = str(result)
        tests['samples'].append({'input': input_str, 'output': output_str})
    
    # Public tests
    public_cases = [
        ("a", "a"),  # 1
        ("test", "best"),  # "est" = 3
        ("algorithm", "logarithm"),  # "logarithm" = 8
        ("abcdef", "defghi"),  # "def" = 3
        ("programming", "gaming")  # "aming" = 5
    ]
    
    for a, b in public_cases:
        result = solve_hsh003(a, b)
        input_str = f"{a}\n{b}"
        output_str = str(result)
        tests['public'].append({'input': input_str, 'output': output_str})
    
    # Hidden tests
    hidden_edge = [
        ("aaaa", "aaaa"),  # All same
        ("abababab", "babababa"),  # Alternating
        ("", "test"),  # Empty string
        ("x", "y"),  # Different single chars
        ("abcdefghij", "jihgfedcba")  # Reverse
    ]
    
    hidden_boundary = [
        ("a", "b"),  # Single different chars
        ("ab", "ba"),  # Two chars
        ("a" * 1000, "a" * 1000),  # Max length same
        ("x" * 500 + "y" * 500, "y" * 500 + "x" * 500),  # Large with overlap
        ("test", "t")  # One very short
    ]
    
    hidden_normal = [
        ("hashing", "ashing"),
        ("substring", "string"),
        ("binary", "unary"),
        ("search", "research"),
        ("common", "uncommon"),
        ("prefix", "suffix"),
        ("rolling", "polling"),
        ("longest", "strongest")
    ]
    
    hidden_special = [
        ("racecar", "carrace"),  # Palindrome
        ("abcabc", "cabcab"),  # Repeated pattern
        ("xyz" * 50, "zyx" * 50),  # Pattern no overlap
        ("pattern" * 10, "pattern" * 10)  # Identical repeated
    ]
    
    hidden_stress = [
        ("a" * 1000, "a" * 800),
        (''.join(random.choice("abc") for _ in range(500)), 
         ''.join(random.choice("abc") for _ in range(500))),
        ("test" * 200, "best" * 200)
    ]
    
    for cases in [hidden_edge, hidden_boundary, hidden_normal, hidden_special, hidden_stress]:
        for a, b in cases:
            result = solve_hsh003(a, b)
            input_str = f"{a}\n{b}"
            output_str = str(result)
            tests['hidden'].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# YAML WRITER
# ============================================================================

def write_yaml(filename: str, data: Dict[str, Any]):
    """Write test cases to YAML file with proper formatting"""
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
# MAIN
# ============================================================================

def main():
    set_seed(42)
    
    output_dir = "Hashing/testcases"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate HSH-002
    print("Generating HSH-002: Substring Equality Queries...")
    tests_002 = generate_hsh002_tests()
    write_yaml(f"{output_dir}/HSH-002-substring-equality-queries.yaml", tests_002)
    print(f"  Generated {len(tests_002['samples'])} samples, {len(tests_002['public'])} public, {len(tests_002['hidden'])} hidden")
    
    # Generate HSH-003
    print("Generating HSH-003: Longest Common Substring...")
    tests_003 = generate_hsh003_tests()
    write_yaml(f"{output_dir}/HSH-003-lcs-hash-two-strings.yaml", tests_003)
    print(f"  Generated {len(tests_003['samples'])} samples, {len(tests_003['public'])} public, {len(tests_003['hidden'])} hidden")
    
    print("\nTest case generation complete!")
    print("Note: HSH-004 through HSH-016 require additional implementation.")
    print("This script provides the framework for comprehensive test generation.")

if __name__ == "__main__":
    main()
