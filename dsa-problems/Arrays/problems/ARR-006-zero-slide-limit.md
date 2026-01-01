---
problem_id: ARR_ZERO_SLIDE_LIMIT__4908
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Easy-Medium
difficulty_score: 34
topics:
  - Arrays
  - Two Pointers
  - Simulation
tags:
  - arrays
  - two-pointers
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-006: Zero Slide With Limit

## Problem Statement

Move all zeros to the end of the array, but you may perform at most m swaps in total. Once the swap budget is exhausted, stop and return the current array.

![Problem Illustration](../images/ARR-006/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer m, the maximum number of swaps

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 1000000000`

## Example

**Input:**
```
5
0 4 0 5 7
1
```

**Output:**
```
4 0 0 5 7
```

**Explanation:**

One swap moves 4 left of a zero, and the swap budget is exhausted.

![Example Visualization](../images/ARR-006/example-1.png)

## Notes

- A swap is counted when a non-zero moves left across a zero.
- Stop immediately when the swap count reaches m.

## Related Topics

Arrays, Two Pointers

---

## Solution Template

### Java



### Python



### C++



### JavaScript


