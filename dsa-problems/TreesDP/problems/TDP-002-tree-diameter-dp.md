---
problem_id: TDP_TREE_DIAMETER_DP__4829
display_id: TDP-002
slug: tree-diameter-dp
title: "Tree Diameter DP"
difficulty: Medium
difficulty_score: 40
topics:
  - Tree DP
  - DFS
  - Tree Diameter
tags:
  - tree-properties
  - dfs
  - longest-path
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TDP-002: Tree Diameter DP

## Problem Statement

You are given a tree with `n` nodes numbered from 1 to n. The tree is represented by `n-1` edges, where each edge connects two nodes.

Find the **diameter** of the tree, which is defined as the length of the longest path between any two nodes in the tree. The length of a path is the number of edges in the path.

![Problem Illustration](../images/TDP-002/problem-illustration.png)

## Input Format

- First line: Single integer `n` (number of nodes)
- Next `n-1` lines: Two integers `u` and `v` representing an edge between nodes u and v

## Output Format

A single integer representing the diameter of the tree (length of the longest path).

## Constraints

- `2 ≤ n ≤ 2 × 10^5`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree (connected, acyclic)
- All edge lengths are 1

## Example

**Input:**

```
4
1 2
2 3
3 4
```

**Output:**

```
3
```

**Explanation:**

The tree is a straight line: 1 - 2 - 3 - 4

The longest path is from node 1 to node 4 (or 4 to 1), which has length 3 (passing through edges 1-2, 2-3, 3-4).

Alternatively, we can visualize all paths:

- 1 to 2: length 1
- 1 to 3: length 2
- 1 to 4: length 3 ✓ (maximum)
- 2 to 3: length 1
- 2 to 4: length 2
- 3 to 4: length 1

The diameter is 3.

![Example Visualization](../images/TDP-002/example-1.png)

## Notes

- Use DFS-based dynamic programming to solve in O(n) time
- For each node, track the two deepest paths in its subtree
- The diameter is the maximum sum of two deepest paths across all nodes
- Alternative approach: Run BFS twice (from any node to farthest, then from that node to farthest)

## Related Topics

Tree DP, DFS, Graph Theory, Longest Path

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private List<Integer>[] tree;
    private int diameter = 0;

    public int treeDiameter(int n, int[][] edges) {
        return 0;
    }

    private int dfs(int node, int parent) {
        int max1 = 0, max2 = 0;

        for (int child : tree[node]) {
            if (child == parent) continue;

            int childDepth = dfs(child, node);

            if (childDepth > max1) {
                max2 = max1;
                max1 = childDepth;
            } else if (childDepth > max2) {
                max2 = childDepth;
            }
        }

        diameter = Math.max(diameter, max1 + max2);
        return max1 + 1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.treeDiameter(n, edges);

        System.out.println(result);
        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys
sys.setrecursionlimit(300000)

class Solution:
    def __init__(self):
        return 0
    def tree_diameter(self, n: int, edges: List[List[int]]) -> int:
        return 0
    def dfs(self, node: int, parent: int) -> int:
        return 0
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
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<vector<int>> tree;
    int diameter;

    int dfs(int node, int parent) {
        return 0;
    }

public:
    int treeDiameter(int n, vector<pair<int, int>>& edges) {
        return 0;
    }
};

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> edges;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    int result = solution.treeDiameter(n, edges);

    cout << result << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    this.tree = [];
    this.diameter = 0;
  }

  treeDiameter(n, edges) {
    return 0;
  }

  dfs(node, parent) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  const n = parseInt(lines[0]);

  const edges = [];
  for (let i = 1; i < n; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.treeDiameter(n, edges);

  console.log(result);
});
```

