---
problem_id: SEG_RANGE_ADD_KTH_ORDER__8059
display_id: SEG-012
slug: range-add-kth-order
title: "Range Add, K-th Order"
difficulty: Hard
difficulty_score: 70
topics:
  - Segment Tree
  - Order Statistics
  - Range Updates
tags:
  - segment-tree
  - kth-statistic
  - range-add
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-012: Range Add, K-th Order

## Problem Statement

Maintain an array under range-add updates and k-th order statistic queries on subarrays.

Operations:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `KTH l r k`: output the k-th smallest value in `a[l..r]`

![Problem Illustration](../images/SEG-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `ADD` or `KTH`

## Output Format

- For each `KTH`, print the k-th smallest value

## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= r - l + 1`

## Example

**Input:**

```
3 2
1 2 3
ADD 0 2 1
KTH 0 2 2
```

**Output:**

```
3
```

**Explanation:**

After adding 1, the array is `[2,3,4]`, so the 2nd smallest in `[0,2]` is 3.

![Example Visualization](../images/SEG-012/example-1.png)

## Notes

- This requires advanced data structures to support order statistics under updates
- Solutions may use sqrt decomposition or offline processing
- Correctness is more important than a specific technique
- Ensure output uses 64-bit values

## Related Topics

Order Statistics, Segment Tree, Range Updates

---

## Solution Template
### Java


### Python


### C++


### JavaScript

