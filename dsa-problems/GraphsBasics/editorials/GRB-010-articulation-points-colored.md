---
problem_id: GRB_ARTICULATION_POINTS_COLORED__1685
display_id: GRB-010
slug: articulation-points-colored
title: "Articulation Points Under Edge Colors"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - DFS
  - Articulation Points
tags:
  - graphs-basics
  - articulation-points
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# GRB-010: Articulation Points Under Edge Colors

## 📋 Problem Summary

You are given an undirected graph with edges colored either **Red (R)** or **Blue (B)**. A node is **critical** if its removal splits the graph into two or more components such that:
1.  At least one component contains a **Red** edge.
2.  At least one *other* component contains a **Blue** edge.

Find all such critical nodes.

## 🌍 Real-World Scenario

**Scenario Title:** Power Plant Failure

Imagine a power grid with two types of power lines:
-   **Red Lines:** High-voltage transmission lines (Long distance).
-   **Blue Lines:** Local distribution lines (Neighborhoods).
-   **Nodes:** Substations.

If a specific substation fails (is removed), it might isolate a region that *only* has high-voltage lines from a region that *only* has local lines. This is a catastrophic failure because the local region loses its connection to the main grid, and the high-voltage region loses its distribution network. We need to identify these critical substations to reinforce them.

