---
problem_id: BIT_MAX_OR_SUBARRAY_LEQ_K__8416
display_id: BIT-016
slug: max-or-subarray-leq-k
title: "Max Bitwise OR Subarray <= K"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - OR
  - Sliding Window
  - Array
tags:
  - bitwise
  - or-operation
  - sliding-window
  - subarray
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# BIT-016: Max Bitwise OR Subarray <= K

## Problem Statement

Find the length of the longest subarray `nums[i..j]` such that `nums[i] | nums[i+1] | ... | nums[j] <= K`.

![Problem Illustration](../images/BIT-016/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: integer K

## Output Format

Print the maximum length of a subarray with OR <= K.

## Constraints

- `1 <= n <= 200000`
- `0 <= a[i], K <= 1000000000`

## Example

**Input:**

```
4
1 2 4 1
7
```

**Output:**

```
4
```

**Explanation:**

The OR of the entire array is 7, so the maximum length is 4.

![Example Visualization](../images/BIT-016/example-1.png)

## Notes

- Use a sliding window with bit counts.
- All elements and K are non-negative.

## Related Topics

Bitwise Operations, Sliding Window

---

## Solution Template

### Java


### Python


### C++


### JavaScript

