import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def deduplicate_at_most_two(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    prev = head
    current = head.next
    count = 1
    
    while current:
        if current.val == prev.val:
            count += 1
            if count > 2:
                # Remove current
                prev.next = current.next
                current = current.next
            else:
                # Keep current
                prev = current
                current = current.next
        else:
            # New value
            count = 1
            prev = current
            current = current.next
            
    return head

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
            
        head = deduplicate_at_most_two(dummy.next)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
