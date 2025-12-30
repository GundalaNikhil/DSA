import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value: int) -> None:
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

def main():
    input = sys.stdin.read
    data = input().splitlines()
    if not data:
        return
    
    n = int(data[0])
    sol = Solution()
    
    for i in range(1, n + 1):
        line = data[i].strip()
        if line.startswith("push_back"):
            _, v = line.split()
            sol.push_back(int(v))
        else:
            arr = sol.to_array()
            print(" ".join(str(x) for x in arr))

if __name__ == "__main__":
    main()
