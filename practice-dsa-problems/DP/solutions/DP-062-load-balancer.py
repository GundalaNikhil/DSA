import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_req = int(input_data[ptr])
    ptr += 1
    s_servers = int(input_data[ptr])
    ptr += 1
    p_overload = int(input_data[ptr])
    ptr += 1
    weights = []
    for _ in range(n_req):
        weights.append(int(input_data[ptr]))
        ptr += 1
        caps = []
        for _ in range(s_servers):
            caps.append(int(input_data[ptr]))
            ptr += 1
            lats = []
            for _ in range(s_servers):
                lats.append(int(input_data[ptr]))
                ptr += 1
            lats.append(int(input_data[ptr]))
            ptr += 1
            
    dp = {tuple([0] * s_servers): 0}
    
    for w in weights:
        new_dp = {}
        for loads, cost in dp.items():
            for i in range(s_servers):
                new_loads = list(loads)
                new_loads[i] += w
                
                over_penalty = p_overload if new_loads[i] > caps[i] else 0
                new_cost = cost + lats[i] + over_penalty
                
                nl_tuple = tuple(new_loads)
                if nl_tuple not in new_dp or new_dp[nl_tuple] > new_cost:
                    new_dp[nl_tuple] = new_cost
        dp = new_dp
        
    print(min(dp.values()) if dp else 0)


if __name__ == "__main__":
    solve()
