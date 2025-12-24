import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# Merges two lists: evens from l1, odds from l2, then remaining from both
def merge_by_parity(l1: ListNode, l2: ListNode) -> ListNode:
    even_dummy = ListNode(0)
    odd_dummy = ListNode(0)
    even_tail = even_dummy
    odd_tail = odd_dummy
    
    # Process L1
    curr = l1
    while curr:
        if curr.val % 2 == 0:
            even_tail.next = ListNode(curr.val)
            even_tail = even_tail.next
        else:
            odd_tail.next = ListNode(curr.val)
            odd_tail = odd_tail.next
        curr = curr.next
        
    # Process L2
    curr = l2
    while curr:
        if curr.val % 2 == 0:
            even_tail.next = ListNode(curr.val)
            even_tail = even_tail.next
        else:
            odd_tail.next = ListNode(curr.val)
            odd_tail = odd_tail.next
        curr = curr.next
        
    # Connect
    even_tail.next = odd_dummy.next
    return even_dummy.next

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

def solve(v1, v2):
    h1 = array_to_list(v1)
    h2 = array_to_list(v2)
    result = merge_by_parity(h1, h2)
    return list_to_array(result) if result else []

def make_test_case(v1, v2):
    n1, n2 = len(v1), len(v2)
    result = solve(v1, v2)
    input_str = f"{n1}\n{' '.join(map(str, v1))}\n{n2}\n{' '.join(map(str, v2))}"
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
        "problem_id": "LNK_LAB_PLAYLIST_MERGE_PARITY__5829",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    inp, out = make_test_case([2, 3], [4, 5])
    test_cases["samples"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 2, 3], [4, 5, 6])
    test_cases["samples"].append({"input": inp, "output": out})

    # Public  
    inp, out = make_test_case([], [])
    test_cases["public"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1], [2])
    test_cases["public"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([2, 4], [1, 3])
    test_cases["public"].append({"input": inp, "output": out})
    
    inp, out = make_test_case([1, 3, 5], [2, 4, 6])
    test_cases["public"].append({"input": inp, "output": out})

    # Hidden
    hidden_cases = []
    for _ in range(13):
        n1 = random.randint(0, 50)
        n2 = random.randint(0, 50)
        v1 = [random.randint(-50, 50) for _ in range(n1)]
        v2 = [random.randint(-50, 50) for _ in range(n2)]
        hidden_cases.append(make_test_case(v1, v2))
    
    # Add stress tests
    v1 = [random.randint(1, 10000) for _ in range(1000)]
    v2 = [random.randint(1, 10000) for _ in range(1000)]
    hidden_cases.append(make_test_case(v1, v2))
    
    v1 = [random.randint(1, 100000) for _ in range(50000)]
    v2 = [random.randint(1, 100000) for _ in range(50000)]
    hidden_cases.append(make_test_case(v1, v2))

    for inp, out in hidden_cases:
        test_cases["hidden"].append({"input": inp, "output": out})

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
