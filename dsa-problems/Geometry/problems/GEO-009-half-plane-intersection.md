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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539587/dsa/geometry/cvh1tufq8ytsijd8mulp.jpg)

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
    public List<double[]> intersectHalfPlanes(int m, long[][] planes) {
        // Implement here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        long[][] planes = new long[m][3];
        for (int i = 0; i < m; i++) {
            String[] p = br.readLine().trim().split("\\s+");
            planes[i][0] = Long.parseLong(p[0]);
            planes[i][1] = Long.parseLong(p[1]);
            planes[i][2] = Long.parseLong(p[2]);
        }

        Solution sol = new Solution();
        List<double[]> result = sol.intersectHalfPlanes(m, planes);

        if (result == null || result.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            System.out.println(result.size());
            PrintWriter out = new PrintWriter(System.out);
            for (double[] p : result) {
                out.printf("%.6f %.6f\n", p[0], p[1]);
            }
            out.flush();
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def intersect_half_planes(self, m, planes):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    idx = 1
    planes = []
    for _ in range(m):
        planes.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
        idx += 3

    sol = Solution()
    result = sol.intersect_half_planes(m, planes)

    if not result:
        print("EMPTY")
    else:
        print(len(result))
        for p in result:
            print(f"{p[0]:.6f} {p[1]:.6f}")

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
#include <deque>

using namespace std;

class Solution {
public:
    struct Point {
        double x, y;
    };

    vector<Point> intersectHalfPlanes(int m, vector<vector<long long>>& planes) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m;
    if (!(cin >> m)) return 0;

    vector<vector<long long>> planes(m, vector<long long>(3));
    for (int i = 0; i < m; i++) {
        cin >> planes[i][0] >> planes[i][1] >> planes[i][2];
    }

    Solution sol;
    vector<Solution::Point> result = sol.intersectHalfPlanes(m, planes);

    if (result.empty()) {
        cout << "EMPTY" << endl;
    } else {
        cout << result.size() << endl;
        cout << fixed << setprecision(6);
        for (const auto& p : result) {
            cout << p.x << " " << p.y << endl;
        }
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  intersectHalfPlanes(m, planes) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const m = parseInt(input[idx++]);
  const planes = [];
  for (let i = 0; i < m; i++) {
    planes.push([
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  const result = sol.intersectHalfPlanes(m, planes);

  if (result.length === 0) {
    console.log("EMPTY");
  } else {
    console.log(result.length);
    result.forEach((p) => console.log(`${p[0].toFixed(6)} ${p[1].toFixed(6)}`));
  }
}

solve();
```
