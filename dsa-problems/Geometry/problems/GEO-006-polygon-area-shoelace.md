---
problem_id: GEO_POLYGON_AREA_SHOELACE__7719
display_id: GEO-006
slug: polygon-area-shoelace
title: "Polygon Area (Shoelace)"
difficulty: Medium
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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539585/dsa/geometry/qvhkvfxbr2mo5fi2tyht.jpg)

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
import java.util.*;
import java.io.*;

class Solution {
    public long getAbsoluteArea(int n, long[][] vertices) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nLine = br.readLine();
        if (nLine == null) return;
        int n = Integer.parseInt(nLine.trim());

        long[][] vertices = new long[n][2];
        for (int i = 0; i < n; i++) {
            String[] v = br.readLine().trim().split("\\s+");
            vertices[i][0] = Long.parseLong(v[0]);
            vertices[i][1] = Long.parseLong(v[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.getAbsoluteArea(n, vertices));
    }
}
```

### Python

```python
import sys

class Solution:
    def get_absolute_area(self, n, vertices):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1
    vertices = []
    for _ in range(n):
        vertices.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2

    sol = Solution()
    print(sol.get_absolute_area(n, vertices))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    long long getAbsoluteArea(int n, vector<pair<long long, long long>>& vertices) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> vertices(n);
    for (int i = 0; i < n; i++) {
        cin >> vertices[i].first >> vertices[i].second;
    }

    Solution sol;
    cout << sol.getAbsoluteArea(n, vertices) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getAbsoluteArea(n, vertices) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const n = parseInt(input[idx++]);
  const vertices = [];
  for (let i = 0; i < n; i++) {
    vertices.push([BigInt(input[idx++]), BigInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.getAbsoluteArea(n, vertices).toString());
}

solve();
```
