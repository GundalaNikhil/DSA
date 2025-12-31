import sys

sys.setrecursionlimit(200000)

def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> int:
    """
    A node is critical if removing it creates components where at least one 
    has only red edges and at least one has only blue edges.
    """
    if not edges:
        return 0
    
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append((v, c))
        adj[v].append((u, c))
    
    critical_count = 0
    
    for remove_node in range(n):
        temp_adj = [[] for _ in range(n)]
        for u, v, c in edges:
            if u != remove_node and v != remove_node:
                temp_adj[u].append((v, c))
                temp_adj[v].append((u, c))
        
        visited = [False] * n
        visited[remove_node] = True
        components = []
        
        for start in range(n):
            if not visited[start]:
                component_nodes = set()
                queue = [start]
                visited[start] = True
                
                while queue:
                    u = queue.pop(0)
                    component_nodes.add(u)
                    for v, c in temp_adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)
                
                has_red = has_blue = False
                for u in component_nodes:
                    for v, c in temp_adj[u]:
                        if v in component_nodes:
                            if c == 0:
                                has_red = True
                            else:
                                has_blue = True
                
                if has_red or has_blue:
                    components.append((has_red, has_blue))
        
        has_red_only = any(r and not b for r, b in components)
        has_blue_only = any(b and not r for r, b in components)
        
        if has_red_only and has_blue_only:
            critical_count += 1
    
    return critical_count

def main():
    input = sys.stdin.read
    data = input().split()
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
        print(ans)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
