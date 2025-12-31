import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def rotate_list(head: ListNode, length: int, k: int):
    if length <= 1 or k % length == 0:
        tail = head
        while tail.next:
            tail = tail.next
        return head, tail
    
    k = k % length
    moves = length - k
    
    new_tail = head
    for _ in range(moves - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    temp = new_head
    while temp.next:
        temp = temp.next
    temp.next = head
    
    return new_head, new_tail

def rotate_blocks(head: ListNode, b: int, k: int) -> ListNode:
    if not head or b <= 0:
        return head
        
    dummy = ListNode(0)
    prev_tail = dummy
    curr = head
    
    while curr:
        block_head = curr
        block_tail = curr
        length = 1
        
        # Find block end
        for _ in range(b - 1):
            if not block_tail.next:
                break
            block_tail = block_tail.next
            length += 1
            
        next_block_head = block_tail.next
        block_tail.next = None # Detach
        
        # Rotate
        new_head, new_tail = rotate_list(block_head, length, k)
        
        # Attach
        prev_tail.next = new_head
        prev_tail = new_tail
        
        curr = next_block_head
        
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
            
        b = int(next(iterator))
        k = int(next(iterator))
        
        head = rotate_blocks(dummy.next, b, k)
        
        out = []
        while head:
            out.append(str(head.val))
            head = head.next
        print(" ".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
