#!/usr/bin/env python3
"""
Automated generator creator for remaining LinkedList problems
Extracts Python solutions from editorials and creates test generators
"""

import re
from pathlib import Path

# Problem specifications
PROBLEMS = {
    "lnk006": {
        "id": "LNK_LAB_LOOP_DETECTOR_ENTRY_LENGTH__6385",
        "name": "LNK-006-lab-loop-detector-entry-length",
        "func": "cycle_info",
        "params": ["head"],
        "special": "cycle"  # Special handling for cycle detection
    },
    "lnk007": {
        "id": "LNK_SEMINAR_WEIGHTED_MIDDLE__4193",
        "name": "LNK-007-seminar-weighted-middle",
        "func": "weighted_middle_value",
        "params": ["head"]
    },
    "lnk008": {
        "id": "LNK_LAB_PLAYLIST_MERGE_PARITY__5829",
        "name": "LNK-008-lab-playlist-merge-parity",
        "func": "merge_by_parity",
        "params": ["l1", "l2"]
    },
    "lnk009": {
        "id": "LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6394",
        "name": "LNK-009-robotics-chunk-reverse-offset-count",
        "func": "reverse_from_offset",
        "params": ["head", "k", "s"]
    },
    "lnk010": {
        "id": "LNK_SHUTTLE_ID_STABLE_PARTITION__5184",
        "name": "LNK-010-shuttle-id-stable-partition",
        "func": "stable_partition",
        "params": ["head", "x"]
    },
    "lnk011": {
        "id": "LNK_EXAM_SEATING_INTERSECTION_SUM__6385",
        "name": "LNK-011-exam-seating-intersection-sum",
        "func": "intersection_sum",
        "params": ["headA", "headB"],
        "special": "intersection"
    },
    "lnk012": {
        "id": "LNK_HOSTEL_NUMBER_REMOVE_MTH__4829",
        "name": "LNK-012-hostel-number-remove-mth",
        "func": "remove_mth",
        "params": ["head", "M"]
    },
    "lnk013": {
        "id": "LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__6385",
        "name": "LNK-013-shuttle-ticket-rotate-blocks",
        "func": "rotate_blocks",
        "params": ["head", "b", "k"]
    },
    "lnk014": {
        "id": "LNK_ROBOTICS_PALINDROME_ONE_SKIP__5829",
        "name": "LNK-014-robotics-palindrome-one-skip",
        "func": "is_palindrome_skip_one",
        "params": ["head"]
    },
    "lnk015": {
        "id": "LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__4829",
        "name": "LNK-015-workshop-odd-even-grouping-stable",
        "func": "group_odd_even_stable",
        "params": ["head"]
    },
    "lnk016": {
        "id": "LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__7395",
        "name": "LNK-016-lecture-notes-subtract-forward-freq",
        "func": "subtract_with_freq",
        "params": ["a", "b"]
    }
}

def extract_python_solution(editorial_path):
    """Extract Python solution from editorial markdown"""
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    # Find Python section
    py_section = re.search(r'### Python\s*```python\n(.*?)\n```', content, re.DOTALL)
    if py_section:
        return py_section.group(1)
    return None

def create_generator_template(prob_key, spec):
    """Create a test generator script"""
    return f'''import sys
import random

# --- Reference Solution (extracted from editorial) ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# TODO: Add solution function from editorial

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def solve(*args):
    # TODO: Implement based on problem
    pass

# --- Test Case Generators ---

def make_test_case(*args):
    # TODO: Implement based on problem input/output format
    pass

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {{line}}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {{line}}")

def main():
    test_cases = {{
        "problem_id": "{spec['id']}",
        "samples": [],
        "public": [],
        "hidden": []
    }}

    # TODO: Add test cases

    # Output YAML
    print(f"problem_id: {{test_cases['problem_id']}}")
    print("samples:")
    for c in test_cases["samples"]:
        print_case(c)
    print("\\npublic:")
    for c in test_cases["public"]:
        print_case(c)
    print("\\nhidden:")
    for c in test_cases["hidden"]:
        print_case(c)

if __name__ == "__main__":
    main()
'''

def main():
    editorials_dir = Path("../../editorials")
    tc_gen_dir = Path(".")
    
    print("Creating generator templates for remaining LinkedList problems...")
    
    for prob_key, spec in PROBLEMS.items():
        gen_file = tc_gen_dir / f"generate_{prob_key}.py"
        if gen_file.exists():
            print(f"✓ {prob_key} already exists")
            continue
        
        editorial_file = editorials_dir / f"{spec['name']}.md"
        if not editorial_file.exists():
            print(f"⚠️  Editorial not found for {prob_key}")
            continue
        
        # Create template
        content = create_generator_template(prob_key, spec)
        
        with open(gen_file, 'w') as f:
            f.write(content)
        
        print(f"✅ Created template for {prob_key}")
    
    print("\\nTemplates created! You need to fill in the solutions manually.")

if __name__ == "__main__":
    main()
