#!/usr/bin/env python3
"""Create final 5 LinkedList generators quickly"""

# Generator templates for remaining problems
GENERATORS = {
    "009": '''import sys
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
    if not head or k <= 0 or s < 0:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    for _ in range(s):
        if not prev.next:
            return dummy.next
        prev = prev.next
    if not prev.next:
        return dummy.next
    new_head, old_head, rest = reverse_segment(prev.next, k)
    prev.next = new_head
    old_head.next = rest
    return dummy.next

def list_to_array(h):
    r = []
    while h:
        r.append(h.val)
        h = h.next
    return r

def array_to_list(a):
    if not a:
        return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def solve(v, k, s):
    h = array_to_list(v)
    result = reverse_from_offset(h, k, s)
    return list_to_array(result) if result else []

def make_test_case(v, k, s):
    n = len(v)
    result = solve(v, k, s)
    inp = f"{n}\\n{' '.join(map(str, v))}\\n{k}\\n{s}"
    out = ' '.join(map(str, result)) if result else ""
    return inp, out

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {line}")

def main():
    test_cases = {"problem_id": "LNK_ROBOTICS_CHUNK_REVERSE_OFFSET_COUNT__6394", "samples": [], "public": [], "hidden": []}
    
    test_cases["samples"].append({"input": *make_test_case([1,2,3,4,5], 2, 1)})
    test_cases["samples"].append({"input": *make_test_case([1,2,3,4,5,6], 3, 0)})
    
    for v,k,s in [([1],1,0), ([1,2],1,1), (list(range(1,11)),3,2), (list(range(1,6)),10,0)]:
        test_cases["public"].append({"input": *make_test_case(v,k,s)})
    
    for _ in range(13):
        n = random.randint(1, 50)
        v = [random.randint(-50,50) for _ in range(n)]
        k = random.randint(1, n+5)
        s = random.randint(0, n)
        test_cases["hidden"].append({"input": *make_test_case(v,k,s)})
    
    test_cases["hidden"].append({"input": *make_test_case(list(range(1,10001)), 500, 100)})
    test_cases["hidden"].append({"input": *make_test_case(list(range(1,100001)), 5000, 1000)})
    
    print(f"problem_id: {test_cases['problem_id']}")
    print("samples:")
    for c in test_cases["samples"]:
        print_case(c)
    print("\\npublic:")
    for c in test_cases["public"]:
        print_case(c)
    print("\\nhidden:")
    for c in test_cases["hidden"]:
        print_case(c)

if __name__ == "__main__":
    main()
''',

    "011": '''import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def get_length(h):
    l = 0
    while h:
        l += 1
        h = h.next
    return l

def intersection_sum(hA, hB):
    la, lb = get_length(hA), get_length(hB)
    while la > lb:
        hA = hA.next
        la -= 1
    while lb > la:
        hB = hB.next
        lb -= 1
    while hA and hB and hA != hB:
        hA = hA.next
        hB = hB.next
    if not hA:
        return 0
    s = 0
    while hA:
        s += hA.val
        hA = hA.next
    return s

def array_to_list(a):
    if not a:
        return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def solve(v1, v2):
    h1 = array_to_list(v1)
    h2 = array_to_list(v2)
    return intersection_sum(h1, h2)

def make_test_case(v1, v2):
    n1, n2 = len(v1), len(v2)
    result = solve(v1, v2)
    inp = f"{n1}\\n{' '.join(map(str, v1))}\\n{n2}\\n{' '.join(map(str, v2))}"
    return inp, str(result)

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_EXAM_SEATING_INTERSECTION_SUM__6385", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append({"input": *make_test_case([1,2,3], [4,5,6])})
    tc["samples"].append({"input": *make_test_case([1,2], [3,4])})
    
    for v1,v2 in [([], []), ([1], [2]), ([1,2,3], [4,5]), (list(range(1,6)), list(range(6,11)))]:
        tc["public"].append({"input": *make_test_case(v1, v2)})
    
    for _ in range(15):
        n1, n2 = random.randint(0,50), random.randint(0,50)
        v1 = [random.randint(-50,50) for _ in range(n1)]
        v2 = [random.randint(-50,50) for _ in range(n2)]
        tc["hidden"].append({"input": *make_test_case(v1, v2)})
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
''',

    "013": '''import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def rotate_list(head, length, k):
    if not head or k == 0:
        return head
    k = k % length if length > 0 else 0
    if k == 0:
        return head
    tail, curr = head, head
    for _ in range(length - k - 1):
        curr = curr.next
    new_head = curr.next
    curr.next = None
    curr = new_head
    while curr and curr.next:
        curr = curr.next
    if curr:
        curr.next = head
    return new_head

def rotate_blocks(head, b, k):
    if not head or b <= 0:
        return head
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while prev.next:
        block_head = prev.next
        curr, length = block_head, 0
        while curr and length < b:
            curr = curr.next
            length += 1
        if length.0:
            rotated = rotate_list(block_head, length, k)
            prev.next = rotated
            while prev.next:
                prev = prev.next
        else:
            break
    return dummy.next

def list_to_array(h):
    r = []
    while h:
        r.append(h.val)
        h = h.next
    return r

def array_to_list(a):
    if not a:
        return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def solve(v, b, k):
    h = array_to_list(v)
    result = rotate_blocks(h, b, k)
    return list_to_array(result) if result else []

def make_test_case(v, b, k):
    n = len(v)
    result = solve(v, b, k)
    inp = f"{n}\\n{' '.join(map(str, v))}\\n{b}\\n{k}"
    out = ' '.join(map(str, result)) if result else ""
    return inp, out

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__6385", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append({"input": *make_test_case([1,2,3,4,5,6], 3, 1)})
    tc["samples"].append({"input": *make_test_case(list(range(1,9)), 2, 1)})
    
    for v,b,k in [([], 2, 1), ([1], 1, 0), ([1,2,3,4], 2, 2), (list(range(1,11)), 5, 2)]:
        tc["public"].append({"input": *make_test_case(v,b,k)})
    
    for _ in range(15):
        n = random.randint(0, 50)
        v = [random.randint(-50,50) for _ in range(n)]
        b = random.randint(1, max(1, n+5))
        k = random.randint(0, 10)
        tc["hidden"].append({"input": *make_test_case(v,b,k)})
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
''',

    "014": '''import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def is_palindrome_skip_one(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    n = len(vals)
    def check(arr):
        return arr == arr[::-1]
    if check(vals):
        return True
    for i in range(n):
        if check(vals[:i] + vals[i+1:]):
            return True
    return False

def array_to_list(a):
    if not a:
        return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def solve(v):
    h = array_to_list(v)
    return "YES" if is_palindrome_skip_one(h) else "NO"

def make_test_case(v):
    n = len(v)
    result = solve(v)
    inp = f"{n}\\n{' '.join(map(str, v))}"
    return inp, result

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_ROBOTICS_PALINDROME_ONE_SKIP__5829", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append({"input": *make_test_case([1,2,1])})
    tc["samples"].append({"input": *make_test_case([1,2,3,2,1])})
    
    for v in [[], [1], [1,1], [1,2], [1,2,3,4,3,2,1], [1,2,2,1]]:
        tc["public"].append({"input": *make_test_case(v)})
    
    for _ in range(15):
        n = random.randint(0, 30)
        v = [random.randint(1,10) for _ in range(n)]
        tc["hidden"].append({"input": *make_test_case(v)})
    
   print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
''',

    "016": '''import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def get_length(h):
    l = 0
    while h:
        l += 1
        h = h.next
    return l

def subtract_with_freq(a, b):
    from collections import Counter
    avals, bvals = [], []
    while a:
        avals.append(a.val)
        a = a.next
    while b:
        bvals.append(b.val)
        b = b.next
    
    b_count = Counter(bvals)
    result, freq = [], 0
    for val in avals:
        if b_count[val] > 0:
            b_count[val] -= 1
            freq += 1
        else:
            result.append(val)
    return result, freq

def array_to_list(a):
    if not a:
        return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def solve(v1, v2):
    h1 = array_to_list(v1)
    h2 = array_to_list(v2)
    res, freq = subtract_with_freq(h1, h2)
    return res, freq

def make_test_case(v1, v2):
    n1, n2 = len(v1), len(v2)
    result, freq = solve(v1, v2)
    inp = f"{n1}\\n{' '.join(map(str, v1))}\\n{n2}\\n{' '.join(map(str, v2))}"
    out = f"{' '.join(map(str, result)) if result else ''}\\n{freq}"
    return inp, out

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__7395", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append({"input": *make_test_case([1,2,3,4], [2,4])})
    tc["samples"].append({"input": *make_test_case([1,2,2,3], [2,2])})
    
    for v1,v2 in [([], []), ([1], []), ([1,2], [1]), ([1,2,3], [4,5]), (list(range(1,6)), [2,4])]:
        tc["public"].append({"input": *make_test_case(v1, v2)})
    
    for _ in range(15):
        n1, n2 = random.randint(0,50), random.randint(0,30)
        v1 = [random.randint(1,20) for _ in range(n1)]
        v2 = [random.randint(1,20) for _ in range(n2)]
        tc["hidden"].append({"input": *make_test_case(v1, v2)})
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
'''
}

# Write all generators
import os
for num, code in GENERATORS.items():
    filename = f"generate_lnk{num}.py"
    with open(filename, 'w') as f:
        f.write(code)
    print(f"✅ Created {filename}")

print(f"\n✨ Created {len(GENERATORS)} generators!")
print("Run them with: for f in generate_lnk{{009,011,013,014,016}}.py; do python3 $f > ../LNK-*.yaml; done")
