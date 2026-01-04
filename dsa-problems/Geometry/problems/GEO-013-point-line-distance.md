---
problem_id: GEO_POINT_LINE_DISTANCE__6402
display_id: GEO-013
slug: point-line-distance
title: "Point-Line Distance"
difficulty: Easy
difficulty_score: 35
topics:
  - Computational Geometry
  - Distance
tags:
  - geometry
  - distance
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-013: Point-Line Distance

## Problem Statement

Given a line segment `AB` with endpoints `A(x1, y1)` and `B(x2, y2)` and a point `P(px, py)`, compute the shortest distance from `P` to the segment.

Print the distance as a floating-point number rounded to 6 decimals.

## ASCII Visual

```
A ●------------------● B
         |
         | shortest
         |
         ● P
```

## Input Format

- Single line: six integers `x1 y1 x2 y2 px py`

## Output Format

- Single floating number: minimum distance from `P` to segment `AB`, rounded to 6 decimals

## Constraints

- `-10^9 <= coordinates <= 10^9`
- `A` and `B` are distinct

## Example

**Input:**

```
0 0 2 0 1 1
```

**Output:**

```
1.000000
```

**Explanation:**

Segment lies on x-axis; perpendicular from `P` meets segment at `(1,0)`, distance 1.

## Notes

- Project `P` onto the line; if projection lies outside the segment, take distance to nearest endpoint.
- Use doubles; avoid overflow by using 64-bit intermediates.

## Related Topics

Distance Computation, Vector Projection

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public double pointLineDistance(double x1, double y1, double x2, double y2, double px, double py) {
        // Implement here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        double x1 = Double.parseDouble(parts[0]);
        double y1 = Double.parseDouble(parts[1]);
        double x2 = Double.parseDouble(parts[2]);
        double y2 = Double.parseDouble(parts[3]);
        double px = Double.parseDouble(parts[4]);
        double py = Double.parseDouble(parts[5]);

        Solution sol = new Solution();
        System.out.printf("%.6f%n", sol.pointLineDistance(x1, y1, x2, y2, px, py));
    }
}
```

### Python

```python
import sys

class Solution:
    def point_line_distance(self, x1, y1, x2, y2, px, py):
        # Implement here
        return 0.0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        x1 = float(next(iterator))
        y1 = float(next(iterator))
        x2 = float(next(iterator))
        y2 = float(next(iterator))
        px = float(next(iterator))
        py = float(next(iterator))

    except StopIteration:
        pass

    sol = Solution()
    print(f"{sol.point_line_distance(x1, y1, x2, y2, px, py):.6f}")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    double pointLineDistance(double x1, double y1, double x2, double y2, double px, double py) {
        // Implement here
        return 0.0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double x1, y1, x2, y2, px, py;
    if (!(cin >> x1 >> y1 >> x2 >> y2 >> px >> py)) return 0;

    Solution sol;
    cout << fixed << setprecision(6) << sol.pointLineDistance(x1, y1, x2, y2, px, py) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  pointLineDistance(x1, y1, x2, y2, px, py) {
    // Implement here
    return 0.0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 6) return;

  let idx = 0;
  function readString() {
    return input[idx++];
  }
  function readFloat() {
    return parseFloat(readString());
  }

  const x1 = readFloat();
  const y1 = readFloat();
  const x2 = readFloat();
  const y2 = readFloat();
  const px = readFloat();
  const py = readFloat();

  const sol = new Solution();
  console.log(sol.pointLineDistance(x1, y1, x2, y2, px, py).toFixed(6));
}

solve();
```

### Python

### C++

### JavaScript
