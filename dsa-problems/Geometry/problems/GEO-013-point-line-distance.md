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
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        long x1 = sc.nextLong(); long y1 = sc.nextLong();
        long x2 = sc.nextLong(); long y2 = sc.nextLong();
        long px = sc.nextLong(); long py = sc.nextLong();
        System.out.printf("%.6f\n", new Solution().distancePointSegment(x1, y1, x2, y2, px, py));
        sc.close();
    }
}
```

### Python

```python
import math

def distance_point_segment(x1: int, y1: int, x2: int, y2: int, px: int, py: int) -> float:
    # Implementation here
    return 0.0

def main():
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        x1 = next(it)
        y1 = next(it)
        x2 = next(it)
        y2 = next(it)
        px = next(it)
        py = next(it)
        print(f"{distance_point_segment(x1, y1, x2, y2, px, py):.6f}")
    except StopIteration:
        return

if __name__ == "__main__":
    main()
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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x1, y1, x2, y2, px, py;
    if (!(cin >> x1 >> y1 >> x2 >> y2 >> px >> py)) return 0;

    Solution sol;
    cout << fixed << setprecision(6) << sol.distancePointSegment(x1, y1, x2, y2, px, py) << "\n";

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
