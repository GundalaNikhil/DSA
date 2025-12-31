from typing import List
import sys

class Solution:
    def __init__(self):
        self.LOG = 20
        self.tree = []
        self.up = []
        self.depth = []
        self.n = 0

    def preprocess(self, root: int, n: int, edges: List[List[int]]) -> None:
        self.n = n
        self.tree = [[] for _ in range(n + 1)]
        self.up = [[-1] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)

        # Build adjacency list
        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        # DFS to compute depths and immediate parents
        self._dfs(root, -1, 0)

        # Binary lifting preprocessing
        for j in range(1, self.LOG):
            for i in range(1, n + 1):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    def _dfs(self, node: int, parent: int, d: int) -> None:
        self.up[node][0] = parent
        self.depth[node] = d
        for child in self.tree[node]:
            if child != parent:
                self._dfs(child, node, d + 1)

    def lca(self, u: int, v: int) -> int:
        # Make u deeper
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # Lift u to same level as v
        diff = self.depth[u] - self.depth[v]
        for j in range(self.LOG):
            if (diff >> j) & 1:
                u = self.up[u][j]

        if u == v:
            return u

        # Lift both simultaneously
        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != -1 and self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        return self.up[u][0]

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    n, q = map(int, input_lines[0].split())

    edges = []
    for i in range(1, n):
        u, v = map(int, input_lines[i].split())
        edges.append([u, v])

    solution = Solution()
    solution.preprocess(1, n, edges)

    results = []
    for i in range(n, n + q):
        u, v = map(int, input_lines[i].split())
        results.append(str(solution.lca(u, v)))

    print('\n'.join(results))

if __name__ == "__main__":
    main()
