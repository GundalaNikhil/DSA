import sys
from collections import deque
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    capacity = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    queue = deque()
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'PUSH':
            val = int(input_data[ptr])
            ptr += 1
            if len(queue) < capacity:
                queue.append(val)
                print("OK")
            else:
                print("BLOCKED")
        elif op == 'POP':
            if queue:
                queue.popleft()
        elif op == 'SIZE':
            print(len(queue))
if __name__ == '__main__':
    solve()