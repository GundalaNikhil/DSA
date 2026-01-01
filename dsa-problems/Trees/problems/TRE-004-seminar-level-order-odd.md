---
problem_id: TRE_SEMINAR_LEVEL_ORDER_ODD__5168
display_id: TRE-004
slug: seminar-level-order-odd
title: "Seminar Level Order Odd-Depth Only"
difficulty: Easy
difficulty_score: 26
topics:
  - Trees
  - BFS
  - Level Order
tags:
  - trees
  - bfs
  - traversal
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-004: Seminar Level Order Odd-Depth Only

## Problem Statement

Return the level-order traversal of a binary tree, but include only nodes at odd depths. The root is at depth 0.

For each odd depth that exists, output the node values in left-to-right order.

![Problem Illustration](../images/TRE-004/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value left right` for nodes `0..n-1`

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- For each odd depth that has nodes, print one line with the values in left-to-right order
- If there are no odd-depth nodes, print an empty line

## Constraints

- `0 <= n <= 100000`
- Node values fit in 32-bit signed integers

## Example

**Input:**

```
4
10 1 2
5 3 -1
12 -1 -1
7 -1 -1
```

**Output:**

```
5 12
```

**Explanation:**

Depth 1 nodes are `5` and `12`. Depth 3 does not exist, so only one line is printed.

![Example Visualization](../images/TRE-004/example-1.png)

## Notes

- Traverse all levels, but only output odd depths.
- Preserve left-to-right order within each level.
- An empty tree produces a single empty line.

## Related Topics

Level Order Traversal, BFS, Binary Trees

---

## Solution Template

### Java


### Python


### C++


### JavaScript

