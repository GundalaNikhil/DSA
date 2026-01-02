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
    public long solve(int n, long[] xs, long[] ys) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        int n = sc.nextInt();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }
        System.out.println(new Solution().solve(n, xs, ys));
        sc.close();
    }
}
```

### Python

```python
def solve(n: int, xs: list, ys: list) -> int:
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
        xs = []
        ys = []
        for _ in range(n):
            xs.append(next(it))
            ys.append(next(it))
        print(solve(n, xs, ys))
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
    long long solve(int n, const vector<long long>& xs, const vector<long long>& ys) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> xs(n), ys(n);
    for (int i = 0; i < n; i++) {
        cin >> xs[i] >> ys[i];
    }

    Solution sol;
    cout << sol.solve(n, xs, ys) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve(n, xs, ys) {
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
    const xs = [], ys = [];
    for (let i = 0; i < n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }
    const sol = new Solution();
    console.log(sol.solve(n, xs, ys));
});
```
