import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def weighted_middle_value(head: ListNode) -> int:
    if not head:
        return 0
        
    # Pass 1: Total weight
    total_weight = 0
    curr = head
    while curr:
        total_weight += curr.val
        curr = curr.next
        
    threshold = (total_weight + 1) // 2
    
    # Pass 2: Find node
    current_sum = 0
    curr = head
    while curr:
        current_sum += curr.val
        if current_sum >= threshold:
            return curr.val
        curr = curr.next
        
    return 0

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
            
        print(weighted_middle_value(dummy.next))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
