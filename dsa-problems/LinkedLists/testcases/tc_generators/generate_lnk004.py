import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def deduplicate_at_most_two(head: ListNode) -> ListNode:
    """Remove duplicates keeping at most 2 of each"""
    if not head or not head.next:
        return head
    
    prev = head
    current = head.next
    count = 1
    
    while current:
        if current.val == prev.val:
            count += 1
            if count > 2:
                # Remove current
                prev.next = current.next
                current = current.next
            else:
                # Keep current
                prev = current
                current = current.next
        else:
            # New value
            count = 1
            prev = current
            current = current.next
            
    return head

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def solve(values):
    if not values:
        return []
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    head = deduplicate_at_most_two(dummy.next)
    return list_to_array(head)

# --- Test Case Generators ---

def make_test_case(values):
    n = len(values)
    result = solve(values)
    input_str = f"{n}\n{' '.join(map(str, values))}"
    output_str = ' '.join(map(str, result))
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
        "problem_id": "LNK_HOSTEL_CLEANUP_DEDUPLICATE_TWO__6294",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([1, 1, 1, 2, 2, 3])
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 1, 2, 2, 2, 3, 3, 3, 3])
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: Empty
    inp, out = make_test_case([])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Single
    inp, out = make_test_case([1])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Two same
    inp, out = make_test_case([1, 1])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: All unique
    inp, out = make_test_case([1, 2, 3, 4, 5])
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: All same value
    hidden_cases.append(make_test_case([5] * 10))
    
    # 2. Edge: All duplicates exactly twice
    hidden_cases.append(make_test_case([1, 1, 2, 2, 3, 3, 4, 4]))
    
    # 3. Boundary: Three of each
    hidden_cases.append(make_test_case([1, 1, 1, 2, 2, 2, 3, 3, 3]))
    
    # 4. Boundary: Many duplicates
    hidden_cases.append(make_test_case([1]*5 + [2]*7 + [3]*3))
    
    # 5. Special: Negative values
    hidden_cases.append(make_test_case([-5, -5, -5, -3, -3, 0, 0, 0, 0]))
    
    # 6. Special: Large values
    hidden_cases.append(make_test_case([1000000]*4 + [2000000]*6))
    
    # 7. Normal: Random sorted small
    vals = sorted([random.randint(1, 10) for _ in range(50)])
    hidden_cases.append(make_test_case(vals))
    
    # 8. Normal: Random sorted medium
    vals = sorted([random.randint(1, 100) for _ in range(500)])
    hidden_cases.append(make_test_case(vals))
    
    # 9. Stress: Large with many duplicates
    vals = sorted([random.randint(1, 1000) for _ in range(10000)])
    hidden_cases.append(make_test_case(vals))
    
    # 10. Stress: Maximum size
    vals = sorted([random.randint(-1000000, 1000000) for _ in range(100000)])
    hidden_cases.append(make_test_case(vals))
    
    # 11. Edge: Alternating pattern
    hidden_cases.append(make_test_case([1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5]))
    
    # 12. Edge: Long run at end
    hidden_cases.append(make_test_case([1, 2, 3] + [100]*10))
    
    # 13. Edge: Long run at start
    hidden_cases.append(make_test_case([1]*10 + [50, 51, 52]))

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
