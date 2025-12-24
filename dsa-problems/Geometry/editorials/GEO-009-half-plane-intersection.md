---
problem_id: GEO_HALF_PLANE_INTERSECTION__8834
display_id: GEO-009
slug: half-plane-intersection
title: "Half-Plane Intersection"
difficulty: Hard
difficulty_score: 80
topics:
  - Computational Geometry
  - Half-Plane Intersection
  - Convex Polygon
tags:
  - geometry
  - half-planes
  - deque
  - hard
premium: true
subscription_tier: basic
---

# GEO-009: Half-Plane Intersection

## 📋 Problem Summary

Given `m` half-planes `a*x + b*y <= c`, compute their intersection polygon. If empty, print `EMPTY`; otherwise print the vertices of the intersection in CCW order starting from the lowest x (then lowest y) vertex.

## 🌍 Real-World Scenario

**Scenario Title:** Safe Flight Envelope**

Airspace constraints (max altitude, min altitude, lateral bounds) can be modeled as half-planes. The feasible “safe envelope” is their intersection. If it’s empty, the route is invalid; otherwise the polygon represents the allowed region.

**Why This Problem Matters:**

- Classic convex-geometry problem beyond hulls and circles.
- Tests robustness with parallel lines and emptiness.
- Fundamental in linear programming (2D), clipping, and visibility.

## ASCII Visual

```
Half-planes:
  x >= 0      => -1*x <= 0
  x <= 1      =>  1*x <= 1
  y >= 0      => -1*y <= 0
  y <= 1      =>  1*y <= 1

Intersection:
(0,0) -> (1,0) -> (1,1) -> (0,1)
```

## Detailed Explanation

### Core Idea

The intersection of half-planes that are all on one side of their directed line is a convex (possibly empty) polygon. A standard `O(m log m)` algorithm:

1. **Normalize lines** and compute their angle `atan2(b, a)`.
2. **Sort** by angle; when angles tie, keep only the most restrictive (smallest `c` in the same direction).
3. **Deque sweep:** Process lines in sorted order, maintaining a deque of candidate lines whose intersection points form the current polygon edges. Before adding a new line, pop from back/front while the last intersection is outside the new half-plane. At the end, also clean up with the first line.
4. **Build polygon:** Intersections of consecutive deque lines plus the wrap-around intersection give the final polygon vertices.

Empty intersection arises when the deque shrinks below 2 or when parallel contradictory lines are encountered.

### Intersections

For lines `a1 x + b1 y = c1` and `a2 x + b2 y = c2`, the intersection is:
```
det = a1*b2 - a2*b1
x = (c1*b2 - c2*b1) / det
y = (a1*c2 - a2*c1) / det
```
Skip if `det == 0` (parallel); handle by keeping the tighter half-plane when directions align, or declaring empty if they point opposite with gap.

### Point-In-Half-Plane

Check `a*x + b*y <= c + EPS`. Use a small epsilon (`1e-9`) to tolerate floating error.

### Ordering Output

The deque gives vertices in CCW order. Start from the lowest x (then y) vertex by rotating the list before printing.

## Input/Output Clarifications

- Output `EMPTY` for empty intersection.
- Otherwise, print `k` then `k` lines of `x y` rounded to 6 decimals.
- Half-planes can be in any order; they may be redundant or contradictory.

## Naive Approach

**Algorithm:** Start with a huge bounding box polygon and iteratively clip it against each half-plane (Sutherland–Hodgman).  
**Time:** `O(m * k)` where `k` grows; `O(m^2)` worst-case.  
**Limitations:** Too slow for `1e5`; still useful conceptually.

## Optimal Approach (Sorted Half-Plane + Deque)

**Algorithm Steps:**

1. For each half-plane `(a,b,c)`, compute angle `ang = atan2(b, a)`. Normalize so `(a,b)` points toward the kept side.
2. Sort by `ang`; if same `ang`, keep only the one with smaller `c` (more restrictive).
3. Initialize deque with the first two lines that are not parallel.
4. For each next line `L`:
   - While deque size ≥ 2 and intersection of last two deque lines is outside `L`, pop back.
   - While deque size ≥ 2 and intersection of first two deque lines is outside `L`, pop front.
   - Push `L`.
5. After processing all lines, perform the same clean-up with the first/last lines to close the polygon.
6. If deque < 2 or lines are incompatible, intersection is empty.
7. Otherwise, compute intersection points of consecutive lines (including wrap), rotate to lowest `(x,y)`, and output.

**Time Complexity:** `O(m log m)`  
**Space Complexity:** `O(m)`

## Reference Implementations

### Python

