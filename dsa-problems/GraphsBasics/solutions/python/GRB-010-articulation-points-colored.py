import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    """
    Brute-force approach: For each node, remove it and check if resulting
    components have the color separation property.
    """
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append((v, c))  # c=0 Red, 1 Blue
        adj[v].append((u, c))
        
    crit_nodes = []
    
    for i in range(n):
        # Remove node i
        visited = [False] * n
        visited[i] = True  # Mark removed node as visited
        
        comps = []
        
        for start_node in range(n):
            if not visited[start_node]:
                # BFS/DFS to find component
                has_red = False
                has_blue = False
                
                stack = [start_node]
                visited[start_node] = True
                
                while stack:
                    u = stack.pop()
                    for v, c in adj[u]:
                        if v == i:
                            continue  # Skip removed node
                        # Check edge (u, v) color
                        if c == 0:
                            has_red = True
                        else:
                            has_blue = True
                        
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                
                comps.append((has_red, has_blue))
                
        # Check condition: exists c1 with Red AND exists c2 with Blue (c1 != c2)
        has_r_comp = [idx for idx, (r, b) in enumerate(comps) if r]
        has_b_comp = [idx for idx, (r, b) in enumerate(comps) if b]
        
        is_crit = False
        if has_r_comp and has_b_comp:
            # Need distinct components
            if len(has_r_comp) > 1 or len(has_b_comp) > 1:
                is_crit = True
            elif has_r_comp[0] != has_b_comp[0]:
                is_crit = True
                
        if is_crit:
            crit_nodes.append(i)
            
    return crit_nodes

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c_str = next(iterator)
            edges.append((u, v, 0 if c_str == "R" else 1))
            
        ans = critical_nodes(n, edges)
        # Output count and node IDs
        print(len(ans))
        if ans:
            print(" ".join(map(str, ans)))
        else:
            print()  # Empty line if no critical nodes
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
