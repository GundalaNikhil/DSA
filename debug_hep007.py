import sys
import heapq
from collections import Counter

class DualHeap:
    def __init__(self, k):
        self.k = k
        self.small = []  # Max-heap (simulated with negative values) storing k smallest
        self.large = []  # Min-heap storing the rest
        self.small_count = 0  # Logical count
        self.large_count = 0  # Logical count
        self.lazy = Counter()
    
    def _prune(self, heap, is_small):
        # Remove invalid elements from top of heap
        while heap:
            val = -heap[0] if is_small else heap[0]
            if self.lazy[val] > 0:
                self.lazy[val] -= 1
                heapq.heappop(heap)
            else:
                break
    
    def add(self, x):
        # Add to small heap initially
        if self.small_count < self.k:
            heapq.heappush(self.small, -x)
            self.small_count += 1
        else:
            # Check if x belongs in small or large
            self._prune(self.small, True)
            small_max = -self.small[0]
            if x < small_max:
                heapq.heappop(self.small)
                heapq.heappush(self.small, -x)
                heapq.heappush(self.large, small_max)
                self.large_count += 1
            else:
                heapq.heappush(self.large, x)
                self.large_count += 1
        self._balance()

    def remove(self, x):
        self.lazy[x] += 1
        # Determine logical removal
        self._prune(self.small, True)
        self._prune(self.large, False)
        
        in_small = False
        if self.small:
            small_max = -self.small[0]
            if x <= small_max:
                in_small = True
            else:
                in_small = False
        else:
            in_small = True
            
        if in_small:
            self.small_count -= 1
        else:
            self.large_count -= 1
            
        self._balance()

    def _balance(self):
        # Ensure small has exactly k elements if possible
        self._prune(self.small, True)
        self._prune(self.large, False)
        
        while self.small_count < self.k and self.large:
            self._prune(self.large, False)
            if not self.large: break
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.small_count += 1
            self.large_count -= 1
            self._prune(self.small, True)

        while self.small_count > self.k:
            self._prune(self.small, True)
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_count -= 1
            self.large_count += 1
            self._prune(self.large, False)

    def get_kth_smallest(self):
        self._prune(self.small, True)
        if self.small:
            return -self.small[0]
        return None

class Solution:
    def kth_smallest_in_windows(self, arr: list, w: int, k: int) -> list:
        n = len(arr)
        if w > n: return []
        
        dh = DualHeap(k)
        result = []
        
        for i in range(w):
            dh.add(arr[i])
            
        result.append(dh.get_kth_smallest())
        
        for i in range(w, n):
            dh.remove(arr[i - w])
            dh.add(arr[i])
            result.append(dh.get_kth_smallest())
            
        return result

def test(arr, w, k):
    print(f"Arr: {arr}, W: {w}, K: {k}")
    solver = Solution()
    try:
        res = solver.kth_smallest_in_windows(arr, w, k)
        print(f"Result: {res}")
        return res
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example 1
test([1, 3, 2, 6, 4], 3, 2)
# Exp: [2, 3, 4]

# Duplicates
test([5, 5, 5, 5], 3, 1)
# Exp: [5, 5]

# k=1 (Min in window)
test([1, 5, 2, 6, 3], 3, 1)
# Exp: [1, 2, 2]

# k=w (Max in window)
test([1, 2, 3, 4], 3, 3)
# Exp: [3, 4]
