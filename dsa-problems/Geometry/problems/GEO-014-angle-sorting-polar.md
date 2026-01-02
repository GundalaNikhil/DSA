---
problem_id: GEO_ANGLE_SORTING_POLAR__2841
display_id: GEO-014
slug: angle-sorting-polar
title: "Angle Sorting for Polar Order"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Sorting
tags:
  - geometry
  - sorting
  - polar-angle
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-014: Angle Sorting for Polar Order

## Problem Statement

Given `n` points (distinct, no point at the origin), sort them by polar angle around the origin (0,0), in counterclockwise order. If two points have the same angle, the closer one (smaller distance to origin) should come first.

Output the points in the required order.

## ASCII Visual

```
   y
   ↑     ● (1,1)
   |  ● (1,0)   ● (0,1)
   |
   O------------→ x
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- `n` lines, each `x y` in the sorted order

## Constraints

- `1 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- No point is at the origin; points are distinct

## Example

**Input:**
```
3
1 0
1 1
0 1
```

**Output:**
```
1 0
1 1
0 1
```

**Explanation:**

Angles: (1,0) at 0°, (1,1) at 45°, (0,1) at 90°.

## Notes

- Use half-plane partition (upper vs lower) then cross product to sort without `atan2` for performance and stability.
- Tie-break by radius when cross product is zero.

## Related Topics

Sorting by Angle, Cross Product, Polar Coordinates

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public List<long[]> sortByAngle(long[] xs, long[] ys) {
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
static class Solution {
    public List<long[]> sortByAngle(long[] xs, long[] ys) {
        int n = xs.length;
        List<long[]> pts = new ArrayList<>();
        for (int i = 0; i < n; i++) pts.add(new long[]{xs[i], ys[i]});
        pts.sort((a, b) -> {
            int ha = (a[1] > 0 || (a[1] == 0 && a[0] > 0)) ? 0 : 1;
            int hb = (b[1] > 0 || (b[1] == 0 && b[0] > 0)) ? 0 : 1;
            if (ha != hb) return ha - hb;
            long cross = a[0]*b[1] - a[1]*b[0];
            if (cross != 0) return cross > 0 ? -1 : 1;
            long ra = a[0]*a[0] + a[1]*a[1];
            long rb = b[0]*b[0] + b[1]*b[1];
            return Long.compare(ra, rb);
        });
        return pts;
    }
}
```

### Python

```
// No template available
```

### C++

```
// No template available
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  sortByAngle(xs, ys) {
    // Implementation here
    return null;
  }
}

const readline = require('readline');

function new Solution().sortByAngle(xs, ys) {
  const pts = xs.map((x, i) => [x, ys[i]]);
  const half = ([x,y]) => (y > 0 || (y === 0 && x > 0)) ? 0 : 1;
  pts.sort((a, b) => {
    const ha = half(a), hb = half(b);
    if (ha !== hb) return ha - hb;
    const cross = a[0]*b[1] - a[1]*b[0];
    if (cross !== 0) return cross > 0 ? -1 : 1;
    const ra = a[0]*a[0] + a[1]*a[1];
    const rb = b[0]*b[0] + b[1]*b[1];
    return ra - rb;
  });
  return pts;
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
    let n = nextInt();
    let xs = [], ys = [];
    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }
    let res = new Solution().sortByAngle(xs, ys);
    res.forEach(p => console.log(p.join(' ')));
});
```
