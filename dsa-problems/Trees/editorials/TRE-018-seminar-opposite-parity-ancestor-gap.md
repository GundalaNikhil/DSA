---
problem_id: TRE_SEMINAR_OPPOSITE_PARITY_ANCESTOR_GAP__9157
display_id: TRE-018
slug: seminar-opposite-parity-ancestor-gap
title: "Seminar Opposite-Parity Ancestor Gap"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - DFS
  - Prefix Min/Max
tags:
  - trees
  - dfs
  - parity
  - medium
premium: true
subscription_tier: basic
---

# TRE-018: Seminar Opposite-Parity Ancestor Gap

## 📋 Problem Summary

For every node in a binary tree, calculate the absolute difference between its value and the value of any of its **ancestors** that have a **different depth parity**.
-   If a node is at an **odd** depth, compare it with ancestors at **even** depths.
-   If a node is at an **even** depth, compare it with ancestors at **odd** depths.
-   Find the **maximum** such difference across the entire tree.

## 🌍 Real-World Scenario

**Scenario Title:** Alternating Shift Handover

Imagine a company with a hierarchy of employees working alternating shifts (Day Shift vs Night Shift).
-   **Even Depth:** Day Shift Managers.
-   **Odd Depth:** Night Shift Managers.
-   **Goal:** Find the biggest "performance gap" (value difference) between an employee and any of their superiors who work the *opposite* shift. This helps identify disconnects between shifts in the chain of command.

