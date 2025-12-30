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
---

# GEO-016: Minimum Spanning Tree on Complete Graph by Geometry

## 📋 Problem Summary

Given `n` points, the complete graph has edge weights = Manhattan distance. Find the MST total weight.

## 🌍 Real-World Scenario

**Scenario Title:** Grid City Fiber Planning**

In a rectilinear city, laying fiber between buildings costs Manhattan distance. You need the cheapest network connecting all buildings—an MST under L1 metric.

**Why This Problem Matters:**

- Direct `O(n^2)` is impossible for `n = 2e5`.
- The Manhattan MST trick reduces candidate edges to `O(n)` using geometry, then Kruskal/Prim.
- A staple pattern for competitive programming and spatial optimization.

## ASCII Visual

```
Points:
● (0,0)   ● (3,0)
     ● (2,2)

Edges (Manhattan):
 (0,0)-(3,0): 3
 (0,0)-(2,2): 4
 (3,0)-(2,2): 3
MST weight = 6 (choose edges 3 and 3)
```

## Detailed Explanation

### Manhattan MST Trick (4 Transforms)

Key idea: For Manhattan distance, the potential nearest neighbors lie among points with maximal `x+y` or `x-y` in certain directions. By sweeping in 4 rotated quadrants, we can generate `O(n)` candidate edges that suffice for the MST.

For each of 4 transforms:
1. Transform points (optionally swap `x,y`, negate `x`, etc.).
2. Sort by `x` then `y`.
3. Sweep; maintain map keyed by `(y - x)` (or use Fenwick) to find best candidate for each point.
4. Add edge between point and candidate with weight = Manhattan distance in original coords.

Transforms (cover all octants):
- `(x, y)`
- `(-x, y)`
- `(x, -y)`
- `(-x, -y)`
And also swap x/y to cover other diagonals, or equivalently handle 4 directions with `(x, y)`, `(y, x)`, `(-x, y)`, `(-y, x)`.

### Why It Works

The rectilinear Voronoi structure implies that for each direction, the closest point that could reduce MST weight is among those maximizing `x+y` (or related expression). The 4 sweeps capture all candidate edges needed for a rectilinear MST (proof akin to Delaunay + MST for L1).

### Build MST

Collect all candidate edges (dedup). Run Kruskal with DSU:
- Sort edges by weight `O(m log m)`, `m = O(n)`.
- Union components, add weight when connecting new component.

Result is MST weight.

## Input/Output Clarifications

- Points can have duplicate coordinates? Typically distinct; if duplicates, zero-weight edges connect them; handle naturally.
- Output only the MST total weight.

## Naive Approach

**Algorithm:** Build all `O(n^2)` edges, run Kruskal/Prim.  
**Time:** `O(n^2)` edges + MST → impossible for `n = 2e5`.

## Optimal Approach (4 Sweeps + Kruskal)

**Algorithm Steps:**

1. For each of 4 direction variants:
   - Sort points by `x`, breaking ties by `y`.
   - Use a structure keyed by `y - x` to find candidate with max `(x+y)` seen so far; add that edge.
