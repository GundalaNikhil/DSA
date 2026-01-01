---
problem_id: GEO_MIN_ENCLOSING_CIRCLE__4205
display_id: GEO-008
slug: minimum-enclosing-circle
title: "Minimum Enclosing Circle"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Randomized Algorithms
  - Circle
tags:
  - geometry
  - circle
  - randomized
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-008: Minimum Enclosing Circle

## Problem Statement

Given `n` points in 2D, find the smallest circle that encloses all the points. Output the center coordinates and the radius.

Return `cx cy r` with values rounded to 6 decimal places.

## ASCII Visual

```
Points:
● (0,0)   ● (1,0)
     ● (0,1)

Smallest enclosing circle:
center (0.5, 0.5), radius ≈ 0.707107
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single line: three floating values `cx cy r` (rounded to 6 decimals)

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**
```
3
0 0
1 0
0 1
```

**Output:**
```
0.500000 0.500000 0.707107
```

**Explanation:**

The circle centered at `(0.5, 0.5)` with radius `sqrt(0.5)` encloses all three points.

## Notes

- Use a randomized incremental algorithm (Welzl) for expected `O(n)`.
- Beware of precision; store as doubles, output rounded to 6 decimals.
- With one point, radius is 0 and center is that point.

## Related Topics

Circle Geometry, Randomized Algorithms

---

## Solution Template

### Java


### Python


### C++


### JavaScript

