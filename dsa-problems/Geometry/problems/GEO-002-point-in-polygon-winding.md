---
problem_id: GEO_POINT_IN_POLYGON__8742
display_id: GEO-002
slug: point-in-polygon-winding
title: "Point in Polygon (Winding)"
difficulty: Medium
difficulty_score: 50
topics:
  - Computational Geometry
  - Polygon
  - Winding Number
tags:
  - geometry
  - polygon
  - winding-number
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-002: Point in Polygon (Winding)

## Problem Statement

Given a simple polygon with `n` vertices in 2D and a query point `Q`, determine whether `Q` is **inside**, **outside**, or on the **boundary** of the polygon using a winding-number style test.

Print one word: `inside`, `outside`, or `boundary`.

```
         P3(4,4)
          ●
         / \
        /   \
 P4(0,4)●    \
 |             ● P2(4,0)
 |              /
 ● P1(0,0)     /
        \     /
         \   /
          \ /
           ● Q(2,2)   => inside
```

## Input Format

- First line: integer `n` (number of polygon vertices)
- Next `n` lines: two integers `xi yi` for each vertex, in order (clockwise or counterclockwise)
- Last line: two integers `qx qy` for the query point `Q`

## Output Format

- Single word: `inside`, `outside`, or `boundary`

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi, qx, qy <= 10^9`
- Polygon is simple (non-self-intersecting); vertices are distinct.

## Example

**Input:**

```
4
0 0
4 0
4 4
0 4
2 2
```

**Output:**

```
inside
```

**Explanation:**

Point `(2,2)` lies strictly inside the axis-aligned square.

```
P4 ●-------● P3
   |       |
   |  Q ●  |
   |       |
P1 ●-------● P2
```

## Notes

- Points exactly on an edge or vertex must return `boundary`.
- Winding number (or an equivalent ray-crossing count with sign) should be used; avoid floating-point angle sums.
- Use 64-bit arithmetic to avoid overflow in cross products with large coordinates.

## Related Topics

Computational Geometry, Polygon Containment, Cross Product

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String checkPointInPolygon(int n, long[][] vertices, long qx, long qy) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[][] vertices = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] v = br.readLine().trim().split("\\s+");
            vertices[i][0] = Long.parseLong(v[0]);
            vertices[i][1] = Long.parseLong(v[1]);
        }

        String[] q = br.readLine().trim().split("\\s+");
        long qx = Long.parseLong(q[0]);
        long qy = Long.parseLong(q[1]);

        Solution sol = new Solution();
        System.out.println(sol.checkPointInPolygon(n, vertices, qx, qy));
    }
}
```

### Python

```python
import sys

class Solution:
    def check_point_in_polygon(self, n, vertices, qx, qy):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1
    vertices = []
    for _ in range(n):
        vertices.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    qx = int(input_data[idx])
    qy = int(input_data[idx+1])

    sol = Solution()
    print(sol.check_point_in_polygon(n, vertices, qx, qy))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string checkPointInPolygon(int n, vector<pair<long long, long long>>& vertices, long long qx, long long qy) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> vertices(n);
    for (int i = 0; i < n; i++) {
        cin >> vertices[i].first >> vertices[i].second;
    }

    long long qx, qy;
    cin >> qx >> qy;

    Solution sol;
    cout << sol.checkPointInPolygon(n, vertices, qx, qy) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  checkPointInPolygon(n, vertices, qx, qy) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const vertices = [];
  for (let i = 0; i < n; i++) {
    vertices.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const qx = BigInt(input[idx++]);
  const qy = BigInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.checkPointInPolygon(n, vertices, qx, qy));
}

solve();
```
