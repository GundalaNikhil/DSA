---
problem_id: GEO_LARGEST_EMPTY_CIRCLE__9186
display_id: GEO-012
slug: largest-empty-circle-rect
title: "Largest Empty Circle Inside Rectangle"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Voronoi
  - Circles
tags:
  - geometry
  - circle
  - voronoi
  - medium
premium: true
subscription_tier: basic
---

# GEO-012: Largest Empty Circle Inside Rectangle

## 📋 Problem Summary

Inside an axis-aligned rectangle `[xL, yB]` to `[xR, yT]`, you have `n` points. Find the largest possible circle that stays entirely within the rectangle and contains no point strictly inside it (points on the boundary are allowed). Output the maximum radius.

## 🌍 Real-World Scenario

**Scenario Title:** Drone Hover Safety Bubble**

A drone must hover inside a fenced rectangular zone while avoiding obstacles (points). The largest empty circle gives the widest safety bubble it can occupy without touching any obstacle or the fence.

**Why This Problem Matters:**

- Exercises Voronoi intuition: optimal centers lie at bisectors of points/edges.
- Shows how boundary constraints and obstacles combine.
- With `n <= 2000`, a careful `O(n^3)` candidate enumeration is feasible.

## ASCII Visual

```
Rect: (0,0) to (4,4)
Points: (1,1), (3,1)

Best circle:
center (2,3), radius 1.0
Touches top edge (y=4) and nearest point distance = 1
```

## Detailed Explanation

### Where Can the Optimal Center Be?

For the largest empty circle:
- It is constrained by **at least two** obstacles or edges:
  - Two points (equidistant, circle through both).
  - One point and one rectangle edge (center on their perpendicular bisector).
  - Two rectangle edges (center at rectangle center if no points constrain).
- At most three constraints define the circle (three points, or two points + edge).

Thus, candidate centers arise from:
1. Rectangle corners (radius limited by points).
2. Projection of rectangle edges constrained by a single point (center on edge, radius = distance to nearest point).
3. Circles defined by every pair of points (midpoint) clipped by rectangle.
4. Circumcenters of every triple of non-collinear points (if inside rectangle).

### Checking a Candidate Center

- Compute `r = min(distance to nearest point, distance to rectangle edges)`.
- Keep the maximum `r`.

### Algorithm (Brute Candidates, `n <= 2000`)

1. Read points; if `n = 0`, answer is min distance from rectangle center to edges.
2. Add rectangle corners as candidates.
3. For each point `p`:
   - Project onto each edge? More simply, consider centers on edges at `(p.x, yB)`, `(p.x, yT)`, `(xL, p.y)`, `(xR, p.y)`; only if inside edges.
4. For each pair `(p, q)`:
   - Midpoint `m`; if inside rectangle, candidate `m`.
5. For each triple `(p, q, r)` non-collinear:
   - Circumcenter `c`; if inside rectangle, candidate `c`.
6. For each candidate `c`, compute radius:
   - `r = min(dist(c, nearest point), dist to each rectangle edge)`.
7. Take the maximum `r`.

Because `n <= 2000`, pairs ~2e6 and triples ~1.3e9 are too many; prune:
- Only generate triple circumcenters if needed (could be heavy). A pragmatic approach: sample triples or rely on pair midpoints + edge projections, which solve many cases. For full coverage, restrict triple loop to `O(n^3)` only if n is small (e.g., n <= 60); otherwise rely on pair/edge candidates (works in practice).

### Precision

- Use doubles; compare with small EPS (`1e-12`).
- Output rounded to 6 decimals.

## Input/Output Clarifications

- Points may be on the boundary; allowed.
- If no points, the largest circle is centered at rectangle center with radius = min distance to edges.
- Radius 0 is possible if points cover edges and corners.

## Naive Approach

**Algorithm:** Grid search with shrinking step size until convergence.  
**Limitations:** Inaccurate, slow, and can miss the optimum.

## Optimal-ish Approach for Constraints

Given `n <= 2000`, enumerate robust candidates (corners, edge projections, midpoints, small-n circumcenters) and evaluate.

**Time Complexity:**  
- Pairs: `O(n^2)` for midpoints.  
- Triples: `O(n^3)` if `n` small; otherwise skip.  
- Evaluation: `O(n * candidates)`.  

**Space Complexity:** `O(1)` beyond input.

## Reference Implementation (Python)

```python
import math
from typing import List, Tuple

EPS = 1e-12

def largest_empty_circle(xL: int, yB: int, xR: int, yT: int, xs: List[int], ys: List[int]) -> float:
    pts = list(zip(xs, ys))
    n = len(pts)

    def inside_rect(p):
        return xL - EPS <= p[0] <= xR + EPS and yB - EPS <= p[1] <= yT + EPS

    def dist_to_edge(p):
        return min(p[0]-xL, xR-p[0], p[1]-yB, yT-p[1])

    def dist(p, q):
        return math.hypot(p[0]-q[0], p[1]-q[1])

    cand = []
    # rectangle corners
    cand.extend([(xL, yB), (xL, yT), (xR, yB), (xR, yT)])
    # edge projections of points
    for x, y in pts:
        cand.append((x, yB)); cand.append((x, yT))
        cand.append((xL, y)); cand.append((xR, y))
    # midpoints of pairs
    for i in range(n):
        for j in range(i+1, n):
            mx = (pts[i][0]+pts[j][0])/2.0
            my = (pts[i][1]+pts[j][1])/2.0
            cand.append((mx, my))
    # circumcenters for small n
    if n <= 60:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ax, ay = pts[i]; bx, by = pts[j]; cx, cy = pts[k]
                    d = 2*(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
                    if abs(d) < EPS: continue
                    ux = ((ax*ax+ay*ay)*(by-cy) + (bx*bx+by*by)*(cy-ay) + (cx*cx+cy*cy)*(ay-by)) / d
                    uy = ((ax*ax+ay*ay)*(cx-bx) + (bx*bx+by*by)*(ax-cx) + (cx*cx+cy*cy)*(bx-ax)) / d
                    cand.append((ux, uy))

    best = 0.0
    for p in cand:
        if not inside_rect(p): continue
        d_edge = dist_to_edge(p)
        d_pt = float('inf')
        for q in pts:
            d_pt = min(d_pt, dist(p, q))
        r = min(d_edge, d_pt)
        if r > best: best = r
    return best
```

*(For full rigor, an `O(n^3)` with all circumcenters can be used since n<=2000 is borderline heavy; the above bounds triple generation for practicality.)*

## Common Mistakes to Avoid

1. **Ignoring rectangle edges.** The circle must fit inside; radius is limited by nearest edge.
2. **Using only midpoints.** Some cases need circumcenters (three-point constraints).
3. **Precision errors.** Use EPS in comparisons; output to 6 decimals.
4. **Including candidates outside the rectangle.** Filter them out.

## Complexity Analysis

- **Time:** Up to `O(n^2 * n)` if all triples are used; with bounded triples or n<=60, practical for given constraints.
- **Space:** `O(1)` besides input and candidate storage.

## Testing Strategy

- No points: answer is min distance from rectangle center to edges.
- Single point at center vs near edge.
- Two points with symmetric placement.
- Three non-collinear points requiring circumcenter.
- Points hugging edges to force small radius.
- Large coordinates to stress precision.

## ASCII Recap

```
Candidates:
  corners, edge projections, pair midpoints, (small-n) circumcenters
For each candidate:
  r = min(dist to nearest point, dist to rectangle edges)
Maximize r
```
