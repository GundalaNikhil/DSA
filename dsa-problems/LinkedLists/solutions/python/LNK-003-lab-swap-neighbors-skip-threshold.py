import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def swap_with_skip(head: ListNode, K: int):
    if not head or not head.next:
        return head, 0
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    swaps_performed = 0
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Check conditions
        non_negative = (first.val >= 0 and second.val >= 0)
        can_swap = (K > 0)
        
        if non_negative and can_swap:
            # Swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            K -= 1
            swaps_performed += 1
            prev = first
        else:
            # Skip
            prev = second
            
    return dummy.next, swaps_performed

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
        
        K = int(next(iterator))
        
        head, swaps = swap_with_skip(dummy.next, K)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(swaps)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
