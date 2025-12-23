---
problem_id: AGR_BIPARTITE_MATCHING_NODE_CAPACITY__8194
display_id: AGR-009
slug: bipartite-matching-node-capacity
title: "Maximum Matching with Node Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Bipartite Matching
  - Max Flow
tags:
  - advanced-graphs
  - bipartite-matching
  - max-flow
  - medium
premium: true
subscription_tier: basic
---

# AGR-009: Maximum Matching with Node Capacities

## 📋 Problem Summary

Find the maximum number of edges we can select in a bipartite graph such that each node `u` in the left set is incident to at most `capU[u]` selected edges, and each node `v` in the right set is incident to at most `capV[v]` selected edges.

## 🌍 Real-World Scenario

**Scenario Title:** Job Fair Hiring

Imagine a job fair with Candidates (Left) and Companies (Right).
-   **Candidates:** Each candidate `u` can accept up to `capU[u]` job offers (for example, multiple part-time gigs).
-   **Companies:** Each company `v` has `capV[v]` open positions.
-   **Edges:** Valid applications/interviews.
-   **Goal:** Maximize the total number of job placements.

![Real-World Application](../images/AGR-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph Construction:**
```
      (capU[0])        (1)        (capV[0])
  S ------------> U0 -------> V0 ------------> T
                  |
                  | (1)
                  v
                  V1 ------------> T
                               (capV[1])
```
-   **Source (S):** Connects to all `U` nodes. Edge capacity `S -> U_i` is `capU[i]`.
-   **Sink (T):** All `V` nodes connect to `T`. Edge capacity `V_j -> T` is `capV[j]`.
-   **Middle:** Original edges `U_i -> V_j` have capacity 1 (since each specific job-candidate pair happens once).

### Algorithm: Max Flow (Dinic's Algorithm)

1.  **Construct Network:**
    -   Create a source node `S` and sink node `T`.
    -   Add edges `S -> u` with capacity `capU[u]`.
    -   Add edges `v -> T` with capacity `capV[v]`.
    -   For every edge `u-v` in input, add directed edge `u -> v` with capacity 1.
2.  **Run Max Flow:**
    -   The maximum flow from `S` to `T` corresponds exactly to the maximum matching size.
    -   Flow conservation ensures node capacities are respected.
    -   Integrality theorem ensures we can find an integer flow (matching).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Capacities:** Can be large (`10^9`), so use `long` (64-bit integer) for flow.
-   **Node Indexing:** Input gives `u` (0 to nU-1) and `v` (0 to nV-1). In the flow graph, you can map them to `1..nU` and `nU+1..nU+nV`.
-   **Multiple Edges:** If input contains duplicate `u-v` edges, they are effectively parallel edges with capacity 1 each (total capacity > 1). Usually, matching implies unique edges, but if "multigraph" is allowed, just sum capacities. Standard assumption: simple graph, capacity 1 per pair.

## Naive Approach

### Intuition

Greedy matching? Sort by capacity?

### Failure Case

Greedy often fails in flow problems. Taking an edge can block a better path that satisfies more demand.

## Optimal Approach (Dinic's Algorithm)

### Time Complexity

-   **O(E * sqrt(V))**: For unit networks (simple bipartite matching), Dinic is `O(E * sqrt(V))`. Here, capacities are not 1, but the "middle" edges are unit capacity. The complexity is generally bounded by `O(E * sqrt(V))` or `O(V * E)` depending on implementation details, which is fast enough for V, E ~ 200,000.

### Space Complexity

-   **O(V + E)**: To store the graph.

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

    public long maxMatching(int nU, int nV, int[] capU, int[] capV, int[][] edges) {
        int S = 0;
        int T = nU + nV + 1;
        N = T + 1;
        adj = new ArrayList<>();
        for (int i = 0; i < N; i++) adj.add(new ArrayList<>());

        // S -> U
        for (int i = 0; i < nU; i++) {
            addEdge(S, i + 1, capU[i]);
        }

        // V -> T
        for (int i = 0; i < nV; i++) {
            addEdge(nU + 1 + i, T, capV[i]);
        }

        // U -> V
        for (int[] e : edges) {
            int u = e[0] + 1;
            int v = nU + 1 + e[1];
            addEdge(u, v, 1);
        }

        return dinic(S, T);
    }

    private void addEdge(int from, int to, long cap) {
        Edge a = new Edge(to, adj.get(to).size(), cap);
        Edge b = new Edge(from, adj.get(from).size(), 0); // Back edge cap 0
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
        int[] capU = new int[nU];
        int[] capV = new int[nV];
        for (int i = 0; i < nU; i++) capU[i] = sc.nextInt();
        for (int i = 0; i < nV; i++) capV[i] = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxMatching(nU, nV, capU, capV, edges));
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

def max_matching(nU: int, nV: int, capU: list[int], capV: list[int], edges: list[tuple[int, int]]) -> int:
    S = 0
    T = nU + nV + 1
    dinic = Dinic(T + 1)
    
    for i, cap in enumerate(capU):
        dinic.add_edge(S, i + 1, cap)
        
    for i, cap in enumerate(capV):
        dinic.add_edge(nU + 1 + i, T, cap)
        
    for u, v in edges:
        dinic.add_edge(u + 1, nU + 1 + v, 1)
        
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
        capU = [int(next(iterator)) for _ in range(nU)]
        capV = [int(next(iterator)) for _ in range(nV)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print(max_matching(nU, nV, capU, capV, edges))
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
    long long maxMatching(int nU, int nV, const vector<int>& capU,
                          const vector<int>& capV, const vector<pair<int, int>>& edges) {
        int S = 0;
        int T = nU + nV + 1;
        Dinic dinic(T + 1);

        for (int i = 0; i < nU; i++) {
            dinic.addEdge(S, i + 1, capU[i]);
        }
        for (int i = 0; i < nV; i++) {
            dinic.addEdge(nU + 1 + i, T, capV[i]);
        }
        for (const auto& e : edges) {
            dinic.addEdge(e.first + 1, nU + 1 + e.second, 1);
        }

        return dinic.maxFlow(S, T);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int nU, nV, m;
    if (!(cin >> nU >> nV >> m)) return 0;
    vector<int> capU(nU), capV(nV);
    for (int i = 0; i < nU; i++) cin >> capU[i];
    for (int i = 0; i < nV; i++) cin >> capV[i];
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << solution.maxMatching(nU, nV, capU, capV, edges) << "\n";
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
    // Forward edge: [to, cap, flow, rev_index]
    // We store flow directly in the object or array
    // Using object for clarity, but array is faster.
    // [to, cap, flow, rev]
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
        const pushed = this.dfs(s, t, 1000000000000000000n, ptr); // Large BigInt
        if (pushed === 0n) break;
        flow += pushed;
      }
    }
    return flow;
  }
}

