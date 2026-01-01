---
problem_id: TRE_AUDITORIUM_TOP_VIEW_HEIGHT__5601
display_id: TRE-010
slug: auditorium-top-view-height
title: "Auditorium Top View With Height Bonus"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - top-view
  - bfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-010: Auditorium Top View With Height Bonus

## 📋 Problem Summary

Find the **Top View** of a binary tree. The top view consists of the nodes visible when looking at the tree from directly above.
-   Nodes are grouped by horizontal distance (column).
-   For each column, the visible node is the one with the **smallest depth** (highest up).
-   **Tie-Breaker:** If multiple nodes in the same column have the same depth, choose the one with the **largest value**.

## 🌍 Real-World Scenario

**Scenario Title:** City Skyline

Imagine a city where buildings (nodes) are located at different horizontal coordinates (columns).
-   When viewed from a satellite (top view), you only see the roof of the tallest building at each coordinate.
-   In this tree analogy, "tallest" means "smallest depth" (closest to the root/sky).
-   If two buildings are at the same location and same height (depth), imagine they are stacked or merged, and the one with the "Height Bonus" (largest value) is the one that represents that spot on the map.

![Real-World Application](../images/TRE-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1
     / \
    2   3
     \
      4
       \
        5
```
**Columns:**
-   **Col 0:** Node 1 (Depth 0).
-   **Col -1:** Node 2 (Depth 1).
-   **Col 1:** Node 3 (Depth 1).
-   **Col 0:** Node 4 (Depth 2). (Blocked by Node 1).
-   **Col 1:** Node 5 (Depth 3). (Blocked by Node 3).

**Visible Nodes:**
-   Col -1: 2
-   Col 0: 1
-   Col 1: 3

**Output:** `2 1 3`

### Algorithm Steps

1.  **BFS Traversal:** Use a queue to store `(node, col, depth)`.
2.  **Tracking:** Use a Map `col -> {minDepth, maxValue}`.
3.  **Update Logic:** For each node `u` at `col` and `depth`:
    -   If `col` is not in map, add `u`.
    -   If `col` is in map:
        -   If `depth < currentMinDepth`, update (found a higher node).
        -   If `depth == currentMinDepth` AND `val > currentMaxVal`, update (tie-breaker).
4.  **Output:** Sort map keys (columns) and print values.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Root Column:** 0.
-   **Left Child:** `col - 1`.
-   **Right Child:** `col + 1`.
-   **Tie-Breaker:** Only applies if depths are *exactly* equal. Usually, BFS guarantees we see smaller depths first, but nodes at the same depth can appear in any order depending on tree structure (e.g., left child of right node vs right child of left node).

## Naive Approach

### Intuition

DFS can visit nodes in any order. We can collect all nodes into a list `(col, depth, val)`, sort them, and pick the best one for each column.

### Algorithm

1.  DFS to collect all nodes.
2.  Group by column.
3.  For each column, sort by `depth` asc, then `val` desc.
4.  Pick first.

### Time Complexity

-   **O(N log N)**: Sorting.

## Optimal Approach (BFS)

BFS naturally visits nodes level by level (depth 0, then 1, etc.).
-   The **first** time we encounter a column `C`, that node is guaranteed to have the minimal depth for that column.
-   **Exception:** If multiple nodes at the *same* depth map to the same column, BFS will visit them in sequence. We must check the tie-breaker (max value).
-   Nodes at *greater* depths will be visited later and can be ignored (since depth is strictly greater).

### Algorithm

1.  Queue `q` stores `(u, col)`.
2.  Map `topView` stores `col -> {val, depth}`.
3.  BFS:
    -   Pop `(u, c)`.
    -   If `c` not in `topView`: store `(val, depth)`.
    -   Else if `depth == storedDepth`: update if `val > storedVal`.
    -   (Note: BFS guarantees `depth >= storedDepth`. We never find a smaller depth later).
4.  Iterate `minCol` to `maxCol` and print.

### Time Complexity

-   **O(N)**: BFS visits each node once. Map operations O(1) or O(log N). Sorting columns takes O(K log K) where K is width (K <= N).

### Space Complexity

-   **O(N)**: Queue and Map.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
1 1 2
2 3 -1
3 -1 4
4 -1 -1
5 -1 -1
```
**Tree:**
- 0(1) -> L:1(2), R:2(3)
- 1(2) -> L:3(4), R:-1
- 2(3) -> L:-1, R:4(5)

**BFS:**
1.  `(0, c=0, d=0)` -> Map: `{0: (1, 0)}`.
2.  `(1, c=-1, d=1)` -> Map: `{0: (1, 0), -1: (2, 1)}`.
3.  `(2, c=1, d=1)` -> Map: `{0: (1, 0), -1: (2, 1), 1: (3, 1)}`.
4.  `(3, c=-2, d=2)` -> Map: `{..., -2: (4, 2)}`.
5.  `(4, c=2, d=2)` -> Map: `{..., 2: (5, 2)}`.

**Sorted Columns:** -2, -1, 0, 1, 2.
**Values:** 4, 2, 1, 3, 5.

## ✅ Proof of Correctness

BFS visits nodes in non-decreasing order of depth.
-   When we first see column `C`, we are at the minimum possible depth for that column (since any future visit will have `depth >= current`).
-   We only update if `depth == minDepth` and `val > currentMax`.
-   This correctly implements the "smallest depth, then largest value" logic.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Bottom View**
    -   Last node seen in each column (max depth).
-   **Extension 2: Left/Right View**
    -   First/Last node in each *level* (not column).
-   **Extension 3: Vertical Sum**
    -   Sum of all nodes in each column.

### Common Mistakes to Avoid

1.  **DFS Order:**
    -   ❌ Using DFS without tracking depth carefully. DFS might visit a deeper node before a shallower one in the same column.
    -   ✅ BFS is safer. If using DFS, must check depth explicitly.
2.  **Tie-Breaker:**
    -   ❌ Forgetting the `val > maxVal` check for equal depths.

## Related Concepts

-   **BFS**
-   **Vertical Traversal**
-   **TreeMap / Hashing**
