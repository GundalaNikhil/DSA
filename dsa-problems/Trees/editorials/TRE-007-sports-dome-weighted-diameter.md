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
import java.util.*;

class Solution {
    long maxDiameter = 0;

    public long weightedDiameter(int n, int[] left, int[] right, long[] lw, long[] rw) {
        if (n == 0) return 0;
        maxDiameter = 0;
        dfs(0, left, right, lw, rw);
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

        maxDiameter = Math.max(maxDiameter, lPath + rPath);

        return Math.max(lPath, rPath);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] left = new int[n];
        int[] right = new int[n];
        long[] lw = new long[n];
        long[] rw = new long[n];
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
            lw[i] = sc.nextLong();
            rw[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.weightedDiameter(n, left, right, lw, rw));
        sc.close();
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
        
    dfs(0)
    return max_diameter

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    left = [0] * n
    right = [0] * n
    lw = [0] * n
    rw = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        lw[i] = int(data[idx]); idx += 1
        rw[i] = int(data[idx]); idx += 1
        
    print(weighted_diameter(n, left, right, lw, rw))

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

        maxDiameter = max(maxDiameter, lPath + rPath);

        return max(lPath, rPath);
    }

public:
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right,
                               const vector<long long>& lw, const vector<long long>& rw) {
        if (n == 0) return 0;
        maxDiameter = 0;
        dfs(0, left, right, lw, rw);
        return maxDiameter;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> left(n), right(n);
    vector<long long> lw(n), rw(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i] >> lw[i] >> rw[i];
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  weightedDiameter(n, left, right, lw, rw) {
    if (n === 0) return 0;
    
    let maxDiameter = 0n;
    
    const dfs = (u) => {
      if (u === -1) return 0n;
      
      let lPath = 0n;
      let rPath = 0n;
      
      if (left[u] !== -1) {
        lPath = BigInt(lw[u]) + dfs(left[u]);
      }
      if (right[u] !== -1) {
        rPath = BigInt(rw[u]) + dfs(right[u]);
      }
      
      const currentDiameter = lPath + rPath;
      if (currentDiameter > maxDiameter) {
        maxDiameter = currentDiameter;
      }
      
      return lPath > rPath ? lPath : rPath;
    };
    
    dfs(0);
    return maxDiameter;
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
  const left = new Array(n);
  const right = new Array(n);
  const lw = new Array(n);
  const rw = new Array(n);
  for (let i = 0; i < n; i++) {
    idx++; // value
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
    lw[i] = parseInt(data[idx++], 10);
    rw[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.weightedDiameter(n, left, right, lw, rw).toString());
});
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
    -   `lPath = 3 + 2 = 5` (Wait, `dfs(1)` returned 2? No, `dfs(1)` returned `max(lPath, rPath)`. `lPath` at node 1 was `2 + dfs(3) = 2`. `rPath` was 0. So `dfs(1)` returns 2.
    -   Wait, `dfs(1)`: `lPath = 2 + dfs(3)`. `dfs(3)` returns 0. So `lPath = 2`.
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

## Common Mistakes to Avoid

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
