import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        w = int(input_data[ptr])
        ptr += 1
        k = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((w, k))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    memo_cost = [0] * (n + 1)
    sys.setrecursionlimit(300000)

    def dfs(u):
        w, k = nodes[u - 1]
        children_costs = []
        for v in adj[u]:
            children_costs.append(dfs(v))
            
        if not children_costs:
            memo_cost[u] = w
            return w
            
        children_costs.sort(reverse=True)
        # Taking top k most expensive children to propagate?
        total = w + sum(children_costs[:k])
        memo_cost[u] = total
        return total

    if root != -1:
        print(dfs(root))
    else:
        print(0)


if __name__ == "__main__":
    solve()
