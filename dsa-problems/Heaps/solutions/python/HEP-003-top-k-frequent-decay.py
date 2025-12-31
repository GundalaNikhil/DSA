import sys
import math
import heapq

class Solution:
    def process_operations(self, d: int, k: int, operations: list) -> list:
        
        state = {} 
        
        heap = []
        
        results = []

        for op_data in operations:
            op_type = op_data[0]
            
            if op_type == "ADD":
                key = op_data[1]
                t = int(op_data[2])
                
                current_count = 0.0
                if key in state:
                    c, last_u, ver = state[key]

                    if t >= last_u:
                        steps = (t - last_u) // d
                        if steps > 0:
                            c *= (0.5 ** steps)
                    current_count = c
                
                # Add 1
                new_count = current_count + 1.0
                # Update state: last_update becomes t (resets phase)
                new_ver = (state[key][2] + 1) if key in state else 1
                state[key] = (new_count, t, new_ver)
                
                heapq.heappush(heap, (-new_count, key, new_ver))
                
            else:
                # QUERY
                t = int(op_data[1])
                
                top_k = []
                temp_back = []
                
                while len(top_k) < k and heap:
                    neg_c, key, ver = heapq.heappop(heap)
                    
                    if key not in state or state[key][2] != ver:
                        continue
                        
                    c, last_u, current_ver = state[key]
                    
                    steps = 0
                    if t >= last_u:
                        steps = (t - last_u) // d
                    
                    if steps > 0:
                        decayed_c = c * (0.5 ** steps)
                        
                        new_last_u = last_u + steps * d
                        
                        new_ver = current_ver + 1
                        state[key] = (decayed_c, new_last_u, new_ver)
                        
                        heapq.heappush(heap, (-decayed_c, key, new_ver))
                        
                    else:
                        top_k.append(key)
                        temp_back.append((-c, key, ver))
                
                if not top_k:
                    results.append("EMPTY")
                else:
                    results.append(" ".join(top_k))
                
                for item in temp_back:
                    heapq.heappush(heap, item)
                    
        return results

def process_operations(d: int, k: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(d, k, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        d = int(next(it))
        k = int(next(it))
        operations = []
        for _ in range(q):
            try:
                op = next(it)
            except StopIteration:
                break
                
            if op == "ADD":
                key = next(it)
                t = next(it)
                operations.append([op, key, t])
            else:
                t = next(it)
                operations.append([op, t])
        
        result = process_operations(d, k, operations)
        print("\n".join(result))
    except StopIteration:
        # Fallback if initial params or arguments fail
        if 'operations' in locals() and operations:
             result = process_operations(d, k, operations)
             print("\n".join(result))

if __name__ == "__main__":
    main()
