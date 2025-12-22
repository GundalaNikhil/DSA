---
problem_id: AGR_MAX_FLOW_VERTEX_CAPACITY__5913
display_id: AGR-002
slug: max-flow-vertex-capacity
title: "Max Flow With Vertex Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Max Flow
  - Vertex Capacities
tags:
  - advanced-graphs
  - max-flow
  - vertex-capacity
  - medium
premium: true
subscription_tier: basic
---

# AGR-002: Max Flow With Vertex Capacities

## 📋 Problem Summary

Compute the maximum flow in a network where not only edges but also **vertices** have capacity limits. A vertex capacity limits the total flow passing *through* that vertex.

## 🌍 Real-World Scenario

**Scenario Title:** Airport Passenger Throughput

Consider an air travel network:
-   **Edges** are flights. A flight from NYC to London has a capacity (number of seats).
-   **Vertices** are airports.
-   **Vertex Capacity:** Even if there are many incoming and outgoing flights, an airport (e.g., London Heathrow) has a limit on how many passengers it can process per hour (security, customs, baggage).
-   **Goal:** Find the max number of people that can travel from Source to Destination, respecting both flight seats and airport processing limits.

![Real-World Application](../images/AGR-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Original Graph:**
```
      (10)       (10)
  A --------> B --------> C
              ^
              | Cap = 5
```
Node B has a capacity of 5. Even though 10 units enter from A and 10 could leave to C, B can only handle 5.

**Transformed Graph (Vertex Splitting):**
```
      (10)          (5)           (10)
  A --------> B_in -----> B_out --------> C
```
We split B into `B_in` and `B_out`.
-   All incoming edges point to `B_in`.
-   All outgoing edges start from `B_out`.
-   Add a new edge `B_in -> B_out` with capacity equal to B's vertex capacity (5).

Now, standard Max Flow algorithms will naturally respect the vertex limit because all flow through B must pass through the `B_in -> B_out` edge.

### Algorithm Steps

1.  **Graph Transformation:**
    -   For each node `i` (0 to N-1), create two nodes in the new graph: `u_in` (index `2*i`) and `u_out` (index `2*i + 1`).
    -   Add edge `u_in -> u_out` with capacity `cap[i]`. (If `cap[i] == -1`, use Infinity).
    -   For each original edge `u -> v` with capacity `c`:
        -   Add edge `u_out -> v_in` with capacity `c`.
2.  **Run Max Flow:**
    -   Source in new graph: `s_in` (or `s_out`? Usually source has infinite capacity, so `s_in -> s_out` is infinite. We can start flow from `s_in`).
    -   Sink in new graph: `t_out`.
    -   Use **Dinic's Algorithm** (or Edmonds-Karp) to find max flow.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Infinite Capacity:** Input uses `-1`. Treat this as `10^18` (safe large number).
-   **Source/Sink:** The problem says `s` and `t` have unlimited capacity. So `s_in -> s_out` and `t_in -> t_out` should be Infinite.
-   **Node Indexing:** Original `i` maps to `2*i` and `2*i+1`. Total nodes `2*N`.

## Naive Approach

### Intuition

Try to modify the Max Flow algorithm to check vertex capacity every time we push flow. This is complex to implement correctly (need to track vertex usage separately) and error-prone.

## Optimal Approach (Vertex Splitting)

Reducing the problem to standard Max Flow is the cleanest and most robust way.

### Time Complexity

-   **O(V^2 E)**: Dinic's complexity. Here `V' = 2N`, `E' = M + N`. So roughly `O(N^2 (M+N))`. For N=2000, M=5000, this is well within limits (Dinic is usually much faster than worst case).

### Space Complexity

-   **O(N + M)**: To store the transformed graph.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        long capacity;
        long flow;
        int rev; // index of reverse edge

        Edge(int to, long capacity, int rev) {
            this.to = to;
            this.capacity = capacity;
            this.rev = rev;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private int[] level;
    private int[] ptr;

    public long maxFlowVertexCap(int n, int s, int t, long[] cap, int[][] edges) {
        int numNodes = 2 * n;
        int sNode = 2 * s; // Start at s_in
        int tNode = 2 * t + 1; // End at t_out

        adj = new ArrayList<>();
        for (int i = 0; i < numNodes; i++) adj.add(new ArrayList<>());

        long INF = 1_000_000_000_000_000L;

        // 1. Add Vertex Capacity Edges (u_in -> u_out)
        for (int i = 0; i < n; i++) {
            long c = (cap[i] == -1 || i == s || i == t) ? INF : cap[i];
            addEdge(2 * i, 2 * i + 1, c);
        }

        // 2. Add Original Edges (u_out -> v_in)
        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int c = e[2];
            addEdge(2 * u + 1, 2 * v, c);
        }

        // 3. Dinic's Algorithm
        long maxFlow = 0;
        while (bfs(sNode, tNode, numNodes)) {
            ptr = new int[numNodes];
            while (true) {
                long pushed = dfs(sNode, tNode, INF);
                if (pushed == 0) break;
                maxFlow += pushed;
            }
        }

        return maxFlow;
    }

    private void addEdge(int from, int to, long cap) {
        Edge a = new Edge(to, cap, adj.get(to).size());
        Edge b = new Edge(from, 0, adj.get(from).size()); // Residual
        adj.get(from).add(a);
        adj.get(to).add(b);
    }

    private boolean bfs(int s, int t, int n) {
        level = new int[n];
        Arrays.fill(level, -1);
        level[s] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (Edge e : adj.get(u)) {
                if (e.capacity - e.flow > 0 && level[e.to] == -1) {
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
            if (level[u] + 1 != level[e.to] || e.capacity - e.flow == 0) continue;
            long tr = dfs(e.to, t, Math.min(pushed, e.capacity - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj.get(e.to).get(e.rev).flow -= tr;
            return tr;
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        long[] cap = new long[n];
        for (int i = 0; i < n; i++) cap[i] = sc.nextLong();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxFlowVertexCap(n, s, t, cap, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for DFS
sys.setrecursionlimit(200000)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, capacity):
        # Forward edge: [v, capacity, flow, reverse_index]
        # Reverse edge: [u, 0, 0, forward_index]
        self.graph[u].append([v, capacity, 0, len(self.graph[v])])
        self.graph[v].append([u, 0, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, flow, rev in self.graph[u]:
                if cap - flow > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, pushed, ptr):
        if pushed == 0 or u == t:
            return pushed
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, flow, rev = self.graph[u][i]
            if self.level[v] != self.level[u] + 1 or cap - flow == 0:
                continue
            tr = self.dfs(v, t, min(pushed, cap - flow), ptr)
            if tr == 0:
                continue
            self.graph[u][i][2] += tr
            self.graph[v][rev][2] -= tr
            return tr
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                flow += pushed
        return flow

def max_flow_vertex_cap(n: int, s: int, t: int, cap: list[int], edges: list[tuple[int, int, int]]) -> int:
    dinic = Dinic(2 * n)
    INF = 10**15
    
    # Vertex capacities
    for i in range(n):
        c = INF if (cap[i] == -1 or i == s or i == t) else cap[i]
        dinic.add_edge(2 * i, 2 * i + 1, c)
        
    # Edges
    for u, v, c in edges:
        dinic.add_edge(2 * u + 1, 2 * v, c)
        
    return dinic.max_flow(2 * s, 2 * t + 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))
        cap = [int(next(iterator)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
        print(max_flow_vertex_cap(n, s, t, cap, edges))
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

class Solution {
    struct Edge {
        int to;
        long long capacity;
        long long flow;
        int rev;
    };

    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

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
                if (e.capacity - e.flow > 0 && level[e.to] == -1) {
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
            if (level[u] + 1 != level[e.to] || e.capacity - e.flow == 0) continue;
            long long tr = dfs(e.to, t, min(pushed, e.capacity - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj[e.to][e.rev].flow -= tr;
            return tr;
        }
        return 0;
    }

public:
    long long maxFlowVertexCap(int n, int s, int t, const vector<long long>& cap,
                               const vector<array<int, 3>>& edges) {
        int numNodes = 2 * n;
        adj.assign(numNodes, vector<Edge>());
        level.resize(numNodes);
        ptr.resize(numNodes);

        long long INF = 1e15;

        for (int i = 0; i < n; i++) {
            long long c = (cap[i] == -1 || i == s || i == t) ? INF : cap[i];
            addEdge(2 * i, 2 * i + 1, c);
        }

        for (const auto& e : edges) {
            addEdge(2 * e[0] + 1, 2 * e[1], e[2]);
        }

        int sNode = 2 * s;
        int tNode = 2 * t + 1;
        long long maxFlow = 0;

        while (bfs(sNode, tNode)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(sNode, tNode, INF)) {
                maxFlow += pushed;
            }
        }

        return maxFlow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<long long> cap(n);
    for (int i = 0; i < n; i++) cin >> cap[i];
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.maxFlowVertexCap(n, s, t, cap, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxFlowVertexCap(n, s, t, cap, edges) {
    const numNodes = 2 * n;
    const adj = Array.from({ length: numNodes }, () => []);
    
    // Edge structure: [to, capacity, flow, revIndex]
    const addEdge = (from, to, cap) => {
      adj[from].push([to, cap, 0, adj[to].length]);
      adj[to].push([from, 0, 0, adj[from].length - 1]);
    };

    const INF = 1e15;

    // Vertex capacities
    for (let i = 0; i < n; i++) {
      let c = (cap[i] === -1 || i === s || i === t) ? INF : cap[i];
      addEdge(2 * i, 2 * i + 1, c);
    }

    // Edges
    for (const [u, v, c] of edges) {
      addEdge(2 * u + 1, 2 * v, c);
    }

    const sNode = 2 * s;
    const tNode = 2 * t + 1;
    let level = new Int32Array(numNodes);
    let ptr = new Int32Array(numNodes);

    const bfs = () => {
      level.fill(-1);
      level[sNode] = 0;
      const q = [sNode];
      let head = 0;
      while (head < q.length) {
        const u = q[head++];
        for (const [v, cap, flow, rev] of adj[u]) {
          if (cap - flow > 0 && level[v] === -1) {
            level[v] = level[u] + 1;
            q.push(v);
          }
        }
      }
      return level[tNode] !== -1;
    };

    const dfs = (u, pushed) => {
      if (pushed === 0 || u === tNode) return pushed;
      for (let i = ptr[u]; i < adj[u].length; i++) {
        ptr[u] = i;
        const [v, cap, flow, rev] = adj[u][i];
        if (level[u] + 1 !== level[v] || cap - flow === 0) continue;
        const tr = dfs(v, Math.min(pushed, cap - flow));
        if (tr === 0) continue;
        adj[u][i][2] += tr;
        adj[v][rev][2] -= tr;
        return tr;
      }
      return 0;
    };

    let maxFlow = 0;
    while (bfs()) {
      ptr.fill(0);
      while (true) {
        const pushed = dfs(sNode, INF);
        if (pushed === 0) break;
        maxFlow += pushed;
      }
    }

    return maxFlow;
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
  const s = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const cap = [];
  for (let i = 0; i < n; i++) cap.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  console.log(solution.maxFlowVertexCap(n, s, t, cap, edges).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 3 0 3
-1 3 2 -1
0 1 3
1 2 2
2 3 3
```
**Graph Construction:**
-   **Vertices:**
    -   `0_in -> 0_out` (INF)
    -   `1_in -> 1_out` (3)
    -   `2_in -> 2_out` (2)
    -   `3_in -> 3_out` (INF)
-   **Edges:**
    -   `0_out -> 1_in` (3)
    -   `1_out -> 2_in` (2)
    -   `2_out -> 3_in` (3)

**Path:** `0_in -> 0_out -> 1_in -> 1_out -> 2_in -> 2_out -> 3_in -> 3_out`
**Capacities:**
-   `0->0`: INF
-   `0->1`: 3
-   `1->1`: 3
-   `1->2`: 2
-   `2->2`: 2
-   `2->3`: 3
-   `3->3`: INF

**Bottleneck:** `min(INF, 3, 3, 2, 2, 3, INF) = 2`.
**Max Flow:** 2.

## ✅ Proof of Correctness

The construction ensures that any unit of flow passing through node `u` must traverse the edge `u_in -> u_out`. Since this edge has capacity `cap[u]`, the total flow through `u` cannot exceed `cap[u]`. Standard Max Flow correctness applies to the rest.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Min-Cost Max-Flow:** If edges/vertices have costs, use MCMF algorithms (SPFA/Dijkstra with potentials).
-   **Undirected Edges:** Split undirected `u-v` into directed `u->v` and `v->u`.
-   **Dynamic Capacities:** How to update flow if a vertex capacity increases/decreases?

## Common Mistakes to Avoid

1.  **Source/Sink Capacity:** Usually, source and sink are assumed to have infinite capacity unless specified otherwise. Don't accidentally cap them.
2.  **Node Indexing:** Be careful mapping `u` to `2*u` and `2*u+1`.
3.  **Edge Direction:** Original edge `u->v` goes from `u_out` to `v_in`. NOT `u_in` to `v_in`.
