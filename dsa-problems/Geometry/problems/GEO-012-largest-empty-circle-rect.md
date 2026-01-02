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
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int xL = sc.nextInt();
        int yB = sc.nextInt();
        int xR = sc.nextInt();
        int yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n];
        int[] ys = new int[n];
        int[] rs = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
            rs[i] = sc.nextInt();
        }
        double result = new Solution().largestEmptyCircle(xL, yB, xR, yT, n, xs, ys, rs);
        System.out.printf("%.6f\n", result);
        sc.close();
    }
}
```

### Python

```python
import random

def largest_empty_circle(xL: int, yB: int, xR: int, yT: int, n: int, xs: list, ys: list, rs: list) -> float:
    # Implementation here
    return 0.0

def main():
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        xL = next(it)
        yB = next(it)
        xR = next(it)
        yT = next(it)
        n = next(it)
        xs = []
        ys = []
        rs = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
            rs.append(next(it))
        result = largest_empty_circle(xL, yB, xR, yT, n, xs, ys, rs)
        print(f"{result:.6f}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double largestEmptyCircle(int xL, int yB, int xR, int yT, int n, const vector<int>& xs, const vector<int>& ys, const vector<int>& rs) {
        // Implementation here
        return 0.0;
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

    Solution sol;
    double result = sol.largestEmptyCircle(xL, yB, xR, yT, n, xs, ys, rs);
    cout << fixed << setprecision(6) << result << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  largestEmptyCircle(xL, yB, xR, yT, n, xs, ys, rs) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const nextInt = () => parseInt(lines[idx++]);
    const xL = nextInt();
    const yB = nextInt();
    const xR = nextInt();
    const yT = nextInt();
    const n = nextInt();
    const xs = [], ys = [], rs = [];
    for (let i = 0; i < n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
        rs.push(nextInt());
    }
    const sol = new Solution();
    const result = sol.largestEmptyCircle(xL, yB, xR, yT, n, xs, ys, rs);
    console.log(result.toFixed(6));
});
```
