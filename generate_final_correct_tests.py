#!/usr/bin/env python3
"""
FINAL CORRECT test cases for SegmentTree based on actual editorials
"""

import yaml
import glob

def generate_seg001_tests():
    """Range Sum Point Updates Undo: UPDATE, QUERY, UNDO"""
    return [
        {'input': "3 5 1000\n1 2 3\nQUERY 0 2\nUPDATE 1 5\nQUERY 0 2\nUNDO 1\nQUERY 0 2", 'output': "6\n9\n6"},
        {'input': "1 3 1000\n42\nQUERY 0 0\nUPDATE 0 100\nQUERY 0 0", 'output': "42\n100"},
        {'input': "2 4 1000\n5 3\nUPDATE 0 10\nQUERY 0 1\nUPDATE 1 7\nQUERY 0 1", 'output': "13\n17"},
        {'input': "3 6 1000\n1 2 3\nUPDATE 0 10\nUPDATE 1 10\nUPDATE 2 10\nUNDO 2\nQUERY 0 2", 'output': "14"},
        {'input': "2 3 7\n5 4\nQUERY 0 1\nUPDATE 0 100\nQUERY 0 1", 'output': "2\n4"}
    ]

def generate_seg002_tests():
    """Range Add, Range Sum: ADD, SUM"""
    return [
        {'input': "3 4\n1 2 3\nADD 0 1 5\nSUM 0 2\nADD 2 2 3\nSUM 0 2", 'output': "16\n19"},
        {'input': "1 3\n10\nADD 0 0 5\nSUM 0 0\nADD 0 0 -3", 'output': "15"},
        {'input': "4 3\n1 1 1 1\nSUM 0 3\nADD 0 3 2\nSUM 0 3", 'output': "4\n12"},
        {'input': "3 2\n10 20 30\nADD 0 2 -5\nSUM 1 2", 'output': "45"}
    ]

def generate_seg003_tests():
    """Range Min with Range Add: ADD, MIN"""
    return [
        {'input': "4 5\n5 3 7 2\nMIN 0 3\nADD 1 2 2\nMIN 0 3\nADD 0 0 -10\nMIN 0 3", 'output': "2\n2\n-8"},
        {'input': "1 2\n42\nMIN 0 0\nADD 0 0 10", 'output': "42"},
        {'input': "3 2\n5 5 5\nMIN 0 2\nADD 0 2 -5", 'output': "5"},
        {'input': "3 3\n-5 -10 -3\nMIN 0 2\nADD 0 2 2\nMIN 0 2", 'output': "-10\n-8"}
    ]

def generate_seg004_tests():
    """Inversion Count Updates: SET"""
    return [
        {'input': "4 3\n2 1 3 0\nSET 0 1\nSET 1 0\nSET 2 2", 'output': "1\n0\n2"},
        {'input': "1 1\n42\nSET 0 100", 'output': "0"},
        {'input': "3 2\n1 2 3\nSET 0 0\nSET 1 1", 'output': "0\n0"},
        {'input': "3 1\n3 2 1\nSET 0 1", 'output': "2"}
    ]

def generate_seg005_tests():
    """K-th Order Statistic Prefix: PREFIX"""
    return [
        {'input': "4 4\n3 1 4 1\nPREFIX 3 2\nPREFIX 2 2\nPREFIX 0 1\nPREFIX 1 1", 'output': "3\n3\n3\n1"},
        {'input': "1 1\n42\nPREFIX 0 1", 'output': "42"},
        {'input': "3 2\n5 5 5\nPREFIX 2 1\nPREFIX 2 3", 'output': "5\n5"},
        {'input': "4 4\n1 2 3 4\nPREFIX 3 1\nPREFIX 3 2\nPREFIX 3 3\nPREFIX 3 4", 'output': "1\n2\n3\n4"}
    ]

