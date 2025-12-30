import sys

class Solution:
    def find_median(self, max_heap: list, min_heap: list) -> float:
        combined = max_heap + min_heap
        combined.sort()
        
        n = len(combined)
        if n == 0:
            return 0.0
            
        if n % 2 == 1:
            return combined[n // 2]
        else:
            mid1 = combined[n // 2 - 1]
            mid2 = combined[n // 2]
            res = (mid1 + mid2) / 2.0
            if res.is_integer():
                return int(res)
            return res

def find_median(max_heap: list, min_heap: list) -> float:
    solver = Solution()
    return solver.find_median(max_heap, min_heap)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        max_heap = []
        for _ in range(n):
            max_heap.append(int(next(it)))
        min_heap = []
        for _ in range(m):
            min_heap.append(int(next(it)))
            
        print(find_median(max_heap, min_heap))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
