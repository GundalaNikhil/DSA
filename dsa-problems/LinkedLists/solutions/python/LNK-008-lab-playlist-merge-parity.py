import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def merge_by_parity(l1: ListNode, l2: ListNode) -> ListNode:
    even_dummy = ListNode(0)
    odd_dummy = ListNode(0)
    even_tail = even_dummy
    odd_tail = odd_dummy
    
    # Process L1
    curr = l1
    while curr:
        if curr.val % 2 == 0:
            even_tail.next = curr
            even_tail = even_tail.next
        else:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        curr = curr.next
        
    # Process L2
    curr = l2
    while curr:
        if curr.val % 2 == 0:
            even_tail.next = curr
            even_tail = even_tail.next
        else:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        curr = curr.next
        
    # Connect
    odd_tail.next = None
    even_tail.next = odd_dummy.next
    
    return even_dummy.next

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        d1 = ListNode()
        c1 = d1
        for _ in range(n):
            c1.next = ListNode(int(next(iterator)))
            c1 = c1.next
            
        m = int(next(iterator))
        d2 = ListNode()
        c2 = d2
        for _ in range(m):
            c2.next = ListNode(int(next(iterator)))
            c2 = c2.next
            
        head = merge_by_parity(d1.next, d2.next)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
