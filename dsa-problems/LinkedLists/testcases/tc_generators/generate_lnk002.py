import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def find_first_index(head: ListNode, target: int) -> int:
    """Find first occurrence of target in linked list"""
    index = 0
    current = head
    while current:
        if current.val == target:
            return index
        current = current.next
        index += 1
    return -1

def solve(values, target):
    """Build list and find target"""
    if not values:
        return -1
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return find_first_index(dummy.next, target)

# --- Test Case Generators ---

def make_test_case(values, target):
    """Generate input and output"""
    n = len(values)
    input_str = f"{n}\n{' '.join(map(str, values))}\n{target}"
    output_str = str(solve(values, target))
    return input_str, output_str

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    test_cases = {
        "problem_id": "LNK_CAMPUS_BADGE_SEARCH__7294",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    test_cases["samples"].append({"input": "4\n5 1 5 9\n9", "output": "3"})
    test_cases["samples"].append({"input": "4\n5 1 5 9\n5", "output": "0"})

    # Public
    # Edge: Single element found
    test_cases["public"].append(make_test_case([42], 42)[0] + "\n" + make_test_case([42], 42)[1])
    inp, out = make_test_case([42], 42)
    test_cases["public"][-1] = {"input": inp, "output": out}
    
    # Edge: Single element not found
    inp, out = make_test_case([42], 10)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Target at end
    inp, out = make_test_case([1, 2, 3, 4, 5], 5)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Duplicates - finds first
    inp, out = make_test_case([7, 7, 7], 7)
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: Not found in large list
    vals = list(range(100))
    hidden_cases.append(make_test_case(vals, 200))
    
    # 2. Edge: Found at very beginning (large list)
    vals = list(range(1000))
    hidden_cases.append(make_test_case(vals, 0))
    
    # 3. Edge: Found at very end (large list)
    vals = list(range(1000))
    hidden_cases.append(make_test_case(vals, 999))
    
    # 4. Boundary: All same value
    vals = [42] * 100
    hidden_cases.append(make_test_case(vals, 42))
    
    # 5. Boundary: All different, not found
    vals = list(range(100))
    hidden_cases.append(make_test_case(vals, -1))
    
    # 6. Special: Negative values
    vals = [-10, -5, -3, -1, 0, 1, 3]
    hidden_cases.append(make_test_case(vals, -3))
    
    # 7. Special: Multiple duplicates
    vals = [1, 2, 3, 2, 4, 2, 5]
    hidden_cases.append(make_test_case(vals, 2))
    
    # 8. Normal: Random medium
    vals = [random.randint(-1000, 1000) for _ in range(100)]
    target = vals[random.randint(0, 99)]
    hidden_cases.append(make_test_case(vals, target))
    
    # 9. Normal: Random large (found)
    vals = [random.randint(-10000, 10000) for _ in range(10000)]
    target = vals[random.randint(0, 9999)]
    hidden_cases.append(make_test_case(vals, target))
    
    # 10. Normal: Random large (not found)
    vals = [random.randint(0, 50000) for _ in range(10000)]
    target = -999999
    hidden_cases.append(make_test_case(vals, target))
    
    # 11. Stress: Maximum size
    vals = [random.randint(-1000000, 1000000) for _ in range(100000)]
    target = vals[50000]  # Middle
    hidden_cases.append(make_test_case(vals, target))
    
    # 12. Stress: Maximum size, target at end
    vals = [random.randint(-1000000, 1000000) for _ in range(100000)]
    vals[99999] = 777777
    target = 777777
    hidden_cases.append(make_test_case(vals, target))
    
    # 13. Edge: Extreme values
    vals = [-2147483648, 0, 2147483647]
    hidden_cases.append(make_test_case(vals, 2147483647))

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
