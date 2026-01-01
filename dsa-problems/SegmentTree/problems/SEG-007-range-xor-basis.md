---
problem_id: SEG_RANGE_XOR_BASIS__8820
display_id: SEG-007
slug: range-xor-basis
title: "Range XOR Basis"
difficulty: Medium
difficulty_score: 56
topics:
  - Segment Tree
  - Bitwise
  - Linear Basis
tags:
  - segment-tree
  - xor
  - linear-basis
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-007: Range XOR Basis

## Problem Statement

Maintain an array `a` with point updates and queries asking for the maximum XOR value obtainable from any subset of elements in `a[l..r]`.

Operations:

- `SET i x`: set `a[i] = x`
- `MAXXOR l r`: output the maximum subset XOR in `[l, r]`

![Problem Illustration](../images/SEG-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `MAXXOR`

## Output Format

- For each `MAXXOR`, print the maximum XOR value

## Constraints

- `1 <= n, q <= 100000`
- `0 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 1
1 2 3
MAXXOR 0 2
```

**Output:**

```
3
```

**Explanation:**

The maximum XOR from subset `{1,2}` is 3.

![Example Visualization](../images/SEG-007/example-1.png)

## Notes

- Store a linear basis in each segment tree node
- Merge bases when combining segments
- Query basis to compute max XOR
- Time per operation: O(log n * B)

## Related Topics

Linear Basis, Segment Tree, Bitwise

---

## Solution Template
### Java


### Python


### C++


### JavaScript

