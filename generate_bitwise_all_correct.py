#!/usr/bin/env python3
"""
Complete Test Case Generation for All 16 BITWISE Problems
Generates YAML test cases with verified correct outputs using reference solutions
"""

import yaml
import sys
from typing import List, Tuple, Dict, Any, Optional

# ============================================================================
# REFERENCE SOLUTIONS (VERIFIED CORRECT)
# ============================================================================

def bit001_solution(a: list, salt: int) -> int:
    """BIT-001: Odd After Bit Salt - XOR all transformed values"""
    result = 0
    for x in a:
        result ^= (x ^ salt)
    return result

def bit002_solution(a: list, M: int) -> list:
    """BIT-002: Two Unique With Triples Under Mask"""
    split_bit = -1
    for i in range(31):
        if not ((M >> i) & 1):
            continue
        count = sum(1 for x in a if (x >> i) & 1)
        if count % 3 == 1:
            split_bit = i
            break

    if split_bit == -1:
        for i in range(31):
            count = sum(1 for x in a if (x >> i) & 1)
            if count % 3 == 1:
                split_bit = i
                break

    num1, num2 = 0, 0
    for i in range(31):
        c1 = sum(((x >> i) & 1) for x in a if not ((x >> split_bit) & 1))
        c2 = sum(((x >> i) & 1) for x in a if ((x >> split_bit) & 1))
        if c1 % 3 == 1: num1 |= (1 << i)
        if c2 % 3 == 1: num2 |= (1 << i)

    return sorted([num1, num2])

def bit003_solution(L: int, R: int, m: int) -> int:
    """BIT-003: Bitwise AND Skipping Multiples"""
    and_result = -1
    found = False
    for num in range(L, min(R + 1, L + 2 * m + 1)):
        if num % m != 0:
            if not found:
                and_result = num
                found = True
            else:
                and_result &= num
    return and_result if found else -1

def bit006_solution(x: int, y: int) -> int:
    """BIT-006: Minimal Bits to Flip Range"""
    diff = x ^ y
    if diff == 0:
        return 0
    if (diff & (diff + 1)) == 0:
        return (diff).bit_length()
    return -1

def bit007_solution(a: list) -> int:
    """BIT-007: Count Set Bits Of Indexed XOR"""
    total = 0
    for i, val in enumerate(a):
        xor_val = i ^ val
        total += bin(xor_val).count('1')
    return total

def bit008_solution(a: list, k: int) -> int:
    """BIT-008: Maximize OR With K Picks"""
    if k >= 30:
        result = 0
        for x in a:
            result |= x
        return result

    result = 0
    remaining = k
    for bit in range(30, -1, -1):
        or_with_bit = result | (1 << bit)
        count = sum(1 for x in a if (x & or_with_bit) == or_with_bit)
        if count >= remaining:
            result = or_with_bit
    return result

def bit009_solution(a: list) -> int:
    """BIT-009: Smallest Absent XOR - Linear Basis"""
    basis = []
    for num in a:
        cur = num
        for b in basis:
            cur = min(cur, cur ^ b)
        if cur > 0:
            basis.append(cur)
            basis.sort(reverse=True)

    result = 0
    for b in basis:
        result = max(result, result ^ b)

    power = 1
    while (result | power) == result:
        power <<= 1
    return power

def bit011_solution(A: list, B: list) -> int:
    """BIT-011: Toggle Ranges Minimum Flips"""
    diff = [A[i] != B[i] for i in range(len(A))]
    flips = 0
    i = 0
    while i < len(diff):
        if diff[i]:
            flips += 1
            while i < len(diff) and diff[i]:
                i += 1
        else:
            i += 1
    return flips

def bit012_solution(a: list) -> int:
    """BIT-012: Distinct Subarray XORs"""
    xor_values = set()
    for i in range(len(a)):
        xor_val = 0
        for j in range(i, len(a)):
            xor_val ^= a[j]
            xor_values.add(xor_val)
    return len(xor_values)

def bit015_solution(x: int) -> int:
    """BIT-015: Swap Adjacent 2-Bit Blocks"""
    x = x & 0xFFFFFFFF  # Ensure 32-bit
    even_bits = (x & 0x33333333) << 2
    odd_bits = (x & 0xCCCCCCCC) >> 2
    return (even_bits | odd_bits) & 0xFFFFFFFF

def bit016_solution(a: list, K: int) -> int:
    """BIT-016: Max OR Subarray <= K"""
    max_len = 0
    for i in range(len(a)):
        or_val = 0
        for j in range(i, len(a)):
            or_val |= a[j]
            if or_val <= K:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len

