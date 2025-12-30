#!/usr/bin/env python3
"""
Test all GameTheory Python solutions against hidden test cases
"""

import sys
import os
import yaml
import subprocess
from pathlib import Path

def load_testcases(yaml_path):
    """Load test cases from YAML file"""
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    return data

def run_solution(solution_path, input_data):
    """Run a Python solution with given input"""
    try:
        result = subprocess.run(
            ['python3', solution_path],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip(), result.stderr
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:
        return None, str(e)

def test_problem(problem_id, base_path):
    """Test a single problem"""
    solution_path = base_path / 'dsa-problems' / 'GameTheory' / 'solutions' / 'python' / f'{problem_id}.py'
    testcase_path = base_path / 'dsa-problems' / 'GameTheory' / 'testcases' / f'{problem_id}.yaml'
    
    if not solution_path.exists():
        return None, f"Solution not found: {solution_path}"
    
    if not testcase_path.exists():
        return None, f"Testcase not found: {testcase_path}"
    
    # Load test cases
    testcases = load_testcases(testcase_path)
    
    results = {
        'sample': {'passed': 0, 'total': 0, 'failures': []},
        'public': {'passed': 0, 'total': 0, 'failures': []},
        'hidden': {'passed': 0, 'total': 0, 'failures': []}
    }
    
    # Test sample cases
    for idx, tc in enumerate(testcases.get('samples', []), 1):
        results['sample']['total'] += 1
        input_data = tc['input']
        expected = tc['output'].strip()
        actual, error = run_solution(solution_path, input_data)
        
        if error:
            results['sample']['failures'].append({
                'test': idx,
                'input': input_data,
                'expected': expected,
                'error': error
            })
        elif actual != expected:
            results['sample']['failures'].append({
                'test': idx,
                'input': input_data,
                'expected': expected,
                'got': actual
            })
        else:
            results['sample']['passed'] += 1
    
    # Test public cases
    for idx, tc in enumerate(testcases.get('public', []), 1):
        results['public']['total'] += 1
        input_data = tc['input']
        expected = tc['output'].strip()
        actual, error = run_solution(solution_path, input_data)
        
        if error:
            results['public']['failures'].append({
                'test': idx,
                'input': input_data,
                'expected': expected,
                'error': error
            })
        elif actual != expected:
            results['public']['failures'].append({
                'test': idx,
                'input': input_data,
                'expected': expected,
                'got': actual
            })
        else:
            results['public']['passed'] += 1
    
    # Test hidden cases
    for idx, tc in enumerate(testcases.get('hidden', []), 1):
        results['hidden']['total'] += 1
        input_data = tc['input']
        expected = tc['output'].strip()
        actual, error = run_solution(solution_path, input_data)
        
        if error:
            results['hidden']['failures'].append({
                'test': idx,
                'input': input_data[:100] + ('...' if len(input_data) > 100 else ''),
                'expected': expected,
                'error': error
            })
        elif actual != expected:
            results['hidden']['failures'].append({
                'test': idx,
                'input': input_data[:100] + ('...' if len(input_data) > 100 else ''),
                'expected': expected,
                'got': actual
            })
        else:
            results['hidden']['passed'] += 1
    
    return results, None

def main():
    base_path = Path(__file__).parent
    
    # List of all GameTheory problems
    problems = [
        'GMT-001-pile-split-choice',
        'GMT-002-token-walk-directed-graph',
        'GMT-003-subtract-square-ban-list',
        'GMT-004-circular-nim-variant',
        'GMT-005-interval-removal-game',
        'GMT-006-divisor-turn-game',
        'GMT-007-grid-chomp-poison',
        'GMT-008-kayles-on-graph',
        'GMT-009-take-or-split-heap',
        'GMT-010-removal-game-strings',
        'GMT-011-blocking-tokens-dag',
        'GMT-012-rectangular-chocolate-cut',
        'GMT-013-matrix-removal-game',
        'GMT-014-greedy-coin-split-game',
        'GMT-015-turning-turtles',
        'GMT-016-nim-with-move-limit'
    ]
    
    all_passed = True
    failed_problems = []
    
    print("=" * 80)
    print("TESTING GAMETHEORY PYTHON SOLUTIONS")
    print("=" * 80)
    print()
    
    for problem_id in problems:
        print(f"Testing {problem_id}...")
        results, error = test_problem(problem_id, base_path)
        
        if error:
            print(f"❌ ERROR: {error}")
            all_passed = False
            failed_problems.append(problem_id)
            continue
        
        sample_pass = results['sample']['passed'] == results['sample']['total']
        public_pass = results['public']['passed'] == results['public']['total']
        hidden_pass = results['hidden']['passed'] == results['hidden']['total']
        
        if sample_pass and public_pass and hidden_pass:
            print(f"✅ PASS {problem_id}")
            print(f"    Sample: {results['sample']['passed']}/{results['sample']['total']}")
            print(f"    Public: {results['public']['passed']}/{results['public']['total']}")
            print(f"    Hidden: {results['hidden']['passed']}/{results['hidden']['total']}")
        else:
            print(f"❌ FAIL {problem_id}")
            print(f"    Sample: {results['sample']['passed']}/{results['sample']['total']}")
            print(f"    Public: {results['public']['passed']}/{results['public']['total']}")
            print(f"    Hidden: {results['hidden']['passed']}/{results['hidden']['total']}")
            
            all_passed = False
            failed_problems.append(problem_id)
            
            # Show failures
            for category in ['sample', 'public', 'hidden']:
                if results[category]['failures']:
                    print(f"\n    {category.upper()} FAILURES:")
                    for failure in results[category]['failures'][:3]:  # Show first 3 failures
                        print(f"      Test {failure['test']}:")
                        print(f"        Input: {failure['input'][:80]}")
                        print(f"        Expected: {failure.get('expected', 'N/A')}")
                        if 'error' in failure:
                            print(f"        Error: {failure['error']}")
                        else:
                            print(f"        Got: {failure.get('got', 'N/A')}")
        print()
    
    print("=" * 80)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
    else:
        print(f"❌ {len(failed_problems)} PROBLEM(S) FAILED:")
        for p in failed_problems:
            print(f"  - {p}")
    print("=" * 80)
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())
