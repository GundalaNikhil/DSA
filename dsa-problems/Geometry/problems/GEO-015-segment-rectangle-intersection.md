---
problem_id: GEO_SEGMENT_RECT_INTERSECT__5580
display_id: GEO-015
slug: segment-rectangle-intersection
title: "Segment-Rectangle Intersection"
difficulty: Medium
difficulty_score: 50
topics:
  - Computational Geometry
  - Segment Intersection
  - Axis-Aligned Rectangle
tags:
  - geometry
  - intersection
  - rectangle
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-015: Segment-Rectangle Intersection

## Problem Statement

Given an axis-aligned rectangle with corners `(xL, yB)` (bottom-left) and `(xR, yT)` (top-right), and a line segment with endpoints `P1(x1, y1)` and `P2(x2, y2)`, determine whether the segment intersects or lies within the rectangle.

Intersection counts if the segment touches or crosses the rectangle boundary.

Print `true` if they intersect, otherwise `false`.

## ASCII Visual

```
Rect:
 (xL,yT) ●-------● (xR,yT)
         |       |
         |       |
 (xL,yB) ●-------● (xR,yB)

Segment that crosses any edge or lies inside → true
```

## Input Format

- Single line: six integers `xL yB xR yT x1 y1 x2 y2`

## Output Format

- Single word: `true` or `false`

## Constraints

- `-10^9 <= coordinates <= 10^9`
- `xL < xR`, `yB < yT`
- Segment endpoints may be outside the rectangle

## Example

**Input:**
```
0 0 2 2 -1 1 1 1
```

**Output:**
```
true
```

**Explanation:**

Segment crosses the left edge at `(0,1)`.

## Notes

- Check if either endpoint is inside; else test segment intersection with each of the 4 rectangle edges.
- Use orientation/on-segment predicates with 64-bit safety.

## Related Topics

Segment Intersection, Bounding Boxes, Orientation Test

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean intersects(long xL, long yB, long xR, long yT, long x1, long y1, long x2, long y2) {
        // Your implementation here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long xL = sc.nextLong(), yB = sc.nextLong(), xR = sc.nextLong(), yT = sc.nextLong();
        long x1 = sc.nextLong(), y1 = sc.nextLong(), x2 = sc.nextLong(), y2 = sc.nextLong();
        Solution sol = new Solution();
        System.out.println(sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
def intersects(xL: int, yB: int, xR: int, yT: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    # Your implementation here
    return False

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) != 8:
        return
    xL, yB, xR, yT, x1, y1, x2, y2 = data
    print("true" if intersects(xL, yB, xR, yT, x1, y1, x2, y2) else "false")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

bool intersects(long long xL, long long yB, long long xR, long long yT,
                long long x1, long long y1, long long x2, long long y2) {
    // Your implementation here
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long xL,yB,xR,yT,x1,y1,x2,y2;
    if (!(cin >> xL >> yB >> xR >> yT >> x1 >> y1 >> x2 >> y2)) return 0;
    cout << (intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function intersects(xL, yB, xR, yT, x1, y1, x2, y2) {
  // Your implementation here
  return false;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length !== 8) return;
  const [xL, yB, xR, yT, x1, y1, x2, y2] = data;
  console.log(intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false");
}

main();
```
