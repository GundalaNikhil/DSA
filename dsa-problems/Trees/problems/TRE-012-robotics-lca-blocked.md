---
problem_id: TRE_ROBOTICS_LCA_BLOCKED__7104
display_id: TRE-012
slug: robotics-lca-blocked
title: "Robotics LCA with Blocked Nodes"
difficulty: Medium
difficulty_score: 54
topics:
  - Trees
  - LCA
  - DFS
tags:
  - trees
  - lca
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-012: Robotics LCA with Blocked Nodes

## Problem Statement

Some nodes in the tree are blocked and cannot be used as part of any path. Given two target nodes that are not blocked, find their lowest common ancestor (LCA) that is also not blocked.

If all common ancestors are blocked, output `-1`.

![Problem Illustration](../images/TRE-012/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value blocked left right` for nodes `0..n-1`
- Last line: two integers `u` and `v`, the node indices of the targets

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Single integer: value of the lowest unblocked common ancestor, or `-1` if none

## Constraints

- `1 <= n <= 100000`
- `blocked` is `0` or `1`
- Node values are distinct and fit in 32-bit signed integers
- Target nodes are unblocked

## Example

**Input:**

```
5
6 1 1 2
2 0 3 4
8 0 -1 -1
1 0 -1 -1
4 0 -1 -1
3 4
```

**Output:**

```
2
```

**Explanation:**

The LCA of nodes 3 and 4 is node 1 (value 2). The root is blocked, but the LCA node itself is unblocked.

![Example Visualization](../images/TRE-012/example-1.png)

## Notes

- If the LCA is blocked, climb to the nearest unblocked ancestor.
- Use DFS to detect presence of targets in subtrees.
- Output `-1` if no unblocked common ancestor exists.

## Related Topics

LCA, DFS, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

