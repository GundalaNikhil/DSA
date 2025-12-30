#!/usr/bin/env python3
"""
Generate comprehensive test cases for SegmentTree problems (SEG-001 to SEG-016)
Focus: basic, simple, edge, and corner cases only
"""

import yaml
import random
from pathlib import Path

random.seed(42)

def generate_seg001_tests():
    """Range Sum Point Updates Undo - with modulo"""
    tests = []

    # Test 1: Basic example
    tests.append({
        'input': "3 5 100\n1 2 3\nQUERY 0 2\nUPDATE 1 5\nQUERY 0 2\nUNDO 1\nQUERY 0 2",
        'output': "6\n9\n6"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 3 1000\n42\nQUERY 0 0\nUPDATE 0 100\nQUERY 0 0",
        'output': "42\n100"
    })

    # Test 3: Negative values
    tests.append({
        'input': "4 4 1000\n-5 10 -3 8\nQUERY 0 3\nUPDATE 0 5\nQUERY 0 3\nUNDO 1",
        'output': "10\n20"
    })

    # Test 4: Undo multiple
    tests.append({
        'input': "3 6 1000\n1 1 1\nUPDATE 0 10\nUPDATE 1 10\nUPDATE 2 10\nUNDO 3\nQUERY 0 2",
        'output': "3"
    })

    # Test 5: Modulo wrap
    tests.append({
        'input': "2 3 7\n5 4\nQUERY 0 1\nUPDATE 0 100\nQUERY 0 1",
        'output': "2\n4"
    })

    return tests

def generate_seg002_tests():
    """Range Add Range Sum"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "3 4\n1 2 3\nADD 0 1 5\nSUM 0 2\nADD 2 2 3\nSUM 0 2",
        'output': "16\n19"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 3\n10\nADD 0 0 5\nSUM 0 0\nADD 0 0 -3",
        'output': "15"
    })

    # Test 3: Full range operations
    tests.append({
        'input': "2 3\n1 1\nADD 0 1 10\nSUM 0 1\nADD 0 1 -5",
        'output': "22"
    })

    # Test 4: Negative values
    tests.append({
        'input': "3 3\n-5 10 -3\nSUM 0 2\nADD 1 1 -10\nSUM 0 2",
        'output': "2\n-8"
    })

    return tests

def generate_seg003_tests():
    """Range Min Range Add"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 5\n5 3 7 2\nQUERY 0 3\nADD 1 2 2\nQUERY 0 3\nADD 0 0 -10\nQUERY 0 3",
        'output': "2\n2\n-8"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 3\n42\nQUERY 0 0\nADD 0 0 10\nQUERY 0 0",
        'output': "42\n52"
    })

    # Test 3: Negative values
    tests.append({
        'input': "3 3\n-5 -10 -3\nQUERY 0 2\nADD 0 2 2\nQUERY 0 2",
        'output': "-10\n-8"
    })

    # Test 4: All same
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2\nADD 0 2 -5",
        'output': "5"
    })

    return tests

def generate_seg004_tests():
    """Inversion Count Updates"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 3\n2 1 3 0\nQUERY 0 3\nUPDATE 1 4\nQUERY 0 3",
        'output': "4\n3"
    })

    # Test 2: Sorted array (no inversions)
    tests.append({
        'input': "3 2\n1 2 3\nQUERY 0 2\nUPDATE 1 10",
        'output': "0"
    })

    # Test 3: Reverse sorted (max inversions)
    tests.append({
        'input': "3 1\n3 2 1\nQUERY 0 2",
        'output': "3"
    })

    # Test 4: Single element
    tests.append({
        'input': "1 2\n42\nQUERY 0 0\nUPDATE 0 100",
        'output': "0"
    })

    return tests

def generate_seg005_tests():
    """K-th Order Statistic"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 3\n3 1 4 1\nQUERY 0 3 2\nQUERY 1 3 1\nQUERY 0 2 1",
        'output': "3\n1\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n42\nQUERY 0 0 1",
        'output': "42"
    })

    # Test 3: All same
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2 1\nQUERY 0 2 3",
        'output': "5\n5"
    })

    # Test 4: Sorted
    tests.append({
        'input': "4 4\n1 2 3 4\nQUERY 0 3 1\nQUERY 0 3 2\nQUERY 0 3 3\nQUERY 0 3 4",
        'output': "1\n2\n3\n4"
    })

    return tests

