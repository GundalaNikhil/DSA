from collections import deque
from typing import List
import sys

def rate_limit(times: List[int], t: int, k: int) -> List[str]:
    q = deque()
    result = []
    
    for time in times:
        # Remove timestamps that are outside the window [time - t, time]
        while q and q[0] < time - t:
            q.popleft()
            
        if len(q) < k:
            q.append(time)
            result.append("true")
        else:
            result.append("false")
            
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly n values, use as times with default t and k
        if len(remaining) == n:
            times = [int(x) for x in remaining]
            t = 1  # Default time window
            k = 1  # Default capacity
        # If we have n + 2 values, first two are t and k
        elif len(remaining) == n + 2:
            t = int(remaining[0])
            k = int(remaining[1])
            times = [int(x) for x in remaining[2:n+2]]
        # If we have more than n, assume first two are parameters
        else:
            t = int(remaining[0]) if len(remaining) > 0 else 1
            k = int(remaining[1]) if len(remaining) > 1 else 1
            times = [int(x) for x in remaining[2:n+2]]

        result = rate_limit(times, t, k)
        print(" ".join(result))
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
