---
problem_id: TDP_SUBTREE_SUM_SIZE__3184
display_id: TDP-003
slug: subtree-sum-size
title: "Subtree Sum and Size"
difficulty: Easy
difficulty_score: 25
topics:
  - Tree DP
  - DFS
  - Subtree Queries
tags:
  - tree-traversal
  - aggregation
  - subtree-properties
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TDP-003: Subtree Sum and Size

## Problem Statement

You are given a rooted tree with `n` nodes numbered from 1 to n, where node 1 is the root. Each node has an integer value associated with it.

For each node, compute the **subtree sum**, which is the sum of values of all nodes in the subtree rooted at that node (including the node itself).

Output the subtree sum for each node from 1 to n.

![Problem Illustration](../images/TDP-003/problem-illustration.png)

## Input Format

- First line: Single integer `n` (number of nodes)
- Second line: `n` space-separated integers representing node values (value[1], value[2], ..., value[n])
- Next `n-1` lines: Two integers `u` and `v` representing an edge between nodes u and v

## Output Format

`n` lines, where the i-th line contains the subtree sum for node i.

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `-10^9 ≤ value[i] ≤ 10^9`
- `1 ≤ u, v ≤ n`
- The given edges form a valid tree

## Example

**Input:**

```
3
1 2 3
1 2
1 3
```

**Output:**

```
6
2
3
```

**Explanation:**

Tree structure:

```
    1 (value=1)
   / \
  2   3
(v=2) (v=3)
```

- Node 1's subtree: {1, 2, 3}, sum = 1 + 2 + 3 = 6
- Node 2's subtree: {2}, sum = 2
- Node 3's subtree: {3}, sum = 3

![Example Visualization](../images/TDP-003/example-1.png)

## Notes

- Use DFS to traverse the tree and compute subtree sums bottom-up
- Be careful with integer overflow - use long/long long for sums
- The subtree of a leaf node contains only itself
- Root node's subtree sum equals the sum of all node values

## Related Topics

Tree DP, DFS, Aggregation, Bottom-Up DP

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private List<Integer>[] tree;
    private int[] values;
    private int[] subtreeSize;
    private long[] subtreeSum;

    public void computeSubtreeMetrics(int n, int[] nodeValues, int[][] edges) {
        // Your implementation here
    }

    private void dfs(int node, int parent) {
        // Your implementation here
    }

    public long[] getSubtreeSums() {
        return subtreeSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.computeSubtreeMetrics(n, values, edges);

        long[] sums = solution.getSubtreeSums();
        for (int i = 1; i <= n; i++) {
            System.out.println(sums[i]);
        }

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
        self.tree = []
        self.values = []
        self.subtree_size = []
        self.subtree_sum = []

    def compute_subtree_metrics(self, n: int, node_values: List[int], edges: List[List[int]]) -> None:
        # Your implementation here
        pass

    def dfs(self, node: int, parent: int) -> None:
        # Your implementation here
        pass

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
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    vector<vector<int>> tree;
    vector<long long> values;
    vector<int> subtreeSize;
    vector<long long> subtreeSum;

    void dfs(int node, int parent) {
        // Your implementation here
    }

public:
    void computeSubtreeMetrics(int n, vector<long long>& nodeValues, vector<pair<int, int>>& edges) {
        // Your implementation here
    }

    vector<long long> getSubtreeSums() {
        return vector<long long>(subtreeSum.begin() + 1, subtreeSum.end());
    }
};

int main() {
    int n;
    cin >> n;

    vector<long long> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    vector<pair<int, int>> edges;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    solution.computeSubtreeMetrics(n, values, edges);

    vector<long long> sums = solution.getSubtreeSums();
    for (long long s : sums) {
        cout << s << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  constructor() {
    this.tree = [];
    this.values = [];
    this.subtreeSize = [];
    this.subtreeSum = [];
  }

  computeSubtreeMetrics(n, nodeValues, edges) {
    // Your implementation here
  }

  dfs(node, parent) {
    // Your implementation here
  }

  getSubtreeSums() {
    return this.subtreeSum.slice(1);
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
  const values = lines[1].split(" ").map(Number);

  const edges = [];
  for (let i = 2; i < n + 1; i++) {
    const [u, v] = lines[i].split(" ").map(Number);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.computeSubtreeMetrics(n, values, edges);

  const sums = solution.getSubtreeSums();
  sums.forEach((s) => console.log(s));
});
```
