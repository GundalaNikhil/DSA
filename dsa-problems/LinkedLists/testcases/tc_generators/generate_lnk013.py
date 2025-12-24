import sys
import random

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def rotate_list(head, length, k):
    if not head or length == 0:
        return head
    k = k % length
    if k == 0:
        return head
    # Move tail to end
    tail = head
    while tail.next:
        tail = tail.next
    # Make it circular
    tail.next = head
    
    # Find new tail: (length - k - 1)th node
    steps = length - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
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
            # We need to find the next pointer and the end of the block
            curr = curr.next
            length += 1
        
        # Save the rest of the list
        rest = curr
        
        if length > 0:
            # Temporarily terminate block
            # To do this safely, we need to find the last node of the block
            block_curr = block_head
            for _ in range(length - 1):
                block_curr = block_curr.next
            block_curr.next = None
            
            rotated = rotate_list(block_head, length, k)
            prev.next = rotated
            
            # Find new tail of the rotated block
            while prev.next:
                prev = prev.next
            # Reattach the rest
            prev.next = rest
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
    inp = f"{n}\n{' '.join(map(str, v))}\n{b}\n{k}"
    out = ' '.join(map(str, result)) if result else ""
    return {"input": inp, "output": out}

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    tc = {"problem_id": "LNK_SHUTTLE_TICKET_ROTATE_BLOCKS__6385", "samples": [], "public": [], "hidden": []}
    
    tc["samples"].append(make_test_case([1,2,3,4,5,6], 3, 1))
    tc["samples"].append(make_test_case(list(range(1,9)), 2, 1))
    
    for v,b,k in [([], 2, 1), ([1], 1, 0), ([1,2,3,4], 2, 2), (list(range(1,11)), 5, 2)]:
        tc["public"].append(make_test_case(v,b,k))
    
    for _ in range(15):
        n = random.randint(0, 50)
        v = [random.randint(-50,50) for _ in range(n)]
        b = random.randint(1, max(1, n+5))
        k = random.randint(0, 10)
        tc["hidden"].append(make_test_case(v,b,k))
    
    print(f"problem_id: {tc['problem_id']}")
    for section in ["samples", "public", "hidden"]:
        print(f"\n{section}:")
        for c in tc[section]:
            print_case(c)

if __name__ == "__main__":
    main()
