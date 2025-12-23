---
problem_id: GEO_MIN_ENCLOSING_CIRCLE__4205
display_id: GEO-008
slug: minimum-enclosing-circle
title: "Minimum Enclosing Circle"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Randomized Algorithms
  - Circle
tags:
  - geometry
  - circle
  - randomized
  - medium
premium: true
subscription_tier: basic
---

# GEO-008: Minimum Enclosing Circle

## 📋 Problem Summary

Given `n` points, find the smallest circle that encloses them all. Output center `(cx, cy)` and radius `r`, rounded to 6 decimals.

## 🌍 Real-World Scenario

**Scenario Title:** Drone Coverage Bubble**

Planning a single hovering station to “cover” all delivery drop points means finding the smallest circle containing all destinations. This minimizes hover radius (battery and time).

**Why This Problem Matters:**

- Classic computational geometry with a clean expected `O(n)` randomized solution.
- Shows how boundary points (<=3) define the optimal circle.
- Precision care: doubles with controlled rounding.

## ASCII Visual

```
Points:
● (0,0)   ● (1,0)
     ● (0,1)

Enclosing circle:
center (0.5, 0.5)
radius ≈ 0.707107
```

## Detailed Explanation

### Properties

- The minimum enclosing circle (MEC) is defined by at most three points on its boundary:
  - 1 point: radius 0.
  - 2 points: circle with that segment as diameter.
  - 3 points: circumcircle of the triangle.

### Randomized Incremental Algorithm (Welzl)

1. Shuffle points (random order).
2. Start with empty circle.
3. For each point `p`:
   - If `p` is inside the current circle, continue.
   - Otherwise, build a new circle with `p` on the boundary:
     - Start with circle centered at `p`, radius 0.
     - For each earlier point `q` not in the circle, set circle to diameter of `p` and `q`.
     - For each earlier `r` not in the circle, set circle to circumcircle of `p,q,r`.
4. Return the final circle.

Expected `O(n)` because boundary updates happen rarely after randomization.

### Circle Constructions

- **Diameter circle (two points):** center = midpoint, radius = half distance.
- **Circumcircle (three points):** compute intersection of perpendicular bisectors (or use determinant formula). Be careful with collinearity: if area is ~0, skip (the pair case already handles it).

### Precision

- Use `double` throughout; EPS (`1e-12`) for inside checks: `dist <= r + EPS`.
- Output with 6 decimals.

## Input/Output Clarifications

- Output: `cx cy r` with rounding; order doesn’t matter.
- If `n = 1`, radius is 0 at that point.
- Points may be repeated; still fine.

## Naive Approach

**Algorithm:** Enumerate all pairs and triplets, build candidate circles, pick smallest enclosing all points.

**Time:** `O(n^4)` (checking inclusion) or `O(n^3)` with pruning — too slow for `n = 2e5`.  
**Space:** `O(1)`.

## Optimal Approach (Welzl)

**Algorithm:**

1. Shuffle points.
2. Initialize `c = (points[0], r=0)`.
3. For each `i` from 1..n-1:
   - If `pi` inside `c`, continue.
   - Else set `c` to circle(pi, 0).
   - For `j` in [0..i-1]:
     - If `pj` inside `c`, continue.
     - Set `c` = diameter circle of `pi,pj`.
     - For `k` in [0..j-1]:
       - If `pk` inside `c`, continue.
       - Set `c` = circumcircle of `pi,pj,pk`.
4. Output `c`.

**Time Complexity:** Expected `O(n)`.  
**Space Complexity:** `O(1)` extra beyond the point list.

## Reference Implementations

### Python

