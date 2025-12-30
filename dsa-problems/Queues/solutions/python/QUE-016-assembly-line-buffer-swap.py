from typing import List
import sys

def swap_queues(q1: List[int], q2: List[int]) -> List[List[int]]:
    return [q2, q1]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        q1 = [int(next(iterator)) for _ in range(n)]
        q2 = [int(next(iterator)) for _ in range(n)]
        
        result = swap_queues(q1, q2)
        for resArr in result:
            print(" ".join(map(str, resArr)))
    except (StopIteration, ValueError):
        pass

if __name__ == "__main__":
    main()
