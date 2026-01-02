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
    public double distancePointSegment(long x1, long y1, long x2, long y2, long px, long py) {
        // Implementation here
        return 0.0;
    }
}

class Main {
static class Solution {
    public double distancePointSegment(long x1, long y1, long x2, long y2, long px, long py) {
        long ux = x2 - x1, uy = y2 - y1;
        long vx = px - x1, vy = py - y1;
        long denom = ux*ux + uy*uy;
        if (denom == 0) return Math.hypot(vx, vy);
        double t = (ux * (double)vx + uy * (double)vy) / denom;
        t = Math.max(0.0, Math.min(1.0, t));
        double cx = x1 + t * ux;
        double cy = y1 + t * uy;
        return Math.hypot(px - cx, py - cy);
    }
}
```

### Python

```
// No template available
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double distancePointSegment(long long x1, long long y1, long long x2, long long y2, long long px, long long py) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    long long x1, y1, x2, y2, px, py; cin >> x1 >> y1 >> x2 >> y2 >> px >> py;
    cout << fixed << setprecision(6) << distancePointSegment(x1, y1, x2, y2, px, py) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  distancePointSegment(x1, y1, x2, y2, px, py) {
    // Implementation here
    return null;
  }
}

const readline = require('readline');

function new Solution().distancePointSegment(x1, y1, x2, y2, px, py) {
  const ux = x2 - x1, uy = y2 - y1;
  const vx = px - x1, vy = py - y1;
  const denom = ux*ux + uy*uy;
  if (denom === 0) return Math.hypot(vx, vy);
  let t = (ux*vx + uy*vy) / denom;
  t = Math.max(0, Math.min(1, t));
  const cx = x1 + t * ux;
  const cy = y1 + t * uy;
  return Math.hypot(px - cx, py - cy);
}


const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    const nextFloat = () => parseFloat(next());
    console.log(new Solution().distancePointSegment(nextInt(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt()).toFixed(6));
});
```
