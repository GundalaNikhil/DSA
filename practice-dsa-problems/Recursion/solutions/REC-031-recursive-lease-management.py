import sys
from collections import defaultdict

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    R_types = int(input_data[ptr])
    ptr += 1
    lease_lengths = []
    for _ in range(R_types):
        lease_lengths.append(int(input_data[ptr]))
        ptr += 1
        node_props = []
        adj = defaultdict(list)
        root = -1
    for i in range(1, n + 1):
        res_type = int(input_data[ptr])
        ptr += 1
        cost = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        node_props.append((res_type - 1, cost))
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    memo = {}
    depths = [0] * (n + 1)

    def calc_depth(u, d):
        depths[u] = d
        for v in adj[u]:
            calc_depth(v, d + 1)
            
    if root != -1:
        calc_depth(root, 0)
        
    def get_min_cost(u, expiries):
        state = (u, expiries)
        if state in memo:
            return memo[state]
            
        r_type, r_cost = node_props[u - 1]
        curr_depth = depths[u]
        
        # Option 1: Renew lease
        new_exp = list(expiries)
        new_exp[r_type] = curr_depth + lease_lengths[r_type]
        cost_renew = r_cost
        
        for v in adj[u]:
            cost_renew += get_min_cost(v, tuple(new_exp))
            
        res = cost_renew
        
        # Option 2: Don't renew (only if valid)
        if expiries[r_type] >= curr_depth:
            cost_no_renew = 0
            for v in adj[u]:
                cost_no_renew += get_min_cost(v, expiries)
            res = min(res, cost_no_renew)
            
        memo[state] = res
        return res

    if root != -1:
        # Initial expiries are -1 (expired)
        print(get_min_cost(root, tuple([-1] * R_types)))
    else:
        print(0)


if __name__ == "__main__":
    solve()
