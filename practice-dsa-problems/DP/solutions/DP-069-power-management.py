import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_states = int(input_data[ptr])
    ptr += 1
    p_power = []
    for _ in range(s_states):
        p_power.append(int(input_data[ptr]))
        ptr += 1
        perf = []
        for _ in range(s_states):
            perf.append(int(input_data[ptr]))
            ptr += 1
            trans_costs = []
            for _ in range(s_states):
                row = []
                for _ in range(s_states):
                    row.append(int(input_data[ptr]))
                    ptr += 1
                    trans_costs.append(row)
                    reqs = []
                    for _ in range(n):
                        reqs.append(int(input_data[ptr]))
                        ptr += 1

                    
    inf = float("inf")
    # DP[state] = min cost at time t
    # Init for t=0
    
    dp = [inf] * s_states
    for i in range(s_states):
        if perf[i] >= reqs[0]:
            dp[i] = p_power[i]
            
    for t in range(1, n):
        new_dp = [inf] * s_states
        r = reqs[t]
        
        # Try moving FROM prev TO curr
        for curr in range(s_states):
            if perf[curr] < r:
                continue
                
            best_curr = inf
            for prev in range(s_states):
                if dp[prev] != inf:
                    cost = (
                        dp[prev]
                        + trans_costs[prev][curr]
                        + p_power[curr]
                    )
                    if cost < best_curr:
                        best_curr = cost
            new_dp[curr] = best_curr
        dp = new_dp
        
    ans = min(dp)
    print(ans if ans != inf else -1)


if __name__ == "__main__":
    solve()