2. Gather all edges; remove duplicates (e.g., using a hash set of pairs).
3. Sort edges by weight.
4. DSU over `n` points to build MST; accumulate weight.

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`

## Reference Implementations

### Python (outline)

```python
def manhattan_mst(xs, ys):
    n = len(xs)
    pts = [(xs[i], ys[i], i) for i in range(n)]
    edges = []
    def add_edges(transform):
        arr = [transform(x,y,i) for x,y,i in pts]
        arr.sort()
        best = {}
        for tx, ty, ox, oy, idx in arr:
            key = ty - tx
            if key in best:
                j = best[key][1]
                w = abs(ox - pts[j][0]) + abs(oy - pts[j][1])
                edges.append((w, idx, j))
            val = tx + ty
            if key not in best or val > best[key][0]:
                best[key] = (val, idx)
    add_edges(lambda x,y,i:(x, y, x, y, i))
    add_edges(lambda x,y,i:(-x, y, x, y, i))
    add_edges(lambda x,y,i:(x, -y, x, y, i))
    add_edges(lambda x,y,i:(-x, -y, x, y, i))
    # Kruskal
    parent=list(range(n)); rank=[0]*n
    def find(a):
        while a!=parent[a]:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        a=find(a); b=find(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    edges = list(set(edges))
    edges.sort()
    ans=0; cnt=0
    for w,u,v in edges:
        if union(u,v):
            ans+=w; cnt+=1
            if cnt==n-1: break
    return ans


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>

using namespace std;

struct Point {
    int x, y, id;
};

struct Edge {
    long long w;
    int u, v;
    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

class DSU {
    vector<int> parent;
public:
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

class Solution {
    void add_edges(vector<Point>& pts, vector<Edge>& edges) {
        sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
            if (a.x != b.x) return a.x < b.x;
            return a.y < b.y;
        });
        
        vector<int> diffs;
        for(auto& p : pts) diffs.push_back(p.y - p.x);
        sort(diffs.begin(), diffs.end());
        diffs.erase(unique(diffs.begin(), diffs.end()), diffs.end());
        
        auto get_idx = [&](int val) {
            return lower_bound(diffs.begin(), diffs.end(), val) - diffs.begin() + 1;
        };
        
        int m = diffs.size();
        vector<pair<int, int>> bit(m + 1, {-2000000000, -1}); // max val, id
        
        auto update = [&](int idx, int val, int id) {
            for (; idx > 0; idx -= idx & -idx) {
                if (val > bit[idx].first) bit[idx] = {val, id};
            }
        };
        
        auto query = [&](int idx) {
            pair<int, int> res = {-2000000000, -1};
            for (; idx <= m; idx += idx & -idx) {
                if (bit[idx].first > res.first) res = bit[idx];
            }
            return res;
        };
        
        for (int i = 0; i < pts.size(); ++i) {
            auto& p = pts[i];
            int key = p.y - p.x;
            int idx = get_idx(key);
            pair<int, int> res = query(idx);
            if (res.second != -1) {
                // res.second is index in current sorted pts array
                auto& q = pts[res.second];
                long long w = abs(p.x - q.x) + abs(p.y - q.y);
                edges.push_back({w, p.id, q.id});
            }
            update(idx, p.x + p.y, i);
        }
    }

public:
    long long manhattanMST(vector<int>& xs, vector<int>& ys) {
        int n = xs.size();
        vector<Point> pts(n);
        for(int i=0; i<n; ++i) pts[i] = {xs[i], ys[i], i};
        
        vector<Edge> edges;
        
        // 4 sweeps
        for(int k=0; k<4; ++k) {
            add_edges(pts, edges);
            // Rotate 90 degrees: (x, y) -> (y, -x)
            for(auto& p : pts) {
                int tmp = p.x;
                p.x = p.y;
                p.y = -tmp;
            }
        }
        
        sort(edges.begin(), edges.end());
        
        DSU dsu(n);
        long long mst_weight = 0;
        int edges_count = 0;
        
        for(const auto& e : edges) {
            if(dsu.unite(e.u, e.v)) {
                mst_weight += e.w;
                edges_count++;
            }
        }
        
        return mst_weight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> xs(n), ys(n);
    for(int i=0; i<n; ++i) cin >> xs[i];
    for(int i=0; i<n; ++i) cin >> ys[i];
    
    Solution sol;
    cout << sol.manhattanMST(xs, ys) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = new Int32Array(n).map((_, i) => i);
  }
  find(i) {
    if (this.parent[i] === i) return i;
    return (this.parent[i] = this.find(this.parent[i]));
  }
  unite(i, j) {
    const root_i = this.find(i);
    const root_j = this.find(j);
    if (root_i !== root_j) {
      this.parent[root_i] = root_j;
      return true;
    }
    return false;
  }
}

class Solution {
  manhattanMST(xs, ys) {
    const n = xs.length;
    let pts = [];
    for (let i = 0; i < n; i++) pts.push({ x: xs[i], y: ys[i], id: i });
    
    const edges = [];
    
    const addEdges = () => {
      pts.sort((a, b) => {
        if (a.x !== b.x) return a.x - b.x;
        return a.y - b.y;
      });
      
      const diffs = [...new Set(pts.map(p => p.y - p.x))].sort((a, b) => a - b);
      const m = diffs.length;
      const bit = new Array(m + 1).fill(null); // {val, idx}
      
      const getIdx = (val) => {
        let l = 0, r = m - 1;
        while (l <= r) {
          const mid = (l + r) >>> 1;
          if (diffs[mid] >= val) r = mid - 1;
          else l = mid + 1;
        }
        return l + 1;
      };
      
      const update = (idx, val, id) => {
        for (; idx > 0; idx -= idx & -idx) {
          if (bit[idx] === null || val > bit[idx].val) {
            bit[idx] = { val, id };
          }
        }
      };
      
      const query = (idx) => {
        let res = null;
        for (; idx <= m; idx += idx & -idx) {
          if (bit[idx] !== null) {
            if (res === null || bit[idx].val > res.val) {
              res = bit[idx];
            }
          }
        }
        return res;
      };
      
      for (let i = 0; i < n; i++) {
        const p = pts[i];
        const key = p.y - p.x;
        const idx = getIdx(key);
        const res = query(idx);
        if (res !== null) {
          const q = pts[res.id]; // res.id is index in current sorted pts
          const w = Math.abs(p.x - q.x) + Math.abs(p.y - q.y);
          edges.push({ w, u: p.id, v: q.id });
        }
        update(idx, p.x + p.y, i);
      }
    };
    
    for (let k = 0; k < 4; k++) {
      addEdges();
      // Rotate 90 degrees: (x, y) -> (y, -x)
      for (const p of pts) {
        const tmp = p.x;
        p.x = p.y;
        p.y = -tmp;
      }
    }
    
    edges.sort((a, b) => a.w - b.w);
    
    const dsu = new DSU(n);
    let mstWeight = 0n;
    let count = 0;
    
    for (const e of edges) {
      if (dsu.unite(e.u, e.v)) {
        mstWeight += BigInt(e.w);
        count++;
      }
    }
    
    return mstWeight.toString();
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  
  const xs = [];
  for (let i = 0; i < n; i++) xs.push(parseInt(data[ptr++], 10));
  
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  console.log(solution.manhattanMST(xs, ys));
});
```

### Common Mistakes to Avoid

1. **Missing transforms.** All four directional sweeps needed to cover candidates.
2. **Not deduplicating edges.** Same edge can appear in multiple sweeps; dedupe before Kruskal.
3. **Overflow:** Use 64-bit for weights.
4. **Incorrect key:** Use `y - x` with sorting by `x` (after transform) and tracking max `x+y`.

### Complexity Analysis

- **Time:** `O(n log n)` (sort + Kruskal)  
- **Space:** `O(n)` for points, edges, DSU.

## Testing Strategy

- Small triangles/rectangles with known MST.
- Duplicate points (zero-weight edges).
- Points on a line (MST is sorted neighbors).
- Random small sets to validate vs brute-force.
- Large coordinates to test overflow.

## ASCII Recap

```
For each transform:
  sort by x, track best by (y-x) with max (x+y), add edge
Collect edges → dedupe → Kruskal → sum weights
```
