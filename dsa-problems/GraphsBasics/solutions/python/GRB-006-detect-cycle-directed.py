import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def has_cycle(n: int, adj: list[list[int]]) -> bool:
    state = [0] * n # 0: unvisited, 1: visiting, 2: visited
    
    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1:
                return True
            if state[v] == 0:
                if dfs(v):
                    return True
        state[u] = 2
        return False

    for i in range(n):
        if state[i] == 0:
            if dfs(i):
                return True
                
    return False

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            
        print("true" if has_cycle(n, adj) else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
