---
problem_id: GEO_ANGLE_SORTING_POLAR__2841
display_id: GEO-014
slug: angle-sorting-polar
title: "Angle Sorting for Polar Order"
difficulty: Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Sorting
tags:
  - geometry
  - sorting
  - polar-angle
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-014: Angle Sorting for Polar Order

## Problem Statement

Given `n` points (distinct, no point at the origin), sort them by polar angle around the origin (0,0), in counterclockwise order. If two points have the same angle, the closer one (smaller distance to origin) should come first.

Output the points in the required order.

## ASCII Visual

```
   y
   ↑     ● (1,1)
   |  ● (1,0)   ● (0,1)
   |
   O------------→ x
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- `n` lines, each `x y` in the sorted order

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- No point is at the origin; points are distinct

## Example

**Input:**
```
3
1 0
1 1
0 1
```

**Output:**
```
1 0
1 1
0 1
```

**Explanation:**

Angles: (1,0) at 0°, (1,1) at 45°, (0,1) at 90°.

## Notes

- Use half-plane partition (upper vs lower) then cross product to sort without `atan2` for performance and stability.
- Tie-break by radius when cross product is zero.

## Related Topics

Sorting by Angle, Cross Product, Polar Coordinates

---

## Solution Template

### Java


### Python


### C++


### JavaScript

