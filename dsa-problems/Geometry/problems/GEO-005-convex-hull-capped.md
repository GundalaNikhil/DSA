---
problem_id: GEO_CONVEX_HULL_CAPPED__2407
display_id: GEO-005
slug: convex-hull-capped
title: "Convex Hull with Interior Caps"
difficulty: Medium
difficulty_score: 65
topics:
  - Computational Geometry
  - Convex Hull
  - Geometry Filtering
tags:
  - geometry
  - convex-hull
  - filtering
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-005: Convex Hull with Interior Caps

## Problem Statement

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539584/dsa/geometry/onjqdalu1umoo97cxonu.jpg)

Given `n` points in 2D and an angle threshold `theta` (degrees, `0 < theta < 180`):

1. Build the convex hull of the points (include collinear boundary points as needed for a standard hull).
2. For each hull vertex, compute its interior angle (in degrees, using the CCW hull order).
3. Discard any hull vertex whose interior angle is **strictly less than** `theta`.
4. Return the remaining “capped” hull vertices in counterclockwise (CCW) order. If all vertices are discarded, output `0`.

Print the vertex count, followed by the remaining vertices.

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`
- Last line: integer `theta`

## Output Format

- First line: integer `k` = number of capped hull vertices
- Next `k` lines (if `k > 0`): `x y` for each vertex in CCW order

## ASCII/Emoji Visual

```
🟢 square hull, theta = 60°
  ● (0,0) ---- ● (4,0)
  |              |
  |      ●       |   => keep all 4 (90° ≥ 60°)
  ● (0,4) ---- ● (4,4)

🔺 triangle hull, theta = 80°
        ●
       / \
      /   \
   ● ----- ●
   all angles 60° < 80° ⇒ discard all ⇒ k = 0
```

## Constraints

- `3 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`
- `0 < theta < 180`

## Example 1

**Input:**

```
5
0 0
4 0
4 4
0 4
2 2
60
```

**Output:**

```
4
0 0
4 0
4 4
0 4
```

**Explanation:** Square hull has interior angles 90°, all ≥ 60°, so nothing is capped away.

## Example 2

**Input:**

```
4
0 0
2 2
4 0
2 -2
100
```

**Output:**

```
0
```

**Explanation:** Hull is a diamond with interior angles 90°; all are < 100°, so every vertex is discarded.

## Notes

- Interior angle is measured inside the polygon; for a convex hull it lies in `(0, 180]`.
- Use squared lengths to avoid precision issues when comparing angles (via cross and dot, or cosine).
- If `k = 0`, print just `0`.

## Related Topics

Convex Hull, Geometry Filtering, Cross Product

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<long[]> findCappedHull(int n, long[][] points, int theta) {
        // Implement here
        return new ArrayList<>();
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

        String thetaLine = br.readLine();
        if (thetaLine == null) return;
        int theta = Integer.parseInt(thetaLine.trim());

        Solution sol = new Solution();
        List<long[]> result = sol.findCappedHull(n, points, theta);

        if (result == null || result.isEmpty()) {
            System.out.println("0");
        } else {
            PrintWriter out = new PrintWriter(System.out);
            out.println(result.size());
            for (long[] p : result) {
                out.println(p[0] + " " + p[1]);
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
    def find_capped_hull(self, n, points, theta):
        # Implement here
        return []

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

    theta = int(input_data[idx])

    sol = Solution()
    result = sol.find_capped_hull(n, points, theta)
    if not result:
        print("0")
    else:
        print(len(result))
        for p in result:
            print(f"{p[0]} {p[1]}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<pair<long long, long long>> findCappedHull(int n, vector<pair<long long, long long>>& points, int theta) {
        // Implement here
        return {};
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

    int theta;
    cin >> theta;

    Solution sol;
    vector<pair<long long, long long>> result = sol.findCappedHull(n, points, theta);

    if (result.empty()) {
        cout << "0" << endl;
    } else {
        cout << result.size() << endl;
        for (const auto& p : result) {
            cout << p.first << " " << p.second << endl;
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
  findCappedHull(n, points, theta) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const points = [];
  for (let i = 0; i < n; i++) {
    points.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const theta = parseInt(input[idx++]);

  const sol = new Solution();
  const result = sol.findCappedHull(n, points, theta);

  if (result.length === 0) {
    console.log("0");
  } else {
    console.log(result.length);
    result.forEach((p) => console.log(`${p[0]} ${p[1]}`));
  }
}

solve();
```
