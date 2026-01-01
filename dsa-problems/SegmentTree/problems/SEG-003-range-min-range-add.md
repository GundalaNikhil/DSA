---
problem_id: SEG_RANGE_MIN_RANGE_ADD__3915
display_id: SEG-003
slug: range-min-range-add
title: "Range Minimum with Range Add"
difficulty: Medium
difficulty_score: 48
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Updates
tags:
  - segment-tree
  - range-min
  - lazy-propagation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-003: Range Minimum with Range Add

## Problem Statement

Given an array `a`, support two operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `MIN l r`: output the minimum value in `a[l..r]`

![Problem Illustration](../images/SEG-003/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: operations `ADD` or `MIN`

## Output Format

- For each `MIN`, print the minimum value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 2
3 1 4
ADD 0 2 2
MIN 1 2
```

**Output:**

```
3
```

**Explanation:**

After adding 2 to all elements, the array becomes `[5, 3, 6]`, and the minimum in `[1,2]` is 3.

![Example Visualization](../images/SEG-003/example-1.png)

## Notes

- Store the minimum in each segment tree node
- Use lazy propagation to defer range adds
- Each operation runs in O(log n)
- Use 64-bit integers if needed

## Related Topics

Segment Tree, Range Minimum Query, Lazy Propagation

---

## Solution Template
### Java


### Python


### C++


### JavaScript

