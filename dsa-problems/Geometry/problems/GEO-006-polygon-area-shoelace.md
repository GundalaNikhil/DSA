---
problem_id: GEO_POLYGON_AREA_SHOELACE__7719
display_id: GEO-006
slug: polygon-area-shoelace
title: "Polygon Area (Shoelace)"
difficulty: Easy-Medium
difficulty_score: 45
topics:
  - Computational Geometry
  - Polygon
  - Shoelace Formula
tags:
  - geometry
  - area
  - shoelace
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-006: Polygon Area (Shoelace)

## Problem Statement

Given a simple polygon with `n` vertices listed in order (clockwise or counterclockwise), compute its **signed area**. Output the absolute area.

Use the shoelace formula; avoid floating point by working in twice-the-area and dividing at the end if needed.

## Emoji Visual

```
⬛ Square:
🟢 (0,0) ---- 🟢 (2,0)
|               |
|               |
🟢 (0,2) ---- 🟢 (2,2)
Area = 4
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi` for each vertex, in order

## Output Format

- Single integer: absolute area of the polygon

## Constraints

- `3 <= n <= 100000`
- `-10^9 <= xi, yi <= 10^9`
- Polygon is simple (non-self-intersecting)

## Example

**Input:**
```
4
0 0
2 0
2 2
0 2
```

**Output:**
```
4
```

**Explanation:**

Axis-aligned square of side 2 has area 4.

## Notes

- Signed area from the shoelace sum may be negative if the order is clockwise; take `abs`.
- Twice-the-area fits in 128-bit; store in 64-bit carefully (`~2e18`).

## Related Topics

Polygon Geometry, Shoelace Formula, Cross Product

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Main {
static class Solution {
    public long polygonArea(long[] xs, long[] ys) {
        //Implement here
        return 0L;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().polygonArea(xs, ys));
    }
}
```

### Python

```python
from typing import List

def polygon_area(xs: List[int], ys: List[int]) -> int:
    # //Implement here
    return 0
def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    try:
        n = next(it)
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
        print(polygon_area(xs, ys))
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
using namespace std;

long long polygonArea(const vector<long long>& xs, const vector<long long>& ys) {
    //Implement here
    return 0;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    cout << polygonArea(xs, ys) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');

function polygonArea(xs, ys) {
  //Implement here
  return 0;
}


const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => { lines.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());
    const nextFloat = () => parseFloat(next());
    let n = nextInt();
    let xs = [], ys = [];
    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }
    console.log(Number(polygonArea(xs, ys)));
});
```

