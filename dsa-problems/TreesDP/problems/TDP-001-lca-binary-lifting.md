---
problem_id: TDP_LCA_BINARY_LIFTING__7291
display_id: TDP-001
slug: lca-binary-lifting
title: "Lowest Common Ancestor (Binary Lifting)"
difficulty: Medium
difficulty_score: 45
topics:
  - Tree DP
  - Binary Lifting
  - LCA
tags:
  - preprocessing
  - tree-traversal
  - ancestors
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TDP-001: Lowest Common Ancestor (Binary Lifting)

## Problem Statement

You are given a rooted tree with `n` nodes numbered from 1 to n. Node 1 is the root. The tree is represented by `n-1` edges, where each edge connects two nodes.

You need to preprocess the tree and then answer `q` queries. Each query asks for the Lowest Common Ancestor (LCA) of two nodes `u` and `v`.

The Lowest Common Ancestor of two nodes is the deepest (farthest from root) node that is an ancestor of both nodes.

![Problem Illustration](../images/TDP-001/problem-illustration.png)

## Input Format

- First line: Two integers `n` and `q` (number of nodes and number of queries)
- Next `n-1` lines: Two integers `u` and `v` representing an edge between nodes u and v
- Next `q` lines: Two integers `u` and `v` representing a query for LCA(u, v)

## Output Format

For each query, output a single integer representing the LCA of the two given nodes.

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `1 ≤ q ≤ 2 × 10^5`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree
- All queries are independent

## Example

**Input:**

```
7 3
1 2
1 3
2 4
2 5
3 6
3 7
4 5
2 3
6 7
```

**Output:**

```
2
1
3
```

**Explanation:**

The tree structure:

```
       1
      / \
     2   3
    / \ / \
   4  5 6  7
```

Query 1: LCA(4, 5) = 2 (node 2 is the parent of both 4 and 5)
Query 2: LCA(2, 3) = 1 (node 1 is the parent of both 2 and 3)
Query 3: LCA(6, 7) = 3 (node 3 is the parent of both 6 and 7)

![Example Visualization](../images/TDP-001/example-1.png)

## Notes

- Use binary lifting to achieve O(log n) time complexity per query
- Preprocess the tree in O(n log n) time
- The root node (node 1) is its own ancestor
- If one node is an ancestor of another, the LCA is the ancestor node itself

## Related Topics

Tree DP, Binary Search, Preprocessing, Graph Traversal

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private int LOG = 20; // log2(200000) ≈ 18
    private List<Integer>[] tree;
    private int[][] up;
    private int[] depth;
    private int n;

    public void preprocess(int root, int n, int[][] edges) {
    }

    private void dfs(int node, int parent, int d) {
        up[node][0] = parent;
        depth[node] = d;
        for (int child : tree[node]) {
            if (child != parent) {
                dfs(child, node, d + 1);
            }
        }
    }

    public int lca(int u, int v) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.preprocess(1, n, edges);

        for (int i = 0; i < q; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            System.out.println(solution.lca(u, v));
        }

        sc.close();
    }
}
```

### Python

```python
from typing import List
import sys

class Solution:
    def __init__(self):
        return 0
    def preprocess(self, root: int, n: int, edges: List[List[int]]) -> None:
        pass
    def _dfs(self, node: int, parent: int, d: int) -> None:
        pass
    def lca(self, u: int, v: int) -> int:
        return 0
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
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MAXN = 100005;
const int LOG = 20;

int up[MAXN][LOG];
int depth[MAXN];
vector<int> tree[MAXN];

void dfs(int node, int parent, int d) {
    up[node][0] = parent;
    depth[node] = d;
    for (int child : tree[node]) {
        if (child != parent) {
            dfs(child, node, d + 1);
        }
    }
}

void preprocess(int root, int n) {
    memset(up, -1, sizeof(up));
    memset(depth, 0, sizeof(depth));
    
    // DFS to compute depths and immediate parents
    dfs(root, -1, 0);
    
    // Binary lifting preprocessing
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= n; i++) {
            if (up[i][j - 1] != -1) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }
    }
}

int lca(int u, int v) {
    // Make u deeper
    if (depth[u] < depth[v]) {
        swap(u, v);
    }
    
    // Lift u to same level as v
    int diff = depth[u] - depth[v];
    for (int j = 0; j < LOG; j++) {
        if ((diff >> j) & 1) {
            u = up[u][j];
        }
    }
    
    if (u == v) return u;
    
    // Lift both simultaneously
    for (int j = LOG - 1; j >= 0; j--) {
        if (up[u][j] != -1 && up[u][j] != up[v][j]) {
            u = up[u][j];
            v = up[v][j];
        }
    }
    
    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
    
    preprocess(1, n);
    
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << "\n";
    }
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    this.LOG = 20;
    this.tree = [];
    this.up = [];
    this.depth = [];
    this.n = 0;
  }

  preprocess(root, n, edges) {
    return 0;
  }

  dfs(node, parent, d) {
    return 0;
  }

  lca(u, v) {
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
  const [n, q] = lines[0].split(" ").map(Number);

  const edges = [];
  for (let i = 1; i < n; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.preprocess(1, n, edges);

  const results = [];
  for (let i = n; i < n + q; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    results.push(solution.lca(u, v));
  }

  console.log(results.join("\n"));
});
```

