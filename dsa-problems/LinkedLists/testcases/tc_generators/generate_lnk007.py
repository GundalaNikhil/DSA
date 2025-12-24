import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def weighted_middle_value(head: ListNode) -> int:
    if not head:
        return 0
        
    # Pass 1: Total weight
    total_weight = 0
    curr = head
    while curr:
        total_weight += curr.val
        curr = curr.next
        
    threshold = (total_weight + 1) // 2
    
    # Pass 2: Find node
    current_sum = 0
    curr = head
    while curr:
        current_sum += curr.val
        if current_sum >= threshold:
            return curr.val
        curr = curr.next
        
    return 0

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
    return weighted_middle_value(head)

def make_test_case(values):
    n = len(values)
    result = solve(values)
    input_str = f"{n}\n{' '.join(map(str, values))}"
    output_str = str(result)
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
        "problem_id": "LNK_SEMINAR_WEIGHTED_MIDDLE__4729",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([2, 1, 3, 4])
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 1, 1, 1, 1])
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: Single
    inp, out = make_test_case([5])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Two elements
    inp, out = make_test_case([1, 10])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: Small
    inp, out = make_test_case([1, 2, 3])
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: All same
    inp, out = make_test_case([5, 5, 5, 5])
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: First element dominates
    hidden_cases.append(make_test_case([1000000, 1, 1, 1]))
    
    # 2. Edge: Last element dominates
    hidden_cases.append(make_test_case([1, 1, 1, 1000000]))
    
    # 3. Boundary: Exact half
    hidden_cases.append(make_test_case([5, 5]))
    
    # 4. Boundary: Odd total
    hidden_cases.append(make_test_case([1, 2, 3, 4, 5]))
    
    # 5. Special: Large values
    hidden_cases.append(make_test_case([1000000000] * 5))
    
    # 6. Special: Increasing sequence
    hidden_cases.append(make_test_case(list(range(1, 21))))
    
    # 7. Normal: Random small
    vals = [random.randint(1, 100) for _ in range(20)]
    hidden_cases.append(make_test_case(vals))
    
    # 8. Normal: Random medium
    vals = [random.randint(1, 1000) for _ in range(100)]
    hidden_cases.append(make_test_case(vals))
    
    # 9. Stress: Large count
    vals = [random.randint(1, 1000) for _ in range(10000)]
    hidden_cases.append(make_test_case(vals))
    
    # 10. Stress: Maximum
    vals = [random.randint(1, 100000) for _ in range(100000)]
    hidden_cases.append(make_test_case(vals))
    
    # 11. Edge: Alternating 1 and large
    hidden_cases.append(make_test_case([1, 1000000, 1, 1000000, 1]))
    
    # 12. Special: Powers of 2
    hidden_cases.append(make_test_case([1, 2, 4, 8, 16, 32, 64]))
    
    # 13. Boundary: Two heavy elements
    hidden_cases.append(make_test_case([1, 1, 10000, 10000, 1, 1]))

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
