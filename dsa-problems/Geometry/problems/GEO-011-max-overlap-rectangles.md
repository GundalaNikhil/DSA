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
import java.io.*;

class Main {
    static class Solution {
        static class Event {
            long x;
            int type;
            int l, r;
            Event(long x, int type, int l, int r) {
                this.x = x;
                this.type = type;
                this.l = l;
                this.r = r;
            }
        }

        private int[] add;
        private int[] mx;

        private void update(int node, int l, int r, int ql, int qr, int val) {
            if (qr <= l || r <= ql) return;
            if (ql <= l && r <= qr) {
                int realVal = -val;
                add[node] += realVal;
                mx[node] += realVal;
                return;
            }
            int mid = (l + r) / 2;
            update(node * 2, l, mid, ql, qr, val);
            update(node * 2 + 1, mid, r, ql, qr, val);
            mx[node] = add[node] + Math.max(mx[node * 2], mx[node * 2 + 1]);
        }

        public int maxOverlap(long[] x1, long[] y1, long[] x2, long[] y2) {
            //Implement here
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int m = sc.nextInt();
        long[] x1 = new long[m]; long[] y1 = new long[m];
        long[] x2 = new long[m]; long[] y2 = new long[m];
        for(int i=0; i<m; i++) {
            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();
            x2[i] = sc.nextLong(); y2[i] = sc.nextLong();
        }
        System.out.println(new Solution().maxOverlap(x1, y1, x2, y2));
    }
}
```

### Python

```python
from typing import List

def max_overlap(x1: List[int], y1: List[int], x2: List[int], y2: List[int]) -> int:
    # //Implement here
    return 0
def main() -> None:
    import sys
    # Use generator input reading for robustness
    sys.setrecursionlimit(200000)
    def input_gen():
        for line in sys.stdin:
            for token in line.split():
                yield token
    it = input_gen()
    try:
        m = int(next(it))
        x1=[]; y1=[]; x2=[]; y2=[]
        for _ in range(m):
            x1.append(int(next(it))); y1.append(int(next(it))); x2.append(int(next(it))); y2.append(int(next(it)))
        print(max_overlap(x1, y1, x2, y2))
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
#include <cmath>
#include <iomanip>
#include <string>
#include <unordered_map>
#include <functional>
using namespace std;

// Same sweep; compress ys; segment tree supports range add and tracks max at root.

long long maxOverlap(const vector<long long>& x1, const vector<long long>& y1,
                     const vector<long long>& x2, const vector<long long>& y2) {
                         //Implement here
                         return 0;
                     }

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m; cin >> m;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    cout << maxOverlap(x1, y1, x2, y2) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

class Solution {
    solve(x1, y1, x2, y2) {
      //Implement here
      return 0;
    }
}
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());

    let m = nextInt();
    let x1=[], y1=[], x2=[], y2=[];
    for(let i=0; i<m; i++) {
        x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(x1, y1, x2, y2));
});
```

