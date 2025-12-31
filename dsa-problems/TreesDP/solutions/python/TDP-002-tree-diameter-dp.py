from typing import List
import sys
sys.setrecursionlimit(300000)

class Solution:
    def __init__(self):
        self.tree = []
        self.diameter = 0

    def tree_diameter(self, n: int, edges: List[List[int]]) -> int:
        self.tree = [[] for _ in range(n + 1)]
        self.diameter = 0

        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        self.dfs(1, -1)
        return self.diameter

    def dfs(self, node: int, parent: int) -> int:
        max1, max2 = 0, 0

        for child in self.tree[node]:
            if child == parent:
                continue

            child_depth = self.dfs(child, node)

            if child_depth > max1:
                max2 = max1
                max1 = child_depth
            elif child_depth > max2:
                max2 = child_depth

        self.diameter = max(self.diameter, max1 + max2)
        return max1 + 1

def main():
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])

    edges = []
    for i in range(1, n):
        u, v = map(int, lines[i].split())
        edges.append([u, v])

    solution = Solution()
    result = solution.tree_diameter(n, edges)
    print(result)

if __name__ == "__main__":
    main()
