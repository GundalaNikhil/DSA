#!/usr/bin/env python3
"""
Comprehensive Test Case Generator for Hashing Problems HSH-007 through HSH-016
Part 2: Completing all remaining hashing problems
"""

import random
import string
import os
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
# HSH-007: Detect Period String
# Input: string s
# Output: Single integer (smallest period length)
# ============================================================================

def solve_hsh007(s: str) -> int:
    """Find smallest period of string"""
    if not s:
        return 0
    
    n = len(s)
    for period in range(1, n + 1):
        if n % period == 0:
            # Check if s is repeating pattern of length 'period'
            pattern = s[:period]
            if pattern * (n // period) == s:
                return period
    return n

def generate_hsh007_tests():
    tests = {'problem_id': 'HSH-007', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = ["abcabcabc", "abc", "aaaa"]
    
    # Public (5)
    public = ["a", "aa", "abab", "test", "xyxyxyxy"]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += ["x", "aaaaaa", "abcdef", "ababababab", "xyzxyzxyz"]
    
    # Boundary (5)
    hidden += ["ab", "ba", "a" * 100, "abcabc", "z" * 999]
    
    # Normal (8)
    hidden += ["algorithm", "hashing", "period", "repeating", "pattern", "string", "detection", "circular"]
    
    # Special (5)
    hidden += ["abcabcabc", "aaabaaab", ("abc" * 33)[:99], "test" * 25, "x" * 50 + "y" * 50]
    
    # Stress (4)
    set_seed(107)
    hidden += [
        "a" * 300,
        "abc" * 200,
        ''.join(random.choice("ab") for _ in range(500)),
        "test" * 125
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s in category_list:
            result = solve_hsh007(s)
            input_str = s
            output_str = str(result)
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-008: Max Repeated Block Length
# Input: string s
# Output: Single integer (max length of non-overlapping repeated substring)
# ============================================================================

def solve_hsh008(s: str) -> int:
    """Find max length of non-overlapping repeated substring"""
    if not s or len(s) < 2:
        return 0
    
    n = len(s)
    max_len = 0
    
    # Try all possible lengths from n//2 down to 1
    for length in range(n // 2, 0, -1):
        # Check all substrings of this length
        seen = {}
        for i in range(n - length + 1):
            substring = s[i:i+length]
            if substring in seen:
                # Check if non-overlapping
                prev_pos = seen[substring]
                if i >= prev_pos + length:
                    return length
            else:
                seen[substring] = i
    
    return max_len

def generate_hsh008_tests():
    tests = {'problem_id': 'HSH-008', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = ["abcabc", "test", "abab"]
    
    # Public (5)
    public = ["a", "aa", "abcdabcd", "hello", "xyzxyz"]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += ["x", "ab", "aaa", "abcdefghij", "xyxyxy"]
    
    # Boundary (5)
    hidden += ["ab", "abc", "a" * 100, "test" * 25, "z" * 50]
    
    # Normal (8)
    hidden += ["algorithm", "repeated", "blocking", "maximum", "substring", "overlapping", "detection", "hashing"]
    
    # Special (5)
    hidden += ["abcabcabc", "testtest", "aaabaaab", "xyzxyzxyz", "racecarracecar"]
    
    # Stress (4)
    set_seed(108)
    hidden += [
        "abc" * 150,
        "a" * 500,
        ''.join(random.choice("abc") for _ in range(400)),
        "test" * 100
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s in category_list:
            result = solve_hsh008(s)
            input_str = s
            output_str = str(result)
            tests[category_name].append({'input': input_str, 'output': output_str})
    
    return tests

# ============================================================================
# HSH-009: Substring Hash Under Edits
# Input: string s, Q operations (UPDATE i c or QUERY l r)
# Output: For each QUERY, output the hash value
# ============================================================================

def solve_hsh009(s: str, operations: List[Tuple]) -> List[int]:
    """Process updates and queries"""
    s_list = list(s)
    results = []
    
    for op in operations:
        if op[0] == "U":
            i, c = op[1], op[2]
            s_list[i] = c
        else:  # Q (QUERY)
            l, r = op[1], op[2]
            substring = ''.join(s_list[l:r+1])
            # Compute hash
            hash_val = 0
            for char in substring:
                hash_val = (hash_val * BASE1 + ord(char)) % MOD1
            results.append(hash_val)
    
    return results

def generate_hsh009_tests():
    tests = {'problem_id': 'HSH-009', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("abc", [("Q", 0, 2), ("U", 1, 'x'), ("Q", 0, 2)]),
        ("test", [("Q", 0, 3), ("U", 0, 'b'), ("Q", 0, 3)]),
        ("hello", [("Q", 0, 4), ("U", 2, 'x'), ("Q", 0, 4)])
    ]
    
    # Public (5)
    public = [
        ("a", [("Q", 0, 0)]),
        ("ab", [("Q", 0, 1), ("U", 0, 'z'), ("Q", 0, 1)]),
        ("xyz", [("Q", 0, 2), ("U", 1, 'a'), ("Q", 0, 2)]),
        ("test", [("U", 0, 'x'), ("Q", 0, 3)]),
        ("hello", [("Q", 1, 3), ("U", 2, 'z'), ("Q", 1, 3)])
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("x", [("Q", 0, 0), ("U", 0, 'y'), ("Q", 0, 0)]),
        ("aaaa", [("Q", 0, 3)] + [("U", i, 'b') for i in range(4)] + [("Q", 0, 3)]),
        ("abcdef", [("Q", i, i+2) for i in range(4)]),
        ("test" * 10, [("Q", 0, 39), ("U", 20, 'x'), ("Q", 0, 39)]),
        ("z" * 50, [("Q", 0, 49)] + [("U", i*5, 'a') for i in range(10)] + [("Q", 0, 49)])
    ]
    
    # Boundary (5)
    hidden += [
        ("ab", [("Q", 0, 0), ("Q", 1, 1)]),
        ("a" * 100, [("Q", 0, 99)] + [("U", i*10, chr(ord('a') + i % 26)) for i in range(10)] + [("Q", 0, 99)]),
        ("test", [("U", i, chr(ord('a') + i)) for i in range(4)] + [("Q", 0, 3)]),
        ("xyz" * 20, [("Q", i*6, i*6+5) for i in range(10)]),
        ("algorithm", [("Q", 0, 8), ("U", 4, 'x'), ("Q", 0, 8)])
    ]
    
    # Normal (8)
    hidden += [
        ("hashing", [("Q", 0, 6), ("U", 3, 'x'), ("Q", 0, 6)]),
        ("rolling", [("Q", 0, 6), ("U", 0, 'p'), ("Q", 0, 6)]),
        ("substring", [("Q", 0, 8), ("U", 4, 'z'), ("Q", 0, 8)]),
        ("updates", [("U", i, chr(ord('a') + i)) for i in range(7)] + [("Q", 0, 6)]),
        ("queries", [("Q", 0, 6), ("U", 3, 'x'), ("U", 5, 'y'), ("Q", 0, 6)]),
        ("dynamic", [("Q", 0, 6), ("U", 2, 'x'), ("Q", 0, 6)]),
        ("mutable", [("Q", 0, 6), ("U", 4, 'z'), ("Q", 0, 6)]),
        ("editable", [("Q", 0, 7), ("U", 3, 'x'), ("Q", 0, 7)])
    ]
    
    # Special (5)
    hidden += [
        ("palindrome", [("Q", 0, 9), ("U", 5, 'x'), ("Q", 0, 9)]),
        ("racecar", [("Q", 0, 6)] + [("U", i, 'a') for i in range(7)] + [("Q", 0, 6)]),
        ("abcabcabc", [("Q", 0, 8), ("U", 3, 'x'), ("Q", 3, 8)]),
        ("test" * 15, [("Q", 0, 59)] + [("U", i*12, 'z') for i in range(5)] + [("Q", 0, 59)]),
        ("mixed", [("Q", 0, 4), ("U", 1, 'x'), ("U", 3, 'y'), ("Q", 0, 4)])
    ]
    
    # Stress (4)
    set_seed(109)
    base_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(200))
    hidden += [
        (base_str, [("Q", 0, 199)] + [("U", random.randint(0, 199), random.choice(string.ascii_lowercase)) for _ in range(20)] + [("Q", 0, 199)]),
        ("a" * 300, [("Q", 0, 299)] + [("U", i*30, chr(ord('a') + i % 26)) for i in range(10)] + [("Q", 0, 299)]),
        ("test" * 100, [("Q", i*50, min(i*50+49, 399)) for i in range(8)]),
        ("abc" * 150, [("Q", 0, 449)] + [("U", i*45, 'z') for i in range(10)] + [("Q", 0, 449)])
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for s, ops in category_list:
            result = solve_hsh009(s, ops)
            input_str = f"{s}\n{len(ops)}\n"
            for op in ops:
                if op[0] == "U":
                    input_str += f"U {op[1]} {op[2]}\n"
                else:
                    input_str += f"Q {op[1]} {op[2]}\n"
            output_str = "\n".join(map(str, result))
            tests[category_name].append({'input': input_str.strip(), 'output': output_str})
    
    return tests

# ============================================================================
# HSH-010: Two String Concat Equal
# Input: Four strings a, b, c, d (each on separate line)
# Output: "true" or "false" (whether a+b == c+d)
# ============================================================================

def solve_hsh010(a: str, b: str, c: str, d: str) -> bool:
    """Check if a+b == c+d using hashing"""
    return a + b == c + d

def generate_hsh010_tests():
    tests = {'problem_id': 'HSH-010', 'samples': [], 'public': [], 'hidden': []}
    
    # Samples (3)
    samples = [
        ("abc", "def", "abcd", "ef"),
        ("hello", "world", "hellow", "orld"),
        ("test", "ing", "tes", "ting")
    ]
    
    # Public (5)
    public = [
        ("a", "b", "a", "b"),
        ("x", "y", "xy", ""),
        ("hello", "", "hel", "lo"),
        ("ab", "cd", "abc", "d"),
        ("test", "test", "testte", "st")
    ]
    
    # Hidden (27)
    hidden = []
    
    # Edge (5)
    hidden += [
        ("", "", "", ""),
        ("a", "", "", "a"),
        ("", "b", "b", ""),
        ("xyz", "abc", "xy", "zabc"),
        ("test", "case", "testc", "ase")
    ]
    
    # Boundary (5)
    hidden += [
        ("a", "b", "c", "d"),
        ("a" * 100, "b" * 100, "a" * 100 + "b" * 100, ""),
        ("x", "y" * 99, "", "x" + "y" * 99),
        ("test", "ing", "testi", "ng"),
        ("algorithm", "", "algo", "rithm")
    ]
    
    # Normal (8)
    hidden += [
        ("hash", "ing", "hashi", "ng"),
        ("concat", "enate", "concate", "nate"),
        ("string", "match", "stringm", "atch"),
        ("equal", "ity", "equali", "ty"),
        ("compare", "test", "comparet", "est"),
        ("verify", "now", "verifyn", "ow"),
        ("check", "sum", "checks", "um"),
        ("valid", "ate", "valida", "te")
    ]
    
    # Special (5)
    hidden += [
        ("abc" * 20, "def" * 20, "abc" * 20 + "def" * 20, ""),
        ("test", "test", "te", "sttest"),
        ("aaa", "bbb", "aa", "abbb"),
        ("racecar", "civic", "racecarc", "ivic"),
        ("pattern", "match", "patternm", "atch")
    ]
    
    # Stress (4)
    set_seed(110)
    s1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(250))
    s2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(250))
    split_point = random.randint(1, 499)
    concatenated = s1 + s2
    hidden += [
        (s1, s2, concatenated[:split_point], concatenated[split_point:]),
        ("a" * 500, "b" * 500, "a" * 500 + "b" * 500, ""),
        ("test" * 125, "best" * 125, "test" * 125 + "best" * 125, ""),
        ("x" * 300, "y" * 300, "x" * 300, "y" * 300)
    ]
    
    for category_name, category_list in [('samples', samples), ('public', public), ('hidden', hidden)]:
        for a, b, c, d in category_list:
            result = solve_hsh010(a, b, c, d)
            input_str = f"{a}\n{b}\n{c}\n{d}"
            output_str = "true" if result else "false"
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
        ('007', 'detect-period-string', generate_hsh007_tests),
        ('008', 'max-repeated-block-length', generate_hsh008_tests),
        ('009', 'substring-hash-under-edits', generate_hsh009_tests),
        ('010', 'two-string-concat-equal', generate_hsh010_tests),
    ]
    
    print("=" * 70)
    print("HASHING TEST GENERATOR - PART 2 (HSH-007 to HSH-010)")
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
    print("PART 2 COMPLETE!")
    print("=" * 70)
    print("\nGenerated HSH-007 through HSH-010")
    print("Next: Create generator for HSH-011 through HSH-016")

if __name__ == "__main__":
    main()
