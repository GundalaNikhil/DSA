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

class Solution {
    public double[] minEnclosingCircle(int[] xs, int[] ys) {
        // Your implementation here
        return new double[]{0.0, 0.0, 0.0};
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
        double[] res = sol.minEnclosingCircle(xs, ys);
        System.out.printf(\"%.6f %.6f %.6f%n\", res[0], res[1], res[2]);
        sc.close();
    }
}
```

### Python

```python
from typing import List, Tuple

def min_enclosing_circle(xs: List[int], ys: List[int]) -> Tuple[float, float, float]:
    # Your implementation here
    return (0.0, 0.0, 0.0)

def main() -> None:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    xs, ys = [], []
    for _ in range(n):
        xs.append(int(next(it))); ys.append(int(next(it)))
    cx, cy, r = min_enclosing_circle(xs, ys)
    print(f\"{cx:.6f} {cy:.6f} {r:.6f}\")

if __name__ == \"__main__\":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

tuple<double,double,double> minEnclosingCircle(const vector<long long>& xs, const vector<long long>& ys) {
    // Your implementation here
    return {0.0, 0.0, 0.0};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    auto [cx, cy, r] = minEnclosingCircle(xs, ys);
    cout.setf(ios::fixed); cout << setprecision(6);
    cout << cx << \" \" << cy << \" \" << r << \"\\n\";
    return 0;
}
```

### JavaScript

```javascript
const fs = require(\"fs\");

function minEnclosingCircle(xs, ys) {
  // Your implementation here
  return [0, 0, 0];
}

function main() {
  const data = fs.readFileSync(0, \"utf8\").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const n = data[idx++];
  const xs = new Array(n), ys = new Array(n);
  for (let i = 0; i < n; i++) { xs[i] = data[idx++]; ys[i] = data[idx++]; }
  const [cx, cy, r] = minEnclosingCircle(xs, ys);
  console.log(`${cx.toFixed(6)} ${cy.toFixed(6)} ${r.toFixed(6)}`);
}

main();
```
