---
problem_id: AGR_BIPARTITE_MIN_COST_VERTEX_COVER__3406
display_id: AGR-010
slug: bipartite-min-cost-vertex-cover
title: "Minimum Cost Vertex Cover in Bipartite Graph"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Vertex Cover
  - Min Cut
tags:
  - advanced-graphs
  - vertex-cover
  - min-cut
  - medium
premium: true
subscription_tier: basic
---

# AGR-010: Minimum Cost Vertex Cover in Bipartite Graph

## 📋 Problem Summary

Given a bipartite graph where each node has a weight, find a subset of vertices with the minimum total weight such that every edge is incident to at least one vertex in the subset.

## 🌍 Real-World Scenario

**Scenario Title:** Security Camera Placement

Imagine a museum with two rows of rooms (Left and Right).
-   **Edges:** Corridors connecting a room on the Left to a room on the Right.
-   **Goal:** Place security guards to monitor all corridors.
-   **Constraint:** A guard placed in a room can monitor all connected corridors.
-   **Cost:** Hiring a guard for room `i` costs `W[i]`.
-   **Objective:** Minimize the total hiring cost while ensuring every corridor is watched by at least one guard.

![Real-World Application](../images/AGR-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph Construction:**
```
      (wU[0])        (INF)        (wV[0])
  S ------------> U0 -------> V0 ------------> T
                  |
                  | (INF)
                  v
                  V1 ------------> T
                               (wV[1])
```
-   **Source (S):** Connects to all `U` nodes. Capacity `S -> U_i` is `wU[i]`.
-   **Sink (T):** All `V` nodes connect to `T`. Capacity `V_j -> T` is `wV[j]`.
-   **Middle:** Edges `U_i -> V_j` have capacity **Infinity**.

**Min-Cut Interpretation:**
-   A cut partitions nodes into `S-set` (reachable from S) and `T-set` (not reachable).
-   **Cut `S->U_i`:** `U_i` is in `T-set`. Cost `wU[i]`. Represents selecting `U_i`.
-   **Cut `V_j->T`:** `V_j` is in `S-set`. Cost `wV[j]`. Represents selecting `V_j`.
-   **Cut `U_i->V_j`:** Impossible (cost INF). This forces that if `U_i` is in `S-set` (not selected), `V_j` MUST be in `S-set` (selected).
-   **Logic:** For edge `(u, v)`, we cannot leave both `u` unselected (`S-set`) and `v` unselected (`T-set`? No, `V` unselected is `T-set`).
    -   `S->U` cut => `U` in T-side => Selected.
    -   `V->T` cut => `V` in S-side => Selected.
    -   Path `S -> U -> V -> T`.
    -   To break path, must cut `S->U` (select U) OR `V->T` (select V).
    -   Cannot cut `U->V` (INF).
    -   So every edge is covered.

### Algorithm: Min-Cut (Max-Flow)

1.  **Construct Network:**
    -   Source `S`, Sink `T`.
    -   `S -> U_i` with capacity `wU[i]`.
    -   `V_j -> T` with capacity `wV[j]`.
    -   `U_i -> V_j` with capacity `INF` for each graph edge.
2.  **Compute Max Flow:**
    -   By Max-Flow Min-Cut theorem, the max flow value equals the min cut capacity.
    -   This value is exactly the minimum weight vertex cover.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Weights:** Can be 0. Can be large (`10^9`). Use `long`.
-   **INF:** Use a value larger than sum of all weights (e.g., `1e18`).
-   **Output:** Only the cost is required, not the vertices.

## Naive Approach

### Intuition

Try all subsets of vertices (2^N).

### Time Complexity

-   **Exponential**: `O(2^N * M)`. Impossible for N=100,000.

## Optimal Approach (Dinic's Algorithm)

### Time Complexity

-   **O(E * sqrt(V))**: For bipartite matching type graphs (even with weights on source/sink edges, the structure is similar). In general `O(V^2 E)` or `O(VE^2)`, but much faster in practice.

### Space Complexity

-   **O(V + E)**: Graph storage.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        int rev;
        long cap;
        long flow;
        Edge(int to, int rev, long cap) {
            this.to = to;
            this.rev = rev;
            this.cap = cap;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private int[] level;
    private int[] ptr;
    private int N;

    public long minVertexCoverCost(int nU, int nV, long[] wU, long[] wV, int[][] edges) {
        int S = 0;
        int T = nU + nV + 1;
        N = T + 1;
        adj = new ArrayList<>();
        for (int i = 0; i < N; i++) adj.add(new ArrayList<>());

        long INF = 1_000_000_000_000_000_000L; // 1e18

        // S -> U
        for (int i = 0; i < nU; i++) {
            addEdge(S, i + 1, wU[i]);
        }

        // V -> T
        for (int i = 0; i < nV; i++) {
            addEdge(nU + 1 + i, T, wV[i]);
        }

        // U -> V
        for (int[] e : edges) {
            int u = e[0] + 1;
            int v = nU + 1 + e[1];
            addEdge(u, v, INF);
        }

        return dinic(S, T);
    }

    private void addEdge(int from, int to, long cap) {
        Edge a = new Edge(to, adj.get(to).size(), cap);
        Edge b = new Edge(from, adj.get(from).size(), 0);
        adj.get(from).add(a);
        adj.get(to).add(b);
    }

    private boolean bfs(int s, int t) {
        level = new int[N];
        Arrays.fill(level, -1);
        level[s] = 0;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (Edge e : adj.get(u)) {
                if (e.cap - e.flow > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.add(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    private long dfs(int u, int t, long pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (; ptr[u] < adj.get(u).size(); ptr[u]++) {
            Edge e = adj.get(u).get(ptr[u]);
            if (level[u] + 1 != level[e.to] || e.cap - e.flow == 0) continue;
            long tr = dfs(e.to, t, Math.min(pushed, e.cap - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj.get(e.to).get(e.rev).flow -= tr;
            return tr;
        }
        return 0;
    }

    private long dinic(int s, int t) {
        long flow = 0;
        while (bfs(s, t)) {
            ptr = new int[N];
            while (true) {
                long pushed = dfs(s, t, Long.MAX_VALUE);
                if (pushed == 0) break;
                flow += pushed;
            }
        }
        return flow;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int nU = sc.nextInt();
        int nV = sc.nextInt();
        int m = sc.nextInt();
        long[] wU = new long[nU];
        long[] wV = new long[nV];
        for (int i = 0; i < nU; i++) wU[i] = sc.nextLong();
        for (int i = 0; i < nV; i++) wV[i] = sc.nextLong();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.minVertexCoverCost(nU, nV, wU, wV, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, flow, ptr):
        if u == t or flow == 0:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f

def min_vertex_cover_cost(nU: int, nV: int, wU: list[int], wV: list[int], edges: list[tuple[int, int]]) -> int:
    S = 0
    T = nU + nV + 1
    dinic = Dinic(T + 1)
    INF = 10**18
    
    for i, w in enumerate(wU):
        dinic.add_edge(S, i + 1, w)
        
    for i, w in enumerate(wV):
        dinic.add_edge(nU + 1 + i, T, w)
        
    for u, v in edges:
        dinic.add_edge(u + 1, nU + 1 + v, INF)
        
    return dinic.max_flow(S, T)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        nU = int(next(iterator))
        nV = int(next(iterator))
        m = int(next(iterator))
        wU = [int(next(iterator)) for _ in range(nU)]
        wV = [int(next(iterator)) for _ in range(nV)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print(min_vertex_cover_cost(nU, nV, wU, wV, edges))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

class Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

public:
    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void addEdge(int from, int to, long long cap) {
        Edge a = {to, cap, 0, (int)adj[to].size()};
        Edge b = {from, 0, 0, (int)adj[from].size()};
        adj[from].push_back(a);
        adj[to].push_back(b);
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (const auto& e : adj[u]) {
                if (e.cap - e.flow > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int u, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (int& cid = ptr[u]; cid < adj[u].size(); ++cid) {
            auto& e = adj[u][cid];
            int tr = e.to;
            if (level[u] + 1 != level[tr] || e.cap - e.flow == 0) continue;
            long long push = dfs(tr, t, min(pushed, e.cap - e.flow));
            if (push == 0) continue;
            e.flow += push;
            adj[tr][e.rev].flow -= push;
            return push;
        }
        return 0;
    }

    long long maxFlow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

class Solution {
public:
    long long minVertexCoverCost(int nU, int nV, const vector<long long>& wU,
                                 const vector<long long>& wV, const vector<pair<int, int>>& edges) {
        int S = 0;
        int T = nU + nV + 1;
        Dinic dinic(T + 1);

        for (int i = 0; i < nU; i++) {
            dinic.addEdge(S, i + 1, wU[i]);
        }
        for (int i = 0; i < nV; i++) {
            dinic.addEdge(nU + 1 + i, T, wV[i]);
        }
        for (const auto& e : edges) {
            dinic.addEdge(e.first + 1, nU + 1 + e.second, INF);
        }

        return dinic.maxFlow(S, T);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int nU, nV, m;
    if (!(cin >> nU >> nV >> m)) return 0;
    vector<long long> wU(nU), wV(nV);
    for (int i = 0; i < nU; i++) cin >> wU[i];
    for (int i = 0; i < nV; i++) cin >> wV[i];
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << solution.minVertexCoverCost(nU, nV, wU, wV, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Dinic {
  constructor(n) {
    this.n = n;
    this.graph = Array.from({ length: n }, () => []);
    this.level = new Int32Array(n);
  }

  addEdge(u, v, cap) {
    this.graph[u].push({ to: v, cap: BigInt(cap), flow: 0n, rev: this.graph[v].length });
    this.graph[v].push({ to: u, cap: 0n, flow: 0n, rev: this.graph[u].length - 1 });
  }

  bfs(s, t) {
    this.level.fill(-1);
    this.level[s] = 0;
    const queue = [s];
    let head = 0;
    while (head < queue.length) {
      const u = queue[head++];
      for (const edge of this.graph[u]) {
        if (edge.cap - edge.flow > 0n && this.level[edge.to] === -1) {
          this.level[edge.to] = this.level[u] + 1;
          queue.push(edge.to);
        }
      }
    }
    return this.level[t] !== -1;
  }

  dfs(u, t, pushed, ptr) {
    if (pushed === 0n || u === t) return pushed;
    for (let i = ptr[u]; i < this.graph[u].length; i++) {
      ptr[u] = i;
      const edge = this.graph[u][i];
      if (this.level[u] + 1 !== this.level[edge.to] || edge.cap - edge.flow === 0n) continue;
      
      let tr = pushed < (edge.cap - edge.flow) ? pushed : (edge.cap - edge.flow);
      const push = this.dfs(edge.to, t, tr, ptr);
      
      if (push === 0n) continue;
      
      edge.flow += push;
      this.graph[edge.to][edge.rev].flow -= push;
      return push;
    }
    return 0n;
  }

  maxFlow(s, t) {
    let flow = 0n;
    while (this.bfs(s, t)) {
      const ptr = new Int32Array(this.n).fill(0);
      while (true) {
        const pushed = this.dfs(s, t, 1000000000000000000n, ptr);
        if (pushed === 0n) break;
        flow += pushed;
      }
    }
    return flow;
  }
}

class Solution {
  minVertexCoverCost(nU, nV, wU, wV, edges) {
    const S = 0;
    const T = nU + nV + 1;
    const dinic = new Dinic(T + 1);
    const INF = 1000000000000000000n; // 1e18

    for (let i = 0; i < nU; i++) {
      dinic.addEdge(S, i + 1, wU[i]);
    }
    for (let i = 0; i < nV; i++) {
      dinic.addEdge(nU + 1 + i, T, wV[i]);
    }
    for (const [u, v] of edges) {
      dinic.addEdge(u + 1, nU + 1 + v, INF);
    }

    return dinic.maxFlow(S, T);
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
  const nU = parseInt(data[idx++], 10);
  const nV = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const wU = [];
  const wV = [];
  for (let i = 0; i < nU; i++) wU.push(parseInt(data[idx++], 10));
  for (let i = 0; i < nV; i++) wV.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.minVertexCoverCost(nU, nV, wU, wV, edges).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 2 3
3 1
2 2
0 0
1 0
1 1
```
-   `wU = [3, 1]`. `wV = [2, 2]`.
-   Edges: `0->0`, `1->0`, `1->1`.

**Graph:**
-   `S->U0` (3), `S->U1` (1).
-   `V0->T` (2), `V1->T` (2).
-   `U0->V0` (INF), `U1->V0` (INF), `U1->V1` (INF).

**Flow:**
1.  Path `S -> U1 -> V0 -> T`.
    -   Bottleneck: `min(1, INF, 2) = 1`.
    -   Flow += 1. `S->U1` full. `V0->T` used 1/2.
2.  Path `S -> U0 -> V0 -> T`.
    -   Bottleneck: `min(3, INF, 2-1) = 1`.
    -   Flow += 1. `S->U0` used 1/3. `V0->T` full.
3.  Path `S -> U0 -> V0 (blocked) ...`
    -   `S -> U0 -> V0` blocked.
    -   `S -> U1` blocked.
    -   `S -> U0 -> ??` (U0 only connects to V0).
    -   Max Flow = 2?
    -   Wait. Is there another path?
    -   `U1->V1`? `S->U1` is full.
    -   Can we redirect?
    -   If we push 1 through `S->U1->V1->T`.
    -   Then `S->U1` is full.
    -   Then `S->U0->V0->T` takes 2.
    -   Total 3.
    -   Let's check cuts.
    -   Cut `S->U1` (1) and `V0->T` (2). Total 3.
    -   Edges covered:
        -   `0->0`: covered by V0.
        -   `1->0`: covered by U1 and V0.
        -   `1->1`: covered by U1.
    -   Valid cover. Cost 3.
    -   Can we do better?
    -   Cover `U0` (3) and `U1` (1)? Cost 4.
    -   Cover `V0` (2) and `V1` (2)? Cost 4.
    -   Cover `U1` (1) and `V1` (2)? `0->0` not covered.
    -   Min cost is 3.

**Result:** 3. Correct.

## ✅ Proof of Correctness

-   **Kőnig's Theorem:** For unweighted bipartite graphs, Min Vertex Cover = Max Matching.
-   **Weighted Extension:** Min Weight Vertex Cover = Min Cut in the constructed network.
-   **Min-Cut Max-Flow:** We solve Min Cut using Max Flow.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Maximum Independent Set:** In bipartite graphs, Max Independent Set = Total Weight - Min Vertex Cover.
-   **General Graphs:** Vertex Cover is NP-Hard. Bipartite property is crucial.
-   **Recovering Solution:** To find the actual vertices, find the Min Cut partition (reachable from S in residual graph). `U_i` selected if `U_i` NOT reachable. `V_j` selected if `V_j` reachable.

### C++ommon Mistakes to Avoid

1.  **INF Capacity:** Must be larger than sum of all weights.
2.  **Graph Direction:** `S->U`, `U->V`, `V->T`. All directed.
3.  **Zero Weights:** Algorithm works fine with zero weights (just 0 capacity edges).
