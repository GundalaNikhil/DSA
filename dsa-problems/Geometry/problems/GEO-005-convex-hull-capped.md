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
time_limit: 2000
memory_limit: 256
---

# GEO-005: Convex Hull with Interior Caps

## Problem Statement

Given `n` points in 2D and an angle threshold `theta` (degrees, `0 < theta < 180`):

1. Build the convex hull of the points (include collinear boundary points as needed for a standard hull).
2. For each hull vertex, compute its interior angle (in degrees, using the CCW hull order).
3. Discard any hull vertex whose interior angle is **strictly less than** `theta`.
4. Return the remaining “capped” hull vertices in counterclockwise (CCW) order. If all vertices are discarded, output `0`.

Print the vertex count, followed by the remaining vertices.

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`
- Last line: integer `theta`

## Output Format

- First line: integer `k` = number of capped hull vertices
- Next `k` lines (if `k > 0`): `x y` for each vertex in CCW order

## ASCII/Emoji Visual

```
🟢 square hull, theta = 60°
  ● (0,0) ---- ● (4,0)
  |              |
  |      ●       |   => keep all 4 (90° ≥ 60°)
  ● (0,4) ---- ● (4,4)

🔺 triangle hull, theta = 80°
        ●
       / \
      /   \
   ● ----- ●
   all angles 60° < 80° ⇒ discard all ⇒ k = 0
```

## Constraints

- `3 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`
- `0 < theta < 180`

## Example 1

**Input:**
```
5
0 0
4 0
4 4
0 4
2 2
60
```

**Output:**
```
4
0 0
4 0
4 4
0 4
```

**Explanation:** Square hull has interior angles 90°, all ≥ 60°, so nothing is capped away.

## Example 2

**Input:**
```
4
0 0
2 2
4 0
2 -2
100
```

**Output:**
```
0
```

**Explanation:** Hull is a diamond with interior angles 90°; all are < 100°, so every vertex is discarded.

## Notes

- Interior angle is measured inside the polygon; for a convex hull it lies in `(0, 180]`.
- Use squared lengths to avoid precision issues when comparing angles (via cross and dot, or cosine).
- If `k = 0`, print just `0`.

## Related Topics

Convex Hull, Geometry Filtering, Cross Product

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<long[]> cappedHull(long[] xs, long[] ys, int theta) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {

static class Solution {
    private long cross(long ox, long oy, long ax, long ay, long bx, long by) {
        return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox);
    }

    public List<long[]> cappedHull(long[] xs, long[] ys, int theta) {
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
            double cosA = dot / (lenU * lenV);
            if (cosA <= cosT) keep.add(curr);
        }
        return keep;
    }
}
```

### Python

