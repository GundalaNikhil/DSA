from typing import List

def find_articulation_points(n: int, adj: List[List[int]]) -> List[int]:
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    ap = set()
    time = [0]
    
    def dfs(u):
        children = 0
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in adj[u]:
            if disc[v] == -1:
                children += 1
                parent[v] = u
                dfs(v)
                
                low[u] = min(low[u], low[v])
                
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap.add(u)
            
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
        
        if parent[u] == -1 and children > 1:
            ap.add(u)
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    
    return list(ap)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
