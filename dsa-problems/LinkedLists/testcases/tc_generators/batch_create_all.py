#!/usr/bin/env python3
"""
Batch create remaining LinkedList test generators (008-016)
Extracts solutions from editorials and creates comprehensive test generators
"""

import os
import re
from pathlib import Path

# Base template for all generators
BASE_TEMPLATE = '''import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def array_to_list(arr):
    if not arr:
        return None
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

{solution_code}

{helper_code}

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
'''

# Problem-specific configurations
PROBLEMS_CONFIG = {
    "008": {
        "id": "LNK_LAB_PLAYLIST_MERGE_PARITY__5829",
        "name": "lab-playlist-merge-parity",
        "solution_func": "merge_by_parity",
        "has_two_lists": True
    },
    "009": {
        "id": "LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6394",
        "name": "robotics-chunk-reverse-offset-count",
        "solution_func": "reverse_from_offset",
        "params": ["head", "k", "s"]
    },
    "010": {
        "id": "LNK_SHUTTLE_ID_STABLE_PARTITION__5184",
        "name": "shuttle-id-stable-partition",
        "solution_func": "stable_partition",
        "params": ["head", "x"]
    },
    "011": {
        "id": "LNK_EXAM_SEATING_INTERSECTION_SUM__6385",
        "name": "exam-seating-intersection-sum",
        "solution_func": "intersection_sum",
        "has_two_lists": True,
        "returns_int": True
    },
    "012": {
        "id": "LNK_HOSTEL_NUMBER_REMOVE_MTH__4829",
        "name": "hostel-number-remove-mth",
        "solution_func": "remove_mth",
        "params": ["head", "M"]
    },
    "013": {
        "id": "LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__6385",
        "name": "shuttle-ticket-rotate-blocks",
        "solution_func": "rotate_blocks",
        "params": ["head", "b", "k"]
    },
    "014": {
        "id": "LNK_ROBOTICS_PALINDROME_ONE_SKIP__5829",
        "name": "robotics-palindrome-one-skip",
        "solution_func": "is_palindrome_skip_one",
        "returns_bool": True
    },
    "015": {
        "id": "LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__4829",
        "name": "workshop-odd-even-grouping-stable",
        "solution_func": "group_odd_even_stable"
    },
    "016": {
        "id": "LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__7395",
        "name": "lecture-notes-subtract-forward-freq",
        "solution_func": "subtract_with_freq",
        "has_two_lists": True,
        "special_output": True
    }
}

def extract_python_solution(editorial_path):
    """Extract Python solution from editorial"""
    try:
        with open(editorial_path, 'r') as f:
            content = f.read()
        
        # Find Python code section
        pattern = r'### Python\s*```python\n(.*?)\n```'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            py_code = match.group(1)
            # Extract just the solution function (not main)
            lines = py_code.split('\n')
            solution_lines = []
            in_solution = False
            indent_level = 0
            
            for line in lines:
                if line.startswith('def ') and not line.startswith('def main'):
                    in_solution = True
                    indent_level = len(line) - len(line.lstrip())
                    solution_lines.append(line)
                elif in_solution:
                    if line.strip() and not line.startswith(' '):
                        # Reached next top-level item
                        if line.startswith('def ') or line.startswith('class '):
                            # Another function/class, include if it's a helper
                            if not line.startswith('def main'):
                                solution_lines.append(line)
                            else:
                                break
                        else:
                            break
                    else:
                        solution_lines.append(line)
                elif line.startswith('class ListNode'):
                    # Skip ListNode class as we have it in template
                    continue
                    
            return '\n'.join(solution_lines)
        return None
    except Exception as e:
        print(f"Error extracting solution: {e}")
        return None

def create_generator(num, config):
    """Create a test generator for a problem"""
    print(f"Creating generator for LNK-{num}...")
    
    editorial_path = Path(f"../../editorials/LNK-{num}-{config['name']}.md")
    if not editorial_path.exists():
        print(f"  ⚠️  Editorial not found: {editorial_path}")
        return False
    
    solution_code = extract_python_solution(editorial_path)
    if not solution_code:
        print(f"  ⚠️  Could not extract solution from editorial")
        return False
    
    # Create helper code based on problem type
    if config.get('has_two_lists'):
        helper_code = create_two_list_helper(config)
    elif config.get('params'):
        helper_code = create_param_helper(config)
    else:
        helper_code = create_single_list_helper(config)
    
    # Create test cases code
    test_code = create_test_cases(num, config)
    
    # Fill template
    generator_code = BASE_TEMPLATE.format(
        solution_code=solution_code,
        helper_code=helper_code,
        problem_id=config['id'],
        test_cases_code=test_code
    )
    
    # Write to file
    output_file = Path(f"generate_lnk{num}.py")
    with open(output_file, 'w') as f:
        f.write(generator_code)
    
    print(f"  ✅ Created: {output_file}")
    return True

