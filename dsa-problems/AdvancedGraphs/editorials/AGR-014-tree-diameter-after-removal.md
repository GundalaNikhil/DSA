---
problem_id: AGR_TREE_DIAMETER_AFTER_REMOVAL__5964
display_id: AGR-014
slug: tree-diameter-after-removal
title: "Tree Diameter With Edge Removal"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Trees
  - Diameter
tags:
  - advanced-graphs
  - tree-diameter
  - rerooting
  - medium
premium: true
subscription_tier: basic
---

# AGR-014: Tree Diameter With Edge Removal

## 📋 Problem Summary

For every edge in a tree, if we remove it, the tree splits into two components. Calculate the diameter of each component, take the maximum of these two, and find the maximum such value over all possible edge removals.

## 🌍 Real-World Scenario

**Scenario Title:** Power Grid Resilience

Consider a power grid structured as a tree.
-   **Edge Removal:** Represents a power line failure.
-   **Components:** The grid splits into two isolated islands.
-   **Diameter:** Represents the "span" or worst-case transmission distance within an island.
-   **Goal:** We want to know the *worst-case* scenario (maximum diameter) among all possible single-line failures to ensure voltage stability protocols can handle the longest possible transmission path in any island configuration.

![Real-World Application](../images/AGR-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Tree:**
```
      0
     / \
    1   2
   / \
  3   4
```
**Remove Edge (0, 1):**
-   Component 1 (Subtree 1): `{1, 3, 4}`. Diameter: `3-1-4` (length 2).
-   Component 2 (Rest): `{0, 2}`. Diameter: `0-2` (length 1).
-   Max: 2.

**Remove Edge (1, 3):**
-   Component 1 (Subtree 3): `{3}`. Diameter: 0.
-   Component 2 (Rest): `{0, 1, 2, 4}`. Diameter: `4-1-0-2` (length 3).
-   Max: 3.

**Result:** Max over all edges is 3.

### Algorithm: Rerooting DP

1.  **Standard DP (Bottom-Up):**
    -   Root at 0.
    -   For each node `u`, compute `height[u]` (max distance to leaf) and `diam[u]` (diameter of subtree).
    -   `height[u] = 1 + max(height[v])`.
    -   `diam[u] = max(max(diam[v]), height[v1] + height[v2] + 2)`.
    -   This gives the diameter of the "lower" component when edge `(u, parent)` is removed.
2.  **Rerooting (Top-Down):**
    -   Compute `up_diam[u]` (diameter of the tree *excluding* subtree `u`) and `up_height[u]` (longest path starting at `parent` going upwards or into other branches).
    -   To compute for child `v` of `u`:
        -   `up_height[v] = 1 + max(up_height[u], height[other_child] + 1)`.
        -   `up_diam[v] = max(up_diam[u], diam[other_child], up_height[u] + height[other_child] + 1, height[other1] + height[other2] + 2)`.
    -   Use prefix/suffix arrays of children's heights/diameters to efficiently query "other children".

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **N:** Up to 200,000. `O(N)` required.
-   **Edges:** Unweighted (length 1).
-   **Output:** Max of (diam(comp1), diam(comp2)) over all edges.

## Naive Approach

### Intuition

Iterate all edges, remove, run BFS twice to find diameter.

### Time Complexity

-   **O(N^2)**: Too slow.

## Optimal Approach (Rerooting)

### Time Complexity

-   **O(N)**: Two DFS passes.

### Space Complexity

-   **O(N)**: DP arrays.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
0 1
1 2
1 3
```
**Tree:** `2-1-0` and `3-1`. 1 is center.
**DFS 1 (Root 0):**
-   `height`: `2:0, 3:0, 1:1, 0:2`.
-   `diam`: `2:0, 3:0, 1:2 (2-1-3), 0:3 (2-1-0)`.
**DFS 2 (Root 0):**
-   `u=0`. `upHeight[0]=-1`, `upDiam[0]=0`.
-   Child 1. `vLen=2`. `lens=[-1, 2] -> [2, -1, -1]`. `diams=[0, 2] -> [2, 0]`.
-   `upHeight[1] = 1 + (-1) = 0`. (Path 0->nothing).
-   `upDiam[1] = max(0, -1 + -1) = 0`.
-   Edge `(1, 0)` removed.
    -   Comp 1 (Subtree 1): `diam[1]=2`.
    -   Comp 2 (Rest 0): `upDiam[1]=0`.
    -   Max: 2. `maxDiam=2`.
-   Recurse `dfs2(1, 0)`.
    -   `u=1`. `upHeight[1]=0, upDiam[1]=0`.
    -   Children 2, 3.
    -   Arms: `Up(0,0)`, `2(1,0)`, `3(1,0)`.
    -   `lens=[1, 1, 0]`. `diams=[0, 0, 0]`.
    -   Child 2: `vLen=1`.
        -   `bestLen` (excl 1) = 1. `upHeight[2]=2`.
        -   `path` (excl 1) = 1 + 0 = 1.
        -   `upDiam[2] = max(0, 1) = 1`.
        -   Edge `(2, 1)` removed. `diam[2]=0`, `upDiam[2]=1`. Max 1.
    -   Child 3: Same. Max 1.
**Result:** 2. Correct.

## ✅ Proof of Correctness

-   **Rerooting:** Correctly computes the diameter of the "rest of the tree" for every node.
-   **Cases:** Considers max diameter in the rest (from other subtrees) AND max path passing through parent (combining two other arms).

## 💡 Interview Extensions (High-Value Add-ons)

-   **Min Diameter:** Find edge to remove to *minimize* the max diameter. (Center finding).
-   **Weighted Tree:** Same logic, just sum weights.
-   **Centroid Decomposition:** Another way to handle path problems.

### Common Mistakes to Avoid

1.  **Top-K Logic:** Correctly excluding the current child's contribution is tricky. Sorting is easiest.
2.  **Base Cases:** Leaves have height 0 (or -1 depending on definition).
3.  **Recursion Depth:** Python needs `sys.setrecursionlimit`.
