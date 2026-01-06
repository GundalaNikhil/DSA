import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_steps = int(input_data[ptr])
    ptr += 1
    m_nodes = int(input_data[ptr])
    ptr += 1
    e_edges = int(input_data[ptr])
    ptr += 1
    edges_by_time = [[] for _ in range(n_steps + 1)]
    for _ in range(e_edges):
        t = int(input_data[ptr])
        ptr += 1
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        w = int(input_data[ptr])
        ptr += 1
        if t <= n_steps:
             edges_by_time[t].append((u, v, w))
             
    inf = float("inf")
    dp = [[-inf] * (m_nodes + 1) for _ in range(n_steps + 1)]
    dp[0][1] = 0 # Starting at node 1 at time 0
    
    available_edges = []
    
    for s in range(1, n_steps + 1):
        # Evolving state space: at each step, new edges might become available (accumulate)
        # Edges `edges_by_time[s]` are added at step s.
        available_edges.extend(edges_by_time[s])
        
        # Or maybe edges are ONLY available at time T?
        # Problem "Evolving State Space": edges might be added dynamically.
        # Assuming cumulative.
        
        for u, v, w in available_edges:
             # Relax edges. Node u at s-1 -> Node v at s.
             if dp[s - 1][u] != -inf:
                 dp[s][v] = max(dp[s][v], dp[s - 1][u] + w)
                 
    ans = dp[n_steps][1:]
    # If list is empty (e.g. no nodes?), handle gracefully. But m_nodes >= 1.
    res = max(ans) if ans else -inf
    print(res if res != -inf else -1)


if __name__ == "__main__":
    solve()
