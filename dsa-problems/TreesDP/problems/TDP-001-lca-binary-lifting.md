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
    public void preprocess(int root, int n, int[][] edges) {
        // Implement here
    }

    public int lca(int u, int v) {
        // Implement here
        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
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
    }
}
```

### Python

```python
from typing import List

class Solution:
    def preprocess(self, root: int, n: int, edges: List[List[int]]) -> None:
        # Implement here
        pass

    def lca(self, u: int, v: int) -> int:
        # Implement here
        return -1

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        q = int(next(iterator))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        solution.preprocess(1, n, edges)

        for _ in range(q):
            u = int(next(iterator))
            v = int(next(iterator))
            print(solution.lca(u, v))
    except StopIteration:
        pass

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
public:
    void preprocess(int root, int n, const vector<vector<int>>& edges) {
        // Implement here
    }

    int lca(int u, int v) {
        // Implement here
        return -1;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    solution.preprocess(1, n, edges);

    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << solution.lca(u, v) << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  preprocess(root, n, edges) {
    // Implement here
  }

  lca(u, v) {
    // Implement here
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
}).on("close", () => {
  const tokens = lines
    .join(" ")
    .split(/\s+/)
    .filter((t) => t !== "");
  if (tokens.length === 0) return;

  let idx = 0;
  const n = parseInt(tokens[idx++]);
  const q = parseInt(tokens[idx++]);

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.preprocess(1, n, edges);

  for (let i = 0; i < q; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    process.stdout.write(solution.lca(u, v) + "\n");
  }
});
```
