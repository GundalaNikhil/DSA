---
problem_id: GEO_POINT_LINE_DISTANCE__6402
display_id: GEO-013
slug: point-line-distance
title: "Point-Line Distance"
difficulty: Easy
difficulty_score: 35
topics:
  - Computational Geometry
  - Distance
tags:
  - geometry
  - distance
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-013: Point-Line Distance

## Problem Statement

Given a line segment `AB` with endpoints `A(x1, y1)` and `B(x2, y2)` and a point `P(px, py)`, compute the shortest distance from `P` to the segment.

Print the distance as a floating-point number rounded to 6 decimals.

## ASCII Visual

```
A ●------------------● B
         |
         | shortest
         |
         ● P
```

## Input Format

- Single line: six integers `x1 y1 x2 y2 px py`

## Output Format

- Single floating number: minimum distance from `P` to segment `AB`, rounded to 6 decimals

## Constraints

- `-10^9 <= coordinates <= 10^9`
- `A` and `B` are distinct

## Example

**Input:**
```
0 0 2 0 1 1
```

**Output:**
```
1.000000
```

**Explanation:**

Segment lies on x-axis; perpendicular from `P` meets segment at `(1,0)`, distance 1.

## Notes

- Project `P` onto the line; if projection lies outside the segment, take distance to nearest endpoint.
- Use doubles; avoid overflow by using 64-bit intermediates.

## Related Topics

Distance Computation, Vector Projection

---

## Solution Template

### Java


### Python


### C++


### JavaScript

