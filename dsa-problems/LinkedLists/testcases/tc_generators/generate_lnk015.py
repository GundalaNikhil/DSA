import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def group_odd_even_stable(head: ListNode) -> ListNode:
    odd_dummy = ListNode(0)
    even_dummy = ListNode(0)
    odd_tail = odd_dummy
    even_tail = even_dummy
    
    curr = head
    while curr:
        if curr.val % 2 != 0:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:
            even_tail.next = curr
            even_tail = even_tail.next
        curr = curr.next
        
    even_tail.next = None
    odd_tail.next = even_dummy.next
    
    return odd_dummy.next

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

def solve(values):
    head = array_to_list(values)
    result = group_odd_even_stable(head)
    return list_to_array(result) if result else []

def make_test_case(values):
    n = len(values)
    result = solve(values)
    input_str = f"{n}\n{' '.join(map(str, values))}"
    output_str = ' '.join(map(str, result)) if result else ""
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
        "problem_id": "LNK_WORKSHOP_ODD_EVEN_GROUPING_STABLE__5392",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([2, 5, 4, 7])
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 2, 3, 4, 5])
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: All odd
    inp, out = make_test_case([1, 3, 5, 7])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: All even
    inp, out = make_test_case([2, 4, 6, 8])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Single odd
    inp, out = make_test_case([3])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: Mixed
    inp, out = make_test_case([10, 1, 8, 3, 6, 5])
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: Alternating
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5, 6, 7, 8]))
    
   # 2. Edge: Two elements (odd, even)
    hidden_cases.append(make_test_case([3, 4]))
    
    # 3. Edge: Two elements (even, odd)
    hidden_cases.append(make_test_case([4, 3]))
    
    # 4. Special: With zeros
    hidden_cases.append(make_test_case([0, 1, 0, 3, 0, 5]))
    
    # 5. Special: Negative values
    hidden_cases.append(make_test_case([-5, -2, -3, 0, 1, 2]))
    
    # 6. Normal: Random small
    vals = [random.randint(-20, 20) for _ in range(20)]
    hidden_cases.append(make_test_case(vals))
    
    # 7. Normal: Random medium
    vals = [random.randint(-100, 100) for _ in range(100)]
    hidden_cases.append(make_test_case(vals))
    
    # 8. Stress: Large with all odd
    vals = [random.randint(0, 10000) * 2 + 1 for _ in range(10000)]
    hidden_cases.append(make_test_case(vals))
    
    # 9. Stress: Large with all even
    vals = [random.randint(0, 10000) * 2 for _ in range(10000)]
    hidden_cases.append(make_test_case(vals))
    
    # 10. Stress: Maximum mixed
    vals = [random.randint(-100000, 100000) for _ in range(100000)]
    hidden_cases.append(make_test_case(vals))
    
    # 11. Special: Decreasing sequence
    hidden_cases.append(make_test_case(list(range(20, 0, -1))))
    
    # 12. Edge: Large values
    hidden_cases.append(make_test_case([2147483647, 2147483646, -2147483648, -2147483647]))
    
    # 13. Boundary: Many duplicates
    hidden_cases.append(make_test_case([1, 1, 1, 2, 2, 2, 3, 3, 3]))

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
