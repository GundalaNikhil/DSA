---
problem_id: SEG_RANGE_MIN_INDEX__3926
display_id: SEG-011
slug: range-min-index
title: "Range Minimum Index"
difficulty: Medium
difficulty_score: 45
topics:
  - Segment Tree
  - Range Queries
  - Tie Breaking
tags:
  - segment-tree
  - range-min
  - index
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-011: Range Minimum Index

## Problem Statement

Given an array `a`, answer queries for the index of the minimum value in a range. If multiple indices have the same minimum value, return the smallest index.

Operations:

- `SET i x`: set `a[i] = x`
- `MINIDX l r`: output the index of the minimum in `a[l..r]`

![Problem Illustration](../images/SEG-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `MINIDX`

## Output Format

- For each `MINIDX`, print the index

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
4 2 2
MINIDX 0 2
```

**Output:**

```
1
```

**Explanation:**

The minimum value is 2 at indices 1 and 2, so return the smaller index 1.

![Example Visualization](../images/SEG-011/example-1.png)

## Notes

- Store (value, index) pairs in the segment tree
- Merge by comparing values, then indices
- Each operation runs in O(log n)
- Use 64-bit for values if needed

## Related Topics

Segment Tree, Range Minimum Query, Tie Breaking

---

## Solution Template
### Java


### Python


### C++


### JavaScript

