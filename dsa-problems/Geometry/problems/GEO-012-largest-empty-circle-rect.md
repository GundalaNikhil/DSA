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
import java.io.*;
import java.util.*;

class Solution {
    public double largestQuietCircle(long xL, long yB, long xR, long yT, long[] xs, long[] ys, long[] rs) {
        //Implemention here
        return 0.0;
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        if (data.length < 5) return;
        long xL = Long.parseLong(data[idx++]);
        long yB = Long.parseLong(data[idx++]);
        long xR = Long.parseLong(data[idx++]);
        long yT = Long.parseLong(data[idx++]);
        int n = Integer.parseInt(data[idx++]);
        if (data.length < 5 + 3 * n) return;
        long[] xs = new long[n];
        long[] ys = new long[n];
        long[] rs = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Long.parseLong(data[idx++]);
            ys[i] = Long.parseLong(data[idx++]);
            rs[i] = Long.parseLong(data[idx++]);
        }

        Solution solution = new Solution();
        double result = solution.largestQuietCircle(xL, yB, xR, yT, xs, ys, rs);
        System.out.print(String.format(Locale.US, "%.6f", result));
    }
}
```

### Python

```python
import sys

def largest_quiet_circle(xL, yB, xR, yT, xs, ys, rs):
    # //Implemention here
    return 0.0

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    if len(data) < 5:
        return
    xL = int(data[idx]);
    yB = int(data[idx + 1]);
    xR = int(data[idx + 2]);
    yT = int(data[idx + 3]);
    idx += 4
    n = int(data[idx]);
    idx += 1
    if len(data) < 5 + 3 * n:
        return
    xs = []
    ys = []
    rs = []
    for _ in range(n):
        xs.append(int(data[idx]));
        ys.append(int(data[idx + 1]));
        rs.append(int(data[idx + 2]));
        idx += 3
    result = largest_quiet_circle(xL, yB, xR, yT, xs, ys, rs)
    sys.stdout.write(f"{result:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

double largest_quiet_circle(long long xL, long long yB, long long xR, long long yT,
                            const vector<long long>& xs, const vector<long long>& ys, const vector<long long>& rs) {
    //Implemention here
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long xL, yB, xR, yT;
    long long n;
    if (!(cin >> xL >> yB >> xR >> yT >> n)) return 0;
    vector<long long> xs(n), ys(n), rs(n);
    for (long long i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i] >> rs[i];
    }

    double result = largest_quiet_circle(xL, yB, xR, yT, xs, ys, rs);
    cout << fixed << setprecision(6) << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function largestQuietCircle(xL, yB, xR, yT, xs, ys, rs) {
  //Implemention here
  return 0.0;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
if (data.length < 5) {
  process.exit(0);
}
const xL = data[idx++];
const yB = data[idx++];
const xR = data[idx++];
const yT = data[idx++];
const n = data[idx++];
if (!Number.isFinite(n) || data.length < 5 + 3 * n) {
  process.exit(0);
}
const xs = [];
const ys = [];
const rs = [];
for (let i = 0; i < n; i++) {
  xs.push(data[idx++]);
  ys.push(data[idx++]);
  rs.push(data[idx++]);
}

const result = largestQuietCircle(xL, yB, xR, yT, xs, ys, rs);
process.stdout.write(result.toFixed(6));
```
