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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767567843/dsa/geometry/xphpdpbt1dlue9karhgo.jpg)


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
import java.io.*;

class Solution {
    public long countIntersections(int m, long[][] segments) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String mLine = br.readLine();
        if (mLine == null) return;
        int m = Integer.parseInt(mLine.trim());

        long[][] segments = new long[m][4];
        for (int i = 0; i < m; i++) {
            String[] s = br.readLine().trim().split("\\s+");
            segments[i][0] = Long.parseLong(s[0]);
            segments[i][1] = Long.parseLong(s[1]);
            segments[i][2] = Long.parseLong(s[2]);
            segments[i][3] = Long.parseLong(s[3]);
        }

        Solution sol = new Solution();
        System.out.println(sol.countIntersections(m, segments));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_intersections(self, m, segments):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    idx = 1
    segments = []
    for _ in range(m):
        segments.append(list(map(int, input_data[idx:idx+4])))
        idx += 4

    sol = Solution()
    print(sol.count_intersections(m, segments))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long countIntersections(int m, vector<vector<long long>>& segments) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m;
    if (!(cin >> m)) return 0;

    vector<vector<long long>> segments(m, vector<long long>(4));
    for (int i = 0; i < m; i++) {
        cin >> segments[i][0] >> segments[i][1] >> segments[i][2] >> segments[i][3];
    }

    Solution sol;
    cout << sol.countIntersections(m, segments) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countIntersections(m, segments) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const m = parseInt(input[idx++]);
  const segments = [];
  for (let i = 0; i < m; i++) {
    segments.push([
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  console.log(sol.countIntersections(m, segments));
}

solve();
```
