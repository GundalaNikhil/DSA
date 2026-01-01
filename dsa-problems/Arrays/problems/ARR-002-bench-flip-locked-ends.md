---
problem_id: ARR_BENCH_FLIP_LOCKED__1397
display_id: ARR-002
slug: bench-flip-locked-ends
title: "Bench Flip With Locked Ends"
difficulty: Easy
difficulty_score: 20
topics:
  - Arrays
  - Two Pointers
  - In-place
tags:
  - arrays
  - two-pointers
  - in-place
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-002: Bench Flip With Locked Ends

## Problem Statement

Reverse the array in place, but keep the first and last elements fixed. Only the middle segment is reversed.

![Problem Illustration](../images/ARR-002/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]

## Output Format

Print the resulting array, space-separated.

## Constraints

- `2 <= n <= 200000`
- `-1000000000 <= arr[i] <= 1000000000`

## Example

**Input:**
```
5
9 3 8 1 5
```

**Output:**
```
9 1 8 3 5
```

**Explanation:**

The first and last elements stay. The middle subarray [3, 8, 1] is reversed to
[1, 8, 3].

![Example Visualization](../images/ARR-002/example-1.png)

## Notes

- If n <= 2, the array is unchanged.
- Use two pointers starting at indices 1 and n-2.

## Related Topics

Arrays, Two Pointers

---

## Solution Template

### Java



### Python



### C++



### JavaScript


