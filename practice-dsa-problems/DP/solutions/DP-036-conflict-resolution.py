import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    b = int(input_data[ptr])
    ptr += 1
    s_node = int(input_data[ptr])
    ptr += 1
    t_node = int(input_data[ptr])
    ptr += 1
    target_mask = int(input_data[ptr])
    ptr += 1
    adj = []
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        mask = int(input_data[ptr])
        ptr += 1
        adj.append((u, v, r, mask))
        
    num_masks = 1 << b
    inf = float("inf")
    # State: dp[u][mask] = max reward
    # Steps: N ?
    # It seems to be N iterations of bellman-ford-like relaxation?
    # Or just iterating N steps of path?
    # Code loop `for _ in range(n)`.
    # Original: `if u == s_node: dp[v][mask] = ...` inside loop `for _ in range(n)`?
    # No, `if u == s_node` block was OUTSIDE the N loop?
    # Original:
    # 36: for u, v, r, mask in adj:
    # 37:     if u == s_node: ...
    # 39:     for _ in range(n): ...
    # So initial step (from S) done once?
    # Then N iterations of propagation?
    
    dp = [[-inf] * num_masks for _ in range(m + 1)] # Wait, range(m+1)? Nodes are up to ?
    # Nodes seem to be arbitrary or 1..m?
    # Problem didn't specify node range explicitly but code used `dp[v][mask]`.
    # Max node index? Not parsed.
    # Usually N is nodes? But N is first input. "n" usually steps or nodes.
    # Code `for _ in range(n)` implies steps.
    # Nodes indices used in `dp`.
    # We should find max node index. Or use a map?
    # `dp = [[-inf] * num_masks for _ in range(105)]`?
    # Let's assume nodes are dense 1..N or something. Or use dict.
    # Original code `dp = [[-inf] * num_masks for _ in range(n + 1)]`.
    # So max node index is N?
    # But input says `n` is first arg.
    # Is `n` node count? Or steps?
    # If `for _ in range(n)`, maybe Bellman-Ford on N nodes?
    # Let's stick to list if N is small, or dict if not.
    # Assuming code logic `range(n + 1)` implies N is max node ID.
    
    dp = [[-inf] * num_masks for _ in range(n + 10)] # Safety padding or just n+1
    
    # Initialization
    for u, v, r, mask in adj:
        if u == s_node:
             # Mask check?
             # If starting, our mask is ???
             # Problem "Conflict Resolution": mask tracks conflicts?
             # Code: `dp[v][mask] = ...`. starting mask 0?
             # Or edge mask IS the new mask state?
             # It sets `dp[v][mask]`.
             # Accumulating reward `r`.
             dp[v][mask] = max(dp[v][mask], r)
             
    # Iterations
    for _ in range(n):
        any_change = False
        for u, v, r, mask in adj:
            if u == s_node: continue # Already handled? Or handled as part of flow?
            # Original code excluded `u == s_node` inside loop.
            
            for m_in in range(num_masks):
                if dp[u][m_in] != -inf:
                    m_out = m_in & mask
                    # Update
                    if dp[v][m_out] < dp[u][m_in] + r:
                        dp[v][m_out] = dp[u][m_in] + r
                        any_change = True
                        
        if not any_change:
            break
            
    ans = dp[t_node][target_mask]
    print(ans if ans != -inf else -1)


if __name__ == "__main__":
    solve()
