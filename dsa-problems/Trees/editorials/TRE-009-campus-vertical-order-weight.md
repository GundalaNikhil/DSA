---
problem_id: TRE_CAMPUS_VERTICAL_ORDER_WEIGHT__4502
display_id: TRE-009
slug: campus-vertical-order-weight
title: "Campus Vertical Order With Weight Priority"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - BFS
  - Sorting
tags:
  - trees
  - vertical-order
  - sorting
  - medium
premium: true
subscription_tier: basic
---

# TRE-009: Campus Vertical Order With Weight Priority

## 📋 Problem Summary

Perform a **vertical order traversal** of a binary tree. Nodes are grouped by their horizontal distance from the root (column index). Within each column, nodes must be sorted by:
1.  **Depth** (ascending, top to bottom).
2.  **Weight** (descending, heavier items first).
3.  **Value** (ascending, tie-breaker).

Finally, filter the output to only include columns where the **sum of weights** of all nodes in that column is at least `W`.

## 🌍 Real-World Scenario

**Scenario Title:** Warehouse Shelving Optimization

Imagine a warehouse where items are stored on vertical racks (columns).
-   **Horizontal Distance:** Represents the rack number relative to the central aisle.
-   **Depth:** Represents the shelf level (higher shelves are depth 0).
-   **Weight:** Heavier items should be listed first for structural checks or priority picking.
-   **Value:** Item ID.

The manager wants a report of all racks that are "heavily loaded" (total weight >= `W`) to schedule maintenance. The report must list items on each rack from top to bottom, prioritizing heavy items on the same shelf.

