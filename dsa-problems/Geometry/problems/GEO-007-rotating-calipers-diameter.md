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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539586/dsa/geometry/zs3qtdzwqnfgqb4tz1ew.jpg)

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
    public long findMaxSquaredDiameter(int n, long[][] vertices) {
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
        System.out.println(sol.findMaxSquaredDiameter(n, vertices));
    }
}
```

### Python

```python
import sys

class Solution:
    def find_max_squared_diameter(self, n, vertices):
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
    print(sol.find_max_squared_diameter(n, vertices))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long findMaxSquaredDiameter(int n, vector<pair<long long, long long>>& vertices) {
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
    cout << sol.findMaxSquaredDiameter(n, vertices) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findMaxSquaredDiameter(n, vertices) {
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
  console.log(sol.findMaxSquaredDiameter(n, vertices).toString());
}

solve();
```
