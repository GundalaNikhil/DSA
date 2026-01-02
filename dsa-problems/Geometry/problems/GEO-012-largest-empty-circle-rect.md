---
problem_id: GEO_LARGEST_EMPTY_CIRCLE__9186
display_id: GEO-012
slug: largest-empty-circle-rect
title: "The Quiet Zone Problem (Largest Empty Circle Among Disks)"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Voronoi
  - Optimization
tags:
  - geometry
  - circle
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-012: The Quiet Zone Problem

## Problem Statement

You are managing a rectangular development zone defined by its corners `[xL, yB]` and `[xR, yT]`. There are `n` noise sources located at points `(xi, yi)`, each having an inherent noise radius `ri`.

Your task is to find the **center and radius of the largest possible "Quiet Circle"** that:
1.  Lies **entirely within** the rectangular zone.
2.  Does **not overlap** with any of the `n` noise disks. A quiet circle of radius `R` and center `C` is valid if for every noise source `i`: `dist(C, Pi) >= R + ri`.

Output the maximum possible radius `R`.

## ASCII Visual

```
Rect: (0,0) to (10,10)
Noise Source: P(5,5), r=2

Largest Quiet Circle:
If centered at (2,2), dist to P is 4.24. 
R + r <= 4.24 => R + 2 <= 4.24 => R <= 2.24.
But R is limited by distance to edges (x=0, y=0) which is 2.0.
So R = 2.0.
```

## Input Format

- First line: five integers `xL yB xR yT n`
- Next `n` lines: three integers `xi yi ri` (noise source location and radius)

## Output Format

- Single floating number: maximum radius `R` (rounded to 6 decimals)

## Constraints

- `-10^9 <= xL < xR <= 10^9`
- `-10^9 <= yB < yT <= 10^9`
- `0 <= n <= 1000`
- `0 <= ri <= 10^9`
- All points `(xi, yi)` lie inside or on the rectangle boundary.

## Example

**Input:**
```
0 0 10 10 1
5 5 0
```

**Output:**
```
2.928932
```

**Explanation:**
The optimal center is roughly at `(2.071, 2.071)`. 
Distance to edges $x=0, y=0$ is $2.071$. (Wait, if R=2.928, the center is at (2.928, 2.928)).
Actually, for $P(5,5), r=0$, the center $C(x,x)$ must satisfy $x = \sqrt{(5-x)^2 + (5-x)^2}$.
$x = \sqrt{2}(5-x) \implies x(1+\sqrt{2}) = 5\sqrt{2} \implies x = \frac{5\sqrt{2}}{1+\sqrt{2}} = \frac{7.071}{2.414} \approx 2.928932$.
Radius $R = x = 2.928932$.

## Notes

- If $n=0$, the center is at the rectangle's midpoint.
- The radius $R$ can be $0$ if noise disks cover the entire area.

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double getRadius(double x, double y, int xL, int yB, int xR, int yT, int n, int[] xs, int[] ys, int[] rs) {
        // Implementation here
        return 0.0;
    }
}

class Main {
    static class Candidate implements Comparable<Candidate> {
        double x, y, r;
        Candidate(double x, double y, double r) { this.x = x; this.y = y; this.r = r; }
        @Override
        public int compareTo(Candidate other) {
            return Double.compare(other.r, this.r);
        }
    }

