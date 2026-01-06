import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    s_root = int(input_data[ptr])
    ptr += 1
    costs = []
    times = []
    for _ in range(n):
        costs.append(int(input_data[ptr]))
        ptr += 1
        times.append(int(input_data[ptr]))
        ptr += 1
        
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        adj[u].append(v)
        
    memo = {}

    def build(u):
        if u in memo:
            return memo[u]
            
        total_c = 0
        current_time = times[u - 1]
        max_dep_time = -1
        
        for v_dep in adj[u]:
            c_v, t_v = build(v_dep)
            total_c += c_v
            if t_v > max_dep_time:
                max_dep_time = t_v
                
        if max_dep_time > current_time:
             # Wait for dependency if it finishes later than our 'ideal' start
             # Logic is vague: "Recursive Build System".
             # Usually: finish_time = max(my_start + duration, dep_finish + duration)
             # But here `current_time` seems to be just `times[u-1]` (duration? or timestamp?).
             # Assuming times[u-1] is minimum finish time if no deps?
             current_time = max_dep_time
             
        # Add our cost/time?
        total_c += costs[u - 1]
        current_time += 1 # Some increment?
        
        # Original logic:
        # if max_dep_time > current_time:
        #    total_c += costs...
        #    current_time = max_dep_time + 1
        # It implies costs are only added if we wait? Or always?
        # Let's clean up structure to match "Build System" generally.
        # Cost = Sum(dep_costs) + My_Cost
        # Time = Max(dep_times) + My_Time (or 1?)
        
        # Re-reading original snippet:
        # `total_c += c_v` (sum dep costs)
        # `if max_dep_time > current_time`: (if delay needed?)
        #   `total_c += costs[u-1]` (add my cost?)
        #   `current_time = max_dep_time + 1`
        # 
        # Wait, if deps are faster, do we add our cost?
        # The structure `return memo[u]` was inside the `if`.
        # This implies if `max_dep_time <= current_time`, we don't return? Or loop continues?
        # But `current_time` was initialized to `times[u-1]`.
        
        # Refined Logic:
        # base_time = times[u-1]
        # if max(deps) > base_time: use max(deps) + 1, add extra cost?
        # else: use base_time, no extra cost (or just base cost)?
        
        # Let's implement:
        # defaults
        final_time = times[u-1]
        extra_cost = 0
        
        if max_dep_time > final_time:
            final_time = max_dep_time + 1
            extra_cost = costs[u-1]
            
        memo[u] = (total_c + extra_cost, final_time)
        return memo[u]

    sys.setrecursionlimit(300000)
    res_cost, res_time = build(s_root)
    print(f"{res_cost} {res_time}")


if __name__ == "__main__":
    solve()
