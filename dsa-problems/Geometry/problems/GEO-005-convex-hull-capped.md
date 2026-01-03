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
import java.io.*;
import java.util.*;

class Solution {
    public List<long[]> cappedHull(long[] xs, long[] ys, long theta) {
        //Implemention here
        return new ArrayList<>();
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
        if (data.length < 1 + 2 * n + 1) return;
        long[] xs = new long[n];
        long[] ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Long.parseLong(data[idx++]);
            ys[i] = Long.parseLong(data[idx++]);
        }
        long theta = Long.parseLong(data[idx++]);

        Solution solution = new Solution();
        List<long[]> result = solution.cappedHull(xs, ys, theta);
        StringBuilder out = new StringBuilder();
        out.append(result.size()).append('\n');
        for (long[] p : result) {
            out.append(p[0]).append(' ').append(p[1]).append('\n');
        }
        System.out.print(out.toString());
    }
}
```

### Python

```python
import sys

def capped_hull(xs, ys, theta):
    # //Implemention here
    return []

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]);
    idx += 1
    if len(data) < 1 + 2 * n + 1:
        return
    xs = []
    ys = []
    for _ in range(n):
        xs.append(int(data[idx]));
        ys.append(int(data[idx + 1]));
        idx += 2
    theta = int(data[idx]);
    result = capped_hull(xs, ys, theta)
    out_lines = [str(len(result))]
    for x, y in result:
        out_lines.append(f"{x} {y}")
    sys.stdout.write("\n".join(out_lines))

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

vector<pair<long long, long long>> capped_hull(const vector<long long>& xs, const vector<long long>& ys, long long theta) {
    //Implemention here
    return {};
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
    long long theta;
    cin >> theta;

    vector<pair<long long, long long>> result = capped_hull(xs, ys, theta);
    cout << result.size() << "\n";
    for (const auto& p : result) {
        cout << p.first << " " << p.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function cappedHull(xs, ys, theta) {
  //Implemention here
  return [];
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
const n = data[idx++];
if (!Number.isFinite(n) || data.length < 1 + 2 * n + 1) {
  process.exit(0);
}
const xs = [];
const ys = [];
for (let i = 0; i < n; i++) {
  xs.push(data[idx++]);
  ys.push(data[idx++]);
}
const theta = data[idx++];

const result = cappedHull(xs, ys, theta);
let out = [];
out.push(String(result.length));
for (const p of result) {
  out.push(p[0] + " " + p[1]);
}
process.stdout.write(out.join("\n"));
```

