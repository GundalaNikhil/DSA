import sys
import heapq

class Solution:
    def kth_smallest_in_windows(self, arr: list, w: int, k: int) -> list:
        n = len(arr)
        result = []
        
        # Max-Heap (Left): stores negative values
        left = []
        # Min-Heap (Right)
        right = []
        
        deleted = {}
        
        left_size = 0
        right_size = 0
        
        def clean(heap, is_max=False):
            while heap:
                val = -heap[0] if is_max else heap[0]
                if deleted.get(val, 0) > 0:
                    heapq.heappop(heap)
                    deleted[val] -= 1
                    if deleted[val] == 0:
                        del deleted[val]
                else:
                    break
                    
        for i in range(n):
            val = arr[i]
            
            # ADD
            clean(left, True)
            if not left or val <= -left[0]:
                heapq.heappush(left, -val)
                left_size += 1
            else:
                heapq.heappush(right, val)
                right_size += 1
                
            # REMOVE
            if i >= w:
                out = arr[i - w]
                deleted[out] = deleted.get(out, 0) + 1
                
                clean(left, True)
                # Check if out was logically in left
                # If out <= left_max, it was in left.
                # Note: left can be empty after clean if k=0 (impossible) or w=0
                if left and out <= -left[0]:
                    left_size -= 1
                else:
                    right_size -= 1
            
            # REBALANCE
            # 1. Size balance
            while left_size < k:
                clean(right, False)
                if not right: break
                val = heapq.heappop(right)
                heapq.heappush(left, -val)
                left_size += 1
                right_size -= 1
                
            while left_size > k:
                clean(left, True)
                if not left: break
                val = -heapq.heappop(left)
                heapq.heappush(right, val)
                left_size -= 1
                right_size += 1
                
            # 2. Value balance (Swap if L.max > R.min)
            while True:
                clean(left, True)
                clean(right, False)
                if not left or not right:
                    break
                l_max = -left[0]
                r_min = right[0]
                if l_max > r_min:
                    heapq.heappop(left)
                    heapq.heappop(right)
                    heapq.heappush(left, -r_min)
                    heapq.heappush(right, l_max)
                else:
                    break
            
            if i >= w - 1:
                clean(left, True)
                result.append(-left[0])
                
        return result

def kth_smallest_in_windows(arr: list, w: int, k: int) -> list:
    solver = Solution()
    return solver.kth_smallest_in_windows(arr, w, k)

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
            
        result = kth_smallest_in_windows(arr, w, k)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
