---
problem_id: DP_LIS_DIFF_RANGE__5881
display_id: DP-006
slug: strict-jump-lis-bounded
title: "Strict Jump LIS With Max Gap"
difficulty: Medium
difficulty_score: 64
topics:
  - Dynamic Programming
  - Segment Tree
  - Coordinate Compression
tags:
  - dp
  - lis
  - segment-tree
  - fenwick
  - medium
premium: true
subscription_tier: basic
time_limit: 3000
memory_limit: 256
---

# DP-006: Strict Jump LIS With Max Gap

## Problem Statement

You are given an integer array `a` of length `n` and two integers `d` and `g` (`d <= g`).

Find the length of the longest subsequence `a[i1], a[i2], ..., a[ik]` (with `i1 < i2 < ... < ik`) such that for every consecutive pair:

`d <= a[i(t+1)] - a[i(t)] <= g`

Return the maximum possible length `k`.

![Problem Illustration](../images/DP-006/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers `a[i]`
- Third line: two integers `d` and `g`

## Output Format

Print one integer: the length of the longest valid subsequence.

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= a[i] <= 10^9`
- `0 <= d <= g <= 10^9`

## Example

**Input:**
```
5
1 3 4 9 10
2 6
```

**Output:**
```
3
```

**Explanation:**

One optimal subsequence is `1 -> 3 -> 9`:

- `3 - 1 = 2` (within [2,6])
- `9 - 3 = 6` (within [2,6])

So the answer is 3.

![Example Visualization](../images/DP-006/example-1.png)

## Notes

- This is a LIS-style problem, but the constraint is on the **difference range** `[d, g]`, not simply “increasing”.
- If `d = 0`, equal consecutive values are allowed (difference 0).
- `O(n^2)` DP will not pass for `n = 10^5`. You need a range-maximum data structure.

## Related Topics

Dynamic Programming, Coordinate Compression, Segment Tree / Fenwick Tree

---

## Solution Template

### Java


### Python


### C++


### JavaScript


