---
problem_id: AGR_APSP_WITH_NEGATIVES__6027
display_id: AGR-004
slug: apsp-with-negatives
title: "All-Pairs Shortest Path With Negative Edges"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - APSP
  - Johnson
tags:
  - advanced-graphs
  - apsp
  - johnson
  - medium
premium: true
subscription_tier: basic
---

# AGR-004: All-Pairs Shortest Path With Negative Edges

## 📋 Problem Summary

Compute the shortest path distance between **every pair of nodes** in a graph that may contain **negative edge weights** (but no negative cycles).

## 🌍 Real-World Scenario

**Scenario Title:** Terrain Hiking with Energy

Imagine hiking on a terrain.
-   **Positive Edge:** Walking uphill consumes energy (cost > 0).
-   **Negative Edge:** Walking downhill recovers energy (cost < 0, or "gain").
-   **Goal:** Find the minimum energy required to get from any point A to any point B.
-   **Challenge:** Since "downhill" edges exist, standard Dijkstra doesn't work. Since the map is huge (2000 points), Floyd-Warshall is too slow. We need a smarter approach.

![Real-World Application](../images/AGR-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (2)
  A --------> B
  |           |
  | (4)       | (-5)
  v           v
  C <-------- D
      (1)
```
**Reweighting (Johnson's Idea):**
We want to transform edge weights to be non-negative so we can use Dijkstra.
-   Assign a "potential" `h[u]` to each node.
-   New weight `w'(u, v) = w(u, v) + h[u] - h[v]`.
-   Telescoping sum: Path cost `A -> ... -> Z` becomes `OriginalCost + h[A] - h[Z]`.
-   If we pick `h` correctly (using Bellman-Ford), all `w'(u, v) >= 0`.

### Algorithm: Johnson's Algorithm

1.  **Add Virtual Source:** Add node `S` with edges `S -> u` (weight 0) for all `u`.
2.  **Compute Potentials:** Run **Bellman-Ford** from `S`. The shortest path distance to `u` becomes `h[u]`.
    -   If Bellman-Ford detects a negative cycle, stop (though problem says none exist).
3.  **Reweight Edges:** `w_new(u, v) = w_old(u, v) + h[u] - h[v]`.
    -   Property: `w_new` is always >= 0.
4.  **Run Dijkstra:** For every node `u`, run Dijkstra using `w_new` to find distances to all `v`.
5.  **Adjust Distances:** `TrueDist(u, v) = DijkstraDist(u, v) - h[u] + h[v]`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **INF:** Use a large number (e.g., `1e18`) for unreachable nodes.
-   **Output:** Print "INF" string for infinity.
-   **Constraints:** N=2000. Floyd-Warshall (O(N^3)) is too slow. Johnson's (O(NM log N)) is required.

## Naive Approach

### Intuition

Run Bellman-Ford from every node.

### Time Complexity

-   **O(N * N * M)**: `2000 * 2000 * 5000` is huge. TLE.

## Optimal Approach (Johnson's Algorithm)

### Time Complexity

-   **O(N * M log N)**: Bellman-Ford takes O(NM). N Dijkstras take O(N * M log N). Total fits in 2s.

### Space Complexity

-   **O(N + M)**: Adjacency list.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        long weight;
        Edge(int to, long weight) { this.to = to; this.weight = weight; }
    }

    public long[][] allPairsShortestPaths(int n, int[][] edges) {
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new Edge(e[1], e[2]));
        }

        long INF = 1_000_000_000_000_000_000L; // 1e18

        // 1. Bellman-Ford to find potentials h[]
        // Virtual source connected to all nodes with 0 weight
        long[] h = new long[n + 1];
        Arrays.fill(h, INF);
        h[n] = 0; // Virtual source index n
        
        // We don't explicitly add node n to adj, we just simulate edges n->i
        // Edges: original edges + (n, i, 0) for all i
        
        boolean changed = true;
        for (int i = 0; i < n; i++) { // n+1 nodes, so n iterations
            changed = false;
            // Edges from virtual source
            for (int u = 0; u < n; u++) {
                if (h[n] + 0 < h[u]) {
                    h[u] = h[n] + 0;
                    changed = true;
                }
            }
            // Original edges
            for (int u = 0; u < n; u++) {
                if (h[u] == INF) continue;
                for (Edge e : adj.get(u)) {
                    if (h[u] + e.weight < h[e.to]) {
                        h[e.to] = h[u] + e.weight;
                        changed = true;
                    }
                }
            }
            if (!changed) break;
        }

        // 2. Reweight edges
        // w'(u,v) = w(u,v) + h[u] - h[v]
        // We compute this on the fly during Dijkstra

        long[][] result = new long[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(result[i], INF);

        // 3. Run Dijkstra from each node
        for (int s = 0; s < n; s++) {
            PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
            long[] d = new long[n];
            Arrays.fill(d, INF);
            
            d[s] = 0;
            pq.add(new long[]{0, s});

            while (!pq.isEmpty()) {
                long[] top = pq.poll();
                long distU = top[0];
                int u = (int) top[1];

                if (distU > d[u]) continue;

                for (Edge e : adj.get(u)) {
                    long newWeight = e.weight + h[u] - h[e.to];
                    if (d[u] + newWeight < d[e.to]) {
                        d[e.to] = d[u] + newWeight;
                        pq.add(new long[]{d[e.to], e.to});
                    }
                }
            }

            // 4. Adjust distances back
            for (int v = 0; v < n; v++) {
                if (d[v] != INF) {
                    result[s][v] = d[v] - h[s] + h[v];
                }
            }
        }

        return result;
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
        long[][] dist = solution.allPairsShortestPaths(n, edges);
        long INF = 1_000_000_000_000_000_000L;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j > 0) sb.append(' ');
                if (dist[i][j] >= INF / 2) sb.append("INF");
                else sb.append(dist[i][j]);
            }
            if (i + 1 < n) sb.append('\n');
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def all_pairs_shortest_paths(n: int, edges: list[tuple[int, int, int]]) -> list[list[int]]:
    INF = 10**18
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        
    # 1. Bellman-Ford for potentials h
    # Virtual source n connected to 0..n-1 with weight 0
    h = [INF] * (n + 1)
    h[n] = 0
    
    # We run n iterations (since V=n+1)
    # Edges: original + (n->i w=0)
    # Optimization: first iteration sets h[0..n-1] = 0.
    # So we can just init h[0..n-1] = 0 and run Bellman-Ford on original graph for n-1 times?
    # Yes, because dist(n, u) <= 0.
    # But we must ensure h[u] is correct shortest path from virtual source.
    # If there are negative edges, h[u] can decrease below 0.
    
    h = [0] * (n + 1) # h[n]=0, others 0 initially (since n->i w=0)
    
    for _ in range(n):
        changed = False
        for u, v, w in edges:
            if h[u] + w < h[v]:
                h[v] = h[u] + w
                changed = True
        if not changed:
            break
            
    # 2. Dijkstra from each node
    result = [[INF] * n for _ in range(n)]
    
    for s in range(n):
        d = [INF] * n
        d[s] = 0
        pq = [(0, s)]
        
        while pq:
            dist_u, u = heapq.heappop(pq)
            if dist_u > d[u]: continue
            
            for v, w in adj[u]:
                new_w = w + h[u] - h[v]
                if d[u] + new_w < d[v]:
                    d[v] = d[u] + new_w
                    heapq.heappush(pq, (d[v], v))
                    
        for v in range(n):
            if d[v] != INF:
                result[s][v] = d[v] - h[s] + h[v]
                
    return result

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
            
        dist = all_pairs_shortest_paths(n, edges)
        INF = 10**18
        out = []
        for i in range(n):
            row = []
            for x in dist[i]:
                if x >= INF // 2:
                    row.append("INF")
                else:
                    row.append(str(x))
            out.append(" ".join(row))
        print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

