from typing import List
from collections import deque
import sys

def process_queue_operations(operations: List[List[str]]) -> str:
    """
    Process queue operations and return the sum of all SIZE operation results
    """
    queue = deque()
    total = 0

    for op_data in operations:
        cmd = op_data[0]

        if cmd == "ENQUEUE":
            queue.append(int(op_data[1]))

        elif cmd == "DEQUEUE":
            if len(queue) > 0:
                queue.popleft()

        elif cmd == "FRONT":
            pass  # Just read

        elif cmd == "REAR":
            pass  # Just read

        elif cmd == "SIZE":
            total += len(queue)

        elif cmd == "ISEMPTY":
            pass  # Just read

    return str(total)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        m = int(next(iterator))  # number of operations
        operations = []
        for _ in range(m):
            op = next(iterator)
            if op in ("ENQUEUE",):
                val = next(iterator)
                operations.append([op, val])
            else:
                operations.append([op])

        result = process_queue_operations(operations)
        print(result)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