def create_single_list_helper(config):
    """Create helper for single-list problems"""
    func_name = config['solution_func']
    if config.get('returns_bool'):
        return f"""
def solve(values):
    head = array_to_list(values)
    result = {func_name}(head)
    return "YES" if result else "NO"

def make_test_case(values):
    n = len(values)
    result = solve(values)
    input_str = f"{{n}}\\n{{' '.join(map(str, values))}}"
    output_str = result
    return input_str, output_str
"""
    else:
        return f"""
def solve(values):
    head = array_to_list(values)
    result = {func_name}(head)
    return list_to_array(result) if result else []

def make_test_case(values):
    n = len(values)
    result = solve(values)
    input_str = f"{{n}}\\n{{' '.join(map(str, values))}}"
    output_str = ' '.join(map(str, result))
    return input_str, output_str
"""

def create_param_helper(config):
    """Create helper for problems with extra parameters"""
    func_name = config['solution_func']
    params = config.get('params', [])
    param_str = ', '.join(params[1:])  # Exclude 'head'
    param_vars = ', '.join([p for p in params[1:]])
    
    return f"""
def solve(values, {param_vars}):
    head = array_to_list(values)
    result = {func_name}(head, {param_vars})
    return list_to_array(result) if result else []

def make_test_case(values, {param_vars}):
    n = len(values)
    result = solve(values, {param_vars})
    input_str = f"{{n}}\\n{{' '.join(map(str, values))}}\\n{('\\n'.join(['{'+p+'}' for p in params[1:]]))}"
    output_str = ' '.join(map(str, result))
    return input_str, output_str
"""

def create_two_list_helper(config):
    """Create helper for two-list problems"""
    func_name = config['solution_func']
    if config.get('returns_int'):
        return f"""
def solve(values1, values2):
    head1 = array_to_list(values1)
    head2 = array_to_list(values2)
    result = {func_name}(head1, head2)
    return result

def make_test_case(values1, values2):
    n1, n2 = len(values1), len(values2)
    result = solve(values1, values2)
    input_str = f"{{n1}}\\n{{' '.join(map(str, values1))}}\\n{{n2}}\\n{{' '.join(map(str, values2))}}"
    output_str = str(result)
    return input_str, output_str
"""
    else:
        return f"""
def solve(values1, values2):
    head1 = array_to_list(values1)
    head2 = array_to_list(values2)
    result = {func_name}(head1, head2)
    return list_to_array(result) if result else []

def make_test_case(values1, values2):
    n1, n2 = len(values1), len(values2)
    result = solve(values1, values2)
    input_str = f"{{n1}}\\n{{' '.join(map(str, values1))}}\\n{{n2}}\\n{{' '.join(map(str, values2))}}"
    output_str = ' '.join(map(str, result))
    return input_str, output_str
"""

def create_test_cases(num, config):
    """Create generic test cases"""
    # Simple generic test cases - will need customization
    return """    # Samples (customize based on problem)
    inp, out = make_test_case([1, 2, 3, 4, 5], 2, 2) if 'params' in {!r} else make_test_case([1, 2, 3])
    test_cases["samples"].append({{"input": inp, "output": out}})
    
    # Public & Hidden - add comprehensive cases
    # TODO: Customize based on problem requirements
    
    for i in range(15):
        vals = [random.randint(1, 100) for _ in range(10)]
        inp, out = make_test_case(vals)
        test_cases["hidden"].append({{"input": inp, "output": out}})
""".format(str(config))

def main():
    print("Batch creating LinkedList test generators (008-016)...\\n")
    
    success_count = 0
   for num, config in PROBLEMS_CONFIG.items():
        if create_generator(num, config):
            success_count += 1
    
    print(f"\\n✅ Successfully created {success_count}/{len(PROBLEMS_CONFIG)} generators!")
    print("⚠️  Note: Generated test cases are basic. Please customize them based on problem requirements.")

if __name__ == "__main__":
    main()
