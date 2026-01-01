---
problem_id: SRT_LONGEST_CONSECUTIVE_ONE_CHANGE__6194
display_id: SRT-011
slug: longest-consecutive-one-change
title: "Longest Consecutive After At Most One Change"
difficulty: Medium
difficulty_score: 53
topics:
  - Sorting
  - Prefix Suffix
  - Arrays
tags:
  - arrays
  - prefix-suffix
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-011: Longest Consecutive After At Most One Change

## Problem Statement

Given an array, you may change at most one element to any value. Find the maximum length of a strictly increasing contiguous subarray you can obtain.

![Problem Illustration](../images/SRT-011/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: maximum possible length

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
6
1 2 3 7 5 6
```

**Output:**

```
6
```

**Explanation:**

Change `7` to `4` to get `[1,2,3,4,5,6]`.

![Example Visualization](../images/SRT-011/example-1.png)

## Notes

- Precompute longest increasing prefix and suffix lengths
- Try bridging around each index with one change
- The answer is at least the original longest run
- Time complexity: O(n)

## Related Topics

Arrays, Prefix/Suffix, Optimization

---

## Solution Template
### Java


### Python


### C++


### JavaScript