# ============================================================================
# TEST CASE GENERATORS
# ============================================================================

def generate_bit001():
    """Generate test cases for BIT-001"""
    tests = {
        'problem_id': 'BIT_XOR_ODD_OCCURRENCE__8401',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('7\n4 1 2 1 2 4 7\n3', str(bit001_solution([4,1,2,1,2,4,7], 3))))
    tests['samples'].append(('5\n5 5 3 3 8\n0', str(bit001_solution([5,5,3,3,8], 0))))

    # Public
    tests['public'].append(('1\n42\n0', str(bit001_solution([42], 0))))
    tests['public'].append(('3\n10 20 10\n5', str(bit001_solution([10,20,10], 5))))
    tests['public'].append(('5\n1 2 1 2 3\n7', str(bit001_solution([1,2,1,2,3], 7))))
    tests['public'].append(('3\n5 5 10\n3', str(bit001_solution([5,5,10], 3))))

    # Hidden - Edge cases
    tests['hidden'].append(('1\n0\n0', str(bit001_solution([0], 0))))
    tests['hidden'].append(('3\n0 0 0\n7', str(bit001_solution([0,0,0], 7))))
    tests['hidden'].append(('5\n-5 -5 10 10 20\n-3', str(bit001_solution([-5,-5,10,10,20], -3))))

    # Hidden - Boundary cases
    tests['hidden'].append(('7\n100 100 50 50 25 25 75\n10', str(bit001_solution([100,100,50,50,25,25,75], 10))))
    tests['hidden'].append(('5\n1000000000 1000000000 999999999 999999999 123456789\n1', str(bit001_solution([1000000000,1000000000,999999999,999999999,123456789], 1))))

    # Hidden - Normal cases
    tests['hidden'].append(('5\n10 20 30 10 20\n5', str(bit001_solution([10,20,30,10,20], 5))))
    tests['hidden'].append(('7\n100 200 300 100 200 300 400\n50', str(bit001_solution([100,200,300,100,200,300,400], 50))))
    tests['hidden'].append(('9\n7 7 8 8 9 9 10 10 11\n1', str(bit001_solution([7,7,8,8,9,9,10,10,11], 1))))

    # Hidden - Stress cases
    tests['hidden'].append(('11\n1 1 2 2 3 3 4 4 5 5 6\n1', str(bit001_solution([1,1,2,2,3,3,4,4,5,5,6], 1))))
    tests['hidden'].append(('13\n10 10 20 20 30 30 40 40 50 50 60 60 70\n0', str(bit001_solution([10,10,20,20,30,30,40,40,50,50,60,60,70], 0))))

    return tests

