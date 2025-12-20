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

class Solution {
    public long diameterSquared(int[] xs, int[] ys) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] xs = new int[n], ys = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = sc.nextInt();
            ys[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.diameterSquared(xs, ys));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def diameter_squared(xs: List[int], ys: List[int]) -> int:
    # Your implementation here
    return 0

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    xs, ys = [], []
    for _ in range(n):
        xs.append(next(it)); ys.append(next(it))
    print(diameter_squared(xs, ys))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long diameterSquared(const vector<long long>& xs, const vector<long long>& ys) {
    // Your implementation here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    cout << diameterSquared(xs, ys) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function diameterSquared(xs, ys) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const n = data[idx++];
  const xs = new Array(n), ys = new Array(n);
  for (let i = 0; i < n; i++) { xs[i] = data[idx++]; ys[i] = data[idx++]; }
  console.log(diameterSquared(xs, ys));
}

main();
```