```
// No template available
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

class Solution {
public:
    long long cross(Point o, Point a, Point b) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    int theta;
    cin >> theta;

    // Remove duplicates
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());

    if (pts.size() <= 1) {
        if (pts.empty()) cout << "0\n";
        else cout << "1\n" << pts[0].x << " " << pts[0].y << "\n";
        return 0;
    }

    // Monotone Chain
    vector<Point> lower, upper;
    for (const auto& p : pts) {
        while (lower.size() >= 2 && cross(lower[lower.size()-2], lower.back(), p) <= 0) {
            lower.pop_back();
        }
        lower.push_back(p);
    }
    for (int i = pts.size() - 1; i >= 0; i--) {
        const auto& p = pts[i];
        while (upper.size() >= 2 && cross(upper[upper.size()-2], upper.back(), p) <= 0) {
            upper.pop_back();
        }
        upper.push_back(p);
    }

    vector<Point> hull = lower;
    hull.pop_back();
    hull.insert(hull.end(), upper.begin(), upper.end());
    hull.pop_back();

    if (hull.size() <= 2) {
        cout << hull.size() << "\n";
        for (const auto& p : hull) cout << p.x << " " << p.y << "\n";
        return 0;
    }

    long long h = hull.size();
    double cosT = cos(theta * M_PI / 180.0);
    vector<Point> keep;

    for (int i = 0; i < h; ++i) {
        Point prev = hull[(i - 1 + h) % h];
        Point curr = hull[i];
        Point nxt = hull[(i + 1) % h];

        double ux = (double)prev.x - curr.x;
        double uy = (double)prev.y - curr.y;
        double vx = (double)nxt.x - curr.x;
        double vy = (double)nxt.y - curr.y;

        double lenU = hypot(ux, uy);
        double lenV = hypot(vx, vy);

        if (lenU == 0 || lenV == 0) {
            keep.push_back(curr);
            continue;
        }

        double dot = ux * vx + uy * vy;
        double cosA = dot / (lenU * lenV); // Note: Python logic: cosA = dot / ...
        
        // Wait, Python logic:
        // ux, uy vector from curr to prev? No: prev - curr. So vector CP.
        // vx, vy vector from curr to nxt? No: nxt - curr. So vector CN.
        // Angle at C is angle betwen CP and CN.
        // dot = |CP||CN|cos(angle)
        // Check my previous C++ implementation (step 271) used cosA = -dot / ... ?
        // Python code (step 270):
        // ux, uy = prev[0]-curr[0], prev[1]-curr[1]  -> Vector CP
        // vx, vy = nxt[0]-curr[0], nxt[1]-curr[1]    -> Vector CN
        // dot = ux*vx + uy*vy
        // cosA = dot / (lenU*lenV)
        // if cosA <= cosT: keep
        // This is correct. My previous C++ at 271 had `cosA = -dot` which was probably wrong.
        
        if (cosA <= cosT + 1e-9) { // strict inequality + epsilon for safety
            keep.push_back(curr);
        }
    }

    cout << keep.size() << "\n";
    for (const auto& p : keep) {
        cout << p.x << " " << p.y << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(xs, ys, theta) {
    // Implementation here
    return null;
  }
}

const readline = require('readline');

class Solution {
    solve(xs, ys, theta) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        // Remove duplicates with Correct Sort
        pts.sort((a, b) => {
            if (a.x !== b.x) return a.x < b.x ? -1 : 1;
            if (a.y !== b.y) return a.y < b.y ? -1 : 1;
            return 0;
        });
        pts = pts.filter((p, i) => i === 0 || p.x !== pts[i-1].x || p.y !== pts[i-1].y);

        if (pts.length <= 1) return pts;

        const cross = (o, a, b) => (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);

        let lower = [];
        for (let p of pts) {
            while (lower.length >= 2 && cross(lower[lower.length-2], lower[lower.length-1], p) <= 0n) {
                lower.pop();
            }
            lower.push(p);
        }
        let upper = [];
        for (let i = pts.length - 1; i >= 0; i--) {
            let p = pts[i];
            while (upper.length >= 2 && cross(upper[upper.length-2], upper[upper.length-1], p) <= 0n) {
                upper.pop();
            }
            upper.push(p);
        }
        
        lower.pop();
        upper.pop();
        let hull = lower.concat(upper);

        if (hull.length <= 2) return hull;

        const h = hull.length;
        const cosT = Math.cos(theta * Math.PI / 180.0);
        let keep = [];

        for (let i = 0; i < h; i++) {
            let prev = hull[(i - 1 + h) % h];
            let curr = hull[i];
            let nxt = hull[(i + 1) % h];

            let ux = Number(prev.x - curr.x);
            let uy = Number(prev.y - curr.y);
            let vx = Number(nxt.x - curr.x);
            let vy = Number(nxt.y - curr.y);

            let lenU = Math.hypot(ux, uy);
            let lenV = Math.hypot(vx, vy);

            if (lenU === 0 || lenV === 0) {
                keep.push(curr);
                continue;
            }

            let dot = ux * vx + uy * vy;
            let cosA = dot / (lenU * lenV);

            if (cosA <= cosT + 1e-9) {
                keep.push(curr);
            }
        }
        return keep;
    }
}
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => next(); 

    let n = parseInt(nextInt());
    let xs = [], ys = [];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }
    let theta = parseInt(nextInt());

    const sol = new Solution();
    const res = sol.solve(xs, ys, theta);
    
    if (res.length === 0) console.log(0);
    else {
        console.log(res.length);
        for(let p of res) console.log(`${p.x} ${p.y}`);
    }
});
```
