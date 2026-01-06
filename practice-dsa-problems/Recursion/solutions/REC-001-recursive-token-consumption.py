import sys

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_bal = int(input_data[ptr])
    ptr += 1
    b_bal = int(input_data[ptr])
    ptr += 1
    costs = []
    for _ in range(n):
        ca = int(input_data[ptr])
        ptr += 1
        cb = int(input_data[ptr])
        ptr += 1
        ga = int(input_data[ptr])
        ptr += 1
        gb = int(input_data[ptr])
        ptr += 1
        costs.append((ca, cb, ga, gb))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(input_data[ptr]) - 1
        ptr += 1
        v = int(input_data[ptr]) - 1
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        
    tree_adj = [[] for _ in range(n)]
    visited = [False] * n
    stack = [0]
    visited[0] = True
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                tree_adj[u].append(v)
                stack.append(v)
                
    curr_a = a_bal
    curr_b = b_bal
    nodes_visited = 0

    def dfs(u, cur_a, cur_b):
        nonlocal nodes_visited
        ca, cb, ga, gb = costs[u]
        if cur_a >= ca and cur_b >= cb:
            nodes_visited += 1
            cur_a -= ca
            cur_b -= cb
            
            # Sort children based on cost sum
            sorted_children = sorted(
                tree_adj[u],
                key=lambda x: (costs[x][0] + costs[x][1]),
            )
            
            for v in sorted_children:
                cur_a, cur_b = dfs(v, cur_a, cur_b)
                
            cur_a += ga
            cur_b += gb
            
        return cur_a, cur_b

    dfs(0, curr_a, curr_b)
    print(nodes_visited)


if __name__ == "__main__":
    solve()
