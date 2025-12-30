import sys
import heapq
from collections import Counter

class Solution:
    def kth_smallest_in_windows(self, arr: list, w: int, k: int) -> list:
        n = len(arr)
        result = []
        window = []

        for i in range(n):
            # Add new element to window
            heapq.heappush(window, arr[i])

            # Remove oldest element when window size exceeds w
            if i >= w:
                # Find and remove the element at position i - w
                # We need to rebuild the heap for reliability
                window = list(window)
                window.remove(arr[i - w])
                heapq.heapify(window)

            # Get k-th smallest element (at index k-1 after sorting)
            if i >= w - 1:
                # k-th smallest is at heap position k-1 in a min-heap
                sorted_window = sorted(window)
                result.append(sorted_window[k - 1])

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
