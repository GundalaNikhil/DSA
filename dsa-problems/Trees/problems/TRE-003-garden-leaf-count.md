---
problem_id: TRE_GARDEN_LEAF_COUNT__2475
display_id: TRE-003
slug: garden-leaf-count
title: "Garden Leaf Count"
difficulty: Easy
difficulty_score: 18
topics:
  - Trees
  - DFS
  - Counting
tags:
  - trees
  - dfs
  - counting
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-003: Garden Leaf Count

## Problem Statement

Count the number of leaf nodes in a binary tree. A leaf node has no left or right child.

![Problem Illustration](../images/TRE-003/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: number of leaf nodes

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
3
7 1 2
4 -1 -1
8 -1 -1
```

**Output:**

```
2
```

**Explanation:**

Nodes `4` and `8` have no children, so the leaf count is 2.

![Example Visualization](../images/TRE-003/example-1.png)

## Notes

- An empty tree has 0 leaves.
- A single-node tree has 1 leaf.
- Use DFS or BFS to count nodes with both children absent.

## Related Topics

Binary Trees, DFS, Tree Traversal

---

## Solution Template

### Java


### Python


### C++


### JavaScript

