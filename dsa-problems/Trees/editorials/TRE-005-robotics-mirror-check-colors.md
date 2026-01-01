---
problem_id: TRE_ROBOTICS_MIRROR_CHECK_COLORS__6729
display_id: TRE-005
slug: robotics-mirror-check-colors
title: "Robotics Mirror Check with Colors"
difficulty: Easy
difficulty_score: 32
topics:
  - Trees
  - Symmetry
  - BFS
tags:
  - trees
  - symmetry
  - bfs
  - easy
premium: true
subscription_tier: basic
---

# TRE-005: Robotics Mirror Check with Colors

## 📋 Problem Summary

You are given a binary tree where each node has a **value** and a **color** (0 or 1). You need to determine if the tree satisfies two conditions:
1.  **Structural & Value Symmetry:** The tree is a mirror image of itself in terms of structure and node values (standard "Symmetric Tree" problem).
2.  **Color Balance:** For every level of the tree, the collection (multiset) of colors in the left subtree must exactly match the collection of colors in the right subtree. Note that colors do *not* need to be in symmetric positions; only their counts at each level must match.

## 🌍 Real-World Scenario

**Scenario Title:** Robot Assembly Quality Control

Imagine a robot built with a left arm and a right arm.
-   **Symmetry:** The mechanical structure (joints, lengths) and component types (values) must be identical mirrors for the robot to be balanced.
-   **Color Balance:** The wiring or aesthetic panels (colors) might be distributed differently, but the *total inventory* of parts used on the left side must match the right side at each vertical level to ensure equal weight distribution or material usage.

![Real-World Application](../images/TRE-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
        1 (Root)
      /   \
     2     2
    / \   / \
   3   4 4   3
```
**Values:** Symmetric. (2==2, 3==3, 4==4).
**Colors:**
-   Root: Irrelevant (center).
-   Level 1: Left Node (Color 0), Right Node (Color 0). Match? Yes.
-   Level 2:
    -   Left Subtree Nodes: [Color 1, Color 0]
    -   Right Subtree Nodes: [Color 0, Color 1]
    -   Multisets: {0, 1} vs {0, 1}. Match? Yes.

**Result:** True.

### Algorithm Steps

1.  **Symmetry Check:**
    -   Use a recursive helper `isMirror(node1, node2)`.
    -   Check if `node1.val == node2.val`.
    -   Recurse: `isMirror(node1.left, node2.right)` AND `isMirror(node1.right, node2.left)`.
2.  **Color Balance Check:**
    -   Perform a traversal (BFS is easiest) on the Left Subtree and Right Subtree separately.
    -   For each level, count the number of 0s and 1s in the Left Subtree.
    -   Compare with the counts in the Right Subtree.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Empty Tree:** Returns `true`.
-   **Color Constraint:** Colors are only 0 or 1. This simplifies the multiset check to just counting sums.
-   **Symmetry:** `left.left` matches `right.right`, `left.right` matches `right.left`.

## Naive Approach

### Intuition

Run two completely separate checks. First, run the standard `isSymmetric` algorithm. If it passes, run a Level Order Traversal on the left child and right child separately, storing colors level-by-level, and compare them.

### Algorithm

1.  If `!isSymmetric(root)`, return `false`.
2.  `leftColors = getLevelColors(root.left)`.
3.  `rightColors = getLevelColors(root.right)`.
4.  Compare `leftColors` and `rightColors`.

### Time Complexity

-   **O(N)**: Both checks visit all nodes.

### Space Complexity

-   **O(N)**: To store levels.

## Optimal Approach (Single Pass / Combined)

We can combine logic, but keeping them separate is cleaner and has the same asymptotic complexity. Since we need to check level-wise properties for colors, BFS is very natural. We can run a BFS that processes the left and right subtrees in parallel (or just level-by-level for the whole tree) but distinguishing left-side nodes from right-side nodes is tricky in a single queue unless we track it.

1.  **Check Symmetry (DFS):** Standard recursive check.
2.  **Check Colors (BFS):**
    -   Queue `qLeft` for root.left, `qRight` for root.right.
    -   At each step, process full level of `qLeft` and `qRight`.
    -   Sum colors in `qLeft` batch. Sum colors in `qRight` batch.
    -   If sums differ (or counts differ), return `false`.

### Time Complexity

-   **O(N)**.

### Space Complexity

-   **O(W)**: Width of tree.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
7
4 0 1 2
2 1 3 4
2 1 5 6
1 0 -1 -1
3 1 -1 -1
3 1 -1 -1
1 0 -1 -1
```

**Structure:**
- Root(4,0) -> L(2,1), R(2,1)
- L -> L(1,0), R(3,1)
- R -> L(3,1), R(1,0)

**Symmetry Check:**
- `val(L) == val(R)` (2==2). OK.
- `L.left(1)` vs `R.right(1)`. Values 1==1. OK.
- `L.right(3)` vs `R.left(3)`. Values 3==3. OK.
- Symmetry Passed.

**Color Check:**
- **Level 1:** `qL=[1]`, `qR=[2]`.
  - `sumL = color[1] = 1`.
  - `sumR = color[2] = 1`.
  - Match.
  - `qL` adds children of 1: 3, 4.
  - `qR` adds children of 2: 5, 6.
- **Level 2:** `qL=[3, 4]`, `qR=[5, 6]`.
  - `sumL = color[3] + color[4] = 0 + 1 = 1`.
  - `sumR = color[5] + color[6] = 1 + 0 = 1`.
  - Match.
- **Level 3:** Empty.

**Result:** `true`.

## ✅ Proof of Correctness

1.  **Symmetry:** Standard recursive check ensures structural and value mirroring.
2.  **Color Balance:** BFS ensures we process nodes level by level. By summing colors (since they are 0/1) or using a frequency map (for general colors), we verify the multiset condition. Since we check every level, the condition is fully verified.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: General Colors**
    -   If colors were 0-100, use a `HashMap` or frequency array instead of `sum`.
-   **Extension 2: Foldable Tree**
    -   Check structure symmetry only (ignore values).
-   **Extension 3: Iterative Symmetry**
    -   Implement `isSymmetric` using a Queue/Stack instead of recursion.

### Common Mistakes to Avoid

1.  **Checking Colors in Symmetry Function:**
    -   ❌ `if (color[u] != color[v]) return false;`
    -   ✅ Problem says colors don't need to match node-for-node, only level-multiset.
2.  **Queue Sync:**
    -   ❌ Processing `qL` and `qR` at different rates.
    -   ✅ Must process exactly `size` nodes for both queues at each step.

