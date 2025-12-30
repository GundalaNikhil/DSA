import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def remove_mth(head: ListNode, M: int) -> ListNode:
    if M <= 0:
        return head
        
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    
    # Move to M-1
    for _ in range(M - 1):
        if not curr:
            return head
        curr = curr.next
        
    if curr and curr.next:
        curr.next = curr.next.next
        
    return dummy.next

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
            
        M = int(next(iterator))
        
        head = remove_mth(dummy.next, M)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
