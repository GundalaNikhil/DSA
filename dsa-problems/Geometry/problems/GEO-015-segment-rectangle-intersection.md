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
import java.io.*;
import java.util.*;

class Solution {
    public boolean intersects(long xL, long yB, long xR, long yT, long x1, long y1, long x2, long y2) {
        //Implemention here
        return false;
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
        if (data.length < 8) return;
        int idx = 0;
        long xL = Long.parseLong(data[idx++]);
        long yB = Long.parseLong(data[idx++]);
        long xR = Long.parseLong(data[idx++]);
        long yT = Long.parseLong(data[idx++]);
        long x1 = Long.parseLong(data[idx++]);
        long y1 = Long.parseLong(data[idx++]);
        long x2 = Long.parseLong(data[idx++]);
        long y2 = Long.parseLong(data[idx++]);

        Solution solution = new Solution();
        boolean result = solution.intersects(xL, yB, xR, yT, x1, y1, x2, y2);
        System.out.print(result ? "true" : "false");
    }
}
```

### Python

```python
import sys

def intersects(xL, yB, xR, yT, x1, y1, x2, y2):
    # //Implemention here
    return False

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 8:
        return
    vals = list(map(int, data[:8]))
    result = intersects(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7])
    sys.stdout.write("true" if result else "false")

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

bool intersects(long long xL, long long yB, long long xR, long long yT,
                long long x1, long long y1, long long x2, long long y2) {
    //Implemention here
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long xL, yB, xR, yT, x1, y1, x2, y2;
    if (!(cin >> xL >> yB >> xR >> yT >> x1 >> y1 >> x2 >> y2)) return 0;

    bool result = intersects(xL, yB, xR, yT, x1, y1, x2, y2);
    cout << (result ? "true" : "false");
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function intersects(xL, yB, xR, yT, x1, y1, x2, y2) {
  //Implemention here
  return false;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
if (data.length < 8) {
  process.exit(0);
}
let idx = 0;
const xL = data[idx++];
const yB = data[idx++];
const xR = data[idx++];
const yT = data[idx++];
const x1 = data[idx++];
const y1 = data[idx++];
const x2 = data[idx++];
const y2 = data[idx++];

const result = intersects(xL, yB, xR, yT, x1, y1, x2, y2);
process.stdout.write(result ? "true" : "false");
```

