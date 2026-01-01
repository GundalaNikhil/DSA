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
time_limit: 2000
memory_limit: 256
---
# AGR-014: Tree Diameter With Edge Removal

## Problem Statement

Given a tree with `n` nodes, consider removing each edge one at a time. This splits the tree into two components. Compute the diameter (longest path length in edges) of each component and take the maximum of the two.

Return the maximum diameter value over all edge removals.

![Problem Illustration](../images/AGR-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Next `n-1` lines: `u v` describing an undirected edge

## Output Format

- Single integer: the maximum diameter after removing one edge

## Constraints

- `2 <= n <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4
0 1
1 2
1 3
```

**Output:**

```
2
```

**Explanation:**

Removing any edge leaves a component with diameter 2, so the maximum is 2.

![Example Visualization](../images/AGR-014/example-1.png)

## Notes

- The tree is unweighted; edge lengths are 1.
- Use rerooting DP to compute subtree diameters and heights.
- The answer fits in 32-bit integers.

## Related Topics

Tree Diameter, Rerooting DP, Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

