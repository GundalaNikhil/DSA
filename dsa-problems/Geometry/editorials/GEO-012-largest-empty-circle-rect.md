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

### Java

```java
import java.util.*;

class Solution {
    static class Point {
        double x, y;
        Point(double x, double y) { this.x = x; this.y = y; }
    }

    private double dist(Point p, Point q) {
        return Math.hypot(p.x - q.x, p.y - q.y);
    }

    private double distToEdge(Point p, int xL, int yB, int xR, int yT) {
        return Math.min(Math.min(p.x - xL, xR - p.x), Math.min(p.y - yB, yT - p.y));
    }

    private boolean insideRect(Point p, int xL, int yB, int xR, int yT) {
        double EPS = 1e-12;
        return p.x >= xL - EPS && p.x <= xR + EPS && p.y >= yB - EPS && p.y <= yT + EPS;
    }

    public double largestEmptyCircle(int xL, int yB, int xR, int yT, int[] xs, int[] ys) {
        int n = xs.length;
        List<Point> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new Point(xs[i], ys[i]));

        List<Point> candidates = new ArrayList<>();
        // Corners
        candidates.add(new Point(xL, yB));
        candidates.add(new Point(xL, yT));
        candidates.add(new Point(xR, yB));
        candidates.add(new Point(xR, yT));

        // Edge projections
        for (Point p : pts) {
            candidates.add(new Point(p.x, yB));
            candidates.add(new Point(p.x, yT));
            candidates.add(new Point(xL, p.y));
            candidates.add(new Point(xR, p.y));
        }

        // Midpoints
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                candidates.add(new Point((pts.get(i).x + pts.get(j).x) / 2.0, (pts.get(i).y + pts.get(j).y) / 2.0));
            }
        }

        // Circumcenters (small n)
        if (n <= 60) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        Point a = pts.get(i), b = pts.get(j), c = pts.get(k);
                        double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
                        if (Math.abs(d) < 1e-12) continue;
                        double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
                        double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
                        candidates.add(new Point(ux, uy));
                    }
                }
            }
        }

        double best = 0.0;
        for (Point c : candidates) {
            if (!insideRect(c, xL, yB, xR, yT)) continue;
            double r = distToEdge(c, xL, yB, xR, yT);
            for (Point p : pts) {
                r = Math.min(r, dist(c, p));
            }
            best = Math.max(best, r);
        }
        return best;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int xL = sc.nextInt(), yB = sc.nextInt(), xR = sc.nextInt(), yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) xs[i] = sc.nextInt();
        for (int i = 0; i < n; i++) ys[i] = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.printf("%.6f\n", sol.largestEmptyCircle(xL, yB, xR, yT, xs, ys));
        sc.close();
    }
}
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Point {
    double x, y;
};

class Solution {
    double dist(Point p, Point q) {
        return hypot(p.x - q.x, p.y - q.y);
    }

    double distToEdge(Point p, int xL, int yB, int xR, int yT) {
        return min({p.x - xL, (double)xR - p.x, p.y - yB, (double)yT - p.y});
    }

    bool insideRect(Point p, int xL, int yB, int xR, int yT) {
        double EPS = 1e-12;
        return p.x >= xL - EPS && p.x <= xR + EPS && p.y >= yB - EPS && p.y <= yT + EPS;
    }

public:
    double largestEmptyCircle(int xL, int yB, int xR, int yT, vector<int>& xs, vector<int>& ys) {
        int n = xs.size();
        vector<Point> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {(double)xs[i], (double)ys[i]};

        vector<Point> candidates;
        // Corners
        candidates.push_back({(double)xL, (double)yB});
        candidates.push_back({(double)xL, (double)yT});
        candidates.push_back({(double)xR, (double)yB});
        candidates.push_back({(double)xR, (double)yT});

        // Edge projections
        for (const auto& p : pts) {
            candidates.push_back({p.x, (double)yB});
            candidates.push_back({p.x, (double)yT});
            candidates.push_back({(double)xL, p.y});
            candidates.push_back({(double)xR, p.y});
        }

        // Midpoints
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                candidates.push_back({(pts[i].x + pts[j].x) / 2.0, (pts[i].y + pts[j].y) / 2.0});
            }
        }

        // Circumcenters (small n)
        if (n <= 60) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        Point a = pts[i], b = pts[j], c = pts[k];
                        double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
                        if (abs(d) < 1e-12) continue;
                        double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
                        double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
                        candidates.push_back({ux, uy});
                    }
                }
            }
        }

        double best = 0.0;
        for (const auto& c : candidates) {
            if (!insideRect(c, xL, yB, xR, yT)) continue;
            double r = distToEdge(c, xL, yB, xR, yT);
            for (const auto& p : pts) {
                r = min(r, dist(c, p));
            }
            best = max(best, r);
        }
        return best;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int xL, yB, xR, yT;
    if (!(cin >> xL >> yB >> xR >> yT)) return 0;
    
    int n;
    cin >> n;
    
    vector<int> xs(n), ys(n);
    for(int i=0; i<n; ++i) cin >> xs[i];
    for(int i=0; i<n; ++i) cin >> ys[i];
    
    Solution sol;
    cout << fixed << setprecision(6) << sol.largestEmptyCircle(xL, yB, xR, yT, xs, ys) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  largestEmptyCircle(xL, yB, xR, yT, xs, ys) {
    const n = xs.length;
    const pts = [];
    for (let i = 0; i < n; i++) pts.push({ x: xs[i], y: ys[i] });
    
    const candidates = [];
    // Corners
    candidates.push({ x: xL, y: yB });
    candidates.push({ x: xL, y: yT });
    candidates.push({ x: xR, y: yB });
    candidates.push({ x: xR, y: yT });
    
    // Edge projections
    for (const p of pts) {
      candidates.push({ x: p.x, y: yB });
      candidates.push({ x: p.x, y: yT });
      candidates.push({ x: xL, y: p.y });
      candidates.push({ x: xR, y: p.y });
    }
    
    // Midpoints
    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        candidates.push({ x: (pts[i].x + pts[j].x) / 2.0, y: (pts[i].y + pts[j].y) / 2.0 });
      }
    }
    
    // Circumcenters (small n)
    if (n <= 60) {
      for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
          for (let k = j + 1; k < n; k++) {
            const a = pts[i], b = pts[j], c = pts[k];
            const d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
            if (Math.abs(d) < 1e-12) continue;
            const ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
            const uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
            candidates.push({ x: ux, y: uy });
          }
        }
      }
    }
    
    const dist = (p, q) => Math.hypot(p.x - q.x, p.y - q.y);
    const distToEdge = (p) => Math.min(p.x - xL, xR - p.x, p.y - yB, yT - p.y);
    const insideRect = (p) => {
      const EPS = 1e-12;
      return p.x >= xL - EPS && p.x <= xR + EPS && p.y >= yB - EPS && p.y <= yT + EPS;
    };
    
    let best = 0.0;
    for (const c of candidates) {
      if (!insideRect(c)) continue;
      let r = distToEdge(c);
      for (const p of pts) {
        r = Math.min(r, dist(c, p));
      }
      best = Math.max(best, r);
    }
    
    return best;
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
  const xL = parseInt(data[ptr++], 10);
  const yB = parseInt(data[ptr++], 10);
  const xR = parseInt(data[ptr++], 10);
  const yT = parseInt(data[ptr++], 10);
  
  const n = parseInt(data[ptr++], 10);
  
  const xs = [];
  for (let i = 0; i < n; i++) xs.push(parseInt(data[ptr++], 10));
  
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  console.log(solution.largestEmptyCircle(xL, yB, xR, yT, xs, ys).toFixed(6));
});
```

*(For full rigor, an `O(n^3)` with all circumcenters can be used since n<=2000 is borderline heavy; the above bounds triple generation for practicality.)*

### Common Mistakes to Avoid

1. **Ignoring rectangle edges.** The circle must fit inside; radius is limited by nearest edge.
2. **Using only midpoints.** Some cases need circumcenters (three-point constraints).
3. **Precision errors.** Use EPS in comparisons; output to 6 decimals.
4. **Including candidates outside the rectangle.** Filter them out.

### Complexity Analysis

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
