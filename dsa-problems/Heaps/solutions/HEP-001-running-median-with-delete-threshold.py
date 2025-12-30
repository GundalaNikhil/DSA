import sys
import heapq

class Solution:
    def process_operations(self, T: int, operations: list) -> list:
        # Left is max heap (store negative values), Right is min heap
        left = [] 
        right = []
        debt = {}
        valid_left = 0
        valid_right = 0
        
        results = []
        
        # Helper to clean heaps
        def clean(heap, is_left):
            while heap:
                val = -heap[0] if is_left else heap[0]
                if debt.get(val, 0) > 0:
                    heapq.heappop(heap)
                    debt[val] -= 1
                else:
                    break
                    
        def rebalance():
            nonlocal valid_left, valid_right
            # Invariant: valid_left == valid_right OR valid_left == valid_right + 1
            
            while valid_left > valid_right + 1:
                clean(left, True)
                val = -heapq.heappop(left)
                valid_left -= 1
                heapq.heappush(right, val)
                valid_right += 1
                
            while valid_right > valid_left:
                clean(right, False)
                val = heapq.heappop(right)
                valid_right -= 1
                heapq.heappush(left, -val)
                valid_left += 1
                
            clean(left, True)
            clean(right, False)

        # We need to track actual existence to handle "DEL x if exists"
        # But for this problem, usually we can assume valid inputs or track global count
        global_counts = {}

        for op_data in operations:
            op = op_data[0]
            
            if op == "ADD":
                x = int(op_data[1])
                global_counts[x] = global_counts.get(x, 0) + 1
                
                # Decide where to push
                # Peek left
                clean(left, True)
                if not left or x <= -left[0]:
                    heapq.heappush(left, -x)
                    valid_left += 1
                else:
                    heapq.heappush(right, x)
                    valid_right += 1
                rebalance()
                
            elif op == "DEL":
                x = int(op_data[1])
                if global_counts.get(x, 0) > 0:
                    global_counts[x] -= 1
                    debt[x] = debt.get(x, 0) + 1
                    
                    # Determine which side it was assumed on
                    clean(left, True)
                    clean(right, False)
                    
                    in_left = False
                    if left and x <= -left[0]:
                        in_left = True
                    elif right and x >= right[0]:
                        in_left = False
                    else:
                        # Should not happen if balanced, but fallback
                        if left: in_left = True
                        else: in_left = False
                    
                    if in_left: valid_left -= 1
                    else: valid_right -= 1
                    
                    rebalance()
                    
            elif op == "MEDIAN":
                clean(left, True)
                total = valid_left + valid_right
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
