#!/usr/bin/env python3
"""
Restore proper YAML formatting with block scalars (|-) for input/output fields.
"""

import yaml
import re
from pathlib import Path

class BlockScalarDumper(yaml.SafeDumper):
    """Custom YAML dumper that uses block scalars for multiline strings."""
    pass

def str_representer(dumper, data):
    """Represent strings using block scalar style for multiline content."""
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|-')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_representer, Dumper=BlockScalarDumper)

def fix_yaml_formatting(yaml_file):
    """Fix YAML formatting to use block scalars."""
    # Load the YAML
    with open(yaml_file) as f:
        data = yaml.safe_load(f)
    
    # Write with custom dumper
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f, Dumper=BlockScalarDumper, default_flow_style=False, 
                  allow_unicode=True, sort_keys=False, width=1000)
    
    print(f"✅ Fixed {yaml_file.name}")

def main():
    base = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays/testcases")
    
    problems = [
        "ARR-001-snack-restock-snapshot",
        "ARR-003-shuttle-shift-blackout",
        "ARR-006-zero-slide-limit",
        "ARR-007-hostel-roster-merge-gap",
        "ARR-008-partner-pair-sum-forbidden",
        "ARR-009-best-streak-one-smoothing",
        "ARR-010-early-discount-stay-window",
        "ARR-011-leaky-roof-reinforcement",
        "ARR-012-longest-zero-sum-even",
        "ARR-013-tool-frequency-top-k-decay",
        "ARR-014-boarding-order-fixed-ones",
        "ARR-015-seat-gap-after-removals",
        "ARR-016-power-window-with-drop",
        "ARR-005-weighted-balance-point",
    ]
    
    for problem in problems:
        yaml_file = base / f"{problem}.yaml"
        if yaml_file.exists():
            fix_yaml_formatting(yaml_file)

if __name__ == "__main__":
    main()
