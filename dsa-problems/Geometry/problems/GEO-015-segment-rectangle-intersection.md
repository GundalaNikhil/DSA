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
import java.io.*;

class Solution {
    public boolean intersects(long xL, long yB, long xR, long yT, long x1, long y1, long x2, long y2) {
        // Implementation here
        return false;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        long xL = sc.nextLong(); long yB = sc.nextLong();
        long xR = sc.nextLong(); long yT = sc.nextLong();
        long x1 = sc.nextLong(); long y1 = sc.nextLong();
        long x2 = sc.nextLong(); long y2 = sc.nextLong();
        System.out.println(new Solution().intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false");
        sc.close();
    }
}
```

### Python

```python
def intersects(xL: int, yB: int, xR: int, yT: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    # Implementation here
    return False

def main():
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        xL = next(it)
        yB = next(it)
        xR = next(it)
        yT = next(it)
        x1 = next(it)
        y1 = next(it)
        x2 = next(it)
        y2 = next(it)
        result = intersects(xL, yB, xR, yT, x1, y1, x2, y2)
        print("true" if result else "false")
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

using namespace std;

class Solution {
public:
    bool intersects(long long xL, long long yB, long long xR, long long yT, long long x1, long long y1, long long x2, long long y2) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long xL, yB, xR, yT, x1, y1, x2, y2;
    if (cin >> xL >> yB >> xR >> yT >> x1 >> y1 >> x2 >> y2) {
        Solution sol;
        cout << (sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false") << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  intersects(xL, yB, xR, yT, x1, y1, x2, y2) {
    // Implementation here
    return null;
  }
}

class Solution {
  intersects(xL, yB, xR, yT, x1, y1, x2, y2) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const xL = data[ptr++];
  const yB = data[ptr++];
  const xR = data[ptr++];
  const yT = data[ptr++];
  const x1 = data[ptr++];
  const y1 = data[ptr++];
  const x2 = data[ptr++];
  const y2 = data[ptr++];
  
  const solution = new Solution();
  console.log(solution.intersects(xL, yB, xR, yT, x1, y1, x2, y2));
});
```
