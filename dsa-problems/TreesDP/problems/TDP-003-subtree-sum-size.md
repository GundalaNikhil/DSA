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
    public void computeSubtreeMetrics(int n, int[] nodeValues, int[][] edges) {
        // Implement here
    }

    public long[] getSubtreeSums() {
        // Implement here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();

        int[] nodeValues = new int[n];
        for (int i = 0; i < n; i++) {
            nodeValues[i] = sc.nextInt();
        }

        int[][] edges = new int[n - 1][2];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        solution.computeSubtreeMetrics(n, nodeValues, edges);

        long[] sums = solution.getSubtreeSums();

        for (int i = 0; i < sums.length; i++) {
             System.out.println(sums[i]);
        }
    }
}
```

### Python

```python
from typing import List
import sys

sys.setrecursionlimit(200000)

class Solution:
    def compute_subtree_metrics(self, n: int, node_values: List[int], edges: List[List[int]]) -> None:
        # Implement here
        pass

    def get_subtree_sums(self) -> List[int]:
        # Implement here
        return []

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        node_values = []
        for _ in range(n):
            node_values.append(int(next(iterator)))

        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

        solution = Solution()
        solution.compute_subtree_metrics(n, node_values, edges)

        sums = solution.get_subtree_sums()
        for s in sums:
            print(s)
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
    void computeSubtreeMetrics(int n, const vector<int>& nodeValues, const vector<vector<int>>& edges) {
        // Implement here
    }

    vector<long long> getSubtreeSums() {
        // Implement here
        return {};
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;

    vector<int> nodeValues(n);
    for (int i = 0; i < n; i++) {
        cin >> nodeValues[i];
    }

    vector<vector<int>> edges(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    solution.computeSubtreeMetrics(n, nodeValues, edges);

    vector<long long> sums = solution.getSubtreeSums();
    for (long long s : sums) {
        cout << s << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  computeSubtreeMetrics(n, nodeValues, edges) {
    // Implement here
  }

  getSubtreeSums() {
    // Implement here
    return [];
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

  const nodeValues = [];
  for (let i = 0; i < n; i++) {
    nodeValues.push(parseInt(tokens[idx++]));
  }

  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(tokens[idx++]);
    const v = parseInt(tokens[idx++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  solution.computeSubtreeMetrics(n, nodeValues, edges);

  const sums = solution.getSubtreeSums();
  sums.forEach((s) => console.log(s));
});
```
