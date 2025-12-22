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
---

# GRB-007: MST Kruskal

## 📋 Problem Summary

Given a connected, undirected, weighted graph, find the **Minimum Spanning Tree (MST)**. An MST is a subset of edges that connects all vertices together, without any cycles, and with the minimum possible total edge weight. You must use **Kruskal's Algorithm**.

## 🌍 Real-World Scenario

**Scenario Title:** Power Grid Expansion

Imagine you are an electrical engineer tasked with connecting `N` cities to the power grid.
-   **Nodes** are cities.
-   **Edges** are potential power lines.
-   **Weights** are the costs to build those lines (based on distance, terrain, etc.).
-   **Goal:** Connect all cities so that electricity can flow to everyone, but do it as cheaply as possible. You don't need redundant loops (cycles); you just need a single connected network. This is exactly what an MST is.

![Real-World Application](../images/GRB-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)
  0 ------- 1
  | \       |
  |  \ (3)  | (2)
  |   \     |
 (4)   \    |
  |     \   |
  3 ------- 2
      (5)
```
**Edges:** `(0,1,1), (1,2,2), (0,2,3), (0,3,4), (2,3,5)`

**Kruskal's Steps:**
1.  **Sort Edges:** `(0,1,1), (1,2,2), (0,2,3), (0,3,4), (2,3,5)`
2.  **Pick (0,1,1):** Connects 0 and 1. OK. (Cost: 1)
3.  **Pick (1,2,2):** Connects 1 and 2. OK. (Cost: 1+2=3)
4.  **Pick (0,2,3):** 0 and 2 are already connected (via 1). **Cycle!** Skip.
5.  **Pick (0,3,4):** Connects 0 and 3. OK. (Cost: 3+4=7)
6.  **Pick (2,3,5):** 2 and 3 are already connected. Skip.

**MST Weight:** 7.

### Algorithm Steps

1.  **Sort Edges:** Sort all edges in ascending order of their weights.
2.  **Initialize DSU:** Create a Disjoint Set Union (DSU) structure where each node starts in its own set.
3.  **Iterate Edges:**
    -   For each edge `(u, v, w)`:
        -   Use DSU `find(u)` and `find(v)` to check if they are already in the same component.
        -   If they are different:
            -   Add `w` to total MST weight.
            -   Use DSU `union(u, v)` to merge the components.
            -   Increment edge count. If count reaches `N-1`, stop (optimization).
4.  **Output:** Total weight.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Connected Graph:** The input is guaranteed to be connected, so an MST always exists.
-   **Weights:** Can be large, so use 64-bit integers (`long` in Java/C++) for the sum.
-   **Multiple Edges:** Kruskal's handles them naturally (duplicates or heavier parallel edges are skipped).

## Naive Approach

### Intuition

Try every possible subset of edges, check if it's a spanning tree, and find the minimum weight.

### Time Complexity

-   **Exponential**: O(2^M). Completely infeasible.

## Optimal Approach (Kruskal's Algorithm)

Kruskal's is a greedy algorithm. It always picks the cheapest available edge that doesn't form a cycle.

### Time Complexity

-   **O(M log M)** or **O(M log N)**: Dominated by sorting the edges. DSU operations are nearly constant time (Inverse Ackermann function, α(N)).

### Space Complexity

-   **O(N + M)**: To store edges and DSU structures.

## Implementations

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
        // Sort edges by weight
        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));

        DSU dsu = new DSU(n);
        long mstWeight = 0;
        int edgesCount = 0;

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            if (dsu.find(u) != dsu.find(v)) {
                dsu.union(u, v);
                mstWeight += w;
                edgesCount++;
            }
        }
        
        return mstWeight;
    }
}

public class Main {
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
        self.parent = list(range(n))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def mst_kruskal(n: int, edges: list[tuple[int, int, int]]) -> int:
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    dsu = DSU(n)
    mst_weight = 0
    edges_count = 0
    
    for u, v, w in edges:
        if dsu.union(u, v):
            mst_weight += w
            edges_count += 1
            if edges_count == n - 1:
                break
                
    return mst_weight

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
    // Sort edges by weight
    edges.sort((a, b) => a[2] - b[2]);

    const dsu = new DSU(n);
    let mstWeight = 0n; // Use BigInt for safety
    let edgesCount = 0;

    for (const [u, v, w] of edges) {
      if (dsu.union(u, v)) {
        mstWeight += BigInt(w);
        edgesCount++;
        if (edgesCount === n - 1) break;
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

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1 1
1 2 2
0 2 3
```

**Initialization:**
-   `edges`: `[(0,1,1), (1,2,2), (0,2,3)]` (Already sorted)
-   `dsu`: `{0:0, 1:1, 2:2}`
-   `mstWeight`: 0

**Iteration 1:**
-   Edge `(0, 1, 1)`. `find(0)=0`, `find(1)=1`. Different.
-   Union(0, 1). `dsu`: `{0:1, 1:1, 2:2}`.
-   `mstWeight` += 1.

**Iteration 2:**
-   Edge `(1, 2, 2)`. `find(1)=1`, `find(2)=2`. Different.
-   Union(1, 2). `dsu`: `{0:1, 1:2, 2:2}`.
-   `mstWeight` += 2. Total: 3.

**Iteration 3:**
-   Edge `(0, 2, 3)`. `find(0)=2`, `find(2)=2`. Same. Skip.

**Result:** 3.

## ✅ Proof of Correctness

Kruskal's algorithm is based on the **Cut Property**: For any cut (a partition of the vertices into two disjoint sets), if an edge has the minimum weight among all edges crossing the cut, then this edge belongs to some MST. Kruskal's effectively picks the minimum weight edge crossing the cut between two currently disconnected components at each step.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Prim's Algorithm:** Another MST algorithm. Better for dense graphs (O(M + N log N) or O(N^2)).
-   **Maximum Spanning Tree:** Just sort edges in descending order.
-   **Second Best MST:** Find MST, then try swapping one edge out for the next best one.

## Common Mistakes to Avoid

1.  **Not Sorting:** Kruskal's relies entirely on processing edges from smallest to largest.
2.  **Cycle Detection:** Using DFS/BFS for cycle detection is O(N) per edge, making the total O(M*N). DSU is O(M α(N)), which is much faster.
3.  **Disconnected Graph:** If the graph isn't connected, Kruskal's finds a Minimum Spanning *Forest*.
