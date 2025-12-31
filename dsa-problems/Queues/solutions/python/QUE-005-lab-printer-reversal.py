from typing import List
from collections import deque
import sys

def reverse_first_k(values: List[int], k: int) -> List[int]:
    queue = deque(values)
    stack = []
    
    # 1. Dequeue first K and push to stack
    for _ in range(k):
        stack.append(queue.popleft())
        
    # 2. Pop from stack and enqueue
    while stack:
        queue.append(stack.pop())
        
    # 3. Rotate remaining N-K elements
    n = len(values)
    for _ in range(n - k):
        queue.append(queue.popleft())
        
    return list(queue)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]

        result = reverse_first_k(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
