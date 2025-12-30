import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def group_odd_even_stable(head: ListNode) -> ListNode:
    odd_dummy = ListNode(0)
    even_dummy = ListNode(0)
    odd_tail = odd_dummy
    even_tail = even_dummy
    
    curr = head
    while curr:
        if curr.val % 2 != 0:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:
            even_tail.next = curr
            even_tail = even_tail.next
        curr = curr.next
        
    even_tail.next = None
    odd_tail.next = even_dummy.next
    
    return odd_dummy.next

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        dummy = ListNode()
        cur = dummy
        for _ in range(n):
            cur.next = ListNode(int(next(iterator)))
            cur = cur.next
            
        head = group_odd_even_stable(dummy.next)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