![Real-World Application](../images/TRE-018/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      8 (Depth 0, Even)
     / \
    3   10 (Depth 1, Odd)
   / \   \
  1  14   4 (Depth 2, Even)
```
**Analysis:**
-   **Node 8 (Even):** No ancestors. Gap = 0.
-   **Node 3 (Odd):** Ancestor 8 (Even). `|3 - 8| = 5`.
-   **Node 10 (Odd):** Ancestor 8 (Even). `|10 - 8| = 2`.
-   **Node 1 (Even):** Ancestor 3 (Odd). `|1 - 3| = 2`. (8 is Even, ignore).
-   **Node 14 (Even):** Ancestor 3 (Odd). `|14 - 3| = 11`.
-   **Node 4 (Even):** Ancestor 10 (Odd). `|4 - 10| = 6`.

**Max Gap:** 11.

### Algorithm Steps

We need to track the **minimum** and **maximum** values seen so far for both **Even** and **Odd** depths as we traverse down the tree.

1.  **DFS State:** Pass `minEven`, `maxEven`, `minOdd`, `maxOdd` down the recursion.
2.  **Current Node:**
    -   If current depth is **Even**:
        -   Compare `val` with `minOdd` and `maxOdd` (if they exist).
        -   Update global max difference.
        -   Update `minEven` and `maxEven` for children.
    -   If current depth is **Odd**:
        -   Compare `val` with `minEven` and `maxEven` (if they exist).
        -   Update global max difference.
        -   Update `minOdd` and `maxOdd` for children.
3.  **Recurse:** Continue to children.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Initialization:** Use infinity/null to indicate "no ancestor found yet" for a specific parity.
-   **Root:** Depth 0 (Even). Has no ancestors, so contributes 0.
-   **Empty Tree:** Return 0.

## Naive Approach

### Intuition

For each node, walk up the parent pointers (or re-traverse from root) to find all ancestors. Check their depths and compute differences.

### Time Complexity

-   **O(N^2)**: In a skewed tree, path length is O(N). Doing this for N nodes is quadratic.

## Optimal Approach (DFS with State Tracking)

We can maintain the necessary ancestor information (min/max of each parity) in O(1) space as we traverse.

### Algorithm

1.  `globalMax = 0`.
2.  `dfs(node, depth, minEven, maxEven, minOdd, maxOdd)`:
    -   If `node` is null, return.
    -   If `depth % 2 == 0`:
        -   If `minOdd` is valid: `globalMax = max(globalMax, abs(val - minOdd), abs(val - maxOdd))`.
        -   Update `minEven = min(minEven, val)`, `maxEven = max(maxEven, val)`.
    -   Else (`depth % 2 != 0`):
        -   If `minEven` is valid: `globalMax = max(globalMax, abs(val - minEven), abs(val - maxEven))`.
        -   Update `minOdd = min(minOdd, val)`, `maxOdd = max(maxOdd, val)`.
    -   Recurse left and right.

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(H)**: Recursion stack.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    long maxDiff = 0;

    public long maxOppositeParityGap(int n, int[] values, int[] left, int[] right) {
        if (n == 0) return 0;
        maxDiff = 0;
        // Use null or special value to indicate "no ancestor".
        // Since values are int, we can use Long.MIN_VALUE/MAX_VALUE but need to be careful with logic.
        // Better: pass initialized flags or use objects.
        // Or simpler: root is depth 0. It sets the initial Even bounds.
        // Odd bounds are initially "empty".
        
        dfs(0, 0, values[0], values[0], Integer.MAX_VALUE, Integer.MIN_VALUE, values, left, right);
        return maxDiff;
    }

    // minE/maxE are valid because root is even.
    // minO/maxO might be invalid (sentinels).
    private void dfs(int u, int depth, int minE, int maxE, int minO, int maxO, int[] values, int[] left, int[] right) {
        if (u == -1) return;

        int val = values[u];

        if (depth % 2 == 0) {
            // Current is Even. Compare with Odd ancestors.
            if (minO != Integer.MAX_VALUE) {
                maxDiff = Math.max(maxDiff, Math.abs((long)val - minO));
                maxDiff = Math.max(maxDiff, Math.abs((long)val - maxO));
            }
            // Update Even bounds for children
            minE = Math.min(minE, val);
            maxE = Math.max(maxE, val);
        } else {
            // Current is Odd. Compare with Even ancestors.
            // Even ancestors always exist (root).
            maxDiff = Math.max(maxDiff, Math.abs((long)val - minE));
            maxDiff = Math.max(maxDiff, Math.abs((long)val - maxE));
            
            // Update Odd bounds for children
            minO = Math.min(minO, val);
            maxO = Math.max(maxO, val);
        }

        if (left[u] != -1) dfs(left[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
        if (right[u] != -1) dfs(right[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
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
        System.out.println(solution.maxOppositeParityGap(n, values, left, right));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def max_opposite_parity_gap(n: int, values: list[int], left: list[int], right: list[int]) -> int:
    if n == 0:
        return 0
        
    max_diff = 0
    
    # min_e, max_e, min_o, max_o
    # Use None for invalid
    
    def dfs(u, depth, min_e, max_e, min_o, max_o):
        nonlocal max_diff
        if u == -1:
            return
            
        val = values[u]
        
        if depth % 2 == 0:
            # Even depth: compare with Odd ancestors
            if min_o is not None:
                max_diff = max(max_diff, abs(val - min_o), abs(val - max_o))
            
            # Update Even bounds
            new_min_e = val if min_e is None else min(min_e, val)
            new_max_e = val if max_e is None else max(max_e, val)
            
            # Pass Odd bounds as is
            if left[u] != -1: dfs(left[u], depth + 1, new_min_e, new_max_e, min_o, max_o)
            if right[u] != -1: dfs(right[u], depth + 1, new_min_e, new_max_e, min_o, max_o)
            
        else:
            # Odd depth: compare with Even ancestors
            if min_e is not None:
                max_diff = max(max_diff, abs(val - min_e), abs(val - max_e))
                
            # Update Odd bounds
            new_min_o = val if min_o is None else min(min_o, val)
            new_max_o = val if max_o is None else max(max_o, val)
            
            # Pass Even bounds as is
            if left[u] != -1: dfs(left[u], depth + 1, min_e, max_e, new_min_o, new_max_o)
            if right[u] != -1: dfs(right[u], depth + 1, min_e, max_e, new_min_o, new_max_o)

    # Root is depth 0 (Even). Initialize Even bounds with root val. Odd bounds None.
    dfs(0, 0, values[0], values[0], None, None)
    return max_diff

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
    print(max_opposite_parity_gap(n, values, left, right))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

class Solution {
    long long maxDiff = 0;

    void dfs(int u, int depth, int minE, int maxE, int minO, int maxO,
             const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        if (u == -1) return;

        int val = values[u];

        if (depth % 2 == 0) {
            // Even
            if (minO != INT_MAX) {
                maxDiff = max(maxDiff, (long long)abs(val - minO));
                maxDiff = max(maxDiff, (long long)abs(val - maxO));
            }
            minE = min(minE, val);
            maxE = max(maxE, val);
        } else {
            // Odd
            if (minE != INT_MAX) {
                maxDiff = max(maxDiff, (long long)abs(val - minE));
                maxDiff = max(maxDiff, (long long)abs(val - maxE));
            }
            minO = min(minO, val);
            maxO = max(maxO, val);
        }

        if (left[u] != -1) dfs(left[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
        if (right[u] != -1) dfs(right[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
    }

public:
    long long maxOppositeParityGap(int n, const vector<int>& values,
                                   const vector<int>& left, const vector<int>& right) {
        if (n == 0) return 0;
        maxDiff = 0;
        // Root is depth 0 (Even).
        dfs(0, 0, values[0], values[0], INT_MAX, INT_MIN, values, left, right);
        return maxDiff;
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
    cout << solution.maxOppositeParityGap(n, values, left, right) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxOppositeParityGap(n, values, left, right) {
    if (n === 0) return 0;
    
    let maxDiff = 0;
    
    // Use null for uninitialized
    const dfs = (u, depth, minE, maxE, minO, maxO) => {
      if (u === -1) return;
      
      const val = values[u];
      
      let nextMinE = minE;
      let nextMaxE = maxE;
      let nextMinO = minO;
      let nextMaxO = maxO;
      
      if (depth % 2 === 0) {
        // Even
        if (minO !== null) {
          maxDiff = Math.max(maxDiff, Math.abs(val - minO));
          maxDiff = Math.max(maxDiff, Math.abs(val - maxO));
        }
        nextMinE = (minE === null) ? val : Math.min(minE, val);
        nextMaxE = (maxE === null) ? val : Math.max(maxE, val);
      } else {
        // Odd
        if (minE !== null) {
          maxDiff = Math.max(maxDiff, Math.abs(val - minE));
          maxDiff = Math.max(maxDiff, Math.abs(val - maxE));
        }
        nextMinO = (minO === null) ? val : Math.min(minO, val);
        nextMaxO = (maxO === null) ? val : Math.max(maxO, val);
      }
      
      if (left[u] !== -1) dfs(left[u], depth + 1, nextMinE, nextMaxE, nextMinO, nextMaxO);
      if (right[u] !== -1) dfs(right[u], depth + 1, nextMinE, nextMaxE, nextMinO, nextMaxO);
    };
    
    dfs(0, 0, values[0], values[0], null, null);
    return maxDiff;
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
  console.log(solution.maxOppositeParityGap(n, values, left, right).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
8 1 2
3 3 -1
10 -1 4
1 -1 -1
14 -1 -1
```
**Tree:**
- 0(8, Even) -> L:1(3, Odd), R:2(10, Odd)
- 1(3, Odd) -> L:3(1, Even), R:-1
- 2(10, Odd) -> L:-1, R:4(14, Even)

**DFS:**
1.  **Node 0 (8, E):** Init Even bounds `[8, 8]`. Odd `None`.
2.  **Node 1 (3, O):** Compare with Even `[8, 8]`. `|3-8|=5`. Max=5. Update Odd `[3, 3]`.
3.  **Node 3 (1, E):** Compare with Odd `[3, 3]`. `|1-3|=2`. Max=5. Update Even `[1, 8]`.
4.  **Node 2 (10, O):** Compare with Even `[8, 8]` (from root path). `|10-8|=2`. Max=5. Update Odd `[10, 10]`.
5.  **Node 4 (14, E):** Compare with Odd `[10, 10]`. `|14-10|=4`. Max=5.

**Result:** 5.

## ✅ Proof of Correctness

We maintain the min and max values of ancestors for both parities.
-   Since we need `max(|val - ancestor|)`, this is equivalent to `max(val - min_ancestor, max_ancestor - val)`.
-   By tracking `min` and `max` for both Even and Odd depths separately, we can perform this check in O(1) at each node against the correct parity set.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Modulo K**
    -   Generalize to depth `mod K`.
-   **Extension 2: Path Sum Parity**
    -   Parity based on sum of values from root, not depth.
-   **Extension 3: Closest Value**
    -   Find opposite-parity ancestor with value closest to current.

### C++ommon Mistakes to Avoid

1.  **Initialization:**
    -   ❌ Using 0 for min/max.
    -   ✅ Use Infinity or Null.
2.  **Parity Logic:**
    -   ❌ Comparing Even with Even.
    -   ✅ Ensure `depth % 2 != ancestor_depth % 2`.

## Related Concepts

-   **DFS**
-   **Prefix Min/Max**
-   **Tree Properties**