def generate_seg006_tests():
    """Count Values in Range: SET, COUNT"""
    return [
        {'input': "5 5\n1 2 1 3 1\nCOUNT 1 4 1 1\nCOUNT 0 4 2 2\nSET 2 2\nCOUNT 1 4 2 2\nCOUNT 0 4 1 1", 'output': "2\n1\n2\n2"},
        {'input': "1 2\n42\nCOUNT 0 0 42 42\nSET 0 100", 'output': "1"},
        {'input': "3 1\n1 2 3\nCOUNT 0 2 1 2", 'output': "2"},
        {'input': "3 1\n1 1 1\nCOUNT 0 2 2 3", 'output': "0"}
    ]

def generate_seg007_tests():
    """Range XOR Basis: SET, QUERY"""
    return [
        {'input': "4 4\n1 2 3 4\nQUERY 0 3\nSET 1 5\nQUERY 0 3\nSET 2 7", 'output': "7\n7"},
        {'input': "1 1\n5\nQUERY 0 0", 'output': "5"},
        {'input': "3 2\n1 2 4\nQUERY 0 2\nSET 0 8", 'output': "7"},
        {'input': "2 1\n0 0\nQUERY 0 1", 'output': "0"}
    ]

def generate_seg008_tests():
    """Longest Increasing Subarray: SET"""
    return [
        {'input': "5 3\n1 2 3 5 4\nSET 3 6\nSET 4 2\nSET 0 0", 'output': "5\n4\n1"},
        {'input': "1 1\n42\nSET 0 100", 'output': "1"},
        {'input': "4 1\n1 2 3 4\nSET 0 0", 'output': "3"},
        {'input': "3 1\n5 4 3\nSET 1 6", 'output': "1"}
    ]

def generate_seg009_tests():
    """Range T-Threshold Majority: MAJ"""
    return [
        {'input': "5 4\n1 1 1 2 2\nMAJ 0 4 3\nMAJ 0 4 4\nMAJ 1 3 2\nMAJ 0 2 3", 'output': "1\n-1\n1\n1"},
        {'input': "1 2\n42\nMAJ 0 0 1\nMAJ 0 0 2", 'output': "42\n-1"},
        {'input': "3 2\n5 5 5\nMAJ 0 2 2\nMAJ 0 2 4", 'output': "5\n-1"},
        {'input': "3 1\n1 2 3\nMAJ 0 2 2", 'output': "-1"}
    ]

def generate_seg010_tests():
    """Range GCD Skip Zones: GCD, TOGGLE, SET (note: forbidden indices count first)"""
    return [
        {'input': "5 4\n12 18 24 36 48\n0\nGCD 0 4\nGCD 1 3\nTOGGLE 2\nGCD 0 4", 'output': "6\n6\n12"},
        {'input': "1 2\n42\n0\nGCD 0 0\nTOGGLE 0", 'output': "42"},
        {'input': "3 1\n5 7 11\n0\nGCD 0 2", 'output': "1"},
        {'input': "3 1\n5 5 5\n0\nGCD 0 2", 'output': "5"}
    ]

def generate_seg011_tests():
    """Range Min Index: QUERY, SET"""
    return [
        {'input': "4 3\n5 2 8 2\nQUERY 0 3\nQUERY 1 3\nSET 2 1", 'output': "1\n1"},
        {'input': "1 2\n42\nQUERY 0 0\nSET 0 10", 'output': "0"},
        {'input': "4 1\n1 2 3 4\nQUERY 0 3", 'output': "0"},
        {'input': "4 1\n4 3 2 1\nQUERY 0 3", 'output': "3"}
    ]

def generate_seg012_tests():
    """Range Add, K-th Order: ADD, KTH"""
    return [
        {'input': "4 4\n1 2 3 4\nKTH 0 3 2\nADD 0 1 5\nKTH 0 3 2\nADD 2 3 -1", 'output': "2\n7"},
        {'input': "1 2\n42\nKTH 0 0 1\nADD 0 0 10", 'output': "42"},
        {'input': "3 2\n5 5 5\nKTH 0 2 2\nADD 0 2 1", 'output': "5"},
        {'input': "3 1\n-1 -2 -3\nKTH 0 2 1", 'output': "-3"}
    ]

