import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    node_data = {}
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        s = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        node_data[i] = (v, s)
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    for u in adj:
        adj[u].sort()
        
    pre_order = []
    stack = [root]
    # Iterative DFS to build preorder?
    # Simple recursive function might clarify intent if allowed, but iterative is fine if correct.
    # Logic: Traverse whole tree, applying side effects cumulatively?
    # Original code had weird nesting.
    
    # Let's fix loop structure first.
    if root == -1:
        return
        
    # Re-implement simple DFS traversal
    dfs_stack = [root]
    path = [] # To accumulate side effects? No, "cascading side effects" usually means value depends on ancestors.
    
    # Actually, the problem logic seems to be:
    # Traverse tree. Maintain sum of 's' (side effect) from ancestors.
    # Current node effective value = v - sum(s of ancestors).
    # Sum all effective values? Or print final total sum?
    # The original code printed `total_sum` at the end presumably.
    
    total_sum = 0
    
    # Recursive helper is cleaner
    def traverse(u, acc_side_effect):
        nonlocal total_sum
        val, s = node_data[u]
        effective_val = val - acc_side_effect
        total_sum += effective_val
        
        # Children inherit current s plus previous acc
        new_acc = acc_side_effect + s
        
        # Sort children for deterministic order if needed, though sum is commutative unless side effects vary by order?
        # Assuming just tree traversal.
        
        for v in adj[u]:
            traverse(v, new_acc)
            
    traverse(root, 0)
    print(total_sum)


if __name__ == "__main__":
    solve()
