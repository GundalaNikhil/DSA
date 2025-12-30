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
---

# GEO-007: Rotating Calipers Diameter

## 📋 Problem Summary

Given a convex polygon in CCW order, find the maximum squared distance between any two vertices (the polygon’s diameter).

## 🌍 Real-World Scenario

**Scenario Title:** Warehouse Drone Range Check**

Before flying perimeter routes, a warehouse drone computes the farthest pair of boundary points. That distance bounds the maximum straight-line flight needed to cross the site, ensuring battery capacity suffices.

**Why This Problem Matters:**

- Rotating calipers is a staple convex-geometry tool (also used for width, antipodal pairs).
- Runs in `O(n)` after a single pass—critical for `n = 1e5`.
- Shows how convexity eliminates `O(n^2)` pair checks.

## Emoji Visuals

```
🟩 Square (0,0)-(1,0)-(1,1)-(0,1)
Farthest pair: 🟢(0,0) ↔ 🟢(1,1)  dist^2 = 2

⬜ Rectangle (0,0)-(4,0)-(4,1)-(0,1)
Farthest pair: 🟢(0,0) ↔ 🟢(4,1)  dist^2 = 17
```

## Detailed Explanation

### Antipodal Pairs via Rotating Calipers

For a convex polygon `P`:

1. Start with `i = 0` (lowest x then y) and `j = 1` such that area of triangle `(i, i+1, j+1)` is maximized (typical calipers init).
2. For each edge `i -> i+1`, rotate the caliper by advancing `j` while `area(i, i+1, j+1) > area(i, i+1, j)`.
3. Track `dist^2` for pairs `(i, j)` and `(i+1, j)` as you advance.
4. Repeat for all `i` (mod n).

Because the polygon is convex, every antipodal pair is visited once; the maximum distance lies among these pairs.

### Distance Computation

Squared distance between points `a(x1,y1)` and `b(x2,y2)`:

```
d2 = (x1 - x2)^2 + (y1 - y2)^2
```

Use 64-bit (or bigger) for `d2`.

### Why It Works

Antipodal pairs are exactly the vertex pairs that can be touched by parallel supporting lines. As the calipers rotate around the hull, the farthest pair must occur at some antipodal configuration. Convexity guarantees no missed pair.

### Edge Cases

- `n = 3` (triangle): algorithm still works; all pairs may be checked.
- Degenerate distances when coordinates repeat (still convex input per constraints).
- Large coordinates: `d2` fits in 128-bit; in Java/C++ use `long`/`long long`.

## Input/Output Clarifications

- Vertices are CCW, convex, and distinct in position order.
- Output is squared distance (integer).
- No need for square roots or floating point.

## Naive Approach

**Algorithm:** Check every pair of vertices.  
**Time:** `O(n^2)`; **Space:** `O(1)`.  
**Why It Fails:** `n = 1e5` makes `1e10` checks impossible.

## Optimal Approach (Rotating Calipers)

**Algorithm:**
1. Read points `p[0..n-1]`.
2. Find index `j = argmax area(p[n-1], p[0], p[j])` by moving `j` while area increases.
3. Set `best = 0`.
4. For `i` from `0` to `n-1`:
   - Update `best` with `dist2(p[i], p[j])`.
   - While `area(p[i], p[i+1], p[j+1]) > area(p[i], p[i+1], p[j])`, advance `j = (j+1)%n` and update `best`.
5. Return `best`.

**Time Complexity:** `O(n)` after linear scan.  
**Space Complexity:** `O(1)` beyond the points.

## Reference Implementations

### Python

```python
from typing import List, Tuple

def diameter_squared(xs: List[int], ys: List[int]) -> int:
    n = len(xs)
    pts = [(xs[i], ys[i]) for i in range(n)]

    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

    def dist2(a, b):
        dx = a[0]-b[0]; dy = a[1]-b[1]
        return dx*dx + dy*dy

    if n == 1:
        return 0
    j = 1
    best = 0
    for i in range(n):
        ni = (i+1)%n
        while cross(pts[i], pts[ni], pts[(j+1)%n]) > cross(pts[i], pts[ni], pts[j]):
            j = (j+1)%n
        best = max(best, dist2(pts[i], pts[j]), dist2(pts[ni], pts[j]))
    return best


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
```

