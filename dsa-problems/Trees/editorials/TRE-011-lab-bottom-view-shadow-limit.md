---
problem_id: TRE_LAB_BOTTOM_VIEW_SHADOW_LIMIT__3395
display_id: TRE-011
slug: lab-bottom-view-shadow-limit
title: "Lab Bottom View with Shadow Limit"
difficulty: Medium
difficulty_score: 50
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - bottom-view
  - bfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-011: Lab Bottom View with Shadow Limit

## 📋 Problem Summary

Find the **Bottom View** of a binary tree, but with a constraint: any node located deeper than depth `D` is considered "in the shadow" or "out of range" and cannot be part of the view.
-   Nodes are grouped by horizontal distance (column).
-   For each column, select the node with the **largest depth** that satisfies `depth <= D`.
-   If multiple nodes in the same column have the same maximal depth (within limit), the one visited **last** in a standard level-order traversal (rightmost) is typically chosen (or the problem implies "visible from bottom", so the last one covering the slot).

## 🌍 Real-World Scenario

**Scenario Title:** Underwater Sensor Array

Imagine a research vessel deploying sensors at various depths in the ocean.
-   **Horizontal Distance:** Location relative to the ship.
-   **Depth:** Distance below surface.
-   **Limit D:** The maximum depth sunlight can penetrate (or sonar range).

You want to map the "deepest visible object" at each horizontal location. Anything deeper than `D` is in the dark zone and shouldn't be reported. You need the deepest sensor reading that is still within the illuminated zone.

