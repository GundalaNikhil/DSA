import sys
from collections import deque

def has_deadlock(n: int, edges: list[list[int]]) -> bool:
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
        
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            
    processed_count = 0
    while queue:
        u = queue.popleft()
        processed_count += 1
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    # If processed_count < n, there is a cycle (deadlock)
    return processed_count < n

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
            edges.append([u, v])
            
        print("true" if has_deadlock(n, edges) else "false")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
