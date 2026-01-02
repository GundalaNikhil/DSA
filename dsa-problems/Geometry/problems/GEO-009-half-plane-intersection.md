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
time_limit: 2000
memory_limit: 256
---

# GEO-009: Half-Plane Intersection

## Problem Statement

You are given `m` half-planes in the form `a*x + b*y <= c`. Compute their intersection polygon. If the intersection is empty, output `EMPTY`. Otherwise output the polygon vertices in counterclockwise order starting from the lowest x (then lowest y) vertex.

Return the vertex count followed by the coordinates.

## ASCII Visual

```
Half-planes forming a square:
0 <= x <= 1
0 <= y <= 1

Intersection polygon:
(0,0) -> (1,0) -> (1,1) -> (0,1)
```

## Input Format

- First line: integer `m`
- Next `m` lines: three integers `a b c` describing half-plane `a*x + b*y <= c`

## Output Format

- If empty: print `EMPTY`
- Else:
  - First line: integer `k` (number of vertices)
  - Next `k` lines: `x y` as floating values rounded to 6 decimals, polygon in CCW order

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= a, b, c <= 10^9`
- At least one feasible intersection may exist, but can also be empty

## Example

**Input:**
```
4
1 0 1
-1 0 0
0 1 1
0 -1 0
```

**Output:**
```
4
0.000000 0.000000
1.000000 0.000000
1.000000 1.000000
0.000000 1.000000
```

**Explanation:**

The four half-planes bound the unit square.

## Notes

- Use the standard O(m log m) half-plane intersection with sorting by angle and deque pruning.
- Parallel lines: keep the most restrictive; discard contradictory ones.
- A large bounding box half-planes may be added if needed; here input is complete as given.

## Related Topics

Half-Plane Intersection, Convex Polygons, Geometry Deque

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Main {
    static class Solution {
        private static final double EPS = 1e-9;

        private static class Line {
            double a, b, c, ang;
            Line(double a, double b, double c) {
                this.a = a;
                this.b = b;
                this.c = c;
                this.ang = Math.atan2(b, a);
            }
        }

        private double norm(Line l) {
        return 0;
    }

        private double[] intersect(Line l1, Line l2) {
        return null;
    }

        private boolean outside(double[] p, Line l) {
        return false;
    }

        private Line secondLast(Deque<Line> dq) {
        return 0;
    }

        private Line secondFirst(Deque<Line> dq) {
        return 0;
    }

        public List<double[]> halfPlaneIntersection(long[] A, long[] B, long[] C) {
        return null;
    }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] A = new long[m]; long[] B = new long[m]; long[] C = new long[m];
        for(int i=0; i<m; i++) { A[i] = sc.nextLong(); B[i] = sc.nextLong(); C[i] = sc.nextLong(); }
        List<double[]> res = new Solution().halfPlaneIntersection(A, B, C);
        if(res.isEmpty()) System.out.println("EMPTY");
        else {
            System.out.println(res.size());
            for(double[] p : res) {
                double x = Math.abs(p[0]) < 1e-9 ? 0.0 : p[0];
                double y = Math.abs(p[1]) < 1e-9 ? 0.0 : p[1];
                System.out.printf("%.6f %.6f\n", x, y);
            }
        }
    }
}
```

### Python

