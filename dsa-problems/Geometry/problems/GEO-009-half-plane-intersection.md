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
import java.util.*;

class Solution {
    public List<double[]> intersectHalfPlanes(long[] a, long[] b, long[] c) {
        // Your implementation here
        return Collections.emptyList();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        long[] a = new long[m], b = new long[m], c = new long[m];
        for (int i = 0; i < m; i++) {
            a[i] = sc.nextLong();
            b[i] = sc.nextLong();
            c[i] = sc.nextLong();
        }
        Solution sol = new Solution();
        List<double[]> poly = sol.intersectHalfPlanes(a, b, c);
        if (poly.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            System.out.println(poly.size());
            for (double[] p : poly) {
                System.out.printf("%.6f %.6f%n", p[0], p[1]);
            }
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def half_plane_intersection(a: List[int], b: List[int], c: List[int]) -> List[Tuple[float, float]]:
    # Your implementation here
    return []

def main() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    m = int(next(it))
    A,B,C = [],[],[]
    for _ in range(m):
        A.append(int(next(it))); B.append(int(next(it))); C.append(int(next(it)))
    poly = half_plane_intersection(A,B,C)
    if not poly:
        print("EMPTY")
    else:
        print(len(poly))
        for x,y in poly:
            print(f"{x:.6f} {y:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<pair<double,double>> halfPlaneIntersection(const vector<long long>& a, const vector<long long>& b, const vector<long long>& c) {
    // Your implementation here
    return {};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> m)) return 0;
    vector<long long> a(m), b(m), c(m);
    for (int i = 0; i < m; ++i) cin >> a[i] >> b[i] >> c[i];
    auto poly = halfPlaneIntersection(a,b,c);
    if (poly.empty()) {
        cout << "EMPTY\n";
    } else {
        cout << poly.size() << "\n";
        cout.setf(ios::fixed); cout << setprecision(6);
        for (auto &p : poly) cout << p.first << " " << p.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function halfPlaneIntersection(a, b, c) {
  // Your implementation here
  return [];
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const m = data[idx++];
  const a = new Array(m), b = new Array(m), c = new Array(m);
  for (let i = 0; i < m; i++) { a[i] = data[idx++]; b[i] = data[idx++]; c[i] = data[idx++]; }
  const poly = halfPlaneIntersection(a, b, c);
  if (poly.length === 0) {
    console.log("EMPTY");
  } else {
    console.log(poly.length);
    for (const [x,y] of poly) console.log(`${x.toFixed(6)} ${y.toFixed(6)}`);
  }
}

main();
```
