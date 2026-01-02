---
problem_id: GEO_MIN_ENCLOSING_CIRCLE__4205
display_id: GEO-008
slug: minimum-enclosing-circle
title: "Minimum Enclosing Circle"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Randomized Algorithms
  - Circle
tags:
  - geometry
  - circle
  - randomized
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-008: Minimum Enclosing Circle

## Problem Statement

Given `n` points in 2D, find the smallest circle that encloses all the points. Output the center coordinates and the radius.

Return `cx cy r` with values rounded to 6 decimal places.

## ASCII Visual

```
Points:
● (0,0)   ● (1,0)
     ● (0,1)

Smallest enclosing circle:
center (0.5, 0.5), radius ≈ 0.707107
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single line: three floating values `cx cy r` (rounded to 6 decimals)

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**
```
3
0 0
1 0
0 1
```

**Output:**
```
0.500000 0.500000 0.707107
```

**Explanation:**

The circle centered at `(0.5, 0.5)` with radius `sqrt(0.5)` encloses all three points.

## Notes

- Use a randomized incremental algorithm (Welzl) for expected `O(n)`.
- Beware of precision; store as doubles, output rounded to 6 decimals.
- With one point, radius is 0 and center is that point.

## Related Topics

Circle Geometry, Randomized Algorithms

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public double[] minEnclosingCircle(long[] xs, long[] ys) {
        // Implementation here
        return new double[0];
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
        double[] res = new Solution().minEnclosingCircle(xs, ys);
        double cx = Math.abs(res[0]) < 1e-9 ? 0.0 : res[0];
        double cy = Math.abs(res[1]) < 1e-9 ? 0.0 : res[1];
        double r = Math.abs(res[2]) < 1e-9 ? 0.0 : res[2];
        System.out.printf("%.6f\n%.6f\n%.6f\n", cx, cy, r);
        sc.close();
    }
}
```

### Python

```python
def min_enclosing_circle(xs: list, ys: list) -> list:
    # Implementation here
    return [0.0, 0.0, 0.0]

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
        res = min_enclosing_circle(xs, ys)
        cx = 0.0 if abs(res[0]) < 1e-9 else res[0]
        cy = 0.0 if abs(res[1]) < 1e-9 else res[1]
        r = 0.0 if abs(res[2]) < 1e-9 else res[2]
        print(f"{cx:.6f}")
        print(f"{cy:.6f}")
        print(f"{r:.6f}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    vector<double> minEnclosingCircle(const vector<long long>& xs, const vector<long long>& ys) {
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

    Solution sol;
    vector<double> res = sol.minEnclosingCircle(xs, ys);

    cout << fixed << setprecision(6);
    cout << res[0] << "\n" << res[1] << "\n" << res[2] << "\n";

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
    const res = sol.solve(xs, ys);
    console.log(res[0].toFixed(6));
    console.log(res[1].toFixed(6));
    console.log(res[2].toFixed(6));
});
```
