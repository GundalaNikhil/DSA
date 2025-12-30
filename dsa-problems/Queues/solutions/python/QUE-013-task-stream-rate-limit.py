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
        t = int(next(iterator))
        k = int(next(iterator))
        times = [int(next(iterator)) for _ in range(n)]
        
        result = rate_limit(times, t, k)
        print(" ".join(result))
    except (StopIteration, ValueError):
        pass

if __name__ == "__main__":
    main()
