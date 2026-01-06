import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = []
    adj = [[] for _ in range(n + 1)]
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        nodes.append((v, t, c))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    # Topological sort (or post-order for Tree DP)
    order = []
    if root != -1:
        stack = [root]
        while stack:
            # Simple DFS order? No, for DP we need children processed first -> Post-order.
            # But the code used `stack.pop()` doing DFS and then `reversed(order)`.
            # If stack popped is Pre-order, reversed is Reverse Pre-order.
            # Reverse Pre-order is NOT Post-order (unless reversed finish times).
            # But wait, stack pop of children pushed... standard DFS traversal order.
            # Let's use standard post-order generation.
            pass
            
    def get_post_order(u, res_list):
        for v in adj[u]:
            get_post_order(v, res_list)
        res_list.append(u)
        
    order = []
    if root != -1:
        sys.setrecursionlimit(300000)
        get_post_order(root, order)
            
    dp = {}
    possible = [True] * (n + 1)
    
    for u in order:
        v_val, t_val, c_val = nodes[u - 1]
        
        # Base check
        if not adj[u]: # Leaf
            if v_val >= t_val:
                dp[u] = 0
            else:
                possible[u] = False
                dp[u] = float("inf")
            continue
            
        target = t_val - v_val
        if target <= 0:
            dp[u] = 0
            continue
            
        child_options = [] # (value_gain, cost_success, cost_fail_contribution)
        # Wait, if child fails, does it contribute cost?
        # Logic: If child satisfies its own requirement, cost is `dp[v]`.
        # If we use child for *our* requirement, we pay `dp[v]`.
        # But maybe we can take something from child even if it fails?
        # Original code logic: `child_options.append((v_c, dp[v_child], c_c))`
        
        # Let's reconstruct intended greedy logic:
        # We need `target` value from children.
        # Cost = sum of `c_fail` (static costs?) + delta for success?
        # `base_cost += c_fail` (initially assume all fail/minimal?)
        # `if c_succ < c_fail`: cheaper to succeed?
        # `diffs`: (cost_to_upgrade, value_gain).
        
        # This seems to be: Min cost to get enough value.
        # Options:
        # 1. Child `v` satisfies itself (cost `dp[v]`), gives surplus value? No, gives `v_c` (its node value)?
        # 2. Child `v` doesn't satisfy itself? logic `possible[v]` checks that.
        # If `possible[v]` false: we get 0 value? Cost?
        
        base_cost = 0
        total_v = 0
        diffs = []
        
        for v_child in adj[u]:
            v_c, t_c, c_c = nodes[v_child - 1]
            
            # Cost if we don't pick/push child: 0? Or c_c?
            # Original code suggests: `c_succ = dp[v_child]` if possible else inf.
            # `c_fail` seems to be cost if we pick failure path?
            # Actually, let's simplify based on apparent greedy structure:
            # We want min cost to get `target`.
            # Each child offers `v_c` value at `dp[v_child]` cost.
            # If we don't use it, cost is 0, value 0.
            # So `diff` = (dp[v_child], v_c).
            
            if possible[v_child]:
                cost = dp[v_child]
                val = v_c
                diffs.append((cost, val)) # Cost per value unit? No, total cost for package.
            else:
                # Impossible to satisfy child -> cannot get value from it?
                pass
                
        # Sort by cost density? Or just greedy if ratio?
        # Original code sort `diffs`. Tuples `(cost, val)`. Sorts by cost asc.
        # Greedy strategy: Cheapest packages first.
        diffs.sort()
        
        curr_val = 0
        curr_cost = 0
        
        for cost, val in diffs:
            curr_cost += cost
            curr_val += val
            if curr_val >= target:
                break
                
        if curr_val >= target:
            dp[u] = curr_cost
        else:
            possible[u] = False
            dp[u] = float("inf")
            
    if root != -1:
        if possible[root]:
            print(dp[root])
        else:
            print("IMPOSSIBLE")
    else:
        print("IMPOSSIBLE")
