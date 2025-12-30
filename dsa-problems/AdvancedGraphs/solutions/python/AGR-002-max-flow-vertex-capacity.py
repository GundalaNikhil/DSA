import sys

# Increase recursion depth for DFS
sys.setrecursionlimit(200000)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, capacity):
        # Forward edge: [v, capacity, flow, reverse_index]
        # Reverse edge: [u, 0, 0, forward_index]
        self.graph[u].append([v, capacity, 0, len(self.graph[v])])
        self.graph[v].append([u, 0, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, flow, rev in self.graph[u]:
                if cap - flow > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, pushed, ptr):
        if pushed == 0 or u == t:
            return pushed
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, flow, rev = self.graph[u][i]
            if self.level[v] != self.level[u] + 1 or cap - flow == 0:
                continue
            tr = self.dfs(v, t, min(pushed, cap - flow), ptr)
            if tr == 0:
                continue
            self.graph[u][i][2] += tr
            self.graph[v][rev][2] -= tr
            return tr
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                flow += pushed
        return flow

def max_flow_vertex_cap(n: int, s: int, t: int, cap: list[int], edges: list[tuple[int, int, int]]) -> int:
    dinic = Dinic(2 * n)
    INF = 10**15
    
    # Vertex capacities
    for i in range(n):
        c = INF if (cap[i] == -1 or i == s or i == t) else cap[i]
        dinic.add_edge(2 * i, 2 * i + 1, c)
        
    # Edges
    for u, v, c in edges:
        dinic.add_edge(2 * u + 1, 2 * v, c)
        
    return dinic.max_flow(2 * s, 2 * t + 1)

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
        cap = [int(next(iterator)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
        print(max_flow_vertex_cap(n, s, t, cap, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
