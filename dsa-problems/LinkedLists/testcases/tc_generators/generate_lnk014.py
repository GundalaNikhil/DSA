import sys
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
    if n <= 2:
        return True # Can always skip one or it's already a palindrome
        
    def check(arr):
        return arr == arr[::-1]
    
    if check(vals):
        return True
        
    # Standard algorithm for "Valid Palindrome II" but for linked list values
    l, r = 0, n - 1
    while l < r:
        if vals[l] == vals[r]:
            l += 1
            r -= 1
        else:
            # Try skipping either left or right
            skip_l = vals[l+1 : r+1]
            skip_r = vals[l : r]
            return check(skip_l) or check(skip_r)
    return True

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
    return "true" if is_palindrome_skip_one(h) else "false"

def make_test_case(v):
    n = len(v)
    result = solve(v)
    inp = f"{n}\n{' '.join(map(str, v))}"
    return {"input": inp, "output": result}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_ROBOTICS_PALINDROME_ONE_SKIP__5829", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append(make_test_case([1,2,1]))
    tc["samples"].append(make_test_case([1,2,3,2,1]))
    
    for v in [[], [1], [1,1], [1,2], [1,2,3,4,3,2,1], [1,2,2,1], [1,2,3,1]]:
        tc["public"].append(make_test_case(v))
    
    for _ in range(15):
        n = random.randint(1, 40)
        # Create a mostly palindrome list
        half = [random.randint(1, 10) for _ in range(n // 2)]
        v = half + ([random.randint(1,10)] if n % 2 != 0 else []) + half[::-1]
        if random.random() > 0.3:
            # Add one error
            pos = random.randint(0, n-1)
            v.insert(pos, random.randint(1, 10))
        if random.random() > 0.7:
             # Add more errors
             for _ in range(2):
                  pos = random.randint(0, len(v)-1)
                  v.insert(pos, random.randint(1, 10))
        tc["hidden"].append(make_test_case(v))
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