![Real-World Application](../images/TRE-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1 (Depth 0)
     / \
    2   3 (Depth 1)
   / \
  4   5 (Depth 2)
```
**Limit D = 1**

**Columns:**
-   **Col 0:** Node 1 (Depth 0).
-   **Col -1:** Node 2 (Depth 1).
-   **Col 1:** Node 3 (Depth 1).
-   **Col -2:** Node 4 (Depth 2). **Ignored (Depth > 1)**.
-   **Col 0:** Node 5 (Depth 2). **Ignored (Depth > 1)**.

**Visible Nodes (Depth <= 1):**
-   Col -1: Node 2.
-   Col 0: Node 1. (Node 5 is ignored).
-   Col 1: Node 3.

**Output:** `2 1 3`

### Algorithm Steps

1.  **BFS Traversal:** Use a queue to store `(node, col, depth)`.
2.  **Tracking:** Use a Map `col -> {val, depth}`.
3.  **Update Logic:** For each node `u` at `col` and `depth`:
    -   If `depth > D`, **skip** processing (don't add to map, but still add children to queue? Yes, children might be deeper, but if `depth > D`, children are `depth+1 > D`, so we can actually stop traversing that branch entirely).
    -   If `depth <= D`, update `map[col] = {val, depth}`.
    -   Since BFS visits level by level, a later visit to the same column at the same or greater depth (but still `<= D`) will overwrite the previous value. This correctly captures the "bottom-most" (and right-most for ties) node.
4.  **Output:** Sort map keys (columns) and print values.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Stopping Condition:** If a node is at depth `D`, its children are at `D+1`. We can stop adding children to the queue if `depth == D`.
-   **Tie-Breaker:** Standard Bottom View usually takes the "last seen" node at the deepest level. BFS naturally handles this if we process left-to-right.
-   **Empty Tree:** Output empty line.

## Naive Approach

### Intuition

Traverse the entire tree using DFS, collect valid nodes, and filter.

### Algorithm

1.  DFS to collect all nodes `(col, depth, val)`.
2.  Filter list where `depth <= D`.
3.  Group by column.
4.  Sort each group by `depth` asc, then `arrival time` (or just update map).
5.  Pick last.

### Time Complexity

-   **O(N)**: Visit all nodes.

## Optimal Approach (BFS with Pruning)

BFS allows us to stop traversing a branch as soon as we hit depth `D`. This is an optimization: we don't even need to visit nodes deeper than `D`.

### Algorithm

1.  Queue `q` stores `(u, col, depth)`.
2.  Map `bottomView` stores `col -> val`.
3.  BFS:
    -   Pop `(u, c, d)`.
    -   Update `bottomView[c] = val`. (Always overwrite, as BFS guarantees non-decreasing depth).
    -   If `d < D`:
        -   Add children to queue with `d + 1`.
4.  Iterate `minCol` to `maxCol` and print.

### Time Complexity

-   **O(N)**: In worst case (D is large), visit all nodes. If D is small, visits fewer.

### Space Complexity

-   **O(N)**: Queue and Map.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> bottomViewWithLimit(int n, int[] values, int[] left, int[] right, int D) {
        if (n == 0) return new ArrayList<>();

        Map<Integer, Integer> map = new TreeMap<>();
        Queue<int[]> q = new LinkedList<>(); // {u, col, depth}
        q.offer(new int[]{0, 0, 0});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int c = curr[1];
            int d = curr[2];

            // Update map since d <= D (guaranteed by check before adding to queue)
            map.put(c, values[u]);

            // Only add children if current depth < D
            if (d < D) {
                if (left[u] != -1) q.offer(new int[]{left[u], c - 1, d + 1});
                if (right[u] != -1) q.offer(new int[]{right[u], c + 1, d + 1});
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int val : map.values()) {
            result.add(val);
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
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        int D = 0;
        if (sc.hasNextInt()) D = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> ans = solution.bottomViewWithLimit(n, values, left, right, D);
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
from collections import deque

def bottom_view_with_limit(n: int, values: list[int], left: list[int], right: list[int], D: int) -> list[int]:
    if n == 0:
        return []
        
    view_map = {}
    q = deque([(0, 0, 0)]) # u, col, depth
    
    min_col, max_col = 0, 0
    
    # If root depth > D (impossible since root is 0 and D >= 0), but safe check
    if D < 0:
        return []
        
    while q:
        u, c, d = q.popleft()
        
        view_map[c] = values[u]
        min_col = min(min_col, c)
        max_col = max(max_col, c)
        
        if d < D:
            if left[u] != -1:
                q.append((left[u], c - 1, d + 1))
            if right[u] != -1:
                q.append((right[u], c + 1, d + 1))
                
    result = []
    for c in range(min_col, max_col + 1):
        if c in view_map:
            result.append(view_map[c])
            
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
    D = int(data[idx]) if idx < len(data) else 0
    ans = bottom_view_with_limit(n, values, left, right, D)
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

class Solution {
public:
    vector<int> bottomViewWithLimit(int n, const vector<int>& values,
                                    const vector<int>& left, const vector<int>& right, int D) {
        if (n == 0) return {};

        map<int, int> viewMap;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            viewMap[c] = values[u];

            if (d < D) {
                if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
                if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
            }
        }

        vector<int> result;
        for (auto const& [col, val] : viewMap) {
            result.push_back(val);
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
    int D;
    cin >> D;

    Solution solution;
    vector<int> ans = solution.bottomViewWithLimit(n, values, left, right, D);
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
  bottomViewWithLimit(n, values, left, right, D) {
    if (n === 0) return [];

    const viewMap = new Map();
    const q = [{ u: 0, c: 0, d: 0 }];
    let minCol = 0;
    let maxCol = 0;

    while (q.length > 0) {
      const { u, c, d } = q.shift();

      viewMap.set(c, values[u]);
      
      if (c < minCol) minCol = c;
      if (c > maxCol) maxCol = c;

      if (d < D) {
        if (left[u] !== -1) q.push({ u: left[u], c: c - 1, d: d + 1 });
        if (right[u] !== -1) q.push({ u: right[u], c: c + 1, d: d + 1 });
      }
    }

    const result = [];
    for (let c = minCol; c <= maxCol; c++) {
      if (viewMap.has(c)) {
        result.push(viewMap.get(c));
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
  const D = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const ans = solution.bottomViewWithLimit(n, values, left, right, D);
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
1
```
**Tree:**
- 0(1) -> L:1(2), R:2(3)
- 1(2) -> L:3(4), R:-1
- 2(3) -> L:-1, R:4(5)
**Limit D=1**

**BFS:**
1.  `(0, c=0, d=0)` -> Map: `{0: 1}`. `d < 1`, add children.
2.  `(1, c=-1, d=1)` -> Map: `{0: 1, -1: 2}`. `d == 1`, stop children.
3.  `(2, c=1, d=1)` -> Map: `{0: 1, -1: 2, 1: 3}`. `d == 1`, stop children.

**Note:** Node 3 (4) and Node 4 (5) are at depth 2. They are never added to queue.

**Result:** `2 1 3` (Sorted by col: -1, 0, 1).

## ✅ Proof of Correctness

BFS visits nodes level by level.
-   We only add nodes to the queue if their depth is `< D`. This ensures we process nodes up to depth `D`.
-   We update the map for every node processed. Since BFS visits deeper nodes later, the map entry for a column will eventually hold the value of the deepest node in that column (within the limit).
-   If multiple nodes are at the same maximal depth, BFS visits left-to-right, so the rightmost one overwrites, which is the standard definition of Bottom View.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Range Query**
    -   Output bottom view only for columns `[L, R]`.
-   **Extension 2: Deepest Node**
    -   Find the single deepest node in the entire tree within limit.
-   **Extension 3: Top View with Limit**
    -   Same logic, but don't overwrite if key exists.

### Common Mistakes to Avoid

1.  **Off-by-one Depth:**
    -   ❌ Stopping at `d < D` but not processing `d == D`.
    -   ✅ Process `d == D`, but don't add children.
2.  **Map Ordering:**
    -   ❌ Iterating map keys in random order.
    -   ✅ Use TreeMap or sort keys.

## Related Concepts

-   **BFS**
-   **Tree Views**
-   **Pruning**
