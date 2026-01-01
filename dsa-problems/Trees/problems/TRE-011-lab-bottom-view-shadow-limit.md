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
time_limit: 2000
memory_limit: 256
---
# TRE-011: Lab Bottom View with Shadow Limit

## Problem Statement

Return the bottom view of a binary tree, but ignore any node deeper than depth `D` (root at depth 0). Only nodes with depth `<= D` can be chosen for each vertical column.

![Problem Illustration](../images/TRE-011/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`
- Last line: integer `D`, maximum depth to consider

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: bottom view values from left to right
- If the tree is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
- `0 <= D <= 100000`
- Node values fit in 32-bit signed integers

## Example

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

**Output:**

```
2 1 3
```

**Explanation:**

Depth limit `D=1` excludes nodes at depth 2. The bottom view within this limit is `[2, 1, 3]`.

![Example Visualization](../images/TRE-011/example-1.png)

## Notes

- Use BFS with column and depth tracking.
- For each column, keep the deepest node seen so far within depth `D`.
- If multiple nodes tie on depth, the later BFS order can be used.

## Related Topics

Bottom View, BFS, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

