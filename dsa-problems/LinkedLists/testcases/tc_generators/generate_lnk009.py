import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverse_segment(head, count):
    prev, curr = None, head
    for _ in range(count):
        if not curr:
            break
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev, head, curr

def reverse_from_offset(head: ListNode, k: int, s: int):
    if not head or k <= 1:
        return head, 0, 0
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to s-1 (s is 1-based)
    for _ in range(s - 1):
        if not prev.next:
            return dummy.next, 0, 0
        prev = prev.next
        
    groups = 0
    total_sum = 0
    
    while True:
        # Probe k steps
        probe = prev
        for _ in range(k):
            probe = probe.next
            if not probe:
                return dummy.next, groups, total_sum
        
        # Reverse k nodes
        tail = prev.next
        curr = tail.next
        group_sum = tail.val
        
        for _ in range(k - 1):
            group_sum += curr.val
            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            tail.next = temp
            curr = temp
            
        groups += 1
        total_sum += group_sum
        prev = tail
        
    return dummy.next, groups, total_sum

def list_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def array_to_list(arr):
    if not arr: return None
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def solve(v, k, s):
    h = array_to_list(v)
    res_head, count, total_sum = reverse_from_offset(h, k, s)
    return list_to_array(res_head), count, total_sum

def make_test_case(v, k, s):
    n = len(v)
    res_vals, count, total_sum = solve(v, k, s)
    inp = f"{n}\n{' '.join(map(str, v))}\n{k}\n{s}"
    out = f"{' '.join(map(str, res_vals))}\n{count}\n{total_sum}"
    return {"input": inp, "output": out}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    test_cases = {"problem_id": "LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6394", "samples": [], "public": [], "hidden": []}
    
    test_cases["samples"].append(make_test_case([1,2,3,4,5], 2, 1))
    test_cases["samples"].append(make_test_case([1,2,3,4,5,6], 3, 0))
    
    for v,k,s in [([1],1,0), ([1,2],1,1), (list(range(1,11)),3,2), (list(range(1,6)),10,0)]:
        test_cases["public"].append(make_test_case(v,k,s))
    
    for _ in range(13):
        n = random.randint(1, 50)
        v = [random.randint(-50,50) for _ in range(n)]
        k = random.randint(1, n+5)
        s = random.randint(0, n)
        test_cases["hidden"].append(make_test_case(v,k,s))
    
    test_cases["hidden"].append(make_test_case(list(range(1,10001)), 500, 100))
    test_cases["hidden"].append(make_test_case(list(range(1,100001)), 5000, 1000))
    
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
