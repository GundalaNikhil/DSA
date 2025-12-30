import sys
import heapq

class Point:
    def __init__(self, num, den, pid):
        self.num = num
        self.den = den
        self.pid = pid
        
    def __lt__(self, other):
        # Less than means "Better" (Smaller Dist or Smaller ID)
        val1 = self.num * other.den
        val2 = other.num * self.den
        if val1 != val2:
            return val1 < val2
        return self.pid < other.pid
        
    def __eq__(self, other):
        return self.num * other.den == other.num * self.den and self.pid == other.pid

class Solution:
    def process_operations(self, k: int, operations: list) -> list:
        # Max-Heap stores "Worst" elements.
        # Python heapq is Min-Heap.
        # To simulate Max-Heap of Points, we need to invert comparison.
        # Or store wrapper objects.
        # Use a wrapper that inverts __lt__.
        
        class MaxHeapItem:
            def __init__(self, p):
                self.p = p
            def __lt__(self, other):
                # We want Max-Heap behavior: pop the LARGEST.
                # heapq pops SMALLEST.
                # So we want "Largest" to be "Smallest" in wrapper.
                # Wrapper A < Wrapper B if A.p > B.p
                return other.p < self.p
        
        pq = [] # Stores MaxHeapItem
        results = []
        current_id = 1
        
        for op in operations:
            if op[0] == "ADD":
                x = int(op[1])
                y = int(op[2])
                w = int(op[3])
                p = Point(x*x + y*y, w, current_id)
                current_id += 1
                
                if len(pq) < k:
                    heapq.heappush(pq, MaxHeapItem(p))
                else:
                    # Peek top (Worst)
                    top = pq[0].p
                    # If p is better than top (p < top), replace
                    if p < top:
                        heapq.heapreplace(pq, MaxHeapItem(p))
                        
            else:
                if not pq:
                    results.append("EMPTY")
                else:
                    # Extract, sort
                    items = [item.p for item in pq]
                    items.sort()
                    res_ids = [str(item.pid) for item in items]
                    results.append(" ".join(res_ids))
                    
        return results

def process_operations(k: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(k, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        k = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "ADD":
                x = next(it)
                y = next(it)
                w = next(it)
                operations.append([op, x, y, w])
            else:
                operations.append([op])
        
        result = process_operations(k, operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