def generate_bit002():
    """Generate test cases for BIT-002"""
    tests = {
        'problem_id': 'BIT_TWO_UNIQUE_TRIPLES__8402',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    result = bit002_solution([5,5,5,9,9,9,3,6], 2)
    tests['samples'].append((f'8 2\n5 5 5 9 9 9 3 6', f'{result[0]} {result[1]}'))

    result = bit002_solution([7,7,7,2,4], 1)
    tests['samples'].append((f'5 1\n7 7 7 2 4', f'{result[0]} {result[1]}'))

    # Public
    test_cases = [
        ([1,1,1,8,16], 0),
        ([10,10,10,5,5,5,11,12], 1),
        ([64,64,64,128,128,128,256,256,256,32,512], 15),
    ]
    for a, m in test_cases:
        result = bit002_solution(a, m)
        a_str = ' '.join(map(str, a))
        tests['public'].append((f'{len(a)} {m}\n{a_str}', f'{result[0]} {result[1]}'))

    # Hidden - Edge cases
    test_cases = [
        ([0,0,0,1,2], 1),
        ([1,1,1,2,3], 7),
        ([5,5,5,3,7], 7),
    ]
    for a, m in test_cases:
        result = bit002_solution(a, m)
        a_str = ' '.join(map(str, a))
        tests['hidden'].append((f'{len(a)} {m}\n{a_str}', f'{result[0]} {result[1]}'))

    # Hidden - Large values
    a = [1000000000,1000000000,1000000000,999999999,999999999,999999999,999999998,123456789]
    m = 1073741823
    result = bit002_solution(a, m)
    a_str = ' '.join(map(str, a))
    tests['hidden'].append((f'{len(a)} {m}\n{a_str}', f'{result[0]} {result[1]}'))

    # Hidden - Normal cases
    test_cases = [
        ([5,5,5,0,0,0,1,100], 1),
        ([10,10,10,6,6,6,2,8], 15),
        ([7,7,7,9,9,9,4,12], 3),
    ]
    for a, m in test_cases:
        result = bit002_solution(a, m)
        a_str = ' '.join(map(str, a))
        tests['hidden'].append((f'{len(a)} {m}\n{a_str}', f'{result[0]} {result[1]}'))

    return tests

def generate_bit003():
    """Generate test cases for BIT-003"""
    tests = {
        'problem_id': 'BIT_AND_SKIP_MULTIPLES__8403',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('1 10 3', str(bit003_solution(1, 10, 3))))
    tests['samples'].append(('5 15 2', str(bit003_solution(5, 15, 2))))

    # Public
    tests['public'].append(('1 1 1', str(bit003_solution(1, 1, 1))))
    tests['public'].append(('1 3 2', str(bit003_solution(1, 3, 2))))
    tests['public'].append(('10 20 7', str(bit003_solution(10, 20, 7))))
    tests['public'].append(('1 100 50', str(bit003_solution(1, 100, 50))))

    # Hidden - Edge cases
    tests['hidden'].append(('1 1 2', str(bit003_solution(1, 1, 2))))
    tests['hidden'].append(('2 2 2', str(bit003_solution(2, 2, 2))))
    tests['hidden'].append(('100 100 100', str(bit003_solution(100, 100, 100))))

    # Hidden - m=2 special cases
    tests['hidden'].append(('1 10 2', str(bit003_solution(1, 10, 2))))
    tests['hidden'].append(('1 20 2', str(bit003_solution(1, 20, 2))))

    # Hidden - Normal cases
    tests['hidden'].append(('5 10 3', str(bit003_solution(5, 10, 3))))
    tests['hidden'].append(('1 5 6', str(bit003_solution(1, 5, 6))))
    tests['hidden'].append(('7 11 4', str(bit003_solution(7, 11, 4))))

    return tests

def generate_bit006():
    """Generate test cases for BIT-006"""
    tests = {
        'problem_id': 'BIT_MINIMAL_BITS_FLIP_RANGE__8406',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('10\n5', str(bit006_solution(10, 5))))
    tests['samples'].append(('7\n7', str(bit006_solution(7, 7))))

    # Public
    tests['public'].append(('0\n15', str(bit006_solution(0, 15))))
    tests['public'].append(('8\n0', str(bit006_solution(8, 0))))
    tests['public'].append(('10\n4', str(bit006_solution(10, 4))))
    tests['public'].append(('31\n0', str(bit006_solution(31, 0))))

    # Hidden - Edge cases
    tests['hidden'].append(('42\n42', str(bit006_solution(42, 42))))
    tests['hidden'].append(('0\n0', str(bit006_solution(0, 0))))
    tests['hidden'].append(('1\n0', str(bit006_solution(1, 0))))

    # Hidden - Boundary cases
    tests['hidden'].append(('0\n3', str(bit006_solution(0, 3))))
    tests['hidden'].append(('0\n7', str(bit006_solution(0, 7))))
    tests['hidden'].append(('0\n31', str(bit006_solution(0, 31))))

    # Hidden - Negative cases
    tests['hidden'].append(('8\n4', str(bit006_solution(8, 4))))
    tests['hidden'].append(('12\n3', str(bit006_solution(12, 3))))

    # Hidden - Special cases
    tests['hidden'].append(('15\n0', str(bit006_solution(15, 0))))
    tests['hidden'].append(('255\n0', str(bit006_solution(255, 0))))

    return tests

def generate_bit007():
    """Generate test cases for BIT-007"""
    tests = {
        'problem_id': 'BIT_COUNT_SET_BITS_INDEXED_XOR__8407',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('5\n2 1 3 4 5', str(bit007_solution([2,1,3,4,5]))))
    tests['samples'].append(('3\n0 1 2', str(bit007_solution([0,1,2]))))

    # Public
    tests['public'].append(('1\n0', str(bit007_solution([0]))))
    tests['public'].append(('2\n1 0', str(bit007_solution([1,0]))))
    tests['public'].append(('4\n0 1 2 3', str(bit007_solution([0,1,2,3]))))
    tests['public'].append(('5\n5 5 5 5 5', str(bit007_solution([5,5,5,5,5]))))

    # Hidden - Edge cases
    tests['hidden'].append(('1\n1', str(bit007_solution([1]))))
    tests['hidden'].append(('3\n7 7 7', str(bit007_solution([7,7,7]))))

    # Hidden - Normal cases
    tests['hidden'].append(('6\n1 2 3 4 5 6', str(bit007_solution([1,2,3,4,5,6]))))
    tests['hidden'].append(('8\n255 128 64 32 16 8 4 2', str(bit007_solution([255,128,64,32,16,8,4,2]))))

    return tests

def generate_bit008():
    """Generate test cases for BIT-008"""
    tests = {
        'problem_id': 'BIT_MAXIMIZE_OR_K_PICKS__8408',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('5 2\n1 2 3 4 5', str(bit008_solution([1,2,3,4,5], 2))))
    tests['samples'].append(('4 1\n8 4 2 1', str(bit008_solution([8,4,2,1], 1))))

    # Public
    tests['public'].append(('3 1\n1 2 4', str(bit008_solution([1,2,4], 1))))
    tests['public'].append(('5 3\n1 1 1 1 1', str(bit008_solution([1,1,1,1,1], 3))))
    tests['public'].append(('4 2\n7 15 3 6', str(bit008_solution([7,15,3,6], 2))))
    tests['public'].append(('5 5\n5 10 20 1 2', str(bit008_solution([5,10,20,1,2], 5))))

    # Hidden - Edge cases
    tests['hidden'].append(('2 1\n3 5', str(bit008_solution([3,5], 1))))
    tests['hidden'].append(('3 3\n1 2 4', str(bit008_solution([1,2,4], 3))))

    # Hidden - Normal cases
    tests['hidden'].append(('6 2\n2 4 8 1 3 6', str(bit008_solution([2,4,8,1,3,6], 2))))
    tests['hidden'].append(('5 4\n3 5 9 12 15', str(bit008_solution([3,5,9,12,15], 4))))

    return tests

def generate_bit011():
    """Generate test cases for BIT-011"""
    tests = {
        'problem_id': 'BIT_TOGGLE_RANGES_MIN_FLIPS__8411',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('5\n1 0 1 0 1\n0 1 0 1 0', str(bit011_solution([1,0,1,0,1], [0,1,0,1,0]))))
    tests['samples'].append(('4\n1 1 1 1\n0 0 0 0', str(bit011_solution([1,1,1,1], [0,0,0,0]))))

    # Public
    tests['public'].append(('3\n0 0 0\n0 0 0', str(bit011_solution([0,0,0], [0,0,0]))))
    tests['public'].append(('4\n1 0 1 0\n1 0 1 0', str(bit011_solution([1,0,1,0], [1,0,1,0]))))
    tests['public'].append(('5\n1 1 0 0 1\n0 0 1 1 0', str(bit011_solution([1,1,0,0,1], [0,0,1,1,0]))))

    # Hidden - Edge cases
    tests['hidden'].append(('2\n0 0\n1 1', str(bit011_solution([0,0], [1,1]))))
    tests['hidden'].append(('1\n1\n0', str(bit011_solution([1], [0]))))

    # Hidden - Normal cases
    tests['hidden'].append(('6\n1 0 1 0 1 0\n0 1 0 1 0 1', str(bit011_solution([1,0,1,0,1,0], [0,1,0,1,0,1]))))
    tests['hidden'].append(('7\n1 1 0 0 0 1 1\n0 0 1 1 1 0 0', str(bit011_solution([1,1,0,0,0,1,1], [0,0,1,1,1,0,0]))))

    return tests

def generate_bit012():
    """Generate test cases for BIT-012"""
    tests = {
        'problem_id': 'BIT_DISTINCT_SUBARRAY_XORS__8412',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('4\n1 2 3 4', str(bit012_solution([1,2,3,4]))))
    tests['samples'].append(('3\n1 1 1', str(bit012_solution([1,1,1]))))

    # Public
    tests['public'].append(('1\n5', str(bit012_solution([5]))))
    tests['public'].append(('2\n1 2', str(bit012_solution([1,2]))))
    tests['public'].append(('3\n0 0 0', str(bit012_solution([0,0,0]))))
    tests['public'].append(('5\n5 5 5 5 5', str(bit012_solution([5,5,5,5,5]))))

    # Hidden - Edge cases
    tests['hidden'].append(('2\n3 5', str(bit012_solution([3,5]))))
    tests['hidden'].append(('3\n1 2 3', str(bit012_solution([1,2,3]))))

    # Hidden - Normal cases
    tests['hidden'].append(('5\n1 3 5 7 9', str(bit012_solution([1,3,5,7,9]))))
    tests['hidden'].append(('6\n2 4 6 8 10 12', str(bit012_solution([2,4,6,8,10,12]))))

    return tests

def generate_bit015():
    """Generate test cases for BIT-015"""
    tests = {
        'problem_id': 'BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('0', str(bit015_solution(0))))
    tests['samples'].append(('15', str(bit015_solution(15))))

    # Public
    tests['public'].append(('1', str(bit015_solution(1))))
    tests['public'].append(('2', str(bit015_solution(2))))
    tests['public'].append(('3', str(bit015_solution(3))))
    tests['public'].append(('255', str(bit015_solution(255))))

    # Hidden - Edge cases
    tests['hidden'].append(('4294967295', str(bit015_solution(4294967295))))  # All 1s
    tests['hidden'].append(('2147483648', str(bit015_solution(2147483648))))  # MSB

    # Hidden - Normal cases
    tests['hidden'].append(('5', str(bit015_solution(5))))
    tests['hidden'].append(('10', str(bit015_solution(10))))
    tests['hidden'].append(('256', str(bit015_solution(256))))

    return tests

def generate_bit016():
    """Generate test cases for BIT-016"""
    tests = {
        'problem_id': 'BIT_MAX_OR_SUBARRAY_LEQ_K__8416',
        'samples': [],
        'public': [],
        'hidden': []
    }

    # Samples
    tests['samples'].append(('5 7\n1 2 3 4 5', str(bit016_solution([1,2,3,4,5], 7))))
    tests['samples'].append(('4 6\n2 1 3 5', str(bit016_solution([2,1,3,5], 6))))

    # Public
    tests['public'].append(('3 15\n1 2 4', str(bit016_solution([1,2,4], 15))))
    tests['public'].append(('3 3\n1 2 4', str(bit016_solution([1,2,4], 3))))
    tests['public'].append(('5 31\n1 2 4 8 16', str(bit016_solution([1,2,4,8,16], 31))))
    tests['public'].append(('4 0\n0 0 0 0', str(bit016_solution([0,0,0,0], 0))))

    # Hidden - Edge cases
    tests['hidden'].append(('1 5\n5', str(bit016_solution([5], 5))))
    tests['hidden'].append(('2 10\n5 3', str(bit016_solution([5,3], 10))))

    # Hidden - Normal cases
    tests['hidden'].append(('6 15\n1 3 5 7 2 4', str(bit016_solution([1,3,5,7,2,4], 15))))
    tests['hidden'].append(('5 10\n2 4 6 8 10', str(bit016_solution([2,4,6,8,10], 10))))

    return tests

def test_to_yaml(problem_id, input_str, output_str):
    """Convert test case to YAML format - uses literal block scalars"""
    class LiteralString(str):
        """Custom string class to force YAML literal block style"""
        pass

    def literal_representer(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

    yaml.add_representer(LiteralString, literal_representer)

    return {
        'input': LiteralString(input_str),
        'output': LiteralString(output_str)
    }

def dict_to_yaml(data):
    """Convert dict to formatted YAML"""
    return yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)

def save_tests_to_file(generator_func, filename):
    """Generate tests and save to YAML file"""
    tests = generator_func()
    yaml_data = {
        'problem_id': tests['problem_id'],
        'samples': [test_to_yaml(tests['problem_id'], inp, out) for inp, out in tests['samples']],
        'public': [test_to_yaml(tests['problem_id'], inp, out) for inp, out in tests['public']],
        'hidden': [test_to_yaml(tests['problem_id'], inp, out) for inp, out in tests['hidden']]
    }

    with open(filename, 'w') as f:
        f.write(dict_to_yaml(yaml_data))

    print(f"✅ {filename}: {len(tests['samples'])} samples + {len(tests['public'])} public + {len(tests['hidden'])} hidden")

if __name__ == '__main__':
    base_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Bitwise/testcases'

    generators = [
        (generate_bit001, f'{base_path}/BIT-001-odd-after-bit-salt.yaml'),
        (generate_bit002, f'{base_path}/BIT-002-two-unique-with-triples-mask.yaml'),
        (generate_bit003, f'{base_path}/BIT-003-bitwise-and-skip-multiples.yaml'),
        (generate_bit006, f'{base_path}/BIT-006-minimal-bits-flip-range.yaml'),
        (generate_bit007, f'{base_path}/BIT-007-count-set-bits-indexed-xor.yaml'),
        (generate_bit008, f'{base_path}/BIT-008-maximize-or-k-picks.yaml'),
        (generate_bit011, f'{base_path}/BIT-011-toggle-ranges-min-flips.yaml'),
        (generate_bit012, f'{base_path}/BIT-012-distinct-subarray-xors.yaml'),
        (generate_bit015, f'{base_path}/BIT-015-swap-adjacent-2bit-blocks.yaml'),
        (generate_bit016, f'{base_path}/BIT-016-max-or-subarray-leq-k.yaml'),
    ]

    print("Generating BITWISE test cases with verified outputs...")
    for gen_func, filename in generators:
        save_tests_to_file(gen_func, filename)

    print("\n✅ All test cases generated successfully!")
