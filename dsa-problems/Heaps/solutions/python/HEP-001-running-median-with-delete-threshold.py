import sys
import heapq
from collections import defaultdict

class Solution:
    def process_operations(self, T: int, operations: list) -> list:
        # Left is max heap (store negative values), Right is min heap
        left = []
        right = []
        debt = defaultdict(int)
        location = {}  # Track where each element currently resides

        results = []

        # Helper to clean heaps
        def clean(heap, is_left):
            while heap:
                val = -heap[0] if is_left else heap[0]
                if debt[val] > 0:
                    heapq.heappop(heap)
                    debt[val] -= 1
                else:
                    break

        def rebalance():
            # Invariant: len(left) == len(right) OR len(left) == len(right) + 1
            clean(left, True)
            clean(right, False)

            while len(left) > len(right) + 1:
                val = -heapq.heappop(left)
                heapq.heappush(right, val)
                location[val] = 'right'

            while len(right) > len(left):
                val = heapq.heappop(right)
                heapq.heappush(left, -val)
                location[val] = 'left'

        for op_data in operations:
            op = op_data[0]

            if op == "ADD":
                x = int(op_data[1])

                # Decide where to push
                clean(left, True)
                if not left or x <= -left[0]:
                    heapq.heappush(left, -x)
                    location[x] = 'left'
                else:
                    heapq.heappush(right, x)
                    location[x] = 'right'
                rebalance()

            elif op == "DEL":
                x = int(op_data[1])
                if x in location:
                    debt[x] += 1
                    del location[x]
                    rebalance()

            elif op == "MEDIAN":
                clean(left, True)
                clean(right, False)
                total = len(left) + len(right)
                if total == 0:
                    results.append("EMPTY")
                elif total < T:
                    results.append("NA")
                else:
                    results.append(str(-left[0]))

        return results

def process_operations(T: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(T, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        T = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op in ("ADD", "DEL"):
                x = next(it)
                operations.append([op, x])
            else:
                operations.append([op])
        
        result = process_operations(T, operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
