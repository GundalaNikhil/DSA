import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def remove_mth(head: ListNode, M: int) -> ListNode:
    if M <= 0:
        return head
        
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    
    # Move to M-1
    for _ in range(M - 1):
        if not curr:
            return head
        curr = curr.next
        
    if curr and curr.next:
        curr.next = curr.next.next
        
    return dummy.next

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

def solve(values, M):
    head = array_to_list(values)
    result = remove_mth(head, M)
    return list_to_array(result) if result else []

def make_test_case(values, M):
    n = len(values)
    result = solve(values, M)
    input_str = f"{n}\n{' '.join(map(str, values))}\n{M}"
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
        "problem_id": "LNK_HOSTEL_NUMBER_REMOVE_MTH__4285",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([9, 8, 7, 6], 2)
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 2, 3, 4, 5], 1)
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: M=1 (remove head)
    inp, out = make_test_case([1, 2, 3], 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: M > n
    inp, out = make_test_case([1, 2, 3], 10)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Single element, M=1
    inp, out = make_test_case([5], 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: Remove middle
    inp, out = make_test_case([1, 2, 3, 4, 5], 3)
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: Remove last
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5], 5))
    
    # 2. Edge: Two elements, remove first
    hidden_cases.append(make_test_case([1, 2], 1))
    
    # 3. Edge: Two elements, remove second
    hidden_cases.append(make_test_case([1, 2], 2))
    
    # 4. Boundary: M=0 (invalid)
    hidden_cases.append(make_test_case([1, 2, 3], 0))
    
    # 5. Special: Negative values
    hidden_cases.append(make_test_case([-5, -3, 0, 2], 2))
    
    # 6. Normal: Random small
    vals = [random.randint(-20, 20) for _ in range(10)]
    M = random.randint(1, len(vals))
    hidden_cases.append(make_test_case(vals, M))
    
    # 7. Normal: Random medium
    vals = [random.randint(-100, 100) for _ in range(100)]
    M = random.randint(1, len(vals))
    hidden_cases.append(make_test_case(vals, M))
    
    # 8. Stress: Large list
    vals = list(range(1, 10001))
    M = 5000
    hidden_cases.append(make_test_case(vals, M))
    
    # 9. Stress: Remove first from large
    vals = list(range(1, 100001))
    M = 1
    hidden_cases.append(make_test_case(vals, M))
    
    # 10. Stress: Remove last from large
    vals = list(range(1, 100001))
    M = len(vals)
    hidden_cases.append(make_test_case(vals, M))
    
    # 11. Edge: All same values
    hidden_cases.append(make_test_case([7]*10, 5))
    
    # 12. Special: M way out of bounds
    hidden_cases.append(make_test_case([1, 2, 3], 1000000))
    
    # 13. Boundary: Exact length
    vals = list(range(1, 21))
    hidden_cases.append(make_test_case(vals, len(vals)))

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
