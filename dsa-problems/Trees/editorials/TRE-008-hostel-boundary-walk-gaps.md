---
problem_id: TRE_HOSTEL_BOUNDARY_WALK_GAPS__3187
display_id: TRE-008
slug: hostel-boundary-walk-gaps
title: "Hostel Boundary Walk with Gaps"
difficulty: Medium
difficulty_score: 44
topics:
  - Trees
  - Boundary Traversal
  - DFS
tags:
  - trees
  - traversal
  - boundary
  - medium
premium: true
subscription_tier: basic
---

# TRE-008: Hostel Boundary Walk with Gaps

## 📋 Problem Summary

Perform a **boundary traversal** of a binary tree. The boundary includes:
1.  The **root** node.
2.  The **left boundary** (nodes on the leftmost path, excluding leaf nodes).
3.  All **leaf nodes** (from left to right).
4.  The **right boundary** (nodes on the rightmost path, excluding leaf nodes) in reverse order (bottom-up).

However, there is a twist: you must **skip** any node whose value is negative. The structural traversal remains the same (i.e., a negative node still defines the boundary path), but its value is not included in the output.

## 🌍 Real-World Scenario

**Scenario Title:** Perimeter Security Patrol

Imagine a security guard patrolling the perimeter (boundary) of a hostel complex.
-   **Root:** Main Gate.
-   **Left Boundary:** West Wall.
-   **Leaves:** Southern Fence (back of the complex).
-   **Right Boundary:** East Wall.

The guard has a checklist of checkpoints to log. Some checkpoints are marked "Inactive" (negative value) due to maintenance. The guard must walk the full perimeter path to ensure security but should only log the active checkpoints in the report.

![Real-World Application](../images/TRE-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
        1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8
```
**Boundary Nodes:**
-   **Root:** 1
-   **Leaves:** 4, 7, 8, 6.
-   **Right Boundary:** 3 (6 is a leaf).

**Traversal Order:** 1 -> 2 -> 4 -> 7 -> 8 -> 6 -> 3.

**With Negative Values:**
If node 2 is `-5`:
Output: 1 -> 4 -> 7 -> 8 -> 6 -> 3. (Skip -5).

### Algorithm Steps

1.  **Root:** Add root value if non-negative.
2.  **Left Boundary:** Start from `root.left`.
    -   If node is a leaf, stop.
    -   Add value if non-negative.
    -   Move to `left` child if exists, else `right` child.
3.  **Leaves:** DFS traversal.
    -   If node is leaf, add value if non-negative.
4.  **Right Boundary:** Start from `root.right`.
    -   If node is a leaf, stop.
    -   Store values in a temporary list (or stack).
    -   Move to `right` child if exists, else `left` child.
    -   After collecting, add values in reverse order (if non-negative).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Root as Leaf:** If root has no children, it's a leaf. Don't add it twice.
-   **Overlap:** Left boundary and leaves should not duplicate nodes. Right boundary and leaves should not duplicate nodes.
-   **Negative Values:** Only affects *output*, not the path logic. A negative node can still have children that are part of the boundary.

## Naive Approach

### Intuition

We can collect all boundary nodes into a list using the standard algorithm, and then filter out negative values at the very end.

### Algorithm

1.  `boundary = []`.
2.  Add Root.
3.  Traverse Left Boundary -> Add to `boundary`.
4.  Traverse Leaves -> Add to `boundary`.
5.  Traverse Right Boundary -> Add to `boundary` (reverse).
6.  Filter `boundary` for `val >= 0`.

### Time Complexity

-   **O(N)**: Visit boundary nodes and leaves.

## Optimal Approach (Standard Boundary Traversal)

The logic is identical to the naive approach, but we can filter "on the fly" to save memory (though O(N) memory is usually fine).

### Algorithm

1.  If `n=0`, return empty.
2.  If `root.val >= 0`, add to result.
3.  **Left Boundary:**
    -   `curr = root.left`.
    -   While `curr` is not leaf:
        -   If `curr.val >= 0`, add.
        -   `curr = curr.left ? curr.left : curr.right`.
4.  **Leaves:**
    -   `addLeaves(root)`. (Helper DFS).
    -   If leaf and `val >= 0`, add.
    -   Note: Root is technically a leaf if `n=1`. Handle carefully to avoid double counting. (Common trick: `addLeaves` skips root if it was already added, or Left Boundary logic handles root exclusion).
    -   *Better:* Left Boundary starts `root.left`. Leaves starts `root`. Right Boundary starts `root.right`.
    -   If `root` is leaf, Left/Right boundary loops won't run. `addLeaves` will add it. So don't add root in Step 1? Or exclude root from `addLeaves`?
    -   *Standard:* Add Root. Left Boundary (exclude root, exclude leaf). Leaves (exclude root? No, leaves are leaves). Right Boundary (exclude root, exclude leaf).
    -   If `n=1`, Root is added. Left/Right loops empty. `addLeaves` adds root. Double count!
    -   *Fix:* `addLeaves` should only add if `node != root`. Or simply:
        -   Add Root.
        -   `getLeft(root.left)`.
        -   `getLeaves(root.left)`.
        -   `getLeaves(root.right)`.
        -   `getRight(root.right)`.

### Time Complexity

-   **O(N)**.

### Space Complexity

-   **O(N)** output.

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
-5 3 -1
15 -1 -1
2 -1 -1
```
**Tree:**
- 0(10) -> L:1(-5), R:2(15)
- 1(-5) -> L:3(2), R:-1
- 2(15) -> Leaf
- 3(2) -> Leaf

**Execution:**
1.  **Root:** 10 >= 0. Add `10`.
2.  **Left Boundary:** Start at 1(-5).
    -   Not leaf.
    -   Val -5 < 0. Skip.
    -   Move to left child 3(2).
    -   3(2) is leaf. Stop.
3.  **Leaves:**
    -   DFS(0) -> DFS(1) -> DFS(3). 3(2) is leaf. Val 2 >= 0. Add `2`.
    -   DFS(2). 2(15) is leaf. Val 15 >= 0. Add `15`.
4.  **Right Boundary:** Start at 2(15).
    -   2(15) is leaf. Stop.

**Result:** `10 2 15`. Correct.

## ✅ Proof of Correctness

The algorithm decomposes the boundary into three disjoint sets (except for potential root/leaf overlaps which are handled):
1.  **Left Boundary:** Strictly follows the leftmost path.
2.  **Leaves:** Strictly follows DFS order (left-to-right).
3.  **Right Boundary:** Strictly follows the rightmost path.
By handling the root separately and ensuring boundary loops stop *before* leaves, we ensure no node is visited twice (except root if `n=1`, handled).
The negative check is a simple filter applied at the point of addition.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Extension 1: Anti-Clockwise vs Clockwise**
    -   Implement clockwise boundary traversal.
-   **Extension 2: Spiral Boundary**
    -   Complex variant.
-   **Extension 3: Sum of Boundary**
    -   Calculate sum instead of listing values.

### Common Mistakes to Avoid

1.  **Double Counting Leaves:**
    -   ❌ Adding a leaf in Left Boundary AND Leaves section.
    -   ✅ Stop Left/Right boundary loops when `isLeaf(curr)` is true.
2.  **Root Duplication:**
    -   ❌ Adding root in Left Boundary loop.
    -   ✅ Start Left Boundary loop from `root.left`.
3.  **Reverse Order:**
    -   ❌ Forgetting to reverse the Right Boundary.

## Related Concepts

-   **Tree Traversal**
-   **DFS**
