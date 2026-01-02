---
problem_id: GEO_SEGMENT_INTERSECTION_COUNT__1538
display_id: GEO-003
slug: segment-intersection-count
title: "Segment Intersection Count"
difficulty: Medium
difficulty_score: 60
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Intersection
tags:
  - geometry
  - sweep-line
  - segments
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-003: Segment Intersection Count

## Problem Statement

You are given `m` line segments in 2D. Count how many **distinct pairs** of segments intersect (including touching at endpoints or overlapping).

Return the total number of intersecting pairs.

## ASCII Visual

```
S1: (0,0) to (2,2)
S2: (0,2) to (2,0)
S3: (3,0) to (3,2)

S1 and S2 intersect (X) once; S3 does not touch others.
```

## Input Format

- First line: integer `m` (number of segments)
- Next `m` lines: four integers `x1 y1 x2 y2` per segment

## Output Format

- Single integer: number of intersecting pairs

## Constraints

- `1 <= m <= 200000`
- `-10^9 <= coordinates <= 10^9`
- All segments are non-degenerate (endpoints are distinct)

## Example

**Input:**
```
2
0 0 2 2
0 2 2 0
```

**Output:**
```
1
```

**Explanation:**

The two segments cross once, so there is exactly one intersecting pair.

## Notes

- Touching at endpoints counts as an intersection.
- Overlapping (collinear) segments count as one intersecting pair.
- Use 64-bit arithmetic in orientation tests to avoid overflow.

## Related Topics

Computational Geometry, Sweep Line, Balanced BST

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int orient(long ax, long ay, long bx, long by, long cx, long cy) {
        // Implementation here
        return 0;
    }
}

class Main {
    private static int orient(long ax, long ay, long bx, long by, long cx, long cy) {
        long v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
        if (v == 0) return 0;
        return (v > 0) ? 1 : -1;
    }

    private static boolean onSeg(long ax, long ay, long bx, long by, long cx, long cy) {
        return Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
               Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
    }

    public static boolean intersects(long[] s, long[] t) {
        int o1 = orient(s[0], s[1], s[2], s[3], t[0], t[1]);
        int o2 = orient(s[0], s[1], s[2], s[3], t[2], t[3]);
        int o3 = orient(t[0], t[1], t[2], t[3], s[0], s[1]);
        int o4 = orient(t[0], t[1], t[2], t[3], s[2], s[3]);

        if (((o1 > 0 && o2 < 0) || (o1 < 0 && o2 > 0)) &&
            ((o3 > 0 && o4 < 0) || (o3 < 0 && o4 > 0))) return true;

        if (o1 == 0 && onSeg(s[0], s[1], s[2], s[3], t[0], t[1])) return true;
        if (o2 == 0 && onSeg(s[0], s[1], s[2], s[3], t[2], t[3])) return true;
        if (o3 == 0 && onSeg(t[0], t[1], t[2], t[3], s[0], s[1])) return true;
        if (o4 == 0 && onSeg(t[0], t[1], t[2], t[3], s[2], s[3])) return true;

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[][] segs = new long[n][4];
        for (int i = 0; i < n; i++) {
            segs[i][0] = sc.nextLong();
            segs[i][1] = sc.nextLong();
            segs[i][2] = sc.nextLong();
            segs[i][3] = sc.nextLong();
        }
        
        long count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (intersects(segs[i], segs[j])) count++;
            }
        }
        System.out.println(count);
        sc.close();
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

using namespace std;

class Solution {
public:
    int orient(long long ax, long long ay, long long bx, long long by, long long cx, long long cy) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Seg> segs(n);
    for (int i = 0; i < n; i++) {
        cin >> segs[i].x1 >> segs[i].y1 >> segs[i].x2 >> segs[i].y2;
    }

    long long count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (intersects(segs[i], segs[j])) count++;
        }
    }

    cout << count << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  orient(ax, ay, bx, by, cx, cy) {
    // Implementation here
    return null;
  }
}

// I/O handling
```
