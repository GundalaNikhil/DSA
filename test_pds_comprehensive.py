#!/usr/bin/env python3

import os
import sys
import yaml
import importlib.util
from pathlib import Path
import traceback
import subprocess

# Add the solutions directory to path
SOLUTIONS_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/ProbabilisticDS/solutions/python"
TESTCASES_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/ProbabilisticDS/testcases"
PROBLEMS_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/ProbabilisticDS/problems"

def load_solution(problem_id):
    """Load a solution module dynamically"""
    solutions = list(Path(SOLUTIONS_DIR).glob(f"{problem_id}-*.py"))

    if not solutions:
        return None, f"Solution file not found for {problem_id}"

    solution_path = str(solutions[0])
    spec = importlib.util.spec_from_file_location(problem_id, solution_path)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)
        return module, None
    except Exception as e:
        return None, f"Error loading module: {str(e)}"

def load_testcase(problem_id):
    """Load testcase YAML"""
    testcase_files = list(Path(TESTCASES_DIR).glob(f"{problem_id}-*.yaml"))

    if not testcase_files:
        return None, f"Testcase file not found for {problem_id}"

    testcase_path = str(testcase_files[0])
    try:
        with open(testcase_path, 'r') as f:
            data = yaml.safe_load(f)
        return data, None
    except Exception as e:
        return None, f"Error loading testcase: {str(e)}"

def get_main_function(module, problem_id):
    """Find the main function (not main() but the actual solve/design function)"""
    # Map of problem IDs to likely function names
    function_patterns = {
        'PDS-001': ['design_bloom'],
        'PDS-002': ['counting_bloom', 'design_counting_bloom'],
        'PDS-003': ['cuckoo_hash', 'cuckoo_success'],
        'PDS-004': ['count_min_sketch', 'sketch_frequency'],
        'PDS-005': ['misra_gries'],
        'PDS-006': ['hyperloglog', 'hll_estimate'],
        'PDS-007': ['flajolet_martin', 'flajolet'],
        'PDS-008': ['bottom_k', 'kmv_sample', 'weighted_sample', 'jaccard_estimate'],
        'PDS-009': ['kmv', 'kmv_count', 'kmv_estimate'],
        'PDS-010': ['count_sketch', 'heavy_hitters', 'count_sketch_estimate'],
        'PDS-011': ['sliding_window', 'decayed_distinct'],
        'PDS-012': ['bloomier', 'bloomier_filter'],
        'PDS-013': ['xor_filter', 'xor_build', 'xor_lookup'],
        'PDS-014': ['perfect_hash', 'build_perfect_hash', 'total_size'],
        'PDS-015': ['minhash', 'lsh_probability'],
        'PDS-016': ['hyperloglog_union', 'hll_union', 'hll_union_estimate'],
    }

    patterns = function_patterns.get(problem_id, [])

    # Try patterns first
    for pattern in patterns:
        if hasattr(module, pattern):
            obj = getattr(module, pattern)
            if callable(obj):
                return pattern

    # Look for any callable that's not underscore or main
    for attr in dir(module):
        if not attr.startswith('_') and attr != 'main':
            obj = getattr(module, attr)
            if callable(obj) and not isinstance(obj, type):
                # Skip common imports
                if attr not in ['sys', 'math', 'random', 'collections', 'itertools', 'functools']:
                    return attr

    return None

def parse_complex_input(input_str, problem_id):
    """Parse input which may be multi-line"""
    lines = str(input_str).strip().split('\n')

    # Parse based on problem type
    if problem_id == 'PDS-005':  # Misra-Gries: n k\nstream
        parts1 = lines[0].split()
        n, k = int(parts1[0]), int(parts1[1])
        stream = list(map(int, lines[1].split()))
        return [stream, k]

    elif problem_id == 'PDS-006':  # HyperLogLog: stream items
        return [list(map(int, lines[0].split()))]

    elif problem_id == 'PDS-008':  # Bottom-K: k\nstream
        k = int(lines[0])
        stream = list(map(int, lines[1].split()))
        return [stream, k]

    elif problem_id == 'PDS-009':  # KMV: k\nstream
        k = int(lines[0])
        stream = list(map(int, lines[1].split()))
        return [stream, k]

    elif problem_id == 'PDS-010':  # Count-Sketch: columns rows\nstream
        parts1 = lines[0].split()
        cols, rows = int(parts1[0]), int(parts1[1])
        stream = list(map(int, lines[1].split()))
        return [stream, cols, rows]

    elif problem_id == 'PDS-011':  # Sliding Window: decay threshold window_size\nstream
        parts1 = lines[0].split()
        decay = float(parts1[0])
        threshold = float(parts1[1])
        window_size = int(parts1[2])
        stream = list(map(int, lines[1].split()))
        return [stream, decay, threshold, window_size]

    elif problem_id == 'PDS-014':  # Perfect Hashing: k\nkeys
        k = int(lines[0])
        keys = list(map(int, lines[1].split()))
        return [keys, k]

    elif problem_id == 'PDS-016':  # HyperLogLog Union: stream1\nstream2
        stream1 = list(map(int, lines[0].split()))
        stream2 = list(map(int, lines[1].split()))
        return [stream1, stream2]

    else:
        # Default: parse all as numbers
        return [int(x) if x.replace('.','').replace('-','').isdigit() else x
                for x in str(input_str).split()]

