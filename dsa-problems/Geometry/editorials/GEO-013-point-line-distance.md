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
---

# GEO-013: Point-Line Distance

## 📋 Problem Summary

Given segment `AB` and point `P`, find the shortest distance from `P` to the segment. Output as a floating value with 6 decimals.

## 🌍 Real-World Scenario

**Scenario Title:** Nearest Edge for a Robot**

A robot knows its position `P` and a wall segment `AB`. It must compute the shortest clearance to avoid collisions.

**Why This Problem Matters:**

- Fundamental geometry primitive used in collision detection, projections, and GIS.
- Reinforces vector projection and clamping to segment endpoints.

## ASCII Visual

```
A ●------------------● B
         |
         | shortest path
         |
         ● P
```

## Detailed Explanation

Let `u = B - A`, `v = P - A`.

Projection scalar `t = (u·v) / (u·u)`:

- If `t < 0`: closest point is `A`.
- If `t > 1`: closest point is `B`.
- Else: closest point is `A + t*u` on the segment.

Distance = Euclidean distance from `P` to that closest point.

Use doubles; `u·u` fits in 64-bit (coords up to 1e9 → squared up to 1e18).

## Input/Output Clarifications

- Input is one line of six integers.
- Segment endpoints are distinct.
- Output rounded to 6 decimals.

## Naive Approach

**Algorithm:** Check distance to infinite line, then clamp:
1. Compute projection `t`.
2. Clamp `t` to `[0,1]`.
3. Compute closest point and distance.

**Time/Space:** `O(1)`.

## Optimal Approach

Same as above—already optimal with constant work.

## Reference Implementations

### Python

```python
import math

def distance_point_segment(x1: int, y1: int, x2: int, y2: int, px: int, py: int) -> float:
    ux, uy = x2 - x1, y2 - y1
    vx, vy = px - x1, py - y1
    denom = ux*ux + uy*uy
    if denom == 0:
        return math.hypot(vx, vy)
    t = (ux*vx + uy*vy) / denom
    t = max(0.0, min(1.0, t))
    cx = x1 + t * ux
    cy = y1 + t * uy
    return math.hypot(px - cx, py - cy)
```

### Java

```java
class Solution {
    public double distancePointSegment(long x1, long y1, long x2, long y2, long px, long py) {
        long ux = x2 - x1, uy = y2 - y1;
        long vx = px - x1, vy = py - y1;
        long denom = ux*ux + uy*uy;
        if (denom == 0) return Math.hypot(vx, vy);
        double t = (ux * (double)vx + uy * (double)vy) / denom;
        t = Math.max(0.0, Math.min(1.0, t));
        double cx = x1 + t * ux;
        double cy = y1 + t * uy;
        return Math.hypot(px - cx, py - cy);
    }
}
```

### C++

```cpp
double distancePointSegment(long long x1, long long y1, long long x2, long long y2, long long px, long long py) {
    long long ux = x2 - x1, uy = y2 - y1;
    long long vx = px - x1, vy = py - y1;
    long long denom = ux*ux + uy*uy;
    if (denom == 0) return hypot((double)vx, (double)vy);
    double t = (ux * (double)vx + uy * (double)vy) / (double)denom;
    t = max(0.0, min(1.0, t));
    double cx = x1 + t * ux;
    double cy = y1 + t * uy;
    return hypot(px - cx, py - cy);
}
```

### JavaScript

```javascript
function distancePointSegment(x1, y1, x2, y2, px, py) {
  const ux = x2 - x1, uy = y2 - y1;
  const vx = px - x1, vy = py - y1;
  const denom = ux*ux + uy*uy;
  if (denom === 0) return Math.hypot(vx, vy);
  let t = (ux*vx + uy*vy) / denom;
  t = Math.max(0, Math.min(1, t));
  const cx = x1 + t * ux;
  const cy = y1 + t * uy;
  return Math.hypot(px - cx, py - cy);
}
```

### C++ommon Mistakes to Avoid

1. **Not clamping `t`.** Without clamping, you might pick a point beyond the segment.
2. **Endpoint zero-length segment.** Guard if `A == B`.
3. **Integer division.** Use doubles for projection.
4. **Precision formatting.** Ensure 6-decimal output.

### C++omplexity Analysis

- **Time:** `O(1)`  
- **Space:** `O(1)`

## Testing Strategy

- Point above the middle (perpendicular drop).
- Point beyond an endpoint (should pick nearest endpoint).
- Vertical/horizontal segments.
- Zero-length segment edge case.
- Large coordinates to stress overflow in products.

## ASCII Recap

```
Project P onto line AB:
  t = (u·v)/(u·u)
Clamp t to [0,1]; closest = A + t*u
Distance = |P - closest|
```