    private static double getRadius(double x, double y, int xL, int yB, int xR, int yT, int n, int[] xs, int[] ys, int[] rs) {
        double r = Math.min(Math.min(x - xL, xR - x), Math.min(y - yB, yT - y));
        if (r <= 0) return 0.0;
        for (int i = 0; i < n; i++) {
            double d = Math.sqrt((x - xs[i]) * (x - xs[i]) + (y - ys[i]) * (y - ys[i]));
            r = Math.min(r, d - rs[i]);
            if (r <= 0) return 0.0;
        }
        return r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int xL = sc.nextInt(), yB = sc.nextInt(), xR = sc.nextInt(), yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n], ys = new int[n], rs = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
            rs[i] = sc.nextInt();
        }

        List<Candidate> cands = new ArrayList<>();
        int gridRes = 120;
        for (int i = 0; i <= gridRes; i++) {
            double cx = xL + (xR - xL) * i / (double)gridRes;
            for (int j = 0; j <= gridRes; j++) {
                double cy = yB + (yT - yB) * j / (double)gridRes;
                double r = getRadius(cx, cy, xL, yB, xR, yT, n, xs, ys, rs);
                if (r > 0) cands.add(new Candidate(cx, cy, r));
            }
        }
        
        for (int i = 0; i < n; i++) {
            cands.add(new Candidate(xs[i], yB, getRadius(xs[i], yB, xL, yB, xR, yT, n, xs, ys, rs)));
            cands.add(new Candidate(xs[i], yT, getRadius(xs[i], yT, xL, yB, xR, yT, n, xs, ys, rs)));
            cands.add(new Candidate(xL, ys[i], getRadius(xL, ys[i], xL, yB, xR, yT, n, xs, ys, rs)));
            cands.add(new Candidate(xR, ys[i], getRadius(xR, ys[i], xL, yB, xR, yT, n, xs, ys, rs)));
            for (int j = i+1; j < n; j++) {
                double mx = (xs[i] + xs[j]) / 2.0;
                double my = (ys[i] + ys[j]) / 2.0;
                cands.add(new Candidate(mx, my, getRadius(mx, my, xL, yB, xR, yT, n, xs, ys, rs)));
            }
        }

        double bestR = 0.0;
        if (cands.isEmpty()) {
            bestR = Math.max(bestR, getRadius((xL + xR)/2.0, (yB + yT)/2.0, xL, yB, xR, yT, n, xs, ys, rs));
        } else {
            Collections.sort(cands);
            int count = 0;
            Set<String> seen = new HashSet<>();
            for (Candidate cand : cands) {
                if (count >= 60) break;
                String key = Math.round(cand.x * 10) + "_" + Math.round(cand.y * 10);
                if (seen.contains(key)) continue;
                seen.add(key);
                count++;
                
                double currX = cand.x, currY = cand.y, currR = cand.r;
                double step = Math.max(xR - xL, yT - yB) / (double)gridRes;
                while (step > 1e-13) {
                    boolean improved = false;
                    double[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}, {0.7,0.7}, {0.7,-0.7}, {-0.7,0.7}, {-0.7,-0.7}, {0.3,0.9}, {0.9,0.3}};
                    for (double[] d : dirs) {
                        double nx = currX + d[0] * step, ny = currY + d[1] * step;
                        if (nx >= xL && nx <= xR && ny >= yB && ny <= yT) {
                            double nr = getRadius(nx, ny, xL, yB, xR, yT, n, xs, ys, rs);
                            if (nr > currR) {
                                currR = nr; currX = nx; currY = ny;
                                improved = true;
                            }
                        }
                    }
                    if (!improved) step *= 0.5;
                }
                bestR = Math.max(bestR, currR);
            }
        }
        System.out.printf("%.6f\n", Math.max(0.0, bestR));
        sc.close();
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
    ld getRadius(ld x, ld y, int xL, int yB, int xR, int yT, int n, const vector<int>& xs, const vector<int>& ys, const vector<int>& rs) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int xL, yB, xR, yT, n;
    if (!(cin >> xL >> yB >> xR >> yT >> n)) return 0;
    
    vector<int> xs(n), ys(n), rs(n);
    for (int i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i] >> rs[i];
    }
    
    struct Candidate {
        ld x, y, r;
        bool operator>(const Candidate& other) const {
            return r > other.r;
        }
    };
    
    vector<Candidate> cands;
    int gridRes = 120;
    for (int i = 0; i <= gridRes; i++) {
        ld cx = xL + (ld)(xR - xL) * i / (ld)gridRes;
        for (int j = 0; j <= gridRes; j++) {
            ld cy = yB + (ld)(yT - yB) * j / (ld)gridRes;
            ld r = getRadius(cx, cy, xL, yB, xR, yT, n, xs, ys, rs);
            if (r > 0) cands.push_back({cx, cy, r});
        }
    }
    
    for (int i = 0; i < n; i++) {
        cands.push_back({(ld)xs[i], (ld)yB, getRadius(xs[i], yB, xL, yB, xR, yT, n, xs, ys, rs)});
        cands.push_back({(ld)xs[i], (ld)yT, getRadius(xs[i], yT, xL, yB, xR, yT, n, xs, ys, rs)});
        cands.push_back({(ld)xL, (ld)ys[i], getRadius(xL, ys[i], xL, yB, xR, yT, n, xs, ys, rs)});
        cands.push_back({(ld)xR, (ld)ys[i], getRadius(xR, ys[i], xL, yB, xR, yT, n, xs, ys, rs)});
        for (int j = i + 1; j < n; j++) {
            ld mx = (xs[i] + xs[j]) / 2.0L;
            ld my = (ys[i] + ys[j]) / 2.0L;
            cands.push_back({mx, my, getRadius(mx, my, xL, yB, xR, yT, n, xs, ys, rs)});
        }
    }
    
    ld bestR = 0.0;
    if (cands.empty()) {
        bestR = max(bestR, getRadius((xL + xR) / 2.0L, (yB + yT) / 2.0L, xL, yB, xR, yT, n, xs, ys, rs));
    } else {
        sort(cands.begin(), cands.end(), greater<Candidate>());
        int count = 0;
        set<pair<long long, long long>> seen;
        for (const auto& cand : cands) {
            if (count >= 60) break;
            pair<long long, long long> key = {round((double)cand.x * 10), round((double)cand.y * 10)};
            if (seen.count(key)) continue;
            seen.insert(key);
            count++;
            
            ld currX = cand.x, currY = cand.y, currR = cand.r;
            ld step = max((ld)(xR - xL), (ld)(yT - yB)) / (ld)gridRes;
            while (step > 1e-13L) {
                bool improved = false;
                ld dirs[10][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {0.7,0.7}, {0.7,-0.7}, {-0.7,0.7}, {-0.7,-0.7}, {0.3,0.9}, {0.9,0.3}};
                for (int i = 0; i < 10; i++) {
                    ld nx = currX + dirs[i][0] * step, ny = currY + dirs[i][1] * step;
                    if (nx >= xL && nx <= xR && ny >= yB && ny <= yT) {
                        ld nr = getRadius(nx, ny, xL, yB, xR, yT, n, xs, ys, rs);
                        if (nr > currR) {
                            currR = nr; currX = nx; currY = ny;
                            improved = true;
                        }
                    }
                }
                if (!improved) step *= 0.5L;
            }
            bestR = max(bestR, currR);
        }
    }
    cout << fixed << setprecision(6) << (double)max(0.0L, bestR) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  getRadius(x, y, xL, yB, xR, yT, n, xs, ys, rs) {
    // Implementation here
    return null;
  }
}

// I/O handling
```
