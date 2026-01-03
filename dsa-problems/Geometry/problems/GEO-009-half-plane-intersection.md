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
import java.io.*;
import java.util.*;

class Solution {
    public List<double[]> halfPlaneIntersection(long[] a, long[] b, long[] c) {
        //Implemention here
        return new ArrayList<>();
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
        int m = Integer.parseInt(data[idx++]);
        if (data.length < 1 + 3 * m) return;
        long[] a = new long[m];
        long[] b = new long[m];
        long[] c = new long[m];
        for (int i = 0; i < m; i++) {
            a[i] = Long.parseLong(data[idx++]);
            b[i] = Long.parseLong(data[idx++]);
            c[i] = Long.parseLong(data[idx++]);
        }

        Solution solution = new Solution();
        List<double[]> result = solution.halfPlaneIntersection(a, b, c);
        if (result.isEmpty()) {
            System.out.print("EMPTY");
            return;
        }
        StringBuilder out = new StringBuilder();
        out.append(result.size()).append('\n');
        for (double[] p : result) {
            out.append(String.format(Locale.US, "%.6f %.6f", p[0], p[1])).append('\n');
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def half_plane_intersection(a, b, c):
    # //Implemention here
    return []

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    m = int(data[idx]);
    idx += 1
    if len(data) < 1 + 3 * m:
        return
    a = []
    b = []
    c = []
    for _ in range(m):
        a.append(int(data[idx]));
        b.append(int(data[idx + 1]));
        c.append(int(data[idx + 2]));
        idx += 3
    result = half_plane_intersection(a, b, c)
    if not result:
        sys.stdout.write("EMPTY")
        return
    out_lines = [str(len(result))]
    for x, y in result:
        out_lines.append(f"{x:.6f} {y:.6f}")
    sys.stdout.write("\n".join(out_lines))

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

vector<pair<double, double>> half_plane_intersection(const vector<long long>& a, const vector<long long>& b,
                                                     const vector<long long>& c) {
    //Implemention here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    if (!(cin >> m)) return 0;
    vector<long long> a(m), b(m), c(m);
    for (long long i = 0; i < m; i++) {
        cin >> a[i] >> b[i] >> c[i];
    }

    vector<pair<double, double>> result = half_plane_intersection(a, b, c);
    if (result.empty()) {
        cout << "EMPTY";
        return 0;
    }
    cout << result.size() << "\n";
    cout << fixed << setprecision(6);
    for (const auto& p : result) {
        cout << p.first << " " << p.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function halfPlaneIntersection(a, b, c) {
  //Implemention here
  return [];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
const m = data[idx++];
if (!Number.isFinite(m) || data.length < 1 + 3 * m) {
  process.exit(0);
}
const a = [];
const b = [];
const c = [];
for (let i = 0; i < m; i++) {
  a.push(data[idx++]);
  b.push(data[idx++]);
  c.push(data[idx++]);
}

const result = halfPlaneIntersection(a, b, c);
if (!result || result.length === 0) {
  process.stdout.write("EMPTY");
  process.exit(0);
}
let out = [];
out.push(String(result.length));
for (const p of result) {
  out.push(p[0].toFixed(6) + " " + p[1].toFixed(6));
}
process.stdout.write(out.join("\n"));
```

