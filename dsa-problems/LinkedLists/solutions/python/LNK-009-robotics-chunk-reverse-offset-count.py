import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverse_from_offset(head: ListNode, k: int, s: int):
    if not head or k <= 1:
        return head, 0, 0
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move to s-1
    for _ in range(s - 1):
        if not prev.next:
            return head, 0, 0
        prev = prev.next
        
    groups = 0
    total_sum = 0
    
    while True:
        # Probe
        probe = prev
        for _ in range(k):
            probe = probe.next
            if not probe:
                return dummy.next, groups, total_sum
        
        # Reverse
        tail = prev.next
        curr = tail.next
        group_sum = tail.val
        
        for _ in range(k - 1):
            group_sum += curr.val
            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            tail.next = temp
            curr = temp
            
        groups += 1
        total_sum += group_sum
        prev = tail
        
    return dummy.next, groups, total_sum

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
            
        k = int(next(iterator))
        s = int(next(iterator))
        
        head, groups, total_sum = reverse_from_offset(dummy.next, k, s)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
        print(groups)
        print(total_sum)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
