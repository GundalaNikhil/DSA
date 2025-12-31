import sys
import heapq
from collections import Counter, defaultdict

class DualHeap:
    def __init__(self, k):
        self.k = k
        self.small = []  # Max-heap (simulated with negative values) storing k smallest
        self.large = []  # Min-heap storing the rest
        self.small_count = 0  # Logical count
        self.large_count = 0  # Logical count
        self.lazy = Counter()
        # Track which heap each value was placed in (counts per heap)
        self.in_small = defaultdict(int)
        self.in_large = defaultdict(int)
    
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
            self.in_small[x] += 1
        else:
            # Check if x belongs in small or large
            self._prune(self.small, True)
            if not self.small:  # Small heap is empty after pruning
                heapq.heappush(self.small, -x)
                self.small_count += 1
                self.in_small[x] += 1
            else:
                small_max = -self.small[0]
                if x <= small_max:
                    heapq.heappop(self.small)
                    self.in_small[small_max] -= 1
                    heapq.heappush(self.small, -x)
                    self.in_small[x] += 1
                    heapq.heappush(self.large, small_max)
                    self.in_large[small_max] += 1
                    self.large_count += 1
                else:
                    heapq.heappush(self.large, x)
                    self.in_large[x] += 1
                    self.large_count += 1
        self._balance()

    def remove(self, x):
        # Use tracking to determine which heap the element is in
        self.lazy[x] += 1
        
        if self.in_small[x] > 0:
            self.in_small[x] -= 1
            self.small_count -= 1
        else:
            self.in_large[x] -= 1
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
            self.in_large[val] -= 1
            heapq.heappush(self.small, -val)
            self.in_small[val] += 1
            self.small_count += 1
            self.large_count -= 1
            self._prune(self.small, True) # Just in case

        while self.small_count > self.k: # Should rarely happen with add logic but good for safety
            self._prune(self.small, True)
            val = -heapq.heappop(self.small)
            self.in_small[val] -= 1
            heapq.heappush(self.large, val)
            self.in_large[val] += 1
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

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        w = int(next(it))
        k = int(next(it))
        arr = []
        for _ in range(n):
            arr.append(int(next(it)))
            
        solution = Solution()
        result = solution.kth_smallest_in_windows(arr, w, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
