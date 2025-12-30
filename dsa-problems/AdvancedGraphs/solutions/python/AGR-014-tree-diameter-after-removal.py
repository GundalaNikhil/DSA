import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def max_diameter_after_removal(n: int, edges: list[tuple[int, int]]) -> int:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    height = [0] * n
    diam = [0] * n
    up_height = [0] * n
    up_diam = [0] * n
    
    # DFS 1: Bottom-up
    def dfs1(u, p):
        max_h1, max_h2 = -1, -1
        max_d = 0
        
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u)
            max_d = max(max_d, diam[v])
            if height[v] > max_h1:
                max_h2 = max_h1
                max_h1 = height[v]
            elif height[v] > max_h2:
                max_h2 = height[v]
        
        height[u] = 1 + max_h1
        diam[u] = max(max_d, (max_h1 + 1) + (max_h2 + 1))
        
    dfs1(0, -1)
    
    ans = 0
    
    # DFS 2: Top-down
    def dfs2(u, p):
        nonlocal ans
        if p != -1:
            ans = max(ans, max(diam[u], up_diam[u]))
            
        # Collect arms: (length_from_u, diam_of_component)
        # Up arm
        arms = []
        if p != -1:
            arms.append((up_height[u], up_diam[u]))
        else:
            arms.append((-1, 0)) # Dummy for root
            
        children = []
        for v in adj[u]:
            if v != p:
                children.append(v)
                arms.append((height[v] + 1, diam[v]))
                
        # We need top 3 lengths and top 2 diams
        # Sort is O(deg log deg). Total O(N log N). Acceptable.
        # Or O(deg) with selection.
        
        # Sort arms by length descending
        arms.sort(key=lambda x: x[0], reverse=True)
        top3_len = [x[0] for x in arms[:3]]
        while len(top3_len) < 3: top3_len.append(-1)
        
        # Sort arms by diam descending
        arms.sort(key=lambda x: x[1], reverse=True)
        top2_diam = [x[1] for x in arms[:2]]
        while len(top2_diam) < 2: top2_diam.append(0)
        
        # Map for quick lookup? No, duplicate lengths possible.
        # Just filter.
        
        for v in children:
            v_len = height[v] + 1
            v_diam = diam[v]
            
            # up_height[v] = 1 + max(other lengths)
            best_len = top3_len[0] if top3_len[0] != v_len else top3_len[1]
            # Handle duplicates: if v_len appears multiple times, we can pick it.
            # If top3_len has [5, 5, 4] and v_len is 5, remaining is 5.
            
            # Robust way:
            current_lens = []
            count = 0
            for l in top3_len:
                if l == v_len and count == 0:
                    count += 1
                    continue
                current_lens.append(l)
            
            up_height[v] = 1 + current_lens[0]
            
            # up_diam[v]
            # 1. Max diam of others
            best_diam = top2_diam[0]
            if best_diam == v_diam:
                # Check if unique
                # Count occurrences in top2
                c = 0
                for d in top2_diam:
                    if d == v_diam: c += 1
                
                # We need to check if v is the ONLY source of this diam.
                # This is tricky if multiple children have same diam.
                # Use a rescan to handle duplicates safely.
                pass
                
            # Re-scanning top 2 diams excluding v
            # Since we sorted arms by diam, we can just pick.
            # We need original arms list or similar.
            
            # Avoid per-child O(deg^2); use top-k logic efficiently.
            # We have sorted lists.
            
            # Max diam excluding v
            d_excl = -1
            c = 0
            for val in top2_diam:
                if val == v_diam and c == 0:
                    c += 1
                    continue
                d_excl = val
                break
            if d_excl == -1: d_excl = 0 # Should not happen if padded
            
            # Path through u excluding v
            # Sum of top 2 lengths in current_lens
            path_excl = current_lens[0] + current_lens[1]
            
            up_diam[v] = max(d_excl, path_excl)
            
            dfs2(v, u)

    dfs2(0, -1)
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print(max_diameter_after_removal(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
