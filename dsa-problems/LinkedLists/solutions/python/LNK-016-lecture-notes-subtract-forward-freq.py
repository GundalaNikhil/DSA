import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def get_length(head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l

def subtract_with_freq(a: ListNode, b: ListNode):
    len_a = get_length(a)
    len_b = get_length(b)
    
    large, small = a, b
    
    if len_a < len_b:
        large, small = b, a
    elif len_a == len_b:
        curr_a, curr_b = a, b
        while curr_a and curr_a.val == curr_b.val:
            curr_a = curr_a.next
            curr_b = curr_b.next
        
        if not curr_a: # Equal
            return 0, ListNode(0), [1] + [0]*9
            
        if curr_a.val < curr_b.val:
            large, small = b, a
            
    s1, s2 = [], []
    curr = large
    while curr:
        s1.append(curr.val)
        curr = curr.next
    curr = small
    while curr:
        s2.append(curr.val)
        curr = curr.next
        
    head = None
    borrow = 0
    
    while s1:
        v1 = s1.pop()
        v2 = s2.pop() if s2 else 0
        
        diff = v1 - v2 - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
            
        node = ListNode(diff)
        node.next = head
        head = node
        
    while head and head.val == 0 and head.next:
        head = head.next
        
    freq = [0] * 10
    curr = head
    while curr:
        freq[curr.val] += 1
        curr = curr.next
        
    return 1, head, freq

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        dummy_a = ListNode()
        cur = dummy_a
        for _ in range(n):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        m = int(next(iterator))
        dummy_b = ListNode()
        cur = dummy_b
        for _ in range(m):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        sign, head, freq = subtract_with_freq(dummy_a.next, dummy_b.next)
        print(sign)
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(" ".join(str(x) for x in freq))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
