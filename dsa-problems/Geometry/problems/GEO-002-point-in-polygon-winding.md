---
problem_id: GEO_POINT_IN_POLYGON__8742
display_id: GEO-002
slug: point-in-polygon-winding
title: "Point in Polygon (Winding)"
difficulty: Medium
difficulty_score: 50
topics:
  - Computational Geometry
  - Polygon
  - Winding Number
tags:
  - geometry
  - polygon
  - winding-number
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-002: Point in Polygon (Winding)

## Problem Statement

Given a simple polygon with `n` vertices in 2D and a query point `Q`, determine whether `Q` is **inside**, **outside**, or on the **boundary** of the polygon using a winding-number style test.

Print one word: `inside`, `outside`, or `boundary`.


```
         P3(4,4)
          ●
         / \
        /   \
 P4(0,4)●    \
 |             ● P2(4,0)
 |              /
 ● P1(0,0)     /
        \     /
         \   /
          \ /
           ● Q(2,2)   => inside
```

## Input Format

- First line: integer `n` (number of polygon vertices)
- Next `n` lines: two integers `xi yi` for each vertex, in order (clockwise or counterclockwise)
- Last line: two integers `qx qy` for the query point `Q`

## Output Format

- Single word: `inside`, `outside`, or `boundary`

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi, qx, qy <= 10^9`
- Polygon is simple (non-self-intersecting); vertices are distinct.

## Example

**Input:**
```
4
0 0
4 0
4 4
0 4
2 2
```

**Output:**
```
inside
```

**Explanation:**

Point `(2,2)` lies strictly inside the axis-aligned square.


```
P4 ●-------● P3
   |       |
   |  Q ●  |
   |       |
P1 ●-------● P2
```

## Notes

- Points exactly on an edge or vertex must return `boundary`.
- Winding number (or an equivalent ray-crossing count with sign) should be used; avoid floating-point angle sums.
- Use 64-bit arithmetic to avoid overflow in cross products with large coordinates.

## Related Topics

Computational Geometry, Polygon Containment, Cross Product

---

## Solution Template

### Java


### Python


### C++


### JavaScript

