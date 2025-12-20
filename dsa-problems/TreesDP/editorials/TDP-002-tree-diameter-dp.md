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
---

# TDP-002: Tree Diameter DP

## 📋 Problem Summary

Find the diameter of a tree, which is the longest path between any two nodes, using dynamic programming with DFS traversal in O(n) time.

## 🌍 Real-World Scenario

**Scenario Title:** Network Latency Optimization in Data Centers

A major cloud computing company operates a vast data center network where servers are connected in a tree topology (no cycles to prevent broadcast storms). The network team needs to determine the maximum possible communication delay between any two servers to establish SLA (Service Level Agreement) guarantees.

The diameter of the network tree represents the worst-case communication path - the maximum number of hops required for any two servers to communicate. This critical metric helps engineers decide where to place cache servers, determine network upgrade priorities, and set realistic latency expectations for distributed applications. If the diameter is too large, it might indicate the need for network restructuring or additional cross-links (converting the tree to a more complex graph).

This concept is also used in biological phylogenetic trees to understand evolutionary distance, in social network analysis to measure the "small world" phenomenon, and in compiler design for dependency graph analysis.

**Why This Problem Matters:**

- **Network Planning:** Determines worst-case latency and helps optimize network topology
- **Scalability Analysis:** Identifies potential bottlenecks in hierarchical systems
- **Efficient Algorithm:** O(n) solution instead of O(n²) brute force saves computation for large networks

![Real-World Application](../images/TDP-002/real-world-scenario.png)

## Detailed Explanation

The diameter of a tree is the length of the longest path between any two nodes. A key insight is that this longest path must go through some node, and from that node, it extends to its two farthest descendant subtrees.

**Key Properties:**

1. The diameter is the maximum of all (height1 + height2 + 2) values, where height1 and height2 are the two largest heights of subtrees for any node
2. Alternatively, we can find the diameter using two BFS/DFS: first find the farthest node from any arbitrary node, then find the farthest node from that node

The DP approach computes for each node:

- The maximum depth in its subtree
- The potential diameter passing through that node (sum of two largest child depths)

## Naive Approach

**Intuition:**
Try all pairs of nodes and compute the distance between them using DFS or BFS. The maximum distance found is the diameter.

### Algorithm

```
function find_diameter_naive():
    max_distance = 0

    // Step 1: Try all pairs of nodes
    for u from 1 to n:
        for v from u+1 to n:
            // Step 2: BFS to find distance
            dist = bfs_distance(u, v)
            max_distance = max(max_distance, dist)

    return max_distance

function bfs_distance(start, end):
    queue = [start]
    visited = {start: 0}
    while queue not empty:
        node = queue.pop()
        if node == end: return visited[node]
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.push(neighbor)
```

### Complexity Analysis

| Phase           | Time      | Space    | Explanation                        |
| --------------- | --------- | -------- | ---------------------------------- |
| Node pairs      | O(n²)     | O(1)     | n(n-1)/2 pairs                     |
| BFS per pair    | O(n)      | O(n)     | Visit all nodes worst case         |
| **Naive Total** | **O(n³)** | **O(n)** | Or O(n²) with all-pairs precompute |

**Why This Complexity:**

- n² pairs × O(n) BFS each = O(n³)
- Can optimize to O(n²) by precomputing all distances, but still too slow
- For n = 200,000: ~8×10¹⁵ operations (infeasible)

**Limitations:**

- Extremely slow for large trees (n = 200,000 would require billions of operations)
- Redundant computation - most pairs aren't endpoints of the diameter
- Doesn't leverage tree structure properties

## Optimal Approach

**Key Insight:**
The diameter either passes through a node (connecting its two deepest subtrees) or is entirely within one subtree. By computing the two largest depths for each node during a single DFS, we can find the diameter in one pass.

### Algorithm

**Method 1: Single DFS with DP**

```
function find_diameter():
    diameter = 0

    function dfs(node, parent):
        max1 = max2 = 0  // Two largest child depths

        for each child of node (except parent):
            child_depth = dfs(child, node)

            // Track two largest depths
            if child_depth > max1:
                max2 = max1
                max1 = child_depth
            else if child_depth > max2:
                max2 = child_depth

        // Path through this node = max1 + max2
        diameter = max(diameter, max1 + max2)

        return max1 + 1  // Depth of this subtree

    dfs(1, -1)
    return diameter
```

**Method 2: Two BFS/DFS**

```
function find_diameter_two_bfs():
    // Step 1: Find farthest node from arbitrary start
    u = bfs_farthest(node=1)

    // Step 2: Find farthest from u (this is diameter endpoint)
    v, distance = bfs_farthest_with_distance(u)

    return distance
```

### Complexity Analysis

