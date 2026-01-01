---
problem_id: GEO_CONVEX_HULL_CAPPED__2407
display_id: GEO-005
slug: convex-hull-capped
title: "Convex Hull with Interior Caps"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Convex Hull
  - Geometry Filtering
tags:
  - geometry
  - convex-hull
  - filtering
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-005: Convex Hull with Interior Caps

## Problem Statement

Given `n` points in 2D and an angle threshold `theta` (degrees, `0 < theta < 180`):

1. Build the convex hull of the points (include collinear boundary points as needed for a standard hull).
2. For each hull vertex, compute its interior angle (in degrees, using the CCW hull order).
3. Discard any hull vertex whose interior angle is **strictly less than** `theta`.
4. Return the remaining “capped” hull vertices in counterclockwise (CCW) order. If all vertices are discarded, output `0`.

Print the vertex count, followed by the remaining vertices.

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`
- Last line: integer `theta`

## Output Format

- First line: integer `k` = number of capped hull vertices
- Next `k` lines (if `k > 0`): `x y` for each vertex in CCW order

## ASCII/Emoji Visual

```
🟢 square hull, theta = 60°
  ● (0,0) ---- ● (4,0)
  |              |
  |      ●       |   => keep all 4 (90° ≥ 60°)
  ● (0,4) ---- ● (4,4)

🔺 triangle hull, theta = 80°
        ●
       / \
      /   \
   ● ----- ●
   all angles 60° < 80° ⇒ discard all ⇒ k = 0
```

## Constraints

- `3 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`
- `0 < theta < 180`

## Example 1

**Input:**
```
5
0 0
4 0
4 4
0 4
2 2
60
```

**Output:**
```
4
0 0
4 0
4 4
0 4
```

**Explanation:** Square hull has interior angles 90°, all ≥ 60°, so nothing is capped away.

## Example 2

**Input:**
```
4
0 0
2 2
4 0
2 -2
100
```

**Output:**
```
0
```

**Explanation:** Hull is a diamond with interior angles 90°; all are < 100°, so every vertex is discarded.

## Notes

- Interior angle is measured inside the polygon; for a convex hull it lies in `(0, 180]`.
- Use squared lengths to avoid precision issues when comparing angles (via cross and dot, or cosine).
- If `k = 0`, print just `0`.

## Related Topics

Convex Hull, Geometry Filtering, Cross Product

---

## Solution Template

### Java


### Python


### C++


### JavaScript

