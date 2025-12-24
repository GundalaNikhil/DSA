import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value: int) -> None:
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

def solve(operations):
    """
    Execute operations and return list of outputs for to_array commands.
    operations: list of tuples like ("push_back", value) or ("to_array",)
    """
    sol = Solution()
    outputs = []
    for op in operations:
        if op[0] == "push_back":
            sol.push_back(op[1])
        elif op[0] == "to_array":
            arr = sol.to_array()
            outputs.append(" ".join(str(x) for x in arr))
    return outputs

# --- Test Case Generators ---

def generate_sample_1():
    """Sample from problem statement"""
    ops = [
        ("push_back", 3),
        ("push_back", 7),
        ("to_array",),
        ("push_back", -2),
        ("to_array",)
    ]
    return ops

def generate_edge_empty():
    """Edge: Only to_array on empty list"""
    ops = [("to_array",)]
    return ops

def generate_edge_single():
    """Edge: Single element"""
    ops = [
        ("push_back", 42),
        ("to_array",)
    ]
    return ops

def generate_basic_small():
    """Public: Basic small test"""
    ops = [
        ("push_back", 10),
        ("push_back", 20),
        ("to_array",),
        ("push_back", 30),
        ("to_array",)
    ]
    return ops

def generate_multiple_to_array():
    """Multiple consecutive to_array calls"""
    ops = [
        ("push_back", 1),
        ("to_array",),
        ("to_array",),
        ("push_back", 2),
        ("to_array",),
        ("to_array",)
    ]
    return ops

def generate_random(n_push, n_to_array, min_val=-1000, max_val=1000):
    """Generate random operations"""
    ops = []
    # First add some push operations
    for _ in range(n_push):
        ops.append(("push_back", random.randint(min_val, max_val)))
    # Intersperse to_array operations
    positions = sorted(random.sample(range(len(ops) + n_to_array), n_to_array))
    for pos in reversed(positions):
        ops.insert(pos, ("to_array",))
    return ops

def generate_stress_large():
    """Stress: Large number of operations"""
    ops = []
    for i in range(50000):
        ops.append(("push_back", i))
    # Add to_array periodically
    for i in range(0, 50000, 10000):
        ops.insert(i, ("to_array",))
    ops.append(("to_array",))
    return ops

def generate_all_negatives():
    """Special: All negative values"""
    ops = []
    for i in range(10):
        ops.append(("push_back", -i-1))
    ops.append(("to_array",))
    return ops

# --- YAML Builder ---

def format_input(operations):
    """Format operations into input string"""
    lines = [str(len(operations))]
    for op in operations:
        if op[0] == "push_back":
            lines.append(f"push_back {op[1]}")
        else:
            lines.append("to_array")
    return "\n".join(lines)

def format_output(outputs):
    """Format output list"""
    return "\n".join(outputs)

def make_test_case(operations):
    """Generate input and output for given operations"""
    input_str = format_input(operations)
    output_list = solve(operations)
    output_str = format_output(output_list)
    return input_str, output_str

def print_case(c):
    """Print a test case in YAML format"""
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    test_cases = {
        "problem_id": "LNK_LAB_ROSTER_APPEND__3582",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    ops = generate_sample_1()
    test_cases["samples"].append({"input": format_input(ops), "output": format_output(solve(ops))})

    # Public
    # Edge: Empty list
    ops = generate_edge_empty()
    test_cases["public"].append({"input": format_input(ops), "output": format_output(solve(ops))})
    
    # Edge: Single element
    ops = generate_edge_single()
    test_cases["public"].append({"input": format_input(ops), "output": format_output(solve(ops))})
    
    # Basic small
    ops = generate_basic_small()
    test_cases["public"].append({"input": format_input(ops), "output": format_output(solve(ops))})
    
    # Multiple to_array
    ops = generate_multiple_to_array()
    test_cases["public"].append({"input": format_input(ops), "output": format_output(solve(ops))})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: Only to_array operations
    ops = [("to_array",)] * 5
    hidden_cases.append(make_test_case(ops))
    
    # 2. Edge: Large single value
    ops = [("push_back", 2147483647), ("to_array",)]
    hidden_cases.append(make_test_case(ops))
    
    # 3. Boundary: Minimum value
    ops = [("push_back", -2147483648), ("to_array",)]
    hidden_cases.append(make_test_case(ops))
    
    # 4. Special: All same values
    ops = [("push_back", 7)] * 100
    ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))
    
    # 5. Special: All negative
    ops = generate_all_negatives()
    hidden_cases.append(make_test_case(ops))
    
    # 6. Normal: Random small
    ops = generate_random(50, 10, -100, 100)
    hidden_cases.append(make_test_case(ops))
    
    # 7. Normal: Random medium
    ops = generate_random(500, 50, -10000, 10000)
    hidden_cases.append(make_test_case(ops))
    
    # 8. Normal: Ascending sequence
    ops = []
    for i in range(100):
        ops.append(("push_back", i))
    ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))
    
    # 9. Normal: Descending sequence
    ops = []
    for i in range(100, 0, -1):
        ops.append(("push_back", i))
    ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))
    
    # 10. Stress: Large with periodic queries
    ops = []
    for i in range(10000):
        ops.append(("push_back", i % 1000))
        if i % 1000 == 0:
            ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))
    
    # 11. Stress: Maximum operations
    ops = []
    for i in range(99000):
        ops.append(("push_back", random.randint(-100000, 100000)))
    # Add to_array at strategic points
    for i in [1000, 5000, 10000, 50000, 99000]:
        ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))
    
    # 12. Edge: Alternating positive/negative
    ops = []
    for i in range(100):
        ops.append(("push_back", i if i % 2 == 0 else -i))
    ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))
    
    # 13. Stress: Many to_array calls
    ops = []
    for i in range(1000):
        ops.append(("push_back", i))
    for _ in range(100):
        ops.append(("to_array",))
    hidden_cases.append(make_test_case(ops))

    for inp, out in hidden_cases:
        test_cases["hidden"].append({"input": inp, "output": out})

    # Output YAML
    print(f"problem_id: {test_cases['problem_id']}")
    print("samples:")
    for c in test_cases["samples"]:
        print_case(c)
    print("\npublic:")
    for c in test_cases["public"]:
        print_case(c)
    print("\nhidden:")
    for c in test_cases["hidden"]:
        print_case(c)

if __name__ == "__main__":
    main()
