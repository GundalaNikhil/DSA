from collections import deque
from typing import List
import sys

def process_commands(commands: List[List[str]]) -> List[str]:
    queue = deque()
    result = []
    
    for cmd in commands:
        op = cmd[0]
        if op == "ENQUEUE":
            queue.append(cmd[1])
        elif op == "DEQUEUE":
            if not queue:
                result.append("EMPTY")
            else:
                result.append(queue.popleft())
        elif op == "FRONT":
            if not queue:
                result.append("EMPTY")
            else:
                result.append(queue[0])
                
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        m = int(next(iterator))
        commands = []
        for _ in range(m):
            op = next(iterator)
            if op == "ENQUEUE":
                val = next(iterator)
                commands.append([op, val])
            else:
                commands.append([op])
        
        result = process_commands(commands)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