![Real-World Application](../images/GRB-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (R)
  0 ------- 1
            |
            | (B)
            |
            2
```
-   **Node 1:**
    -   Removes edge (0,1) [Red] and (1,2) [Blue].
    -   Component {0} has NO edges.
    -   Component {2} has NO edges.
    -   Result: Node 1 is NOT critical in this simple specific derivation (needs careful component analysis).

**Better Example:**
```
  (R)     (R)        (B)     (B)
0 --- 1 ------- 2 ------- 3 --- 4
```
-   **Remove Node 2:**
    -   Left Component: `{0, 1}` with edge `(0,1)` [Red].
    -   Right Component: `{3, 4}` with edge `(3,4)` [Blue].
    -   **Result:** Node 2 is Critical. It separates a "Red Component" from a "Blue Component".

### Algorithm Steps

1.  **Find Articulation Points:** Use Tarjan's or Hopcroft-Tarjan algorithm (DFS with `discovery_time` and `low_link` values).
2.  **Track Colors in Subtrees:**
    -   During DFS, for each node `u`, track if its subtree contains a Red edge or a Blue edge.
    -   `hasRed[u]` = true if subtree at `u` has a Red edge.
    -   `hasBlue[u]` = true if subtree at `u` has a Blue edge.
3.  **Check Critical Condition:**
    -   When exploring child `v` of `u`:
        -   If `low[v] >= disc[u]`, then `u` is an articulation point separating `v`'s subtree.
        -   Check if `v`'s subtree has Red edges and the "rest of the graph" (everything excluding `v`'s subtree) has Blue edges.
        -   OR check if `v`'s subtree has Blue edges and the "rest of the graph" has Red edges.
    -   "Rest of graph" color info can be derived: `TotalRed - SubtreeRed[v] > 0`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Edge Colors:** Edges are strictly R or B.
-   **Components:** A single node with no edges does *not* contain a Red or Blue edge.
-   **Root Node:** Special case for the root of the DFS tree. It needs >1 child to be an articulation point.

## Naive Approach

### Intuition

For each node `i`:
1.  Temporarily remove `i`.
2.  Run BFS/DFS to find connected components.
3.  Check each component for Red/Blue edges.
4.  If condition met, add `i` to result.

### Time Complexity

-   **O(N * (N + M))**: Too slow for N=100,000.

## Optimal Approach (DFS with Color Tracking)

We augment the standard Articulation Point algorithm.

### State Tracking
-   `redCount[u]`: Number of Red edges in subtree of `u`.
-   `blueCount[u]`: Number of Blue edges in subtree of `u`.
-   `totalRed`, `totalBlue`: Total counts in the entire graph.

### Critical Check
For a node `u` and its child `v` (where `low[v] >= disc[u]`):
-   **Separated Component:** The subtree rooted at `v`.
    -   Has Red? `redCount[v] > 0`
    -   Has Blue? `blueCount[v] > 0`
-   **Remaining Component:** The rest of the graph.
    -   Has Red? `totalRed - redCount[v] > 0`
    -   Has Blue? `totalBlue - blueCount[v] > 0`

**Condition:**
`u` is critical if for any child `v` (where `low[v] >= disc[u]`):
-   (`redCount[v] > 0` AND `totalBlue - blueCount[v] > 0`) OR
-   (`blueCount[v] > 0` AND `totalRed - redCount[v] > 0`)

### Time Complexity

-   **O(N + M)**: Single DFS traversal.

### Space Complexity

-   **O(N + M)**: Recursion stack and arrays.

## Implementations

### Java

*Correction on Logic:* The standard `low[v] >= disc[u]` check works for root too if we treat each child as a separate component check. The only difference is root needs `children > 1` to be an AP, but for *this specific problem*, even if root has 1 child, removing it removes the root and its edges. If the remaining graph (child's subtree) has Red and "removed part" (root + edges) has Blue... wait.
Removing a node removes its incident edges.
If root has 1 child `v`, removing root leaves `v`'s subtree.
The "rest of graph" is empty. Empty set has no edges.
So root with 1 child can NEVER be critical because one component is empty.
So `children > 1` is implicitly required for root to split graph into >= 2 non-empty components?
So we need at least 2 components.
For root, if `children > 1`, we have multiple subtrees.
If `children == 1`, we have 1 subtree. Removing root leaves 1 component. We need 2. So root must have `children > 1`.

Let's rewrite the implementation cleanly.


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
5 4
0 2 R
3 4 B
1 0 R
1 3 B
```
**Graph Structure:** `2 -[R]- 0 -[R]- 1 -[B]- 3 -[B]- 4`
**Edges:** `(0,2,R), (3,4,B), (1,0,R), (1,3,B)`
**Total:** Red=2, Blue=2.

**DFS(1) [Root]:**
-   **Child 0:** Edge (1,0,R).
    -   **DFS(0):**
        -   **Child 2:** Edge (0,2,R).
            -   **DFS(2):** Leaf. `subRed=0, subBlue=0`.
            -   Back to 0. `branchRed=1, branchBlue=0`. `subRed[0]=1`.
            -   `low[2] >= disc[0]`. Check split:
                -   Branch (2): Red=1, Blue=0.
                -   Rest: Red=1, Blue=2.
                -   (Red && Blue) -> True. **0 is Critical.**
    -   Back to 1. `branchRed=2, branchBlue=0`. `subRed[1]=2`.
    -   `low[0] >= disc[1]`. Check split:
        -   Branch (0,2): Red=2, Blue=0.
        -   Rest (3,4): Red=0, Blue=2.
        -   (Red && Blue) -> True. **1 is Critical.**
-   **Child 3:** Edge (1,3,B).
    -   **DFS(3):**
        -   **Child 4:** Edge (3,4,B).
            -   **DFS(4):** Leaf.
            -   Back to 3. `branchRed=0, branchBlue=1`.
            -   `low[4] >= disc[3]`. Check split:
                -   Branch (4): Blue=1.
                -   Rest: Red=2, Blue=1.
                -   (Blue && Red) -> True. **3 is Critical.**
    -   Back to 1. `branchRed=0, branchBlue=2`.
    -   `low[3] >= disc[1]`. Check split:
        -   Branch (3,4): Blue=2.
        -   Rest (0,2): Red=2.
        -   (Blue && Red) -> True. **1 is Critical.**

**Root Check:** Node 1 has 2 children (0 and 3). So it stays critical.

**Analysis:**
-   **Node 0:** Child 2. `subRed[2]=0`. Component {2} has 0 Red. Not critical.
-   **Node 3:** Child 4. `subBlue[4]=0`. Component {4} has 0 Blue. Not critical.
-   **Node 1:**
    -   Child 0 (subtree {0,2}). `subRed[0]=1` (edge 0-2).
    -   Rest (subtree {3,4}). `subBlue[3]=1` (edge 3-4).
    -   Split: {0,2} has Red. {3,4} has Blue. **1 is Critical.**

**Result:** `1`. Matches example!

## ✅ Proof of Correctness

The logic relies on the property of articulation points: removing `u` separates `v`'s subtree from the rest.
-   Edges *inside* `v`'s subtree are counted in `subRed[v]`.
-   Edges *outside* `v`'s subtree (including the edge `u-v`) are `Total - subRed[v]`.
-   When `u` is removed, `u-v` is gone. So "Rest" has `Total - subRed[v] - (u-v is Red? 1 : 0)`.
-   We simply check if `subRed[v] > 0` and `RestBlue > 0` (or vice versa).

## 💡 Interview Extensions (High-Value Add-ons)

-   **Biconnected Components:** This is related to finding biconnected components.
-   **Dynamic Updates:** What if edge colors change? (Harder).

### Common Mistakes to Avoid

1.  **Counting the connecting edge:** The edge `(u, v)` is removed when `u` is removed. Do not count it as part of `v`'s component or the remaining component.
2.  **Root Case:** Root needs >1 child to be an AP.
3.  **Back-edges:** Back-edges from `v`'s subtree to `u` (or above) are impossible if `low[v] >= disc[u]`.
