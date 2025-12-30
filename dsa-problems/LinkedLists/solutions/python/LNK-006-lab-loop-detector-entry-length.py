import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def cycle_info(head: ListNode):
    if not head:
        return (-1, 0, 0)
    
    slow = head
    fast = head
    has_cycle = False
    
    # Phase 1: Detect
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return (-1, 0, 0)
        
    # Phase 2: Find Entry
    entry = head
    entry_index = 0
    while entry != slow:
        entry = entry.next
        slow = slow.next
        entry_index += 1
        
    # Phase 3: Stats
    length = 0
    max_val = -float('inf')
    curr = entry
    while True:
        length += 1
        max_val = max(max_val, curr.val)
        curr = curr.next
        if curr == entry:
            break
            
    return (entry_index, length, max_val)

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
        nodes = []
        for _ in range(n):
            node = ListNode(int(next(iterator)))
            cur.next = node
            cur = cur.next
            nodes.append(node)
            
        pos = int(next(iterator))
        if pos >= 0 and n > 0:
            cur.next = nodes[pos]
            
        entry, length, max_val = cycle_info(dummy.next)
        print(f"{entry} {length} {max_val}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
