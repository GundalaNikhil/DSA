#!/usr/bin/env python3
"""Fix YAML format for Math Advanced test cases to use |- syntax."""

import os
import yaml
from typing import Dict, Any, List

TESTCASES_DIR = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases"

def str_representer(dumper, data):
    """Custom string representer that uses |- for multiline strings."""
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|-')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

# Override default string representation
yaml.add_representer(str, str_representer)

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
            yaml.dump(data, f, sort_keys=False, default_flow_style=False, 
                     allow_unicode=True, width=1000)
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    """Fix all Math Advanced YAML files."""
    print("=" * 70)
    print("FIXING YAML FORMAT FOR MATH ADVANCED TEST CASES")
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
