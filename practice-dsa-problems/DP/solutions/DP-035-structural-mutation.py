import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n_limit = int(input_data[ptr])
    ptr += 1
    m_nodes = int(input_data[ptr])
    ptr += 1
    e_edges = int(input_data[ptr])
    ptr += 1
    adj = [[] for _ in range(m_nodes + 1)]
    fragile_edges = []
    for i in range(e_edges):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        f = int(input_data[ptr])
        ptr += 1
        if f == 1:
            fid = len(fragile_edges)
            fragile_edges.append((u, v, r))
            adj[u].append((v, r, fid))
            adj[v].append((u, r, fid))
        else:
            adj[u].append((v, r, -1))
            adj[v].append((u, r, -1))
            
    memo = {}
    ans = get_max_reward(0, 1, 0, n_limit, adj, memo)
    print(ans if ans != -float("inf") else 0)


def get_max_reward(step, u, mask, n_limit, adj, memo):
    if step == n_limit:
        return 0
    state = (step, u, mask)
    if state in memo:
        return memo[state]
        
    res = -float("inf")
    for v, r, fid in adj[u]:
        if fid == -1:
            # Normal edge
            res = max(res, r + get_max_reward(step + 1, v, mask, n_limit, adj, memo))
        else:
            # Fragile edge, checking if used
            if not (mask & (1 << fid)):
                # Use it, mark used
                res = max(res, r + get_max_reward(step + 1, v, mask | (1 << fid), n_limit, adj, memo))
                
    memo[state] = res
    return res


if __name__ == "__main__":
    solve()
