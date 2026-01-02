---
problem_id: GEO_ROTATING_CALIPERS_DIAM__3154
display_id: GEO-007
slug: rotating-calipers-diameter
title: "Rotating Calipers Diameter"
difficulty: Medium
difficulty_score: 55
topics:
  - Computational Geometry
  - Rotating Calipers
  - Convex Polygon
tags:
  - geometry
  - diameter
  - rotating-calipers
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-007: Rotating Calipers Diameter

## Problem Statement

You are given a **convex** polygon with `n` vertices in counterclockwise order. Find the maximum squared distance between any pair of its vertices (the squared diameter of the polygon).

Return that maximum squared distance as an integer.

## Emoji Visual

```
🟢 Square (0,0)-(1,0)-(1,1)-(0,1)
Fartherst pair are opposite corners:
🟢(0,0) ..... 🟢(1,1)   dist^2 = 2
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi` in CCW order

## Output Format

- Single integer: maximum squared distance between any two vertices

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- Polygon is convex and vertices are given in CCW order

## Example

**Input:**
```
4
0 0
1 0
1 1
0 1
```

**Output:**
```
2
```

**Explanation:**

Opposite corners `(0,0)` and `(1,1)` give the diameter squared `2`.

## Notes

- Work with squared distances to avoid square roots.
- Rotating calipers over antipodal pairs gives `O(n)` after one pass.
- For triangles, check all three edges and vertices with calipers logic.

## Related Topics

Rotating Calipers, Convex Geometry, Distance Computation

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Main {
static class Solution {
    private long cross(long ax, long ay, long bx, long by, long cx, long cy) {
        return 0;
    }
    private long dist2(long ax, long ay, long bx, long by) {
        return 0;
    }
    public long diameterSquared(long[] xs, long[] ys) {
        return 0;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().diameterSquared(xs, ys));
    }
}
```

### Python

```python
from typing import List, Tuple

def diameter_squared(xs: List[int], ys: List[int]) -> int:
    return 0
def main() -> None:
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
        print(diameter_squared(xs, ys))
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

long long diameterSquared(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    if (n <= 1) return 0;
    auto cross = [&](int a, int b, int c)->long long{
        return (xs[b]-xs[a])*(ys[c]-ys[a]) - (ys[b]-ys[a])*(xs[c]-xs[a]);
    };
    auto dist2 = [&](int a, int b)->long long{
        long long dx = xs[a]-xs[b], dy = ys[a]-ys[b];
        return dx*dx + dy*dy;
    };
    long long best = 0;
    int j = 1;
    for (int i = 0; i < n; ++i) {
        int ni = (i+1)%n;
        while (cross(i, ni, (j+1)%n) > cross(i, ni, j)) j = (j+1)%n;
        best = max(best, dist2(i, j));
        best = max(best, dist2(ni, j));
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    cout << diameterSquared(xs, ys) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    solve(xs, ys) {
    return 0;
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
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
```

