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

class Solution {
    public List<double[]> halfPlaneIntersection(long[] A, long[] B, long[] C) {
        // Implementation here
        return new ArrayList<>();
    }
}

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
            return Math.hypot(l.a, l.b);
        }

        private double[] intersect(Line l1, Line l2) {
            double det = l1.a * l2.b - l2.a * l1.b;
            if (Math.abs(det) < EPS) return null;
            double x = (l1.c * l2.b - l2.c * l1.b) / det;
            double y = (l1.a * l2.c - l2.a * l1.c) / det;
            return new double[]{x, y};
        }

        private boolean outside(double[] p, Line l) {
            return l.a * p[0] + l.b * p[1] - l.c > EPS;
        }

        private Line secondLast(Deque<Line> dq) {
            Iterator<Line> it = dq.descendingIterator();
            it.next();
            return it.next();
        }

        private Line secondFirst(Deque<Line> dq) {
            Iterator<Line> it = dq.iterator();
            it.next();
            return it.next();
        }

        public List<double[]> halfPlaneIntersection(long[] A, long[] B, long[] C) {
            int n = A.length;
            List<Line> lines = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                lines.add(new Line(A[i], B[i], C[i]));
            }
            lines.sort((l1, l2) -> {
                if (Math.abs(l1.ang - l2.ang) > EPS) return Double.compare(l1.ang, l2.ang);
                double o1 = l1.c / norm(l1);
                double o2 = l2.c / norm(l2);
                return Double.compare(o1, o2);
            });

            List<Line> pruned = new ArrayList<>();
            for (Line l : lines) {
                if (!pruned.isEmpty() && Math.abs(l.ang - pruned.get(pruned.size() - 1).ang) < EPS) {
                    Line prev = pruned.get(pruned.size() - 1);
                    if (l.c / norm(l) < prev.c / norm(prev)) {
                        pruned.set(pruned.size() - 1, l);
                    }
                } else {
                    pruned.add(l);
                }
            }
            lines = pruned;

            Deque<Line> dq = new ArrayDeque<>();
            for (Line l : lines) {
                while (dq.size() >= 2) {
                    double[] p = intersect(secondLast(dq), dq.peekLast());
                    if (p == null || !outside(p, l)) break;
                    dq.removeLast();
                }
                while (dq.size() >= 2) {
                    double[] p = intersect(dq.peekFirst(), secondFirst(dq));
                    if (p == null || !outside(p, l)) break;
                    dq.removeFirst();
                }
                dq.addLast(l);
            }

            while (dq.size() >= 3) {
                double[] p = intersect(secondLast(dq), dq.peekLast());
                if (p == null || !outside(p, dq.peekFirst())) break;
                dq.removeLast();
            }
            while (dq.size() >= 3) {
                double[] p = intersect(dq.peekFirst(), secondFirst(dq));
                if (p == null || !outside(p, dq.peekLast())) break;
                dq.removeFirst();
            }

            if (dq.size() < 3) return Collections.emptyList();

            List<Line> dqList = new ArrayList<>(dq);
            List<double[]> pts = new ArrayList<>();
            for (int i = 0; i < dqList.size(); i++) {
                Line l1 = dqList.get(i);
                Line l2 = dqList.get((i + 1) % dqList.size());
                double[] p = intersect(l1, l2);
                if (p == null) return Collections.emptyList();
                pts.add(p);
            }

            List<double[]> unique = new ArrayList<>();
            for (double[] p : pts) {
                if (unique.isEmpty()) {
                    unique.add(p);
                } else {
                    double[] last = unique.get(unique.size() - 1);
                    if (Math.hypot(p[0] - last[0], p[1] - last[1]) > EPS) {
                        unique.add(p);
                    }
                }
            }
            if (unique.size() > 1) {
                double[] first = unique.get(0);
                double[] last = unique.get(unique.size() - 1);
                if (Math.hypot(first[0] - last[0], first[1] - last[1]) < EPS) {
                    unique.remove(unique.size() - 1);
                }
            }
            if (unique.size() < 3) return Collections.emptyList();

            int idx = 0;
            for (int i = 1; i < unique.size(); i++) {
                double[] p = unique.get(i);
                double[] best = unique.get(idx);
                if (p[0] < best[0] - EPS || (Math.abs(p[0] - best[0]) < EPS && p[1] < best[1])) {
                    idx = i;
                }
            }
            List<double[]> res = new ArrayList<>();
            for (int i = 0; i < unique.size(); i++) {
                res.add(unique.get((idx + i) % unique.size()));
            }
            return res;
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
    bool cmp(const Line& a, const Line& b) {
        // Implementation here
        return {};
    }
};

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
const readline = require("readline");

