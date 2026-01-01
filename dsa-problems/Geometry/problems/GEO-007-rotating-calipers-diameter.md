---
problem_id: GEO_ROTATING_CALIPERS_DIAM__3154
display_id: GEO-007
slug: rotating-calipers-diameter
title: "Rotating Calipers Diameter"
difficulty: Medium
difficulty_score: 55
topics:
  - Computational Geometry
  - Rotating Calipers
  - Convex Polygon
tags:
  - geometry
  - diameter
  - rotating-calipers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-007: Rotating Calipers Diameter

## Problem Statement

You are given a **convex** polygon with `n` vertices in counterclockwise order. Find the maximum squared distance between any pair of its vertices (the squared diameter of the polygon).

Return that maximum squared distance as an integer.

## Emoji Visual

```
🟢 Square (0,0)-(1,0)-(1,1)-(0,1)
Fartherst pair are opposite corners:
🟢(0,0) ..... 🟢(1,1)   dist^2 = 2
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi` in CCW order

## Output Format

- Single integer: maximum squared distance between any two vertices

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- Polygon is convex and vertices are given in CCW order

## Example

**Input:**
```
4
0 0
1 0
1 1
0 1
```

**Output:**
```
2
```

**Explanation:**

Opposite corners `(0,0)` and `(1,1)` give the diameter squared `2`.

## Notes

- Work with squared distances to avoid square roots.
- Rotating calipers over antipodal pairs gives `O(n)` after one pass.
- For triangles, check all three edges and vertices with calipers logic.

## Related Topics

Rotating Calipers, Convex Geometry, Distance Computation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

