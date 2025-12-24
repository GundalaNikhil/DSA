---
problem_id: GEO_MST_MANHATTAN__7082
display_id: GEO-016
slug: mst-complete-geometry
title: "Minimum Spanning Tree on Complete Graph by Geometry"
difficulty: Hard
difficulty_score: 80
topics:
  - Computational Geometry
  - Minimum Spanning Tree
  - Manhattan Distance
tags:
  - geometry
  - manhattan
  - mst
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GEO-016: Minimum Spanning Tree on Complete Graph by Geometry

## Problem Statement

You are given `n` points in 2D. The complete graph has an edge between every pair of points with weight equal to their **Manhattan distance** (`|x1 - x2| + |y1 - y2|`).

Compute the total weight of a Minimum Spanning Tree (MST) of this graph.

Return the MST weight as an integer.

## ASCII Visual

```
Points:
● (0,0)   ● (3,0)
     ● (2,2)

Edge weights (Manhattan):
 (0,0)-(3,0): 3
 (0,0)-(2,2): 4
 (3,0)-(2,2): 3
MST weight = 6
```

## Input Format

- First line: integer `n`
- Next `n` lines: two integers `xi yi`

## Output Format

- Single integer: total weight of the MST

## Constraints

- `2 <= n <= 200000`
- `-10^9 <= xi, yi <= 10^9`

## Example

**Input:**
```
3
0 0
2 2
3 0
```

**Output:**
```
6
```

**Explanation:**

Edges: 4,3,3; MST chooses 3+3 = 6.

## Notes

- Use the Manhattan MST trick: consider 4 directional transforms and connect near neighbors via sweep with Fenwick/Hash map.
- Then run Kruskal on candidate edges (`O(n log n)`).

## Related Topics

MST, Manhattan Geometry, Kruskal, Sweep

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long manhattanMST(int[] xs, int[] ys) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] xs = new int[n], ys = new int[n];
        for (int i = 0; i < n; i++) { xs[i] = sc.nextInt(); ys[i] = sc.nextInt(); }
        Solution sol = new Solution();
        System.out.println(sol.manhattanMST(xs, ys));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def manhattan_mst(xs: List[int], ys: List[int]) -> int:
    # Your implementation here
    return 0

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    xs=[]; ys=[]
    for _ in range(n):
        xs.append(next(it)); ys.append(next(it))
    print(manhattan_mst(xs, ys))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long manhattanMST(const vector<long long>& xs, const vector<long long>& ys) {
    // Your implementation here
    return 0LL;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; ++i) cin >> xs[i] >> ys[i];
    cout << manhattanMST(xs, ys) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const fs = require("fs");

function manhattanMST(xs, ys) {
  // Your implementation here
  return 0;
}

function main() {
  const data = fs.readFileSync(0, "utf8").trim().split(/\\s+/).map(Number);
  if (data.length === 0) return;
  let idx = 0;
  const n = data[idx++];
  const xs = [], ys = [];
  for (let i = 0; i < n; i++) { xs.push(data[idx++]); ys.push(data[idx++]); }
  console.log(manhattanMST(xs, ys));
}

main();
```
