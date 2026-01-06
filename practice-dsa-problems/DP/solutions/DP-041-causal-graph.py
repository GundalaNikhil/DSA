import sys

sys.setrecursionlimit(1000000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    s_node = int(input_data[ptr])
    ptr += 1
    t_node = int(input_data[ptr])
    ptr += 1
    rewards = []
    for _ in range(n):
        rewards.append(int(input_data[ptr]))
        ptr += 1
        adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        for _ in range(m):
            u = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
        adj[u].append(v)
        in_degree[v] += 1
        
    inf = float("inf")
    dp = [-inf] * (n + 1)
    
    # Init simple DP on DAG?
    # Logic: `dp[s_node] = rewards[s_node - 1]`
    # Use Topological Sort.
    dp[s_node] = rewards[s_node - 1]
    
    topo_order = []
    # Initial queue: in-degree 0 nodes
    q = [i for i in range(1, n + 1) if in_degree[i] == 0]
    
    # If s_node is not in q (cycle or internal node?), we might miss it if we only process q.
    # But s_node IS the start.
    # If DAG, standard BFS works.
    # If s_node has in-degree > 0, it won't be in initial q?
    # Original logic: `q = [i for i ... if curr_in[i] == 0]`.
    # And used `curr_in` which was copy of `in_degree`.
    # My logic: maintain `in_degree` array.
    
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        topo_order.append(u)
        
        for v in adj[u]:
             in_degree[v] -= 1
             if in_degree[v] == 0:
                 q.append(v)
                 
    # DP propagation in topo order
    for u in topo_order:
         if dp[u] == -inf:
             continue
         for v in adj[u]:
             dp[v] = max(dp[v], dp[u] + rewards[v - 1])
             
    ans = dp[t_node]
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
