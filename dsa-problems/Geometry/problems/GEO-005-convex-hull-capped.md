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

class Main {

static class Solution {
    private long cross(long ox, long oy, long ax, long ay, long bx, long by) {
        return 0;
    }

    public List<long[]> cappedHull(long[] xs, long[] ys, int theta) {
        return null;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        int theta = sc.nextInt();
        List<long[]> res = new Solution().cappedHull(xs, ys, theta);
        System.out.println(res.size());
        for(long[] p : res) System.out.println(p[0] + " " + p[1]);
    }
}
```

### Python

```python
import math
from typing import List, Tuple

def capped_hull(xs: List[int], ys: List[int], theta: int) -> List[Tuple[int, int]]:
    return []
def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        n = next(it)
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
        theta = next(it)
        res = capped_hull(xs, ys, theta)
        print(len(res))
        for x, y in res:
            print(f"{x} {y}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
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
    long long x, y;
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

long long cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

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
const readline = require('readline');

class Solution {
    solve(xs, ys, theta) {
    return 0;
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

