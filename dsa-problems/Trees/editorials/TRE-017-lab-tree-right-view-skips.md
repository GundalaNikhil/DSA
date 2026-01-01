---
problem_id: TRE_LAB_TREE_RIGHT_VIEW_SKIPS__3748
display_id: TRE-017
slug: lab-tree-right-view-skips
title: "Lab Tree Right View with Skips"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - right-view
  - bfs
  - medium
premium: true
subscription_tier: basic
---

# TRE-017: Lab Tree Right View with Skips

## 📋 Problem Summary

Find the **Right View** of a binary tree, but with a twist:
-   Ignore any node whose value is **negative**.
-   For each level of the tree, find the rightmost node that is **non-negative**.
-   If a level contains only negative nodes (or no nodes at all), that level produces no output.

## 🌍 Real-World Scenario

**Scenario Title:** Security Camera Blind Spots

Imagine a multi-story building where you want to install security cameras on the right side to monitor each floor.
-   **Nodes:** Rooms on each floor.
-   **Right View:** The room visible from the rightmost camera position.
-   **Negative Values:** Rooms that are "blocked" or "restricted" (e.g., maintenance shafts, pillars) and cannot host a camera or be monitored.
-   **Goal:** List the ID of the rightmost *usable* room on each floor. If a floor has only blocked rooms, no camera is installed there.

![Real-World Application](../images/TRE-017/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      10
     /  \
    -5   20
   / \   /
  30 -8 40
```
**Levels:**
-   **Level 0:** Node 10. Positive. Rightmost is 10.
-   **Level 1:** Nodes -5, 20. Positive: 20. Rightmost is 20.
-   **Level 2:** Nodes 30, -8, 40. Positive: 30, 40. Rightmost is 40.

**Result:** `10 20 40`

**Example with Skip:**
```
      10
     /  \
    5   -20
```
-   **Level 1:** Nodes 5, -20.
-   -20 is skipped.
-   Rightmost valid is 5.
-   **Result:** `10 5`

### Algorithm Steps

1.  **Traversal:** We can use BFS (Level Order) or DFS (Reverse Preorder: Root -> Right -> Left).
2.  **Tracking:**
    -   **BFS:** For each level, iterate through all nodes. Keep track of the last seen non-negative node. If found, add to result.
    -   **DFS:** Pass `level` as parameter. Keep a map/list `level -> value`. Since we visit Right before Left, the *first* valid node we see at a new level is the rightmost one.
3.  **Filtering:** Explicitly check `node.val >= 0`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Negative Nodes:** Are traversed (their children might be positive), but they themselves are never part of the view.
-   **Empty Level:** If a level has nodes but all are negative, output nothing for that level.
-   **Output Order:** Top to bottom.

## Naive Approach

### Intuition

Collect all nodes into a list of `(level, index, value)`. Filter out negatives. Group by level. Sort by index descending. Pick first.

### Time Complexity

-   **O(N log N)**: Sorting.

## Optimal Approach (DFS - Root, Right, Left)

DFS is elegant here. If we traverse **Root -> Right -> Left**, the first valid node we encounter at any depth `d` is guaranteed to be the rightmost valid node for that depth.

### Algorithm

1.  `view = Map<Integer, Integer>` (Depth -> Value).
2.  `dfs(node, depth)`:
    -   If `node` is null, return.
    -   If `node.val >= 0` AND `depth` not in `view`:
        -   `view.put(depth, node.val)`
    -   `dfs(node.right, depth + 1)`
    -   `dfs(node.left, depth + 1)`
3.  Iterate `0` to `maxDepth`. If depth exists in map, print value.

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
4
10 1 2
-6 3 -1
14 -1 -1
7 -1 -1
```
**Tree:**
- 0(10) -> L:1(-6), R:2(14)
- 1(-6) -> L:3(7), R:-1
- 2(14) -> Leaf
- 3(7) -> Leaf

**DFS (Root -> Right -> Left):**
1.  **Node 0 (10, d=0):** Valid. Map: `{0: 10}`.
2.  **Node 2 (14, d=1):** Valid. Map: `{0: 10, 1: 14}`.
3.  **Node 1 (-6, d=1):** Invalid (Negative). Skip map update.
    -   Recurse Right (null).
    -   Recurse Left (Node 3).
4.  **Node 3 (7, d=2):** Valid. Map: `{0: 10, 1: 14, 2: 7}`.

**Result:** `10 14 7`.

## ✅ Proof of Correctness

DFS traversal order `Root -> Right -> Left` ensures that for any depth `d`, the first node we encounter is the rightmost node at that depth.
-   We add the condition `values[u] >= 0` to filter.
-   We add the condition `!view.containsKey(depth)` to ensure we only pick the *first* valid node (the rightmost one).
-   This correctly implements the "Right View with Skips" logic.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Left View**
    -   Same logic, but traverse `Root -> Left -> Right`.
-   **Extension 2: Max Value View**
    -   Instead of rightmost, find max value at each level.
-   **Extension 3: Diagonal View**
    -   Group by `depth - col`.

### Common Mistakes to Avoid

1.  **Skipping Traversal:**
    -   ❌ `if (val < 0) return;`
    -   ✅ Negative nodes can have positive children. Must continue traversal.
2.  **Map Overwrite:**
    -   ❌ Overwriting map entry with left children.
    -   ✅ Only write if key doesn't exist.

## Related Concepts

-   **Tree Views**
-   **DFS vs BFS**
-   **Recursion**
