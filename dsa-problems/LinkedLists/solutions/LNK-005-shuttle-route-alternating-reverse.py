import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def alternating_reverse(head: ListNode, l: int, k: int) -> ListNode:
    if not head or k <= 1:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to start position l
    for _ in range(l - 1):
        if not prev.next:
            return head
        prev = prev.next
        
    reverse_turn = True
    
    while prev.next:
        if reverse_turn:
            # Reverse next k nodes
            tail = prev.next
            curr = tail.next
            count = 1
            while curr and count < k:
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                tail.next = temp
                curr = temp
                count += 1
            prev = tail # Move prev to end of reversed block
        else:
            # Skip k nodes
            count = 0
            while prev.next and count < k:
                prev = prev.next
                count += 1
        
        reverse_turn = not reverse_turn
        
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
            
        l = int(next(iterator))
        k = int(next(iterator))
        
        head = alternating_reverse(dummy.next, l, k)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
