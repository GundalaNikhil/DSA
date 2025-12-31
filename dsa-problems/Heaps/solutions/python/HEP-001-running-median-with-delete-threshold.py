import sys
import heapq
from collections import defaultdict

class Solution:
    def process_operations(self, T: int, operations: list) -> list:
        # Left is max heap (store negative values), Right is min heap
        left = []
        right = []
       
        left_debt = defaultdict(int)
        right_debt = defaultdict(int)
        
        # logical counts
        l_cnt = 0
        r_cnt = 0
        
        results = []
        
        def clean_left():
            while left and left_debt[-left[0]] > 0:
                val = -heapq.heappop(left)
                left_debt[val] -= 1

        def clean_right():
            while right and right_debt[right[0]] > 0:
                val = heapq.heappop(right)
                right_debt[val] -= 1
        
        def balance():
            # maximize l_cnt, r_cnt constraint: 
            # l_cnt == r_cnt OR l_cnt == r_cnt + 1
            
            # Clean first to ensure tops are valid candidates for moving
            clean_left()
            clean_right()
            
            nonlocal l_cnt, r_cnt
            
            while l_cnt > r_cnt + 1:
                clean_left() # ensure we move a valid item
                val = -heapq.heappop(left)
                heapq.heappush(right, val)
                l_cnt -= 1
                r_cnt += 1
                clean_left()
                
            clean_right()
            while r_cnt > l_cnt:
                clean_right()
                val = heapq.heappop(right)
                heapq.heappush(left, -val)
                r_cnt -= 1
                l_cnt += 1
                clean_right()

        counts = defaultdict(int)
        for op_data in operations:
            op = op_data[0]
            
            if op == "ADD":
                x = int(op_data[1])
                counts[x] += 1
                # Naive push then balance
                # Push to left first? Or compare with left top?
                
                clean_left()
                if not left or x <= -left[0]:
                    heapq.heappush(left, -x)
                    l_cnt += 1
                else:
                    heapq.heappush(right, x)
                    r_cnt += 1
                
                balance()
                
            elif op == "DEL":
                x = int(op_data[1])
                if counts[x] > 0:
                    counts[x] -= 1
                    # Decide where to delete from
                    clean_left()
                    clean_right()
                    
                    
                    
                    deleted = False
                    if left and x <= -left[0]:
                         left_debt[x] += 1
                         l_cnt -= 1
                         deleted = True
                    else:
                        right_debt[x] += 1
                        r_cnt -= 1
                        deleted = True
                    
                    if deleted:
                        balance()
                    
            elif op == "MEDIAN":
                clean_left()
                # total valid size
                if (l_cnt + r_cnt) == 0:
                    results.append("EMPTY")
                elif (l_cnt + r_cnt) < T:
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
    
    q_str = next(it, None)
    if q_str is None: return
    q = int(q_str)
    t_str = next(it, None)
    if t_str is None: return
    T = int(t_str)
    
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

if __name__ == "__main__":
    main()
