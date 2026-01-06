import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s = int(input_data[ptr])
    ptr += 1
    budget = int(input_data[ptr])
    ptr += 1
    u_cap = int(input_data[ptr])
    ptr += 1
    dec = int(input_data[ptr])
    ptr += 1
    base_costs = []
    incs = []
    for _ in range(s):
        base_costs.append(int(input_data[ptr]))
        incs.append(int(input_data[ptr + 1]))
        ptr += 2
        
    dp = {}
    init_state = (0,) * s
    dp[init_state] = 0
    max_steps = 0
    
    for step in range(n):
        new_dp = {}
        for state, cost in dp.items():
            if cost > budget:
                continue
            max_steps = max(max_steps, step)
            
            # Try to upgrade ONE slot/variable j?
            for j in range(s):
                this_cost = base_costs[j] + state[j]
                
                if cost + this_cost <= budget:
                    new_u = list(state)
                    # Upgrade j
                    new_u[j] = min(u_cap, new_u[j] + incs[j])
                    
                    # Downgrade others
                    for k in range(s):
                        if k != j:
                            new_u[k] = max(0, new_u[k] - dec)
                            
                    target_state = tuple(new_u)
                    if (
                        target_state not in new_dp
                        or new_dp[target_state] > cost + this_cost
                    ):
                        new_dp[target_state] = cost + this_cost
                        
        if not new_dp:
            break
        dp = new_dp
        if dp:
            max_steps = max(max_steps, step + 1)
            
    print(max_steps)


if __name__ == "__main__":
    solve()
