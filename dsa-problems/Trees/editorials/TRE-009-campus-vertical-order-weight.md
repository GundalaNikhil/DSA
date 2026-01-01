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
import java.io.*;
import java.util.*;

class Solution {
    static class NodeInfo {
        int val;
        int weight;
        int depth;
        NodeInfo(int val, int weight, int depth) {
            this.val = val;
            this.weight = weight;
            this.depth = depth;
        }
    }

    public List<List<Integer>> verticalOrderWithWeights(int n, int[] values, int[] weights,
                                                       int[] left, int[] right, int W) {
        if (n == 0) return new ArrayList<>();

        boolean[] hasParent = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        Map<Integer, List<NodeInfo>> cols = new HashMap<>();
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{root, 0, 0});
        boolean[] visited = new boolean[n];
        visited[root] = true;

        int minCol = 0;
        int maxCol = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            cols.computeIfAbsent(c, k -> new ArrayList<>()).add(new NodeInfo(values[u], weights[u], d));
            minCol = Math.min(minCol, c);
            maxCol = Math.max(maxCol, c);

            if (left[u] != -1 && !visited[left[u]]) {
                visited[left[u]] = true;
                q.add(new int[]{left[u], c - 1, d + 1});
            }
            if (right[u] != -1 && !visited[right[u]]) {
                visited[right[u]] = true;
                q.add(new int[]{right[u], c + 1, d + 1});
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int c = minCol; c <= maxCol; c++) {
            List<NodeInfo> list = cols.get(c);
            if (list == null) continue;
            long totalWeight = 0;
            for (NodeInfo node : list) totalWeight += node.weight;
            if (totalWeight >= W) {
                list.sort((a, b) -> {
                    if (a.depth != b.depth) return a.depth - b.depth;
                    if (a.weight != b.weight) return b.weight - a.weight;
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

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (!line.isEmpty()) lines.add(line);
        }
        if (lines.isEmpty()) return;

        int n = Integer.parseInt(lines.get(0));
        int[] values = new int[n];
        int[] weights = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            values[i] = Integer.parseInt(parts[0]);
            if (parts.length >= 4) {
                weights[i] = Integer.parseInt(parts[1]);
                left[i] = Integer.parseInt(parts[2]);
                right[i] = Integer.parseInt(parts[3]);
            } else {
                weights[i] = 1;
                left[i] = Integer.parseInt(parts[1]);
                right[i] = Integer.parseInt(parts[2]);
            }
        }

        int W = 0;
        if (lines.size() > n + 1) {
            W = Integer.parseInt(lines.get(n + 1));
        }

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
    }
}
```

### Python
```python
import sys
sys.setrecursionlimit(200000)
from collections import deque, defaultdict

def vertical_order_with_weights(n: int, values: list[int], weights: list[int],
                                left: list[int], right: list[int], W: int) -> list[list[int]]:
    if n == 0:
        return []

    # Identify Root
    has_parent = [False] * n
    for i in range(n):
        if left[i] != -1: has_parent[left[i]] = True
        if right[i] != -1: has_parent[right[i]] = True
        
    root = 0
    for i in range(n):
        if not has_parent[i]:
            root = i
            break
            
