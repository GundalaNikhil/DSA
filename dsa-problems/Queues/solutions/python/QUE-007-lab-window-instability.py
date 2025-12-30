from typing import List
from collections import deque
import heapq
import sys

class MedianFinder:
    def __init__(self):
        self.small = [] # Max heap (negative values)
        self.large = [] # Min heap
        self.delayed = {} # Lazy removal
        self.small_size = 0
        self.large_size = 0

    def add(self, num: int):
        # Add to small
        heapq.heappush(self.small, -num)
        # Move to large
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        self.large_size += 1
        
        # Rebalance: small needs to be size k or k+1
        if self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1

    def remove(self, num: int):
        self.delayed[num] = self.delayed.get(num, 0) + 1
        
        # Determine which heap it effectively belongs to
        # small.peek is the median (or close to it)
        # If num <= small.peek(), it's in small
        small_top = -self.small[0] if self.small else float('-inf')
        
        if num <= small_top:
            self.small_size -= 1
        else:
            self.large_size -= 1
            
        # Prune dead roots
        self.prune()
        
        # Rebalance sizes
        if self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1
        elif self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1
            
        self.prune()

    def prune(self):
        while self.small and self.delayed.get(-self.small[0], 0) > 0:
            val = -heapq.heappop(self.small)
            self.delayed[val] -= 1
        while self.large and self.delayed.get(self.large[0], 0) > 0:
            val = heapq.heappop(self.large)
            self.delayed[val] -= 1

    def get_median(self) -> int:
        return -self.small[0]

def window_instability(values: List[int], k: int) -> List[int]:
    n = len(values)
    result = []
    min_dq = deque()
    max_dq = deque()
    mf = MedianFinder()
    
    for i in range(n):
        # Min Deque
        while min_dq and min_dq[0] <= i - k:
            min_dq.popleft()
        while min_dq and values[min_dq[-1]] >= values[i]:
            min_dq.pop()
        min_dq.append(i)
        
        # Max Deque
        while max_dq and max_dq[0] <= i - k:
            max_dq.popleft()
        while max_dq and values[max_dq[-1]] <= values[i]:
            max_dq.pop()
        max_dq.append(i)
        
        # Median
        mf.add(values[i])
        if i >= k:
            mf.remove(values[i-k])
            
        if i >= k - 1:
            min_val = values[min_dq[0]]
            max_val = values[max_dq[0]]
            med = mf.get_median()
            if med == 0:
                result.append(0)
            else:
                result.append((max_val - min_val) // med)
                
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        
        result = window_instability(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
