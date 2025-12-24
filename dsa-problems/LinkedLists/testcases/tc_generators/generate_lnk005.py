import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def alternating_reverse(head: ListNode, l: int, k: int) -> ListNode:
    """Alternating reverse: reverse k, skip k, repeat from position l"""
    if not head or k <= 1:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to start position l
    for _ in range(l - 1):
        if not prev.next:
            return head
        prev = prev.next
        
    reverse_turn = True
    
    while prev.next:
        if reverse_turn:
            # Reverse next k nodes
            tail = prev.next
            curr = tail.next
            count = 1
            while curr and count < k:
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                tail.next = temp
                curr = temp
                count += 1
            prev = tail # Move prev to end of reversed block
        else:
            # Skip k nodes
            count = 0
            while prev.next and count < k:
                prev = prev.next
                count += 1
        
        reverse_turn = not reverse_turn
        
    return dummy.next

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def solve(values, l, k):
    if not values:
        return []
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    head = alternating_reverse(dummy.next, l, k)
    return list_to_array(head)

# --- Test Case Generators ---

def make_test_case(values, l, k):
    n = len(values)
    result = solve(values, l, k)
    input_str = f"{n}\n{' '.join(map(str, values))}\n{l}\n{k}"
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
        "problem_id": "LNK_SHUTTLE_ROUTE_ALTERNATING_REVERSE__5831",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([1, 2, 3, 4, 5, 6, 7], 2, 2)
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 2, 3, 4, 5], 1, 2)
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: Empty
    inp, out = make_test_case([], 1, 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Single
    inp, out = make_test_case([1], 1, 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: k=1
    inp, out = make_test_case([1, 2, 3, 4], 1, 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: l=n (start from last)
    inp, out = make_test_case([1, 2, 3, 4, 5], 5, 2)
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: k > n
    hidden_cases.append(make_test_case([1, 2, 3], 1, 10))
    
    # 2. Edge: l > n
    hidden_cases.append(make_test_case([1, 2, 3], 10, 2))
    
    # 3. Boundary: Exact blocks
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5, 6], 1, 3))
    
    # 4. Boundary: Partial last block on reverse turn
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5, 6, 7], 1, 3))
    
    # 5. Special: Large k
    hidden_cases.append(make_test_case(list(range(1, 21)), 1, 5))
    
    # 6. Special: From middle
    hidden_cases.append(make_test_case(list(range(1, 11)), 5, 2))
    
    # 7. Normal: Random small
    vals = list(range(1, 21))
    random.shuffle(vals)
    hidden_cases.append(make_test_case(vals, 3, 4))
    
    # 8. Normal: Random medium
    vals = list(range(1, 101))
    hidden_cases.append(make_test_case(vals, 10, 7))
    
    # 9. Stress: Large list
    vals = list(range(1, 10001))
    hidden_cases.append(make_test_case(vals, 100, 50))
    
    # 10. Stress: Maximum size
    vals = list(range(1, 100001))
    hidden_cases.append(make_test_case(vals, 1, 1000))
    
    # 11. Edge: Negative values
    hidden_cases.append(make_test_case([-5, -4, -3, -2, -1, 0, 1, 2], 1, 3))
    
    # 12. Edge: All skip (l from end, k large)
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5], 4, 10))
    
    # 13. Special: k=2 pattern
    hidden_cases.append(make_test_case(list(range(1, 21)), 1, 2))

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
