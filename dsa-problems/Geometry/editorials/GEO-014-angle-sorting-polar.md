---
problem_id: GEO_ANGLE_SORTING_POLAR__2841
display_id: GEO-014
slug: angle-sorting-polar
title: "Angle Sorting for Polar Order"
difficulty: Easy-Medium
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
---

# GEO-014: Angle Sorting for Polar Order

## 📋 Problem Summary

Given `n` points (none at the origin), output them sorted by polar angle around the origin in counterclockwise order. Ties (same angle) are broken by distance to the origin (closer first).

## 🌍 Real-World Scenario

**Scenario Title:** Radar Target Sweep**

A radar marks targets relative to its origin. To render them in sweep order, targets are sorted by angle. If two align on the same bearing, the closer appears first.

**Why This Problem Matters:**

- Polar sorting underpins convex hull algorithms and angular sweeps.
- Shows how to avoid `atan2` by using half-plane partition + cross product for speed and stability.

## ASCII Visual

```
   y
   ↑     ● (1,1)
   |  ● (1,0)   ● (0,1)
   |
   O------------→ x
```

Order: (1,0) → (1,1) → (0,1) → ... continuing CCW.

## Detailed Explanation

### Half-Plane Partition

Classify a point `(x,y)` as:
- Upper half: `y > 0` or `y == 0 && x > 0`
- Lower half: otherwise

When sorting:
1. Points in the upper half come before points in the lower half.
2. If two points are in the same half, order by cross product sign:
   - For `a` then `b`, `cross(a, b) > 0` ⇒ `a` before `b` (CCW).
   - If `cross == 0`, tie-break by radius `r^2 = x^2 + y^2` (smaller first).

This avoids computing angles explicitly.

### Cross Product

`cross(a, b) = a.x * b.y - a.y * b.x`  
Positive => `b` is CCW from `a`.

### Why This Works

Sorting by half then cross product matches the order of `atan2(y,x)`:
- Half determines whether angle is in `[0, π)` or `[π, 2π)`.
- Cross product compares angles within the same half.

## Input/Output Clarifications

- No point equals (0,0).
- Points are distinct.
- Output exactly the points in sorted order, one per line.

## Naive Approach

**Algorithm:** Compute `atan2(y,x)` for each point; sort by angle then radius.

**Limitations:** Uses floating point angles; slower and subject to precision issues.

## Optimal Approach (Half-Plane + Cross)

**Algorithm:**
1. Define `half(p)` as above.
2. Sort points with comparator:
   - If `half(a) != half(b)`, `half(a) < half(b)` first.
   - Else, if `cross(a, b) != 0`, order by cross sign.
   - Else, order by squared radius.
3. Output sorted list.

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(1)` beyond storage.

## Reference Implementations

### Python

```python
def sort_by_angle(xs, ys):
    pts = list(zip(xs, ys))
    def half(p):
        x,y = p
        return 0 if (y > 0 or (y == 0 and x > 0)) else 1
    def key(p):
        return (half(p), 0)  # comparator implemented manually below
    pts.sort(key=lambda p: (half(p), 0))  # placeholder
    pts.sort(key=lambda p: (half(p),), reverse=False)
    pts.sort(key=None)  # will override with comparator below
    # better: use sorted with cmp
    pts = sorted(pts, key=lambda p: (half(p),), cmp=None)
    return pts
```

*(In practice, implement a comparator; Python’s `sorted` doesn’t take cmp in modern versions, so use functools.cmp_to_key.)*

```python
import functools
def sort_by_angle(xs, ys):
    pts = list(zip(xs, ys))
    def half(p):
        x,y = p
        return 0 if (y > 0 or (y == 0 and x > 0)) else 1
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        cross = a[0]*b[1] - a[1]*b[0]
        if cross != 0:
            return -1 if cross > 0 else 1
        ra = a[0]*a[0] + a[1]*a[1]
        rb = b[0]*b[0] + b[1]*b[1]
        if ra == rb: return 0
        return -1 if ra < rb else 1
    pts.sort(key=functools.cmp_to_key(cmp))
    return pts
```

### Java

```java
class Solution {
    public List<long[]> sortByAngle(int[] xs, int[] ys) {
        int n = xs.length;
        List<long[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new long[]{xs[i], ys[i]});
        pts.sort((a, b) -> {
            int ha = (a[1] > 0 || (a[1] == 0 && a[0] > 0)) ? 0 : 1;
            int hb = (b[1] > 0 || (b[1] == 0 && b[0] > 0)) ? 0 : 1;
            if (ha != hb) return ha - hb;
            long cross = a[0]*b[1] - a[1]*b[0];
            if (cross != 0) return cross > 0 ? -1 : 1;
            long ra = a[0]*a[0] + a[1]*a[1];
            long rb = b[0]*b[0] + b[1]*b[1];
            return Long.compare(ra, rb);
        });
        return pts;
    }
}
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<long long,long long>> sortByAngle(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    vector<pair<long long,long long>> pts(n);
    for (int i = 0; i < n; ++i) pts[i] = {xs[i], ys[i]};
    auto half = [](const pair<long long,long long>& p) {
        return (p.second > 0 || (p.second == 0 && p.first > 0)) ? 0 : 1;
    };
    sort(pts.begin(), pts.end(), [&](auto &a, auto &b){
        int ha = half(a), hb = half(b);
        if (ha != hb) return ha < hb;
        long long cross = a.first * b.second - a.second * b.first;
        if (cross != 0) return cross > 0;
        long long ra = a.first * a.first + a.second * a.second;
        long long rb = b.first * b.first + b.second * b.second;
        return ra < rb;
    });
    return pts;
}
```

### JavaScript

```javascript
function sortByAngle(xs, ys) {
  const pts = xs.map((x, i) => [x, ys[i]]);
  const half = ([x,y]) => (y > 0 || (y === 0 && x > 0)) ? 0 : 1;
  pts.sort((a, b) => {
    const ha = half(a), hb = half(b);
    if (ha !== hb) return ha - hb;
    const cross = a[0]*b[1] - a[1]*b[0];
    if (cross !== 0) return cross > 0 ? -1 : 1;
    const ra = a[0]*a[0] + a[1]*a[1];
    const rb = b[0]*b[0] + b[1]*b[1];
    return ra - rb;
  });
  return pts;
}
```

## Common Mistakes to Avoid

1. **Using `atan2` everywhere.** Slower and can misorder near 180° vs -180°; half+cross avoids that.
2. **Origin point present.** The problem forbids it; if present, handle separately.
3. **Wrong tie-break for same angle.** Must use radius to order closer first.
4. **Half-plane definition errors.** Ensure `(y > 0) or (y == 0 and x > 0)` defines the upper half.

## Complexity Analysis

- **Time:** `O(n log n)`  
- **Space:** `O(1)` beyond input storage.

## Testing Strategy

- Points in all four quadrants.
- Collinear with origin (same angle) to test radius tie-break.
- Only upper-half or only lower-half points.
- Large coordinate magnitudes (cross fits in 128-bit if needed).

## ASCII Recap

```
Half = upper? else lower
Sort by (half, cross>0?, radius)
```
