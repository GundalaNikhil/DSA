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
---

# GEO-005: Convex Hull with Interior Caps

## 📋 Problem Summary

Build the convex hull of `n` points, then drop any hull vertex whose interior angle is **strictly less than** `theta` (degrees). Output the remaining vertices in CCW order; if none remain, output `0`.

## 🌍 Real-World Scenario

**Scenario Title:** Drone Flight Path Smoothing**

Before publishing a polygonal flight boundary, operations wants to remove “too sharp” hull corners (below `theta`) to ensure smooth turns. The capped hull represents the smoothed boundary the drone can follow safely.

**Why This Problem Matters:**

- Extends convex hull by post-processing with angle-based pruning.
- Reinforces robust hull construction and angle checks without floating error.
- Practical for simplifying polygons under turning constraints.

## Emoji Visuals

```
🟩 Square hull, theta = 60°
  🟢 (0,0) ---- 🟢 (4,0)
  |              |
  |      ⚙️      |   => all 4 kept (90° ≥ 60°)
  🟢 (0,4) ---- 🟢 (4,4)

🔺 Triangle hull, theta = 80°
        🟢
       / \
      /   \
   🟢 ----- 🟢
   angles 60° < 80° ⇒ all capped away ⇒ k = 0
```

## Detailed Explanation

### Step 1: Convex Hull

Use a standard hull algorithm (Andrew’s monotone chain). Keep the hull in CCW order. Interior angles on a convex hull lie in `(0, 180]`.

### Step 2: Interior Angle Test

For consecutive hull vertices `(prev, curr, next)`, compute:

- `dot = (prev - curr) · (next - curr)`
- `cross = (prev - curr) x (next - curr)`

Interior angle `α` satisfies `cos α = -dot / (|prev-curr| * |next-curr|)` and `sin α = |cross| / (|prev-curr| * |next-curr|)`. To avoid trig, compare using cosine threshold:

- We need `α < theta` to discard.
- Compute `cos α = -dot / (|u||v|)`.
- Precompute `cos(theta)` once (in double) and discard if `cos α > cos(theta)` **and** `cross != 0` (since cos decreases as angle grows in `[0, π]`).

Alternatively, compare using tan/side-lengths with squared lengths to stay integer-heavy; a single cosine comparison is fine with doubles because we only need a strict inequality.

### Corner Cases

- **Collinear hull edges:** angle is 180°; never discarded unless `theta > 180` (impossible here), so they stay.
- **All removed:** output `0`.
- **Duplicate points:** hull algorithm ignores them; duplicates can cause 0 distance edges; ensure you skip zero-length vectors when computing angle.

## Input/Output Clarifications

- Output first the count `k`, then the `k` vertices CCW.
- If `k = 0`, print just `0`.
- `theta` is in degrees; convert to radians for cosine if needed.

## Naive Approach

**Algorithm:**
1. Compute hull.
2. For each hull vertex, compute actual angle via `acos` and compare with `theta`.

**Time:** `O(n log n)` for hull, `O(h)` for angles.  
**Space:** `O(h)`.

**Limitations:** Uses `acos` per vertex; slower and less stable than cosine comparison.

## Optimal Approach

**Key Insight:** You can compare angles without computing them explicitly.

**Algorithm:**
1. Build hull `H` in CCW via monotone chain. Let `h = |H|`.
2. Precompute `cosT = cos(theta)` in radians.
3. For each `i` in `H`, let `prev = H[(i-1+h)%h]`, `curr = H[i]`, `next = H[(i+1)%h]`.
4. Compute vectors `u = prev - curr`, `v = next - curr`.
5. If either `u` or `v` is zero-length, skip discarding.
6. Compute `dot = u.x*v.x + u.y*v.y`, `lenU = |u|`, `lenV = |v|`, `cosA = -dot / (lenU*lenV)`.
7. If `cosA > cosT` (i.e., angle smaller than `theta`), discard `curr`; otherwise keep it.
8. Output kept vertices.

**Time Complexity:** `O(n log n)` (hull dominates).  
**Space Complexity:** `O(n)` for hull arrays.

## Reference Implementations

### Python

