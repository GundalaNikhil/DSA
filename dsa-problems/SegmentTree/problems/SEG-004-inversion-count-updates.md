---
problem_id: SEG_INVERSION_COUNT_UPDATES__5048
display_id: SEG-004
slug: inversion-count-updates
title: "Inversion Count Updates"
difficulty: Medium
difficulty_score: 58
topics:
  - Segment Tree
  - Fenwick Tree
  - Inversions
tags:
  - inversion-count
  - segment-tree
  - fenwick
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-004: Inversion Count Updates

## Problem Statement

You are given an array `a`. An inversion is a pair `(i, j)` with `i < j` and `a[i] > a[j]`.

Process point updates `SET i x`. After each update, output the current inversion count of the whole array.

![Problem Illustration](../images/SEG-004/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET i x`

## Output Format

- Print one line after each update: the inversion count

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
3 1 2
SET 1 4
```

**Output:**

```
2
```

**Explanation:**

After setting `a[1]=4`, the array is `[3,4,2]` with inversions `(3,2)` and `(4,2)`.

![Example Visualization](../images/SEG-004/example-1.png)

## Notes

- Coordinate-compress values to a compact range
- Use a BIT or segment tree to count inversions
- Updating a position affects pairs with its left and right sides
- Output fits in 64-bit signed integer

## Related Topics

Inversion Count, Fenwick Tree, Segment Tree

---

## Solution Template
### Java


### Python


### C++


### JavaScript