### Java

```java
class Solution {
    private long cross(long ax, long ay, long bx, long by, long cx, long cy) {
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
    }
    private long dist2(long ax, long ay, long bx, long by) {
        long dx = ax - bx, dy = ay - by;
        return dx*dx + dy*dy;
    }
    public long diameterSquared(int[] xs, int[] ys) {
        int n = xs.length;
        long best = 0;
        int j = 1;
        for (int i = 0; i < n; i++) {
            int ni = (i + 1) % n;
            while (cross(xs[i], ys[i], xs[ni], ys[ni], xs[(j+1)%n], ys[(j+1)%n]) >
                   cross(xs[i], ys[i], xs[ni], ys[ni], xs[j], ys[j])) {
                j = (j + 1) % n;
            }
            best = Math.max(best, dist2(xs[i], ys[i], xs[j], ys[j]));
            best = Math.max(best, dist2(xs[ni], ys[ni], xs[j], ys[j]));
        }
        return best;
    }
}
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long diameterSquared(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    auto cross = [&](int a, int b, int c)->long long{
        return (xs[b]-xs[a])*(ys[c]-ys[a]) - (ys[b]-ys[a])*(xs[c]-xs[a]);
    };
    auto dist2 = [&](int a, int b)->long long{
        long long dx = xs[a]-xs[b], dy = ys[a]-ys[b];
        return dx*dx + dy*dy;
    };
    long long best = 0;
    int j = 1;
    for (int i = 0; i < n; ++i) {
        int ni = (i+1)%n;
        while (cross(i, ni, (j+1)%n) > cross(i, ni, j)) j = (j+1)%n;
        best = max(best, dist2(i, j));
        best = max(best, dist2(ni, j));
    }
    return best;
}
```

### JavaScript

```javascript
function diameterSquared(xs, ys) {
  const n = xs.length;
  const cross = (a, b, c) =>
    (xs[b]-xs[a]) * (ys[c]-ys[a]) - (ys[b]-ys[a]) * (xs[c]-xs[a]);
  const dist2 = (a, b) => {
    const dx = xs[a]-xs[b], dy = ys[a]-ys[b];
    return dx*dx + dy*dy;
  };
  let best = 0;
  let j = 1;
  for (let i = 0; i < n; i++) {
    const ni = (i + 1) % n;
    while (cross(i, ni, (j + 1) % n) > cross(i, ni, j)) j = (j + 1) % n;
    best = Math.max(best, dist2(i, j), dist2(ni, j));
  }
  return best;
}
```

### Common Mistakes to Avoid

1. **Using `O(n^2)` pair scans.** Too slow for `n = 1e5`.
2. **Non-convex input.** Algorithm assumes convexity; if not convex, calipers is invalid.
3. **Forgetting wrap-around.** Use modulo when advancing indices.
4. **Overflow in distance.** Use 64-bit for `dx*dx + dy*dy`.
5. **Missing both pairs per step.** Check `(i, j)` and `(i+1, j)` to catch maxima on either vertex of the edge.

### Complexity Analysis

- **Time:** `O(n)` after the initial ordering (already given CCW).
- **Space:** `O(1)` extra.

## Testing Strategy

- Square and rectangle (known diameters).
- Triangle (max is a side or vertex pair).
- Regular hexagon (diameter is opposing vertices).
- Large coordinates to stress overflow.
- Thin rectangle to ensure calipers catch far corners.

## Emoji Recap

```
📏 Rotate parallel calipers around the convex hull 🌀
🔍 Track farthest antipodal pairs
✅ Return max squared distance
```
