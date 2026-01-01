---
problem_id: GEO_SEGMENT_RECT_INTERSECT__5580
display_id: GEO-015
slug: segment-rectangle-intersection
title: "Segment-Rectangle Intersection"
difficulty: Medium
difficulty_score: 50
topics:
  - Computational Geometry
  - Segment Intersection
  - Axis-Aligned Rectangle
tags:
  - geometry
  - intersection
  - rectangle
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-015: Segment-Rectangle Intersection

## Problem Statement

Given an axis-aligned rectangle with corners `(xL, yB)` (bottom-left) and `(xR, yT)` (top-right), and a line segment with endpoints `P1(x1, y1)` and `P2(x2, y2)`, determine whether the segment intersects or lies within the rectangle.

Intersection counts if the segment touches or crosses the rectangle boundary.

Print `true` if they intersect, otherwise `false`.

## ASCII Visual

```
Rect:
 (xL,yT) ●-------● (xR,yT)
         |       |
         |       |
 (xL,yB) ●-------● (xR,yB)

Segment that crosses any edge or lies inside → true
```

## Input Format

- Single line: six integers `xL yB xR yT x1 y1 x2 y2`

## Output Format

- Single word: `true` or `false`

## Constraints

- `-10^9 <= coordinates <= 10^9`
- `xL < xR`, `yB < yT`
- Segment endpoints may be outside the rectangle

## Example

**Input:**
```
0 0 2 2 -1 1 1 1
```

**Output:**
```
true
```

**Explanation:**

Segment crosses the left edge at `(0,1)`.

## Notes

- Check if either endpoint is inside; else test segment intersection with each of the 4 rectangle edges.
- Use orientation/on-segment predicates with 64-bit safety.

## Related Topics

Segment Intersection, Bounding Boxes, Orientation Test

---

## Solution Template

### Java


### Python


### C++


### JavaScript

