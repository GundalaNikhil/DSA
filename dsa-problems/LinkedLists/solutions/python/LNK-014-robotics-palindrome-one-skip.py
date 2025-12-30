import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def is_palindrome(vals, left, right):
    while left < right:
        if vals[left] != vals[right]:
            return False
        left += 1
        right -= 1
    return True

def can_be_palindrome(head: ListNode) -> bool:
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
        
    left, right = 0, len(vals) - 1
    while left < right:
        if vals[left] != vals[right]:
            return is_palindrome(vals, left + 1, right) or \
                   is_palindrome(vals, left, right - 1)
        left += 1
        right -= 1
        
    return True

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
            
        print("true" if can_be_palindrome(dummy.next) else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
