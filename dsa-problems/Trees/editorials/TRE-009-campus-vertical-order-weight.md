---
problem_id: TRE_CAMPUS_VERTICAL_ORDER_WEIGHT__4502
display_id: TRE-009
slug: campus-vertical-order-weight
title: "Campus Vertical Order With Weight Priority"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - BFS
  - Sorting
tags:
  - trees
  - vertical-order
  - sorting
  - medium
premium: true
subscription_tier: basic
---

# TRE-009: Campus Vertical Order With Weight Priority

## 📋 Problem Summary

Perform a **vertical order traversal** of a binary tree. Nodes are grouped by their horizontal distance from the root (column index). Within each column, nodes must be sorted by:
1.  **Depth** (ascending, top to bottom).
2.  **Weight** (descending, heavier items first).
3.  **Value** (ascending, tie-breaker).

Finally, filter the output to only include columns where the **sum of weights** of all nodes in that column is at least `W`.

## 🌍 Real-World Scenario

**Scenario Title:** Warehouse Shelving Optimization

Imagine a warehouse where items are stored on vertical racks (columns).
-   **Horizontal Distance:** Represents the rack number relative to the central aisle.
-   **Depth:** Represents the shelf level (higher shelves are depth 0).
-   **Weight:** Heavier items should be listed first for structural checks or priority picking.
-   **Value:** Item ID.

The manager wants a report of all racks that are "heavily loaded" (total weight >= `W`) to schedule maintenance. The report must list items on each rack from top to bottom, prioritizing heavy items on the same shelf.

![Real-World Application](../images/TRE-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      3 (W=5)
     / \
    9   8 (W=3)
       / \
      4   7 (W=4)
```
**Columns:**
-   **Col -1:** Node 9 (Weight 2). Total = 2.
-   **Col 0:** Node 3 (Weight 5), Node 4 (Weight 1). Total = 6.
-   **Col 1:** Node 8 (Weight 3). Total = 3.
-   **Col 2:** Node 7 (Weight 4). Total = 4.

**Threshold W = 3:**
-   Col -1 (Total 2) < 3. Skip.
-   Col 0 (Total 6) >= 3. Keep.
-   Col 1 (Total 3) >= 3. Keep.
-   Col 2 (Total 4) >= 3. Keep.

**Ordering in Col 0:**
-   Node 3 (Depth 0, Weight 5).
-   Node 4 (Depth 2, Weight 1).
-   Order: 3, 4.

### Algorithm Steps

1.  **BFS Traversal:** Use a queue to traverse the tree. Store tuples `(node, col, depth)`.
2.  **Grouping:** Use a Map `col -> List<NodeInfo>`. `NodeInfo` stores `{val, weight, depth}`.
3.  **Sorting:** For each column list, sort using the custom comparator:
    -   Compare `depth`: if different, smaller depth comes first.
    -   Compare `weight`: if different, larger weight comes first.
    -   Compare `val`: if different, smaller val comes first.
4.  **Filtering:** Calculate total weight for each column. Discard columns with `total < W`.
5.  **Output:** Print valid columns sorted by column index (min to max).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Column Index:** Root is 0. Left child is `col - 1`. Right child is `col + 1`.
-   **Depth:** Root is 0. Children are `depth + 1`.
-   **Sorting:** Strict priority: Depth -> Weight (Desc) -> Value (Asc).
-   **Weights:** Can be large, use `long` for sums.

## Naive Approach

### Intuition

We can use DFS to traverse and collect nodes. DFS naturally visits deeper nodes later, but not necessarily in order of depth for the same column (e.g., left subtree depth 2 vs right subtree depth 2). So explicit sorting is required regardless of traversal method.

### Algorithm

1.  DFS(root, col, depth).
2.  Store all nodes in a list.
3.  Group by column.
4.  Sort each group.
5.  Filter and print.

### Time Complexity

-   **O(N log N)**: Due to sorting nodes within columns.

## Optimal Approach (BFS + Sorting)

BFS is slightly better than DFS because it naturally visits nodes in depth order. This means the primary sort key (depth) is already mostly sorted. However, since we have secondary criteria (weight, value) for nodes at the *same* depth/column, we still need to sort.

### Algorithm

1.  Queue `q` stores `(u, col, depth)`.
2.  Map `map` stores `col -> List<Node>`.
3.  BFS:
    -   Pop `(u, c, d)`.
    -   Add `u` to `map[c]`.
    -   Push `(left, c-1, d+1)` and `(right, c+1, d+1)`.
4.  Iterate `minCol` to `maxCol`.
5.  If `map[c]` exists:
    -   Sum weights. If `< W`, continue.
    -   Sort `map[c]`.
    -   Print values.

### Time Complexity

-   **O(N log N)**: Sorting is the bottleneck. BFS is O(N).

### Space Complexity

-   **O(N)**: Store all nodes.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5
3 5 1 2
9 2 -1 -1
8 3 3 4
4 1 -1 -1
7 4 -1 -1
3
```
**Tree:**
- 0(3, w=5) -> L:1(9, w=2), R:2(8, w=3)
- 2(8, w=3) -> L:3(4, w=1), R:4(7, w=4)

**BFS:**
- `(0, c=0, d=0)` -> Col 0: `[(3, 5, 0)]`
- `(1, c=-1, d=1)` -> Col -1: `[(9, 2, 1)]`
- `(2, c=1, d=1)` -> Col 1: `[(8, 3, 1)]`
- `(3, c=0, d=2)` -> Col 0: `[(3, 5, 0), (4, 1, 2)]`
- `(4, c=2, d=2)` -> Col 2: `[(7, 4, 2)]`

**Weights & Filtering (W=3):**
- Col -1: Total 2. Fail.
- Col 0: Total 6. Pass. Sorted: `(3,5,0), (4,1,2)`. Values: `3 4`.
- Col 1: Total 3. Pass. Sorted: `(8,3,1)`. Values: `8`.
- Col 2: Total 4. Pass. Sorted: `(7,4,2)`. Values: `7`.

**Output:**
```
3 4
8
7
```

## ✅ Proof of Correctness

BFS ensures we visit nodes level by level, but since we need to group by column first, we collect everything into a Map.
The sorting step explicitly enforces the problem's ordering rules (Depth -> Weight -> Value).
The filtering step explicitly checks the sum condition.
Using a TreeMap or iterating `minCol` to `maxCol` ensures columns are output in left-to-right order.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Top View**
    -   Print only the first node in each column.
-   **Extension 2: Diagonal Traversal**
    -   Group by `depth - col` (or similar metric).
-   **Extension 3: Width of Tree**
    -   `maxCol - minCol + 1`.

### Common Mistakes to Avoid

1.  **Sorting Order:**
    -   ❌ Sorting weight ascending.
    -   ✅ Problem says weight **descending**.
2.  **Column Order:**
    -   ❌ Printing columns in random hash map order.
    -   ✅ Must be sorted by column index.
3.  **Tie-Breaking:**
    -   ❌ Ignoring value tie-breaker.