def generate_seg006_tests():
    """Count Values in Range"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "5 4\n1 2 1 3 1\nCOUNT 1 4 1\nCOUNT 0 4 2\nUPDATE 2 2\nCOUNT 1 4 2",
        'output': "2\n1\n2"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nCOUNT 0 0 42\nUPDATE 0 100",
        'output': "1"
    })

    # Test 3: No matches
    tests.append({
        'input': "3 2\n1 1 1\nCOUNT 0 2 2\nCOUNT 0 2 1",
        'output': "0\n3"
    })

    # Test 4: All different
    tests.append({
        'input': "4 2\n1 2 3 4\nCOUNT 0 3 2\nCOUNT 0 3 5",
        'output': "1\n0"
    })

    return tests

def generate_seg007_tests():
    """Range XOR Basis"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 3\n1 2 3 4\nQUERY 0 3\nUPDATE 1 5\nQUERY 0 3",
        'output': "7\n7"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n5\nQUERY 0 0",
        'output': "5"
    })

    # Test 3: Powers of 2
    tests.append({
        'input': "3 2\n1 2 4\nQUERY 0 2\nUPDATE 0 8",
        'output': "7"
    })

    # Test 4: Zeros
    tests.append({
        'input': "2 1\n0 0\nQUERY 0 1",
        'output': "0"
    })

    return tests

def generate_seg008_tests():
    """Longest Increasing Subarray"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "5 3\n1 2 3 5 4\nQUERY 0 4\nUPDATE 3 6\nQUERY 0 4",
        'output': "4\n5"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n42\nQUERY 0 0",
        'output': "1"
    })

    # Test 3: All increasing
    tests.append({
        'input': "4 1\n1 2 3 4\nQUERY 0 3",
        'output': "4"
    })

    # Test 4: Decreasing
    tests.append({
        'input': "3 1\n5 4 3\nQUERY 0 2",
        'output': "1"
    })

    return tests

def generate_seg009_tests():
    """Range T-Threshold Majority"""
    tests = []

    # Test 1: Basic with majority
    tests.append({
        'input': "5 3\n1 1 1 2 2\nQUERY 0 4 3\nQUERY 0 4 4\nQUERY 1 3 2",
        'output': "1\n-1\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nQUERY 0 0 1\nQUERY 0 0 2",
        'output': "42\n-1"
    })

    # Test 3: All same
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2 2\nQUERY 0 2 4",
        'output': "5\n-1"
    })

    # Test 4: No majority
    tests.append({
        'input': "3 1\n1 2 3\nQUERY 0 2 2",
        'output': "-1"
    })

    return tests

def generate_seg010_tests():
    """Range GCD Skip Zones"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "5 4\n12 18 24 36 48\nGCD 0 4\nGCD 1 3\nSKIP 2\nGCD 0 4",
        'output': "6\n6\n12"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nGCD 0 0\nSKIP 0",
        'output': "42"
    })

    # Test 3: Coprime
    tests.append({
        'input': "3 1\n5 7 11\nGCD 0 2",
        'output': "1"
    })

    # Test 4: All same
    tests.append({
        'input': "3 1\n5 5 5\nGCD 0 2",
        'output': "5"
    })

    return tests

def generate_seg011_tests():
    """Range Min Index"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 3\n5 2 8 2\nQUERY 0 3\nQUERY 1 3\nUPDATE 2 1",
        'output': "1\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nQUERY 0 0\nUPDATE 0 10",
        'output': "0"
    })

    # Test 3: Increasing
    tests.append({
        'input': "4 1\n1 2 3 4\nQUERY 0 3",
        'output': "0"
    })

    # Test 4: Decreasing
    tests.append({
        'input': "4 1\n4 3 2 1\nQUERY 0 3",
        'output': "3"
    })

    return tests

def generate_seg012_tests():
    """Range Add K-th Order"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 4\n1 2 3 4\nQUERY 0 3 2\nADD 0 1 5\nQUERY 0 3 2\nADD 2 3 -1",
        'output': "2\n7"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nQUERY 0 0 1\nADD 0 0 10",
        'output': "42"
    })

    # Test 3: All same before add
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2 2\nADD 0 2 1",
        'output': "5"
    })

    # Test 4: Negative
    tests.append({
        'input': "3 2\n-1 -2 -3\nQUERY 0 2 1\nADD 0 2 10",
        'output': "-3"
    })

    return tests

def generate_seg013_tests():
    """Range Sum Multiple Powers (MOD 10^9+7)"""
    tests = []

    # Test 1: Power 1
    tests.append({
        'input': "3 2\n1 2 3\nQUERY 0 2 1\nQUERY 0 2 2",
        'output': "6\n14"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n5\nQUERY 0 0 1\nQUERY 0 0 3",
        'output': "5\n125"
    })

    # Test 3: Power 3
    tests.append({
        'input': "2 1\n2 3\nQUERY 0 1 3",
        'output': "35"
    })

    # Test 4: Mixed powers
    tests.append({
        'input': "3 3\n1 1 1\nQUERY 0 2 1\nQUERY 0 2 2\nQUERY 0 2 3",
        'output': "3\n3\n3"
    })

    return tests

