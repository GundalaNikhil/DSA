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

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539589/dsa/geometry/naxy3vh0ezzdg5bnqeqs.jpg)

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
import java.io.*;

class Solution {
    public int getMaxOverlap(int m, long[][] rects) {
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

        long[][] rects = new long[m][4];
        for (int i = 0; i < m; i++) {
            String[] r = br.readLine().trim().split("\\s+");
            rects[i][0] = Long.parseLong(r[0]);
            rects[i][1] = Long.parseLong(r[1]);
            rects[i][2] = Long.parseLong(r[2]);
            rects[i][3] = Long.parseLong(r[3]);
        }

        Solution sol = new Solution();
        System.out.println(sol.getMaxOverlap(m, rects));
    }
}
```

### Python

```python
import sys

class Solution:
    def get_max_overlap(self, m, rects):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    idx = 1
    rects = []
    for _ in range(m):
        rects.append(list(map(int, input_data[idx:idx+4])))
        idx += 4

    sol = Solution()
    print(sol.get_max_overlap(m, rects))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getMaxOverlap(int m, vector<vector<long long>>& rects) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m;
    if (!(cin >> n)) return 0; // Wait, I should use m here

    vector<vector<long long>> rects(m, vector<long long>(4));
    for (int i = 0; i < m; i++) {
        cin >> rects[i][0] >> rects[i][1] >> rects[i][2] >> rects[i][3];
    }

    Solution sol;
    cout << sol.getMaxOverlap(m, rects) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  getMaxOverlap(m, rects) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 1) return;

  let idx = 0;
  const m = parseInt(input[idx++]);
  const rects = [];
  for (let i = 0; i < m; i++) {
    rects.push([
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
      parseInt(input[idx++]),
    ]);
  }

  const sol = new Solution();
  console.log(sol.getMaxOverlap(m, rects));
}

solve();
```
