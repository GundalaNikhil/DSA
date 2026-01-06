import sys

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_limit = int(input_data[ptr])
    ptr += 1
    adj = [[] for _ in range(n + 1)]
    labels = [0] * (n + 1)
    root = -1
    for i in range(1, n + 1):
        l = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        labels[i] = l
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    counts = {}
    visited_count = 0

    def dfs(u):
        nonlocal visited_count
        l = labels[u]
        curr_cnt = counts.get(l, 0) + 1
        if curr_cnt > k_limit:
            return
            
        counts[l] = curr_cnt
        visited_count += 1
        
        for v in adj[u]:
            dfs(v)
            
        counts[l] -= 1 # Backtrack count for correct path counting? 
        # Wait, if frequency limit is global per path or global?
        # Usually frequency limits are path-based in recursion unless specific constraints.
        # But this DFS effectively counts accessible nodes respecting limit on *current path*.
        # So we MUST decrement count when returning from recursion to maintain path property.
        # Although original code didn't do it because it was broken/missing.
        
    dfs(root)
    print(visited_count)


if __name__ == "__main__":
    solve()
