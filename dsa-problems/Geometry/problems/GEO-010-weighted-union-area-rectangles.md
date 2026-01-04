---
problem_id: GEO_WEIGHTED_UNION_AREA__5312
display_id: GEO-010
slug: weighted-union-area-rectangles
title: "Line Sweep Weighted Union Area"
difficulty: Medium
difficulty_score: 70
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
tags:
  - geometry
  - sweep-line
  - rectangles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-010: Line Sweep Weighted Union Area

## Problem Statement

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539588/dsa/geometry/sqvamg6caov7nny1qcek.jpg)

You are given `m` axis-aligned rectangles. Each rectangle `i` has integer weight `w[i]` (can be negative or positive). Given a threshold `W`, compute the total area of all points covered by rectangles whose **cumulative weight is at least `W`**.

Return that area as an integer.

## ASCII Visual

```
Rect A (w=1): (0,0)-(2,2)
Rect B (w=2): (1,1)-(3,3)

Overlap area (weight sum = 3) = 1x1 = 1
Total area where weight >= 2 is 4 (overlap 1 + B-only region 3)
```

## Input Format

- First line: integers `m` and `W`
- Next `m` lines: five integers `x1 y1 x2 y2 w` (`x1 < x2`, `y1 < y2`)

## Output Format

- Single integer: area of regions where cumulative weight >= `W`

## Constraints

- `1 <= m <= 100000`
- `|w[i]| <= 10^6`
- `1 <= W <= 10^6`
- `-10^9 <= x1 < x2 <= 10^9`
- `-10^9 <= y1 < y2 <= 10^9`

## Example

**Input:**

```
2 2
0 0 2 2 1
1 1 3 3 2
```

**Output:**

```
4
```

**Explanation:**

Weight-sum >= 2 region consists of overlap (1 area) plus B-only region (3 area).

## Notes

- Use sweep over x with events at rectangle edges; segment tree over y to maintain length where sum >= W.
- Coordinate compress y to handle large coords.
- Area accumulation: delta_x \* covered_y_length.

## Related Topics

Sweep Line, Segment Tree, Coordinate Compression

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long getWeightedUnionArea(int m, int W, long[][] rects) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        String[] parts = firstLine.trim().split("\\s+");
        int m = Integer.parseInt(parts[0]);
        int W = Integer.parseInt(parts[1]);

        long[][] rects = new long[m][5];
        for (int i = 0; i < m; i++) {
            String[] r = br.readLine().trim().split("\\s+");
            rects[i][0] = Long.parseLong(r[0]);
            rects[i][1] = Long.parseLong(r[1]);
            rects[i][2] = Long.parseLong(r[2]);
            rects[i][3] = Long.parseLong(r[3]);
            rects[i][4] = Long.parseLong(r[4]);
        }

        Solution sol = new Solution();
        System.out.println(sol.getWeightedUnionArea(m, W, rects));
    }
}
```

### Python

```python
import sys

class Solution:
    def get_weighted_union_area(self, m, W, rects):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    W = int(input_data[1])
    idx = 2
    rects = []
    for _ in range(m):
        rects.append(list(map(int, input_data[idx:idx+5])))
        idx += 5

    sol = Solution()
    print(sol.get_weighted_union_area(m, W, rects))

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
    long long getWeightedUnionArea(int m, int W, vector<vector<long long>>& rects) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m, W;
    if (!(cin >> m >> W)) return 0;

    vector<vector<long long>> rects(m, vector<long long>(5));
    for (int i = 0; i < m; i++) {
        cin >> rects[i][0] >> rects[i][1] >> rects[i][2] >> rects[i][3] >> rects[i][4];
    }

    Solution sol;
    cout << sol.getWeightedUnionArea(m, W, rects) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getWeightedUnionArea(m, W, rects) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const m = parseInt(input[idx++]);
  const W = parseInt(input[idx++]);
  const rects = [];
  for (let i = 0; i < m; i++) {
    rects.push([
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  console.log(sol.getWeightedUnionArea(m, W, rects).toString());
}

solve();
```
