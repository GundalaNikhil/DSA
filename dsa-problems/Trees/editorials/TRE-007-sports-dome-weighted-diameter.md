---
problem_id: TRE_SPORTS_DOME_WEIGHTED_DIAMETER__9532
display_id: TRE-007
slug: sports-dome-weighted-diameter
title: "Sports Dome Weighted Diameter"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - DFS
  - Tree Diameter
tags:
  - trees
  - diameter
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-007: Sports Dome Weighted Diameter

## 📋 Problem Summary

Given a binary tree where edges have non-negative weights, find the **weighted diameter**. The weighted diameter is defined as the maximum total edge weight along any simple path between two nodes in the tree. The path does not necessarily need to pass through the root.

## 🌍 Real-World Scenario

**Scenario Title:** Fiber Optic Cable Latency

Imagine a network of servers connected by fiber optic cables in a tree topology. Each cable has a specific length (weight), which corresponds to latency. To optimize the network or determine the worst-case communication delay, you need to find the two servers that are "furthest apart" in terms of total cable length. This maximum distance is the weighted diameter of the network.

![Real-World Application](../images/TRE-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1
     / \
(2) /   \ (3)
   2     3
        /
   (1) /
      4
```
**Weights:**
-   1 -> 2: Weight 2
-   1 -> 3: Weight 3
-   3 -> 4: Weight 1

**Paths:**
-   2 -> 1 -> 3: Weight 2 + 3 = 5.
-   2 -> 1 -> 3 -> 4: Weight 2 + 3 + 1 = 6.
-   1 -> 3 -> 4: Weight 3 + 1 = 4.

**Diameter:** 6 (Path 2 -> 4).

### Algorithm Steps

1.  For any node `u`, the longest path passing through `u` (where `u` is the highest node in the path) is formed by combining the longest downward path in its left subtree and the longest downward path in its right subtree.
2.  Let `maxDepth(u)` be the maximum weight of a path starting at `u` and going down to a leaf.
    -   `maxDepth(u) = max(weight(u->left) + maxDepth(left), weight(u->right) + maxDepth(right))`.
3.  The diameter passing through `u` is `(weight(u->left) + maxDepth(left)) + (weight(u->right) + maxDepth(right))`.
4.  We compute `maxDepth` using DFS. During the DFS, we update a global `maxDiameter` variable with the diameter passing through the current node.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Weights:** Non-negative integers.
-   **Empty Tree:** Diameter is 0.
-   **Single Node:** Diameter is 0.
-   **Result Type:** Can exceed 32-bit integer, use `long` (64-bit).

## Naive Approach

### Intuition

For every node `u`, calculate the longest path starting at `u` using BFS/DFS. Then find the max distance between any pair `(u, v)`.

### Algorithm

1.  For each node `i` from `0` to `n-1`:
    -   Run BFS starting at `i` to find the furthest node `j`.
    -   Record distance `dist(i, j)`.
2.  Return max distance found.

### Time Complexity

-   **O(N^2)**: BFS takes O(N), run N times.

## Optimal Approach (DFS)

### Key Insight

We can compute the diameter in a single bottom-up traversal (Post-order DFS). For every node, if we know the max downward lengths of its left and right branches, we can calculate:
1.  The longest path passing *through* this node (Left Branch + Right Branch).
2.  The longest path starting *at* this node and going down (max(Left Branch, Right Branch)).

### Algorithm

1.  Global `ans = 0`.
2.  `dfs(u)`:
    -   If `u == -1`, return 0.
    -   `leftMax = dfs(left[u])`.
    -   `rightMax = dfs(right[u])`.
    -   `leftPath = (left[u] != -1) ? leftMax + weightLeft : 0`.
    -   `rightPath = (right[u] != -1) ? rightMax + weightRight : 0`.
    -   `ans = max(ans, leftPath + rightPath)`.
    -   Return `max(leftPath, rightPath)`.

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(H)**: Recursion stack depth.

## Implementations

### Java
```java
import java.io.*;
import java.util.*;

class Solution {
    private long maxDiameter = 0;

    public long weightedDiameter(int n, int[] left, int[] right, long[] lw, long[] rw) {
        if (n == 0) return 0;
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

        maxDiameter = 0;
        dfs(root, left, right, lw, rw);
        return maxDiameter;
    }

    private long dfs(int u, int[] left, int[] right, long[] lw, long[] rw) {
        if (u == -1) return 0;
        long lPath = 0;
        long rPath = 0;
        if (left[u] != -1) {
            lPath = lw[u] + dfs(left[u], left, right, lw, rw);
        }
        if (right[u] != -1) {
            rPath = rw[u] + dfs(right[u], left, right, lw, rw);
        }
        if (lPath + rPath > maxDiameter) {
            maxDiameter = lPath + rPath;
        }
        return Math.max(lPath, rPath);
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
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];

        for (int i = 0; i < n && i + 1 < lines.size(); i++) {
            String[] parts = lines.get(i + 1).split("\\s+");
            if (parts.length < 3) continue;
            left[i] = Integer.parseInt(parts[1]);
            right[i] = Integer.parseInt(parts[2]);
            if (parts.length >= 5) {
                lw[i] = Long.parseLong(parts[3]);
                rw[i] = Long.parseLong(parts[4]);
            } else {
                lw[i] = 1;
                rw[i] = 1;
            }
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
    }
}
```

### Python
```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def weighted_diameter(n: int, left: list[int], right: list[int], lw: list[int], rw: list[int]) -> int:
    if n == 0:
        return 0
        
    max_diameter = 0
    
    def dfs(u):
        nonlocal max_diameter
        if u == -1:
            return 0
            
        l_path = 0
        r_path = 0
        
        if left[u] != -1:
            l_path = lw[u] + dfs(left[u])
        if right[u] != -1:
            r_path = rw[u] + dfs(right[u])
            
        max_diameter = max(max_diameter, l_path + r_path)
        
        return max(l_path, r_path)
        
    # Find root - node with no incoming edges (no parent)
    has_parent = [False] * n
    for i in range(n):
        if left[i] != -1: has_parent[left[i]] = True
        if right[i] != -1: has_parent[right[i]] = True
        
    root = 0
    for i in range(n):
        if not has_parent[i]:
            root = i
            break
            
    dfs(root)
    return max_diameter

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    valid_lines = [l.strip() for l in lines if l.strip()]
    if not valid_lines: return
    iterator = iter(valid_lines)
    
    try:
        n = int(next(iterator))
        left = [0] * n
        right = [0] * n
        lw = [0] * n
        rw = [0] * n
        
        for i in range(n):
            line = next(iterator)
            parts = list(map(int, line.split()))
            left[i] = parts[1]
            right[i] = parts[2]
            if len(parts) >= 5:
                lw[i] = parts[3]
                rw[i] = parts[4]
            else:
                lw[i] = 1
                rw[i] = 1
                
        print(weighted_diameter(n, left, right, lw, rw))
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

using namespace std;

class Solution {
    long long maxDiameter = 0;

    long long dfs(int u, const vector<int>& left, const vector<int>& right,
                  const vector<long long>& lw, const vector<long long>& rw) {
        if (u == -1) return 0;
        long long lPath = 0;
        long long rPath = 0;
        if (left[u] != -1) {
            lPath = lw[u] + dfs(left[u], left, right, lw, rw);
        }
        if (right[u] != -1) {
            rPath = rw[u] + dfs(right[u], left, right, lw, rw);
        }
        if (lPath + rPath > maxDiameter) {
            maxDiameter = lPath + rPath;
        }
        return lPath > rPath ? lPath : rPath;
    }

public:
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right,
                               const vector<long long>& lw, const vector<long long>& rw) {
        if (n == 0) return 0;
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
        maxDiameter = 0;
        dfs(root, left, right, lw, rw);
        return maxDiameter;
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
    vector<int> left(n, -1), right(n, -1);
    vector<long long> lw(n, 1), rw(n, 1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        left[i] = (int)parts[1];
        right[i] = (int)parts[2];
        if (parts.size() >= 5) {
            lw[i] = parts[3];
            rw[i] = parts[4];
        }
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << "\n";
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
if (n === 0) {
  console.log("0");
  process.exit(0);
}

const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);
const lw = new Array(n).fill(1);
const rw = new Array(n).fill(1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  left[i] = parts[1];
  right[i] = parts[2];
  if (parts.length >= 5) {
    lw[i] = parts[3];
    rw[i] = parts[4];
  }
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

const stack = [root];
const order = [];
const visited = new Array(n).fill(false);
visited[root] = true;

while (stack.length > 0) {
  const u = stack.pop();
  order.push(u);
  const l = left[u];
  const r = right[u];
  if (l !== -1 && !visited[l]) {
    visited[l] = true;
    stack.push(l);
  }
  if (r !== -1 && !visited[r]) {
    visited[r] = true;
    stack.push(r);
  }
}

const dist = new Array(n).fill(0);
let maxDiameter = 0;
for (let i = order.length - 1; i >= 0; i--) {
  const u = order[i];
  let lPath = 0;
  let rPath = 0;
  if (left[u] !== -1) lPath = lw[u] + dist[left[u]];
  if (right[u] !== -1) rPath = rw[u] + dist[right[u]];
  const dia = lPath + rPath;
  if (dia > maxDiameter) maxDiameter = dia;
  dist[u] = lPath > rPath ? lPath : rPath;
}

console.log(maxDiameter.toString());
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
1 1 2 3 1
2 3 -1 2 0
3 -1 -1 0 0
4 -1 -1 0 0
```
**Tree:**
- 0(1) -> L:1(2, w=3), R:2(3, w=1)
- 1(2) -> L:3(4, w=2), R:-1
- 2(3) -> Leaf
- 3(4) -> Leaf

**Execution:**
1.  `dfs(0)`
    -   `dfs(1)` (Left of 0, weight 3)
        -   `dfs(3)` (Left of 1, weight 2)
            -   Returns 0.
            -   `lPath = 2 + 0 = 2`. `rPath = 0`.
            -   `maxDiameter = max(0, 2) = 2`.
            -   Returns 2.
        -   `lPath = 3 + 2 = 5`. `rPath = 0`.
        -   `maxDiameter = max(2, 5) = 5`.
        -   Returns 5.
    -   `dfs(2)` (Right of 0, weight 1)
        -   Returns 0.
        -   `lPath = 0`. `rPath = 0`.
        -   Returns 0.
    -   `dfs(1)` returns 2.
    -   Back at `dfs(0)`: `lPath = 3 + dfs(1) = 3 + 2 = 5`.
    -   `rPath = 1 + dfs(2) = 1 + 0 = 1`.
    -   `maxDiameter = max(5, 5 + 1) = 6`.
    -   Returns 5.

**Output:** `6`. Correct.

## ✅ Proof of Correctness

The diameter of a tree is the longest path between any two nodes.
Any simple path in a tree has a unique highest node (the Lowest Common Ancestor of the endpoints).
By iterating over every node `u` and calculating the longest path passing through `u` (which is `LongestDownLeft + LongestDownRight`), and taking the maximum over all `u`, we guarantee finding the global maximum.
Our DFS computes `LongestDown` for every node and updates the global maximum in the same pass.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Unweighted Diameter**
    -   Same logic, weights = 1.
-   **Extension 2: Path Output**
    -   Reconstruct the actual path nodes. (Store `maxChild` pointers).
-   **Extension 3: Center of Tree**
    -   Find node(s) that minimize the max distance to any other node.

### Common Mistakes to Avoid

1.  **Edge Weights vs Node Values:**
    -   ❌ Adding node values.
    -   ✅ Problem specifies edge weights.
2.  **Negative Weights:**
    -   ❌ Dijkstra doesn't work with negative edges (though tree DP still works).
    -   ✅ Problem says non-negative.
3.  **Global Variable:**
    -   ❌ Forgetting to reset `maxDiameter` between test cases (if static).

## Related Concepts

-   **Tree DP**
-   **Longest Path in DAG**