```python
import math, random
from typing import List, Tuple

def min_enclosing_circle(xs: List[int], ys: List[int]) -> Tuple[float,float,float]:
    pts = list(zip(xs, ys))
    random.shuffle(pts)

    def dist(a, b):
        dx, dy = a[0]-b[0], a[1]-b[1]
        return math.hypot(dx, dy)

    def circle_two(a, b):
        cx = (a[0]+b[0]) / 2.0
        cy = (a[1]+b[1]) / 2.0
        r = dist(a, b) / 2.0
        return (cx, cy, r)

    def circle_three(a, b, c):
        d = 2*(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]))
        if abs(d) < 1e-15:
            return (0.0, 0.0, -1.0)  # invalid
        ux = ((a[0]*a[0]+a[1]*a[1])*(b[1]-c[1]) + (b[0]*b[0]+b[1]*b[1])*(c[1]-a[1]) + (c[0]*c[0]+c[1]*c[1])*(a[1]-b[1])) / d
        uy = ((a[0]*a[0]+a[1]*a[1])*(c[0]-b[0]) + (b[0]*b[0]+b[1]*b[1])*(a[0]-c[0]) + (c[0]*c[0]+c[1]*c[1])*(b[0]-a[0])) / d
        r = dist((ux, uy), a)
        return (ux, uy, r)

    def inside(p, c):
        cx, cy, r = c
        return dist(p, (cx, cy)) <= r + 1e-12

    c = (pts[0][0], pts[0][1], 0.0)
    for i in range(1, len(pts)):
        if inside(pts[i], c): continue
        c = (pts[i][0], pts[i][1], 0.0)
        for j in range(i):
            if inside(pts[j], c): continue
            c = circle_two(pts[i], pts[j])
            for k in range(j):
                if inside(pts[k], c): continue
                c = circle_three(pts[i], pts[j], pts[k])
    return c
```

### Java

