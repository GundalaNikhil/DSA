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
import java.io.*;
import java.util.*;

class Solution {
    public long countIntersections(long[] x1, long[] y1, long[] x2, long[] y2) {
        //Implemention here
        return 0L;
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
        int idx = 0;
        int m = Integer.parseInt(data[idx++]);
        if (data.length < 1 + 4 * m) return;
        long[] x1 = new long[m];
        long[] y1 = new long[m];
        long[] x2 = new long[m];
        long[] y2 = new long[m];
        for (int i = 0; i < m; i++) {
            x1[i] = Long.parseLong(data[idx++]);
            y1[i] = Long.parseLong(data[idx++]);
            x2[i] = Long.parseLong(data[idx++]);
            y2[i] = Long.parseLong(data[idx++]);
        }

        Solution solution = new Solution();
        long result = solution.countIntersections(x1, y1, x2, y2);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def count_intersections(x1, y1, x2, y2):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    m = int(data[idx]);
    idx += 1
    if len(data) < 1 + 4 * m:
        return
    x1 = [0] * m
    y1 = [0] * m
    x2 = [0] * m
    y2 = [0] * m
    for i in range(m):
        x1[i] = int(data[idx]);
        y1[i] = int(data[idx + 1]);
        x2[i] = int(data[idx + 2]);
        y2[i] = int(data[idx + 3]);
        idx += 4
    result = count_intersections(x1, y1, x2, y2)
    sys.stdout.write(str(result))

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

long long count_intersections(const vector<long long>& x1, const vector<long long>& y1,
                              const vector<long long>& x2, const vector<long long>& y2) {
    //Implemention here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    if (!(cin >> m)) return 0;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for (long long i = 0; i < m; i++) {
        cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    }

    cout << count_intersections(x1, y1, x2, y2);
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function countIntersections(x1, y1, x2, y2) {
  //Implemention here
  return 0;
}

const input = fs.readFileSync(0, "utf8").trim();
if (input.length === 0) {
  process.exit(0);
}
const data = input.split(/\s+/).map(Number);
let idx = 0;
const m = data[idx++];
if (!Number.isFinite(m) || data.length < 1 + 4 * m) {
  process.exit(0);
}
const x1 = [];
const y1 = [];
const x2 = [];
const y2 = [];
for (let i = 0; i < m; i++) {
  x1.push(data[idx++]);
  y1.push(data[idx++]);
  x2.push(data[idx++]);
  y2.push(data[idx++]);
}

const result = countIntersections(x1, y1, x2, y2);
process.stdout.write(String(result));
```

