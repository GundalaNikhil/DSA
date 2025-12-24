"""
Generate comprehensive test cases for Hashing problems (HSH-001 to HSH-016)
Following the Universal Test Case Generation Framework
"""

import yaml
import sys

def compute_prefix_hashes(s, B, M):
    """Helper for HSH-001"""
    hashes = []
    current_hash = 0
    for char in s:
        current_hash = (current_hash * B + ord(char)) % M
        hashes.append(current_hash)
    return hashes

def substring_equal_hash(s, queries, B=911382323, M=1000000007):
    """Helper for HSH-002: Check if substrings are equal using hash"""
    n = len(s)
    # Compute prefix hashes
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = (prefix[i] * B + ord(s[i])) % M
    
    # Compute powers of B
    pow_B = [1] * (n + 1)
    for i in range(1, n + 1):
        pow_B[i] = (pow_B[i - 1] * B) % M
    
    results = []
    for l1, r1, l2, r2 in queries:
        # Hash of s[l1..r1]
        len1 = r1 - l1 + 1
        hash1 = (prefix[r1 + 1] - prefix[l1] * pow_B[len1]) % M
        
        # Hash of s[l2..r2]
        len2 = r2 - l2 + 1
        hash2 = (prefix[r2 + 1] - prefix[l2] * pow_B[len2]) % M
        
        results.append("YES" if hash1 == hash2 else "NO")
    return results

def lcs_hash(s, t):
    """Helper for HSH-003: Longest Common Substring using hash"""
    n, m = len(s), len(t)
    
    def get_all_substrings_hash(string, length, B=911382323, M=1000000007):
        """Get all substring hashes of given length"""
        if length > len(string):
            return set()
        
        hashes = set()
        curr_hash = 0
        pow_B = pow(B, length - 1, M)
        
        # First window
        for i in range(length):
            curr_hash = (curr_hash * B + ord(string[i])) % M
        hashes.add(curr_hash)
        
        # Sliding window
        for i in range(length, len(string)):
            curr_hash = (curr_hash - ord(string[i - length]) * pow_B) % M
            curr_hash = (curr_hash * B + ord(string[i])) % M
            hashes.add(curr_hash)
        
        return hashes
    
    # Binary search on length
    left, right = 0, min(n, m)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Get all hashes of length mid from both strings
        s_hashes = get_all_substrings_hash(s, mid)
        t_hashes = get_all_substrings_hash(t, mid)
        
        # Check if there's a common hash
        if s_hashes & t_hashes:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def count_distinct_substrings(s):
    """Helper for HSH-005"""
    B = 313
    M = 1000000007
    n = len(s)
    hashes = set()
    
    for i in range(n):
        current_hash = 0
        for j in range(i, n):
            current_hash = (current_hash * B + ord(s[j])) % M
            hashes.add(current_hash)
    
    return len(hashes) + 1  # +1 for empty string

# Generate HSH-001: Polynomial Hash of Prefixes
def generate_hsh001():
    test_cases = {
        'problem_id': 'HSH_POLYNOMIAL_HASH_PREFIXES__3824',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Samples
    s = 'abc'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['samples'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    s = 'a'
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['samples'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Public test cases
    # Edge: Single character
    s = 'z'
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge: Two same characters
    s = 'aa'
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal: Simple string
    s = 'hello'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Hidden test cases
    # Edge: All same character
    s = 'zzzzzzzzzz'
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge: Alphabet sequence
    s = 'abcdefghij'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge: Maximum ASCII lowercase letter
    s = 'zzz'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge: Minimum ASCII lowercase letter
    s = 'aaa'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary: Small B (base 2)
    s = 'test'
    B, M = 2, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary: Large B close to M
    s = 'code'
    B, M = 999999937, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary: Small M to test collision potential
    s = 'collision'
    B, M = 31, 1000003
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special Constraint: Palindrome
    s = 'racecar'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special Constraint: Repeated pattern
    s = 'ababab'
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special Constraint: Different base (53 is common for hashing)
    s = 'hash'
    B, M = 53, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal: Mixed letters
    s = 'thequickbrownfox'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal: Medium length
    s = 'programming'
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal: Repeated substring
    s = 'abcabcabc'
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Stress: Long string with pattern
    s = 'abc' * 100  # 300 characters
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Stress: Long alternating
    s = 'ab' * 250  # 500 characters
    B, M = 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Stress: All same long
    s = 'a' * 500
    B, M = 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    return test_cases

# Generate HSH-005: Count Distinct Substrings
def generate_hsh005():
    test_cases = {
        'problem_id': 'HSH_COUNT_DISTINCT_SUBSTRINGS__8741',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Samples
    test_cases['samples'].append({
        'input': 'aaa',
        'output': '4'
    })
    
    test_cases['samples'].append({
        'input': 'abc',
        'output': '7'
    })
    
    # Public test cases
    # Edge: Single character
    s = 'a'
    result = count_distinct_substrings(s)
    test_cases['public'].append({
        'input': s,
        'output': str(result)
    })
    
    # Edge: Two same characters
    s = 'aa'
    result = count_distinct_substrings(s)
    test_cases['public'].append({
        'input': s,
        'output': str(result)
    })
    
    # Normal: Short distinct string
    s = 'abcd'
    result = count_distinct_substrings(s)
    test_cases['public'].append({
        'input': s,
        'output': str(result)
    })
    
    # Hidden test cases
    # Edge: All same characters (long)
    s = 'zzzzz'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Edge: Two character alternating
    s = 'abababa'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Boundary: Palindrome
    s = 'racecar'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Normal: Mixed characters
    s = 'hello'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Normal: Repeated pattern
    s = 'abcabc'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Normal: All unique characters
    s = 'abcdefgh'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Stress: Medium length repeated
    s = 'abc' * 10  # 30 chars
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Stress: Medium length unique
    s = 'abcdefghijklmnopqrstuvwxyz'[:20]  # 20 unique chars
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    # Special: Binary string
    s = '0101010101'
    result = count_distinct_substrings(s)
    test_cases['hidden'].append({
        'input': s,
        'output': str(result)
    })
    
    return test_cases

def write_yaml(filename, data):
    """Write test cases to YAML file with proper formatting"""
    with open(filename, 'w') as f:
        f.write(f"problem_id: {data['problem_id']}\n")
        
        # Write samples
        f.write("samples:\n")
        for test in data['samples']:
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            f.write(f"      {test['output']}\n")
        
        # Write public
        f.write("public:\n")
        for test in data['public']:
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            f.write(f"      {test['output']}\n")
        
        # Write hidden
        f.write("hidden:\n")
        for test in data['hidden']:
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            f.write(f"      {test['output']}\n")
    
    print(f"✅ Generated: {filename}")

def main():
    # Generate test cases for each problem
    problems = [
        ('HSH-001-polynomial-hash-prefixes.yaml', generate_hsh001),
        ('HSH-005-count-distinct-substrings-hash.yaml', generate_hsh005),
    ]
    
    base_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Hashing/testcases/'
    
    for filename, generator_func in problems:
        print(f"\n🔄 Generating {filename}...")
        test_cases = generator_func()
        filepath = base_path + filename
        write_yaml(filepath, test_cases)
        
        # Print summary
        print(f"   Samples: {len(test_cases['samples'])}")
        print(f"   Public: {len(test_cases['public'])}")
        print(f"   Hidden: {len(test_cases['hidden'])}")
        print(f"   Total: {len(test_cases['samples']) + len(test_cases['public']) + len(test_cases['hidden'])}")

if __name__ == "__main__":
    main()
    print("\n✨ Test case generation complete!")
