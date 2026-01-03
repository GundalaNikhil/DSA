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
time_limit: 2000
memory_limit: 256
---

# GEO-008: Minimum Enclosing Circle

## Problem Statement

Given `n` points in 2D, find the smallest circle that encloses all the points. Output the center coordinates and the radius.

Return `cx cy r` with values rounded to 6 decimal places.

## ASCII Visual

```
Points:
● (0,0)   ● (1,0)
     ● (0,1)

Smallest enclosing circle:
center (0.5, 0.5), radius ≈ 0.707107
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single line: three floating values `cx cy r` (rounded to 6 decimals)

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**
```
3
0 0
1 0
0 1
```

**Output:**
```
0.500000 0.500000 0.707107
```

**Explanation:**

The circle centered at `(0.5, 0.5)` with radius `sqrt(0.5)` encloses all three points.

## Notes

- Use a randomized incremental algorithm (Welzl) for expected `O(n)`.
- Beware of precision; store as doubles, output rounded to 6 decimals.
- With one point, radius is 0 and center is that point.

## Related Topics

Circle Geometry, Randomized Algorithms

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Main {

static class Solution {
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

    public double[] minEnclosingCircle(long[] xs, long[] ys) {
        //Implement here
        return new double[0];
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        double[] res = new Solution().minEnclosingCircle(xs, ys);
        double cx = Math.abs(res[0]) < 1e-9 ? 0.0 : res[0];
        double cy = Math.abs(res[1]) < 1e-9 ? 0.0 : res[1];
        double r = Math.abs(res[2]) < 1e-9 ? 0.0 : res[2];
        System.out.printf("%.6f\n%.6f\n%.6f\n", cx, cy, r);
    }
}
```

### Python

```python
import math, random
from typing import List, Tuple

def min_enclosing_circle(xs: List[int], ys: List[int]) -> Tuple[float,float,float]:
    # //Implement here
    return 0
def main() -> None:
    import sys
    sys.setrecursionlimit(200000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
        cx, cy, r = min_enclosing_circle(xs, ys)
        if abs(r) < 1e-9: r = 0.0
        if abs(cx) < 1e-9: cx = 0.0
        if abs(cy) < 1e-9: cy = 0.0

        print(f"{cx:.6f}\n{cy:.6f}\n{r:.6f}")
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
#include <random>

using namespace std;

struct Point {
    double x, y;
};

struct Circle {
    double x, y, r;
};

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

Circle circleTwo(Point a, Point b) {
    Point c = {(a.x + b.x) / 2.0, (a.y + b.y) / 2.0};
    return {c.x, c.y, dist(a, b) / 2.0};
}

Circle circleThree(Point a, Point b, Point c) {
    double d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
    if (abs(d) < 1e-9) return {0, 0, -1}; // Invalid
    double ux = ((a.x * a.x + a.y * a.y) * (b.y - c.y) + (b.x * b.x + b.y * b.y) * (c.y - a.y) + (c.x * c.x + c.y * c.y) * (a.y - b.y)) / d;
    double uy = ((a.x * a.x + a.y * a.y) * (c.x - b.x) + (b.x * b.x + b.y * b.y) * (a.x - c.x) + (c.x * c.x + c.y * c.y) * (b.x - a.x)) / d;
    return {ux, uy, dist({ux, uy}, a)};
}

bool inside(Point p, Circle c) {
    return dist(p, {c.x, c.y}) <= c.r + 1e-9;
}

Circle minEnclosingCircle(vector<Point>& pts) {
    //Implement here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> xs(n), ys(n);
    // Correct input parsing: Python reads xs then ys interleaved?
    // Wait, the Python code:
    // for _ in range(n): xs.append(int(next(it))); ys.append(int(next(it)))
    // So inputs are X1 Y1 X2 Y2 ...
    // My C++ fixes batch script fixed input parsing for GEO-008 to be interleaved.
    // I should maintain that.
    
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
    }

    Circle c = minEnclosingCircle(pts);

    cout << fixed << setprecision(6);
    if (abs(c.r) < 1e-9) c.r = 0.0;
    if (abs(c.x) < 1e-9) c.x = 0.0;
    if (abs(c.y) < 1e-9) c.y = 0.0;

    cout << c.x << "\n" << c.y << "\n" << c.r << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    solve(xs, ys) {
      //Implement here
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

    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    const c = sol.solve(xs, ys);
    
    let cx = Math.abs(c.x) < 1e-9 ? 0.0 : c.x;
    let cy = Math.abs(c.y) < 1e-9 ? 0.0 : c.y;
    let r = Math.abs(c.r) < 1e-9 ? 0.0 : c.r;

    console.log(cx.toFixed(6));
    console.log(cy.toFixed(6));
    console.log(r.toFixed(6));
});
```