```python
import math
from typing import List, Tuple

def capped_hull(xs: List[int], ys: List[int], theta: int) -> List[Tuple[int, int]]:
    pts = sorted(set(zip(xs, ys)))
    if len(pts) == 1:
        return pts

    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    # Monotone chain
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    h = len(hull)
    if h <= 2:
        return hull

    cosT = math.cos(math.radians(theta))
    keep = []
    for i in range(h):
        prev = hull[(i-1)%h]; curr = hull[i]; nxt = hull[(i+1)%h]
        ux, uy = prev[0]-curr[0], prev[1]-curr[1]
        vx, vy = nxt[0]-curr[0], nxt[1]-curr[1]
        lenU = math.hypot(ux, uy); lenV = math.hypot(vx, vy)
        if lenU == 0 or lenV == 0:
            keep.append(curr); continue
        dot = ux*vx + uy*vy
        cosA = -dot / (lenU*lenV)
        if cosA <= cosT:  # angle >= theta
            keep.append(curr)
    return keep
```

### Java

```java
import java.util.*;

class Solution {
    private long cross(long ox, long oy, long ax, long ay, long bx, long by) {
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
    }

    public List<long[]> cappedHull(int[] xs, int[] ys, int theta) {
        int n = xs.length;
        List<long[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new long[]{xs[i], ys[i]});
        pts.sort((a,b) -> a[0]==b[0] ? Long.compare(a[1], b[1]) : Long.compare(a[0], b[0]));
        List<long[]> unique = new ArrayList<>();
        long lastX = Long.MIN_VALUE, lastY = Long.MIN_VALUE;
        for (long[] p : pts) {
            if (p[0]!=lastX || p[1]!=lastY) { unique.add(p); lastX=p[0]; lastY=p[1]; }
        }
        pts = unique;
        if (pts.size() == 1) return pts;
        List<long[]> lower = new ArrayList<>();
        for (long[] p : pts) {
            while (lower.size() >= 2 && cross(lower.get(lower.size()-2)[0], lower.get(lower.size()-2)[1],
                                              lower.get(lower.size()-1)[0], lower.get(lower.size()-1)[1],
                                              p[0], p[1]) <= 0) {
                lower.remove(lower.size()-1);
            }
            lower.add(p);
        }
        List<long[]> upper = new ArrayList<>();
        for (int i = pts.size()-1; i>=0; i--) {
            long[] p = pts.get(i);
            while (upper.size() >= 2 && cross(upper.get(upper.size()-2)[0], upper.get(upper.size()-2)[1],
                                              upper.get(upper.size()-1)[0], upper.get(upper.size()-1)[1],
                                              p[0], p[1]) <= 0) {
                upper.remove(upper.size()-1);
            }
            upper.add(p);
        }
        List<long[]> hull = new ArrayList<>(lower);
        hull.remove(hull.size()-1);
        upper.remove(upper.size()-1);
        hull.addAll(upper);
        int h = hull.size();
        if (h <= 2) return hull;

        double cosT = Math.cos(Math.toRadians(theta));
        List<long[]> keep = new ArrayList<>();
        for (int i = 0; i < h; i++) {
            long[] prev = hull.get((i-1+h)%h);
            long[] curr = hull.get(i);
            long[] nxt = hull.get((i+1)%h);
            long ux = prev[0]-curr[0], uy = prev[1]-curr[1];
            long vx = nxt[0]-curr[0], vy = nxt[1]-curr[1];
            double lenU = Math.hypot(ux, uy), lenV = Math.hypot(vx, vy);
            if (lenU == 0 || lenV == 0) { keep.add(curr); continue; }
            double dot = ux*vx + uy*vy;
            double cosA = -dot / (lenU * lenV);
            if (cosA <= cosT) keep.add(curr);
        }
        return keep;
    }
}
```

## Common Mistakes to Avoid

1. **Using `acos` per vertex.**  
   Compare cosines; it’s faster and avoids precision pitfalls.

2. **Dropping collinear edges incorrectly.**  
   Collinear angles are 180° and should not be removed for `theta < 180`.

3. **Losing hull order.**  
   Ensure the hull remains CCW after building; the filtering must preserve order.

4. **Zero-length edges.**  
   Duplicates can create zero-length vectors; guard against division by zero.

## Complexity Analysis

- **Time:** `O(n log n)` (hull) + `O(h)` (filter).  
- **Space:** `O(n)` for hull buffers.

## Testing Strategy

- Square with small `theta` (keep all).
- Square with `theta > 90` (discard all).
- Triangle with `theta` below/above 60°.
- Collinear points (degenerate hull of 2 points).
- Large coordinates to ensure 64-bit safety.

## Applications

- Simplifying polygons under turn constraints.
- Smoothing navigation boundaries.
- Filtering noisy hulls before rendering.

## Emoji Recap

```
🟢 Hull built (CCW) ➜ 🪓 Remove sharp corners (< theta) ➜ ✅ Output capped hull
```
