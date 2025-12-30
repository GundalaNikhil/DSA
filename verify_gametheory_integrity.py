#!/usr/bin/env python3
"""
Comprehensive verification of GameTheory module integrity
"""

import os
from pathlib import Path
import yaml

def verify_gametheory_module():
    base_path = Path('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/GameTheory')
    
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
    
    print("=" * 80)
    print("GAMETHEORY MODULE INTEGRITY CHECK")
    print("=" * 80)
    print()
    
    all_good = True
    
    for problem_id in problems:
        print(f"Checking {problem_id}...")
        
        # Check problem statement
        problem_file = base_path / 'problems' / f'{problem_id}.md'
        if not problem_file.exists():
            print(f"  ❌ Missing problem statement")
            all_good = False
        else:
            print(f"  ✅ Problem statement exists ({problem_file.stat().st_size} bytes)")
        
        # Check editorial
        editorial_file = base_path / 'editorials' / f'{problem_id}.md'
        if not editorial_file.exists():
            print(f"  ❌ Missing editorial")
            all_good = False
        else:
            print(f"  ✅ Editorial exists ({editorial_file.stat().st_size} bytes)")
        
        # Check test cases
        testcase_file = base_path / 'testcases' / f'{problem_id}.yaml'
        if not testcase_file.exists():
            print(f"  ❌ Missing test cases")
            all_good = False
        else:
            with open(testcase_file, 'r') as f:
                tc_data = yaml.safe_load(f)
            public_count = len(tc_data.get('public', []))
            hidden_count = len(tc_data.get('hidden', []))
            print(f"  ✅ Test cases exist (Public: {public_count}, Hidden: {hidden_count})")
        
        # Check Python solution
        py_solution = base_path / 'solutions' / 'python' / f'{problem_id}.py'
        if not py_solution.exists():
            print(f"  ❌ Missing Python solution")
            all_good = False
        else:
            print(f"  ✅ Python solution exists ({py_solution.stat().st_size} bytes)")
        
        # Check other language solutions
        cpp_solution = base_path / 'solutions' / 'cpp' / f'{problem_id}.cpp'
        java_solution = base_path / 'solutions' / 'java' / f'{problem_id}.java'
        js_solution = base_path / 'solutions' / 'javascript' / f'{problem_id}.js'
        
        lang_count = sum([
            cpp_solution.exists(),
            java_solution.exists(),
            js_solution.exists()
        ])
        print(f"  ✅ Other solutions: {lang_count}/3 languages")
        
        print()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total problems: {len(problems)}")
    print(f"All files present: {'YES ✅' if all_good else 'NO ❌'}")
    print()
    
    # Count total test cases
    total_public = 0
    total_hidden = 0
    for problem_id in problems:
        testcase_file = base_path / 'testcases' / f'{problem_id}.yaml'
        if testcase_file.exists():
            with open(testcase_file, 'r') as f:
                tc_data = yaml.safe_load(f)
            total_public += len(tc_data.get('public', []))
            total_hidden += len(tc_data.get('hidden', []))
    
    print(f"Total public test cases: {total_public}")
    print(f"Total hidden test cases: {total_hidden}")
    print(f"Total test cases: {total_public + total_hidden}")
    print("=" * 80)

if __name__ == '__main__':
    verify_gametheory_module()
