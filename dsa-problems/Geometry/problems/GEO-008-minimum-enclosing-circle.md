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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539586/dsa/geometry/d5zv80g327upnuahpvc6.jpg)

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

class Solution {
    public double[] findMinEnclosingCircle(int n, long[][] points) {
        // Implement here
        return new double[3];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[][] points = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] p = br.readLine().trim().split("\\s+");
            points[i][0] = Long.parseLong(p[0]);
            points[i][1] = Long.parseLong(p[1]);
        }

        Solution sol = new Solution();
        double[] result = sol.findMinEnclosingCircle(n, points);
        System.out.printf("%.6f %.6f %.6f\n", result[0], result[1], result[2]);
    }
}
```

### Python

```python
import sys
import random

class Solution:
    def find_min_enclosing_circle(self, n, points):
        # Implement here
        return 0, 0, 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1
    points = []
    for _ in range(n):
        points.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    sol = Solution()
    cx, cy, r = sol.find_min_enclosing_circle(n, points)
    print(f"{cx:.6f} {cy:.6f} {r:.6f}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <random>

using namespace std;

class Solution {
public:
    struct Result {
        double cx, cy, r;
    };

    Result findMinEnclosingCircle(int n, vector<pair<long long, long long>>& points) {
        // Implement here
        return {0, 0, 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    Solution sol;
    Solution::Result res = sol.findMinEnclosingCircle(n, points);
    cout << fixed << setprecision(6) << res.cx << " " << res.cy << " " << res.r << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMinEnclosingCircle(n, points) {
    // Implement here
    return { cx: 0, cy: 0, r: 0 };
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const points = [];
  for (let i = 0; i < n; i++) {
    points.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  const { cx, cy, r } = sol.findMinEnclosingCircle(n, points);
  console.log(`${cx.toFixed(6)} ${cy.toFixed(6)} ${r.toFixed(6)}`);
}

solve();
```
