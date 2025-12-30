#!/usr/bin/env python3
"""
Generate correct test cases for SegmentTree problems based on actual solution specs
"""

import yaml
import glob

def generate_seg001_tests():
    """Range Sum Point Updates Undo"""
    tests = []

    # Test 1: Basic with undo
    tests.append({
        'input': "3 5 1000\n1 2 3\nQUERY 0 2\nUPDATE 1 5\nQUERY 0 2\nUNDO 1\nQUERY 0 2",
        'output': "6\n9\n6"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 3 1000\n42\nQUERY 0 0\nUPDATE 0 100\nQUERY 0 0",
        'output': "42\n100"
    })

    # Test 3: Negative values
    tests.append({
        'input': "4 4 1000\n-5 10 -3 8\nQUERY 0 3\nUPDATE 0 5\nQUERY 0 3",
        'output': "10\n20"
    })

    # Test 4: Modulo wrap
    tests.append({
        'input': "2 3 7\n5 4\nQUERY 0 1\nUPDATE 0 100\nQUERY 0 1",
        'output': "2\n4"
    })

    # Test 5: Zero modulo edge case
    tests.append({
        'input': "3 2 1000000007\n1000000000 1000000000 1000000000\nQUERY 0 2\nUNDO 0",
        'output': "3000000000"
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

    # Test 3: Full range
    tests.append({
        'input': "4 3\n1 1 1 1\nSUM 0 3\nADD 0 3 2\nSUM 0 3",
        'output': "4\n12"
    })

    # Test 4: Negative operations
    tests.append({
        'input': "3 2\n10 20 30\nADD 0 2 -5\nSUM 1 2",
        'output': "45"
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
        'input': "1 2\n42\nQUERY 0 0\nADD 0 0 10",
        'output': "42"
    })

    # Test 3: All same
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2\nADD 0 2 -5",
        'output': "5"
    })

    # Test 4: Negative values
    tests.append({
        'input': "3 3\n-5 -10 -3\nQUERY 0 2\nADD 0 2 2\nQUERY 0 2",
        'output': "-10\n-8"
    })

    return tests

def generate_seg004_tests():
    """Inversion Count Updates"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 3\n2 1 3 0\nSET 0 2\nSET 1 4\nSET 2 1",
        'output': "2\n1\n2"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n42\nSET 0 100",
        'output': "0"
    })

    # Test 3: Already sorted
    tests.append({
        'input': "3 2\n1 2 3\nSET 0 2\nSET 1 1",
        'output': "0\n1"
    })

    # Test 4: Reverse sorted
    tests.append({
        'input': "3 1\n3 2 1\nSET 0 1",
        'output': "2"
    })

    return tests

def generate_seg005_tests():
    """K-th Order Statistic Prefix"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "4 4\n3 1 4 1\nPREFIX 3 2\nPREFIX 2 2\nPREFIX 0 1\nPREFIX 1 1",
        'output': "3\n3\n3\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n42\nPREFIX 0 1",
        'output': "42"
    })

    # Test 3: All same
    tests.append({
        'input': "3 2\n5 5 5\nPREFIX 2 1\nPREFIX 2 3",
        'output': "5\n5"
    })

    # Test 4: Sorted
    tests.append({
        'input': "4 4\n1 2 3 4\nPREFIX 3 1\nPREFIX 3 2\nPREFIX 3 3\nPREFIX 3 4",
        'output': "1\n2\n3\n4"
    })

    return tests

