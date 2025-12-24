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

def subtract_with_freq(a, b):
    # Determine which is larger
    avals, bvals = [], []
    curr = a
    while curr:
        avals.append(curr.val)
        curr = curr.next
    curr = b
    while curr:
        bvals.append(curr.val)
        curr = curr.next
    
    n, m = len(avals), len(bvals)
    large, small = avals, bvals
    sign = 1
    
    if n < m:
        large, small = bvals, avals
        sign = 1 # Signs are handled relative to Large - Small
    elif n == m:
        if avals == bvals:
            return 0, [0], [1] + [0]*9
        if avals < bvals:
            large, small = bvals, avals
            
    # Subtraction A - B (where A >= B)
    # Pad B with leading zeros
    small = [0] * (len(large) - len(small)) + small
    
    res = []
    borrow = 0
    for i in range(len(large) - 1, -1, -1):
        diff = large[i] - small[i] - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        res.append(diff)
    
    res.reverse()
    # Remove leading zeros
    while len(res) > 1 and res[0] == 0:
        res.pop(0)
        
    freq = [0] * 10
    for digit in res:
        freq[digit] += 1
        
    return sign, res, freq

def array_to_list(a):
    if not a: return None
    d = ListNode()
    c = d
    for v in a:
        c.next = ListNode(v)
        c = c.next
    return d.next

def solve(v1, v2):
    h1 = array_to_list(v1)
    h2 = array_to_list(v2)
    sign, res_vals, freq = subtract_with_freq(h1, h2)
    return sign, res_vals, freq

def make_test_case(v1, v2):
    n1, n2 = len(v1), len(v2)
    sign, res_vals, freq = solve(v1, v2)
    inp = f"{n1}\n{' '.join(map(str, v1)) if v1 else ''}\n{n2}\n{' '.join(map(str, v2)) if v2 else ''}"
    out = f"{sign}\n{' '.join(map(str, res_vals))}\n{' '.join(map(str, freq))}"
    return {"input": inp, "output": out}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__7395", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append(make_test_case([1,2,3,4], [2,4]))
    tc["samples"].append(make_test_case([1,2,2,3], [2,2]))
    
    for v1,v2 in [([], []), ([1], []), ([1,2], [1]), ([1,2,3], [4,5]), (list(range(1,6)), [2,4])]:
        tc["public"].append(make_test_case(v1, v2))
    
    for _ in range(15):
        n1, n2 = random.randint(0, 50), random.randint(0, 30)
        v1 = [random.randint(0, 9) for _ in range(n1)]
        v2 = [random.randint(0, 9) for _ in range(n2)]
        tc["hidden"].append(make_test_case(v1, v2))
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
