---
problem_id: GEO_ROTATING_CALIPERS_DIAM__3154
display_id: GEO-007
slug: rotating-calipers-diameter
title: "Rotating Calipers Diameter"
difficulty: Medium
difficulty_score: 55
topics:
  - Computational Geometry
  - Rotating Calipers
  - Convex Polygon
tags:
  - geometry
  - diameter
  - rotating-calipers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-007: Rotating Calipers Diameter

## Problem Statement

You are given a **convex** polygon with `n` vertices in counterclockwise order. Find the maximum squared distance between any pair of its vertices (the squared diameter of the polygon).

Return that maximum squared distance as an integer.

## Emoji Visual

```
🟢 Square (0,0)-(1,0)-(1,1)-(0,1)
Fartherst pair are opposite corners:
🟢(0,0) ..... 🟢(1,1)   dist^2 = 2
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi` in CCW order

## Output Format

- Single integer: maximum squared distance between any two vertices

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- Polygon is convex and vertices are given in CCW order

## Example

**Input:**
```
4
0 0
1 0
1 1
0 1
```

**Output:**
```
2
```

**Explanation:**

Opposite corners `(0,0)` and `(1,1)` give the diameter squared `2`.

## Notes

- Work with squared distances to avoid square roots.
- Rotating calipers over antipodal pairs gives `O(n)` after one pass.
- For triangles, check all three edges and vertices with calipers logic.

## Related Topics

Rotating Calipers, Convex Geometry, Distance Computation

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long diameterSquared(long[] xs, long[] ys) {
        // Implementation here
        return 0;
    }
}

class Main {
static class Solution {
    private long cross(long ax, long ay, long bx, long by, long cx, long cy) {
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
    }
    private long dist2(long ax, long ay, long bx, long by) {
        long dx = ax - bx, dy = ay - by;
        return dx*dx + dy*dy;
    }
    public long diameterSquared(long[] xs, long[] ys) {
        int n = xs.length;
        if (n <= 1) return 0;
        long best = 0;
        int j = 1;
        for (int i = 0; i < n; i++) {
            int ni = (i + 1) % n;
            while (cross(xs[i], ys[i], xs[ni], ys[ni], xs[(j+1)%n], ys[(j+1)%n]) >
                   cross(xs[i], ys[i], xs[ni], ys[ni], xs[j], ys[j])) {
                j = (j + 1) % n;
            }
            best = Math.max(best, dist2(xs[i], ys[i], xs[j], ys[j]));
            best = Math.max(best, dist2(xs[ni], ys[ni], xs[j], ys[j]));
        }
        return best;
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
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    long long diameterSquared(const vector<long long>& xs, const vector<long long>& ys) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    cout << diameterSquared(xs, ys) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(xs, ys) {
    // Implementation here
    return null;
  }
}

const readline = require('readline');

class Solution {
    solve(xs, ys) {
        let pts = xs.map((x, i) => ({x: BigInt(x), y: BigInt(ys[i])}));
        pts.sort((a, b) => {
            if (a.x !== b.x) return a.x < b.x ? -1 : 1;
            if (a.y !== b.y) return a.y < b.y ? -1 : 1;
            return 0;
        });
        pts = pts.filter((p, i) => i === 0 || p.x !== pts[i-1].x || p.y !== pts[i-1].y);
        
        if (pts.length <= 1) return 0n;
        if (pts.length === 2) return (pts[0].x-pts[1].x)**2n + (pts[0].y-pts[1].y)**2n;
        
        const cross = (o, a, b) => (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
        let lower = [];
        for (let p of pts) {
            while (lower.length >= 2 && cross(lower[lower.length-2], lower[lower.length-1], p) <= 0n) lower.pop();
            lower.push(p);
        }
        let upper = [];
        for (let i = pts.length - 1; i >= 0; i--) {
            let p = pts[i];
            while (upper.length >= 2 && cross(upper[upper.length-2], upper[upper.length-1], p) <= 0n) upper.pop();
            upper.push(p);
        }
        lower.pop(); upper.pop();
        let hull = lower.concat(upper);
        
        if (hull.length <= 1) return 0n;
        if (hull.length === 2) return (hull[0].x-hull[1].x)**2n + (hull[0].y-hull[1].y)**2n;
        
        let maxD2 = 0n;
        let k = 1;
        let n = hull.length;
        
        const distSq = (a, b) => (a.x-b.x)**2n + (a.y-b.y)**2n;
        const absVal = (n) => n < 0n ? -n : n;

        for (let i = 0; i < n; i++) {
            while (true) {
                let nextK = (k + 1) % n;
                let p_i = hull[i];
                let p_next = hull[(i+1)%n];
                
                let distK = absVal(cross(p_i, p_next, hull[k]));
                let distNextK = absVal(cross(p_i, p_next, hull[nextK]));
                
                if (distNextK > distK) {
                    k = nextK;
                } else {
                    break;
                }
            }
            
            let d1 = distSq(hull[i], hull[k]);
            let d2 = distSq(hull[(i+1)%n], hull[k]);
            if (d1 > maxD2) maxD2 = d1;
            if (d2 > maxD2) maxD2 = d2;
        }
        return maxD2.toString();
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
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
```
