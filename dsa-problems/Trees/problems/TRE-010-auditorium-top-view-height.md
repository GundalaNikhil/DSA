---
problem_id: TRE_AUDITORIUM_TOP_VIEW_HEIGHT__5601
display_id: TRE-010
slug: auditorium-top-view-height
title: "Auditorium Top View With Height Bonus"
difficulty: Medium
difficulty_score: 46
topics:
  - Trees
  - BFS
  - Views
tags:
  - trees
  - top-view
  - bfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-010: Auditorium Top View With Height Bonus

## Problem Statement

For each vertical column, choose the node with the smallest depth (top view). If multiple nodes share the same column and depth, choose the one with the largest value.

Return the chosen values from leftmost column to rightmost column.

![Problem Illustration](../images/TRE-010/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single line: top view values from left to right, separated by spaces
- If the tree is empty, print an empty line

## Constraints

- `0 <= n <= 100000`
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
```

**Output:**

```
4 2 1 3 5
```

**Explanation:**

Columns from left to right are `-2, -1, 0, 1, 2`, giving values `4, 2, 1, 3, 5`.

![Example Visualization](../images/TRE-010/example-1.png)

## Notes

- Track column and depth for each node using BFS.
- Tie-breaking on the same depth uses the larger value.
- The root is always part of the top view if it exists.

## Related Topics

Top View, BFS, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

