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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767567845/dsa/geometry/cfjqty1oj7yjm7jjjgey.jpg)


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
import java.io.*;

class Solution {
    public double largestEmptyCircle(double xL, double yB, double xR, double yT, int n, double[][] points) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        double xL = Double.parseDouble(parts[0]);
        double yB = Double.parseDouble(parts[1]);
        double xR = Double.parseDouble(parts[2]);
        double yT = Double.parseDouble(parts[3]);
        int n = Integer.parseInt(parts[4]);

        double[][] points = new double[n][3];
        for (int i = 0; i < n; i++) {
            line = br.readLine();
            parts = line.trim().split("\\s+");
            points[i][0] = Double.parseDouble(parts[0]);
            points[i][1] = Double.parseDouble(parts[1]);
            points[i][2] = Double.parseDouble(parts[2]); // radius
        }

        Solution sol = new Solution();
        System.out.printf("%.6f%n", sol.largestEmptyCircle(xL, yB, xR, yT, n, points));
    }
}
```

### Python

```python
import sys

class Solution:
    def largest_empty_circle(self, xL, yB, xR, yT, n, points):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        xL = float(next(iterator))
        yB = float(next(iterator))
        xR = float(next(iterator))
        yT = float(next(iterator))
        n = int(next(iterator))

        points = []
        for _ in range(n):
            xi = float(next(iterator))
            yi = float(next(iterator))
            ri = float(next(iterator))
            points.append([xi, yi, ri])

    except StopIteration:
        pass

    sol = Solution()
    print(f"{sol.largest_empty_circle(xL, yB, xR, yT, n, points):.6f}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

class Solution {
public:
    double largestEmptyCircle(double xL, double yB, double xR, double yT, int n, vector<vector<double>>& points) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double xL, yB, xR, yT;
    int n;
    if (!(cin >> xL >> yB >> xR >> yT >> n)) return 0;

    vector<vector<double>> points(n, vector<double>(3));
    for (int i = 0; i < n; i++) {
        cin >> points[i][0] >> points[i][1] >> points[i][2];
    }

    Solution sol;
    cout << fixed << setprecision(6) << sol.largestEmptyCircle(xL, yB, xR, yT, n, points) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  largestEmptyCircle(xL, yB, xR, yT, n, points) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 5) return;

  let idx = 0;
  function readString() {
    return input[idx++];
  }
  function readFloat() {
    return parseFloat(readString());
  }
  function readInt() {
    return parseInt(readString());
  }

  const xL = readFloat();
  const yB = readFloat();
  const xR = readFloat();
  const yT = readFloat();
  const n = readInt();

  const points = [];
  for (let i = 0; i < n; i++) {
    const xi = readFloat();
    const yi = readFloat();
    const ri = readFloat();
    points.push([xi, yi, ri]);
  }

  const sol = new Solution();
  console.log(sol.largestEmptyCircle(xL, yB, xR, yT, n, points).toFixed(6));
}

solve();
```
