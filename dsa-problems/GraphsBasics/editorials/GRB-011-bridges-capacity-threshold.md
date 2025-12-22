---
problem_id: GRB_BRIDGES_CAPACITY_THRESHOLD__4509
display_id: GRB-011
slug: bridges-capacity-threshold
title: "Bridges With Capacity Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Graphs
  - Bridges
  - DFS
tags:
  - graphs-basics
  - bridges
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# GRB-011: Bridges With Capacity Threshold

## 📋 Problem Summary

You are given an undirected graph where each edge has a **capacity**. You need to find all edges that are **critical**. An edge is critical if:
1.  It is a **Bridge** (removing it disconnects the graph).
2.  Its capacity is strictly less than a threshold `T`.

Return these edges in the order they appear in the input.

## 🌍 Real-World Scenario

**Scenario Title:** Supply Chain Bottlenecks

Imagine a logistics network where trucks deliver goods between warehouses.
-   **Nodes** are warehouses.
-   **Edges** are roads.
-   **Capacity** is the max weight a road can handle.
-   **Bridge:** A road is a "bridge" if it's the *only* way to get from one group of warehouses to another. If this road collapses, the network is split.
-   **Threshold:** You have a heavy shipment of weight `T`.
-   **Critical Edge:** A road that is both vital (a bridge) AND too weak to support your shipment (capacity < T). These are the bottlenecks you must upgrade immediately.

