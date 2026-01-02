---
problem_id: GRB_MST_KRUSKAL__2657
display_id: GRB-007
slug: mst-kruskal
title: "MST Kruskal"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - DSU
tags:
  - graphs-basics
  - mst
  - dsu
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-007: MST Kruskal

## Problem Statement

Given a connected, undirected weighted graph, compute the total weight of its minimum spanning tree (MST) using Kruskal's algorithm.

![Problem Illustration](../images/GRB-007/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing an undirected edge with weight `w`

## Output Format

- Single integer: the total weight of the MST

## Constraints

- `1 <= n <= 100000`
- `n-1 <= m <= 200000`
- `0 <= w <= 10^9`
- The graph is connected

## Example

**Input:**

```
3 3
0 1 1
1 2 2
0 2 3
```

**Output:**

```
3
```

**Explanation:**

The MST uses edges (0-1) and (1-2) with total weight 3.

![Example Visualization](../images/GRB-007/example-1.png)

## Notes

- Sort edges by weight and add if they connect different components.
- Use DSU (disjoint set union) with path compression and union by rank.
- The total fits in 64-bit integers.

## Related Topics

Minimum Spanning Tree, Kruskal, DSU

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    class DSU {
        int[] parent;
        DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        void union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) parent[rootI] = rootJ;
        }
    }

    public long mstKruskal(int n, int[][] edges) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.mstKruskal(n, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

class DSU:
    def __init__(self, n):
        return 0
    def find(self, i):
        return 0
    def union(self, i, j):
        return 0
def mst_kruskal(n: int, edges: list[tuple[int, int, int]]) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        print(mst_kruskal(n, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <numeric>

using namespace std;

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
    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) parent[rootI] = rootJ;
    }
};

class Solution {
public:
    long long mstKruskal(int n, vector<array<int, 3>>& edges) {
        sort(edges.begin(), edges.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
            return a[2] < b[2];
        });

        DSU dsu(n);
        long long mstWeight = 0;
        int edgesCount = 0;

        for (const auto& edge : edges) {
            if (dsu.find(edge[0]) != dsu.find(edge[1])) {
                dsu.unite(edge[0], edge[1]);
                mstWeight += edge[2];
                edgesCount++;
            }
        }
        return mstWeight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.mstKruskal(n, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = new Int32Array(n);
    for (let i = 0; i < n; i++) this.parent[i] = i;
  }
  find(i) {
    if (this.parent[i] === i) return i;
    return (this.parent[i] = this.find(this.parent[i]));
  }
  union(i, j) {
    const rootI = this.find(i);
    const rootJ = this.find(j);
    if (rootI !== rootJ) {
      this.parent[rootI] = rootJ;
      return true;
    }
    return false;
  }
}

class Solution {
  mstKruskal(n, edges) {
    return 0;
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
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.mstKruskal(n, edges));
});
```

