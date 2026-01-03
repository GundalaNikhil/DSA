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
import java.io.*;
import java.util.*;

class Solution {
    public double distancePointSegment(long x1, long y1, long x2, long y2, long px, long py) {
        //Implemention here
        return 0.0;
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
        if (data.length < 6) return;
        int idx = 0;
        long x1 = Long.parseLong(data[idx++]);
        long y1 = Long.parseLong(data[idx++]);
        long x2 = Long.parseLong(data[idx++]);
        long y2 = Long.parseLong(data[idx++]);
        long px = Long.parseLong(data[idx++]);
        long py = Long.parseLong(data[idx++]);

        Solution solution = new Solution();
        double result = solution.distancePointSegment(x1, y1, x2, y2, px, py);
        System.out.print(String.format(Locale.US, "%.6f", result));
    }
}
```

### Python

```python
import sys

def distance_point_segment(x1, y1, x2, y2, px, py):
    # //Implemention here
    return 0.0

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 6:
        return
    x1, y1, x2, y2, px, py = map(int, data[:6])
    result = distance_point_segment(x1, y1, x2, y2, px, py)
    sys.stdout.write(f"{result:.6f}")

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

double distance_point_segment(long long x1, long long y1, long long x2, long long y2,
                              long long px, long long py) {
    //Implemention here
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x1, y1, x2, y2, px, py;
    if (!(cin >> x1 >> y1 >> x2 >> y2 >> px >> py)) return 0;

    double result = distance_point_segment(x1, y1, x2, y2, px, py);
    cout << fixed << setprecision(6) << result;
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function distancePointSegment(x1, y1, x2, y2, px, py) {
  //Implemention here
  return 0.0;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
if (data.length < 6) {
  process.exit(0);
}
let idx = 0;
const x1 = data[idx++];
const y1 = data[idx++];
const x2 = data[idx++];
const y2 = data[idx++];
const px = data[idx++];
const py = data[idx++];

const result = distancePointSegment(x1, y1, x2, y2, px, py);
process.stdout.write(result.toFixed(6));
```

