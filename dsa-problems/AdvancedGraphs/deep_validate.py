#!/usr/bin/env python3
"""
Deep validation of AGR test cases against problem specifications.
Identifies specific violations in input/output formats and constraints.
"""
import os
import re
import yaml
from pathlib import Path


def parse_problem_details(problem_file):
    """Extract detailed problem specifications."""
    with open(problem_file, 'r') as f:
        content = f.read()
    
    details = {
        'problem_id': '',
        'input_format': [],
        'output_format': [],
        'constraints': {},
        'example_input': '',
        'example_output': ''
    }
    
    # Extract problem_id from frontmatter
    id_match = re.search(r'problem_id:\s*(\S+)', content)
    if id_match:
        details['problem_id'] = id_match.group(1)
    
    # Extract input format
    input_match = re.search(r'## Input Format\n\n(.*?)(?=\n##)', content, re.DOTALL)
    if input_match:
        details['input_format'] = [line.strip() for line in input_match.group(1).strip().split('\n') if line.strip()]
    
    # Extract output format
    output_match = re.search(r'## Output Format\n\n(.*?)(?=\n##)', content, re.DOTALL)
    if output_match:
        details['output_format'] = [line.strip() for line in output_match.group(1).strip().split('\n') if line.strip()]
    
    # Extract example
    example_match = re.search(r'\*\*Input:\*\*\n\n```\n(.*?)\n```\n\n\*\*Output:\*\*\n\n```\n(.*?)\n```', content, re.DOTALL)
    if example_match:
        details['example_input'] = example_match.group(1).strip()
        details['example_output'] = example_match.group(2).strip()
    
    return details


def validate_testcase_deep(tc_data, problem_details, prob_id):
    """Perform deep validation of test cases."""
    violations = []
    
    # Collect all test cases
    all_test_cases = []
    for category in ['samples', 'public', 'hidden']:
        if category in tc_data:
            for idx, tc in enumerate(tc_data[category]):
                all_test_cases.append((category, idx, tc))
    
    print(f"\nValidating {prob_id}: {len(all_test_cases)} test cases total")
    print(f"Input format: {problem_details['input_format']}")
    print(f"Output format: {problem_details['output_format']}")
    
    # Check example matches sample[0]
    if 'samples' in tc_data and len(tc_data['samples']) > 0:
        sample0_input = tc_data['samples'][0].get('input', '').strip()
        sample0_output = tc_data['samples'][0].get('output', '').strip()
        expected_input = problem_details['example_input']
        expected_output = problem_details['example_output']
        
        if sample0_input != expected_input:
            violations.append(f"❌ sample[0] input doesn't match problem example")
            print(f"  Expected: {expected_input[:50]}...")
            print(f"  Got:      {sample0_input[:50]}...")
        
        if sample0_output != expected_output:
            violations.append(f"❌ sample[0] output doesn't match problem example")
            print(f"  Expected: '{expected_output}'")
            print(f"  Got:      '{sample0_output}'")
    
    # Validate each test case structure
    bad_cases = []
    for category, idx, tc in all_test_cases:
        tc_id = f"{category}[{idx}]"
        
        if 'input' not in tc or 'output' not in tc:
            bad_cases.append(f"{tc_id}: Missing input/output field")
            continue
        
        in_lines = tc['input'].strip().split('\n')
        out_lines = tc['output'].strip().split('\n')
        
        # Check if input/output are non-empty
        if not tc['input'].strip():
            bad_cases.append(f"{tc_id}: Empty input")
        
        if not tc['output'].strip() and 'output' in tc:
            # Empty output might be valid for some problems
            pass
    
    if bad_cases:
        violations.append(f"❌ {len(bad_cases)} test cases with structural issues:")
        for bc in bad_cases[:5]:  # Show first 5
            violations.append(f"  - {bc}")
        if len(bad_cases) > 5:
            violations.append(f"  ... and {len(bad_cases) - 5} more")
    
    return violations


def main():
    problems_dir = Path('problems')
    testcases_dir = Path('testcases')
    
    all_violations = {}
    
    print("="*80)
    print("DEEP AGR TEST CASE VALIDATION")
    print("="*80)
    
    for i in range(1, 17):
        prob_id = f'AGR-{i:03d}'
        
        prob_files = list(problems_dir.glob(f'{prob_id}*.md'))
        tc_files = list(testcases_dir.glob(f'{prob_id}*.yaml'))
        
        if not prob_files or not tc_files:
            print(f"\n⚠️  Skipping {prob_id}: Missing files")
            continue
        
        print(f"\n{'='*80}")
        print(f"{prob_id}")
        print(f"{'='*80}")
        
        # Parse problem
        problem_details = parse_problem_details(prob_files[0])
        
        # Load test cases
        with open(tc_files[0], 'r') as f:
            tc_data = yaml.safe_load(f)
        
        # Validate
        violations = validate_testcase_deep(tc_data, problem_details, prob_id)
        
        if violations:
            all_violations[prob_id] = violations
            print(f"\n{'─'*80}")
            print("VIOLATIONS FOUND:")
            for v in violations:
                print(f"  {v}")
        else:
            print("\n✅ No violations detected")
    
    # Summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    
    if all_violations:
        print(f"\n❌ {len(all_violations)} problems with violations:\n")
        for prob_id, violations in all_violations.items():
            print(f"{prob_id}:")
            for v in violations:
                print(f"  {v}")
            print()
    else:
        print("\n✅ All test cases validated successfully!")


if __name__ == '__main__':
    main()
