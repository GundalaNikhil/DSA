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
    private int LOG = 20;
    private List<Integer>[] tree;
    private int[][] up;
    private int[] depth;
    private int n;

    public void preprocess(int root, int n, int[][] edges) {
        // Your implementation here
    }

    public int lca(int u, int v) {
        // Your implementation here
        return -1;
    }
}

public class Main {
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
        self.LOG = 20
        self.tree = []
        self.up = []
        self.depth = []
        self.n = 0

    def preprocess(self, root: int, n: int, edges: List[List[int]]) -> None:
        # Your implementation here
        pass

    def lca(self, u: int, v: int) -> int:
        # Your implementation here
        return -1

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

class Solution {
private:
    static const int LOG = 20;
    vector<vector<int>> tree;
    int up[200005][LOG];
    int depth[200005];
    int n;

public:
    void preprocess(int root, int n, vector<pair<int, int>>& edges) {
        // Your implementation here
    }

    int lca(int u, int v) {
        // Your implementation here
        return -1;
    }
};

int main() {
    int n, q;
    cin >> n >> q;

    vector<pair<int, int>> edges;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    solution.preprocess(1, n, edges);

    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << solution.lca(u, v) << endl;
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
    // Your implementation here
  }

  lca(u, v) {
    // Your implementation here
    return -1;
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
