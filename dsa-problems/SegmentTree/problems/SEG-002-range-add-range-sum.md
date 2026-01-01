---
problem_id: SEG_RANGE_ADD_RANGE_SUM__6841
display_id: SEG-002
slug: range-add-range-sum
title: "Range Add, Range Sum"
difficulty: Medium
difficulty_score: 46
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Updates
tags:
  - segment-tree
  - lazy-propagation
  - range-sum
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-002: Range Add, Range Sum

## Problem Statement

You are given an array `a`. Support two operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `SUM l r`: output the sum of `a[l..r]`

Process operations in order and output answers for each `SUM`.

![Problem Illustration](../images/SEG-002/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers (initial array)
- Next `q` lines: operations `ADD` or `SUM`

## Output Format

- For each `SUM`, print the range sum

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 3
0 0 0
ADD 0 1 5
ADD 1 2 2
SUM 0 2
```

**Output:**

```
14
```

**Explanation:**

After updates, the array is `[5, 7, 2]`, so the sum over `[0,2]` is 14.

![Example Visualization](../images/SEG-002/example-1.png)

## Notes

- Use a segment tree with lazy propagation
- Each operation runs in O(log n)
- Store segment sums and pending add values
- Use 64-bit integers for sums

## Related Topics

Segment Tree, Lazy Propagation, Range Updates

---

## Solution Template
### Java


### Python


### C++


### JavaScript

