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

class Main {

static class Solution {
    private boolean onSegment(long xi, long yi, long xj, long yj, long qx, long qy) {
        return false;
    }

    public String pointInPolygon(long[] xs, long[] ys, long qx, long qy) {
        return "";
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        long qx = sc.nextLong(); long qy = sc.nextLong();
        System.out.println(new Solution().pointInPolygon(xs, ys, qx, qy));
    }
}
```

### Python

```python
from typing import List

def classify_point(xs: List[int], ys: List[int], qx: int, qy: int) -> str:
    return ""
def main() -> None:
    import sys
    # Read all tokens at once to handle newlines/spaces robustly
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        n = next(it)
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
        qx = next(it)
        qy = next(it)
        print(classify_point(xs, ys, qx, qy))
    except StopIteration:
        return

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

using namespace std;

string classifyPoint(const vector<long long>& xs, const vector<long long>& ys, long long qx, long long qy) {
    int n = xs.size();
    int wn = 0;
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        long long xi = xs[i], yi = ys[i], xj = xs[j], yj = ys[j];
        long long cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi);
        if (cross == 0 && min(xi, xj) <= qx && qx <= max(xi, xj) && min(yi, yj) <= qy && qy <= max(yi, yj))
            return "boundary";
        if (yi <= qy && yj > qy && cross > 0) wn++;
        else if (yi > qy && yj <= qy && cross < 0) wn--;
    }
    return wn != 0 ? "inside" : "outside";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    long long qx, qy; cin >> qx >> qy;
    cout << classifyPoint(xs, ys, qx, qy) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

function classifyPoint(xs, ys, qx, qy) {
    return 0;
  }

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    const nextFloat = () => parseFloat(next());
    let n = nextInt();
    let xs = [], ys = [];
    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }
    console.log(classifyPoint(xs, ys, nextInt(), nextInt()));
});
```

