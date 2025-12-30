#!/usr/bin/env python3
"""
Convert existing Math Advanced YAMLs to proper format
Load with safe_load, dump with clean format
"""
import yaml
import os

base = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/MathAdvanced/testcases"

files_to_convert = [
    'MTH-003-inverse-polynomial.yaml',
    'MTH-004-multipoint-evaluation.yaml',
    'MTH-005-lagrange-interpolation-mod.yaml',
    'MTH-006-determinant-gaussian.yaml',
    'MTH-007-matrix-exp-linear-recurrence.yaml',
    'MTH-008-fwht-xor-convolution.yaml',
    'MTH-009-subset-convolution-and-or.yaml',
    'MTH-010-berlekamp-massey.yaml',
    'MTH-011-minimal-polynomial-matrix.yaml',
    'MTH-012-convolution-multi-mod-crt.yaml',
    'MTH-013-invert-vandermonde.yaml',
    'MTH-014-largest-eigenvalue-power.yaml',
]

print("Converting YAMLs to proper format...")
for fname in files_to_convert:
    fpath = f"{base}/{fname}"
    
    # Load existing
    with open(fpath, 'r') as f:
        data = yaml.safe_load(f)
    
    # Convert input/output strings - replace escaped newlines with actual newlines
    for category in ['samples', 'public', 'hidden']:
        if category in data and data[category]:
            for tc in data[category]:
                if 'input' in tc and isinstance(tc['input'], str):
                    tc['input'] = tc['input'].replace('\\n', '\n')
                if 'output' in tc and isinstance(tc['output'], str):
                    tc['output'] = tc['output'].replace('\\n', '\n')
    
    # Save with proper format
    with open(fpath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    total = len(data.get('samples', [])) + len(data.get('public', [])) + len(data.get('hidden', []))
    print(f"  {fname}: {total} tests converted")

print("\nDone!")