```python
import math
from typing import List, Tuple

EPS = 1e-9

def half_plane_intersection(A: List[int], B: List[int], C: List[int]) -> List[Tuple[float, float]]:
    return []
def main() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        m = int(next(it))
        A,B,C = [],[],[]
        for _ in range(m):
            A.append(int(next(it)))
            B.append(int(next(it)))
            C.append(int(next(it)))
        poly = half_plane_intersection(A,B,C)
        if not poly:
            print("EMPTY")
        else:
            print(len(poly))
            for x,y in poly:
                print(f"{x:.6f} {y:.6f}")
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
#include <deque>

using namespace std;

const double EPS = 1e-9;

struct Line {
    double a, b, c;
    double ang; // angle
};

struct Point {
    double x, y;
};

// Sort comparator
bool cmp(const Line& a, const Line& b) {
    if (abs(a.ang - b.ang) > EPS) return a.ang < b.ang;
    // Tie break: deeper cut first (larger c/norm? or smaller?)
    // Python code: t[3] / hypot(t[1], t[2]) is c/norm
    // If parallel, key is c/norm. Python uses lambda t: (t[0], t[3]/norm)
    // and prune parallel keeping tightest?
    // Python prune: if L[3]/normL < pruned[-1][3]/normP keep pruned else replace
    // This implies we want larger C/norm? No, wait.
    // Logic: ax + by <= c.
    // Distance from origin is c / norm.
    // Actually, let's just use the Python logic exactly.
    // Sort by angle.
    return false; // handled in sort block
}

Point intersect(Line l1, Line l2) {
    double det = l1.a * l2.b - l2.a * l1.b;
    if (abs(det) < EPS) return {NAN, NAN}; // Should not happen for non-parallel
    double x = (l1.c * l2.b - l2.c * l1.b) / det;
    double y = (l1.a * l2.c - l2.a * l1.c) / det;
    return {x, y};
}

bool outside(Point p, Line l) {
    if (isnan(p.x)) return true;
    return l.a * p.x + l.b * p.y - l.c > EPS;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (!(cin >> m)) return 0;

    vector<Line> lines;
    for (int i = 0; i < m; ++i) {
        double a, b, c;
        cin >> a >> b >> c;
        lines.push_back({a, b, c, atan2(b, a)});
    }

    sort(lines.begin(), lines.end(), [](const Line& a, const Line& b) {
        if (abs(a.ang - b.ang) > EPS) return a.ang < b.ang;
        double normA = hypot(a.a, a.b);
        double normB = hypot(b.a, b.b);
        return a.c / normA < b.c / normB;
    });

    // Prune parallel lines
    vector<Line> unique_lines;
    for (const auto& l : lines) {
        if (unique_lines.empty()) {
            unique_lines.push_back(l);
        } else {
            Line& last = unique_lines.back();
            if (abs(l.ang - last.ang) < EPS) {
                // Same angle, we sorted by c/norm ascending
                // Python logic: kept the one with smaller c/norm?
                // Python: if L[3]/normL < pruned[-1][3]/normP: pruned[-1] = L
                // So python keeps the SMALLER c/norm.
                // Since we sorted ascending, the smaller one is first.
                // So if we see a duplicate angle, the first one was smaller.
                // Wait, if sort is ascending, then unique_lines.back() is smaller than l.
                // So we just ignore l?
                // Let's re-read python carefully.
                // lines.sort(key=...) ascending.
                // for L in lines:
                //   if abs(ang diff) < EPS:
                //      if L.c/norm < last.c/norm: replace last with L
                //      else: ignore L
                // Since list is sorted ascending by c/norm:
                // The first one encountered for a given angle group is the SMALLEST c/norm.
                // Subsequent ones are larger.
                // So Python keeps the smallest c/norm.
                // Wait, if ax + by <= c, smaller c means the half plane has "smaller area" or is "shifted left"?
                // Yes, smaller c is tighter constraint.
                // So we want smallest c.
                // Since we sorted ascending, the first one is best.
                // So we just skip subsequent ones.
                continue; 
            } else {
                unique_lines.push_back(l);
            }
        }
    }

    deque<Line> dq;
    for (const auto& l : unique_lines) {
        while (dq.size() >= 2 && outside(intersect(dq[dq.size()-2], dq.back()), l)) {
            dq.pop_back();
        }
        while (dq.size() >= 2 && outside(intersect(dq[0], dq[1]), l)) {
            dq.pop_front();
        }
        dq.push_back(l);
    }

    while (dq.size() >= 3 && outside(intersect(dq[dq.size()-2], dq.back()), dq.front())) {
        dq.pop_back();
    }
    while (dq.size() >= 3 && outside(intersect(dq.front(), dq[1]), dq.back())) {
        dq.pop_front();
    }

    vector<Point> res;
    if (dq.size() < 3) {
        // empty
    } else {
        for (int i = 0; i < dq.size(); ++i) {
            Point p = intersect(dq[i], dq[(i+1)%dq.size()]);
            if (isnan(p.x)) { res.clear(); break; }
            res.push_back(p);
        }
    }

    // Filter duplicates and print
    // Logic from python: filter adjacent duplicates, rotate to min x,y
    if (res.empty()) {
        cout << "EMPTY\n";
    } else {
        // Remove duplicate points
        vector<Point> unique_pts;
        for (const auto& p : res) {
            if (unique_pts.empty()) unique_pts.push_back(p);
            else if (hypot(p.x - unique_pts.back().x, p.y - unique_pts.back().y) > EPS) {
                unique_pts.push_back(p);
            }
        }
        if (unique_pts.size() > 1 && hypot(unique_pts[0].x - unique_pts.back().x, unique_pts[0].y - unique_pts.back().y) < EPS) {
            unique_pts.pop_back();
        }

        if (unique_pts.size() < 3) {
            cout << "EMPTY\n";
        } else {
            // Find min idx
            int idx = 0;
            for (int i = 1; i < unique_pts.size(); ++i) {
                if (unique_pts[i].x < unique_pts[idx].x - EPS || 
                   (abs(unique_pts[i].x - unique_pts[idx].x) < EPS && unique_pts[i].y < unique_pts[idx].y)) {
                    idx = i;
                }
            }
            
            cout << unique_pts.size() << "\n";
            cout << fixed << setprecision(6);
            for (int i = 0; i < unique_pts.size(); ++i) {
                Point p = unique_pts[(idx + i) % unique_pts.size()];
                if (abs(p.x) < 1e-9) p.x = 0; // Avoid -0.000000
                if (abs(p.y) < 1e-9) p.y = 0;
                cout << p.x << " " << p.y << "\n";
            }
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const EPS = 1e-9;

class Solution {
    solve(A, B, C) {
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
    const nextInt = () => parseInt(next());

    let m = nextInt();
    let A = [], B = [], C = [];
    for(let i=0; i<m; i++) {
        A.push(nextInt()); B.push(nextInt()); C.push(nextInt());
    }

    const sol = new Solution();
    const res = sol.solve(A, B, C);
    
    if (res.length === 0) console.log("EMPTY");
    else {
        console.log(res.length);
        for(let p of res) {
            let px = Math.abs(p.x) < 1e-9 ? 0.0 : p.x;
            let py = Math.abs(p.y) < 1e-9 ? 0.0 : p.y;
            console.log(`${px.toFixed(6)} ${py.toFixed(6)}`);
        }
    }
});
```

