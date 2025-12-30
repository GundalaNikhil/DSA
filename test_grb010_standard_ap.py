import sys

sys.setrecursionlimit(200000)

def count_articulation_points(n: int, edges: list[tuple[int, int, int]]) -> int:
    """
    Find articulation points (standard algorithm, ignoring colors for now)
    """
    if not edges:
        return 0
    
    adj = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    timer = [0]
    articulation_points = set()
    
    def dfs(u):
        children = 0
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        
        for v in adj[u]:
            if disc[v] == -1:  # Tree edge
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])
                
                # Check articulation point condition
                if parent[u] == -1 and children > 1:
                    # Root with multiple children
                    articulation_points.add(u)
                elif parent[u] != -1 and low[v] >= disc[u]:
                    # Non-root articulation point
                    articulation_points.add(u)
            
            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    
    return len(articulation_points)

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
        
        ans = count_articulation_points(n, edges)
        print(ans)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
