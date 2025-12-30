import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def euler_tour(n: int, adj: list[list[int]], root: int):
    tin = [0] * n
    tout = [0] * n
    timer = [0]  # Use list to make it mutable in nested function
    
    def dfs(u, p):
        tin[u] = timer[0]
        timer[0] += 1
        
        for v in adj[u]:
            if v != p:
                dfs(v, u)
                timer[0] += 1
                
        tout[u] = timer[0]
        
    dfs(root, -1)
    return tin, tout

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        root = int(next(iterator))
        
        tin, tout = euler_tour(n, adj, root)
        print(" ".join(map(str, tin)))
        print(" ".join(map(str, tout)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
