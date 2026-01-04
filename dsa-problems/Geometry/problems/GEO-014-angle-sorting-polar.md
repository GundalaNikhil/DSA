---
problem_id: GEO_ANGLE_SORTING_POLAR__2841
display_id: GEO-014
slug: angle-sorting-polar
title: "Angle Sorting for Polar Order"
difficulty: Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Sorting
tags:
  - geometry
  - sorting
  - polar-angle
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-014: Angle Sorting for Polar Order

## Problem Statement

Given `n` points (distinct, no point at the origin), sort them by polar angle around the origin (0,0), in counterclockwise order. If two points have the same angle, the closer one (smaller distance to origin) should come first.

Output the points in the required order.

## ASCII Visual

```
   y
   ↑     ● (1,1)
   |  ● (1,0)   ● (0,1)
   |
   O------------→ x
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- `n` lines, each `x y` in the sorted order

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- No point is at the origin; points are distinct

## Example

**Input:**

```
3
1 0
1 1
0 1
```

**Output:**

```
1 0
1 1
0 1
```

**Explanation:**

Angles: (1,0) at 0°, (1,1) at 45°, (0,1) at 90°.

## Notes

- Use half-plane partition (upper vs lower) then cross product to sort without `atan2` for performance and stability.
- Tie-break by radius when cross product is zero.

## Related Topics

Sorting by Angle, Cross Product, Polar Coordinates

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int[][] sortPoints(int n, int[][] points) {
        // Implement here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        int n = Integer.parseInt(line.trim());

        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            line = br.readLine();
            String[] parts = line.trim().split("\\s+");
            points[i][0] = Integer.parseInt(parts[0]);
            points[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        int[][] result = sol.sortPoints(n, points);

        for (int[] p : result) {
            System.out.println(p[0] + " " + p[1]);
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def sort_points(self, n, points):
        # Implement here
        return []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        points = []
        for _ in range(n):
            x = int(next(iterator))
            y = int(next(iterator))
            points.append([x, y])
    except StopIteration:
        pass

    sol = Solution()
    result = sol.sort_points(n, points)

    for p in result:
        print(f"{p[0]} {p[1]}")

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
    vector<vector<int>> sortPoints(int n, vector<vector<int>>& points) {
        // Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> points(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> points[i][0] >> points[i][1];
    }

    Solution sol;
    vector<vector<int>> result = sol.sortPoints(n, points);

    for (const auto& p : result) {
        cout << p[0] << " " << p[1] << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  sortPoints(n, points) {
    // Implement here
    return [];
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const points = [];
  for (let i = 0; i < n; i++) {
    const x = readInt();
    const y = readInt();
    points.push([x, y]);
  }

  const sol = new Solution();
  const result = sol.sortPoints(n, points);

  result.forEach((p) => console.log(p[0] + " " + p[1]));
}

solve();
```

### Python

### C++

### JavaScript
