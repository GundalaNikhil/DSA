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
import java.io.*;

class Main {
    static class Point {
        int x, y, id;
        Point(int x, int y, int id) { this.x = x; this.y = y; this.id = id; }
    }

    static class Edge implements Comparable<Edge> {
        int u, v;
        long weight;
        Edge(int u, int v, long weight) { this.u = u; this.v = v; this.weight = weight; }
        @Override
        public int compareTo(Edge other) { return Long.compare(this.weight, other.weight); }
    }

    static class DSU {
        int[] parent;
        DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        boolean union(int i, int j) {
            //Implement here
            return false;
        }
    }

    static class BIT {
        long[] minVal;
        int[] id;
        int size;
        BIT(int n) {
            size = n;
            minVal = new long[n + 1];
            id = new int[n + 1];
            Arrays.fill(minVal, Long.MAX_VALUE);
            Arrays.fill(id, -1);
        }
        void update(int i, long val, int pId) {
            for (; i > 0; i -= i & -i) {
                if (val < minVal[i]) {
                    minVal[i] = val;
                    id[i] = pId;
                }
            }
        }
        int query(int i) {
            long minV = Long.MAX_VALUE;
            int resId = -1;
            for (; i <= size; i += i & -i) {
                if (minVal[i] < minV) {
                    minV = minVal[i];
                    resId = id[i];
                }
            }
            return resId;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = br.readLine();
        if (firstLine == null) return;
        StringTokenizer st = new StringTokenizer(firstLine);
        if (!st.hasMoreTokens()) return;
        int n = Integer.parseInt(st.nextToken());
        
        Point[] pts = new Point[n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            if (line == null) break;
            st = new StringTokenizer(line);
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pts[i] = new Point(x, y, i);
        }

        if (n <= 1) {
            System.out.println(0);
            return;
        }

        List<Edge> edges = new ArrayList<>();
        for (int s1 = 0; s1 < 2; s1++) {
            for (int s2 = 0; s2 < 2; s2++) {
                for (int swap = 0; swap < 2; swap++) {
                    Arrays.sort(pts, (a, b) -> a.x != b.x ? b.x - a.x : b.y - a.y);
                    
                    int[] ys = new int[n];
                    for (int i = 0; i < n; i++) ys[i] = pts[i].y - pts[i].x;
                    int[] sortedYs = ys.clone();
                    Arrays.sort(sortedYs);
                    Map<Integer, Integer> rank = new HashMap<>();
                    int r = 1;
                    if (n > 0) rank.put(sortedYs[0], r++);
                    for (int i = 1; i < n; i++) if (sortedYs[i] != sortedYs[i-1]) rank.put(sortedYs[i], r++);
                    
                    BIT bit = new BIT(r);
                    for (int i = 0; i < n; i++) {
                        int pos = rank.get(ys[i]);
                        int idx = bit.query(pos);
                        if (idx != -1) {
                            long d = Math.abs((long)pts[i].x - pts[idx].x) + Math.abs((long)pts[i].y - pts[idx].y);
                            edges.add(new Edge(pts[i].id, pts[idx].id, d));
                        }
                        bit.update(pos, (long)pts[i].x + pts[i].y, i);
                    }

                    for (Point p : pts) { int tmp = p.x; p.x = p.y; p.y = tmp; }
                }
                for (Point p : pts) p.y = -p.y;
            }
            for (Point p : pts) p.x = -p.x;
        }

        Collections.sort(edges);
        DSU dsu = new DSU(n);
        long mst = 0;
        int count = 0;
        for (Edge e : edges) {
            if (dsu.union(e.u, e.v)) {
                mst += e.weight;
                count++;
                if (count == n - 1) break;
            }
        }
        System.out.println(mst);
    }
}
```

### Python

```python
def manhattan_mst(xs, ys):
    # //Implement here
    return 0
def main() -> None:
    import sys
    # Use robust reading for large inputs
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        xs = []
        ys = []
        for _ in range(n):
            xs.append(int(next(it)))
            ys.append(int(next(it)))
        print(manhattan_mst(xs, ys))
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
#include <numeric>

using namespace std;

struct Point {
    int x, y, id;
};

struct Edge {
    int u, v;
    long long w;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

struct BIT {
    int n;
    vector<long long> min_val;
    vector<int> id;
    BIT(int n) : n(n), min_val(n + 1, 4e18), id(n + 1, -1) {}
    void update(int i, long long val, int p_id) {
        for (; i > 0; i -= i & -i) {
            if (val < min_val[i]) {
                min_val[i] = val;
                id[i] = p_id;
            }
        }
    }
    int query(int i) {
        long long res_val = 4e18;
        int res_id = -1;
        for (; i <= n; i += i & -i) {
            if (min_val[i] < res_val) {
                res_val = min_val[i];
                res_id = id[i];
            }
        }
        return res_id;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        return parent[i] == i ? i : parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        //Implement here
        return false;
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
const fs = require('fs');

class BIT {
  constructor(n) {
    this.n = n;
    this.minVal = new Float64Array(n + 1).fill(4e18);
    this.id = new Int32Array(n + 1).fill(-1);
  }
  update(i, val, pId) {
    for (; i > 0; i -= i & -i) {
      if (val < this.minVal[i]) {
        this.minVal[i] = val;
        this.id[i] = pId;
      }
    }
  }
  query(i) {
    let resVal = 4e18;
    let resId = -1;
    for (; i <= this.n; i += i & -i) {
      if (this.minVal[i] < resVal) {
        resVal = this.minVal[i];
        resId = this.id[i];
      }
    }
    return resId;
  }
}

class DSU {
  constructor(n) {
    this.parent = new Int32Array(n);
    for (let i = 0; i < n; i++) this.parent[i] = i;
  }
  find(i) {
    if (this.parent[i] === i) return i;
    return this.parent[i] = this.find(this.parent[i]);
  }
  union(i, j) {
    //Implement here
    return false;
  }
}

function solve() {
  const input = fs.readFileSync(0, 'utf8').split(/\s+/);
  let ptr = 0;
  const n = parseInt(input[ptr++], 10);
  if (Number.isNaN(n)) return;
  if (n <= 1) {
    process.stdout.write("0\n");
    return;
  }

  const pts = [];
  for (let i = 0; i < n; i++) {
    pts.push({ x: parseInt(input[ptr++], 10), y: parseInt(input[ptr++], 10), id: i });
  }

  const edges = [];
  for (let s1 = 0; s1 < 2; s1++) {
    for (let s2 = 0; s2 < 2; s2++) {
      for (let sw = 0; sw < 2; sw++) {
        pts.sort((a, b) => a.x !== b.x ? b.x - a.x : b.y - a.y);

        const ys = pts.map(p => p.y - p.x);
        const sortedYs = Array.from(new Set(ys)).sort((a, b) => a - b);

        const bit = new BIT(sortedYs.length);
        for (let i = 0; i < n; i++) {
          const pos = sortedYs.indexOf(ys[i]) + 1;
          const idx = bit.query(pos);
          if (idx !== -1) {
            const d = Math.abs(pts[i].x - pts[idx].x) + Math.abs(pts[i].y - pts[idx].y);
            edges.push({ u: pts[i].id, v: pts[idx].id, w: d });
          }
          bit.update(pos, pts[i].x + pts[i].y, i);
        }

        for (const p of pts) {
          const tmp = p.x;
          p.x = p.y;
          p.y = tmp;
        }
      }
      for (const p of pts) p.y = -p.y;
    }
    for (const p of pts) p.x = -p.x;
  }

  edges.sort((a, b) => a.w - b.w);
  const dsu = new DSU(n);
  let mst = 0;
  let count = 0;
  for (const e of edges) {
    if (dsu.union(e.u, e.v)) {
      mst += e.w;
      if (++count === n - 1) break;
    }
  }
  process.stdout.write(mst.toString() + "\n");
}

solve();
```
