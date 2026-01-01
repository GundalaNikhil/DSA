---
problem_id: SEG_COUNT_VALUES_IN_RANGE__1637
display_id: SEG-006
slug: count-values-in-range
title: "Count of Values in Range"
difficulty: Medium
difficulty_score: 51
topics:
  - Segment Tree
  - BIT
  - Range Queries
tags:
  - segment-tree
  - range-count
  - fenwick
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-006: Count of Values in Range

## Problem Statement

Maintain an array `a` under point updates and range count queries. The operations are:

- `SET i x`: set `a[i] = x`
- `COUNT l r x y`: count how many `a[i]` in `[l, r]` satisfy `x <= a[i] <= y`

![Problem Illustration](../images/SEG-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `COUNT` operations

## Output Format

- For each `COUNT`, print the number of values in range

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x, y <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
1 5 2
COUNT 0 2 2 5
```

**Output:**

```
2
```

**Explanation:**

In `[1,5,2]`, the values in `[2,5]` are 5 and 2.

![Example Visualization](../images/SEG-006/example-1.png)

## Notes

- Coordinate-compress all values from updates and queries
- Use a segment tree of Fenwick trees or a BIT of BITs
- Each operation runs in O(log^2 n)
- Counts fit in 32-bit integer

## Related Topics

Segment Tree, Fenwick Tree, Range Counting

---

## Solution Template
### Java


### Python


### C++


### JavaScript

