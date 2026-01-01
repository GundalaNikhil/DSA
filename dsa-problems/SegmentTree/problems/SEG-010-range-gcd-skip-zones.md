---
problem_id: SEG_RANGE_GCD_SKIP_ZONES__6230
display_id: SEG-010
slug: range-gcd-skip-zones
title: "Range GCD with Skip Zones"
difficulty: Medium
difficulty_score: 54
topics:
  - Segment Tree
  - GCD
  - Dynamic Sets
tags:
  - segment-tree
  - gcd
  - toggles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# SEG-010: Range GCD with Skip Zones

## Problem Statement

You are given an array `a` and a set of forbidden indices. The GCD of a range is computed using only indices that are not forbidden.
Operations:

- `TOGGLE i`: flip whether index `i` is forbidden
- `SET i x`: set `a[i] = x`
- `GCD l r`: output the gcd of all allowed elements in `[l, r]`, or 0 if none
  ![Problem Illustration](../images/SEG-010/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Third line: integer `f` (initial forbidden count)
- Next `f` lines: forbidden indices
- Next `q` lines: operations `TOGGLE`, `SET`, or `GCD`

## Output Format

- For each `GCD`, print the gcd value

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based

## Example

**Input:**

```
3 3
6 9 3
1
1
GCD 0 2
TOGGLE 1
GCD 0 2
```

**Output:**

```
3
3
```

**Explanation:**
Initially index 1 is forbidden, so gcd(6,3) = 3. After toggling, all indices are allowed and gcd(6,9,3) = 3.
![Example Visualization](../images/SEG-010/example-1.png)

## Notes

- Store gcd in a segment tree, but ignore forbidden indices
- You can represent forbidden indices as zeroed values
- GCD of an empty set is 0
- Use absolute values for gcd on negatives

## Related Topics

## Segment Tree, GCD, Range Queries

## Solution Template

### Java


### Python


### C++


### JavaScript