    cols = defaultdict(list)
    q = deque([(root, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    visited = {root} # Safety against cycles/bad input
    
    while q:
        u, c, d = q.popleft()
        cols[c].append((values[u], weights[u], d))
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if left[u] != -1 and left[u] not in visited:
            visited.add(left[u])
            q.append((left[u], c - 1, d + 1))
        if right[u] != -1 and right[u] not in visited:
            visited.add(right[u])
            q.append((right[u], c + 1, d + 1))
            
    result = []
    for c in range(min_col, max_col + 1):
        if c in cols:
            nodes = cols[c]
            total_weight = sum(node[1] for node in nodes)
            if total_weight >= W:
                # Priority: depth asc (x[2]), weight desc (-x[1]), value asc (x[0])
                nodes.sort(key=lambda x: (x[2], -x[1], x[0]))
                result.append([x[0] for x in nodes])
                
    return result

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        values = [0] * n
        weights = [0] * n
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            # 4 tokens: val weight left right
            # 3 tokens: val left right (default weight 1)
            
            values[i] = parts[0]
            if len(parts) >= 4:
                weights[i] = parts[1]
                left[i] = parts[2]
                right[i] = parts[3]
            else:
                weights[i] = 1
                left[i] = parts[1]
                right[i] = parts[2]
                
        # W might be on next line
        try:
            line = next(iterator)
            W = int(line)
        except StopIteration:
            W = 0
            
        cols = vertical_order_with_weights(n, values, weights, left, right, W)
        if not cols:
            print()
        else:
            print("\n".join(" ".join(str(x) for x in col) for col in cols))
            
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

struct NodeInfo {
    int val;
    int weight;
    int depth;
};

class Solution {
public:
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values,
                                                 const vector<int>& weights, const vector<int>& left,
                                                 const vector<int>& right, int W) {
        if (n == 0) return {};

        vector<bool> hasParent(n, false);
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        unordered_map<int, vector<NodeInfo>> cols;
        queue<pair<int, pair<int, int>>> q;
        vector<bool> visited(n, false);
        q.push({root, {0, 0}});
        visited[root] = true;

        int minCol = 0;
        int maxCol = 0;

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            cols[c].push_back({values[u], weights[u], d});
            minCol = min(minCol, c);
            maxCol = max(maxCol, c);

            if (left[u] != -1 && !visited[left[u]]) {
                visited[left[u]] = true;
                q.push({left[u], {c - 1, d + 1}});
            }
            if (right[u] != -1 && !visited[right[u]]) {
                visited[right[u]] = true;
                q.push({right[u], {c + 1, d + 1}});
            }
        }

        vector<vector<int>> result;
        for (int c = minCol; c <= maxCol; c++) {
            auto it = cols.find(c);
            if (it == cols.end()) continue;
            auto& list = it->second;
            long long totalWeight = 0;
            for (const auto& node : list) totalWeight += node.weight;
            if (totalWeight >= W) {
                sort(list.begin(), list.end(), [](const NodeInfo& a, const NodeInfo& b) {
                    if (a.depth != b.depth) return a.depth < b.depth;
                    if (a.weight != b.weight) return a.weight > b.weight;
                    return a.val < b.val;
                });
                vector<int> colValues;
                for (const auto& node : list) colValues.push_back(node.val);
                result.push_back(colValues);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty()) {
            bool allSpace = true;
            for (char ch : line) {
                if (ch > ' ') {
                    allSpace = false;
                    break;
                }
            }
            if (!allSpace) lines.push_back(line);
        }
    }
    if (lines.empty()) return 0;

    int n = stoi(lines[0]);
    vector<int> values(n, 0), weights(n, 1), left(n, -1), right(n, -1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        values[i] = (int)parts[0];
        if (parts.size() >= 4) {
            weights[i] = (int)parts[1];
            left[i] = (int)parts[2];
            right[i] = (int)parts[3];
        } else {
            weights[i] = 1;
            left[i] = (int)parts[1];
            right[i] = (int)parts[2];
        }
    }

    int W = 0;
    if ((int)lines.size() > n + 1) {
        W = stoi(lines[n + 1]);
    }

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
const fs = require("fs");

const lines = fs
  .readFileSync(0, "utf8")
  .split(/\r?\n/)
  .map((line) => line.trim())
  .filter((line) => line.length > 0);

if (lines.length === 0) {
  process.exit(0);
}

const n = parseInt(lines[0], 10);
const values = new Array(n).fill(0);
const weights = new Array(n).fill(1);
const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  values[i] = parts[0];
  if (parts.length >= 4) {
    weights[i] = parts[1];
    left[i] = parts[2];
    right[i] = parts[3];
  } else {
    weights[i] = 1;
    left[i] = parts[1];
    right[i] = parts[2];
  }
}

let W = 0;
if (lines.length > n + 1) {
  W = parseInt(lines[n + 1], 10);
}

if (n === 0) {
  console.log("");
  process.exit(0);
}

const hasParent = new Array(n).fill(false);
for (let i = 0; i < n; i++) {
  if (left[i] !== -1) hasParent[left[i]] = true;
  if (right[i] !== -1) hasParent[right[i]] = true;
}
let root = 0;
for (let i = 0; i < n; i++) {
  if (!hasParent[i]) {
    root = i;
    break;
  }
}

const cols = new Map();
const queue = [[root, 0, 0]];
let head = 0;
const visited = new Array(n).fill(false);
visited[root] = true;
let minCol = 0;
let maxCol = 0;

while (head < queue.length) {
  const [u, c, d] = queue[head++];
  if (!cols.has(c)) cols.set(c, []);
  cols.get(c).push({ val: values[u], weight: weights[u], depth: d });
  if (c < minCol) minCol = c;
  if (c > maxCol) maxCol = c;

  if (left[u] !== -1 && !visited[left[u]]) {
    visited[left[u]] = true;
    queue.push([left[u], c - 1, d + 1]);
  }
  if (right[u] !== -1 && !visited[right[u]]) {
    visited[right[u]] = true;
    queue.push([right[u], c + 1, d + 1]);
  }
}

const result = [];
for (let c = minCol; c <= maxCol; c++) {
  if (!cols.has(c)) continue;
  const list = cols.get(c);
  let totalWeight = 0;
  for (const node of list) totalWeight += node.weight;
  if (totalWeight >= W) {
    list.sort((a, b) => {
      if (a.depth !== b.depth) return a.depth - b.depth;
      if (a.weight !== b.weight) return b.weight - a.weight;
      return a.val - b.val;
    });
    result.push(list.map((node) => node.val));
  }
}

if (result.length === 0) {
  console.log("");
} else {
  console.log(result.map((col) => col.join(" ")).join("\n"));
}
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

