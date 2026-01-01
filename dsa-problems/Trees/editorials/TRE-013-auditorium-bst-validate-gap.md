---
problem_id: TRE_AUDITORIUM_BST_VALIDATE_GAP__6370
display_id: TRE-013
slug: auditorium-bst-validate-gap
title: "Auditorium BST Validate with Gap"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - BST
  - Validation
tags:
  - trees
  - bst
  - validation
  - medium
premium: true
subscription_tier: basic
---

# TRE-013: Auditorium BST Validate with Gap

## 📋 Problem Summary

Determine if a given binary tree is a valid **Binary Search Tree (BST)** that also satisfies a **Gap Rule**.
1.  **BST Property:** For every node, all values in the left subtree are strictly smaller, and all values in the right subtree are strictly larger.
2.  **Gap Rule:** For every parent-child edge, the absolute difference between their values must be at least `G`. That is, `|parent.val - child.val| >= G`.

## 🌍 Real-World Scenario

**Scenario Title:** Socially Distanced Seating

Imagine an auditorium seating chart arranged as a tree structure (e.g., a hierarchy of VIP sections).
-   **BST Property:** Ensures orderly seating by ticket number (smaller numbers left, larger numbers right).
-   **Gap Rule:** To maintain social distancing or security protocols, no two directly connected seats (parent and child) can have ticket numbers too close to each other. They must differ by at least `G`.

![Real-World Application](../images/TRE-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      10
     /  \
    5    15
```
**Gap G = 3**

**Checks:**
1.  **BST:**
    -   Left child 5 < 10. OK.
    -   Right child 15 > 10. OK.
2.  **Gap:**
    -   `|10 - 5| = 5`. 5 >= 3. OK.
    -   `|10 - 15| = 5`. 5 >= 3. OK.

**Result:** True.

**Invalid Case (G=6):**
-   `|10 - 5| = 5`. 5 < 6. **Fail**.

### Algorithm Steps

We can validate both properties simultaneously using a recursive approach (DFS).
-   Maintain a valid range `(min, max)` for the BST property.
-   For each node, check:
    1.  `min < node.val < max` (BST Check).
    2.  `|node.val - parent.val| >= G` (Gap Check - passed as parameter or checked before recursion).
-   Recurse left with range `(min, node.val)`.
-   Recurse right with range `(node.val, max)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Empty Tree:** Valid (True).
-   **Single Node:** Valid (True). Gap rule applies to edges, and there are none.
-   **Values:** Can be negative. Use `long` (64-bit) to prevent overflow during subtraction (though `abs` difference is safe if inputs fit in long).
-   **Strict BST:** No duplicate values allowed (implied by strict inequality).

## Naive Approach

### Intuition

1.  Perform Inorder Traversal to check if values are sorted strictly increasing (BST check).
2.  Perform any traversal (Preorder/BFS) to check the Gap Rule for every edge.

### Algorithm

1.  `inorder = []`. Traverse and collect.
2.  Check `inorder[i] < inorder[i+1]`. If not, return `false`.
3.  Traverse tree again. For each node `u`:
    -   If `u.left`: check `abs(u.val - u.left.val) >= G`.
    -   If `u.right`: check `abs(u.val - u.right.val) >= G`.
4.  Return `true` if all pass.

### Time Complexity

-   **O(N)**: Two passes.

## Optimal Approach (Single Pass DFS)

We can validate everything in one pass. The standard "Validate BST" algorithm passes down `min` and `max` limits. We simply add the Gap check at each step.

### Algorithm

1.  `validate(node, min, max)`:
    -   If `node` is null, return `true`.
    -   If `node.val <= min` or `node.val >= max`, return `false`.
    -   (Gap check is done relative to parent, but here we don't have parent easily unless passed. Alternatively, check children before recursing).
    -   Check Left Child:
        -   If `left` exists:
            -   `abs(node.val - left.val) < G` -> return `false`.
            -   Recurse `validate(left, min, node.val)`.
    -   Check Right Child:
        -   If `right` exists:
            -   `abs(node.val - right.val) < G` -> return `false`.
            -   Recurse `validate(right, node.val, max)`.
    -   Return `true` if all checks pass.

### Time Complexity

-   **O(N)**: Visit every node once.

### Space Complexity

-   **O(H)**: Recursion stack.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public boolean validateBSTGap(int n, long[] values, int[] left, int[] right, long G) {
        if (n == 0) return true;
        return validate(0, Long.MIN_VALUE, Long.MAX_VALUE, values, left, right, G);
    }

    private boolean validate(int u, long min, long max, long[] values, int[] left, int[] right, long G) {
        if (u == -1) return true;

        long val = values[u];
        // BST Check
        if (val <= min || val >= max) return false;

        // Left Child Check
        if (left[u] != -1) {
            long lVal = values[left[u]];
            if (Math.abs(val - lVal) < G) return false; // Gap Check
            if (!validate(left[u], min, val, values, left, right, G)) return false;
        }

        // Right Child Check
        if (right[u] != -1) {
            long rVal = values[right[u]];
            if (Math.abs(val - rVal) < G) return false; // Gap Check
            if (!validate(right[u], val, max, values, left, right, G)) return false;
        }

        return true;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long G = 0;
        if (sc.hasNextLong()) G = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.validateBSTGap(n, values, left, right, G) ? "true" : "false");
        sc.close();
    }
}
```

### Python
```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def validate_bst_gap(n: int, values: list[int], left: list[int], right: list[int], G: int) -> bool:
    if n == 0:
        return True
        
    def validate(u, min_val, max_val):
        if u == -1:
            return True
            
        val = values[u]
        # BST Check
        if val <= min_val or val >= max_val:
            return False
            
        # Left Child
        if left[u] != -1:
            l_val = values[left[u]]
            if abs(val - l_val) < G:
                return False
            if not validate(left[u], min_val, val):
                return False
                
        # Right Child
        if right[u] != -1:
            r_val = values[right[u]]
            if abs(val - r_val) < G:
                return False
            if not validate(right[u], val, max_val):
                return False
                
        return True

    return validate(0, float('-inf'), float('inf'))

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
    G = int(data[idx]) if idx < len(data) else 0
    
    print("true" if validate_bst_gap(n, values, left, right, G) else "false")

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