```python
import math
from typing import List, Tuple

EPS = 1e-9

def half_plane_intersection(A: List[int], B: List[int], C: List[int]) -> List[Tuple[float, float]]:
    lines = []
    for a, b, c in zip(A, B, C):
        ang = math.atan2(b, a)
        lines.append((ang, a, b, c))
    # sort by angle, tie by offset along the normal (more restrictive first)
    lines.sort(key=lambda t: (t[0], t[3] / math.hypot(t[1], t[2])))

    # prune parallel lines keeping the tightest
    pruned = []
    for L in lines:
        if pruned and abs(L[0] - pruned[-1][0]) < EPS:
            normL = math.hypot(L[1], L[2])
            normP = math.hypot(pruned[-1][1], pruned[-1][2])
            if L[3] / normL < pruned[-1][3] / normP:
                pruned[-1] = L
        else:
            pruned.append(L)
    lines = pruned

    def intersect(L1, L2):
        _, a1, b1, c1 = L1
        _, a2, b2, c2 = L2
        det = a1 * b2 - a2 * b1
        if abs(det) < EPS:
            return None
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        return (x, y)

    def outside(p, L):
        _, a, b, c = L
        return a * p[0] + b * p[1] - c > EPS

    dq = []
    for L in lines:
        while len(dq) >= 2:
            p = intersect(dq[-2], dq[-1])
            if p is None or not outside(p, L):
                break
            dq.pop()
        while len(dq) >= 2:
            p = intersect(dq[0], dq[1])
            if p is None or not outside(p, L):
                break
            dq.pop(0)
        dq.append(L)

    # final cleanup to close the polygon
    while len(dq) >= 3:
        p = intersect(dq[-2], dq[-1])
        if p is None or not outside(p, dq[0]):
            break
        dq.pop()
    while len(dq) >= 3:
        p = intersect(dq[0], dq[1])
        if p is None or not outside(p, dq[-1]):
            break
        dq.pop(0)

    if len(dq) < 3:
        return []
    pts = []
    for i in range(len(dq)):
        p = intersect(dq[i], dq[(i + 1) % len(dq)])
        if p is None:
            return []
        pts.append(p)
    # rotate to lowest x, then y
    idx = min(range(len(pts)), key=lambda i: (pts[i][0], pts[i][1]))
    return pts[idx:] + pts[:idx]
```

### Java (outline)

