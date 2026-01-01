---
problem_id: TRE_AUDITORIUM_TOP_VIEW_HEIGHT__5601
display_id: TRE-010
slug: auditorium-top-view-height
title: "Auditorium Top View With Height Bonus"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - top-view
  - bfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-010: Auditorium Top View With Height Bonus

## 📋 Problem Summary

Find the **Top View** of a binary tree. The top view consists of the nodes visible when looking at the tree from directly above.
-   Nodes are grouped by horizontal distance (column).
-   For each column, the visible node is the one with the **smallest depth** (highest up).
-   **Tie-Breaker:** If multiple nodes in the same column have the same depth, choose the one with the **largest value**.

## 🌍 Real-World Scenario

**Scenario Title:** City Skyline

Imagine a city where buildings (nodes) are located at different horizontal coordinates (columns).
-   When viewed from a satellite (top view), you only see the roof of the tallest building at each coordinate.
-   In this tree analogy, "tallest" means "smallest depth" (closest to the root/sky).
-   If two buildings are at the same location and same height (depth), imagine they are stacked or merged, and the one with the "Height Bonus" (largest value) is the one that represents that spot on the map.

![Real-World Application](../images/TRE-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1
     / \
    2   3
     \
      4
       \
        5
```
**Columns:**
-   **Col 0:** Node 1 (Depth 0).
-   **Col -1:** Node 2 (Depth 1).
-   **Col 1:** Node 3 (Depth 1).
-   **Col 0:** Node 4 (Depth 2). (Blocked by Node 1).
-   **Col 1:** Node 5 (Depth 3). (Blocked by Node 3).

**Visible Nodes:**
-   Col -1: 2
-   Col 0: 1
-   Col 1: 3

**Output:** `2 1 3`

### Algorithm Steps

1.  **BFS Traversal:** Use a queue to store `(node, col, depth)`.
2.  **Tracking:** Use a Map `col -> {minDepth, maxValue}`.
3.  **Update Logic:** For each node `u` at `col` and `depth`:
    -   If `col` is not in map, add `u`.
    -   If `col` is in map:
        -   If `depth < currentMinDepth`, update (found a higher node).
        -   If `depth == currentMinDepth` AND `val > currentMaxVal`, update (tie-breaker).
4.  **Output:** Sort map keys (columns) and print values.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Root Column:** 0.
-   **Left Child:** `col - 1`.
-   **Right Child:** `col + 1`.
-   **Tie-Breaker:** Only applies if depths are *exactly* equal. Usually, BFS guarantees we see smaller depths first, but nodes at the same depth can appear in any order depending on tree structure (e.g., left child of right node vs right child of left node).

## Naive Approach

### Intuition

DFS can visit nodes in any order. We can collect all nodes into a list `(col, depth, val)`, sort them, and pick the best one for each column.

### Algorithm

1.  DFS to collect all nodes.
2.  Group by column.
3.  For each column, sort by `depth` asc, then `val` desc.
4.  Pick first.

### Time Complexity

-   **O(N log N)**: Sorting.

## Optimal Approach (BFS)

BFS naturally visits nodes level by level (depth 0, then 1, etc.).
-   The **first** time we encounter a column `C`, that node is guaranteed to have the minimal depth for that column.
-   **Exception:** If multiple nodes at the *same* depth map to the same column, BFS will visit them in sequence. We must check the tie-breaker (max value).
-   Nodes at *greater* depths will be visited later and can be ignored (since depth is strictly greater).

### Algorithm

1.  Queue `q` stores `(u, col)`.
2.  Map `topView` stores `col -> {val, depth}`.
3.  BFS:
    -   Pop `(u, c)`.
    -   If `c` not in `topView`: store `(val, depth)`.
    -   Else if `depth == storedDepth`: update if `val > storedVal`.
    -   (Note: BFS guarantees `depth >= storedDepth`. We never find a smaller depth later).
4.  Iterate `minCol` to `maxCol` and print.

### Time Complexity

-   **O(N)**: BFS visits each node once. Map operations O(1) or O(log N). Sorting columns takes O(K log K) where K is width (K <= N).

### Space Complexity

-   **O(N)**: Queue and Map.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    static class NodeEntry {
        int val;
        int depth;
        NodeEntry(int v, int d) {
            this.val = v;
            this.depth = d;
        }
    }

    public List<Integer> topView(int n, int[] values, int[] left, int[] right) {
        if (n == 0) return new ArrayList<>();

        Map<Integer, NodeEntry> map = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>(); // {u, col, depth}
        q.offer(new int[]{0, 0, 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            if (!map.containsKey(c)) {
                map.put(c, new NodeEntry(values[u], d));
            } else {
                NodeEntry existing = map.get(c);
                if (d < existing.depth) {
                    // Should not happen with BFS unless we revisit? BFS is level-order.
                    map.put(c, new NodeEntry(values[u], d));
                } else if (d == existing.depth) {
                    if (values[u] > existing.val) {
                        existing.val = values[u];
                    }
                }
            }

            if (left[u] != -1) q.offer(new int[]{left[u], c - 1, d + 1});
            if (right[u] != -1) q.offer(new int[]{right[u], c + 1, d + 1});
        }

        List<Integer> result = new ArrayList<>();
        for (int c : map.keySet()) {
            result.add(map.get(c).val);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<Integer> ans = solution.topView(n, values, left, right);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ans.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(ans.get(i));
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python
```python
import sys
sys.setrecursionlimit(200000)
from collections import deque

def top_view(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    if n == 0:
        return []
        
    # Map: col -> (depth, val)
    view_map = {}
    q = deque([(0, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    while q:
        u, c, d = q.popleft()
        
        if c not in view_map:
            view_map[c] = (d, values[u])
        else:
            existing_depth, existing_val = view_map[c]
            if d < existing_depth:
                view_map[c] = (d, values[u])
            elif d == existing_depth:
                if values[u] > existing_val:
                    view_map[c] = (d, values[u])
                    
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if left[u] != -1:
            q.append((left[u], c - 1, d + 1))
        if right[u] != -1:
            q.append((right[u], c + 1, d + 1))
            
    result = []
    for c in range(min_col, max_col + 1):
        if c in view_map:
            result.append(view_map[c][1])
            
    return result

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    values = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        values[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    ans = top_view(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

struct NodeInfo {
    int val;
    int depth;
};

class Solution {
public:
    vector<int> topView(int n, const vector<int>& values,
                        const vector<int>& left, const vector<int>& right) {
        if (n == 0) return {};

        map<int, NodeInfo> viewMap;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            if (viewMap.find(c) == viewMap.end()) {
                viewMap[c] = {values[u], d};
            } else {
                if (d < viewMap[c].depth) {
                    viewMap[c] = {values[u], d};
                } else if (d == viewMap[c].depth) {
                    if (values[u] > viewMap[c].val) {
                        viewMap[c].val = values[u];
                    }
                }
            }

            if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
            if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
        }

        vector<int> result;
        for (auto const& [col, info] : viewMap) {
            result.push_back(info.val);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.topView(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  topView(n, values, left, right) {
    if (n === 0) return [];

    const viewMap = new Map(); // col -> {val, depth}
    const q = [{ u: 0, c: 0, d: 0 }];
    let minCol = 0;
    let maxCol = 0;

    while (q.length > 0) {
      const { u, c, d } = q.shift();

      if (!viewMap.has(c)) {
        viewMap.set(c, { val: values[u], depth: d });
      } else {
        const existing = viewMap.get(c);
        if (d < existing.depth) {
          viewMap.set(c, { val: values[u], depth: d });
        } else if (d === existing.depth) {
          if (values[u] > existing.val) {
            existing.val = values[u];
          }
        }
      }

      if (c < minCol) minCol = c;
      if (c > maxCol) maxCol = c;

      if (left[u] !== -1) q.push({ u: left[u], c: c - 1, d: d + 1 });
      if (right[u] !== -1) q.push({ u: right[u], c: c + 1, d: d + 1 });
    }

    const result = [];
    for (let c = minCol; c <= maxCol; c++) {
      if (viewMap.has(c)) {
        result.push(viewMap.get(c).val);
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
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const ans = solution.topView(n, values, left, right);
  console.log(ans.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
1 1 2
2 3 -1
3 -1 4
4 -1 -1
5 -1 -1
```
**Tree:**
- 0(1) -> L:1(2), R:2(3)
- 1(2) -> L:3(4), R:-1
- 2(3) -> L:-1, R:4(5)

**BFS:**
1.  `(0, c=0, d=0)` -> Map: `{0: (1, 0)}`.
2.  `(1, c=-1, d=1)` -> Map: `{0: (1, 0), -1: (2, 1)}`.
3.  `(2, c=1, d=1)` -> Map: `{0: (1, 0), -1: (2, 1), 1: (3, 1)}`.
4.  `(3, c=-2, d=2)` -> Map: `{..., -2: (4, 2)}`.
5.  `(4, c=2, d=2)` -> Map: `{..., 2: (5, 2)}`.

**Sorted Columns:** -2, -1, 0, 1, 2.
**Values:** 4, 2, 1, 3, 5.

## ✅ Proof of Correctness

BFS visits nodes in non-decreasing order of depth.
-   When we first see column `C`, we are at the minimum possible depth for that column (since any future visit will have `depth >= current`).
-   We only update if `depth == minDepth` and `val > currentMax`.
-   This correctly implements the "smallest depth, then largest value" logic.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Bottom View**
    -   Last node seen in each column (max depth).
-   **Extension 2: Left/Right View**
    -   First/Last node in each *level* (not column).
-   **Extension 3: Vertical Sum**
    -   Sum of all nodes in each column.

### Common Mistakes to Avoid

1.  **DFS Order:**
    -   ❌ Using DFS without tracking depth carefully. DFS might visit a deeper node before a shallower one in the same column.
    -   ✅ BFS is safer. If using DFS, must check depth explicitly.
2.  **Tie-Breaker:**
    -   ❌ Forgetting the `val > maxVal` check for equal depths.

## Related Concepts

-   **BFS**
-   **Vertical Traversal**
-   **TreeMap / Hashing**
