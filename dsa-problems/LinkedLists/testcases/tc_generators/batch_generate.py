#!/usr/bin/env python3
"""
Batch generation script for all remaining LinkedList test cases
"""

import subprocess
import sys
from pathlib import Path

# Problem mapping with their reference solutions
problems = [
    ("lnk004", "LNK-004-hostel-cleanup-deduplicate-two"),
    ("lnk005", "LNK-005-shuttle-route-alternating-reverse"),
    ("lnk006", "LNK-006-lab-loop-detector-entry-length"),
    ("lnk007", "LNK-007-seminar-weighted-middle"),
    ("lnk008", "LNK-008-lab-playlist-merge-parity"),
    ("lnk009", "LNK-009-robotics-chunk-reverse-offset-count"),
    ("lnk010", "LNK-010-shuttle-id-stable-partition"),
    ("lnk011", "LNK-011-exam-seating-intersection-sum"),
    ("lnk012", "LNK-012-hostel-number-remove-mth"),
    ("lnk013", "LNK-013-shuttle-ticket-rotate-blocks"),
    ("lnk014", "LNK-014-robotics-palindrome-one-skip"),
    ("lnk015", "LNK-015-workshop-odd-even-grouping-stable"),
    ("lnk016", "LNK-016-lecture-notes-subtract-forward-freq"),
]

def main():
    tc_gen_dir = Path(".")
    output_dir = Path("..")
    
    print("Starting batch generation for LinkedList problems 4-16...")
    
    for gen_name, yaml_name in problems:
        gen_file = tc_gen_dir / f"generate_{gen_name}.py"
        yaml_file = output_dir / f"{yaml_name}.yaml"
        
        if not gen_file.exists():
            print(f"⚠️  Skipping {gen_name}: generator not found")
            continue
            
        print(f"Generating {yaml_name}...")
        try:
            result = subprocess.run(
                [sys.executable, str(gen_file)],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                print(f"❌ Failed {gen_name}: {result.stderr}")
                continue
                
            with open(yaml_file, 'w') as f:
                f.write(result.stdout)
                
            print(f"✅ Generated {yaml_name}")
            
        except subprocess.TimeoutExpired:
            print(f"❌ Timeout for {gen_name}")
        except Exception as e:
            print(f"❌ Error for {gen_name}: {e}")
    
    print("\\nBatch generation complete!")

if __name__ == "__main__":
    main()
