import sys

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.history = []

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.rank[root_i] += self.rank[root_j]
            self.history.append((root_j, root_i))
            return True
        else:
            self.history.append((-1, -1))
            return False

    def rollback(self):
        child, parent_node = self.history.pop()
        if child != -1:
            self.parent[child] = child
            self.rank[parent_node] -= self.rank[child]

    def connected(self, i, j):
        return self.find(i) == self.find(j)

class Solution:
    def process(self, n: int, events: list[list[str]]) -> list[str]:
        m = len(events)
        tree = [[] for _ in range(4 * m)]
        queries = [None] * m
        active_edges = {}
        
        for i, ev in enumerate(events):
            type, u, v = ev[0], int(ev[1]), int(ev[2])
            if u > v: u, v = v, u
            key = (u, v)
            
            if type == "ADD":
                active_edges[key] = i
            elif type == "REMOVE":
                if key in active_edges:
                    start = active_edges.pop(key)
                    self.add_edge(tree, 0, 0, m - 1, start, i - 1, (u, v))
            else:
                queries[i] = (u, v)
                
        for key, start in active_edges.items():
            self.add_edge(tree, 0, 0, m - 1, start, m - 1, key)
            
        dsu = DSU(n)
        results = []
        self.dfs(tree, 0, 0, m - 1, dsu, queries, results)
        return results

    def add_edge(self, tree, node, start, end, l, r, edge):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            tree[node].append(edge)
            return
        mid = (start + end) // 2
        self.add_edge(tree, 2 * node + 1, start, mid, l, r, edge)
        self.add_edge(tree, 2 * node + 2, mid + 1, end, l, r, edge)

    def dfs(self, tree, node, start, end, dsu, queries, results):
        ops = 0
        for u, v in tree[node]:
            dsu.union(u, v)
            ops += 1
            
        if start == end:
            if queries[start]:
                u, v = queries[start]
                results.append("true" if dsu.connected(u, v) else "false")
        else:
            mid = (start + end) // 2
            self.dfs(tree, 2 * node + 1, start, mid, dsu, queries, results)
            self.dfs(tree, 2 * node + 2, mid + 1, end, dsu, queries, results)
            
        for _ in range(ops):
            dsu.rollback()

def main():
    import sys
    sys.setrecursionlimit(500000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    events = []
    for _ in range(m):
        type = next(it)
        events.append([type, next(it), next(it)])
    
    sol = Solution()
    results = sol.process(n, events)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
