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
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        long xL = Long.parseLong(parts[0]);
        long yB = Long.parseLong(parts[1]);
        long xR = Long.parseLong(parts[2]);
        long yT = Long.parseLong(parts[3]);
        long x1 = Long.parseLong(parts[4]);
        long y1 = Long.parseLong(parts[5]);
        long x2 = Long.parseLong(parts[6]);
        long y2 = Long.parseLong(parts[7]);

        Solution sol = new Solution();
        System.out.println(sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false");
    }
}
```

### Python

```python
import sys

class Solution:
    def intersects(self, xL, yB, xR, yT, x1, y1, x2, y2):
        # Implement here
        return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        xL = int(next(iterator))
        yB = int(next(iterator))
        xR = int(next(iterator))
        yT = int(next(iterator))
        x1 = int(next(iterator))
        y1 = int(next(iterator))
        x2 = int(next(iterator))
        y2 = int(next(iterator))
    except StopIteration:
        pass

    sol = Solution()
    print("true" if sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) else "false")

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool intersects(long long xL, long long yB, long long xR, long long yT, long long x1, long long y1, long long x2, long long y2) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long xL, yB, xR, yT, x1, y1, x2, y2;
    if (!(cin >> xL >> yB >> xR >> yT >> x1 >> y1 >> x2 >> y2)) return 0;

    Solution sol;
    cout << (sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false") << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  intersects(xL, yB, xR, yT, x1, y1, x2, y2) {
    // Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 8) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  } // Coordinates can be large, but JS uses numbers (doubles), up to 2^53 safe integer. 10^9 fits easily.

  const xL = readInt();
  const yB = readInt();
  const xR = readInt();
  const yT = readInt();
  const x1 = readInt();
  const y1 = readInt();
  const x2 = readInt();
  const y2 = readInt();

  const sol = new Solution();
  console.log(
    sol.intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false"
  );
}

solve();
```

### Python

### C++

### JavaScript
