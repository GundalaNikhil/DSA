---
problem_id: TRE_CAMPUS_VERTICAL_ORDER_WEIGHT__4502
display_id: TRE-009
slug: campus-vertical-order-weight
title: "Campus Vertical Order With Weight Priority"
difficulty: Medium
difficulty_score: 58
topics:
  - Trees
  - BFS
  - Sorting
tags:
  - trees
  - vertical-order
  - sorting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# TRE-009: Campus Vertical Order With Weight Priority

## Problem Statement

Each node has a value and a weight. Return the vertical order traversal of the tree with custom ordering rules inside each column:

1. Depth ascending
2. Weight descending
3. Value ascending

Only include columns whose total weight is at least `W`.

![Problem Illustration](../images/TRE-009/problem-illustration.png)

## Input Format

- First line: integer `n`, number of nodes
- Next `n` lines: `value weight left right` for nodes `0..n-1`
- Last line: integer `W`, the minimum column weight

`left` and `right` are child indices, or `-1` if absent. The root is node `0` when `n > 0`.

## Output Format

- Print columns from left to right
- Each column is one line with its values in the required order
- If no column meets the threshold, print an empty line

## Constraints

- `0 <= n <= 100000`
- `1 <= weight <= 1000000`
- `0 <= W <= 10^12`

## Example

**Input:**

```
5
3 5 1 2
9 2 -1 -1
8 3 3 4
4 1 -1 -1
7 4 -1 -1
3
```

**Output:**

```
3 4
8
7
```

**Explanation:**

Column weights are: col -1 = 2, col 0 = 6, col 1 = 3, col 2 = 4. Columns with weight >= 3 are col 0, 1, and 2.

![Example Visualization](../images/TRE-009/example-1.png)

## Notes

- Columns are indexed by horizontal distance from the root.
- Stable ordering is not required; use the specified sort keys.
- Use 64-bit integers for column weight sums.

## Related Topics

Vertical Traversal, BFS, Sorting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

