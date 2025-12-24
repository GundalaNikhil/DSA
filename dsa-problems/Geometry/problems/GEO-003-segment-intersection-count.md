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
    public long countIntersections(int[] x1, int[] y1, int[] x2, int[] y2) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int[] x1 = new int[m], y1 = new int[m], x2 = new int[m], y2 = new int[m];
        for (int i = 0; i < m; i++) {
            x1[i] = sc.nextInt();
            y1[i] = sc.nextInt();
            x2[i] = sc.nextInt();
            y2[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.countIntersections(x1, y1, x2, y2));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def count_intersections(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    # Your implementation here
    return 0

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    m = next(it)
    x1 = [0]*m; y1 = [0]*m; x2 = [0]*m; y2 = [0]*m
    for i in range(m):
        x1[i] = next(it); y1[i] = next(it); x2[i] = next(it); y2[i] = next(it)
    print(count_intersections(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long countIntersections(const vector<long long>& x1, const vector<long long>& y1,
                             const vector<long long>& x2, const vector<long long>& y2) {
    // Your implementation here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> m)) return 0;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for (int i = 0; i < m; ++i) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    cout << countIntersections(x1, y1, x2, y2) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function countIntersections(x1, y1, x2, y2) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const m = data[idx++];
  const x1 = new Array(m), y1 = new Array(m), x2 = new Array(m), y2 = new Array(m);
  for (let i = 0; i < m; i++) {
    x1[i] = data[idx++]; y1[i] = data[idx++]; x2[i] = data[idx++]; y2[i] = data[idx++];
  }
  console.log(countIntersections(x1, y1, x2, y2));
}

main();
```