def generate_seg014_tests():
    """K Smallest Prefix Updates"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "5 3\n3 1 4 1 5\nQUERY 0 4 2\nASSIGN 0 2 2\nQUERY 0 4 2",
        'output': "1\n2"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nQUERY 0 0 1\nASSIGN 0 0 10",
        'output': "42"
    })

    # Test 3: K equals length
    tests.append({
        'input': "3 1\n3 1 2\nQUERY 0 2 3",
        'output': "3"
    })

    # Test 4: Negative values
    tests.append({
        'input': "3 2\n-1 -5 -2\nQUERY 0 2 1\nASSIGN 0 1 0",
        'output': "-5"
    })

    return tests

def generate_seg015_tests():
    """Range Min After Toggles"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 4\n5 3 8 2\nQUERY 0 3\nADD 1 2 5\nQUERY 0 3\nFLIP 0 1",
        'output': "2\n8"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 3\n10\nQUERY 0 0\nADD 0 0 5\nFLIP 0 0",
        'output': "10"
    })

    # Test 3: All same
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2\nADD 0 2 3",
        'output': "5"
    })

    # Test 4: Negative values
    tests.append({
        'input': "3 2\n-5 -3 -8\nQUERY 0 2\nADD 1 1 2",
        'output': "-8"
    })

    return tests

def generate_seg016_tests():
    """Dynamic Connectivity Offline"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 5\nADD 0 1\nQUERY 0 1\nADD 1 2\nQUERY 0 2\nREMOVE 0 1",
        'output': "YES\nYES\nNO"
    })

    # Test 2: No edges
    tests.append({
        'input': "3 2\nQUERY 0 1\nQUERY 1 2",
        'output': "NO\nNO"
    })

    # Test 3: Complete graph
    tests.append({
        'input': "3 4\nADD 0 1\nADD 1 2\nADD 0 2\nQUERY 0 2",
        'output': "YES"
    })

    # Test 4: Self loops
    tests.append({
        'input': "2 3\nADD 0 0\nQUERY 0 0\nADD 0 1",
        'output': "YES\nYES"
    })

    return tests

def save_testcases(problem_id, tests):
    """Save test cases in YAML format"""
    output = {
        'samples': tests,
        'public': []
    }

    file_path = f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases/{problem_id}-*.yaml"

    # Find the actual filename
    import glob
    files = glob.glob(file_path)
    if files:
        actual_path = files[0]
    else:
        # Create a reasonable filename
        name_map = {
            'SEG-001': 'range-sum-point-updates-undo',
            'SEG-002': 'range-add-range-sum',
            'SEG-003': 'range-min-range-add',
            'SEG-004': 'inversion-count-updates',
            'SEG-005': 'kth-order-stat-prefix',
            'SEG-006': 'count-values-in-range',
            'SEG-007': 'range-xor-basis',
            'SEG-008': 'longest-increasing-subarray-updates',
            'SEG-009': 'range-t-threshold-majority',
            'SEG-010': 'range-gcd-skip-zones',
            'SEG-011': 'range-min-index',
            'SEG-012': 'range-add-kth-order',
            'SEG-013': 'range-sum-multiple-powers',
            'SEG-014': 'k-smallest-prefix-updates',
            'SEG-015': 'range-min-after-toggles',
            'SEG-016': 'dynamic-connectivity-offline',
        }
        actual_path = f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases/{problem_id}-{name_map.get(problem_id, 'unknown')}.yaml"

    with open(actual_path, 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True)

    print(f"✓ {problem_id}: {len(tests)} test cases saved")

def main():
    generators = [
        ('SEG-001', generate_seg001_tests),
        ('SEG-002', generate_seg002_tests),
        ('SEG-003', generate_seg003_tests),
        ('SEG-004', generate_seg004_tests),
        ('SEG-005', generate_seg005_tests),
        ('SEG-006', generate_seg006_tests),
        ('SEG-007', generate_seg007_tests),
        ('SEG-008', generate_seg008_tests),
        ('SEG-009', generate_seg009_tests),
        ('SEG-010', generate_seg010_tests),
        ('SEG-011', generate_seg011_tests),
        ('SEG-012', generate_seg012_tests),
        ('SEG-013', generate_seg013_tests),
        ('SEG-014', generate_seg014_tests),
        ('SEG-015', generate_seg015_tests),
        ('SEG-016', generate_seg016_tests),
    ]

    print("=" * 60)
    print("GENERATING SEGMENTTREE TEST CASES")
    print("=" * 60)

    for problem_id, generator_func in generators:
        tests = generator_func()
        save_testcases(problem_id, tests)

    print("\n" + "=" * 60)
    print("✓ ALL TEST CASES GENERATED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
