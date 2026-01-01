---
problem_id: SEG_LONGEST_INCREASING_SUBARRAY_UPDATES__2654
display_id: SEG-008
slug: longest-increasing-subarray-updates
title: "Longest Increasing Subarray After Updates"
difficulty: Medium
difficulty_score: 55
topics:
  - Segment Tree
  - Dynamic Arrays
  - Monotonicity
tags:
  - segment-tree
  - increasing
  - updates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-008: Longest Increasing Subarray After Updates

## Problem Statement

Given an array `a`, you must handle point updates. After each update, output the length of the longest strictly increasing contiguous subarray.

Operation:

- `SET i x`: set `a[i] = x`

![Problem Illustration](../images/SEG-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SET i x`

## Output Format

- For each update, print the current longest increasing subarray length

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
3 1
1 2 1
SET 2 3
```

**Output:**

```
3
```

**Explanation:**

After the update the array becomes `[1, 2, 3]`, which is strictly increasing.

![Example Visualization](../images/SEG-008/example-1.png)

## Notes

- Store prefix and suffix increasing lengths per segment
- Merge using boundary comparisons between segments
- Update affects only O(log n) nodes
- The answer is the max length stored at the root

## Related Topics

Segment Tree, Range Merge, Dynamic Updates

---

## Solution Template
### Java


### Python


### C++


### JavaScript

