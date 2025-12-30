from typing import List
import sys
sys.setrecursionlimit(300000)

class Solution:
    def __init__(self):
        self.tree = []
        self.values = []
        self.subtree_size = []
        self.subtree_sum = []

    def compute_subtree_metrics(self, n: int, node_values: List[int], edges: List[List[int]]) -> None:
        self.tree = [[] for _ in range(n + 1)]
        self.values = [0] + node_values
        self.subtree_size = [0] * (n + 1)
        self.subtree_sum = [0] * (n + 1)

        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        self.dfs(1, -1)

    def dfs(self, node: int, parent: int) -> None:
        self.subtree_size[node] = 1
        self.subtree_sum[node] = self.values[node]

        for child in self.tree[node]:
            if child == parent:
                continue

            self.dfs(child, node)
            self.subtree_size[node] += self.subtree_size[child]
            self.subtree_sum[node] += self.subtree_sum[child]

    def get_subtree_sums(self) -> List[int]:
        return self.subtree_sum[1:]

def main():
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    values = list(map(int, lines[1].split()))

    edges = []
    for i in range(2, n + 1):
        u, v = map(int, lines[i].split())
        edges.append([u, v])

    solution = Solution()
    solution.compute_subtree_metrics(n, values, edges)

    sums = solution.get_subtree_sums()
    for s in sums:
        print(s)

if __name__ == "__main__":
    main()
