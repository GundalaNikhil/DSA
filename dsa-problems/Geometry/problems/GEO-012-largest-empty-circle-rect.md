---
problem_id: GEO_LARGEST_EMPTY_CIRCLE__9186
display_id: GEO-012
slug: largest-empty-circle-rect
title: "Largest Empty Circle Inside Rectangle"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Voronoi
  - Circles
tags:
  - geometry
  - circle
  - voronoi
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-012: Largest Empty Circle Inside Rectangle

## Problem Statement

Given a set of points inside an axis-aligned rectangle `[xL, yB]` to `[xR, yT]`, find the largest possible circle that:

- Lies fully inside the rectangle, and
- Does not contain any point strictly inside it (points on the boundary are allowed).

Output the maximum possible radius (floating-point, 6 decimals).

## ASCII Visual

```
Rect: (0,0) to (4,4)
Points: (1,1), (3,1)

Largest empty circle:
center (2,3), radius 1.0
```

## Input Format

- First line: five integers `xL yB xR yT n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single floating number: maximum radius (rounded to 6 decimals)

## Constraints

- `-10^9 <= xL < xR <= 10^9`
- `-10^9 <= yB < yT <= 10^9`
- `0 <= n <= 2000`
- All points lie inside or on the rectangle

## Example

**Input:**
```
0 0 4 4 2
1 1
3 1
```

**Output:**
```
1.000000
```

**Explanation:**

Center at `(2,3)` touches top edge and is distance 1 from the nearest point; no larger circle fits.

## Notes

- Optimal centers occur at: a point-to-point bisector intersection, a point-to-edge bisector, or rectangle corners/edges.
- Enumerate candidate centers: rectangle edges constrained by each point, circumcenters of point pairs/triples within the rectangle.
- With `n <= 2000`, `O(n^3)` is acceptable.

## Related Topics

Circle Geometry, Voronoi Diagrams, Closest Point

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public double largestEmptyCircle(int xL, int yB, int xR, int yT, int[] xs, int[] ys) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int xL = sc.nextInt(), yB = sc.nextInt(), xR = sc.nextInt(), yT = sc.nextInt();
        int n = sc.nextInt();
        int[] xs = new int[n], ys = new int[n];
        for (int i = 0; i < n; i++) { xs[i] = sc.nextInt(); ys[i] = sc.nextInt(); }
        Solution sol = new Solution();
        double r = sol.largestEmptyCircle(xL, yB, xR, yT, xs, ys);
        System.out.printf("%.6f%n", r);
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def largest_empty_circle(xL: int, yB: int, xR: int, yT: int, xs: List[int], ys: List[int]) -> float:
    # Your implementation here
    return 0.0

def main() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    xL, yB, xR, yT, n = map(int, [next(it), next(it), next(it), next(it), next(it)])
    xs = []; ys = []
    for _ in range(n):
        xs.append(int(next(it))); ys.append(int(next(it)))
    r = largest_empty_circle(xL, yB, xR, yT, xs, ys)
    print(f"{r:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

double largestEmptyCircle(long long xL, long long yB, long long xR, long long yT,
                          const vector<long long>& xs, const vector<long long>& ys) {
    // Your implementation here
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long xL, yB, xR, yT;
    if (!(cin >> xL >> yB >> xR >> yT)) return 0;
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    cout.setf(ios::fixed); cout << setprecision(6);
    cout << largestEmptyCircle(xL, yB, xR, yT, xs, ys) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function largestEmptyCircle(xL, yB, xR, yT, xs, ys) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const xL = data[idx++], yB = data[idx++], xR = data[idx++], yT = data[idx++], n = data[idx++];
  const xs = [], ys = [];
  for (let i = 0; i < n; i++) { xs.push(data[idx++]); ys.push(data[idx++]); }
  const r = largestEmptyCircle(xL, yB, xR, yT, xs, ys);
  console.log(r.toFixed(6));
}

main();
```
