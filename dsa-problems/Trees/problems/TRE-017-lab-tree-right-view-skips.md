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
time_limit: 2000
memory_limit: 256
---
# TRE-017: Lab Tree Right View with Skips

## Problem Statement

Return the right view of a binary tree, but skip any node whose value is negative. If a level contains only skipped nodes, omit that level entirely.

![Problem Illustration](../images/TRE-017/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: right view values separated by spaces
- If no visible nodes exist, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
-6 3 -1
14 -1 -1
7 -1 -1
```

**Output:**

```
10 14 7
```

**Explanation:**

At depth 1, the rightmost node is `14`. At depth 2, the only node is `7`. The negative node `-6` is skipped.

![Example Visualization](../images/TRE-017/example-1.png)

## Notes

- Level order traversal makes it easy to identify rightmost nodes.
- Skip nodes with negative values but still traverse their children.
- If the tree is empty, output an empty line.

## Related Topics

Right View, BFS, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

