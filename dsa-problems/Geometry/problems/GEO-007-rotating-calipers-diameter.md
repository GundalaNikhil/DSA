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

class Solution {
    public long diameterSquared(long[] xs, long[] ys) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().diameterSquared(xs, ys));
        sc.close();
    }
}
```

### Python

```python
def diameter_squared(xs: list, ys: list) -> int:
    # Implementation here
    return 0

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

using namespace std;

class Solution {
public:
    long long diameterSquared(const vector<long long>& xs, const vector<long long>& ys) {
        // Implementation here
        return {};
    }
};

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
const readline = require("readline");

class Solution {
  solve(xs, ys) {
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
    const n = nextInt();
    const xs = [], ys = [];
    for (let i = 0; i < n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }
    const sol = new Solution();
    console.log(sol.solve(xs, ys));
});
```
