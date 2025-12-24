import sys
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
    ptrA, ptrB = hA, hB
    while la > lb:
        ptrA = ptrA.next
        la -= 1
    while lb > la:
        ptrB = ptrB.next
        lb -= 1
    while ptrA != ptrB:
        ptrA = ptrA.next
        ptrB = ptrB.next
    if not ptrA:
        return 0
    s = 0
    curr = ptrA
    while curr:
        s += curr.val
        curr = curr.next
    return s

def array_to_list(a):
    if not a: return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def make_test_case(v1, v2, ia=-1, ib=-1):
    n, m = len(v1), len(v2)
    hA = array_to_list(v1)
    hB = array_to_list(v2)
    
    # Store nodes in lists for easy indexing
    nodesA = []
    curr = hA
    while curr:
        nodesA.append(curr)
        curr = curr.next
    nodesB = []
    curr = hB
    while curr:
        nodesB.append(curr)
        curr = curr.next
        
    # Apply intersection
    if ia != -1 and ib != -1 and n > 0 and m > 0:
        if ib < m and ia < n:
            nodesB[ib].next = nodesA[ia]
            
    res = intersection_sum(hA, hB)
    
    inp = f"{n} {m}\n{' '.join(map(str, v1)) if v1 else ''}\n{' '.join(map(str, v2)) if v2 else ''}\n{ia} {ib}"
    out = str(res)
    return {"input": inp, "output": out}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_EXAM_SEATING_INTERSECTION_SUM__6385", "samples": [], "public": [], "hidden": []}
    
    # In this problem, we'll assume the intersection is defined by the values if they are shared at the end.
    # But for the generator, we'll just use the list approach.
    
    tc["samples"].append(make_test_case([1,2,3], [4,2,3])) # Intersects at 2
    tc["samples"].append(make_test_case([1,2], [3,4])) # No intersection
    
    for v1,v2 in [([], []), ([1], [2]), ([1,2,3], [4,5]), (list(range(1,6)), list(range(10,15)))]:
        tc["public"].append(make_test_case(v1, v2))
    
    for _ in range(15):
        n1, n2 = random.randint(0,50), random.randint(0,50)
        v1 = [random.randint(-50,50) for _ in range(n1)]
        v2 = [random.randint(-50,50) for _ in range(n2)]
        # Occasionally force intersection
        idx = -1
        if n1 > 0 and random.random() > 0.5:
             idx = random.randint(0, n1-1)
             # Modify v2 to have the same suffix as v1 from idx
             suffix = v1[idx:]
             prefix2 = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
             v2 = prefix2 + suffix
        tc["hidden"].append(make_test_case(v1, v2))
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
