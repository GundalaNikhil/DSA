import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.history = []

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.history.append((root_j, root_i))
            return True
        return False

    def rollback(self):
        child, parent = self.history.pop()
        self.parent[child] = child
        self.size[parent] -= self.size[child]

def offline_lca(n: int, edges: list[tuple[int, int]], ops: list[tuple[str, int, int]]) -> list[int]:
    # 1. LCA Precalc
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    LOG = 20
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    def dfs(u, p, d):
        depth[u] = d
        up[u][0] = p
        for i in range(1, LOG):
            if up[u][i-1] != -1:
                up[u][i] = up[up[u][i-1]][i-1]
            else:
                up[u][i] = -1
        for v in adj[u]:
            if v != p:
                dfs(v, u, d + 1)

    dfs(0, -1, 0)

    def get_lca(u, v):
        if depth[u] < depth[v]: u, v = v, u
        for i in range(LOG - 1, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        if u == v: return u
        for i in range(LOG - 1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]

    # 2. Intervals
    edge_start = {}
    for u, v in edges:
        if u > v: u, v = v, u
        edge_start[(u, v)] = 0

    q = len(ops)
    intervals = []
    queries = []

    for i, (t, u, v) in enumerate(ops):
        if u > v: u, v = v, u
        if t == "cut":
            if (u, v) in edge_start:
                start = edge_start.pop((u, v))
                intervals.append((start, i, u, v))
        elif t == "link":
            edge_start[(u, v)] = i + 1
        else: # query
            queries.append((i, u, v)) # u, v can be swapped, but for LCA/DSU it's fine

    for (u, v), start in edge_start.items():
        intervals.append((start, q, u, v))

    # 3. Segment Tree
    seg = [[] for _ in range(4 * (q + 1))]

    def add_range(node, start, end, l, r, u, v):
        if r < start or end < l: return
        if l <= start and end <= r:
            seg[node].append((u, v))
            return
        mid = (start + end) // 2
        add_range(node * 2, start, mid, l, r, u, v)
        add_range(node * 2 + 1, mid + 1, end, l, r, u, v)

    for l, r, u, v in intervals:
        if l <= r:
            add_range(1, 0, q, l, r, u, v)

    # 4. Solve
    dsu = DSU(n)
    results = {}
    query_map = {t: (u, v) for t, u, v in queries}

    def solve(node, start, end):
        ops_count = 0
        for u, v in seg[node]:
            if dsu.union(u, v):
                ops_count += 1

        if start == end:
            if start in query_map:
                u, v = query_map[start]
                if dsu.find(u) == dsu.find(v):
                    # Use original u, v for LCA? Yes, order doesn't matter
                    results[start] = get_lca(u, v)
                else:
                    results[start] = -1
        else:
            mid = (start + end) // 2
            solve(node * 2, start, mid)
            solve(node * 2 + 1, mid + 1, end)

        for _ in range(ops_count):
            dsu.rollback()

    solve(1, 0, q)

    final_out = []
    for t, _, _ in queries:
        final_out.append(results[t])
    return final_out

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    iterator = iter(data)
    try:
        n = int(next(iterator))
        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))

        q = int(next(iterator))
        ops = []
        for _ in range(q):
            t = next(iterator)
            u = int(next(iterator))
            v = int(next(iterator))
            ops.append((t, u, v))

        out = offline_lca(n, edges, ops)
        sys.stdout.write("\n".join(map(str, out)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
