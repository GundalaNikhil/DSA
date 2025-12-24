---
problem_id: TRE_LAB_TREE_RIGHT_VIEW_SKIPS__3748
display_id: TRE-017
slug: lab-tree-right-view-skips
title: "Lab Tree Right View with Skips"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - right-view
  - bfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-017: Lab Tree Right View with Skips

## 📋 Problem Summary

Find the **Right View** of a binary tree, but with a twist:
-   Ignore any node whose value is **negative**.
-   For each level of the tree, find the rightmost node that is **non-negative**.
-   If a level contains only negative nodes (or no nodes at all), that level produces no output.

## 🌍 Real-World Scenario

**Scenario Title:** Security Camera Blind Spots

Imagine a multi-story building where you want to install security cameras on the right side to monitor each floor.
-   **Nodes:** Rooms on each floor.
-   **Right View:** The room visible from the rightmost camera position.
-   **Negative Values:** Rooms that are "blocked" or "restricted" (e.g., maintenance shafts, pillars) and cannot host a camera or be monitored.
-   **Goal:** List the ID of the rightmost *usable* room on each floor. If a floor has only blocked rooms, no camera is installed there.

![Real-World Application](../images/TRE-017/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      10
     /  \
    -5   20
   / \   /
  30 -8 40
```
**Levels:**
-   **Level 0:** Node 10. Positive. Rightmost is 10.
-   **Level 1:** Nodes -5, 20. Positive: 20. Rightmost is 20.
-   **Level 2:** Nodes 30, -8, 40. Positive: 30, 40. Rightmost is 40.

**Result:** `10 20 40`

**Example with Skip:**
```
      10
     /  \
    5   -20
```
-   **Level 1:** Nodes 5, -20.
-   -20 is skipped.
-   Rightmost valid is 5.
-   **Result:** `10 5`

### Algorithm Steps

1.  **Traversal:** We can use BFS (Level Order) or DFS (Reverse Preorder: Root -> Right -> Left).
2.  **Tracking:**
    -   **BFS:** For each level, iterate through all nodes. Keep track of the last seen non-negative node. If found, add to result.
    -   **DFS:** Pass `level` as parameter. Keep a map/list `level -> value`. Since we visit Right before Left, the *first* valid node we see at a new level is the rightmost one.
3.  **Filtering:** Explicitly check `node.val >= 0`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Negative Nodes:** Are traversed (their children might be positive), but they themselves are never part of the view.
-   **Empty Level:** If a level has nodes but all are negative, output nothing for that level.
-   **Output Order:** Top to bottom.

## Naive Approach

### Intuition

Collect all nodes into a list of `(level, index, value)`. Filter out negatives. Group by level. Sort by index descending. Pick first.

### Time Complexity

-   **O(N log N)**: Sorting.

## Optimal Approach (DFS - Root, Right, Left)

DFS is elegant here. If we traverse **Root -> Right -> Left**, the first valid node we encounter at any depth `d` is guaranteed to be the rightmost valid node for that depth.

### Algorithm

1.  `view = Map<Integer, Integer>` (Depth -> Value).
2.  `dfs(node, depth)`:
    -   If `node` is null, return.
    -   If `node.val >= 0` AND `depth` not in `view`:
        -   `view.put(depth, node.val)`
    -   `dfs(node.right, depth + 1)`
    -   `dfs(node.left, depth + 1)`
3.  Iterate `0` to `maxDepth`. If depth exists in map, print value.

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(H)**: Recursion stack.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public List<Integer> rightViewWithSkips(int n, int[] values, int[] left, int[] right) {
        if (n == 0) return new ArrayList<>();
        
        Map<Integer, Integer> view = new HashMap<>();
        int maxDepth = dfs(0, 0, values, left, right, view);
        
        List<Integer> result = new ArrayList<>();
        for (int d = 0; d <= maxDepth; d++) {
            if (view.containsKey(d)) {
                result.add(view.get(d));
            }
        }
        return result;
    }

    private int dfs(int u, int depth, int[] values, int[] left, int[] right, Map<Integer, Integer> view) {
        if (u == -1) return -1;

        // If valid and first time seeing this depth (since we go Right -> Left)
        if (values[u] >= 0 && !view.containsKey(depth)) {
            view.put(depth, values[u]);
        }

        int d1 = dfs(right[u], depth + 1, values, left, right, view);
        int d2 = dfs(left[u], depth + 1, values, left, right, view);
        
        return Math.max(depth, Math.max(d1, d2));
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

        Solution solution = new Solution();
        List<Integer> ans = solution.rightViewWithSkips(n, values, left, right);
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

# Increase recursion depth
sys.setrecursionlimit(200000)

def right_view_with_skips(n: int, values: list[int], left: list[int], right: list[int]) -> list[int]:
    if n == 0:
        return []
        
    view = {}
    max_depth = -1
    
    def dfs(u, depth):
        nonlocal max_depth
        if u == -1:
            return
            
        max_depth = max(max_depth, depth)
        
        if values[u] >= 0 and depth not in view:
            view[depth] = values[u]
            
        dfs(right[u], depth + 1)
        dfs(left[u], depth + 1)
        
    dfs(0, 0)
    
    result = []
    for d in range(max_depth + 1):
        if d in view:
            result.append(view[d])
            
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
    ans = right_view_with_skips(n, values, left, right)
    sys.stdout.write(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    int maxDepth = -1;
    void dfs(int u, int depth, const vector<int>& values, const vector<int>& left, const vector<int>& right, map<int, int>& view) {
        if (u == -1) return;

        maxDepth = max(maxDepth, depth);

        if (values[u] >= 0 && view.find(depth) == view.end()) {
            view[depth] = values[u];
        }

        dfs(right[u], depth + 1, values, left, right, view);
        dfs(left[u], depth + 1, values, left, right, view);
    }

public:
    vector<int> rightViewWithSkips(int n, const vector<int>& values,
                                   const vector<int>& left, const vector<int>& right) {
        if (n == 0) return {};

        map<int, int> view;
        maxDepth = -1;
        dfs(0, 0, values, left, right, view);

        vector<int> result;
        for (int d = 0; d <= maxDepth; d++) {
            if (view.count(d)) {
                result.push_back(view[d]);
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
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.rightViewWithSkips(n, values, left, right);
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
  rightViewWithSkips(n, values, left, right) {
    if (n === 0) return [];

    const view = new Map();
    let maxDepth = -1;

    const dfs = (u, depth) => {
      if (u === -1) return;

      if (depth > maxDepth) maxDepth = depth;

      if (values[u] >= 0 && !view.has(depth)) {
        view.set(depth, values[u]);
      }

      dfs(right[u], depth + 1);
      dfs(left[u], depth + 1);
    };

    dfs(0, 0);

    const result = [];
    for (let d = 0; d <= maxDepth; d++) {
      if (view.has(d)) {
        result.push(view.get(d));
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
  const ans = solution.rightViewWithSkips(n, values, left, right);
  console.log(ans.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
10 1 2
-6 3 -1
14 -1 -1
7 -1 -1
```
**Tree:**
- 0(10) -> L:1(-6), R:2(14)
- 1(-6) -> L:3(7), R:-1
- 2(14) -> Leaf
- 3(7) -> Leaf

**DFS (Root -> Right -> Left):**
1.  **Node 0 (10, d=0):** Valid. Map: `{0: 10}`.
2.  **Node 2 (14, d=1):** Valid. Map: `{0: 10, 1: 14}`.
3.  **Node 1 (-6, d=1):** Invalid (Negative). Skip map update.
    -   Recurse Right (null).
    -   Recurse Left (Node 3).
4.  **Node 3 (7, d=2):** Valid. Map: `{0: 10, 1: 14, 2: 7}`.

**Result:** `10 14 7`.

## ✅ Proof of Correctness

DFS traversal order `Root -> Right -> Left` ensures that for any depth `d`, the first node we encounter is the rightmost node at that depth.
-   We add the condition `values[u] >= 0` to filter.
-   We add the condition `!view.containsKey(depth)` to ensure we only pick the *first* valid node (the rightmost one).
-   This correctly implements the "Right View with Skips" logic.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Left View**
    -   Same logic, but traverse `Root -> Left -> Right`.
-   **Extension 2: Max Value View**
    -   Instead of rightmost, find max value at each level.
-   **Extension 3: Diagonal View**
    -   Group by `depth - col`.

### Common Mistakes to Avoid

1.  **Skipping Traversal:**
    -   ❌ `if (val < 0) return;`
    -   ✅ Negative nodes can have positive children. Must continue traversal.
2.  **Map Overwrite:**
    -   ❌ Overwriting map entry with left children.
    -   ✅ Only write if key doesn't exist.

## Related Concepts

-   **Tree Views**
-   **DFS vs BFS**
-   **Recursion**
