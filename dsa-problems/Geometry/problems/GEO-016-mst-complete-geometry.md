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

```
// No template available
```

### Python

```
// No template available
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    void update(int i, long long val, int p_id) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 1) {
        cout << 0 << endl;
        return 0;
    }

    vector<Point> pts(n);
    for (int i = 0; i < n; i++) {
        cin >> pts[i].x >> pts[i].y;
        pts[i].id = i;
    }

    vector<Edge> edges;
    for (int s1 = 0; s1 < 2; s1++) {
        for (int s2 = 0; s2 < 2; s2++) {
            for (int sw = 0; sw < 2; sw++) {
                sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
                    return a.x != b.x ? a.x > b.x : a.y > b.y;
                });
                
                vector<int> ys(n);
                for (int i = 0; i < n; i++) ys[i] = pts[i].y - pts[i].x;
                vector<int> sorted_ys = ys;
                sort(sorted_ys.begin(), sorted_ys.end());
                sorted_ys.erase(unique(sorted_ys.begin(), sorted_ys.end()), sorted_ys.end());
                
                int m = sorted_ys.size();
                BIT bit(m);
                for (int i = 0; i < n; i++) {
                    int pos = lower_bound(sorted_ys.begin(), sorted_ys.end(), ys[i]) - sorted_ys.begin() + 1;
                    int idx = bit.query(pos);
                    if (idx != -1) {
                        long long d = abs((long long)pts[i].x - pts[idx].x) + abs((long long)pts[i].y - pts[idx].y);
                        edges.push_back({pts[i].id, pts[idx].id, d});
                    }
                    bit.update(pos, (long long)pts[i].x + pts[i].y, i);
                }

                for (auto& p : pts) swap(p.x, p.y);
            }
            for (auto& p : pts) p.y = -p.y;
        }
        for (auto& p : pts) p.x = -p.x;
    }

    sort(edges.begin(), edges.end());
    DSU dsu(n);
    long long mst = 0;
    int count = 0;
    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst += e.w;
            if (++count == n - 1) break;
        }
    }
    cout << mst << endl;

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  solve() {
    // Implementation here
    return null;
  }
}

// I/O handling
```
