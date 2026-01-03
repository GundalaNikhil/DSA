---
problem_id: GEO_MAX_OVERLAP_RECTS__6720
display_id: GEO-011
slug: max-overlap-rectangles
title: "Maximum Overlap of Rectangles"
difficulty: Medium
difficulty_score: 55
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
tags:
  - geometry
  - rectangles
  - sweep-line
  - overlap
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-011: Maximum Overlap of Rectangles

## Problem Statement

Given `m` axis-aligned rectangles, find the **maximum number of rectangles covering any point**. Rectangles are closed: points on edges or corners count as covered.

Return that maximum overlap count.

## ASCII Visual

```
Rect A: (0,0)-(2,2)
Rect B: (1,1)-(3,3)
Rect C: (2,0)-(4,2)

Max overlap = 2 (A∩B and B∩C touch, but no point has all 3)
```

## Input Format

- First line: integer `m`
- Next `m` lines: four integers `x1 y1 x2 y2` (`x1 < x2`, `y1 < y2`)

## Output Format

- Single integer: maximum overlap count

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x1 < x2 <= 10^9`
- `-10^9 <= y1 < y2 <= 10^9`

## Example

**Input:**
```
3
0 0 2 2
1 1 3 3
2 0 4 2
```

**Output:**
```
2
```

**Explanation:**

No point lies in all three; the best overlap is 2.

## Notes

- Sweep line over x with events at left/right edges; segment tree over y to maintain current max coverage.
- Coordinate compress y endpoints.

## Related Topics

Sweep Line, Segment Tree, Coordinate Compression

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long maxOverlap(long[] x1, long[] y1, long[] x2, long[] y2) {
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
        long result = solution.maxOverlap(x1, y1, x2, y2);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def max_overlap(x1, y1, x2, y2):
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
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for _ in range(m):
        x1.append(int(data[idx]));
        y1.append(int(data[idx + 1]));
        x2.append(int(data[idx + 2]));
        y2.append(int(data[idx + 3]));
        idx += 4
    result = max_overlap(x1, y1, x2, y2)
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

long long max_overlap(const vector<long long>& x1, const vector<long long>& y1,
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

    cout << max_overlap(x1, y1, x2, y2);
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function maxOverlap(x1, y1, x2, y2) {
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

const result = maxOverlap(x1, y1, x2, y2);
process.stdout.write(String(result));
```

