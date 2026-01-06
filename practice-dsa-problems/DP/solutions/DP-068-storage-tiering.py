import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    t_steps = int(input_data[ptr])
    ptr += 1
    m_cost = int(input_data[ptr])
    ptr += 1
    costs = []
    for _ in range(t_steps):
        row = []
        for _ in range(n):
            row.append(int(input_data[ptr]))
            ptr += 1
            costs.append(row)

            
    inf = float("inf")
    # DP for each file i:
    # d0: min cost ending in slow tier
    # d1: min cost ending in fast tier
    # Sum up for all files.
    
    total_min_cost = 0
    
    for i in range(n):
        d0, d1 = 0, inf # Start at slow? Or 0 cost initially?
        # Initial: time 0. Code assumes `d0` starts 0, `d1` inf (all in slow tier initially).
        
        for t in range(t_steps):
            # Cost at time t
            # Slow cost: costs[t][i]
            # Fast cost: 0? Code implies specific cost logic.
            # Code:
            # nd0 = min(d0 + cur_slow, d1 + m_cost + cur_slow)
            # nd1 = min(d1, d0 + m_cost) (Fast tier cost 0?)
            
            cur_slow = costs[t][i] # Variable name missing in original code snippet (`cur_slow_cost` vs `cur_slow`?)
            # Original code: `cur_slow_cost = costs[t][i]`. 
            # Then: `nd0 = min(d0 + cur_slow, ...)` -> `cur_slow` is undefined?
            # It seems user meant `cur_slow_cost`.
            
            # Logic:
            # d0 (Slow): Stay Slow (d0 + cost) OR Move Fast->Slow (d1 + move_cost + cost)
            # d1 (Fast): Stay Fast (d1 + 0?) OR Move Slow->Fast (d0 + move_cost + 0?)
            
            nd0 = min(d0 + cur_slow, d1 + m_cost + cur_slow)
            nd1 = min(d1, d0 + m_cost) # Fast storage has 0 access cost in this problem?
            
            d0, d1 = nd0, nd1
            
        total_min_cost += min(d0, d1)
        
    print(total_min_cost)


if __name__ == "__main__":
    solve()
