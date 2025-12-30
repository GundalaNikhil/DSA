import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t, delta):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, rev in self.graph[u]:
                if cap >= delta and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, flow, ptr, delta):
        if u == t or flow == 0:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap >= delta:
                pushed = self.dfs(v, t, min(flow, cap), ptr, delta)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_cap = 0
        for u in range(self.n):
            for v, cap, rev in self.graph[u]:
                max_cap = max(max_cap, cap)
        
        delta = 1
        while delta * 2 <= max_cap:
            delta *= 2
            
        max_f = 0
        while delta >= 1:
            while self.bfs(s, t, delta):
                ptr = [0] * self.n
                while True:
                    pushed = self.dfs(s, t, float('inf'), ptr, delta)
                    if pushed == 0:
                        break
                    max_f += pushed
            delta //= 2
        return max_f

def max_flow(n: int, s: int, t: int, edges: list[tuple[int, int, int]]) -> int:
    dinic = Dinic(n)
    for u, v, c in edges:
        dinic.add_edge(u, v, c)
    return dinic.max_flow(s, t)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
            
        print(max_flow(n, s, t, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
