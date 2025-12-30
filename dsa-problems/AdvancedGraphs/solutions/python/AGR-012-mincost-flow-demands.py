import sys
import heapq

# Increase recursion depth
sys.setrecursionlimit(300000)

class MinCostMaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.h = [0] * n
        self.INF = 10**18

    def add_edge(self, u, v, cap, cost):
        # [to, cap, cost, flow, rev]
        self.graph[u].append([v, cap, cost, 0, len(self.graph[v])])
        self.graph[v].append([u, 0, -cost, 0, len(self.graph[u]) - 1])

    def spfa(self, s):
        self.h = [self.INF] * self.n
        self.h[s] = 0
        in_queue = [False] * self.n
        queue = [s]
        in_queue[s] = True
        
        while queue:
            u = queue.pop(0)
            in_queue[u] = False
            for v, cap, cost, flow, rev in self.graph[u]:
                if cap - flow > 0 and self.h[v] > self.h[u] + cost:
                    self.h[v] = self.h[u] + cost
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True

    def dijkstra(self, s, t):
        dist = [self.INF] * self.n
        parent_node = [-1] * self.n
        parent_edge = [-1] * self.n
        dist[s] = 0
        pq = [(0, s)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for i, (v, cap, cost, flow, rev) in enumerate(self.graph[u]):
                reduced_cost = cost + self.h[u] - self.h[v]
                if cap - flow > 0 and dist[v] > dist[u] + reduced_cost:
                    dist[v] = dist[u] + reduced_cost
                    parent_node[v] = u
                    parent_edge[v] = i
                    heapq.heappush(pq, (dist[v], v))
                    
        return dist, parent_node, parent_edge

    def solve(self, s, t):
        flow = 0
        cost = 0
        
        # Initial potentials
        self.spfa(s)
        
        while True:
            dist, parent_node, parent_edge = self.dijkstra(s, t)
            if dist[t] == self.INF:
                break
                
            # Update potentials
            for i in range(self.n):
                if dist[i] != self.INF:
                    self.h[i] += dist[i]
                    
            push = self.INF
            curr = t
            while curr != s:
                p = parent_node[curr]
                idx = parent_edge[curr]
                edge = self.graph[p][idx]
                push = min(push, edge[1] - edge[3]) # cap - flow
                curr = p
                
            flow += push
            curr = t
            while curr != s:
                p = parent_node[curr]
                idx = parent_edge[curr]
                # Update flow
                self.graph[p][idx][3] += push
                rev_idx = self.graph[p][idx][4]
                self.graph[curr][rev_idx][3] -= push
                cost += push * self.graph[p][idx][2]
                curr = p
                
        return flow, cost

def min_cost_flow(n: int, b: list[int], edges: list[tuple[int, int, int, int, int]]):
    base_cost = 0
    supply = list(b)
    
    S = n
    T = n + 1
    mcmf = MinCostMaxFlow(n + 2)
    
    for u, v, low, high, cost in edges:
        if high < low: return None
        base_cost += low * cost
        supply[u] -= low
        supply[v] += low
        mcmf.add_edge(u, v, high - low, cost)
        
    total_supply = 0
    for i in range(n):
        if supply[i] > 0:
            mcmf.add_edge(S, i, supply[i], 0)
            total_supply += supply[i]
        elif supply[i] < 0:
            mcmf.add_edge(i, T, -supply[i], 0)
            
    flow, cost = mcmf.solve(S, T)
    
    if flow != total_supply:
        return None
        
    return base_cost + cost

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        b = [int(next(iterator)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            low = int(next(iterator))
            high = int(next(iterator))
            cost = int(next(iterator))
            edges.append((u, v, low, high, cost))
            
        ans = min_cost_flow(n, b, edges)
        if ans is None:
            sys.stdout.write("INFEASIBLE")
        else:
            sys.stdout.write("FEASIBLE\n" + str(ans))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
