#!/usr/bin/env python3
"""
Regenerate all AGR test cases using editorial solutions as source of truth.
Preserves existing test inputs, regenerates outputs using editorial Python solutions.
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
    
    pattern = r'### Python\n\n```python\n(.*?)\n```'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return None
    
    return match.group(1)


def run_solution(solution_code, test_input):
    """Run solution code with test input and get output."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(solution_code)
        temp_file = f.name
    
    try:
        result = subprocess.run(
            ['python3', temp_file],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            return None, f"ERROR: {result.stderr}"
        
        return result.stdout.strip(), None
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:
        return None, str(e)
    finally:
        os.unlink(temp_file)


def regenerate_testcase_yaml(prob_id):
    """Regenerate test cases for a single problem."""
    print(f"\n{'='*60}")
    print(f"Regenerating {prob_id}")
    print(f"{'='*60}")
    
    # Find files
    editorial_files = list(Path('editorials').glob(f'{prob_id}*.md'))
    testcase_files = list(Path('testcases').glob(f'{prob_id}*.yaml'))
    
    if not editorial_files:
        print(f"  ❌ Editorial not found")
        return False
    
    if not testcase_files:
        print(f"  ❌ Test case file not found")
        return False
    
    editorial_file = editorial_files[0]
    testcase_file = testcase_files[0]
    
    # Extract solution
    solution_code = extract_python_solution(editorial_file)
    if not solution_code:
        print(f"  ❌ No Python solution in editorial")
        return False
    
    print(f"  ✓ Extracted Python solution")
    
    # Load existing test cases
    with open(testcase_file, 'r') as f:
        tc_data = yaml.safe_load(f)
    
    problem_id = tc_data.get('problem_id', '')
    
    # Regenerate outputs for all test cases
    regenerated = {'problem_id': problem_id, 'samples': [], 'public': [], 'hidden': []}
    
    total_cases = 0
    success_count = 0
    
    for category in ['samples', 'public', 'hidden']:
        if category not in tc_data:
            continue
        
        for idx, tc in enumerate(tc_data[category]):
            total_cases += 1
            test_input = tc['input']
            
            # Run through editorial solution
            output, error = run_solution(solution_code, test_input)
            
            if error:
                print(f"  ⚠️  {category}[{idx}]: {error}")
                # Keep original output if solution fails
                regenerated[category].append(tc)
            else:
                success_count += 1
                regenerated[category].append({
                    'input': test_input,
                    'output': output
                })
    
    print(f"  ✓ Regenerated {success_count}/{total_cases} test cases")
    
    # Write new YAML in block scalar format
    yaml_content = f"problem_id: {problem_id}\n"
    
    for category in ['samples', 'public', 'hidden']:
        if not regenerated[category]:
            continue
        
        yaml_content += f"{category}:\n"
        for tc in regenerated[category]:
            yaml_content += "  - input: |-\n"
            for line in tc['input'].strip().split('\n'):
                yaml_content += f"      {line}\n"
            yaml_content += "    output: |-\n"
            for line in tc['output'].strip().split('\n'):
                yaml_content += f"      {line}\n"
    
    # Write to file
    with open(testcase_file, 'w') as f:
        f.write(yaml_content)
    
    print(f"  ✅ Written to {testcase_file.name}")
    
    return success_count == total_cases


def main():
    os.chdir('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/AdvancedGraphs')
    
    print("="*60)
    print("AGR TEST CASE REGENERATION")
    print("="*60)
    print("\nUsing editorial Python solutions as source of truth")
    print("Preserving test inputs, regenerating outputs\n")
    
    results = {}
    
    for i in range(1, 17):
        prob_id = f'AGR-{i:03d}'
        success = regenerate_testcase_yaml(prob_id)
        results[prob_id] = success
    
    # Summary
    print(f"\n\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    successful = sum(1 for v in results.values() if v)
    failed = len(results) - successful
    
    print(f"\n✅ Successfully regenerated: {successful}/16 problems")
    if failed > 0:
        print(f"❌ Failed: {failed}/16 problems")
        print("\nFailed problems:")
        for prob_id, success in results.items():
            if not success:
                print(f"  - {prob_id}")
    else:
        print("\n🎉 ALL TEST CASES REGENERATED!")
        print("\nNext step: Run test_solutions.py to validate")


if __name__ == '__main__':
    main()
