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
import java.io.*;
import java.util.*;

class Solution {
    public String classifyPoint(long[] xs, long[] ys, long qx, long qy) {
        //Implemention here
        return "";
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
        if (data.length == 0) return;
        int n = Integer.parseInt(data[idx++]);
        if (data.length < 1 + 2 * n + 2) return;
        long[] xs = new long[n];
        long[] ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = Long.parseLong(data[idx++]);
            ys[i] = Long.parseLong(data[idx++]);
        }
        long qx = Long.parseLong(data[idx++]);
        long qy = Long.parseLong(data[idx++]);

        Solution solution = new Solution();
        String result = solution.classifyPoint(xs, ys, qx, qy);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def classify_point(xs, ys, qx, qy):
    # //Implemention here
    return ""

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]);
    idx += 1
    if len(data) < 1 + 2 * n + 2:
        return
    xs = []
    ys = []
    for _ in range(n):
        xs.append(int(data[idx]));
        ys.append(int(data[idx + 1]));
        idx += 2
    qx = int(data[idx]);
    qy = int(data[idx + 1]);
    result = classify_point(xs, ys, qx, qy)
    sys.stdout.write(str(result))

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

string classify_point(const vector<long long>& xs, const vector<long long>& ys, long long qx, long long qy) {
    //Implemention here
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<long long> data;
    long long val;
    while (cin >> val) {
        data.push_back(val);
    }
    if (data.empty()) return 0;
    size_t idx = 0;
    long long n = data[idx++];
    if (data.size() < 1 + 2 * n + 2) return 0;
    vector<long long> xs(n), ys(n);
    for (long long i = 0; i < n; i++) {
        xs[i] = data[idx++];
        ys[i] = data[idx++];
    }
    long long qx = data[idx++];
    long long qy = data[idx++];

    cout << classify_point(xs, ys, qx, qy);
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function classifyPoint(xs, ys, qx, qy) {
  //Implemention here
  return "";
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
const n = data[idx++];
if (!Number.isFinite(n) || data.length < 1 + 2 * n + 2) {
  process.exit(0);
}
const xs = [];
const ys = [];
for (let i = 0; i < n; i++) {
  xs.push(data[idx++]);
  ys.push(data[idx++]);
}
const qx = data[idx++];
const qy = data[idx++];

const result = classifyPoint(xs, ys, qx, qy);
process.stdout.write(String(result));
```

