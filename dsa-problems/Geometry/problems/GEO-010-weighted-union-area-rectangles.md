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

class Main {
    public static long solve(int n, int targetW, int[][] rects) {
        //Implement here
        return 0L;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int targetW = sc.nextInt();
        int[][] rects = new int[n][5];
        for (int i = 0; i < n; i++) {
            rects[i][0] = sc.nextInt();
            rects[i][1] = sc.nextInt();
            rects[i][2] = sc.nextInt();
            rects[i][3] = sc.nextInt();
            rects[i][4] = sc.nextInt();
        }
        System.out.println(solve(n, targetW, rects));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def weighted_area(x1: List[int], y1: List[int], x2: List[int], y2: List[int], w: List[int], W: int) -> int:
    # //Implement here
    return 0
def main() -> None:
    import sys
    # Increase recursion depth for deep segment tree
    sys.setrecursionlimit(200000)
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        m = int(next(it))
        if m == 0:
            return
        W = int(next(it))
        x1, y1, x2, y2, w = [], [], [], [], []
        for _ in range(m):
            x1.append(int(next(it)))
            y1.append(int(next(it)))
            x2.append(int(next(it)))
            y2.append(int(next(it)))
            w.append(int(next(it)))
        print(weighted_area(x1, y1, x2, y2, w, W))
    except StopIteration:
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

struct Rect {
    int x1, y1, x2, y2, w;
};

long long weightedUnionArea(const vector<Rect>& rects, long long targetW) {
    //Implement here
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long targetW;
    if (!(cin >> n >> targetW)) return 0;
    vector<Rect> rects(n);
    for (int i = 0; i < n; i++) {
        cin >> rects[i].x1 >> rects[i].y1 >> rects[i].x2 >> rects[i].y2 >> rects[i].w;
    }

    cout << weightedUnionArea(rects, targetW) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require('fs');

function weightedUnionArea(rects, targetW) {
  //Implement here
  return 0;
}

function solve() {
  const input = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
  if (input.length === 0 || input[0] === '') return;
  let idx = 0;
  const n = parseInt(input[idx++], 10);
  const targetW = parseInt(input[idx++], 10);
  if (Number.isNaN(n)) return;

  const rects = [];
  for (let i = 0; i < n; i++) {
    const x1 = parseInt(input[idx++], 10);
    const y1 = parseInt(input[idx++], 10);
    const x2 = parseInt(input[idx++], 10);
    const y2 = parseInt(input[idx++], 10);
    const w = parseInt(input[idx++], 10);
    rects.push({ x1, y1, x2, y2, w });
  }

  const result = weightedUnionArea(rects, targetW);
  console.log(result.toString());
}

solve();
```