![Real-World Application](../images/GRB-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (5)
  0 ------- 1
  | \       |
  |  \ (2)  | (5)
  |   \     |
 (5)   \    |
  |     \   |
  3 ------- 2
      (1)
```
**Threshold T = 3**

**Bridges:**
-   Edges in cycle `0-1-2-0` are NOT bridges.
-   Edge `(2,3)` connects the cycle to node 3. It IS a bridge.

**Capacities:**
-   Edges `(0,1), (0,2), (1,2), (0,3)` have capacities >= 3. Not critical.
-   Edge `(2,3)` has capacity 1. `1 < 3`.

**Result:** Edge `(2,3)` is critical.

### Algorithm Steps

1.  **Identify Bridges:** Use Tarjan's Bridge-Finding Algorithm (DFS with `discovery_time` and `low_link`).
    -   `disc[u]`: Time when `u` was first visited.
    -   `low[u]`: Lowest `disc` value reachable from `u` (including back-edges).
    -   Edge `(u, v)` is a bridge if `low[v] > disc[u]`.
2.  **Filter by Capacity:**
    -   While running the algorithm, if we identify `(u, v)` as a bridge, check if `capacity < T`.
    -   If yes, mark it as critical.
3.  **Maintain Order:**
    -   The problem requires output in input order.
    -   Store the original index of each edge.
    -   Collect indices of critical edges, sort them, and then output the corresponding `u v`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Input Order:** Output must preserve the relative order of edges from the input.
-   **Multiple Edges:** The problem implies a simple graph or standard multigraph handling. Tarjan's handles multigraphs if implemented carefully (don't go back to parent via the *same* edge index).
-   **Disconnected Graph:** Handle all components.

## Naive Approach

### Intuition

For every edge:
1.  Temporarily remove it.
2.  Run BFS/DFS to check connectivity.
3.  If disconnected AND capacity < T, add to result.

### Time Complexity

-   **O(M * (N + M))**: Too slow for M=200,000.

## Optimal Approach (Tarjan's Bridge Algorithm)

We find all bridges in a single DFS pass.

### Algorithm Details

1.  `timer = 0`, `disc` array, `low` array.
2.  DFS from each unvisited node.
3.  For edge `u -> v`:
    -   If `v` is parent of `u`, skip.
    -   If `v` is visited: `low[u] = min(low[u], disc[v])`.
    -   If `v` is unvisited:
        -   `dfs(v, u)`
        -   `low[u] = min(low[u], low[v])`
        -   If `low[v] > disc[u]`: **Bridge Found!**
            -   Check capacity. If `< T`, add edge index to a list.

### Handling Parallel Edges
If there are multiple edges between `u` and `v`, only one can be the "parent" edge. The others are back-edges. To handle this robustly, pass the `edgeIndex` of the parent edge to the DFS, not just the `parent` node.

### Time Complexity

-   **O(N + M)**: Single DFS.

### Space Complexity

-   **O(N + M)**: Recursion stack and arrays.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    private int timer;
    private int[] disc, low;
    private List<Integer> criticalIndices;
    
    public List<int[]> criticalEdges(int n, int[][] edges, int T) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int c = edges[i][2];
            adj.get(u).add(new int[]{v, c, i});
            adj.get(v).add(new int[]{u, c, i});
        }

        disc = new int[n];
        low = new int[n];
        Arrays.fill(disc, -1);
        criticalIndices = new ArrayList<>();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1, adj, T);
            }
        }
        
        Collections.sort(criticalIndices);
        
        List<int[]> result = new ArrayList<>();
        for (int idx : criticalIndices) {
            result.add(new int[]{edges[idx][0], edges[idx][1]});
        }
        return result;
    }

    private void dfs(int u, int parentEdgeIdx, List<List<int[]>> adj, int T) {
        disc[u] = low[u] = ++timer;
        
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int cap = edge[1];
            int idx = edge[2];
            
            if (idx == parentEdgeIdx) continue; // Don't go back via same edge
            
            if (disc[v] != -1) {
                low[u] = Math.min(low[u], disc[v]);
            } else {
                dfs(v, idx, adj, T);
                low[u] = Math.min(low[u], low[v]);
                
                if (low[v] > disc[u]) {
                    // Bridge found
                    if (cap < T) {
                        criticalIndices.add(idx);
                    }
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int T = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<int[]> ans = solution.criticalEdges(n, edges, T);
        StringBuilder sb = new StringBuilder();
        sb.append(ans.size()).append('\n');
        for (int[] e : ans) {
            sb.append(e[0]).append(' ').append(e[1]).append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def critical_edges(n: int, edges: list[tuple[int, int, int]], T: int) -> list[tuple[int, int]]:
    adj = [[] for _ in range(n)]
    for i, (u, v, c) in enumerate(edges):
        adj[u].append((v, c, i))
        adj[v].append((u, c, i))
        
    disc = [-1] * n
    low = [-1] * n
    timer = 0
    critical_indices = []
    
    def dfs(u, parent_edge_idx):
        nonlocal timer
        timer += 1
        disc[u] = low[u] = timer
        
        for v, cap, idx in adj[u]:
            if idx == parent_edge_idx:
                continue
            
            if disc[v] != -1:
                low[u] = min(low[u], disc[v])
            else:
                dfs(v, idx)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    if cap < T:
                        critical_indices.append(idx)
                        
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
            
    critical_indices.sort()
    return [(edges[i][0], edges[i][1]) for i in critical_indices]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        T = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
            
        ans = critical_edges(n, edges, T)
        out = [str(len(ans))]
        out += [f"{u} {v}" for (u, v) in ans]
        print("\n".join(out))
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

using namespace std;

class Solution {
    int timer;
    vector<int> disc, low;
    vector<int> criticalIndices;
    vector<vector<array<int, 3>>> adj; // {v, cap, idx}

    void dfs(int u, int parentEdgeIdx, int T) {
        disc[u] = low[u] = ++timer;

        for (auto& edge : adj[u]) {
            int v = edge[0];
            int cap = edge[1];
            int idx = edge[2];

            if (idx == parentEdgeIdx) continue;

            if (disc[v] != -1) {
                low[u] = min(low[u], disc[v]);
            } else {
                dfs(v, idx, T);
                low[u] = min(low[u], low[v]);

                if (low[v] > disc[u]) {
                    if (cap < T) {
                        criticalIndices.push_back(idx);
                    }
                }
            }
        }
    }

public:
    vector<pair<int, int>> criticalEdges(int n, const vector<array<int, 3>>& edges, int T) {
        adj.assign(n, vector<array<int, 3>>());
        for (int i = 0; i < edges.size(); i++) {
            adj[edges[i][0]].push_back({edges[i][1], edges[i][2], i});
            adj[edges[i][1]].push_back({edges[i][0], edges[i][2], i});
        }

        disc.assign(n, -1);
        low.assign(n, -1);
        criticalIndices.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1, T);
            }
        }

        sort(criticalIndices.begin(), criticalIndices.end());

        vector<pair<int, int>> result;
        for (int idx : criticalIndices) {
            result.push_back({edges[idx][0], edges[idx][1]});
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, T;
    if (!(cin >> n >> m >> T)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<pair<int, int>> ans = solution.criticalEdges(n, edges, T);
    cout << ans.size() << "\n";
    for (auto& e : ans) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  criticalEdges(n, edges, T) {
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
      const [u, v, c] = edges[i];
      adj[u].push({ v, c, idx: i });
      adj[v].push({ u, c, idx: i });
    }

    const disc = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const criticalIndices = [];
    let timer = 0;

    // Use explicit stack for iterative DFS to avoid recursion limit
    // However, Tarjan's is tricky to implement iteratively because of the post-order update low[u] = min(low[u], low[v])
    // We'll use recursion but note the limit. For competitive JS, recursion is usually fine up to 10^4-10^5 depending on engine.
    // If stack overflow occurs, we need a manual stack simulation.
    
    const dfs = (u, parentEdgeIdx) => {
      disc[u] = low[u] = ++timer;
      
      for (const { v, c, idx } of adj[u]) {
        if (idx === parentEdgeIdx) continue;
        
        if (disc[v] !== -1) {
          low[u] = Math.min(low[u], disc[v]);
        } else {
          dfs(v, idx);
          low[u] = Math.min(low[u], low[v]);
          
          if (low[v] > disc[u]) {
            if (c < T) {
              criticalIndices.push(idx);
            }
          }
        }
      }
    };

    for (let i = 0; i < n; i++) {
      if (disc[i] === -1) {
        dfs(i, -1);
      }
    }

    criticalIndices.sort((a, b) => a - b);
    return criticalIndices.map((idx) => [edges[idx][0], edges[idx][1]]);
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
  const T = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  const ans = solution.criticalEdges(n, edges, T);
  const out = [ans.length.toString(), ...ans.map((e) => `${e[0]} ${e[1]}`)];
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4 3
0 1 1
1 2 5
2 0 1
1 3 2
```
**Edges:**
0. `(0, 1, 1)`
1. `(1, 2, 5)`
2. `(2, 0, 1)`
3. `(1, 3, 2)`

**DFS(0):**
-   `disc[0]=1, low[0]=1`.
-   **Neighbor 1 (Edge 0):**
    -   `dfs(1, 0)`. `disc[1]=2, low[1]=2`.
    -   **Neighbor 2 (Edge 1):**
        -   `dfs(2, 1)`. `disc[2]=3, low[2]=3`.
        -   **Neighbor 0 (Edge 2):**
            -   Visited. `low[2] = min(3, disc[0]=1) = 1`.
        -   Back to 1. `low[1] = min(2, low[2]=1) = 1`.
    -   **Neighbor 3 (Edge 3):**
        -   `dfs(3, 3)`. `disc[3]=4, low[3]=4`.
        -   No neighbors.
        -   Back to 1. `low[1] = min(1, low[3]=4) = 1`.
        -   Check Bridge: `low[3] (4) > disc[1] (2)`. **Bridge!**
        -   Check Cap: `cap=2 < T=3`. **Critical!** Add index 3.
    -   Back to 0. `low[0] = min(1, low[1]=1) = 1`.

**Result:** Index 3 -> Edge `(1, 3)`.

## ✅ Proof of Correctness

1.  **Bridge Property:** `low[v] > disc[u]` implies there is no back-edge from `v` or its descendants to `u` or its ancestors. Thus, `(u, v)` is the only path.
2.  **Capacity Check:** We strictly follow the problem statement: if it's a bridge AND capacity < T.
3.  **Ordering:** We store indices and sort them at the end, ensuring input order is preserved.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Dynamic Bridges:** How to maintain bridges if edges are added/removed? (Link-Cut Trees or dynamic graph algorithms).
-   **2-Edge-Connected Components:** Condense the graph by shrinking all cycles. The remaining edges are bridges.

### C++ommon Mistakes to Avoid

1.  **Parent Node vs Parent Edge:** In multigraphs (parallel edges), checking `v != parent` is insufficient. You must check `edgeIndex != parentEdgeIndex`.
2.  **Sorting Output:** The problem asks for edges in input order. Don't just print them as you find them (DFS order != Input order).
3.  **Capacity Threshold:** Ensure strict inequality `< T` vs `<= T` based on problem statement.
