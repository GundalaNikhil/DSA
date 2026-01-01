---
problem_id: GEO_CLOSEST_PAIR_POINTS__5901
display_id: GEO-004
slug: closest-pair-points
title: "Closest Pair of Points"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Divide and Conquer
  - Sorting
tags:
  - geometry
  - closest-pair
  - divide-and-conquer
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-004: Closest Pair of Points

## Problem Statement

Given `n` points in 2D, find the **minimum squared Euclidean distance** between any pair of distinct points.

Return that squared distance as an integer.

## ASCII Visual

```
Points:
● (0,0)   ● (3,4)
      ● (1,1)

Closest pair: (0,0) and (1,1) with dist^2 = 1^2 + 1^2 = 2
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single integer: minimum squared distance among all pairs

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`
- Points are not guaranteed distinct (distance can be 0).

## Example

**Input:**
```
3
0 0
3 4
1 1
```

**Output:**
```
2
```

**Explanation:**

Closest pair is `(0,0)` and `(1,1)` with squared distance `2`.

## Notes

- Using squared distance avoids floating-point operations.
- Divide-and-conquer with a strip check achieves `O(n log n)`.
- If duplicate points exist, answer is `0`.

## Related Topics

Computational Geometry, Sorting, Divide and Conquer

---

## Solution Template

### Java


### Python


### C++


### JavaScript

