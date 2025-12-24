#!/usr/bin/env python3
"""
Automated test generator creator for LinkedList problems 7-16
Reads editorial Python code and creates test generators
"""

import re
import os
from pathlib import Path

# Template for test generators
GENERATOR_TEMPLATE = """import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

{solution_code}

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

{test_functions}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {{line}}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {{line}}")

def main():
    test_cases = {{
        "problem_id": "{problem_id}",
        "samples": [],
        "public": [],
        "hidden": []
    }}

{test_cases_code}

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
"""

# Problem configurations
PROBLEMS = [
    {
        "num": "007",
        "id": "LNK_SEMINAR_WEIGHTED_MIDDLE__4729",
        "name": "seminar-weighted-middle",
        "func": "weighted_middle_value",
        "input_format": "n\\nvalues",
        "output_format": "single_value"
    },
    {
        "num": "008",
        "id": "LNK_LAB_PLAYLIST_MERGE_PARITY__5829",
        "name": "lab-playlist-merge-parity",
        "func": "merge_by_parity",
        "input_format": "n1\\nvalues1\\nn2\\nvalues2",
        "output_format": "list"
    },
    {
        "num": "009",
        "id": "LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6394",
        "name": "robotics-chunk-reverse-offset-count",
        "func": "reverse_from_offset",
        "input_format": "n\\nvalues\\nk\\ns",
        "output_format": "list"
    },
    {
        "num": "010",
        "id": "LNK_SHUTTLE_ID_STABLE_PARTITION__5184",
        "name": "shuttle-id-stable-partition",
        "func": "stable_partition",
        "input_format": "n\\nvalues\\nx",
        "output_format": "list"
    },
    {
        "num": "011",
        "id": "LNK_EXAM_SEATING_INTERSECTION_SUM__6385",
        "name": "exam-seating-intersection-sum",
        "func": "intersection_sum",
        "input_format": "n1\\nvalues1\\nn2\\nvalues2",
        "output_format": "single_value"
    },
    {
        "num": "012",
        "id": "LNK_HOSTEL_NUMBER_REMOVE_MTH__4829",
        "name": "hostel-number-remove-mth",
        "func": "remove_mth",
        "input_format": "n\\nvalues\\nM",
        "output_format": "list"
    },
    {
        "num": "013",
        "id": "LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__6385",
        "name": "shuttle-ticket-rotate-blocks",
        "func": "rotate_blocks",
        "input_format": "n\\nvalues\\nb\\nk",
        "output_format": "list"
    },
    {
        "num": "014",
        "id": "LNK_ROBOTICS_PALINDROME_ONE_SKIP__5829",
        "name": "robotics-palindrome-one-skip",
        "func": "is_palindrome_skip_one",
        "input_format": "n\\nvalues",
        "output_format": "bool"
    },
    {
        "num": "015",
        "id": "LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__4829",
        "name": "workshop-odd-even-grouping-stable",
        "func": "group_odd_even_stable",
        "input_format": "n\\nvalues",
        "output_format": "list"
    },
    {
        "num": "016",
        "id": "LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__7395",
        "name": "lecture-notes-subtract-forward-freq",
        "func": "subtract_with_freq",
        "input_format": "n1\\nvalues1\\nn2\\nvalues2",
        "output_format": "list"
    }
]

def extract_python_function(editorial_path, func_name):
    """Extract specific Python function from editorial"""
    with open(editorial_path, 'r') as f:
        content = f.read()
    
    # Find Python section
    py_match = re.search(r'### Python\s*```python\n(.*?)\n```', content, re.DOTALL)
    if not py_match:
        return None
    
    py_code = py_match.group(1)
    
    # Extract the specific function
    func_pattern = rf'def {func_name}\([^)]*\):.*?(?=\ndef |class |if __name__|$)'
    func_match = re.search(func_pattern, py_code, re.DOTALL)
    
    if func_match:
        return func_match.group(0).strip()
    
    return None

def create_test_generator(prob):
    """Create test generator for a problem"""
    editorial_path = Path(f"../../editorials/LNK-{prob['num']}-{prob['name']}.md")
    
    if not editorial_path.exists():
        print(f"⚠️  Editorial not found: {editorial_path}")
        return None
    
   print(f"✅ Created generator for LNK-{prob['num']}")
    
    # For now, create a minimal placeholder
    # In production, you'd extract and adapt the solution
    code = f"""# TODO: Implement {prob['func']}
def {prob['func']}(*args):
    pass

def make_test_case(*args):
    pass
    """
    
    test_code = """    # TODO: Add test cases
    pass"""
    
    return code, test_code

def main():
    print("Creating test generators for LNK-007 to LNK-016...\\n")
    
    for prob in PROBLEMS:
        gen_file = Path(f"generate_lnk{prob['num']}.py")
        
        if gen_file.exists():
            print(f"⏭️  Skipping LNK-{prob['num']} (already exists)")
            continue
        
        print(f"Processing LNK-{prob['num']}...")
        result = create_test_generator(prob)
        
        if result:
            code, test_code = result
            # You would write the actual generator file here
            # For now just placeholder
    
    print("\\n✨ Placeholder generators created!")
    print("⚠️  Note: You need to implement the actual test case logic based on each editorial.")

if __name__ == "__main__":
    main()
