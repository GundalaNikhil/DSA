import sys


class ListNode:
    def __init__(self, val):
        self.val = val
        self.access_count = 0


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    current_list = []
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        current_list.append(ListNode(v))
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "ACCESS":
            pos = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(current_list):
                current_list[pos - 1].access_count += 1
                
        elif op == "REORDER":
            # Stable sort for consistency if counts are equal? 
            # Python's sort is stable.
            current_list.sort(key=lambda x: x.access_count, reverse=True)
            print(*(node.val for node in current_list))


if __name__ == "__main__":
    solve()
