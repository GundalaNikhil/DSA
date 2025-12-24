#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Hashing Problems HSH-014 through HSH-016
Part 4: Final problems
"""

import random
import string
import os
from typing import List, Dict, Any
from collections import Counter, defaultdict

# Hashing constants
MOD1 = 10**9 + 7
BASE1 = 313

def set_seed(seed=42):
    random.seed(seed)

# ============================================================================
# HSH-014: Longest Palindrome Prefix After Append
# Input: String s, character c
# Output: Length of longest palindromic prefix of s+c
# ============================================================================

def solve_hsh014(s: str, c: str) -> int:
    """Find longest palindromic prefix of s+c"""
    T = s + c
    n = len(T)
    
    # Check each prefix length
    for length in range(n, 0, -1):
        prefix = T[:length]
        if prefix == prefix[::-1]:
            return length
    
    return 0

def generate_hsh014_tests():
    tests = {'problem_id': 'HSH-014', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("abc", 'b'),
        ("racecar", 'x'),
        ("a", 'a')
    ]
    
    # Public (5)
    public = [
        ("", 'a'),
        ("a", 'b'),
        ("ab", 'a'),
        ("abcd", 'd'),
        ("racecar", 'r')
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("", 'z'),
        ("x", 'x'),
        ("a", 'a'),
        ("ab", 'b'),
        ("abc", 'c')
    ]
    
    # Boundary (5)
    hidden += [
        ("a" * 50, 'a'),
        ("ab", 'a'),
        ("abc" * 20, 'd'),
        ("z" * 100, 'z'),
        ("test", 't')
    ]
    
    # Normal (8)
    hidden += [
        ("hello", 'o'),
        ("world", 'd'),
        ("palindrome", 'e'),
        ("algorithm", 'm'),
        ("hashing", 'g'),
        ("rolling", 'g'),
        ("prefix", 'x'),
        ("suffix", 'x')
    ]
    
    # Special (5)
    hidden += [
        ("racecar", 'r'),
        ("noon", 'n'),
        ("level", 'l'),
        ("radar", 'r'),
        ("abcba", 'a')
    ]
    
    # Stress (4)
    set_seed(114)
    hidden += [
        ("a" * 200, 'a'),
        (''.join(random.choice(string.ascii_lowercase) for _ in range(150)), 'x'),
        ("abc" * 100, 'd'),
        ("test" * 75, 't')
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s, c in category_list:
            result = solve_hsh014(s, c)
            input_str = f"{s}\n{c}"
            output_str = str(result)
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-015: Count Pairs Equal Double Hash
# Input: String s, Length L
# Output: Number of pairs (i, j) where i < j and s[i:i+L] has same double hash as s[j:j+L]
# ============================================================================

def solve_hsh015(s: str, L: int) -> int:
    """Count pairs of substrings with same double hash"""
    if L > len(s):
        return 0
    
    n = len(s)
    hash_count = {}
    
    # Generate all substrings of length L and their hashes
    for i in range(n - L + 1):
        substring = s[i:i+L]
        
        # Compute double hash (using two different bases/mods)
        hash1 = 0
        for char in substring:
            hash1 = (hash1 * BASE1 + ord(char)) % MOD1
        
        hash2 = 0
        BASE2 = 317
        MOD2 = 10**9 + 9
        for char in substring:
            hash2 = (hash2 * BASE2 + ord(char)) % MOD2
        
        double_hash = (hash1, hash2)
        hash_count[double_hash] = hash_count.get(double_hash, 0) + 1
    
    # Count pairs: C(n, 2) for each hash with count n
    pairs = 0
    for count in hash_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    
    return pairs

def generate_hsh015_tests():
    tests = {'problem_id': 'HSH-015', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("abcabc", 3),
        ("aaaa", 2),
        ("test", 2)
    ]
    
    # Public (5)
    public = [
        ("a", 1),
        ("aa", 1),
        ("abc", 1),
        ("abab", 2),
        ("test", 1)
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("x", 1),
        ("aa", 1),
        ("aaa", 1),
        ("aaaa", 1),
        ("abcdefghij", 1)
    ]
    
    # Boundary (5)
    hidden += [
        ("a" * 100, 50),
        ("ab" * 50, 2),
        ("abc" * 30, 3),
        ("test", 4),
        ("a" * 50, 25)
    ]
    
    # Normal (8)
    hidden += [
        ("algorithm", 3),
        ("hashing", 2),
        ("rolling", 3),
        ("substring", 4),
        ("matching", 3),
        ("pattern", 2),
        ("detection", 3),
        ("collision", 4)
    ]
    
    # Special (5)
    hidden += [
        ("abcabc", 3),
        ("ababab", 2),
        ("test" * 10, 4),
        ("xyz" * 20, 3),
        ("a" * 30 + "b" * 30, 10)
    ]
    
    # Stress (4)
    set_seed(115)
    hidden += [
        ("a" * 200, 50),
        ("abc" * 100, 3),
        (''.join(random.choice("ab") for _ in range(300)), 10),
        ("test" * 100, 4)
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s, L in category_list:
            result = solve_hsh015(s, L)
            input_str = f"{s}\n{L}"
            output_str = str(result)
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-016: Hash Near-Anagram Indexing
# Input: List of words
# Output: Number of connected components (words connected if near-anagrams)
# ============================================================================

def solve_hsh016(words: List[str]) -> int:
    """
    Count connected components of near-anagram groups
    Two words are near-anagrams if removing one char from each makes them anagrams
    """
    if not words:
        return 0
    
    # Union-Find
    parent = list(range(len(words)))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    def are_near_anagrams(w1: str, w2: str) -> bool:
        """Check if w1 and w2 are near-anagrams"""
        # Try removing each character from w1
        for i in range(len(w1)):
            reduced_w1 = w1[:i] + w1[i+1:]
            # Try removing each character from w2
            for j in range(len(w2)):
                reduced_w2 = w2[:j] + w2[j+1:]
                # Check if anagrams
                if sorted(reduced_w1) == sorted(reduced_w2):
                    return True
        return False
    
    # Check all pairs
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if are_near_anagrams(words[i], words[j]):
                union(i, j)
    
    # Count components
    return len(set(find(i) for i in range(len(words))))

def generate_hsh016_tests():
    tests = {'problem_id': 'HSH-016', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        (["abc", "bcd", "cde"]),
        (["ab", "ba", "abc"]),
        (["test", "best", "rest"])
    ]
    
    # Public (5)
    public = [
        (["a"]),
        (["ab", "ba"]),
        (["abc", "def"]),
        (["test", "best"]),
        (["hello", "world"])
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        (["x"]),
        (["a", "b", "c"]),
        (["aa", "ab", "ba"]),
        (["abc"]),
        (["test", "test"])
    ]
    
    # Boundary (5)
    hidden += [
        (["a", "b"]),
        (["ab", "ba", "ab"]),
        (["test"] * 10),
        (["a" * 10 for _ in range(5)]),
        ([chr(ord('a') + i) * 5 for i in range(10)])
    ]
    
    # Normal (8)
    hidden += [
        (["hash", "ash", "has"]),
        (["test", "best", "west", "rest"]),
        (["abc", "bca", "cab"]),
        (["word", "lord", "cord"]),
        (["string", "spring", "bring"]),
        (["code", "node", "mode"]),
        (["data", "date", "late"]),
        (["hash", "cash", "dash"])
    ]
    
    # Special (5)
    hidden += [
        (["abc", "bcd", "cde", "def"]),
        (["test", "best", "rest", "west"]),
        (["a" * 5, "a" * 6, "a" * 7]),
        (["abc" * i for i in range(1, 6)]),
        (["pattern", "pattern"])
    ]
    
    # Stress (4)
    set_seed(116)
    hidden += [
        ([f"word{i}" for i in range(20)]),
        (["test"] * 30),
        ([''.join(random.choice(string.ascii_lowercase) for _ in range(5)) for _ in range(25)]),
        (["a" * random.randint(3, 8) for _ in range(30)])
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for words in category_list:
            result = solve_hsh016(words)
            input_str = f"{len(words)}\n" + "\n".join(words)
            output_str = str(result)
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
        ('014', 'longest-pal-prefix-after-append', generate_hsh014_tests),
        ('015', 'count-pairs-equal-double-hash', generate_hsh015_tests),
        ('016', 'hash-near-anagram-indexing', generate_hsh016_tests),
    ]
    
    print("=" * 70)
    print("HASHING TEST GENERATOR - PART 4 (HSH-014 to HSH-016)")
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
    print("ALL HASHING TEST GENERATION COMPLETE!")
    print("=" * 70)
    print("\nGenerated HSH-014 through HSH-016")
    print("HSH-001 through HSH-016 (except HSH-011) are complete with 35 test cases each")

if __name__ == "__main__":
    main()
