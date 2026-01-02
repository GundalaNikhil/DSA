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
static class Solution {
    private int orient(long ax,long ay,long bx,long by,long cx,long cy){
        long v = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax);
        return Long.compare(v,0);
    }
    private boolean onSeg(long ax,long ay,long bx,long by,long cx,long cy){
        return orient(ax,ay,bx,by,cx,cy)==0 &&
               Math.min(ax,bx)<=cx && cx<=Math.max(ax,bx) &&
               Math.min(ay,by)<=cy && cy<=Math.max(ay,by);
    }
    private boolean segInter(long ax,long ay,long bx,long by,long cx,long cy,long dx,long dy){
        int o1=orient(ax,ay,bx,by,cx,cy), o2=orient(ax,ay,bx,by,dx,dy);
        int o3=orient(cx,cy,dx,dy,ax,ay), o4=orient(cx,cy,dx,dy,bx,by);
        if (o1==0 && onSeg(ax,ay,bx,by,cx,cy)) return true;
        if (o2==0 && onSeg(ax,ay,bx,by,dx,dy)) return true;
        if (o3==0 && onSeg(cx,cy,dx,dy,ax,ay)) return true;
        if (o4==0 && onSeg(cx,cy,dx,dy,bx,by)) return true;
        return (long)o1*o2 < 0 && (long)o3*o4 < 0;
    }
    public boolean intersects(long xL, long yB, long xR, long yT, long x1, long y1, long x2, long y2) {
        boolean inside1 = (xL <= x1 && x1 <= xR && yB <= y1 && y1 <= yT);
        boolean inside2 = (xL <= x2 && x2 <= xR && yB <= y2 && y2 <= yT);
        if (inside1 || inside2) return true;
        long[][] edges = {{xL,yB,xR,yB},{xR,yB,xR,yT},{xR,yT,xL,yT},{xL,yT,xL,yB}};
        for (long[] e: edges) {
            if (segInter(x1,y1,x2,y2,e[0],e[1],e[2],e[3])) return true;
        }
        return false;
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
    xL = BigInt(xL); yB = BigInt(yB); xR = BigInt(xR); yT = BigInt(yT);
    x1 = BigInt(x1); y1 = BigInt(y1); x2 = BigInt(x2); y2 = BigInt(y2);

    const orient = (ax, ay, bx, by, cx, cy) => {
      const v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
      if (v > 0n) return 1;
      if (v < 0n) return -1;
      return 0;
    };

    const onSeg = (ax, ay, bx, by, cx, cy) => {
      return orient(ax, ay, bx, by, cx, cy) === 0 &&
             (ax < bx ? ax : bx) <= cx && cx <= (ax > bx ? ax : bx) &&
             (ay < by ? ay : by) <= cy && cy <= (ay > by ? ay : by);
    };

    const segInter = (ax, ay, bx, by, cx, cy, dx, dy) => {
      const o1 = orient(ax, ay, bx, by, cx, cy);
      const o2 = orient(ax, ay, bx, by, dx, dy);
      const o3 = orient(cx, cy, dx, dy, ax, ay);
      const o4 = orient(cx, cy, dx, dy, bx, by);

      if (o1 === 0 && onSeg(ax, ay, bx, by, cx, cy)) return true;
      if (o2 === 0 && onSeg(ax, ay, bx, by, dx, dy)) return true;
      if (o3 === 0 && onSeg(cx, cy, dx, dy, ax, ay)) return true;
      if (o4 === 0 && onSeg(cx, cy, dx, dy, bx, by)) return true;

      return o1 !== o2 && o3 !== o4;
    };

    const inside1 = (xL <= x1 && x1 <= xR && yB <= y1 && y1 <= yT);
    const inside2 = (xL <= x2 && x2 <= xR && yB <= y2 && y2 <= yT);
    if (inside1 || inside2) return true;

    const edges = [
      [xL, yB, xR, yB],
      [xR, yB, xR, yT],
      [xR, yT, xL, yT],
      [xL, yT, xL, yB]
    ];

    for (const e of edges) {
      if (segInter(x1, y1, x2, y2, e[0], e[1], e[2], e[3])) return true;
    }

    return false;
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
