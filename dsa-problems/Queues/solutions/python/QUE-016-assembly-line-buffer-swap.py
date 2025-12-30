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
        remaining = list(iterator)

        # If we have exactly 2n values, split them in half
        if len(remaining) == 2 * n:
            q1 = [int(x) for x in remaining[:n]]
            q2 = [int(x) for x in remaining[n:]]
        # If we have exactly n values, use as q1, create q2
        elif len(remaining) == n:
            q1 = [int(x) for x in remaining]
            q2 = [0] * n  # Default second queue
        # Otherwise try to split as much as possible
        else:
            q1 = [int(x) for x in remaining[:n]]
            q2 = [int(x) for x in remaining[n:]] if len(remaining) > n else [0] * n

        result = swap_queues(q1, q2)
        for resArr in result:
            print(" ".join(map(str, resArr)))
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
