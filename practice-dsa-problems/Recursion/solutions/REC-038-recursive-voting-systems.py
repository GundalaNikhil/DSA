import sys
from collections import defaultdict

sys.setrecursionlimit(500000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_count = int(input_data[ptr])
    ptr += 1
    strategies = []
    for _ in range(s_count):
        strategies.append(input_data[ptr])
        ptr += 1
        base_values = []
        adj = defaultdict(list)
        root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        par = int(input_data[ptr])
        ptr += 1
        base_values.append(v)
        if par == 0:
            root = i
        else:
            adj[par].append(i)
            
    def get_strategy_values(u):
        # Base case: leaf node
        if not adj[u]:
            return [base_values[u - 1]] * s_count
            
        child_results = []
        for v_child in adj[u]:
            child_results.append(get_strategy_values(v_child))
            
        results = []
        for s in range(s_count):
            op = strategies[s]
            s_vals = [cr[s] for cr in child_results]
            
            res = 0
            if op == "SUM":
                res = sum(s_vals)
            elif op == "MIN":
                res = min(s_vals)
            else: # MAX
                res = max(s_vals)
                
            results.append(res + base_values[u - 1])
            
        return results

    if root != -1:
        all_vals = get_strategy_values(root)
        all_vals.sort()
        # Median?
        print(all_vals[s_count // 2])
    else:
        print(0)


if __name__ == "__main__":
    solve()