```java
import java.util.*;

class Solution {
    static class Circle { double x,y,r; Circle(double x,double y,double r){this.x=x;this.y=y;this.r=r;} }

    private double dist(double x1, double y1, double x2, double y2) {
        double dx = x1 - x2, dy = y1 - y2;
        return Math.hypot(dx, dy);
    }
    private Circle fromTwo(double x1, double y1, double x2, double y2) {
        double cx = (x1 + x2) / 2.0, cy = (y1 + y2) / 2.0;
        double r = dist(x1, y1, x2, y2) / 2.0;
        return new Circle(cx, cy, r);
    }
    private Circle fromThree(double x1, double y1, double x2, double y2, double x3, double y3) {
        double d = 2*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2));
        if (Math.abs(d) < 1e-15) return new Circle(0,0,-1);
        double ux = ((x1*x1+y1*y1)*(y2-y3) + (x2*x2+y2*y2)*(y3-y1) + (x3*x3+y3*y3)*(y1-y2)) / d;
        double uy = ((x1*x1+y1*y1)*(x3-x2) + (x2*x2+y2*y2)*(x1-x3) + (x3*x3+y3*y3)*(x2-x1)) / d;
        double r = dist(ux, uy, x1, y1);
        return new Circle(ux, uy, r);
    }
    private boolean inside(double px, double py, Circle c) {
        return dist(px, py, c.x, c.y) <= c.r + 1e-12;
    }

    public double[] minEnclosingCircle(int[] xs, int[] ys) {
        int n = xs.length;
        List<int[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new int[]{xs[i], ys[i]});
        Collections.shuffle(pts, new Random());
        Circle c = new Circle(pts.get(0)[0], pts.get(0)[1], 0);
        for (int i = 1; i < n; i++) {
            int[] p = pts.get(i);
            if (inside(p[0], p[1], c)) continue;
            c = new Circle(p[0], p[1], 0);
            for (int j = 0; j < i; j++) {
                int[] q = pts.get(j);
                if (inside(q[0], q[1], c)) continue;
                c = fromTwo(p[0], p[1], q[0], q[1]);
                for (int k = 0; k < j; k++) {
                    int[] r = pts.get(k);
                    if (inside(r[0], r[1], c)) continue;
                    c = fromThree(p[0], p[1], q[0], q[1], r[0], r[1]);
                }
            }
        }
        return new double[]{c.x, c.y, c.r};
    }
}
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <iomanip>

using namespace std;

struct Point {
    double x, y;
};

struct Circle {
    double x, y, r;
};

class Solution {
    double dist(Point a, Point b) {
        return hypot(a.x - b.x, a.y - b.y);
    }

    Circle fromTwo(Point a, Point b) {
        Point center = {(a.x + b.x) / 2.0, (a.y + b.y) / 2.0};
        return {center.x, center.y, dist(a, b) / 2.0};
    }

    Circle fromThree(Point a, Point b, Point c) {
        double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
        if (abs(d) < 1e-15) return {0, 0, -1};
        double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
        double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
        return {ux, uy, dist({ux, uy}, a)};
    }

    bool inside(Point p, Circle c) {
        return dist(p, {c.x, c.y}) <= c.r + 1e-12;
    }

public:
    vector<double> minEnclosingCircle(vector<int>& xs, vector<int>& ys) {
        int n = xs.size();
        vector<Point> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {(double)xs[i], (double)ys[i]};
        
        random_device rd;
        mt19937 g(rd());
        shuffle(pts.begin(), pts.end(), g);

        Circle c = {pts[0].x, pts[0].y, 0};

        for (int i = 1; i < n; i++) {
            if (inside(pts[i], c)) continue;
            c = {pts[i].x, pts[i].y, 0};
            for (int j = 0; j < i; j++) {
                if (inside(pts[j], c)) continue;
                c = fromTwo(pts[i], pts[j]);
                for (int k = 0; k < j; k++) {
                    if (inside(pts[k], c)) continue;
                    c = fromThree(pts[i], pts[j], pts[k]);
                }
            }
        }
        return {c.x, c.y, c.r};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> xs(n), ys(n);
    for(int i=0; i<n; ++i) cin >> xs[i];
    for(int i=0; i<n; ++i) cin >> ys[i];
    
    Solution sol;
    vector<double> res = sol.minEnclosingCircle(xs, ys);
    
    cout << fixed << setprecision(6) << res[0] << " " << res[1] << " " << res[2] << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minEnclosingCircle(xs, ys) {
    const n = xs.length;
    const pts = [];
    for (let i = 0; i < n; i++) pts.push({ x: xs[i], y: ys[i] });
    
    // Shuffle
    for (let i = n - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pts[i], pts[j]] = [pts[j], pts[i]];
    }
    
    const dist = (a, b) => Math.hypot(a.x - b.x, a.y - b.y);
    
    const fromTwo = (a, b) => {
      const cx = (a.x + b.x) / 2.0;
      const cy = (a.y + b.y) / 2.0;
      const r = dist(a, b) / 2.0;
      return { x: cx, y: cy, r: r };
    };
    
    const fromThree = (a, b, c) => {
      const d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
      if (Math.abs(d) < 1e-15) return { x: 0, y: 0, r: -1 };
      const ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
      const uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
      return { x: ux, y: uy, r: dist({ x: ux, y: uy }, a) };
    };
    
    const inside = (p, c) => dist(p, c) <= c.r + 1e-12;
    
    let c = { x: pts[0].x, y: pts[0].y, r: 0 };
    
    for (let i = 1; i < n; i++) {
      if (inside(pts[i], c)) continue;
      c = { x: pts[i].x, y: pts[i].y, r: 0 };
      for (let j = 0; j < i; j++) {
        if (inside(pts[j], c)) continue;
        c = fromTwo(pts[i], pts[j]);
        for (let k = 0; k < j; k++) {
          if (inside(pts[k], c)) continue;
          c = fromThree(pts[i], pts[j], pts[k]);
        }
      }
    }
    
    return [c.x, c.y, c.r];
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
  const n = parseInt(data[ptr++], 10);
  
  const xs = [];
  for (let i = 0; i < n; i++) xs.push(parseInt(data[ptr++], 10));
  
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  const res = solution.minEnclosingCircle(xs, ys);
  
  console.log(``res[0].toFixed(6)`{res[1].toFixed(6)} ${res[2].toFixed(6)}`);
});
```

### Common Mistakes to Avoid

1. **Skipping shuffle.** Without random order, worst-case degenerates to `O(n^3)`.
2. **Precision in inside check.** Use an EPS tolerance; exact compares fail on boundaries.
3. **Invalid circumcircle on collinear points.** Guard with determinant near zero.
4. **Using integers for circle math.** Stick to doubles for centers/radius.
5. **Not rounding output.** Print to 6 decimals as required.

### Complexity Analysis

- **Expected Time:** `O(n)`  
- **Space:** `O(1)` extra.

## Testing Strategy

- Single point (radius 0).
- Two points on a line (diameter circle).
- Right triangle (hypotenuse as diameter).
- Equilateral triangle (circumcircle).
- Axis-aligned rectangles (center midpoint, radius half-diagonal).
- Large coordinates to test stability.

## Applications

- Coverage planning (drones, sensors).
- Bounding volumes in collision detection.
- Smallest enclosing circle preprocessing for clustering.

## ASCII Recap

```
Shuffle points ➜ grow circle as needed
Boundary size ≤ 3:
 1 pt → r=0
 2 pts → diameter circle
 3 pts → circumcircle
```
