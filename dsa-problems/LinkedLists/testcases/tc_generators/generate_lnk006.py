import sys
import random

# --- Reference Solution ---
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def cycle_info(head: ListNode):
    if not head:
        return (-1, 0, 0)
    
    slow = head
    fast = head
    has_cycle = False
    
    # Phase 1: Detect
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return (-1, 0, 0)
        
    # Phase 2: Find Entry
    entry = head
    entry_index = 0
    while entry != slow:
        entry = entry.next
        slow = slow.next
        entry_index += 1
        
    # Phase 3: Stats
    length = 0
    max_val = -float('inf')
    curr = entry
    while True:
        length += 1
        max_val = max(max_val, curr.val)
        curr = curr.next
        if curr == entry:
            break
            
    return (entry_index, length, max_val)

def build_list_with_cycle(values, pos):
    """Build list with cycle at position pos"""
    if not values:
        return None
    dummy = ListNode()
    cur = dummy
    nodes = []
    for v in values:
        node = ListNode(v)
        cur.next = node
        cur = cur.next
        nodes.append(node)
    if pos >= 0 and pos < len(nodes):
        cur.next = nodes[pos]
    return dummy.next

def make_test_case(values, pos):
    n = len(values)
    head = build_list_with_cycle(values, pos)
    entry, length, max_val = cycle_info(head)
    input_str = f"{n}\n{' '.join(map(str, values))}\n{pos}"
    output_str = f"{entry} {length} {max_val}"
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
        "problem_id": "LNK_LAB_LOOP_DETECTOR_ENTRY_LENGTH__8412",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([1, 2, 3, 4], 1)
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 2, 3, 4, 5], -1)
    test_cases["samples"].append({"input": inp, "output": out})

    # Public
    # Edge: No cycle
    inp, out = make_test_case([1], -1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Self loop
    inp, out = make_test_case([1], 0)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Edge: Two nodes, cycle from second
    inp, out = make_test_case([1, 2], 1)
    test_cases["public"].append({"input": inp, "output": out})
    
    # Basic: Cycle from head
    inp, out = make_test_case([1, 2, 3], 0)
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: Long tail, small cycle
    hidden_cases.append(make_test_case(list(range(1, 21)), 15))
    
    # 2. Edge: Short tail, large cycle
    hidden_cases.append(make_test_case(list(range(1, 21)), 2))
    
    # 3. Boundary: Cycle at last node
    hidden_cases.append(make_test_case(list(range(1, 11)), 9))
    
    # 4. Special: Negative values in cycle
    hidden_cases.append(make_test_case([-5, -3, 10, 20, -1], 2))
    
    # 5. Normal: Medium list with middle cycle
    vals = list(range(1, 51))
    hidden_cases.append(make_test_case(vals, 25))
    
    # 6. Normal: No cycle large list
    vals = list(range(1, 101))
    hidden_cases.append(make_test_case(vals, -1))
    
    # 7. Stress: Large list with cycle
    vals = list(range(1, 10001))
    hidden_cases.append(make_test_case(vals, 5000))
    
    # 8. Stress: Maximum size
    vals = list(range(1, 100001))
    hidden_cases.append(make_test_case(vals, 50000))
    
    # 9. Edge: All same values
    hidden_cases.append(make_test_case([7]*10, 3))
    
    # 10. Edge: Alternating values
    vals = [i if i % 2 == 0 else -i for i in range(1, 21)]
    hidden_cases.append(make_test_case(vals, 10))
    
    # 11. Special: Very large values
    hidden_cases.append(make_test_case([1000000, 2000000, 3000000, 4000000], 1))
    
    # 12. Stress: Cycle at position 0
    vals = list(range(100000, 200000))
    hidden_cases.append(make_test_case(vals, 0))
    
    # 13. Edge: Min values
    hidden_cases.append(make_test_case([-2147483648, 0, 2147483647], 0))

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
