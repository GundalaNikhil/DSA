---
problem_id: TRE_ROBOTICS_BALANCE_CHECK_WEIGHT__6280
display_id: TRE-016
slug: robotics-balance-check-weight
title: "Robotics Balance Check with Weight Limit"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - DFS
  - Balance
tags:
  - trees
  - balance
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-016: Robotics Balance Check with Weight Limit

## 📋 Problem Summary

Determine if a binary tree is "balanced" based on two criteria that must hold for **every node**:
1.  **Height Balance:** The height difference between the left and right subtrees is at most 1.
2.  **Weight Balance:** The absolute difference between the **total weight** of the left subtree and the right subtree is at most `W`.

## 🌍 Real-World Scenario

**Scenario Title:** Kinetic Mobile Sculpture

Imagine a hanging mobile art piece (like those found in cribs or museums).
-   **Height Balance:** Ensures the structure isn't lopsided visually (one side dragging on the floor).
-   **Weight Balance:** Ensures the pivot point doesn't snap or tilt excessively due to uneven mass distribution.
-   **Goal:** Verify that every joint (node) in the sculpture satisfies both structural integrity (weight) and aesthetic (height) constraints.

![Real-World Application](../images/TRE-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      10 (w=5)
     /  \
    2    3 (w=2)
   (w=4)
```
**Weights:**
-   Left Subtree (Node 2): Total Weight = 4. Height = 1.
-   Right Subtree (Node 3): Total Weight = 2. Height = 1.

**Check Root:**
1.  **Height Diff:** `|1 - 1| = 0`. (<= 1) OK.
2.  **Weight Diff:** `|4 - 2| = 2`.
    -   If `W >= 2`, OK.
    -   If `W < 2`, Fail.

### Algorithm Steps

We need to compute two properties for every node: **Height** and **Total Subtree Weight**.
Instead of calculating these separately for every node (which would be slow), we can compute them **bottom-up**.

1.  **DFS Function:** Returns a tuple/object `{height, totalWeight, isBalanced}`.
2.  **Base Case:** Null node returns `{0, 0, true}`.
3.  **Recursive Step:**
    -   Call DFS on Left Child -> `{hL, wL, balL}`.
    -   Call DFS on Right Child -> `{hR, wR, balR}`.
4.  **Validation:**
    -   `isBalanced = balL && balR` (Children must be balanced).
    -   `&& abs(hL - hR) <= 1` (Height condition).
    -   `&& abs(wL - wR) <= W` (Weight condition).
5.  **Return:** `{max(hL, hR) + 1, wL + wR + node.weight, isBalanced}`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Total Weight:** Includes the node itself plus all descendants.
-   **Weight Diff:** Only compares the *subtrees* (left total vs right total), not including the current node's weight.
-   **Empty Tree:** Balanced.
-   **Leaf Node:** Balanced (Left 0, Right 0 -> Diff 0).

## Naive Approach

### Intuition

For each node, call `getHeight(node)` and `getWeight(node)`. Check conditions. Recurse.

### Time Complexity

-   **O(N^2)**: `getHeight` and `getWeight` take O(N). Calling them for every node results in quadratic time for skewed trees.

## Optimal Approach (Bottom-Up DFS)

Compute height and weight simultaneously as we return from recursion. This visits every node exactly once.

### Algorithm

1.  Define a helper function `check(u)` that returns `(height, weight)`.
2.  Use a global flag or return a special value (like -1 height) to indicate imbalance immediately.
3.  If `check(root)` is valid, return `true`.

### Time Complexity

-   **O(N)**: Single traversal.

### Space Complexity

-   **O(H)**: Recursion stack.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Result {
        int height;
        long weight;
        boolean balanced;

        Result(int h, long w, boolean b) {
            this.height = h;
            this.weight = w;
            this.balanced = b;
        }
    }

    public boolean isBalancedWeighted(int n, long[] weight, int[] left, int[] right, long W) {
        if (n == 0) return true;
        return dfs(0, weight, left, right, W).balanced;
    }

    private Result dfs(int u, long[] weight, int[] left, int[] right, long W) {
        if (u == -1) return new Result(0, 0, true);

        Result l = dfs(left[u], weight, left, right, W);
        if (!l.balanced) return new Result(0, 0, false); // Optimization: propagate failure

        Result r = dfs(right[u], weight, left, right, W);
        if (!r.balanced) return new Result(0, 0, false);

        boolean hBal = Math.abs(l.height - r.height) <= 1;
        boolean wBal = Math.abs(l.weight - r.weight) <= W;

        if (hBal && wBal) {
            return new Result(Math.max(l.height, r.height) + 1, l.weight + r.weight + weight[u], true);
        } else {
            return new Result(0, 0, false);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] weight = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            weight[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long W = 0;
        if (sc.hasNextLong()) W = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def is_balanced_weighted(n: int, weight: list[int], left: list[int], right: list[int], W: int) -> bool:
    if n == 0:
        return True
        
    # Returns (height, total_weight, is_balanced)
    def dfs(u):
        if u == -1:
            return 0, 0, True
            
        h_l, w_l, bal_l = dfs(left[u])
        if not bal_l:
            return 0, 0, False
            
        h_r, w_r, bal_r = dfs(right[u])
        if not bal_r:
            return 0, 0, False
            
        h_bal = abs(h_l - h_r) <= 1
        w_bal = abs(w_l - w_r) <= W
        
        if h_bal and w_bal:
            return max(h_l, h_r) + 1, w_l + w_r + weight[u], True
        else:
            return 0, 0, False

    return dfs(0)[2]

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    weight = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        weight[i] = int(data[idx]); idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
    W = int(data[idx]) if idx < len(data) else 0
    
    print("true" if is_balanced_weighted(n, weight, left, right, W) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Result {
    int height;
    long long weight;
    bool balanced;
};

class Solution {
    Result dfs(int u, const vector<long long>& weight, const vector<int>& left, const vector<int>& right, long long W) {
        if (u == -1) return {0, 0, true};

        Result l = dfs(left[u], weight, left, right, W);
        if (!l.balanced) return {0, 0, false};

        Result r = dfs(right[u], weight, left, right, W);
        if (!r.balanced) return {0, 0, false};

        bool hBal = abs(l.height - r.height) <= 1;
        bool wBal = abs(l.weight - r.weight) <= W;

        if (hBal && wBal) {
            return {max(l.height, r.height) + 1, l.weight + r.weight + weight[u], true};
        } else {
            return {0, 0, false};
        }
    }

public:
    bool isBalancedWeighted(int n, const vector<long long>& weight,
                            const vector<int>& left, const vector<int>& right, long long W) {
        if (n == 0) return true;
        return dfs(0, weight, left, right, W).balanced;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> weight(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i] >> left[i] >> right[i];
    }
    long long W;
    cin >> W;

    Solution solution;
    cout << (solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  isBalancedWeighted(n, weight, left, right, W) {
    if (n === 0) return true;

    const dfs = (u) => {
      if (u === -1) return { height: 0, weight: 0n, balanced: true };

      const l = dfs(left[u]);
      if (!l.balanced) return { height: 0, weight: 0n, balanced: false };

      const r = dfs(right[u]);
      if (!r.balanced) return { height: 0, weight: 0n, balanced: false };

      const hDiff = Math.abs(l.height - r.height);
      let wDiff = l.weight - r.weight;
      if (wDiff < 0n) wDiff = -wDiff;

      const hBal = hDiff <= 1;
      const wBal = wDiff <= BigInt(W);

      if (hBal && wBal) {
        return {
          height: Math.max(l.height, r.height) + 1,
          weight: l.weight + r.weight + BigInt(weight[u]),
          balanced: true,
        };
      } else {
        return { height: 0, weight: 0n, balanced: false };
      }
    };

    return dfs(0).balanced;
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
  const weight = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    weight[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const W = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
1 1 2
2 -1 -1
1 -1 -1
1
```
**Tree:**
- 0(w=1) -> L:1(w=2), R:2(w=1)
**W = 1**

**DFS:**
1.  **Node 1 (Leaf):**
    -   L: {0, 0, true}, R: {0, 0, true}
    -   H-Diff: 0. W-Diff: 0.
    -   Return: {1, 2, true}.
2.  **Node 2 (Leaf):**
    -   L: {0, 0, true}, R: {0, 0, true}
    -   H-Diff: 0. W-Diff: 0.
    -   Return: {1, 1, true}.
3.  **Node 0 (Root):**
    -   L: {1, 2, true}, R: {1, 1, true}
    -   H-Diff: `|1-1| = 0`. OK.
    -   W-Diff: `|2-1| = 1`. 1 <= 1. OK.
    -   Return: {2, 4, true}.

**Result:** `true`.

## ✅ Proof of Correctness

The bottom-up approach ensures that for any node `u`, we have already validated and computed the properties of its subtrees.
-   If any subtree is unbalanced, the `balanced` flag propagates `false` upwards immediately.
-   If subtrees are balanced, we check the local condition at `u`.
-   This covers all nodes and conditions efficiently.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Count Imbalanced Nodes**
    -   Return number of nodes violating the property instead of boolean.
-   **Extension 2: Min Weight Adjustment**
    -   Minimum weight to add/subtract to make it balanced.
-   **Extension 3: Diameter**
    -   Compute diameter while checking balance.

### Common Mistakes to Avoid

1.  **Weight Calculation:**
    -   ❌ Forgetting to add `node.weight` to the total returned.
    -   ✅ `total = left + right + current`.
2.  **Condition Logic:**
    -   ❌ Checking `weight[left] - weight[right]` instead of subtree totals.
3.  **Overflow:**
    -   ❌ Using `int` for weight sums.
    -   ✅ Use `long`.

