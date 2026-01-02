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
    public List<long[]> cappedHull(long[] xs, long[] ys, int theta) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        try {
            if (!sc.hasNext()) return;
            int n = sc.nextInt();
            long[] xs = new long[n];
            long[] ys = new long[n];
            for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
            int theta = sc.nextInt();
            List<long[]> res = new Solution().cappedHull(xs, ys, theta);
            System.out.println(res.size());
            for(long[] p : res) System.out.println(p[0] + " " + p[1]);
        } finally {
            sc.close();
        }
    }
}
```

### Python

```python
from typing import List
import math

def capped_hull(xs: List[int], ys: List[int], theta: int) -> List:
    # Implementation here
    return []

def main():
    import sys
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
        theta = next(it)
        res = capped_hull(xs, ys, theta)
        print(len(res))
        for p in res:
            print(p[0], p[1])
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

using namespace std;

class Solution {
public:
    vector<pair<long long, long long>> cappedHull(const vector<long long>& xs, const vector<long long>& ys, int theta) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i];
    }

    int theta;
    if (!(cin >> theta)) return 0;

    Solution sol;
    vector<pair<long long, long long>> res = sol.cappedHull(xs, ys, theta);
    cout << res.size() << "\n";
    for (const auto& p : res) {
        cout << p.first << " " << p.second << "\n";
    }

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(xs, ys, theta) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => next(); 

    let n = parseInt(nextInt());
    let xs = [], ys = [];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }
    let theta = parseInt(nextInt());

    const sol = new Solution();
    const res = sol.solve(xs, ys, theta);
    
    if (res.length === 0) console.log(0);
    else {
        console.log(res.length);
        for(let p of res) console.log(`${p.x} ${p.y}`);
    }
});
```
