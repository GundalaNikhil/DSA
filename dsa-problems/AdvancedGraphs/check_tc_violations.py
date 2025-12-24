#!/usr/bin/env python3
"""
Check AGR test cases against problem constraints.
Identify violations in input format, constraints, and output format.
"""
import os
import re
import yaml
from pathlib import Path

def extract_constraints_from_problem(problem_file):
    """Extract constraints from problem markdown file."""
    with open(problem_file, 'r') as f:
        content = f.read()
    
    # Find constraints section
    constraints_match = re.search(r'## Constraints\n\n(.*?)(?=\n##|$)', content, re.DOTALL)
    if not constraints_match:
        return {}
    
    constraints_text = constraints_match.group(1)
    constraints = {}
    
    # Parse constraint lines
    for line in constraints_text.strip().split('\n'):
        line = line.strip('- `').strip('`')
        if '<=' in line or '>=' in line or '<' in line or '>' in line:
            constraints[line] = line
    
    return constraints

def extract_input_format(problem_file):
    """Extract input format from problem markdown file."""
    with open(problem_file, 'r') as f:
        content = f.read()
    
    input_match = re.search(r'## Input Format\n\n(.*?)(?=\n##|$)', content, re.DOTALL)
    if not input_match:
        return []
    
    return input_match.group(1).strip().split('\n')

def extract_output_format(problem_file):
    """Extract output format from problem markdown file."""
    with open(problem_file, 'r') as f:
        content = f.read()
    
    output_match = re.search(r'## Output Format\n\n(.*?)(?=\n##|$)', content, re.DOTALL)
    if not output_match:
        return []
    
    return output_match.group(1).strip().split('\n')

def check_testcase(tc_file, problem_file, problem_id):
    """Check a single test case file against its problem."""
    print(f"\n{'='*80}")
    print(f"Checking {problem_id}")
    print(f"{'='*80}")
    
    # Load test case YAML
    with open(tc_file, 'r') as f:
        tc_data = yaml.safe_load(f)
    
    # Extract from problem
    constraints = extract_constraints_from_problem(problem_file)
    input_format = extract_input_format(problem_file)
    output_format = extract_output_format(problem_file)
    
    print(f"\nInput Format:")
    for line in input_format:
        print(f"  {line}")
    
    print(f"\nOutput Format:")
    for line in output_format:
        print(f"  {line}")
        
    print(f"\nConstraints:")
    for constraint in constraints:
        print(f"  {constraint}")
    
    violations = []
    
    # Check all test cases (samples, public, hidden)
    all_test_cases = []
    if 'samples' in tc_data:
        all_test_cases.extend([(tc, 'sample') for tc in tc_data['samples']])
    if 'public' in tc_data:
        all_test_cases.extend([(tc, 'public') for tc in tc_data['public']])
    if 'hidden' in tc_data:
        all_test_cases.extend([(tc, 'hidden') for tc in tc_data['hidden']])
    
    print(f"\nTotal test cases: {len(all_test_cases)}")
    
    # For each test case, do basic validation
    for idx, (tc, tc_type) in enumerate(all_test_cases):
        if 'input' not in tc or 'output' not in tc:
            violations.append(f"{tc_type}[{idx}]: Missing input or output")
            continue
    
        # Check if input/output follow expected patterns
        input_lines = tc['input'].strip().split('\n')
        output_lines = tc['output'].strip().split('\n')
        
        # Report format
        print(f"\n{tc_type}[{idx}]:")
        print(f"  Input lines: {len(input_lines)}")
        print(f"  Output lines: {len(output_lines)}")
        print(f"  First input line: {input_lines[0] if input_lines else 'EMPTY'}")
        print(f"  First output line: {output_lines[0] if output_lines else 'EMPTY'}")
    
    if violations:
        print(f"\n❌ VIOLATIONS FOUND:")
        for v in violations:
            print(f"  - {v}")
    else:
        print(f"\n✅ No structural violations found")
    
    return violations

def main():
    problems_dir = Path('problems')
    testcases_dir = Path('testcases')
    
    all_violations = {}
    
    for i in range(1, 17):
        prob_id = f'AGR-{i:03d}'
        
        # Find files
        prob_files = list(problems_dir.glob(f'{prob_id}*.md'))
        tc_files = list(testcases_dir.glob(f'{prob_id}*.yaml'))
        
        if not prob_files or not tc_files:
            print(f"⚠️  Skipping {prob_id}: Missing files")
            continue
        
        violations = check_testcase(tc_files[0], prob_files[0], prob_id)
        if violations:
            all_violations[prob_id] = violations
    
    print(f"\n\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    
    if all_violations:
        print(f"\n❌ Problems with violations:")
        for prob_id, violations in all_violations.items():
            print(f"\n{prob_id}:")
            for v in violations:
                print(f"  - {v}")
    else:
        print(f"\n✅ All test cases pass structural checks!")

if __name__ == '__main__':
    main()
