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
import java.util.*;

class Solution {
    public int maxOverlap(int[] x1, int[] y1, int[] x2, int[] y2) {
        // Your implementation here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();
        int[] x1 = new int[m], y1 = new int[m], x2 = new int[m], y2 = new int[m];
        for (int i = 0; i < m; i++) {
            x1[i] = sc.nextInt(); y1[i] = sc.nextInt(); x2[i] = sc.nextInt(); y2[i] = sc.nextInt();
        }
        Solution sol = new Solution();
        System.out.println(sol.maxOverlap(x1, y1, x2, y2));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def max_overlap(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    # Your implementation here
    return 0

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    m = next(it)
    x1=[]; y1=[]; x2=[]; y2=[]
    for _ in range(m):
        x1.append(next(it)); y1.append(next(it)); x2.append(next(it)); y2.append(next(it))
    print(max_overlap(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int maxOverlap(const vector<long long>& x1, const vector<long long>& y1,
               const vector<long long>& x2, const vector<long long>& y2) {
    // Your implementation here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> m)) return 0;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for (int i = 0; i < m; ++i) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    cout << maxOverlap(x1, y1, x2, y2) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function maxOverlap(x1, y1, x2, y2) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const m = data[idx++];
  const x1=[], y1=[], x2=[], y2=[];
  for (let i = 0; i < m; i++) {
    x1.push(data[idx++]); y1.push(data[idx++]); x2.push(data[idx++]); y2.push(data[idx++]);
  }
  console.log(maxOverlap(x1, y1, x2, y2));
}

main();
```