class Solution {
public:
    vector<vector<long long>> allPairsShortestPaths(int n, const vector<array<int, 3>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
        }

        // Bellman-Ford
        vector<long long> h(n + 1, 0); // Virtual source n, connected to all with 0
        // Init h[0..n-1] = 0 is equivalent to 1st iteration of BF from virtual source
        
        for (int i = 0; i < n; i++) {
            bool changed = false;
            for (const auto& e : edges) {
                if (h[e[0]] + e[2] < h[e[1]]) {
                    h[e[1]] = h[e[0]] + e[2];
                    changed = true;
                }
            }
            if (!changed) break;
        }

        vector<vector<long long>> result(n, vector<long long>(n, INF));

        for (int s = 0; s < n; s++) {
            priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
            vector<long long> d(n, INF);

            d[s] = 0;
            pq.push({0, s});

            while (!pq.empty()) {
                long long distU = pq.top().first;
                int u = pq.top().second;
                pq.pop();

                if (distU > d[u]) continue;

                for (const auto& e : adj[u]) {
                    int v = e.first;
                    int w = e.second;
                    long long newWeight = w + h[u] - h[v];
                    if (d[u] + newWeight < d[v]) {
                        d[v] = d[u] + newWeight;
                        pq.push({d[v], v});
                    }
                }
            }

            for (int v = 0; v < n; v++) {
                if (d[v] != INF) {
                    result[s][v] = d[v] - h[s] + h[v];
                }
            }
        }

