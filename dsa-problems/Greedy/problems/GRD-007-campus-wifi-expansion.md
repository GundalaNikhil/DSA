---
problem_id: GRD_CAMPUS_WIFI_EXPANSION__4892
display_id: GRD-007
slug: campus-wifi-expansion
title: "Campus Wi-Fi Expansion"
difficulty: Medium
difficulty_score: 55
topics:
  - Greedy Algorithms
  - Minimum Spanning Tree
  - Kruskal's Algorithm
tags:
  - greedy
  - mst
  - kruskal
  - graph
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRD-007: Campus Wi-Fi Expansion

## Problem Statement

You need to connect `n` buildings on campus with network cables. Some buildings may already have cable connections between them (at no additional cost).

For buildings that aren't connected, laying a new cable between buildings `i` and `j` costs `|h[i] - h[j]|`, where `h[i]` is the height of building `i`.

Your goal is to find the minimum total cost to ensure all buildings are connected (directly or indirectly) to the same network.

![Problem Illustration](../images/GRD-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of buildings)
- Second line: `n` space-separated integers representing building heights `h[0], h[1], ..., h[n-1]`
- Third line: integer `m` (number of existing free cables)
- Next `m` lines: two integers `u v` representing an existing cable between buildings `u` and `v`

## Output Format

- Single integer: minimum total cost to connect all buildings

## Constraints

- `1 <= n <= 10^5`
- `1 <= h[i] <= 10^9`
- `0 <= m < n`
- `0 <= u, v < n`

## Example

**Input:**
```
3
5 1 9
0
```

**Output:**
```
8
```

**Explanation:**

Buildings with heights: [5, 1, 9]
No existing cables (m = 0)

Need to connect all 3 buildings. Possible edges:
- Building 0 to Building 1: cost = |5 - 1| = 4
- Building 0 to Building 2: cost = |5 - 9| = 4
- Building 1 to Building 2: cost = |1 - 9| = 8

Using Minimum Spanning Tree (MST):
- Connect buildings 0 and 1: cost = 4
- Connect buildings 0 and 2: cost = 4
- Total cost = 8

![Example Visualization](../images/GRD-007/example-1.png)

## Notes

- This is a Minimum Spanning Tree (MST) problem
- Existing cables are free (cost = 0) and should be used first
- For new cables, generate all possible edges with costs |h[i] - h[j]|
- Use Kruskal's algorithm with Union-Find
- Optimization: Sort buildings by height and only consider edges between adjacent buildings in sorted order
- Time complexity: O(n² log n) for generating all edges, or O(n log n) with optimization

## Related Topics

Minimum Spanning Tree, Kruskal's Algorithm, Greedy Algorithms, Union-Find, Graph Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Edge implements Comparable<Edge> {
        int u, v, cost;
        public Edge(int u, int v, int cost) {
            this.u = u;
            this.v = v;
            this.cost = cost;
        }
        @Override
        public int compareTo(Edge other) {
        return 0;
    }
    }

    static class DSU {
        int[] parent;
        public DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        public int find(int x) {
        return 0;
    }
        public boolean union(int x, int y) {
        return false;
    }
    }

    public long minCost(int n, int[] heights, int[][] existingCables) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) heights[i] = sc.nextInt();
        
        int m = sc.nextInt();
        int[][] existingCables = new int[m][2];
        for (int i = 0; i < m; i++) {
            existingCables[i][0] = sc.nextInt();
            existingCables[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.minCost(n, heights, existingCables));
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
    def find(self, x):
        return 0
    def union(self, x, y):
        return 0
def min_cost(n: int, heights: list, existing_cables: list) -> int:
    return 0
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    heights = []
    for _ in range(n):
        heights.append(int(next(iterator)))
        
    m = int(next(iterator))
    existing_cables = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        existing_cables.append([u, v])
        
    print(min_cost(n, heights, existing_cables))

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

struct Edge {
    int u, v, cost;
    bool operator<(const Edge& other) const {
        return cost < other.cost;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
            return true;
        }
        return false;
    }
};

class Solution {
public:
    long long minCost(int n, vector<int>& heights, vector<pair<int,int>>& existingCables) {
        DSU dsu(n);
        
        for (auto& cable : existingCables) {
            dsu.unite(cable.first, cable.second);
        }
        
        vector<pair<int,int>> sortedBuildings(n);
        for (int i = 0; i < n; i++) {
            sortedBuildings[i] = {heights[i], i};
        }
        
        sort(sortedBuildings.begin(), sortedBuildings.end());
        
        vector<Edge> edges;
        for (int i = 0; i < n - 1; i++) {
            int u = sortedBuildings[i].second;
            int v = sortedBuildings[i+1].second;
            int cost = sortedBuildings[i+1].first - sortedBuildings[i].first;
            edges.push_back({u, v, cost});
        }
        
        sort(edges.begin(), edges.end());
        
        long long totalCost = 0;
        for (const auto& edge : edges) {
            if (dsu.unite(edge.u, edge.v)) {
                totalCost += edge.cost;
            }
        }
        
        return totalCost;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> heights(n);
    for (int i = 0; i < n; i++) cin >> heights[i];

    int m;
    if (!(cin >> m)) return 0; // Should not happen based on constraints but safe check

    vector<pair<int,int>> existingCables(m);
    for (int i = 0; i < m; i++) {
        cin >> existingCables[i].first >> existingCables[i].second;
    }

    Solution solution;
    cout << solution.minCost(n, heights, existingCables) << "\n";

    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
  }
  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }
  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);
    if (rootX !== rootY) {
      this.parent[rootX] = rootY;
      return true;
    }
    return false;
  }
}

class Solution {
  minCost(n, heights, existingCables) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const heights = data[ptr++].split(" ").map(Number);
  const m = parseInt(data[ptr++]);
  
  const existingCables = [];
  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    existingCables.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.minCost(n, heights, existingCables));
});
```

