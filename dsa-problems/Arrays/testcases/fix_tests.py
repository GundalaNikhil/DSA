#!/usr/bin/env python3
"""
Fix test case outputs by running editorial solutions and updating YAML files.
"""

import yaml
import sys
import re
from io import StringIO
from pathlib import Path

def extract_python_solution(editorial_path):
    """Extract Python solution from editorial."""
    with open(editorial_path) as f:
        content = f.read()
    match = re.search(r'### Python\s*```python\s*(.*?)```', content, re.DOTALL)
    if not match:
        raise ValueError(f"No Python solution in {editorial_path}")
    return match.group(1).strip()

def run_solution(solution_code, input_data):
    """Run solution and return output."""
    old_stdin, old_stdout = sys.stdin, sys.stdout
    try:
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()
        exec(solution_code, {'__name__': '__main__'})
        return sys.stdout.getvalue().rstrip('\n')
    except Exception as e:
        return f"ERROR: {e}"
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout

def fix_problem(problem_id):
    """Fix all test cases for a problem."""
    base = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays")
    yaml_file = base / "testcases" / f"{problem_id}.yaml"
    editorial_file = base / "editorials" / f"{problem_id}.md"
    
    # Load solution
    solution = extract_python_solution(editorial_file)
    
    # Load test cases
    with open(yaml_file) as f:
        data = yaml.safe_load(f)
    
    fixed = 0
    
    # Fix all test cases
    for category in ['samples', 'public', 'hidden']:
        if category not in data:
            continue
        for test in data[category]:
            correct_output = run_solution(solution, test['input'])
            if test['output'] != correct_output:
                test['output'] = correct_output
                fixed += 1
    
    # Save updated YAML
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"✅ {problem_id}: Fixed {fixed} test cases")
    return fixed

def main():
    problems = sys.argv[1:] if len(sys.argv) > 1 else [
        "ARR-001-snack-restock-snapshot",
        "ARR-003-shuttle-shift-blackout",
        "ARR-009-best-streak-one-smoothing",
        "ARR-010-early-discount-stay-window",
        "ARR-011-leaky-roof-reinforcement",
        "ARR-012-longest-zero-sum-even",
        "ARR-013-tool-frequency-top-k-decay",
        "ARR-015-seat-gap-after-removals",
        "ARR-016-power-window-with-drop",
    ]
    
    total_fixed = 0
    for problem in problems:
        try:
            total_fixed += fix_problem(problem)
        except Exception as e:
            print(f"❌ {problem}: {e}")
    
    print(f"\n🎉 Total fixed: {total_fixed} test cases")

if __name__ == "__main__":
    main()
