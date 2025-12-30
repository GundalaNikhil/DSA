import heapq
import sys
import math
from collections import defaultdict

def median_after_batches(k: int, t: int, batches: list) -> list:
    # MaxHeap (lower) stores negative values
    lower = []
    upper = []
    
    freq = defaultdict(int)
    # location[x] = [count_in_lower, count_in_upper]
    location = defaultdict(lambda: [0, 0])
    
    valid_lower = 0
    valid_upper = 0
    results = []
    
    for batch in batches:
        for x in batch:
            freq[x] += 1
            f = freq[x]
            
            if f > t + 1:
                continue
            
            if f == t + 1:
                # Became stale
                valid_lower -= location[x][0]
                valid_upper -= location[x][1]
                continue
                
            # Add to heaps
            # Compare with effective top of lower
            # But we can just compare with raw top, rebalance handles correctness
            if not lower or x <= -lower[0]:
                heapq.heappush(lower, -x)
                location[x][0] += 1
                valid_lower += 1
            else:
                heapq.heappush(upper, x)
                location[x][1] += 1
                valid_upper += 1
                
        # Balance
        while True:
            # Prune stale
            while lower and freq[-lower[0]] > t:
                heapq.heappop(lower)
            while upper and freq[upper[0]] > t:
                heapq.heappop(upper)
                
            if valid_lower > valid_upper + 1:
                val = -heapq.heappop(lower)
                location[val][0] -= 1
                location[val][1] += 1
                heapq.heappush(upper, val)
                valid_lower -= 1
                valid_upper += 1
            elif valid_upper > valid_lower:
                val = heapq.heappop(upper)
                location[val][1] -= 1
                location[val][0] += 1
                heapq.heappush(lower, -val)
                valid_upper -= 1
                valid_lower += 1
            else:
                break
                
        if valid_lower + valid_upper == 0:
            results.append("NA")
        else:
            if (valid_lower + valid_upper) % 2 == 1:
                med = -lower[0]
            else:
                v1 = -lower[0]
                v2 = upper[0]
                med = math.floor((v1 + v2) / 2)
            results.append(str(med))
            
    return results

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        k = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    batches = []
    for _ in range(k):
        m = int(next(iterator))
        batch = []
        for _ in range(m):
            batch.append(int(next(iterator)))
        batches.append(batch)

    result = median_after_batches(k, t, batches)
    print(' '.join(result))

if __name__ == "__main__":
    main()
