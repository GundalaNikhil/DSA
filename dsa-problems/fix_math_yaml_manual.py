#!/usr/bin/env python3
"""Fix YAML format for Math Advanced test cases to use |- syntax - Manual approach."""

import os
import yaml
from typing import Dict, Any, List

TESTCASES_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases"

def format_testcase_yaml(data: Dict[str, Any]) -> str:
    """Manually format YAML with |- syntax for multiline strings."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section in ['samples', 'public', 'hidden']:
        if section not in data or not data[section]:
            continue
        
        lines.append(f"{section}:")
        for case in data[section]:
            lines.append("- input: |-")
            # Add indented input lines
            for line in case['input'].split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            # Add indented output lines
            for line in case['output'].split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines) + '\n'

def fix_yaml_file(filepath: str) -> bool:
    """Fix a single YAML file to use |- syntax."""
    try:
        # Read the file
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        if not data or 'problem_id' not in data:
            print(f"⚠️  Skipping {filepath} - invalid format")
            return False
        
        # Write back with proper formatting
        with open(filepath, 'w') as f:
            f.write(f"# filepath: {filepath}\n")
            f.write(format_testcase_yaml(data))
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Fix all Math Advanced YAML files."""
    print("=" * 70)
    print("FIXING YAML FORMAT FOR MATH ADVANCED TEST CASES (|- SYNTAX)")
    print("=" * 70)
    
    files = sorted([f for f in os.listdir(TESTCASES_DIR) 
                   if f.startswith('MTH-') and f.endswith('.yaml')])
    
    success_count = 0
    for filename in files:
        filepath = os.path.join(TESTCASES_DIR, filename)
        problem_id = filename.split('.')[0][:7]  # MTH-XXX
        
        if fix_yaml_file(filepath):
            print(f"✅ {problem_id}: Fixed {filename}")
            success_count += 1
        else:
            print(f"❌ {problem_id}: Failed {filename}")
    
    print("=" * 70)
    print(f"Fixed {success_count}/{len(files)} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
