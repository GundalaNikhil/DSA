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
    public long countIntersections(long[][] segs) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        long[][] segs = new long[m][4];
        for (int i = 0; i < m; i++) {
            segs[i][0] = sc.nextLong();
            segs[i][1] = sc.nextLong();
            segs[i][2] = sc.nextLong();
            segs[i][3] = sc.nextLong();
        }
        long count = new Solution().countIntersections(segs);
        System.out.println(count);
        sc.close();
    }
}
```

### Python

```python
from typing import List

def count_intersections(segs: List) -> int:
    # Implementation here
    return 0

def main() -> None:
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        m = int(next(it))
        segs = []
        for _ in range(m):
            x1 = int(next(it))
            y1 = int(next(it))
            x2 = int(next(it))
            y2 = int(next(it))
            segs.append([x1, y1, x2, y2])
        print(count_intersections(segs))
    except (StopIteration, ValueError):
        return

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countIntersections(const vector<vector<long long>>& segs) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (!(cin >> m)) return 0;

    vector<vector<long long>> segs(m, vector<long long>(4));
    for (int i = 0; i < m; i++) {
        cin >> segs[i][0] >> segs[i][1] >> segs[i][2] >> segs[i][3];
    }

    Solution sol;
    cout << sol.countIntersections(segs) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countIntersections(segs) {
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
    const nextInt = () => parseInt(lines[idx++]);
    const m = nextInt();
    const segs = [];
    for (let i = 0; i < m; i++) {
        const x1 = nextInt();
        const y1 = nextInt();
        const x2 = nextInt();
        const y2 = nextInt();
        segs.push([x1, y1, x2, y2]);
    }
    const sol = new Solution();
    console.log(sol.countIntersections(segs));
});
```
