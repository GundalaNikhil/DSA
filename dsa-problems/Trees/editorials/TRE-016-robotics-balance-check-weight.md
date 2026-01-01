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


### Python


### C++


### JavaScript


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

