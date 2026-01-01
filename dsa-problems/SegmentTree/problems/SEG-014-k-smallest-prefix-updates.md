---
problem_id: SEG_K_SMALLEST_PREFIX_UPDATES__9461
display_id: SEG-014
slug: k-smallest-prefix-updates
title: "K Smallest Prefix Updates"
difficulty: Medium
difficulty_score: 50
topics:
  - Segment Tree
  - Range Assignment
  - Prefix Updates
tags:
  - segment-tree
  - assignment
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-014: K Smallest Prefix Updates

## Problem Statement

Maintain an array `a` under prefix assignment updates. The operations are:

- `SETPREFIX k x`: set `a[0..k-1] = x`
- `SUM l r`: output the sum of `a[l..r]`

![Problem Illustration](../images/SEG-014/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `SETPREFIX` or `SUM`

## Output Format

- For each `SUM`, print the range sum

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= n`

## Example

**Input:**

```
3 2
1 2 3
SETPREFIX 2 5
SUM 0 2
```

**Output:**

```
13
```

**Explanation:**

After the prefix assignment, the array is `[5, 5, 3]`, so the sum is 13.

![Example Visualization](../images/SEG-014/example-1.png)

## Notes

- This is a range assignment on a prefix
- Use a segment tree with lazy assignment tags
- Each operation is O(log n)
- Sums may require 64-bit integers

## Related Topics

Segment Tree, Range Assignment, Prefix Updates

---

## Solution Template
### Java


### Python


### C++


### JavaScript

