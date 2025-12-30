import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    q = int(data[idx]); idx += 1
    marked = {}
    results = []

    def bfs(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    queue.append(v)
        min_cost = float('inf')
        for node, val in marked.items():
            if dist[node] != float('inf'):
                min_cost = min(min_cost, dist[node] + val)
        return min_cost

    for _ in range(q):
        qtype = int(data[idx]); idx += 1
        if qtype == 1:
            v = int(data[idx]); idx += 1
            val = int(data[idx]); idx += 1
            t = int(data[idx]); idx += 1
            marked[v] = val
        else:
            v = int(data[idx]); idx += 1
            t = int(data[idx]); idx += 1
            results.append(str(bfs(v)))

    print('\n'.join(results))

if __name__ == "__main__":
    main()
