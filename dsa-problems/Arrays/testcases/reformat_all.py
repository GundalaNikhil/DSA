#!/usr/bin/env python3
"""
Reformat all Array test case YAML files to have proper block scalar formatting.
This will fix the alignment and formatting to match ARR-005 style.
"""

import yaml
from pathlib import Path

def format_yaml_properly(yaml_file):
    """Reformat YAML with proper block scalars and indentation."""
    
    # Load the data
    with open(yaml_file) as f:
        data = yaml.safe_load(f)
    
    # Manually write with proper formatting
    with open(yaml_file, 'w') as f:
        # Write problem_id
        f.write(f"problem_id: {data['problem_id']}\n")
        
        # Write samples
        f.write("samples:\n")
        for test in data.get('samples', []):
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            for line in test['output'].split('\n'):
                f.write(f"      {line}\n")
            f.write("\n")
        
        # Write public
        f.write("public:\n")
        for test in data.get('public', []):
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            for line in test['output'].split('\n'):
                f.write(f"      {line}\n")
            f.write("\n")
        
        # Write hidden
        f.write("hidden:\n")
        for test in data.get('hidden', []):
            f.write("  - input: |-\n")
            for line in test['input'].split('\n'):
                f.write(f"      {line}\n")
            f.write("    output: |-\n")
            for line in test['output'].split('\n'):
                f.write(f"      {line}\n")
            f.write("\n")
    
    print(f"✅ Reformatted {yaml_file.name}")

def main():
    base = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Arrays/testcases")
    
    # Skip ARR-004 (different file name) and ARR-005 (already formatted)
    problems = [
        "ARR-001-snack-restock-snapshot",
        "ARR-002-bench-flip-locked-ends",
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
    ]
    
    for problem in problems:
        yaml_file = base / f"{problem}.yaml"
        if yaml_file.exists():
            format_yaml_properly(yaml_file)

if __name__ == "__main__":
    main()