class Solution {
  maxMatching(nU, nV, capU, capV, edges) {
    const S = 0;
    const T = nU + nV + 1;
    const dinic = new Dinic(T + 1);

    for (let i = 0; i < nU; i++) {
      dinic.addEdge(S, i + 1, capU[i]);
    }
    for (let i = 0; i < nV; i++) {
      dinic.addEdge(nU + 1 + i, T, capV[i]);
    }
    for (const [u, v] of edges) {
      dinic.addEdge(u + 1, nU + 1 + v, 1);
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
  const capU = [];
  const capV = [];
  for (let i = 0; i < nU; i++) capU.push(parseInt(data[idx++], 10));
  for (let i = 0; i < nV; i++) capV.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxMatching(nU, nV, capU, capV, edges).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 2 3
1 2
1 1
0 0
1 0
1 1
```
-   `nU=2, nV=2`.
-   `capU = [1, 2]`. `capV = [1, 1]`.
-   Edges: `0->0`, `1->0`, `1->1`.

**Graph:**
-   `S -> U0` (cap 1)
-   `S -> U1` (cap 2)
-   `U0 -> V0` (cap 1)
-   `U1 -> V0` (cap 1)
-   `U1 -> V1` (cap 1)
-   `V0 -> T` (cap 1)
-   `V1 -> T` (cap 1)

**Flow:**
1.  Path `S -> U0 -> V0 -> T`. Flow 1.
    -   `S->U0` full. `V0->T` full.
2.  Path `S -> U1 -> V1 -> T`. Flow 1.
    -   `S->U1` used 1/2. `V1->T` full.
3.  Any other path?
    -   `S -> U1 -> V0` blocked (V0->T full).
    -   `S -> U0` blocked.
    -   Max Flow = 2.

**Result:** 2. Correct.

## ✅ Proof of Correctness

-   **Reduction:** This is a standard reduction from Bipartite Matching to Max Flow.
-   **Capacities:** The capacities on `S->U` and `V->T` enforce the node constraints. The capacity 1 on `U->V` ensures each edge is used at most once.
-   **Integrality:** Since all capacities are integers, Max Flow guarantees an integer solution.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Min Cost Max Flow:** If edges have costs (e.g., hiring cost), use MCMF.
-   **Dynamic Matching:** If edges are added/removed, can we update flow? (Yes, dynamic graph algorithms).
-   **Hopcroft-Karp:** For standard bipartite matching (all caps 1), Hopcroft-Karp is `O(E sqrt(V))`, which is essentially Dinic on unit networks.

### Common Mistakes to Avoid

1.  **Node Indexing:** Ensure U and V nodes don't collide. Offset V indices by `nU`.
2.  **Capacity Overflow:** Use `long long` (Java `long`, JS `BigInt`) for flow variables, even if capacities fit in int, total flow can exceed int (though here max flow <= M).
3.  **Infinite Loops:** In DFS, ensure `level[v] == level[u] + 1` check is strict to avoid cycles (though BFS levels prevent this).
