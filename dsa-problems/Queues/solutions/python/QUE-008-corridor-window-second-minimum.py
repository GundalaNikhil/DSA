from typing import List
import sys
# Python doesn't have a built-in TreeMap/Multiset.
# We can use SortedList from sortedcontainers library, but in standard interviews/environments
# we might need to simulate it or use two heaps with lazy deletion.
# For simplicity and standard library adherence, let's use Two Heaps with Lazy Deletion.
# Or just one Min-Heap with lazy deletion, popping twice to find second min?
# Popping twice is destructive. We'd need to put them back.
# Let's implement a simplified solution using heapq and lazy removal.

import heapq

class Solution:
    def second_minimums(self, values: List[int], k: int) -> List[int]:
        if k == 1:
            return values
            
        n = len(values)
        result = []
        min_heap = [] # Stores (val, index)
        
        # We need to find the 2nd smallest.
        # A single heap gives the smallest.
        # We can peek. If top is valid, pop it, peek next valid, then push back first.
        # But lazy deletion makes "peek next valid" hard because the top might be invalid.
        
        # Better approach for Python without SortedList:
        # Maintain two heaps? No.
        # Just use a min-heap. When querying:
        # 1. Clean top (remove indices <= i-k).
        # 2. Pop min (v1).
        # 3. Clean new top.
        # 4. Peek/Pop second min (v2).
        # 5. Push v1 back.
        
        # Optimization: We only need to clean when we access.
        
        for i in range(n):
            heapq.heappush(min_heap, (values[i], i))
            
            if i >= k - 1:
                # Clean top
                while min_heap and min_heap[0][1] <= i - k:
                    heapq.heappop(min_heap)
                
                first = heapq.heappop(min_heap)
                
                # Clean top again to find second
                while min_heap and min_heap[0][1] <= i - k:
                    heapq.heappop(min_heap)
                
                second = min_heap[0] # This is the second min
                
                result.append(second[0])
                
                # Push first back
                heapq.heappush(min_heap, first)
                
        return result

def second_minimums(values: List[int], k: int) -> List[int]:
    return Solution().second_minimums(values, k)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        values = [int(next(iterator)) for _ in range(n)]
        
        result = second_minimums(values, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
