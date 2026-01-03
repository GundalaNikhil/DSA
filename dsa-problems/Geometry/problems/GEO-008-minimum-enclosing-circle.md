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
import java.io.*;
import java.util.*;

class Solution {
    public double[] minEnclosingCircle(long[] xs, long[] ys) {
        //Implemention here
        return new double[] {0.0, 0.0, 0.0};
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append(' ');
        }
        String input = sb.toString().trim();
        if (input.isEmpty()) return;
        String[] data = input.split("\\s+");
        int idx = 0;
        int n = Integer.parseInt(data[idx++]);
        if (data.length < 1 + 2 * n) return;
        long[] xs = new long[n];
        long[] ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Long.parseLong(data[idx++]);
            ys[i] = Long.parseLong(data[idx++]);
        }

        Solution solution = new Solution();
        double[] result = solution.minEnclosingCircle(xs, ys);
        String out = String.format(Locale.US, "%.6f\n%.6f\n%.6f", result[0], result[1], result[2]);
        System.out.print(out);
    }
}
```

### Python

```python
import sys

def min_enclosing_circle(xs, ys):
    # //Implemention here
    return (0.0, 0.0, 0.0)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]);
    idx += 1
    if len(data) < 1 + 2 * n:
        return
    xs = []
    ys = []
    for _ in range(n):
        xs.append(int(data[idx]));
        ys.append(int(data[idx + 1]));
        idx += 2
    cx, cy, r = min_enclosing_circle(xs, ys)
    sys.stdout.write(f"{cx:.6f}\n{cy:.6f}\n{r:.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

vector<double> min_enclosing_circle(const vector<long long>& xs, const vector<long long>& ys) {
    //Implemention here
    return {0.0, 0.0, 0.0};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (long long i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i];
    }

    vector<double> result = min_enclosing_circle(xs, ys);
    if (result.size() < 3) return 0;
    cout << fixed << setprecision(6);
    cout << result[0] << "\n" << result[1] << "\n" << result[2];
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function minEnclosingCircle(xs, ys) {
  //Implemention here
  return [0.0, 0.0, 0.0];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
const n = data[idx++];
if (!Number.isFinite(n) || data.length < 1 + 2 * n) {
  process.exit(0);
}
const xs = [];
const ys = [];
for (let i = 0; i < n; i++) {
  xs.push(data[idx++]);
  ys.push(data[idx++]);
}

const result = minEnclosingCircle(xs, ys);
const cx = result[0] ?? 0;
const cy = result[1] ?? 0;
const r = result[2] ?? 0;
process.stdout.write(cx.toFixed(6) + "\n" + cy.toFixed(6) + "\n" + r.toFixed(6));
```

