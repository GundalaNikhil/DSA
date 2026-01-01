---
problem_id: SEG_RANGE_SUM_MULTIPLE_POWERS__4175
display_id: SEG-013
slug: range-sum-multiple-powers
title: "Range Sum of Multiple Powers"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Modular Arithmetic
  - Range Sum
tags:
  - segment-tree
  - range-sum
  - modular
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-013: Range Sum of Multiple Powers

## Problem Statement

Maintain an array `a` with point updates and queries asking for the sum of powers in a range.

Operations:

- `SET i x`: set `a[i] = x`
- `SUM l r p`: output `sum(a[i]^p)` for `i` in `[l,r]` where `p` is 1, 2, or 3

All answers are modulo `MOD = 1000000007`.

![Problem Illustration](../images/SEG-013/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET` or `SUM`

## Output Format

- For each `SUM`, print the sum modulo `MOD`

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `p` is in `{1,2,3}`

## Example

**Input:**

```
2 2
2 3
SUM 0 1 2
SUM 0 1 3
```

**Output:**

```
13
35
```

**Explanation:**

`2^2 + 3^2 = 13` and `2^3 + 3^3 = 35`.

![Example Visualization](../images/SEG-013/example-1.png)

## Notes

- Store sums of powers 1, 2, and 3 per segment
- Recompute these values on point updates
- Use modular arithmetic for all sums
- Each operation is O(log n)

## Related Topics

Segment Tree, Modular Arithmetic, Range Sum

---

## Solution Template
### Java


### Python


### C++


### JavaScript

