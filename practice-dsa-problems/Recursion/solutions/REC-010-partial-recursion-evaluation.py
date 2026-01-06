import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    d_limit = int(input_data[ptr])
    ptr += 1
    nodes = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        exact = int(input_data[ptr])
        ptr += 1
        estimate = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((exact, estimate))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    sys.setrecursionlimit(300000)

    def dfs(u, depth):
        exact, estimate = nodes[u - 1]
        if depth > d_limit:
            return estimate
            
        total = exact
        for v in adj[u]:
            total += dfs(v, depth + 1)
        return total

    if root != -1:
        print(dfs(root, 0))
    else:
        print(0)


if __name__ == "__main__":
    solve()
