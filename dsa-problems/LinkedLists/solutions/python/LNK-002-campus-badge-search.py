import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def find_first_index(head: ListNode, target: int) -> int:
    current = head
    index = 0
    while current:
        if current.val == target:
            return index
        current = current.next
        index += 1
    return -1

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
            val = int(next(iterator))
            cur.next = ListNode(val)
            cur = cur.next
        
        target = int(next(iterator))
        print(find_first_index(dummy.next, target))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
