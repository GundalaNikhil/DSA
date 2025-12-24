import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def stable_partition(head: ListNode, x: int) -> ListNode:
    less_head = ListNode(0)
    equal_head = ListNode(0)
    greater_head = ListNode(0)
    
    less = less_head
    equal = equal_head
    greater = greater_head
    
    curr = head
    while curr:
        if curr.val < x:
            less.next = curr
            less = less.next
        elif curr.val == x:
            equal.next = curr
            equal = equal.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next
        
    # Connect
    greater.next = None
    equal.next = greater_head.next
    less.next = equal_head.next if equal_head.next else greater_head.next
    
    return less_head.next

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

def solve(values, x):
    head = array_to_list(values)
    result = stable_partition(head, x)
    return list_to_array(result) if result else []

def make_test_case(values, x):
    n = len(values)
    result = solve(values, x)
    input_str = f"{n}\n{' '.join(map(str, values))}\n{x}"
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
        "problem_id": "LNK_SHUTTLE_ID_STABLE_PARTITION__7184",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([5, 1, 4, 2, 5], 4)
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([3, 5, 8, 5, 10, 2, 1], 5)
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: All less than x
    inp, out = make_test_case([1, 2, 3], 10)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: All equal to x
    inp, out = make_test_case([5, 5, 5], 5)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: All greater than x
    inp, out = make_test_case([10, 20, 30], 5)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: Mixed
    inp, out = make_test_case([1, 5, 3, 5, 7], 5)
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: Single element (less)
    hidden_cases.append(make_test_case([1], 5))
    
    # 2. Edge: Single element (equal)
    hidden_cases.append(make_test_case([5], 5))
    
    # 3. Boundary: Two elements
    hidden_cases.append(make_test_case([7, 3], 5))
    
    # 4. Special: Negative values
    hidden_cases.append(make_test_case([-5, -3, 0, 2, -1], 0))
    
    # 5. Special: All same value
    hidden_cases.append(make_test_case([7]*10, 7))
    
    # 6. Normal: Random small
    vals = [random.randint(-20, 20) for _ in range(20)]
    x = random.choice(vals)
    hidden_cases.append(make_test_case(vals, x))
    
    # 7. Normal: Random medium
    vals = [random.randint(-100, 100) for _ in range(100)]
    x = random.randint(-50, 50)
    hidden_cases.append(make_test_case(vals, x))
    
    # 8. Stress: Large
    vals = [random.randint(-10000, 10000) for _ in range(10000)]
    x = 0
    hidden_cases.append(make_test_case(vals, x))
    
    # 9. Stress: Maximum
    vals = [random.randint(-100000, 100000) for _ in range(100000)]
    x = 0
    hidden_cases.append(make_test_case(vals, x))
    
    # 10. Special: Ascending then x
    vals = list(range(1, 11)) + [5]
    hidden_cases.append(make_test_case(vals, 5))
    
    # 11. Special: Descending
    vals = list(range(20, 0, -1))
    hidden_cases.append(make_test_case(vals, 10))
    
    # 12. Edge: Extreme values
    hidden_cases.append(make_test_case([-2147483648, 0, 2147483647], 0))
    
    # 13. Boundary: Alternating pattern
    vals = [i if i % 2 == 0 else -i for i in range(1, 21)]
    hidden_cases.append(make_test_case(vals, 0))

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
