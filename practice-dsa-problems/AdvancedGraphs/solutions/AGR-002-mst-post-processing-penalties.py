import sys


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.num_sets -= 1
            return True
        return False


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    edges = []
    for _ in range(m):
        u = int(input_data[ptr])
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        w = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        edges.append((w, p, u, v))
        edges.sort()
        dsu = DSU(n)
        total_cost = 0
        edges_used = 0
        for w, p, u, v in edges:
            if dsu.union(u, v):
                total_cost += w + p
                edges_used += 1
                if edges_used < n - 1:
                    print("-1")
                else:
                    print(total_cost)


if __name__ == "__main__":
    solve()
