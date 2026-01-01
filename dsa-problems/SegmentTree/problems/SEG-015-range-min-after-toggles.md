---
problem_id: SEG_RANGE_MIN_AFTER_TOGGLES__5728
display_id: SEG-015
slug: range-min-after-toggles
title: "Range Min After Additive Toggles"
difficulty: Medium
difficulty_score: 60
topics:
  - Segment Tree
  - Lazy Propagation
  - Range Queries
tags:
  - segment-tree
  - range-min
  - toggles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-015: Range Min After Additive Toggles

## Problem Statement

Maintain an array with two update types and range minimum queries:

- `ADD l r x`: add `x` to all elements in `a[l..r]`
- `FLIP l r`: multiply all elements in `a[l..r]` by `-1`
- `MIN l r`: output the minimum value in `a[l..r]`

![Problem Illustration](../images/SEG-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `ADD`, `FLIP`, or `MIN`

## Output Format

- For each `MIN`, print the minimum value

## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 3
1 -2 3
FLIP 0 2
ADD 1 2 1
MIN 0 2
```

**Output:**

```
-2
```

**Explanation:**

After flip: `[-1, 2, -3]`, after add: `[-1, 3, -2]`, minimum is -2.

![Example Visualization](../images/SEG-015/example-1.png)

## Notes

- Track both min and max to handle sign flips
- Lazy tags include pending add and pending flip
- Apply flip by swapping min/max and negating
- Each operation runs in O(log n)

## Related Topics

Segment Tree, Lazy Propagation, Range Minimum

---

## Solution Template
### Java


### Python


### C++


### JavaScript

