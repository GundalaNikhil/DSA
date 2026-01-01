---
problem_id: TRE_SPORTS_DOME_WEIGHTED_DIAMETER__9532
display_id: TRE-007
slug: sports-dome-weighted-diameter
title: "Sports Dome Weighted Diameter"
difficulty: Medium
difficulty_score: 48
topics:
  - Trees
  - DFS
  - Tree Diameter
tags:
  - trees
  - diameter
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-007: Sports Dome Weighted Diameter

## Problem Statement

Edges of the binary tree have non-negative weights. Find the maximum total edge weight along any path between two nodes.

This value is the weighted diameter of the tree.

![Problem Illustration](../images/TRE-007/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right leftWeight rightWeight` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The corresponding weight is ignored when the child is `-1`. The root is node `0` when `n > 0`.

## Output Format

- Single integer: weighted diameter of the tree

## Constraints

- `0 <= n <= 100000`
- Edge weights are integers in `[0, 10^9]`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
1 1 2 3 1
2 3 -1 2 0
3 -1 -1 0 0
4 -1 -1 0 0
```

**Output:**

```
6
```

**Explanation:**

The path `4 -> 2 -> 1 -> 3` has total weight `2 + 3 + 1 = 6`, which is the maximum.

![Example Visualization](../images/TRE-007/example-1.png)

## Notes

- The diameter can pass through or avoid the root.
- Use DFS to compute the best downward path at each node.
- The answer fits in 64-bit signed integers.

## Related Topics

Tree Diameter, DFS, Weighted Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