        return result;
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
    vector<vector<long long>> dist = solution.allPairsShortestPaths(n, edges);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j) cout << ' ';
            if (dist[i][j] >= INF / 2) cout << "INF";
            else cout << dist[i][j];
        }
        if (i + 1 < n) cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(comparator = (a, b) => a - b) {
    this.heap = [];
    this.comparator = comparator;
  }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.heap.length === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.comparator(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const lIdx = 2 * idx + 1;
      const rIdx = 2 * idx + 2;
      let swapIdx = null;
      if (lIdx < this.heap.length && this.comparator(this.heap[lIdx], this.heap[idx]) < 0) swapIdx = lIdx;
      if (rIdx < this.heap.length && this.comparator(this.heap[rIdx], swapIdx === null ? this.heap[idx] : this.heap[swapIdx]) < 0) swapIdx = rIdx;
      if (swapIdx !== null) {
        [this.heap[idx], this.heap[swapIdx]] = [this.heap[swapIdx], this.heap[idx]];
        idx = swapIdx;
      } else break;
    }
  }
}

class Solution {
  allPairsShortestPaths(n, edges) {
    const INF = 1e15;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
      adj[u].push({ to: v, w });
    }

    // 1. Bellman-Ford
    const h = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
      let changed = false;
      for (const [u, v, w] of edges) {
        if (h[u] + w < h[v]) {
          h[v] = h[u] + w;
          changed = true;
        }
      }
      if (!changed) break;
    }

    const result = Array.from({ length: n }, () => new Array(n).fill(INF));

    // 2. Dijkstra
    for (let s = 0; s < n; s++) {
      const d = new Array(n).fill(INF);
      d[s] = 0;
      const pq = new PriorityQueue((a, b) => a.dist - b.dist);
      pq.push({ dist: 0, u: s });

      while (!pq.isEmpty()) {
        const { dist: distU, u } = pq.pop();
        if (distU > d[u]) continue;

        for (const { to: v, w } of adj[u]) {
          const newW = w + h[u] - h[v];
          if (d[u] + newW < d[v]) {
            d[v] = d[u] + newW;
            pq.push({ dist: d[v], u: v });
          }
        }
      }

      for (let v = 0; v < n; v++) {
        if (d[v] !== INF) {
          result[s][v] = d[v] - h[s] + h[v];
        }
      }
    }

    return result;
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
  const dist = solution.allPairsShortestPaths(n, edges);
  const INF = 1e15;
  const out = dist.map((row) => row.map(x => x >= INF / 2 ? "INF" : x).join(" "));
  console.log(out.join("\n"));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1 2
1 2 -1
0 2 4
```
**Bellman-Ford (Potentials h):**
-   Init `h = [0, 0, 0]`.
-   Iter 1:
    -   `0->1 (2)`: `h[1] = min(0, 0+2) = 0`.
    -   `1->2 (-1)`: `h[2] = min(0, 0-1) = -1`.
    -   `0->2 (4)`: `h[2] = min(-1, 0+4) = -1`.
-   `h = [0, 0, -1]`.
-   Iter 2: No changes.

**Reweighted Edges:**
-   `0->1`: `2 + h[0] - h[1] = 2 + 0 - 0 = 2`.
-   `1->2`: `-1 + h[1] - h[2] = -1 + 0 - (-1) = 0`.
-   `0->2`: `4 + h[0] - h[2] = 4 + 0 - (-1) = 5`.

**Dijkstra from 0:**
-   `d[0]=0`.
-   `0->1` (w'=2): `d[1]=2`.
-   `0->2` (w'=5): `d[2]=5`.
-   `1->2` (w'=0): `d[2] = min(5, 2+0) = 2`.
-   Final `d`: `[0, 2, 2]`.
-   Real Dist:
    -   `0->0`: `0 - 0 + 0 = 0`.
    -   `0->1`: `2 - 0 + 0 = 2`.
    -   `0->2`: `2 - 0 + (-1) = 1`.
-   Row 0: `0 2 1`. (Matches example)

## ✅ Proof of Correctness

Johnson's algorithm uses the potential function `h` to reweight edges such that `w'(u,v) >= 0` while preserving shortest paths. `dist'(u,v) = dist(u,v) + h[u] - h[v]`. Since `h` values are fixed, minimizing `dist'` minimizes `dist`. The non-negative weights allow Dijkstra, ensuring efficiency.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Detect Negative Cycle:** If Bellman-Ford step finds a change in the N-th iteration, a negative cycle exists.
-   **SPFA:** Shortest Path Faster Algorithm (queue-based Bellman-Ford) can be used instead of Dijkstra if graph is sparse, but worst case is exponential.
-   **Parallelization:** The N Dijkstra runs are independent and can be parallelized.

### Common Mistakes to Avoid

1.  **INF Value:** Use a large number but not `LLONG_MAX` to avoid overflow when adding weights.
2.  **Bellman-Ford Init:** Initialize `h` to 0 (equivalent to virtual source edges).
3.  **Output Format:** Problem asks for "INF" string, not the number.
