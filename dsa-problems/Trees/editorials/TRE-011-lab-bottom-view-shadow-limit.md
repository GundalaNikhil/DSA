---
problem_id: TRE_LAB_BOTTOM_VIEW_SHADOW_LIMIT__3395
display_id: TRE-011
slug: lab-bottom-view-shadow-limit
title: "Lab Bottom View with Shadow Limit"
difficulty: Medium
difficulty_score: 50
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - bottom-view
  - bfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-011: Lab Bottom View with Shadow Limit

## 📋 Problem Summary

Find the **Bottom View** of a binary tree, but with a constraint: any node located deeper than depth `D` is considered "in the shadow" or "out of range" and cannot be part of the view.
-   Nodes are grouped by horizontal distance (column).
-   For each column, select the node with the **largest depth** that satisfies `depth <= D`.
-   If multiple nodes in the same column have the same maximal depth (within limit), the one visited **last** in a standard level-order traversal (rightmost) is typically chosen (or the problem implies "visible from bottom", so the last one covering the slot).

## 🌍 Real-World Scenario

**Scenario Title:** Underwater Sensor Array

Imagine a research vessel deploying sensors at various depths in the ocean.
-   **Horizontal Distance:** Location relative to the ship.
-   **Depth:** Distance below surface.
-   **Limit D:** The maximum depth sunlight can penetrate (or sonar range).

You want to map the "deepest visible object" at each horizontal location. Anything deeper than `D` is in the dark zone and shouldn't be reported. You need the deepest sensor reading that is still within the illuminated zone.

![Real-World Application](../images/TRE-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      1 (Depth 0)
     / \
    2   3 (Depth 1)
   / \
  4   5 (Depth 2)
```
**Limit D = 1**

**Columns:**
-   **Col 0:** Node 1 (Depth 0).
-   **Col -1:** Node 2 (Depth 1).
-   **Col 1:** Node 3 (Depth 1).
-   **Col -2:** Node 4 (Depth 2). **Ignored (Depth > 1)**.
-   **Col 0:** Node 5 (Depth 2). **Ignored (Depth > 1)**.

**Visible Nodes (Depth <= 1):**
-   Col -1: Node 2.
-   Col 0: Node 1. (Node 5 is ignored).
-   Col 1: Node 3.

**Output:** `2 1 3`

### Algorithm Steps

1.  **BFS Traversal:** Use a queue to store `(node, col, depth)`.
2.  **Tracking:** Use a Map `col -> {val, depth}`.
3.  **Update Logic:** For each node `u` at `col` and `depth`:
    -   If `depth > D`, **skip** processing (don't add to map, but still add children to queue? Yes, children might be deeper, but if `depth > D`, children are `depth+1 > D`, so we can actually stop traversing that branch entirely).
    -   If `depth <= D`, update `map[col] = {val, depth}`.
    -   Since BFS visits level by level, a later visit to the same column at the same or greater depth (but still `<= D`) will overwrite the previous value. This correctly captures the "bottom-most" (and right-most for ties) node.
4.  **Output:** Sort map keys (columns) and print values.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Stopping Condition:** If a node is at depth `D`, its children are at `D+1`. We can stop adding children to the queue if `depth == D`.
-   **Tie-Breaker:** Standard Bottom View usually takes the "last seen" node at the deepest level. BFS naturally handles this if we process left-to-right.
-   **Empty Tree:** Output empty line.

## Naive Approach

### Intuition

Traverse the entire tree using DFS, collect valid nodes, and filter.

### Algorithm

1.  DFS to collect all nodes `(col, depth, val)`.
2.  Filter list where `depth <= D`.
3.  Group by column.
4.  Sort each group by `depth` asc, then `arrival time` (or just update map).
5.  Pick last.

### Time Complexity

-   **O(N)**: Visit all nodes.

## Optimal Approach (BFS with Pruning)

BFS allows us to stop traversing a branch as soon as we hit depth `D`. This is an optimization: we don't even need to visit nodes deeper than `D`.

### Algorithm

1.  Queue `q` stores `(u, col, depth)`.
2.  Map `bottomView` stores `col -> val`.
3.  BFS:
    -   Pop `(u, c, d)`.
    -   Update `bottomView[c] = val`. (Always overwrite, as BFS guarantees non-decreasing depth).
    -   If `d < D`:
        -   Add children to queue with `d + 1`.
4.  Iterate `minCol` to `maxCol` and print.

### Time Complexity

-   **O(N)**: In worst case (D is large), visit all nodes. If D is small, visits fewer.

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
1
```
**Tree:**
- 0(1) -> L:1(2), R:2(3)
- 1(2) -> L:3(4), R:-1
- 2(3) -> L:-1, R:4(5)
**Limit D=1**

**BFS:**
1.  `(0, c=0, d=0)` -> Map: `{0: 1}`. `d < 1`, add children.
2.  `(1, c=-1, d=1)` -> Map: `{0: 1, -1: 2}`. `d == 1`, stop children.
3.  `(2, c=1, d=1)` -> Map: `{0: 1, -1: 2, 1: 3}`. `d == 1`, stop children.

**Note:** Node 3 (4) and Node 4 (5) are at depth 2. They are never added to queue.

**Result:** `2 1 3` (Sorted by col: -1, 0, 1).

## ✅ Proof of Correctness

BFS visits nodes level by level.
-   We only add nodes to the queue if their depth is `< D`. This ensures we process nodes up to depth `D`.
-   We update the map for every node processed. Since BFS visits deeper nodes later, the map entry for a column will eventually hold the value of the deepest node in that column (within the limit).
-   If multiple nodes are at the same maximal depth, BFS visits left-to-right, so the rightmost one overwrites, which is the standard definition of Bottom View.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Range Query**
    -   Output bottom view only for columns `[L, R]`.
-   **Extension 2: Deepest Node**
    -   Find the single deepest node in the entire tree within limit.
-   **Extension 3: Top View with Limit**
    -   Same logic, but don't overwrite if key exists.

### Common Mistakes to Avoid

1.  **Off-by-one Depth:**
    -   ❌ Stopping at `d < D` but not processing `d == D`.
    -   ✅ Process `d == D`, but don't add children.
2.  **Map Ordering:**
    -   ❌ Iterating map keys in random order.
    -   ✅ Use TreeMap or sort keys.

## Related Concepts

-   **BFS**
-   **Tree Views**
-   **Pruning**
