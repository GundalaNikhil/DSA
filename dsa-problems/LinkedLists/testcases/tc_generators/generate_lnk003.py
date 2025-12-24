import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def swap_with_skip(head: ListNode, K: int):
    """Swap pairs with constraints"""
    if not head or not head.next:
        return head, 0
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    swaps_performed = 0
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Check conditions
        non_negative = (first.val >= 0 and second.val >= 0)
        can_swap = (K > 0)
        
        if non_negative and can_swap:
            # Swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            K -= 1
            swaps_performed += 1
            prev = first
        else:
            # Skip
            prev = second
            
    return dummy.next, swaps_performed

def list_to_array(head):
    """Convert linked list to array"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def solve(values, K):
    """Build list and solve"""
    if not values:
        return [], 0
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    head, swaps = swap_with_skip(dummy.next, K)
    return list_to_array(head), swaps

# --- Test Case Generators ---

def make_test_case(values, K):
    """Generate input and output"""
    n = len(values)
    result, swaps = solve(values, K)
    input_str = f"{n}\n{' '.join(map(str, values))}\n{K}"
    output_str = f"{' '.join(map(str, result))}\n{swaps}"
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
        "problem_id": "LNK_LAB_SWAP_NEIGHBORS_SKIP__5817",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([1, -2, 3, 4, 5, 6], 1)
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 2, 3, 4], 10)
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: Empty list
    inp, out = make_test_case([], 0)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Single element
    inp, out = make_test_case([5], 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: K=0
    inp, out = make_test_case([1, 2, 3, 4], 0)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: All positive, unlimited K
    inp, out = make_test_case([1, 2, 3, 4, 5, 6], 10)
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: All negative
    hidden_cases.append(make_test_case([-1, -2, -3, -4], 10))
    
    # 2. Edge: K larger than possible swaps
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5, 6, 7, 8], 100))
    
    # 3. Boundary: Exactly K swaps possible
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5, 6], 3))
    
    # 4. Boundary: Odd length
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5], 2))
    
    # 5. Special: Alternating negative/positive
    hidden_cases.append(make_test_case([-1, 1, -2, 2, -3, 3], 5))
    
    # 6. Special: First pair negative
    hidden_cases.append(make_test_case([-1, -2, 3, 4, 5, 6], 10))
    
    # 7. Special: Last pair can't swap (K limit)
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5, 6, 7, 8], 2))
    
    # 8. Normal: Random small
    vals = [random.randint(-10, 10) for _ in range(20)]
    K = random.randint(1, 5)
    hidden_cases.append(make_test_case(vals, K))
    
    # 9. Normal: Random medium
    vals = [random.randint(-100, 100) for _ in range(100)]
    K = random.randint(10, 30)
    hidden_cases.append(make_test_case(vals, K))
    
    # 10. Stress: Large list, no negatives
    vals = [random.randint(1, 1000) for _ in range(10000)]
    K = 5000
    hidden_cases.append(make_test_case(vals, K))
    
    # 11. Stress: Large list, many negatives
    vals = [random.randint(-1000, 1000) for _ in range(10000)]
    K = 1000
    hidden_cases.append(make_test_case(vals, K))
    
    # 12. Stress: Maximum size
    vals = [random.randint(1, 100000) for _ in range(100000)]
    K = 50000
    hidden_cases.append(make_test_case(vals, K))
    
    # 13. Edge: Zero values (non-negative)
    hidden_cases.append(make_test_case([0, 0, 0, 0], 2))

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
