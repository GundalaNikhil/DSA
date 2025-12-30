import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def stable_partition(head: ListNode, x: int) -> ListNode:
    less_head = ListNode(0)
    equal_head = ListNode(0)
    greater_head = ListNode(0)
    
    less = less_head
    equal = equal_head
    greater = greater_head
    
    curr = head
    while curr:
        if curr.val < x:
            less.next = curr
            less = less.next
        elif curr.val == x:
            equal.next = curr
            equal = equal.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next
        
    # Connect
    greater.next = None
    equal.next = greater_head.next
    less.next = equal_head.next if equal_head.next else greater_head.next
    
    return less_head.next

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
            
        x = int(next(iterator))
        
        head = stable_partition(dummy.next, x)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
