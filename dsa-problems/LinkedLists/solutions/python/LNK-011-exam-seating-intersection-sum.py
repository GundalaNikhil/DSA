import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def intersection_sum(headA: ListNode, headB: ListNode) -> int:
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    ptrA = headA
    ptrB = headB
    
    # Align
    while lenA > lenB:
        ptrA = ptrA.next
        lenA -= 1
    while lenB > lenA:
        ptrB = ptrB.next
        lenB -= 1
        
    # Find intersection
    while ptrA != ptrB:
        ptrA = ptrA.next
        ptrB = ptrB.next
        
    if not ptrA:
        return 0
        
    # Sum suffix
    total_sum = 0
    while ptrA:
        total_sum += ptrA.val
        ptrA = ptrA.next
        
    return total_sum

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        dummyA = ListNode()
        curA = dummyA
        nodesA = []
        for _ in range(n):
            node = ListNode(int(next(iterator)))
            curA.next = node
            curA = curA.next
            nodesA.append(node)
            
        dummyB = ListNode()
        curB = dummyB
        nodesB = []
        for _ in range(m):
            node = ListNode(int(next(iterator)))
            curB.next = node
            curB = curB.next
            nodesB.append(node)
            
        ia = int(next(iterator))
        ib = int(next(iterator))
        
        if ia >= 0 and ib >= 0 and n > 0 and m > 0:
            nodesB[ib].next = nodesA[ia]
            
        print(intersection_sum(dummyA.next, dummyB.next))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