class Solution {
  solve(A, B, C) {
    // Implementation here
    return null;
  }
}

const readline = require('readline');
const EPS = 1e-9;

class Solution {
    solve(A, B, C) {
        let lines = A.map((a, i) => ({
            a: Number(a), b: Number(B[i]), c: Number(C[i]), 
            ang: Math.atan2(Number(B[i]), Number(a))
        }));

        lines.sort((l1, l2) => {
            if (Math.abs(l1.ang - l2.ang) > EPS) return l1.ang - l2.ang;
            return 0; 
        });

        let unique = [];
        for (let l of lines) {
            if (unique.length > 0 && Math.abs(l.ang - unique[unique.length-1].ang) < EPS) {
                let last = unique[unique.length-1];
                let normL = Math.hypot(l.a, l.b);
                let normLast = Math.hypot(last.a, last.b);
                if (l.c / normL < last.c / normLast) {
                    unique[unique.length-1] = l;
                }
            } else {
                unique.push(l);
            }
        }
        lines = unique;

        const intersect = (l1, l2) => {
            let det = l1.a * l2.b - l2.a * l1.b;
            if (Math.abs(det) < EPS) return null;
            let x = (l1.c * l2.b - l2.c * l1.b) / det;
            let y = (l1.a * l2.c - l2.a * l1.c) / det;
            return {x, y};
        };

        const outside = (p, l) => {
            if (!p) return true; 
            return l.a * p.x + l.b * p.y - l.c > EPS;
        };

        let dq = [];
        for (let l of lines) {
            while (dq.length >= 2 && outside(intersect(dq[dq.length-2], dq[dq.length-1]), l)) dq.pop();
            while (dq.length >= 2 && outside(intersect(dq[0], dq[1]), l)) dq.shift();
            dq.push(l);
        }

        while (dq.length >= 3 && outside(intersect(dq[dq.length-2], dq[dq.length-1]), dq[0])) dq.pop();
        while (dq.length >= 3 && outside(intersect(dq[0], dq[1]), dq[dq.length-1])) dq.shift();

        if (dq.length < 3) return [];

        let pts = [];
        for (let i = 0; i < dq.length; i++) {
            let p = intersect(dq[i], dq[(i+1)%dq.length]);
            if (!p) return [];
            pts.push(p);
        }

        let uniquePts = [];
        for (let p of pts) {
            if (uniquePts.length === 0) uniquePts.push(p);
            else if (Math.hypot(p.x - uniquePts[uniquePts.length-1].x, p.y - uniquePts[uniquePts.length-1].y) > EPS) {
                uniquePts.push(p);
            }
        }
        if (uniquePts.length > 1 && Math.hypot(uniquePts[0].x - uniquePts[uniquePts.length-1].x, uniquePts[0].y - uniquePts[uniquePts.length-1].y) < EPS) {
            uniquePts.pop();
        }

        if (uniquePts.length < 3) return [];

        let minIdx = 0;
        for (let i = 1; i < uniquePts.length; i++) {
            if (uniquePts[i].x < uniquePts[minIdx].x - EPS || 
               (Math.abs(uniquePts[i].x - uniquePts[minIdx].x) < EPS && uniquePts[i].y < uniquePts[minIdx].y)) {
                minIdx = i;
            }
        }
        
        let res = [];
        for (let i = 0; i < uniquePts.length; i++) {
            res.push(uniquePts[(minIdx + i) % uniquePts.length]);
        }
        return res;
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
