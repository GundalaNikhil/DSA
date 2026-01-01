---
problem_id: TRE_LAB_TREE_HEIGHT__1934
display_id: TRE-002
slug: lab-tree-height
title: "Lab Tree Height"
difficulty: Easy
difficulty_score: 20
topics:
  - Trees
  - DFS
  - Recursion
tags:
  - trees
  - dfs
  - recursion
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-002: Lab Tree Height

## Problem Statement

Compute the height of a binary tree. The height is defined as the number of edges on the longest path from the root to any leaf.

If the tree is empty, output `-1`.

![Problem Illustration](../images/TRE-002/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: height of the tree

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
5 1 2
3 3 -1
9 -1 -1
1 -1 -1
```

**Output:**

```
2
```

**Explanation:**

The longest root-to-leaf path is `5 -> 3 -> 1`, which has 2 edges.

![Example Visualization](../images/TRE-002/example-1.png)

## Notes

- Height is measured in edges, not nodes.
- Return `-1` for an empty tree.
- A single-node tree has height 0.

## Related Topics

Binary Trees, DFS, Recursion

---

## Solution Template

### Java


### Python


### C++


### JavaScript