class Solution {
    bool validate(int u, long long minVal, long long maxVal, const vector<long long>& values,
                  const vector<int>& left, const vector<int>& right, long long G) {
        if (u == -1) return true;

        long long val = values[u];
        if (val <= minVal || val >= maxVal) return false;

        if (left[u] != -1) {
            long long lVal = values[left[u]];
            if (abs(val - lVal) < G) return false;
            if (!validate(left[u], minVal, val, values, left, right, G)) return false;
        }

        if (right[u] != -1) {
            long long rVal = values[right[u]];
            if (abs(val - rVal) < G) return false;
            if (!validate(right[u], val, maxVal, values, left, right, G)) return false;
        }

        return true;
    }

public:
    bool validateBSTGap(int n, const vector<long long>& values,
                        const vector<int>& left, const vector<int>& right, long long G) {
        if (n == 0) return true;
        return validate(0, numeric_limits<long long>::min(), numeric_limits<long long>::max(), values, left, right, G);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }
    long long G;
    cin >> G;

    Solution solution;
    cout << (solution.validateBSTGap(n, values, left, right, G) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  validateBSTGap(n, values, left, right, G) {
    if (n === 0) return true;
    
    const minInit = -BigInt("9223372036854775808"); // Min 64-bit signed
    const maxInit = BigInt("9223372036854775807");  // Max 64-bit signed
    
    const validate = (u, minVal, maxVal) => {
      if (u === -1) return true;
      
      const val = BigInt(values[u]);
      if (val <= minVal || val >= maxVal) return false;
      
      const gVal = BigInt(G);
      
      if (left[u] !== -1) {
        const lVal = BigInt(values[left[u]]);
        let diff = val - lVal;
        if (diff < 0n) diff = -diff;
        if (diff < gVal) return false;
        if (!validate(left[u], minVal, val)) return false;
      }
      
      if (right[u] !== -1) {
        const rVal = BigInt(values[right[u]]);
        let diff = val - rVal;
        if (diff < 0n) diff = -diff;
        if (diff < gVal) return false;
        if (!validate(right[u], val, maxVal)) return false;
      }
      
      return true;
    };
    
    return validate(0, minInit, maxInit);
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
  const G = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.validateBSTGap(n, values, left, right, G) ? "true" : "false");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3
5 1 2
1 -1 -1
7 -1 -1
2
```
**Tree:**
- 0(5) -> L:1(1), R:2(7)
**G = 2**

**Execution:**
1.  `validate(0, -inf, inf)`
    -   Val 5. OK.
    -   **Left:** Child 1(1).
        -   Gap: `|5 - 1| = 4`. 4 >= 2. OK.
        -   Recurse `validate(1, -inf, 5)`.
            -   Val 1. OK.
            -   No children. Return True.
    -   **Right:** Child 2(7).
        -   Gap: `|5 - 7| = 2`. 2 >= 2. OK.
        -   Recurse `validate(2, 5, inf)`.
            -   Val 7. OK.
            -   No children. Return True.
    -   Return True.

**Result:** `true`.

## ✅ Proof of Correctness

The algorithm checks two conditions:
1.  **BST Property:** By passing `(min, max)` ranges and updating them (`min` becomes `node.val` for right child, `max` becomes `node.val` for left child), we ensure every node falls within the valid range defined by its ancestors.
2.  **Gap Rule:** By checking `abs(node.val - child.val) >= G` for every edge, we ensure the local gap constraint is met.
Since we visit every node and edge exactly once, and the checks are local or propagated correctly, the validation is complete.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Fix One Swap**
    -   If the tree has exactly two nodes swapped (violating BST), find them.
-   **Extension 2: Largest Valid Subtree**
    -   Find the largest subtree that satisfies both conditions.
-   **Extension 3: Min Gap**
    -   Find the actual minimum gap in the entire tree (closest pair of values).

### Common Mistakes to Avoid

1.  **Integer Overflow:**
    -   ❌ Using `int` for values when constraints allow large numbers.
    -   ✅ Use `long` or `BigInt`.
2.  **Range Initialization:**
    -   ❌ Using small constants for infinity.
    -   ✅ Use `Long.MIN_VALUE` / `Long.MAX_VALUE`.
3.  **Gap Logic:**
    -   ❌ Checking gap between siblings instead of parent-child.


