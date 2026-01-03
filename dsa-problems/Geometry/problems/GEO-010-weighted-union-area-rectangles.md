---
problem_id: GEO_WEIGHTED_UNION_AREA__5312
display_id: GEO-010
slug: weighted-union-area-rectangles
title: "Line Sweep Weighted Union Area"
difficulty: Medium
difficulty_score: 70
topics:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
tags:
  - geometry
  - sweep-line
  - rectangles
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-010: Line Sweep Weighted Union Area

## Problem Statement

You are given `m` axis-aligned rectangles. Each rectangle `i` has integer weight `w[i]` (can be negative or positive). Given a threshold `W`, compute the total area of all points covered by rectangles whose **cumulative weight is at least `W`**.

Return that area as an integer.

## ASCII Visual

```
Rect A (w=1): (0,0)-(2,2)
Rect B (w=2): (1,1)-(3,3)

Overlap area (weight sum = 3) = 1x1 = 1
Total area where weight >= 2 is 4 (overlap 1 + B-only region 3)
```

## Input Format

- First line: integers `m` and `W`
- Next `m` lines: five integers `x1 y1 x2 y2 w` (`x1 < x2`, `y1 < y2`)

## Output Format

- Single integer: area of regions where cumulative weight >= `W`

## Constraints

- `1 <= m <= 100000`
- `|w[i]| <= 10^6`
- `1 <= W <= 10^6`
- `-10^9 <= x1 < x2 <= 10^9`
- `-10^9 <= y1 < y2 <= 10^9`

## Example

**Input:**
```
2 2
0 0 2 2 1
1 1 3 3 2
```

**Output:**
```
4
```

**Explanation:**

Weight-sum >= 2 region consists of overlap (1 area) plus B-only region (3 area).

## Notes

- Use sweep over x with events at rectangle edges; segment tree over y to maintain length where sum >= W.
- Coordinate compress y to handle large coords.
- Area accumulation: delta_x * covered_y_length.

## Related Topics

Sweep Line, Segment Tree, Coordinate Compression

---

## Solution Template

### Java

```java
import java.io.*;
import java.util.*;

class Solution {
    public long weightedArea(long[] x1, long[] y1, long[] x2, long[] y2, long[] w, long W) {
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
        if (data.length < 2) return;
        long W = Long.parseLong(data[idx++]);
        if (data.length < 2 + 5 * m) return;
        long[] x1 = new long[m];
        long[] y1 = new long[m];
        long[] x2 = new long[m];
        long[] y2 = new long[m];
        long[] w = new long[m];
        for (int i = 0; i < m; i++) {
            x1[i] = Long.parseLong(data[idx++]);
            y1[i] = Long.parseLong(data[idx++]);
            x2[i] = Long.parseLong(data[idx++]);
            y2[i] = Long.parseLong(data[idx++]);
            w[i] = Long.parseLong(data[idx++]);
        }

        Solution solution = new Solution();
        long result = solution.weightedArea(x1, y1, x2, y2, w, W);
        System.out.print(result);
    }
}
```

### Python

```python
import sys

def weighted_area(x1, y1, x2, y2, w, W):
    # //Implemention here
    return 0

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    m = int(data[idx]);
    idx += 1
    if len(data) < 2:
        return
    W = int(data[idx]);
    idx += 1
    if len(data) < 2 + 5 * m:
        return
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    w = []
    for _ in range(m):
        x1.append(int(data[idx]));
        y1.append(int(data[idx + 1]));
        x2.append(int(data[idx + 2]));
        y2.append(int(data[idx + 3]));
        w.append(int(data[idx + 4]));
        idx += 5
    result = weighted_area(x1, y1, x2, y2, w, W)
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

long long weighted_area(const vector<long long>& x1, const vector<long long>& y1,
                        const vector<long long>& x2, const vector<long long>& y2,
                        const vector<long long>& w, long long W) {
    //Implemention here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    if (!(cin >> m)) return 0;
    long long W;
    cin >> W;
    vector<long long> x1(m), y1(m), x2(m), y2(m), w(m);
    for (long long i = 0; i < m; i++) {
        cin >> x1[i] >> y1[i] >> x2[i] >> y2[i] >> w[i];
    }

    cout << weighted_area(x1, y1, x2, y2, w, W);
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function weightedArea(x1, y1, x2, y2, w, W) {
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
if (!Number.isFinite(m) || data.length < 2) {
  process.exit(0);
}
const W = data[idx++];
if (data.length < 2 + 5 * m) {
  process.exit(0);
}
const x1 = [];
const y1 = [];
const x2 = [];
const y2 = [];
const w = [];
for (let i = 0; i < m; i++) {
  x1.push(data[idx++]);
  y1.push(data[idx++]);
  x2.push(data[idx++]);
  y2.push(data[idx++]);
  w.push(data[idx++]);
}

const result = weightedArea(x1, y1, x2, y2, w, W);
process.stdout.write(String(result));
```
