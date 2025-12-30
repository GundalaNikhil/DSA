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

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, flow, ptr):
        if u == t or flow == 0:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f

def min_vertex_cover_cost(nU: int, nV: int, wU: list[int], wV: list[int], edges: list[tuple[int, int]]) -> int:
    S = 0
    T = nU + nV + 1
    dinic = Dinic(T + 1)
    INF = 10**18
    
    for i, w in enumerate(wU):
        dinic.add_edge(S, i + 1, w)
        
    for i, w in enumerate(wV):
        dinic.add_edge(nU + 1 + i, T, w)
        
    for u, v in edges:
        dinic.add_edge(u + 1, nU + 1 + v, INF)
        
    return dinic.max_flow(S, T)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        nU = int(next(iterator))
        nV = int(next(iterator))
        m = int(next(iterator))
        wU = [int(next(iterator)) for _ in range(nU)]
        wV = [int(next(iterator)) for _ in range(nV)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print(min_vertex_cover_cost(nU, nV, wU, wV, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
