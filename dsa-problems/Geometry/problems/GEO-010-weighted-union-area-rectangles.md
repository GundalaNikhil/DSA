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
import java.util.*;

class Solution {
    public long weightedArea(int[] x1, int[] y1, int[] x2, int[] y2, int[] w, int W) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int W = sc.nextInt();
        int[] x1 = new int[m], y1 = new int[m], x2 = new int[m], y2 = new int[m], w = new int[m];
        for (int i = 0; i < m; i++) {
            x1[i] = sc.nextInt(); y1[i] = sc.nextInt(); x2[i] = sc.nextInt(); y2[i] = sc.nextInt(); w[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.weightedArea(x1, y1, x2, y2, w, W));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def weighted_area(x1: List[int], y1: List[int], x2: List[int], y2: List[int], w: List[int], W: int) -> int:
    # Your implementation here
    return 0

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    m = next(it); W = next(it)
    x1=y1=x2=y2=w=None
    x1=[]; y1=[]; x2=[]; y2=[]; w=[]
    for _ in range(m):
        x1.append(next(it)); y1.append(next(it)); x2.append(next(it)); y2.append(next(it)); w.append(next(it))
    print(weighted_area(x1, y1, x2, y2, w, W))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long weightedArea(const vector<long long>& x1, const vector<long long>& y1,
                       const vector<long long>& x2, const vector<long long>& y2,
                       const vector<long long>& w, long long W) {
    // Your implementation here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m; long long W;
    if (!(cin >> m >> W)) return 0;
    vector<long long> x1(m), y1(m), x2(m), y2(m), w(m);
    for (int i = 0; i < m; ++i) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i] >> w[i];
    cout << weightedArea(x1, y1, x2, y2, w, W) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function weightedArea(x1, y1, x2, y2, w, W) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const m = data[idx++], W = data[idx++];
  const x1 = [], y1 = [], x2 = [], y2 = [], w = [];
  for (let i = 0; i < m; i++) {
    x1.push(data[idx++]); y1.push(data[idx++]); x2.push(data[idx++]); y2.push(data[idx++]); w.push(data[idx++]);
  }
  console.log(weightedArea(x1, y1, x2, y2, w, W));
}

main();
```
