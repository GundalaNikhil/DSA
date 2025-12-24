"""
COMPREHENSIVE Test Case Generation for Hashing Problems
Following Universal Test Case Generation Framework EXACTLY
Target: 30-40 test cases per problem with proper distribution
"""

import sys

# ============================================================================
# HELPER FUNCTION - HSH-001: Polynomial Hash of Prefixes
# ============================================================================

def compute_prefix_hashes(s, B, M):
    """
    Compute polynomial rolling hash for every prefix.
    H_0 = s[0] mod M
    H_i = (H_{i-1} * B + s[i]) mod M
    """
    hashes = []
    current_hash = 0
    
    for char in s:
        current_hash = (current_hash * B + ord(char)) % M
        hashes.append(current_hash)
        
    return hashes

# ============================================================================
# HSH-001 TEST CASE GENERATOR
# ============================================================================

def generate_hsh001():
    """
    HSH-001: Polynomial Hash of Prefixes
    
    Target: 30-40 total test cases
    - Samples: 2-3
    - Public: 3-5
    - Hidden: 25-35 (Edge: 5, Boundary: 5, Negative: N/A, Special: 5, Normal: 8, Stress: 4)
    """
    test_cases = {
        'problem_id': 'HSH_POLYNOMIAL_HASH_PREFIXES__3824',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # =================================================================
    # SAMPLES (2-3) - From editorial
    # =================================================================
    
    # Sample 1: Basic example from editorial
    s, B, M = 'abc', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['samples'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Sample 2: Single character
    s, B, M = 'a', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['samples'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Sample 3: Short string with standard base
    s, B, M = 'test', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['samples'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # =================================================================
    # PUBLIC (3-5) - Basic scenarios visible to users
    # =================================================================
    
    # Public 1: Minimum constraint - single character 'z'
    s, B, M = 'z', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Public 2: Two same characters
    s, B, M = 'aa', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Public 3: Simple word
    s, B, M = 'hello', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Public 4: Palindrome
    s, B, M = 'aba', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Public 5: All different characters
    s, B, M = 'abcde', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['public'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # =================================================================
    # HIDDEN - EDGE CASES (5 test cases)
    # =================================================================
    
    # Edge 1: All same character (minimum ASCII)
    s, B, M = 'aaaaaaaaaa', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge 2: All same character (maximum ASCII)
    s, B, M = 'zzzzzzzzzz', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge 3: Alternating two characters
    s, B, M = 'ababababab', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge 4: Sequential alphabet
    s, B, M = 'abcdefghijklmnopqrst', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Edge 5: Reverse alphabet sequence
    s, B, M = 'zyxwvutsrq', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # =================================================================
    # HIDDEN - BOUNDARY CASES (5 test cases)
    # =================================================================
    
    # Boundary 1: Minimum base (B=2)
    s, B, M = 'binary', 2, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary 2: Small base (B=10)
    s, B, M = 'decimal', 10, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary 3: Large base close to M
    s, B, M = 'large', 999999937, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary 4: Small modulus (collision potential)
    s, B, M = 'collision', 31, 1000003
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Boundary 5: Different common base (B=53)
    s, B, M = 'prime', 53, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # =================================================================
    # HIDDEN - SPECIAL CONSTRAINT CASES (5 test cases)
    # =================================================================
    
    # Special 1: Palindrome string
    s, B, M = 'racecar', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special 2: Repeated pattern (abc)
    s, B, M = 'abcabcabcabc', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special 3: Powers of 2 length
    s, B, M = 'a' * 16, 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special 4: Prime length (13 characters)
    s, B, M = 'thequickbrown', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Special 5: Common hash base combination
    s, B, M = 'hashing', 911382323, 1000000009
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # =================================================================
    # HIDDEN - NORMAL CASES (8 test cases)
    # =================================================================
    
    # Normal 1: English word
    s, B, M = 'algorithm', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 2: Programming term
    s, B, M = 'function', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 3: Mixed vowels and consonants
    s, B, M = 'beautiful', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 4: Medium length word
    s, B, M = 'programming', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 5: Double letters
    s, B, M = 'football', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 6: All unique characters
    s, B, M = 'abcdefghij', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 7: With repeated substrings
    s, B, M = 'banana', 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Normal 8: Technical term
    s, B, M = 'database', 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # =================================================================
    # HIDDEN - STRESS CASES (4 test cases)
    # =================================================================
    
    # Stress 1: Long repeated pattern (300 chars)
    s, B, M = 'abc' * 100, 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Stress 2: Long alternating (500 chars)
    s, B, M = 'ab' * 250, 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Stress 3: All same character long (1000 chars)
    s, B, M = 'a' * 1000, 911382323, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    # Stress 4: Maximum variety (alphabet * 38 = 988 chars)
    s, B, M = 'abcdefghijklmnopqrstuvwxyz' * 38, 31, 1000000007
    result = compute_prefix_hashes(s, B, M)
    test_cases['hidden'].append({
        'input': f'{s}\n{B} {M}',
        'output': ' '.join(map(str, result))
    })
    
    return test_cases

# ============================================================================
# YAML WRITER WITH EXACT FORMAT
# ============================================================================

def write_yaml(filename, data):
    """Write test cases to YAML with exact |- format"""
    with open(filename, 'w') as f:
        f.write(f"problem_id: {data['problem_id']}\n")
        
        # Samples
        f.write("samples:\n")
        for test in data['samples']:
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            for line in test['output'].split('\n'):
                f.write(f"      {line}\n")
        
        # Public
        f.write("public:\n")
        for test in data['public']:
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            for line in test['output'].split('\n'):
                f.write(f"      {line}\n")
        
        # Hidden
        f.write("hidden:\n")
        for test in data['hidden']:
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            for line in test['output'].split('\n'):
                f.write(f"      {line}\n")
    
    print(f"✅ Generated: {filename}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    base_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Hashing/testcases/'
    
    print("=" * 80)
    print("COMPREHENSIVE TEST CASE GENERATION - HSH-001")
    print("Target: 30-40 test cases per problem")
    print("=" * 80)
    
    print(f"\n🔄 Generating HSH-001-polynomial-hash-prefixes.yaml...")
    test_cases = generate_hsh001()
    
    samples = len(test_cases['samples'])
    public = len(test_cases['public'])
    hidden = len(test_cases['hidden'])
    total = samples + public + hidden
    
    print(f"\n📊 Test Case Distribution:")
    print(f"   Samples: {samples}")
    print(f"   Public: {public}")
    print(f"   Hidden: {hidden}")
    print(f"      ├─ Edge Cases: 5")
    print(f"      ├─ Boundary Cases: 5")
    print(f"      ├─ Special Constraint: 5")
    print(f"      ├─ Normal Cases: 8")
    print(f"      └─ Stress Cases: 4")
    print(f"   TOTAL: {total}")
    
    filepath = base_path + 'HSH-001-polynomial-hash-prefixes.yaml'
    write_yaml(filepath, test_cases)
    
    print("\n" + "=" * 80)
    print(f"✨ COMPLETE! Generated {total} test cases")
    print("=" * 80)

if __name__ == "__main__":
    main()
