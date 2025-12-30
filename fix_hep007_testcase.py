#!/usr/bin/env python3
"""Regenerate HEP-007 test case expected outputs using the corrected solution."""

import yaml
import sys
sys.path.insert(0, '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/solutions/python')

from importlib import import_module
import importlib.util

# Load the corrected solution
spec = importlib.util.spec_from_file_location(
    "solution", 
    "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/solutions/python/HEP-007-sliding-window-kth-smallest.py"
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

Solution = solution_module.Solution

def regenerate_outputs():
    yaml_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/testcases/HEP-007-sliding-window-kth-smallest.yaml'
    
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    
    solution = Solution()
    
    # Process all test cases
    for category in ['samples', 'public', 'hidden']:
        if category not in data:
            continue
        
        for test_case in data[category]:
            input_lines = test_case['input'].strip().split('\n')
            first_line = input_lines[0].split()
            n, w, k = int(first_line[0]), int(first_line[1]), int(first_line[2])
            
            arr = list(map(int, input_lines[1].split()))
            
            # Generate correct output
            result = solution.kth_smallest_in_windows(arr, w, k)
            test_case['output'] = ' '.join(map(str, result))
    
    # Write back to file with proper formatting
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print("✅ Successfully regenerated all HEP-007 test case outputs!")

if __name__ == '__main__':
    regenerate_outputs()