![Real-World Application](../images/TRE-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      3 (W=5)
     / \
    9   8 (W=3)
       / \
      4   7 (W=4)
```
**Columns:**
-   **Col -1:** Node 9 (Weight 2). Total = 2.
-   **Col 0:** Node 3 (Weight 5), Node 4 (Weight 1). Total = 6.
-   **Col 1:** Node 8 (Weight 3). Total = 3.
-   **Col 2:** Node 7 (Weight 4). Total = 4.

**Threshold W = 3:**
-   Col -1 (Total 2) < 3. Skip.
-   Col 0 (Total 6) >= 3. Keep.
-   Col 1 (Total 3) >= 3. Keep.
-   Col 2 (Total 4) >= 3. Keep.

**Ordering in Col 0:**
-   Node 3 (Depth 0, Weight 5).
-   Node 4 (Depth 2, Weight 1).
-   Order: 3, 4.

### Algorithm Steps

1.  **BFS Traversal:** Use a queue to traverse the tree. Store tuples `(node, col, depth)`.
2.  **Grouping:** Use a Map `col -> List<NodeInfo>`. `NodeInfo` stores `{val, weight, depth}`.
3.  **Sorting:** For each column list, sort using the custom comparator:
    -   Compare `depth`: if different, smaller depth comes first.
    -   Compare `weight`: if different, larger weight comes first.
    -   Compare `val`: if different, smaller val comes first.
4.  **Filtering:** Calculate total weight for each column. Discard columns with `total < W`.
5.  **Output:** Print valid columns sorted by column index (min to max).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Column Index:** Root is 0. Left child is `col - 1`. Right child is `col + 1`.
-   **Depth:** Root is 0. Children are `depth + 1`.
-   **Sorting:** Strict priority: Depth -> Weight (Desc) -> Value (Asc).
-   **Weights:** Can be large, use `long` for sums.

## Naive Approach

### Intuition

We can use DFS to traverse and collect nodes. DFS naturally visits deeper nodes later, but not necessarily in order of depth for the same column (e.g., left subtree depth 2 vs right subtree depth 2). So explicit sorting is required regardless of traversal method.

### Algorithm

1.  DFS(root, col, depth).
2.  Store all nodes in a list.
3.  Group by column.
4.  Sort each group.
5.  Filter and print.

### Time Complexity

-   **O(N log N)**: Due to sorting nodes within columns.

## Optimal Approach (BFS + Sorting)

BFS is slightly better than DFS because it naturally visits nodes in depth order. This means the primary sort key (depth) is already mostly sorted. However, since we have secondary criteria (weight, value) for nodes at the *same* depth/column, we still need to sort.

### Algorithm

1.  Queue `q` stores `(u, col, depth)`.
2.  Map `map` stores `col -> List<Node>`.
3.  BFS:
    -   Pop `(u, c, d)`.
    -   Add `u` to `map[c]`.
    -   Push `(left, c-1, d+1)` and `(right, c+1, d+1)`.
4.  Iterate `minCol` to `maxCol`.
5.  If `map[c]` exists:
    -   Sum weights. If `< W`, continue.
    -   Sort `map[c]`.
    -   Print values.

### Time Complexity

-   **O(N log N)**: Sorting is the bottleneck. BFS is O(N).

### Space Complexity

-   **O(N)**: Store all nodes.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class NodeInfo {
        int val, weight, depth;
        NodeInfo(int v, int w, int d) {
            this.val = v;
            this.weight = w;
            this.depth = d;
        }
    }

    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights,
                                                       int[] left, int[] right, long W) {
        if (n == 0) return new ArrayList<>();

        Map<Integer, List<NodeInfo>> cols = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>(); // {u, col, depth}
        q.offer(new int[]{0, 0, 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            cols.computeIfAbsent(c, k -> new ArrayList<>()).add(new NodeInfo(values[u], weights[u], d));

            if (left[u] != -1) q.offer(new int[]{left[u], c - 1, d + 1});
            if (right[u] != -1) q.offer(new int[]{right[u], c + 1, d + 1});
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int c : cols.keySet()) {
            List<NodeInfo> list = cols.get(c);
            long totalWeight = 0;
            for (NodeInfo node : list) totalWeight += node.weight;

            if (totalWeight >= W) {
                Collections.sort(list, (a, b) -> {
                    if (a.depth != b.depth) return a.depth - b.depth;
                    if (a.weight != b.weight) return b.weight - a.weight; // Descending
                    return a.val - b.val;
                });

                List<Integer> colValues = new ArrayList<>();
                for (NodeInfo node : list) colValues.add(node.val);
                result.add(colValues);
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            weights[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long W = 0;
        if (sc.hasNextLong()) W = sc.nextLong();

        Solution solution = new Solution();
        List<List<Integer>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
        if (cols.isEmpty()) {
            System.out.println();
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < cols.size(); i++) {
                List<Integer> col = cols.get(i);
                for (int j = 0; j < col.size(); j++) {
                    if (j > 0) sb.append(' ');
                    sb.append(col.get(j));
                }
                if (i + 1 < cols.size()) sb.append('\n');
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque, defaultdict

def vertical_order_with_weights(n: int, values: list[int], weights: list[int],
                                left: list[int], right: list[int], W: int) -> list[list[int]]:
    if n == 0:
        return []
        
    cols = defaultdict(list)
    q = deque([(0, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    while q:
        u, c, d = q.popleft()
        cols[c].append((values[u], weights[u], d))
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if left[u] != -1:
            q.append((left[u], c - 1, d + 1))
        if right[u] != -1:
            q.append((right[u], c + 1, d + 1))
            
    result = []
    for c in range(min_col, max_col + 1):
        if c in cols:
            nodes = cols[c]
            total_weight = sum(node[1] for node in nodes)
            
            if total_weight >= W:
                # Sort: depth asc, weight desc, val asc
                nodes.sort(key=lambda x: (x[2], -x[1], x[0]))
                result.append([x[0] for x in nodes])
                
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    weights = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        weights[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    W = int(data[idx]) if idx < len(data) else 0
    
    cols = vertical_order_with_weights(n, values, weights, left, right, W)
    if not cols:
        print()
    else:
        print("\n".join(" ".join(str(x) for x in col) for col in cols))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct NodeInfo {
    int val, weight, depth;
};

class Solution {
public:
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values,
                                                 const vector<int>& weights, const vector<int>& left,
                                                 const vector<int>& right, long long W) {
        if (n == 0) return {};

        map<int, vector<NodeInfo>> cols;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            cols[c].push_back({values[u], weights[u], d});

            if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
            if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
        }

        vector<vector<int>> result;
        for (auto& entry : cols) {
            long long totalWeight = 0;
            for (const auto& node : entry.second) totalWeight += node.weight;

            if (totalWeight >= W) {
                sort(entry.second.begin(), entry.second.end(), [](const NodeInfo& a, const NodeInfo& b) {
                    if (a.depth != b.depth) return a.depth < b.depth;
                    if (a.weight != b.weight) return a.weight > b.weight; // Descending
                    return a.val < b.val;
                });

                vector<int> colValues;
                for (const auto& node : entry.second) colValues.push_back(node.val);
                result.push_back(colValues);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), weights(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> weights[i] >> left[i] >> right[i];
    }
    long long W;
    cin >> W;

    Solution solution;
    vector<vector<int>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
    if (cols.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)cols.size(); i++) {
            for (int j = 0; j < (int)cols[i].size(); j++) {
                if (j) cout << ' ';
                cout << cols[i][j];
            }
            if (i + 1 < (int)cols.size()) cout << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  verticalOrderWithWeights(n, values, weights, left, right, W) {
    if (n === 0) return [];

    const cols = new Map();
    const q = [{ u: 0, c: 0, d: 0 }];
    let minCol = 0;
    let maxCol = 0;

    while (q.length > 0) {
      const { u, c, d } = q.shift();
      
      if (!cols.has(c)) cols.set(c, []);
      cols.get(c).push({ val: values[u], weight: weights[u], depth: d });
      
      if (c < minCol) minCol = c;
      if (c > maxCol) maxCol = c;

      if (left[u] !== -1) q.push({ u: left[u], c: c - 1, d: d + 1 });
      if (right[u] !== -1) q.push({ u: right[u], c: c + 1, d: d + 1 });
    }

    const result = [];
    for (let c = minCol; c <= maxCol; c++) {
      if (cols.has(c)) {
        const list = cols.get(c);
        let totalWeight = 0n;
        for (const node of list) totalWeight += BigInt(node.weight);

        if (totalWeight >= BigInt(W)) {
          list.sort((a, b) => {
            if (a.depth !== b.depth) return a.depth - b.depth;
            if (a.weight !== b.weight) return b.weight - a.weight;
            return a.val - b.val;
          });
          result.push(list.map(node => node.val));
        }
      }
    }
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  const weights = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    weights[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const W = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
  if (cols.length === 0) {
    console.log("");
  } else {
    console.log(cols.map((col) => col.join(" ")).join("\n"));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
3 5 1 2
9 2 -1 -1
8 3 3 4
4 1 -1 -1
7 4 -1 -1
3
```
**Tree:**
- 0(3, w=5) -> L:1(9, w=2), R:2(8, w=3)
- 2(8, w=3) -> L:3(4, w=1), R:4(7, w=4)

**BFS:**
- `(0, c=0, d=0)` -> Col 0: `[(3, 5, 0)]`
- `(1, c=-1, d=1)` -> Col -1: `[(9, 2, 1)]`
- `(2, c=1, d=1)` -> Col 1: `[(8, 3, 1)]`
- `(3, c=0, d=2)` -> Col 0: `[(3, 5, 0), (4, 1, 2)]`
- `(4, c=2, d=2)` -> Col 2: `[(7, 4, 2)]`

**Weights & Filtering (W=3):**
- Col -1: Total 2. Fail.
- Col 0: Total 6. Pass. Sorted: `(3,5,0), (4,1,2)`. Values: `3 4`.
- Col 1: Total 3. Pass. Sorted: `(8,3,1)`. Values: `8`.
- Col 2: Total 4. Pass. Sorted: `(7,4,2)`. Values: `7`.

**Output:**
```
3 4
8
7
```

## ✅ Proof of Correctness

BFS ensures we visit nodes level by level, but since we need to group by column first, we collect everything into a Map.
The sorting step explicitly enforces the problem's ordering rules (Depth -> Weight -> Value).
The filtering step explicitly checks the sum condition.
Using a TreeMap or iterating `minCol` to `maxCol` ensures columns are output in left-to-right order.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Top View**
    -   Print only the first node in each column.
-   **Extension 2: Diagonal Traversal**
    -   Group by `depth - col` (or similar metric).
-   **Extension 3: Width of Tree**
    -   `maxCol - minCol + 1`.

### Common Mistakes to Avoid

1.  **Sorting Order:**
    -   ❌ Sorting weight ascending.
    -   ✅ Problem says weight **descending**.
2.  **Column Order:**
    -   ❌ Printing columns in random hash map order.
    -   ✅ Must be sorted by column index.
3.  **Tie-Breaking:**
    -   ❌ Ignoring value tie-breaker.

