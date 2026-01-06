import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_chunk = int(input_data[ptr])
    ptr += 1
    m_val = int(input_data[ptr])
    ptr += 1
    l_bound = int(input_data[ptr])
    ptr += 1
    r_bound = int(input_data[ptr])
    ptr += 1
    d_diff = int(input_data[ptr])
    ptr += 1
    costs = []
    for _ in range(n):
        c = []
        for _ in range(m_val + 1):
            c.append(int(input_data[ptr]))
            ptr += 1
        costs.append(c)

    # dp[(current_chunk_sum, first_val_in_chunk)] = min_cost
    dp = {}
    dp[(0, -1)] = 0
    
    for i in range(n):
        new_dp = {}
        for (c_sum, first_v), total_cost in dp.items():
            # Try picking value x for current position i
            for x in range(m_val + 1):
                new_sum = c_sum + x
                # If this is start of chunk (first_v == -1), set it. Else keep.
                # Actually, if chunk resets, first_v becomes -1. 
                # Logic below: `new_first = first_v if first_v != -1 else x`
                new_first = first_v if first_v != -1 else x
                
                # Check if chunk ends at i
                is_chunk_end = ((i + 1) % k_chunk == 0) or (i == n - 1)
                
                cost_here = costs[i][x]
                
                if is_chunk_end:
                    # Validate constraints
                    # We only care if we are ending a chunk transition
                    if l_bound <= new_sum <= r_bound and abs(new_first - x) <= d_diff:
                        # If this is the very last index, we don't need to transition to 'reset' state
                        if i == n - 1:
                            key = (new_sum, new_first) 
                            new_dp[key] = min(new_dp.get(key, float('inf')), total_cost + costs[i][x])
                        else:
                            # Start next chunk fresh
                             new_dp[(0, -1)] = min(new_dp.get((0, -1), float('inf')), total_cost + costs[i][x])
                else:
                    # Not a chunk end, accumulate state
                    key = (new_sum, new_first)
                    new_dp[key] = min(new_dp.get(key, float('inf')), total_cost + costs[i][x])
                    
        dp = new_dp
        if not dp:
            print("-1")
            return

    res = min(dp.values())
    print(res if res != float('inf') else "-1")
if __name__ == '__main__':
    solve()