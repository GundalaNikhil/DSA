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


### Python


### C++


### JavaScript


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

### Common Mistakes to Avoid

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
