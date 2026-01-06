import sys


class RollbackDSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.history = []

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
            return i

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
                self.history.append((root_j, root_i))
                self.parent[root_j] = root_i
                self.size[root_i] += self.size[root_j]
                return True
            return False

    def rollback(self, target_len):
        while len(self.history) > target_len:
            curr, par = self.history.pop()
            self.size[par] -= self.size[curr]
            self.parent[curr] = curr


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    edge_intervals = {}
    queries = []
    tree_edges = [[] for _ in range(4 * q + 1)]
    for t in range(q):
        op = input_data[ptr]
        ptr += 1
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        if u > v:
            u, v = v, u
            if op == "ADD":
                edge_intervals[(u, v)] = t
                queries.append(("ADD", u, v))
            elif op == "REM":
                start = edge_intervals.pop((u, v))


def add_to_tree(node, l, r, ql, qr, edge):
    if ql <= l and r <= qr:
        tree_edges[node].append(edge)
        return
    mid = (l + r) // 2
    if ql <= mid:
        add_to_tree(2 * node, l, mid, ql, qr, edge)
        if qr > mid:
            add_to_tree(2 * node + 1, mid + 1, r, ql, qr, edge)
            stack = [(1, 0, q - 1)]
            while stack:
                node, l, r = stack.pop()
                if start <= l and r <= t:
                    tree_edges[node].append((u, v))
                else:
                    mid = (l + r) // 2
                    if start <= mid:
                        stack.append((2 * node, l, mid))
                        if t > mid:
                            stack.append((2 * node + 1, mid + 1, r))
                            queries.append(("REM", u, v))
                        else:
                            queries.append(("ASK", u, v))
                            for (u, v), start in edge_intervals.items():
                                stack = [(1, 0, q - 1)]
                                while stack:
                                    node, l, r = stack.pop()
                                    if start <= l and r <= q - 1:
                                        tree_edges[node].append((u, v))
                                    else:
                                        mid = (l + r) // 2
                                        if start <= mid:
                                            stack.append((2 * node, l, mid))
                                            if q - 1 > mid:
                                                stack.append((2 * node + 1, mid + 1, r))
                                                dsu = RollbackDSU(n)
                                                ans = [None] * q


def traverse(node, l, r):
    prev_len = len(dsu.history)
    for u, v in tree_edges[node]:
        dsu.union(u, v)
        if l == r:
            if queries[l][0] == "ASK":
                u, v = queries[l][1], queries[l][2]
                ans[l] = "YES" if dsu.find(u) == dsu.find(v) else "NO"
            else:
                mid = (l + r) // 2
                traverse(2 * node, l, mid)
                traverse(2 * node + 1, mid + 1, r)
                dsu.rollback(prev_len)
                traverse(1, 0, q - 1)
                for x in ans:
                    if x:
                        print(x)


if __name__ == "__main__":
    solve()
