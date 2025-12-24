#!/usr/bin/env python3
"""
Test AGR solutions against all test cases.
Extracts Python solutions from editorials and runs all test cases.
"""
import os
import re
import sys
import yaml
import subprocess
import tempfile
from pathlib import Path


def extract_python_solution(editorial_file):
    """Extract Python solution from editorial markdown."""
    with open(editorial_file, 'r') as f:
        content = f.read()
    
    # Find Python code block in editorial
    pattern = r'### Python\n\n```python\n(.*?)\n```'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None
    
    return match.group(1)


def run_test_case(solution_code, test_input):
    """Run a single test case through the solution."""
    # Create temporary file with solution
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(solution_code)
        temp_file = f.name
    
    try:
        # Run the solution with test input
        result = subprocess.run(
            ['python3', temp_file],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        return result.stdout.strip(), result.stderr
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:
        return None, str(e)
    finally:
        os.unlink(temp_file)


def test_problem(prob_id):
    """Test all test cases for a single problem."""
    # Find files using glob
    editorial_files = list(Path('editorials').glob(f'{prob_id}*.md'))
    testcase_files = list(Path('testcases').glob(f'{prob_id}*.yaml'))
    
    if not editorial_files or not testcase_files:
        return {'status': 'FILES_NOT_FOUND', 'passed': 0, 'failed': 0, 'errors': []}
    
    editorial_file = editorial_files[0]
    testcase_file = testcase_files[0]
    
    # Extract solution
    solution_code = extract_python_solution(editorial_file)
    if not solution_code:
        return {'status': 'NO_SOLUTION', 'passed': 0, 'failed': 0, 'errors': []}
    
    # Load test cases
    with open(testcase_file, 'r') as f:
        tc_data = yaml.safe_load(f)
    
    # Run all test cases
    results = {'status': 'OK', 'passed': 0, 'failed': 0, 'errors': []}
    
    for category in ['samples', 'public', 'hidden']:
        if category not in tc_data:
            continue
        
        for idx, tc in enumerate(tc_data[category]):
            tc_id = f"{category}[{idx}]"
            test_input = tc['input']
            expected_output = tc['output'].strip()
            
            actual_output, error = run_test_case(solution_code, test_input)
            
            if error:
                results['failed'] += 1
                results['errors'].append({
                    'tc_id': tc_id,
                    'error': error,
                    'type': 'RUNTIME_ERROR'
                })
            elif actual_output != expected_output:
                results['failed'] += 1
                results['errors'].append({
                    'tc_id': tc_id,
                    'expected': expected_output[:100],
                    'actual': actual_output[:100] if actual_output else 'None',
                    'type': 'WRONG_ANSWER'
                })
            else:
                results['passed'] += 1
    
    return results


def main():
    print("="*80)
    print("AGR TEST CASE VALIDATION AGAINST EDITORIAL SOLUTIONS")
    print("="*80)
    
    all_results = {}
    total_passed = 0
    total_failed = 0
    
    for i in range(1, 17):
        prob_id = f'AGR-{i:03d}'
        
        # Find the editorial file
        editorial_files = list(Path('editorials').glob(f'{prob_id}*.md'))
        if not editorial_files:
            print(f"\n{prob_id}: ⚠️  Editorial not found")
            continue
        
        print(f"\n{prob_id}: Testing...")
        
        try:
            results = test_problem(prob_id)
            all_results[prob_id] = results
            
            total_passed += results['passed']
            total_failed += results['failed']
            
            if results['status'] == 'NO_SOLUTION':
                print(f"  ⚠️  No Python solution found in editorial")
            elif results['failed'] == 0:
                print(f"  ✅ Passed: {results['passed']}/{results['passed']}")
            else:
                print(f"  ❌ Passed: {results['passed']}, Failed: {results['failed']}")
                for error in results['errors'][:3]:  # Show first 3 errors
                    print(f"     - {error['tc_id']}: {error['type']}")
                    if error['type'] == 'WRONG_ANSWER':
                        print(f"       Expected: {error['expected'][:50]}...")
                        print(f"       Actual:   {error['actual'][:50]}...")
        
        except Exception as e:
            print(f"  ❌ Error: {e}")
            all_results[prob_id] = {'status': 'ERROR', 'error': str(e)}
    
    # Summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"\nTotal Test Cases: {total_passed + total_failed}")
    print(f"✅ Passed: {total_passed}")
    print(f"❌ Failed: {total_failed}")
    
    if total_failed == 0:
        print(f"\n🎉 ALL TEST CASES PASSED!")
    else:
        print(f"\n⚠️  {total_failed} test cases failed")
        print(f"\nProblems with failures:")
        for prob_id, results in all_results.items():
            if results.get('failed', 0) > 0:
                print(f"  {prob_id}: {results['failed']} failures")


if __name__ == '__main__':
    os.chdir('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs')
    main()