def parse_output(output_str):
    """Parse output string into appropriate types"""
    if not output_str or output_str.strip() == '':
        return []

    parts = str(output_str).split()
    result = []
    for part in parts:
        try:
            if '.' in part or 'e' in part.lower():
                result.append(float(part))
            else:
                result.append(int(part))
        except:
            result.append(part)
    return result if len(result) > 1 else (result[0] if result else [])

def compare_values(result, expected, tolerance=0.001):
    """Compare values with tolerance for floats"""
    # Normalize both to lists for comparison
    if not isinstance(result, list):
        result = [result] if result is not None else []
    if not isinstance(expected, list):
        expected = [expected] if expected is not None else []

    # Check length
    if len(result) != len(expected):
        return False

    # Compare each element
    for r, e in zip(result, expected):
        if isinstance(e, float) and isinstance(r, (int, float)):
            if abs(r - e) >= tolerance:
                return False
        elif isinstance(e, (list, tuple)) and isinstance(r, (list, tuple)):
            if not compare_values(r, e, tolerance):
                return False
        elif r != e:
            return False

    return True

def test_solution(problem_id):
    """Test a single solution"""
    # Load module
    module, error = load_solution(problem_id)
    if error:
        return {"status": "LOAD_ERROR", "error": error, "passed": 0, "total": 0}

    # Load testcase
    testcase, error = load_testcase(problem_id)
    if error:
        return {"status": "TESTCASE_ERROR", "error": error, "passed": 0, "total": 0}

    if not testcase:
        return {"status": "INVALID_TESTCASE", "error": "Empty testcase", "passed": 0, "total": 0}

    # Get hidden test cases (most important for validation)
    test_cases = testcase.get('hidden', [])
    if not test_cases:
        test_cases = testcase.get('public', [])

    if not test_cases:
        return {"status": "NO_TESTS", "error": "No hidden or public test cases", "passed": 0, "total": 0}

    func_name = get_main_function(module, problem_id)
    if not func_name:
        return {"status": "NO_FUNCTION", "error": "No callable function found", "passed": 0, "total": 0}

    func = getattr(module, func_name)
    passed = 0
    failed = []

    for idx, test_case in enumerate(test_cases):
        try:
            input_str = test_case.get('input', '')
            output_str = test_case.get('output', '')

            # Parse input based on problem type
            input_args = parse_complex_input(input_str, problem_id)
            expected = parse_output(output_str)

            # Call function
            if len(input_args) == 1:
                result = func(input_args[0])
            else:
                result = func(*input_args)

            # Parse result if it's a string
            if isinstance(result, str):
                result = parse_output(result)

            # Normalize result
            if isinstance(result, tuple):
                result = list(result)
            if result is not None and not isinstance(result, list):
                result = [result]

            success = compare_values(result, expected, tolerance=0.0001)

            if success:
                passed += 1
            else:
                failed.append({
                    "index": idx,
                    "input": input_str[:100],
                    "expected": output_str,
                    "got": result
                })

        except Exception as e:
            failed.append({
                "index": idx,
                "error": str(e),
                "input": test_case.get('input', '')[:100],
            })

    total = len(test_cases)
    return {
        "status": "OK",
        "passed": passed,
        "total": total,
        "success": passed == total,
        "failures": failed if failed else None
    }

def main():
    print("="*60)
    print("Testing ProbabilisticDS Solutions")
    print("="*60 + "\n")

    # Test all problems
    results = {}
    for i in range(1, 17):
        problem_id = f"PDS-{i:03d}"
        print(f"Testing {problem_id}...", end=" ", flush=True)

        result = test_solution(problem_id)
        results[problem_id] = result

        if result['status'] == 'OK':
            if result['success']:
                print(f"✓ PASSED ({result['passed']}/{result['total']})")
            else:
                print(f"✗ FAILED ({result['passed']}/{result['total']})")
        else:
            print(f"✗ {result['status']}")

    # Summary
    print("\n" + "="*60)
    print("COMPREHENSIVE TEST REPORT")
    print("="*60)

    total_passed = 0
    total_tests = 0
    failures = {}

    for problem_id, result in sorted(results.items()):
        if result['status'] == 'OK':
            total_passed += result['passed']
            total_tests += result['total']
            if not result['success']:
                failures[problem_id] = result['failures']

            status = "✓ PASS" if result['success'] else "✗ FAIL"
            print(f"{problem_id}: {status} ({result['passed']}/{result['total']})")
        else:
            print(f"{problem_id}: {result['status']}")
            if 'error' in result:
                print(f"  Error: {result['error'][:100]}")

    print("="*60)
    if total_tests > 0:
        print(f"Success Rate: {total_passed}/{total_tests} = {100*total_passed/total_tests:.1f}%")
    else:
        print("No tests found!")
    print("="*60)

    if failures:
        print("\nFAILURES DETAILS:")
        print("="*60)
        for problem_id, failure_list in sorted(failures.items()):
            print(f"\n{problem_id}:")
            for failure in failure_list[:2]:  # Show first 2 failures
                print(f"  Test #{failure['index']}:")
                if 'error' in failure:
                    print(f"    Error: {failure['error']}")
                else:
                    print(f"    Input: {failure.get('input', 'N/A')}")
                    print(f"    Expected: {failure.get('expected', 'N/A')}")
                    print(f"    Got: {failure.get('got', 'N/A')}")

if __name__ == "__main__":
    main()