| Phase                    | Time          | Space    | Explanation                    |
| ------------------------ | ------------- | -------- | ------------------------------ |
| **Method 1: Single DFS** |               |          |                                |
| DFS traversal            | O(n)          | O(h)     | Visit each node once           |
| Track max depths         | O(1) per node | O(1)     | Constant work                  |
| **Total**                | **O(n)**      | **O(h)** | h = height ≤ n                 |
| **Method 2: Two BFS**    |               |          |                                |
| First BFS                | O(n)          | O(n)     | Find one endpoint              |
| Second BFS               | O(n)          | O(n)     | Find other endpoint + distance |
| **Total**                | **O(n)**      | **O(n)** | Linear                         |

**Why This Is Optimal:**

- Each edge is visited exactly once (or twice in two-BFS method)
- No redundant computation
- Linear time is optimal since we must visit all nodes
- For n = 200,000: ~200K operations vs ~40B naive

![Algorithm Visualization](../images/TDP-002/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private List<Integer>[] tree;
    private int diameter = 0;

    public int treeDiameter(int n, int[][] edges) {
        tree = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }

        dfs(1, -1);
        return diameter;
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

public class Main {
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

        diameter = max(diameter, max1 + max2);
        return max1 + 1;
    }

public:
    int treeDiameter(int n, vector<pair<int, int>>& edges) {
        tree.resize(n + 1);
        diameter = 0;

        for (auto& edge : edges) {
            tree[edge.first].push_back(edge.second);
            tree[edge.second].push_back(edge.first);
        }

        dfs(1, -1);
        return diameter;
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
    this.tree = Array.from({ length: n + 1 }, () => []);
    this.diameter = 0;

    for (const [u, v] of edges) {
      this.tree[u].push(v);
      this.tree[v].push(u);
    }

    this.dfs(1, -1);
    return this.diameter;
  }

  dfs(node, parent) {
    let max1 = 0,
      max2 = 0;

    for (const child of this.tree[node]) {
      if (child === parent) continue;

      const childDepth = this.dfs(child, node);

      if (childDepth > max1) {
        max2 = max1;
        max1 = childDepth;
      } else if (childDepth > max2) {
        max2 = childDepth;
      }
    }

    this.diameter = Math.max(this.diameter, max1 + max2);
    return max1 + 1;
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

---

## 🧪 Walkthrough: Sample Testcase

### Input

```
5
1 2
1 3
2 4
2 5
```

### Visual Representation

```
Tree Structure:
        1
       / \
      2   3
     / \
    4   5

Edges: 1-2, 1-3, 2-4, 2-5
```

### DFS Walkthrough (rooted at 1)

| Node | Children | Depths from children | max1 | max2 | Diameter candidate | Return |
| ---- | -------- | -------------------- | ---- | ---- | ------------------ | ------ |
| 4    | none     | []                   | 0    | 0    | 0                  | 1      |
| 5    | none     | []                   | 0    | 0    | 0                  | 1      |
| 2    | 4, 5     | [1, 1]               | 1    | 1    | **2**              | 2      |
| 3    | none     | []                   | 0    | 0    | 0                  | 1      |
| 1    | 2, 3     | [2, 1]               | 2    | 1    | **3**              | 3      |

**Diameter = max(0, 2, 3) = 3** (path: 4→2→1→3 or 5→2→1→3)

**Output:** `3`

---

## ⚠️ Common Mistakes to Avoid

| #   | Mistake                  | ❌ Wrong                        | ✅ Correct                                      |
| --- | ------------------------ | ------------------------------- | ----------------------------------------------- |
| 1   | **Track only one depth** | `diameter = max1`               | `diameter = max1 + max2`                        |
| 2   | **Wrong return value**   | `return max1 + max2` (diameter) | `return max1 + 1` (depth for parent)            |
| 3   | **Forget base case**     | No handling for leaves          | `return 1` for leaf nodes                       |
| 4   | **Off-by-one in edges**  | `diameter = max1 + max2 + 2`    | `diameter = max1 + max2` (depths include edges) |

### Detailed Example:

**Mistake 2: Returning Diameter Instead of Depth**

```python
# ❌ Wrong: Returns diameter (sum of depths) to parent
def dfs(u, p):
    max1, max2 = 0, 0
    for v in adj[u]:
        if v != p:
            d = dfs(v, u)
            # Update max1, max2...
    return max1 + max2  # WRONG! Parent needs depth, not diameter

# ✅ Correct: Returns depth (longest path down from u)
def dfs(u, p):
    max1, max2 = 0, 0
    for v in adj[u]:
        if v != p:
            d = dfs(v, u)
            if d > max1:
                max1, max2 = d, max1
            elif d > max2:
                max2 = d
    global diameter
    diameter = max(diameter, max1 + max2)
    return max1 + 1  # Return depth for parent's calculation
```

---

## Related Concepts

- **Tree Height:** Maximum depth from root (special case of diameter)
- **Tree Center:** Node(s) minimizing maximum distance to all other nodes
- **Tree Centroid:** Node whose removal creates most balanced subtrees
- **All-Pairs Shortest Paths:** General problem tree diameter is a special case of
