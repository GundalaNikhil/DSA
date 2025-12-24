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

class Solution {
    public String classifyPoint(int[] xs, int[] ys, long qx, long qy) {
        // Your implementation here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] xs = new int[n];
        int[] ys = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
        }
        long qx = sc.nextLong(), qy = sc.nextLong();
        Solution sol = new Solution();
        System.out.println(sol.classifyPoint(xs, ys, qx, qy));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def classify_point(xs: List[int], ys: List[int], qx: int, qy: int) -> str:
    # Your implementation here
    return ""

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    xs = []
    ys = []
    for _ in range(n):
        xs.append(next(it))
        ys.append(next(it))
    qx = next(it)
    qy = next(it)
    print(classify_point(xs, ys, qx, qy))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

string classifyPoint(const vector<long long>& xs, const vector<long long>& ys, long long qx, long long qy) {
    // Your implementation here
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    long long qx, qy;
    cin >> qx >> qy;
    cout << classifyPoint(xs, ys, qx, qy) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function classifyPoint(xs, ys, qx, qy) {
  // Your implementation here
  return "";
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const n = data[idx++];
  const xs = Array(n);
  const ys = Array(n);
  for (let i = 0; i < n; i++) {
    xs[i] = data[idx++];
    ys[i] = data[idx++];
  }
  const qx = data[idx++], qy = data[idx++];
  console.log(classifyPoint(xs, ys, qx, qy));
}

main();
```
