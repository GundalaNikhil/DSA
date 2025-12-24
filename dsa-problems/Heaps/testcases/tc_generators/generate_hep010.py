
import random
import heapq
import yaml

def solve(n, m, k, d, A, B):
    # Max-heap: stores (-value, ...)
    pq = []
    
    # Region 1: i - j >= d => j <= i - d
    # Iterate rows i: d to n-1
    for i in range(d, n):
        limit_j = i - d
        if limit_j < 0: continue # Should not happen with range start
        
        # Row i, valid j in [0, limit_j]
        # A[i] is constant.
        if A[i] >= 0:
            # B is decreasing positive (or decreasing real).
            # A[i] >= 0 => max product where B[j] is max => j=0
            # Next move: j increase (0 -> 1 -> ... -> limit_j)
            val = A[i] * B[0]
            # (val, type, fixed_idx, curr_var, var_step, var_limit)
            # type 0: fixed i, moving j
            heapq.heappush(pq, (-val, 0, i, 0, 1, limit_j))
        else:
            # A[i] < 0 => max product where B[j] is min => j=limit_j
            # B is decreasing, so B[limit_j] is smallest (most negative or least positive)
            # Wait, B is decreasing. B[0] > B[1] ... > B[m-1]
            # If A[i] < 0, we want B[j] to be as small (negative) as possible to make product large positive
            # OR as small (least positive) as possible to make product least negative.
            # In short, we want smallest B[j]. Smallest B[j] is at largest index.
            # Max index is limit_j.
            # So start at limit_j, move down to 0?
            val = A[i] * B[limit_j]
            heapq.heappush(pq, (-val, 0, i, limit_j, -1, 0))

    # Region 2: j - i >= d => i <= j - d
    # Iterate cols j: d to m-1
    for j in range(d, m):
        limit_i = j - d
        if limit_i < 0: continue
        
        # Col j, valid i in [0, limit_i]
        # B[j] is constant
        if B[j] >= 0:
            # A is decreasing. Max A at i=0.
            # Start i=0, move up to limit_i
            val = A[0] * B[j]
            # type 1: fixed j, moving i
            heapq.heappush(pq, (-val, 1, j, 0, 1, limit_i))
        else:
            # B[j] < 0. Want smallest A. Smallest A at largest index i=limit_i.
            val = A[limit_i] * B[j]
            heapq.heappush(pq, (-val, 1, j, limit_i, -1, 0))
            
    res = []
    while k > 0 and pq:
        neg_val, type_, fixed, var, step, limit = heapq.heappop(pq)
        val = -neg_val
        res.append(val)
        k -= 1
        
        next_var = var + step
        valid = False
        if step > 0:
            if next_var <= limit: valid = True
        else:
            if next_var >= limit: valid = True
            
        if valid:
            if type_ == 0: # Fixed Row i=fixed, moving j=var
                new_val = A[fixed] * B[next_var]
                heapq.heappush(pq, (-new_val, 0, fixed, next_var, step, limit))
            else: # Fixed Col j=fixed, moving i=var
                new_val = A[next_var] * B[fixed]
                heapq.heappush(pq, (-new_val, 1, fixed, next_var, step, limit))
                
    return res

def generate_test_cases():
    test_cases = []
    
    # 1. SAMPLE
    A_sample = [9, 7, 5]
    B_sample = [8, 3, 1]
    n, m, k, d = 3, 3, 3, 1
    test_cases.append({
        "input": f"{n} {m} {k} {d}\n{' '.join(map(str, A_sample))}\n{' '.join(map(str, B_sample))}",
        "output": " ".join(map(str, solve(n, m, k, d, A_sample, B_sample))),
        "category": "sample",
        "description": "Sample case"
    })
    
    # 2. EDGE
    # d = 0 (All pairs valid)
    n, m, k, d = 2, 2, 4, 0
    A = [10, -10]
    B = [5, -5]
    # Products: 50, -50, -50, 50. Output: 50 50 -50 -50
    test_cases.append({
        "input": f"{n} {m} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}",
        "output": " ".join(map(str, solve(n, m, k, d, A, B))),
        "category": "edge",
        "description": "d=0, mixed signs"
    })
    
    # d >= max(n, m) => No pairs? Actually constraints say d < max(n, m).
    # d large enough to restrict heavily
    n, m, k, d = 5, 5, 5, 4
    A = [10, 8, 6, 4, 2]
    B = [10, 8, 6, 4, 2]
    # |i-j| >= 4. Indices (0,4) and (4,0).
    # (0,4): A[0]*B[4] = 10*2=20
    # (4,0): A[4]*B[0] = 2*10=20
    # Only 2 pairs. k=5. Should return 20 20.
    test_cases.append({
        "input": f"{n} {m} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}",
        "output": " ".join(map(str, solve(n, m, k, d, A, B))),
        "category": "edge",
        "description": "d large, few valid pairs"
    })
    
    # 3. BOUNDARY
    # All Negative
    n, m, k, d = 3, 3, 5, 1
    A = [-1, -3, -5]
    B = [-2, -4, -6]
    test_cases.append({
        "input": f"{n} {m} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}",
        "output": " ".join(map(str, solve(n, m, k, d, A, B))),
        "category": "boundary",
        "description": "All negative numbers"
    })
    
    # 4. STRESS
    n = 1000
    m = 1000
    k = 1000
    d = 100
    A = sorted([random.randint(-10000, 10000) for _ in range(n)], reverse=True)
    B = sorted([random.randint(-10000, 10000) for _ in range(m)], reverse=True)
    test_cases.append({
        "input": f"{n} {m} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}",
        "output": " ".join(map(str, solve(n, m, k, d, A, B))),
        "category": "stress",
        "description": "Large random inputs"
    })
    
    return test_cases

def main():
    test_cases = generate_test_cases()
    
    yaml_output = {
        "problem_id": "HEP-010",
        "test_cases": test_cases
    }
    
    class BlockDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(BlockDumper, self).increase_indent(flow, False)

    def str_presenter(dumper, data):
        if '\n' in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter, Dumper=BlockDumper)
    
    output_path = "HEP-010-topk-products-index-gap.yaml"
    with open(output_path, 'w') as f:
        yaml.dump(yaml_output, f, Dumper=BlockDumper, default_flow_style=False, sort_keys=False)
    
    print(f"Generated {len(test_cases)} test cases in {output_path}")

if __name__ == "__main__":
    main()
