#!/usr/bin/env python3
"""
Verify the expanded test cases for PRB-014, PRB-015, and PRB-016.
"""

import yaml
import math

def load_yaml_testcases(filepath):
    """Load test cases from YAML file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Parse manually since we have custom format
    lines = content.split('\n')
    cases = []
    current_case = None
    current_field = None
    
    for line in lines:
        if line.startswith('- input:'):
            if current_case:
                cases.append(current_case)
            current_case = {'input': '', 'output': ''}
            current_field = 'input'
        elif line.startswith('  output:'):
            current_field = 'output'
        elif line.startswith('    ') and current_case:
            content_line = line[4:]  # Remove 4-space indent
            if current_case[current_field]:
                current_case[current_field] += '\n' + content_line
            else:
                current_case[current_field] = content_line
    
    if current_case:
        cases.append(current_case)
    
    return cases


# ============================================================================
# PRB-014: Randomized MST Verification
# ============================================================================

def verify_prb014(filepath):
    """Verify PRB-014 test cases."""
    print("\n" + "="*80)
    print("VERIFYING PRB-014: Randomized MST Verification")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    
    def min_trials_mst(n, C):
        p = 1.0 / (n * n)
        if C >= 1.0 or C <= 0.0:
            return None
        num = math.log(1.0 - C)
        den = math.log(1.0 - p)
        t = num / den
        return math.ceil(t)
    
    passed = 0
    failed = 0
    
    for i, case in enumerate(cases, 1):
        try:
            parts = case['input'].strip().split()
            n = int(parts[0])
            C = float(parts[1])
            expected = int(case['output'].strip())
            
            actual = min_trials_mst(n, C)
            
            if actual == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: n={n}, C={C}")
                print(f"   Expected: {expected}")
                print(f"   Actual: {actual}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# PRB-015: Median of Uniforms CLT
# ============================================================================

def verify_prb015(filepath):
    """Verify PRB-015 test cases."""
    print("\n" + "="*80)
    print("VERIFYING PRB-015: Median of Uniforms CLT")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    
    def median_clt(n):
        mean = 0.5
        variance = 1.0 / (4.0 * n)
        return mean, variance
    
    passed = 0
    failed = 0
    tolerance = 1e-5
    
    for i, case in enumerate(cases, 1):
        try:
            n = int(case['input'].strip())
            output_parts = case['output'].strip().split()
            expected_mean = float(output_parts[0])
            expected_var = float(output_parts[1])
            
            actual_mean, actual_var = median_clt(n)
            
            mean_match = abs(actual_mean - expected_mean) < tolerance
            var_match = abs(actual_var - expected_var) < tolerance
            
            if mean_match and var_match:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: n={n}")
                print(f"   Expected: mean={expected_mean:.6f}, var={expected_var:.6f}")
                print(f"   Actual: mean={actual_mean:.6f}, var={actual_var:.6f}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# PRB-016: Random Permutation Cycle Structure
# ============================================================================

def verify_prb016(filepath):
    """Verify PRB-016 test cases."""
    print("\n" + "="*80)
    print("VERIFYING PRB-016: Random Permutation Cycle Structure")
    print("="*80)
    
    cases = load_yaml_testcases(filepath)
    
    def cycle_expectations(n, k):
        expected_cycles_k = 1.0 / k
        expected_longest = 0.624330 * n
        return expected_cycles_k, expected_longest
    
    passed = 0
    failed = 0
    tolerance = 1e-5
    
    for i, case in enumerate(cases, 1):
        try:
            input_parts = case['input'].strip().split()
            n = int(input_parts[0])
            k = int(input_parts[1])
            
            output_parts = case['output'].strip().split()
            expected_cycles = float(output_parts[0])
            expected_longest = float(output_parts[1])
            
            actual_cycles, actual_longest = cycle_expectations(n, k)
            
            cycles_match = abs(actual_cycles - expected_cycles) < tolerance
            longest_match = abs(actual_longest - expected_longest) < tolerance
            
            if cycles_match and longest_match:
                passed += 1
            else:
                failed += 1
                print(f"❌ Case {i} FAILED:")
                print(f"   Input: n={n}, k={k}")
                print(f"   Expected: cycles={expected_cycles:.6f}, longest={expected_longest:.6f}")
                print(f"   Actual: cycles={actual_cycles:.6f}, longest={actual_longest:.6f}")
        except Exception as e:
            failed += 1
            print(f"❌ Case {i} ERROR: {e}")
    
    print(f"\n✅ Passed: {passed}/{len(cases)}")
    print(f"❌ Failed: {failed}/{len(cases)}")
    print(f"📊 Pass Rate: {100*passed/len(cases):.1f}%")
    
    return passed == len(cases)


# ============================================================================
# Main Verification
# ============================================================================

def main():
    """Run all verifications."""
    print("="*80)
    print("VERIFICATION OF EXPANDED PROBABILISTIC TEST CASES")
    print("="*80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Probabilistic/testcases"
    
    results = {}
    
    # PRB-014
    prb014_path = f"{base_path}/PRB-014-randomized-mst-verification.yaml"
    results['PRB-014'] = verify_prb014(prb014_path)
    
    # PRB-015
    prb015_path = f"{base_path}/PRB-015-median-uniforms-clt.yaml"
    results['PRB-015'] = verify_prb015(prb015_path)
    
    # PRB-016
    prb016_path = f"{base_path}/PRB-016-permutation-cycle-structure.yaml"
    results['PRB-016'] = verify_prb016(prb016_path)
    
    # Summary
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    
    all_passed = all(results.values())
    
    for problem, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{problem}: {status}")
    
    print("\n" + "="*80)
    if all_passed:
        print("🎉 ALL VERIFICATIONS PASSED!")
        print("✅ All expanded test cases are correct and ready for production.")
    else:
        print("⚠️ Some verifications failed. Please review the errors above.")
    print("="*80)


if __name__ == "__main__":
    main()
