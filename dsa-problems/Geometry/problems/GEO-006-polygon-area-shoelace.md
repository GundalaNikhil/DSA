---
problem_id: GEO_POLYGON_AREA_SHOELACE__7719
display_id: GEO-006
slug: polygon-area-shoelace
title: "Polygon Area (Shoelace)"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Polygon
  - Shoelace Formula
tags:
  - geometry
  - area
  - shoelace
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-006: Polygon Area (Shoelace)

## Problem Statement

Given a simple polygon with `n` vertices listed in order (clockwise or counterclockwise), compute its **signed area**. Output the absolute area.

Use the shoelace formula; avoid floating point by working in twice-the-area and dividing at the end if needed.

## Emoji Visual

```
⬛ Square:
🟢 (0,0) ---- 🟢 (2,0)
|               |
|               |
🟢 (0,2) ---- 🟢 (2,2)
Area = 4
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi` for each vertex, in order

## Output Format

- Single integer: absolute area of the polygon

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- Polygon is simple (non-self-intersecting)

## Example

**Input:**
```
4
0 0
2 0
2 2
0 2
```

**Output:**
```
4
```

**Explanation:**

Axis-aligned square of side 2 has area 4.

## Notes

- Signed area from the shoelace sum may be negative if the order is clockwise; take `abs`.
- Twice-the-area fits in 128-bit; store in 64-bit carefully (`~2e18`).

## Related Topics

Polygon Geometry, Shoelace Formula, Cross Product

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long polygonArea(long[] xs, long[] ys) {
        //Implemention here
        return 0L;
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
        long result = solution.polygonArea(xs, ys);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def polygon_area(xs, ys):
    # //Implemention here
    return 0

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
    result = polygon_area(xs, ys)
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

long long polygon_area(const vector<long long>& xs, const vector<long long>& ys) {
    //Implemention here
    return 0LL;
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

    cout << polygon_area(xs, ys);
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function polygonArea(xs, ys) {
  //Implemention here
  return 0;
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

const result = polygonArea(xs, ys);
process.stdout.write(String(result));
```

