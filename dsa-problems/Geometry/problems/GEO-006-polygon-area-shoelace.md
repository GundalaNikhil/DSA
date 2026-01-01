---
problem_id: GEO_POLYGON_AREA_SHOELACE__7719
display_id: GEO-006
slug: polygon-area-shoelace
title: "Polygon Area (Shoelace)"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Polygon
  - Shoelace Formula
tags:
  - geometry
  - area
  - shoelace
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-006: Polygon Area (Shoelace)

## Problem Statement

Given a simple polygon with `n` vertices listed in order (clockwise or counterclockwise), compute its **signed area**. Output the absolute area.

Use the shoelace formula; avoid floating point by working in twice-the-area and dividing at the end if needed.

## Emoji Visual

```
⬛ Square:
🟢 (0,0) ---- 🟢 (2,0)
|               |
|               |
🟢 (0,2) ---- 🟢 (2,2)
Area = 4
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi` for each vertex, in order

## Output Format

- Single integer: absolute area of the polygon

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- Polygon is simple (non-self-intersecting)

## Example

**Input:**
```
4
0 0
2 0
2 2
0 2
```

**Output:**
```
4
```

**Explanation:**

Axis-aligned square of side 2 has area 4.

## Notes

- Signed area from the shoelace sum may be negative if the order is clockwise; take `abs`.
- Twice-the-area fits in 128-bit; store in 64-bit carefully (`~2e18`).

## Related Topics

Polygon Geometry, Shoelace Formula, Cross Product

---

## Solution Template

### Java


### Python


### C++


### JavaScript

