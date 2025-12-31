
def has_deadlock(n: int, edges: list[tuple[int, int]]) -> bool:
    # Nodes 1..n
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
        
    queue = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            
    processed_count = 0
    while queue:
        u = queue.pop(0)
        processed_count += 1
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    return processed_count != n

def main():
    import sys
    # Use generator pattern for robust reading
    def input_gen():
        for line in sys.stdin:
            for token in line.split():
                yield token
    it = input_gen()
    
    try:
        n = int(next(it))
        m = int(next(it))
        edges = []
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            edges.append((u, v))
        
        if has_deadlock(n, edges):
            print("DEADLOCK")
        else:
            print("NO DEADLOCK")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