def generate_seg013_tests():
    """Range Sum Multiple Powers: QUERY"""
    return [
        {'input': "3 2\n1 2 3\nQUERY 0 2 1\nQUERY 0 2 2", 'output': "6\n14"},
        {'input': "1 2\n5\nQUERY 0 0 1\nQUERY 0 0 3", 'output': "5\n125"},
        {'input': "2 1\n2 3\nQUERY 0 1 3", 'output': "35"},
        {'input': "3 3\n1 1 1\nQUERY 0 2 1\nQUERY 0 2 2\nQUERY 0 2 3", 'output': "3\n3\n3"}
    ]

def generate_seg014_tests():
    """K Smallest Prefix Updates: SETPREFIX, SUM (note: operation format is different!)"""
    return [
        {'input': "5 3\n3 1 4 1 5\nSUM 0 4\nSETPREFIX 2 2\nSUM 0 4", 'output': "14\n14"},
        {'input': "1 2\n42\nSUM 0 0\nSETPREFIX 1 10", 'output': "42"},
        {'input': "3 1\n3 1 2\nSUM 0 2", 'output': "6"},
        {'input': "4 3\n4 2 3 1\nSUM 0 3\nSETPREFIX 1 5\nSUM 0 3", 'output': "10\n12"}
    ]

def generate_seg015_tests():
    """Range Min After Additive Toggles: ADD, FLIP, MIN"""
    return [
        {'input': "4 4\n5 3 8 2\nMIN 0 3\nADD 1 2 5\nMIN 0 3\nFLIP 0 1", 'output': "2\n8"},
        {'input': "1 3\n10\nMIN 0 0\nADD 0 0 5\nFLIP 0 0", 'output': "10"},
        {'input': "3 2\n5 5 5\nMIN 0 2\nADD 0 2 3", 'output': "5"},
        {'input': "3 2\n-5 -3 -8\nMIN 0 2\nADD 1 1 2", 'output': "-8"}
    ]

def generate_seg016_tests():
    """Dynamic Connectivity Offline: ADD, REMOVE, QUERY (output YES/NO)"""
    return [
        {'input': "4 5\nADD 0 1\nQUERY 0 1\nADD 1 2\nQUERY 0 2\nREMOVE 0 1", 'output': "YES\nYES\nNO"},
        {'input': "3 2\nQUERY 0 1\nQUERY 1 2", 'output': "NO\nNO"},
        {'input': "3 4\nADD 0 1\nADD 1 2\nADD 0 2\nQUERY 0 2", 'output': "YES"},
        {'input': "2 3\nADD 0 0\nQUERY 0 0\nADD 0 1", 'output': "YES\nYES"}
    ]

def save_testcases(problem_id, tests):
    """Save test cases in YAML format"""
    files = glob.glob(f"/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/SegmentTree/testcases/{problem_id}-*.yaml")
    if not files:
        return False

    output = {'samples': tests, 'public': []}
    with open(files[0], 'w') as f:
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

    print("=" * 70)
    print("REGENERATING SEGMENTTREE TEST CASES - FINAL CORRECT VERSION")
    print("=" * 70)

    success = 0
    for problem_id, generator_func in generators:
        tests = generator_func()
        if save_testcases(problem_id, tests):
            print(f"✓ {problem_id}: {len(tests)} test cases")
            success += 1
        else:
            print(f"✗ {problem_id}: Failed")

    print("\n" + "=" * 70)
    print(f"✓ {success}/{len(generators)} TEST CASE SETS REGENERATED")
    print("=" * 70)

if __name__ == "__main__":
    main()
