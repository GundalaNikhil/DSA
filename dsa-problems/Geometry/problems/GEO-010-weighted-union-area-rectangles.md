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
    public long solve(int n, int targetW, int[][] rects) {
        // Implementation here
        return 0;
    }
}

class Main {
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
        System.out.println(new Solution().solve(n, targetW, rects));
        sc.close();
    }
}
```

### Python

```python
def solve(n: int, targetW: int, rects: list) -> int:
    # Implementation here
    return 0

def main():
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        n = next(it)
        targetW = next(it)
        rects = []
        for _ in range(n):
            x1 = next(it)
            y1 = next(it)
            x2 = next(it)
            y2 = next(it)
            w = next(it)
            rects.append([x1, y1, x2, y2, w])
        print(solve(n, targetW, rects))
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

class Solution {
public:
    long long solve(int n, int targetW, const vector<vector<int>>& rects) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, targetW;
    if (!(cin >> n >> targetW)) return 0;

    vector<vector<int>> rects(n, vector<int>(5));
    for (int i = 0; i < n; i++) {
        cin >> rects[i][0] >> rects[i][1] >> rects[i][2] >> rects[i][3] >> rects[i][4];
    }

    Solution sol;
    cout << sol.solve(n, targetW, rects) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(n, targetW, rects) {
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
    const n = nextInt();
    const targetW = nextInt();
    const rects = [];
    for (let i = 0; i < n; i++) {
        const x1 = nextInt();
        const y1 = nextInt();
        const x2 = nextInt();
        const y2 = nextInt();
        const w = nextInt();
        rects.push([x1, y1, x2, y2, w]);
    }
    const sol = new Solution();
    console.log(sol.solve(n, targetW, rects));
});
```
