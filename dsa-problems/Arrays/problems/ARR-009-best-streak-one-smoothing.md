---
problem_id: ARR_BEST_STREAK_SMOOTH__2467
display_id: ARR-009
slug: best-streak-one-smoothing
title: "Best Streak With One Smoothing"
difficulty: Medium
difficulty_score: 54
topics:
  - Arrays
  - Dynamic Programming
  - Kadane
tags:
  - arrays
  - dynamic-programming
  - kadane
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-009: Best Streak With One Smoothing

## Problem Statement

You must pick exactly one index i (1 <= i <= n-2) and replace a[i] with floor((a[i-1] + a[i] + a[i+1]) / 3). After this smoothing, compute the maximum subarray sum. Return the maximum possible value.

![Problem Illustration](../images/ARR-009/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]

## Output Format

Print the maximum subarray sum achievable after one smoothing.

## Constraints

- `3 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`

## Example

**Input:**
```
4
-2 3 -4 5
```

**Output:**
```
9
```

**Explanation:**

Smooth index 2: (-4) becomes floor((3 - 4 + 5)/3) = 1. The array becomes
[-2, 3, 1, 5], whose maximum subarray sum is 9.

![Example Visualization](../images/ARR-009/example-1.png)

## Notes

- You must smooth exactly one middle element.
- Use 64-bit arithmetic for sums.

## Related Topics

Kadane, Dynamic Programming, Arrays

---

## Solution Template

### Java



### Python



### C++



### JavaScript


