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
import java.io.*;

class Solution {
    public List<double[]> halfPlaneIntersection(long[] A, long[] B, long[] C) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] A = new long[m]; long[] B = new long[m]; long[] C = new long[m];
        for(int i=0; i<m; i++) { A[i] = sc.nextLong(); B[i] = sc.nextLong(); C[i] = sc.nextLong(); }
        List<double[]> res = new Solution().halfPlaneIntersection(A, B, C);
        if(res.isEmpty()) System.out.println("EMPTY");
        else {
            System.out.println(res.size());
            for(double[] p : res) {
                double x = Math.abs(p[0]) < 1e-9 ? 0.0 : p[0];
                double y = Math.abs(p[1]) < 1e-9 ? 0.0 : p[1];
                System.out.printf("%.6f %.6f\n", x, y);
            }
        }
        sc.close();
    }
}
```

### Python

```python
from typing import List

def half_plane_intersection(A: List[int], B: List[int], C: List[int]) -> List:
    # Implementation here
    return []

def main():
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        m = next(it)
        A = []
        B = []
        C = []
        for _ in range(m):
            A.append(next(it))
            B.append(next(it))
            C.append(next(it))
        res = half_plane_intersection(A, B, C)
        if not res:
            print("EMPTY")
        else:
            print(len(res))
            for p in res:
                x = 0.0 if abs(p[0]) < 1e-9 else p[0]
                y = 0.0 if abs(p[1]) < 1e-9 else p[1]
                print(f"{x:.6f} {y:.6f}")
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
    vector<pair<double, double>> halfPlaneIntersection(int m, const vector<int>& A, const vector<int>& B, const vector<int>& C) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (!(cin >> m)) return 0;

    vector<int> A(m), B(m), C(m);
    for (int i = 0; i < m; i++) {
        cin >> A[i] >> B[i] >> C[i];
    }

    Solution sol;
    vector<pair<double, double>> res = sol.halfPlaneIntersection(m, A, B, C);

    if (res.empty()) {
        cout << "EMPTY\n";
    } else {
        cout << res.size() << "\n";
        cout << fixed << setprecision(6);
        for (const auto& p : res) {
            double x = (abs(p.first) < 1e-9) ? 0.0 : p.first;
            double y = (abs(p.second) < 1e-9) ? 0.0 : p.second;
            cout << x << " " << y << "\n";
        }
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(A, B, C) {
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
    const m = nextInt();
    const A = [], B = [], C = [];
    for (let i = 0; i < m; i++) {
        A.push(nextInt());
        B.push(nextInt());
        C.push(nextInt());
    }
    const sol = new Solution();
    const res = sol.solve(A, B, C);
    if (res.length === 0) {
        console.log("EMPTY");
    } else {
        console.log(res.length);
        for (let p of res) {
            const px = Math.abs(p.x) < 1e-9 ? 0.0 : p.x;
            const py = Math.abs(p.y) < 1e-9 ? 0.0 : p.y;
            console.log(`${px.toFixed(6)} ${py.toFixed(6)}`);
        }
    }
});
```
