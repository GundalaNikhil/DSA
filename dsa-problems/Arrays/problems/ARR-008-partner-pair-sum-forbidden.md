---
problem_id: ARR_PAIR_SUM_FORBIDDEN__8320
display_id: ARR-008
slug: partner-pair-sum-forbidden
title: "Partner Pair Sum With Forbidden"
difficulty: Medium
difficulty_score: 36
topics:
  - Arrays
  - Two Pointers
  - Hashing
tags:
  - arrays
  - two-pointers
  - hashing
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-008: Partner Pair Sum With Forbidden

## Problem Statement

Given a sorted array and a target sum, determine if there exists a pair of elements that sums to the target such that neither index is in the forbidden set.

![Problem Illustration](../images/ARR-008/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i] (sorted)
- Third line: integer target
- Fourth line: integer f, the number of forbidden indices
- Fifth line: f space-separated indices (0-based); if f = 0, this line is omitted

## Output Format

Print "true" if a valid pair exists, otherwise "false".

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= arr[i], target <= 1000000000`
- `0 <= f <= n`

## Example

**Input:**
```
4
1 4 6 7
11
1
0
```

**Output:**
```
true
```

**Explanation:**

Indices 1 and 3 are not forbidden, and 4 + 7 = 11.

![Example Visualization](../images/ARR-008/example-1.png)

## Notes

- Forbidden indices are 0-based.
- Two-pointer scans should skip forbidden indices.

## Related Topics

Arrays, Two Pointers, Hashing

---

## Solution Template

### Java



### Python



### C++



### JavaScript