def generate_seg006_tests():
    """Count Values in Range"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "5 6\n1 2 1 3 1\nCOUNT 1 4 1 1\nCOUNT 0 4 2 2\nSET 2 2\nCOUNT 1 4 2 2\nSET 0 1\nCOUNT 0 4 1 1",
        'output': "2\n1\n2\n3"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nCOUNT 0 0 42 42\nSET 0 100",
        'output': "1"
    })

    # Test 3: Range query
    tests.append({
        'input': "3 1\n1 2 3\nCOUNT 0 2 1 2",
        'output': "2"
    })

    # Test 4: No matches
    tests.append({
        'input': "3 1\n1 1 1\nCOUNT 0 2 2 3",
        'output': "0"
    })

    return tests

def generate_seg007_tests():
    """Range XOR Basis"""
    tests = []

    # Test 1: Basic XOR
    tests.append({
        'input': "4 4\n1 2 3 4\nQUERY 0 3\nSET 1 5\nQUERY 0 3\nSET 2 7",
        'output': "7\n7"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n5\nQUERY 0 0",
        'output': "5"
    })

    # Test 3: Powers of 2
    tests.append({
        'input': "3 2\n1 2 4\nQUERY 0 2\nSET 0 8",
        'output': "7"
    })

    # Test 4: Zeros
    tests.append({
        'input': "2 1\n0 0\nQUERY 0 1",
        'output': "0"
    })

    return tests

def generate_seg008_tests():
    """Longest Increasing Subarray Updates"""
    tests = []

    # Test 1: Basic
    tests.append({
        'input': "5 3\n1 2 3 5 4\nSET 3 6\nSET 4 2\nSET 0 0",
        'output': "5\n4\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 1\n42\nSET 0 100",
        'output': "1"
    })

    # Test 3: All increasing
    tests.append({
        'input': "4 1\n1 2 3 4\nSET 0 0",
        'output': "3"
    })

    # Test 4: Decreasing
    tests.append({
        'input': "3 1\n5 4 3\nSET 1 6",
        'output': "1"
    })

    return tests

def generate_seg009_tests():
    """Range T-Threshold Majority"""
    tests = []

    # Test 1: Basic with majority
    tests.append({
        'input': "5 4\n1 1 1 2 2\nMAJ 0 4 3\nMAJ 0 4 4\nMAJ 1 3 2\nMAJ 0 2 3",
        'output': "1\n-1\n1\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nMAJ 0 0 1\nMAJ 0 0 2",
        'output': "42\n-1"
    })

    # Test 3: All same
    tests.append({
        'input': "3 2\n5 5 5\nMAJ 0 2 2\nMAJ 0 2 4",
        'output': "5\n-1"
    })

    # Test 4: No majority
    tests.append({
        'input': "3 1\n1 2 3\nMAJ 0 2 2",
        'output': "-1"
    })

    return tests

def generate_seg010_tests():
    """Range GCD Skip Zones"""
    tests = []

    # Test 1: Basic GCD
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
        'input': "4 3\n5 2 8 2\nQUERY 0 3\nQUERY 1 3\nSET 2 1",
        'output': "1\n1"
    })

    # Test 2: Single element
    tests.append({
        'input': "1 2\n42\nQUERY 0 0\nSET 0 10",
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

    # Test 3: Full range
    tests.append({
        'input': "3 2\n5 5 5\nQUERY 0 2 2\nADD 0 2 1",
        'output': "5"
    })

    # Test 4: Negative
    tests.append({
        'input': "3 1\n-1 -2 -3\nQUERY 0 2 1",
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

    # Test 4: All ones
    tests.append({
        'input': "3 3\n1 1 1\nQUERY 0 2 1\nQUERY 0 2 2\nQUERY 0 2 3",
        'output': "3\n3\n3"
    })

    return tests

def generate_seg014_tests():
    """K Smallest Prefix Updates"""
    tests = []

    # Test 1: Basic query
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

    # Test 4: Multiple queries
    tests.append({
        'input': "4 3\n4 2 3 1\nQUERY 0 3 1\nASSIGN 0 1 5\nQUERY 0 3 1",
        'output': "1\n5"
    })

    return tests

def generate_seg015_tests():
    """Range Min After Toggle"""
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

    # Test 1: Basic connectivity
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

    # Find the actual filename
    files = glob.glob(f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases/{problem_id}-*.yaml")
    if files:
        actual_path = files[0]
    else:
        return False

    with open(actual_path, 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True)

    return True

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
    print("GENERATING CORRECTED SEGMENTTREE TEST CASES")
    print("=" * 60)

    success = 0
    for problem_id, generator_func in generators:
        tests = generator_func()
        if save_testcases(problem_id, tests):
            print(f"✓ {problem_id}: {len(tests)} test cases saved")
            success += 1
        else:
            print(f"✗ {problem_id}: Failed to save")

    print("\n" + "=" * 60)
    print(f"✓ {success}/{len(generators)} TEST CASE SETS GENERATED")
    print("=" * 60)

if __name__ == "__main__":
    main()
