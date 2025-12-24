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

class Solution {
    public double distancePointSegment(long x1, long y1, long x2, long y2, long px, long py) {
        // Your implementation here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long x1 = sc.nextLong(), y1 = sc.nextLong(), x2 = sc.nextLong(), y2 = sc.nextLong(), px = sc.nextLong(), py = sc.nextLong();
        Solution sol = new Solution();
        System.out.printf("%.6f%n", sol.distancePointSegment(x1, y1, x2, y2, px, py));
        sc.close();
    }
}
```

### Python

```python
def distance_point_segment(x1: int, y1: int, x2: int, y2: int, px: int, py: int) -> float:
    # Your implementation here
    return 0.0

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) != 6:
        return
    x1, y1, x2, y2, px, py = data
    print(f"{distance_point_segment(x1, y1, x2, y2, px, py):.6f}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

double distancePointSegment(long long x1, long long y1, long long x2, long long y2, long long px, long long py) {
    // Your implementation here
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long x1,y1,x2,y2,px,py;
    if (!(cin >> x1 >> y1 >> x2 >> y2 >> px >> py)) return 0;
    cout.setf(ios::fixed); cout << setprecision(6);
    cout << distancePointSegment(x1, y1, x2, y2, px, py) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function distancePointSegment(x1, y1, x2, y2, px, py) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
  if (data.length !== 6) return;
  const [x1, y1, x2, y2, px, py] = data;
  console.log(distancePointSegment(x1, y1, x2, y2, px, py).toFixed(6));
}

main();
```