```java
// Implementation follows the same deque method; ensure EPS checks and sorting by angle.
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-9;
struct Line {
    double ang, a, b, c;
};

pair<double,double> intersect(const Line& L1, const Line& L2) {
    double det = L1.a * L2.b - L2.a * L1.b;
    return {(L1.c * L2.b - L2.c * L1.b) / det,
            (L1.a * L2.c - L2.a * L1.c) / det};
}

bool outside(const pair<double,double>& p, const Line& L) {
    return L.a * p.first + L.b * p.second - L.c > EPS;
}

vector<pair<double,double>> halfPlaneIntersection(const vector<long long>& A, const vector<long long>& B, const vector<long long>& C) {
    int m = A.size();
    vector<Line> L;
    L.reserve(m);
    for (int i = 0; i < m; ++i) {
        Line ln; ln.a = A[i]; ln.b = B[i]; ln.c = C[i];
        ln.ang = atan2(ln.b, ln.a);
        L.push_back(ln);
    }
    sort(L.begin(), L.end(), [](const Line& x, const Line& y){
        if (fabs(x.ang - y.ang) > EPS) return x.ang < y.ang;
        return x.c / hypot(x.a, x.b) < y.c / hypot(y.a, y.b);
    });
    vector<Line> uniq;
    for (auto &ln : L) {
        if (!uniq.empty() && fabs(ln.ang - uniq.back().ang) < EPS) {
            // keep tighter
            if (ln.c / hypot(ln.a, ln.b) < uniq.back().c / hypot(uniq.back().a, uniq.back().b))
                uniq.back() = ln;
        } else uniq.push_back(ln);
    }
    deque<Line> dq;
    for (auto &ln : uniq) {
        while (dq.size() >= 2 && outside(intersect(dq[dq.size()-2], dq.back()), ln)) dq.pop_back();
        while (dq.size() >= 2 && outside(intersect(dq[0], dq[1]), ln)) dq.pop_front();
        dq.push_back(ln);
    }
    while (dq.size() >= 3 && outside(intersect(dq[dq.size()-2], dq.back()), dq[0])) dq.pop_back();
    while (dq.size() >= 3 && outside(intersect(dq[0], dq[1]), dq.back())) dq.pop_front();
    if (dq.size() < 2) return {};
    vector<pair<double,double>> poly;
    for (int i = 0; i < (int)dq.size(); ++i) {
        poly.push_back(intersect(dq[i], dq[(i+1)%dq.size()]));
    }
    int idx = min_element(poly.begin(), poly.end(), [](auto &p1, auto &p2){
        if (fabs(p1.first - p2.first) > EPS) return p1.first < p2.first;
        return p1.second < p2.second;
    }) - poly.begin();
    rotate(poly.begin(), poly.begin()+idx, poly.end());
    return poly;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  halfPlaneIntersection(A, B, C) {
    const EPS = 1e-9;
    const m = A.length;
    let lines = [];
    
    for (let i = 0; i < m; i++) {
      const a = Number(A[i]);
      const b = Number(B[i]);
      const c = Number(C[i]);
      const ang = Math.atan2(b, a);
      lines.push({ a, b, c, ang });
    }
    
    // Sort by angle
    lines.sort((l1, l2) => {
      if (Math.abs(l1.ang - l2.ang) > EPS) {
        return l1.ang - l2.ang;
      }
      // Tie-break: keep tighter constraint (smaller c / norm)
      // distance from origin is c / hypot(a,b)
      // If angles are same, they are parallel and point same direction.
      // We want the one with smaller c (shifted more towards negative normal)
      // Distance from origin along normal (a,b) is c/|n|.
      // Smaller c means closer to -infinity along normal direction.
      // So smaller c is more restrictive.
      const dist1 = l1.c / Math.hypot(l1.a, l1.b);
      const dist2 = l2.c / Math.hypot(l2.a, l2.b);
      return dist1 - dist2;
    });
    
    // Remove duplicates (parallel with same angle)
    const unique = [];
    for (const ln of lines) {
      if (unique.length > 0 && Math.abs(ln.ang - unique[unique.length - 1].ang) < EPS) {
        // Already sorted by restrictiveness, so the first one we saw was the most restrictive?
        // No, we sorted ascending by dist.
        // So the first one is smaller c (more restrictive).
        // Or did we sort such that the BEST one is first?
        // Yes, dist1 - dist2 means smaller dist comes first.
        // So we keep the first one we see for each angle group.
        continue;
      }
      unique.push(ln);
    }
    lines = unique;
    
    const intersect = (l1, l2) => {
      const det = l1.a * l2.b - l2.a * l1.b;
      if (Math.abs(det) < EPS) return null;
      const x = (l1.c * l2.b - l2.c * l1.b) / det;
      const y = (l1.a * l2.c - l2.a * l1.c) / det;
      return { x, y };
    };
    
    const outside = (p, l) => {
      return l.a * p.x + l.b * p.y - l.c > EPS;
    };
    
    const dq = [];
    
    for (const ln of lines) {
      while (dq.length >= 2 && outside(intersect(dq[dq.length - 2], dq[dq.length - 1]), ln)) {
        dq.pop();
      }
      while (dq.length >= 2 && outside(intersect(dq[0], dq[1]), ln)) {
        dq.shift();
      }
      dq.push(ln);
    }
    
    while (dq.length >= 3 && outside(intersect(dq[dq.length - 2], dq[dq.length - 1]), dq[0])) {
      dq.pop();
    }
    while (dq.length >= 3 && outside(intersect(dq[0], dq[1]), dq[dq.length - 1])) {
      dq.shift();
    }
    
    if (dq.length < 3) return [];
    
    const poly = [];
    for (let i = 0; i < dq.length; i++) {
      const p = intersect(dq[i], dq[(i + 1) % dq.length]);
      if (!p) return []; // Should not happen if logic is correct
      poly.push(p);
    }
    
    // Rotate to lowest x, then y
    let minIdx = 0;
    for (let i = 1; i < poly.length; i++) {
      if (poly[i].x < poly[minIdx].x - EPS || (Math.abs(poly[i].x - poly[minIdx].x) < EPS && poly[i].y < poly[minIdx].y)) {
        minIdx = i;
      }
    }
    
    const res = [];
    for (let i = 0; i < poly.length; i++) {
      res.push(poly[(minIdx + i) % poly.length]);
    }
    
    return res;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const m = parseInt(data[ptr++], 10);
  
  const A = [];
  const B = [];
  const C = [];
  
  for (let i = 0; i < m; i++) {
    A.push(parseInt(data[ptr++], 10));
    B.push(parseInt(data[ptr++], 10));
    C.push(parseInt(data[ptr++], 10));
  }
  
  const solution = new Solution();
  const res = solution.halfPlaneIntersection(A, B, C);
  
  if (res.length === 0) {
    console.log("EMPTY");
  } else {
    console.log(res.length);
    for (const p of res) {
      console.log(``p.x.toFixed(6)`{p.y.toFixed(6)}`);
    }
  }
});
```

### Common Mistakes to Avoid

1. **Not handling parallel lines.** Keep the tightest; contradictory parallels make the intersection empty.
2. **Wrong angle sorting.** Sorting by slope alone fails when `a=0`; use `atan2(b, a)`.
3. **Missing deque cleanup at end.** You must also prune with first/last lines to close the polygon.
4. **Precision errors in inside check.** Add EPS.
5. **Incorrect output order.** Rotate to the lowest `(x,y)` and ensure CCW.

### Complexity Analysis

- **Time:** `O(m log m)` for sorting; deque scan is `O(m)`.
- **Space:** `O(m)` for lines and deque.

## Testing Strategy

- Axis-aligned box (unit square).
- Single half-plane (unbounded, but polygon not printable unless combined—expect EMPTY or need bounding box; here, multiple constraints form bounded shapes).
- Contradictory parallels (empty).
- Slanted constraints forming a hexagon.
- Large coefficients to test stability.

## Applications

- 2D linear programming (feasible region).
- Polygon clipping (against multiple lines).
- Visibility polygons and half-plane intersections in robotics.

## ASCII Recap

```
Sort by angle ➜ prune parallels ➜ sweep with deque:
  pop back/front if last intersection is outside new half-plane
  push new line
Close deque ➜ build intersection points ➜ rotate to lowest (x,y)
```
