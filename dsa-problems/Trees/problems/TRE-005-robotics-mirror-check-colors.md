---
problem_id: TRE_ROBOTICS_MIRROR_CHECK_COLORS__6729
display_id: TRE-005
slug: robotics-mirror-check-colors
title: "Robotics Mirror Check with Colors"
difficulty: Easy
difficulty_score: 32
topics:
  - Trees
  - Symmetry
  - BFS
tags:
  - trees
  - symmetry
  - bfs
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-005: Robotics Mirror Check with Colors

## Problem Statement

Each node has a value and a color bit (0 or 1). Determine whether the tree is symmetric in both structure and values, and also whether the multiset of colors on each mirrored level matches.

Colors do not need to match node-for-node across the mirror, but the multiset of colors on each level in the left subtree must equal the multiset on the corresponding level in the right subtree.

![Problem Illustration](../images/TRE-005/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value color left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print `true` if the tree passes both checks, otherwise `false`

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers
- `color` is `0` or `1`

## Example

**Input:**

```
7
4 0 1 2
2 1 3 4
2 1 5 6
1 0 -1 -1
3 1 -1 -1
3 1 -1 -1
1 0 -1 -1
```

**Output:**

```
true
```

**Explanation:**

The tree is structurally symmetric with equal values. At each depth, the multiset of colors in the left subtree matches the right subtree.

![Example Visualization](../images/TRE-005/example-1.png)

## Notes

- If the tree is empty, return `true`.
- You must check both structural/value symmetry and color multiset balance.
- BFS by levels or a mirrored DFS can be used.

## Related Topics

Binary Trees, Symmetry, BFS

---

## Solution Template

### Java


### Python


### C++


### JavaScript

