import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def critical_nodes(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    total_red = 0
    total_blue = 0
    
    for u, v, c in edges:
        adj[u].append((v, c))
        adj[v].append((u, c))
        if c == 0: total_red += 1
        else: total_blue += 1
        
    disc = [-1] * n
    low = [-1] * n
    sub_red = [0] * n
    sub_blue = [0] * n
    timer = 0
    critical = set()
    
    def dfs(u, p):
        nonlocal timer
        timer += 1
        disc[u] = low[u] = timer
        children = 0
        
        for v, c in adj[u]:
            if v == p:
                continue
            
            if disc[v] != -1:
                low[u] = min(low[u], disc[v])
                if disc[v] < disc[u]: # Back-edge
                    if c == 0: sub_red[u] += 1
                    else: sub_blue[u] += 1
            else:
                children += 1
                dfs(v, u)
                
                branch_red = sub_red[v] + (1 if c == 0 else 0)
                branch_blue = sub_blue[v] + (1 if c == 1 else 0)
                
                sub_red[u] += branch_red
                sub_blue[u] += branch_blue
                
                low[u] = min(low[u], low[v])
                
                if low[v] >= disc[u]:
                    # When u is removed, edge (u,v) is also removed.
                    # Component v has only internal edges (sub_red[v], sub_blue[v]).
                    v_red = sub_red[v]
                    v_blue = sub_blue[v]

                    # Rest of graph minus v's subtree and the edge (u,v)
                    rest_red = total_red - v_red - (1 if c == 0 else 0)
                    rest_blue = total_blue - v_blue - (1 if c == 1 else 0)

                    if (v_red > 0 and rest_blue > 0) or (v_blue > 0 and rest_red > 0):
                        critical.add(u)
                        
        if p == -1 and children < 2:
            if u in critical: critical.remove(u)

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
            
    return sorted(list(critical))

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
        print(len(ans))
        print(" ".join(map(str, ans)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
