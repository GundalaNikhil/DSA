import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def euler_trail(n: int, edges: list[tuple[int, int]]):
    m = len(edges)
    if m == 0:
        return [0]
        
    in_deg = [0] * n
    out_deg = [0] * n
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        out_deg[u] += 1
        in_deg[v] += 1
        adj[u].append(v)
        
    start_node = -1
    end_node = -1
    diff_count = 0
    
    for i in range(n):
        if out_deg[i] == in_deg[i] + 1:
            if start_node != -1: return None
            start_node = i
            diff_count += 1
        elif in_deg[i] == out_deg[i] + 1:
            if end_node != -1: return None
            end_node = i
            diff_count += 1
        elif in_deg[i] != out_deg[i]:
            return None
            
    if diff_count == 0:
        for i in range(n):
            if out_deg[i] > 0:
                start_node = i
                break
    elif diff_count != 2:
        return None
        
    if start_node == -1: return None
    
    trail = []
    
    def dfs(u):
        while adj[u]:
            v = adj[u].pop()
            dfs(v)
        trail.append(u)
        
    dfs(start_node)
    
    if len(trail) != m + 1:
        return None
        
    return trail[::-1]

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
            edges.append((u, v))
            
        trail = euler_trail(n, edges)
        if trail is None:
            sys.stdout.write("NO")
        else:
            sys.stdout.write("YES\n" + " ".join(map(str, trail)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
