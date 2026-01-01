---
problem_id: ARR_WEIGHTED_BALANCE_POINT__7742
display_id: ARR-005
slug: weighted-balance-point
title: "Weighted Balance Point"
difficulty: Medium
difficulty_score: 44
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-005: Weighted Balance Point

## Problem Statement

Find the smallest index i such that the weighted sum of elements to the left of i equals the weighted sum of elements to the right of i. The left side excludes i and is multiplied by L, the right side excludes i and is multiplied by R.

![Problem Illustration](../images/ARR-005/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers a[i]
- Third line: two integers L and R

## Output Format

Print the smallest index i (0-based) that satisfies the condition, or -1.

## Constraints

- `1 <= n <= 200000`
- `-1000000000 <= a[i] <= 1000000000`
- `1 <= L, R <= 1000000`

## Example

**Input:**
```
5
2 3 -1 3 2
2 1
```

**Output:**
```
2
```

**Explanation:**

At i = 2, left sum is 5 and right sum is 8. 5 * 2 == 8 * 1, so the answer is 2.

![Example Visualization](../images/ARR-005/example-1.png)

## Notes

- Use 64-bit integers to avoid overflow.
- Left and right sums exclude index i.

## Related Topics

Arrays, Prefix Sum, Math

---

## Solution Template

### Java



### Python



### C++



### JavaScript


