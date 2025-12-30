import sys

class Solution:
    def process_operations(self, operations: list) -> list:
        heap = [] # List of [value, id]
        pos = {}  # id -> index
        
        def swap(i, j):
            heap[i], heap[j] = heap[j], heap[i]
            pos[heap[i][1]] = i
            pos[heap[j][1]] = j
            
        def less(i, j):
            # Compare heap[i] and heap[j]
            # Tie-break: smaller id
            v1, id1 = heap[i]
            v2, id2 = heap[j]
            if v1 != v2:
                return v1 < v2
            return id1 < id2
            
        def bubble_up(k):
            while k > 0:
                p = (k - 1) // 2
                if less(k, p):
                    swap(k, p)
                    k = p
                else:
                    break
                    
        def bubble_down(k):
            n = len(heap)
            while True:
                left = 2 * k + 1
                if left >= n:
                    break
                child = left
                right = left + 1
                if right < n and less(right, left):
                    child = right
                
                if less(child, k):
                    swap(k, child)
                    k = child
                else:
                    break
                    
        results = []
        
        for op in operations:
            type = op[0]
            if type == "INSERT":
                gid = op[1]
                val = int(op[2])
                heap.append([val, gid])
                pos[gid] = len(heap) - 1
                bubble_up(len(heap) - 1)
                
            elif type == "DECREASE":
                gid = op[1]
                delta = int(op[2])
                if gid in pos:
                    idx = pos[gid]
                    heap[idx][0] -= delta
                    bubble_up(idx)
                    
            elif type == "EXTRACT":
                if not heap:
                    results.append("EMPTY")
                else:
                    val, gid = heap[0]
                    results.append(f"{val} {gid}")
                    
                    last = heap.pop()
                    del pos[gid]
                    
                    if heap:
                        heap[0] = last
                        pos[last[1]] = 0
                        bubble_down(0)
                        
        return results

def process_operations(operations: list) -> list:
    solver = Solution()
    return solver.process_operations(operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "INSERT":
                gid = next(it)
                val = next(it)
                operations.append([op, gid, val])
            elif op == "DECREASE":
                gid = next(it)
                delta = next(it)
                operations.append([op, gid, delta])
            else:
                operations.append([op])
                
        result = process_operations(operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
