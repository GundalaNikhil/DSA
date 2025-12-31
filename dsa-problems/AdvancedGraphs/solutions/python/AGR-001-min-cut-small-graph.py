import sys

def min_cut(n: int, edges: list[tuple[int, int, int]]) -> int:
    adj = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        adj[u][v] += w
        adj[v][u] += w
        
    global_min_cut = float('inf')
    merged = [False] * n
    nodes_remaining = n
    
    while nodes_remaining > 1:
        # Minimum Cut Phase
        weights = [0] * n
        in_set = [False] * n
        prev = -1
        curr = -1
        
        # Add nodes one by one
        for _ in range(nodes_remaining):
            prev = curr
            curr = -1
            max_w = -1
            
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    if weights[i] > max_w:
                        max_w = weights[i]
                        curr = i
            
            in_set[curr] = True
            
            # Update weights
            for i in range(n):
                if not merged[i] and not in_set[i]:
                    weights[i] += adj[curr][i]
                    
        # Update global min cut
        # weights[curr] is the cut value of the phase
        global_min_cut = min(global_min_cut, weights[curr])
        
        # Merge curr (t) into prev (s)
        for i in range(n):
            if i != curr and i != prev and not merged[i]:
                adj[prev][i] += adj[curr][i]
                adj[i][prev] += adj[curr][i]
                
        merged[curr] = True
        nodes_remaining -= 1
        
    return global_min_cut if global_min_cut != float('inf') else 0

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
            w = int(next(iterator))
            edges.append((u, v, w))
        print(min_cut(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
