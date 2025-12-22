---
problem_id: AGR_K_EDGE_DISJOINT_PATHS__2167
display_id: AGR-013
slug: k-edge-disjoint-paths
title: "K-Edge-Disjoint Paths"
difficulty: Hard
difficulty_score: 68
topics:
  - Graphs
  - Max Flow
  - Disjoint Paths
tags:
  - advanced-graphs
  - disjoint-paths
  - max-flow
  - hard
premium: true
subscription_tier: basic
---

# AGR-013: K-Edge-Disjoint Paths

## 📋 Problem Summary

Determine if there are at least `k` paths from a source `s` to a sink `t` such that no two paths share an edge.

## 🌍 Real-World Scenario

**Scenario Title:** Redundant Network Routing

In a communication network, reliability is key.
-   **Goal:** Send data packets from Server A to Server B.
-   **Constraint:** If a link fails, we need backup paths.
-   **Requirement:** We want `k` independent paths. If any `k-1` links fail, at least one path remains operational.
-   **Edge-Disjoint:** Paths don't share wires (edges), ensuring failure of one wire doesn't affect others.

![Real-World Application](../images/AGR-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)        (1)
  S --------> A --------> T
  |                       ^
  | (1)                   | (1)
  v                       |
  B ----------------------+
```
-   Path 1: `S -> A -> T`.
-   Path 2: `S -> B -> T`.
-   Edges used: `(S,A), (A,T), (S,B), (B,T)`.
-   Are they disjoint? Yes, no shared edges.
-   Max Flow = 2. If `k=2`, YES. If `k=3`, NO.

### Algorithm: Max Flow (Menger's Theorem)

1.  **Menger's Theorem:** The maximum number of edge-disjoint paths from `s` to `t` is equal to the minimum number of edges whose removal disconnects `s` from `t` (Min-Cut).
2.  **Max-Flow Min-Cut:** By the Max-Flow Min-Cut theorem, this value is exactly the maximum flow in a network where every edge has **capacity 1**.
3.  **Procedure:**
    -   Construct a flow network.
    -   Assign capacity 1 to every directed edge.
    -   Run Max Flow (Dinic).
    -   If `max_flow >= k`, return YES.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Directed:** Edges are directed. `u->v` is distinct from `v->u`.
-   **Optimization:** You can stop the max flow algorithm as soon as the flow reaches `k`.
-   **Constraints:** `N=100,000`. Dinic is efficient on unit capacity networks (`O(min(V^{2/3}, E^{1/2}) * E)`).

## Naive Approach

### Intuition

Find a path (BFS), remove edges, repeat.

### Failure Case

Greedy path finding might block future paths.
Example:
```
    A
  /   \
S - M - T
  \   /
    B
```
Edges: `S->A, A->M, M->B, B->T`, `S->M`, `M->T`.
If we greedily take `S->M->T`, we block `M`.

## Optimal Approach (Dinic's Algorithm)

### Time Complexity

-   **O(E * min(V^(2/3), E^(1/2)))**: For unit networks. With `K` limit, it's effectively `O(k * E)` or faster.

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
        int cap;
        int flow;
        Edge(int to, int rev, int cap) {
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

    public boolean hasKEdgeDisjointPaths(int n, int s, int t, int k, int[][] edges) {
        N = n;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int[] e : edges) {
            addEdge(e[0], e[1], 1);
        }

        return dinic(s, t, k) >= k;
    }

    private void addEdge(int from, int to, int cap) {
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

    private int dfs(int u, int t, int pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (; ptr[u] < adj.get(u).size(); ptr[u]++) {
            Edge e = adj.get(u).get(ptr[u]);
            if (level[u] + 1 != level[e.to] || e.cap - e.flow == 0) continue;
            int tr = dfs(e.to, t, Math.min(pushed, e.cap - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj.get(e.to).get(e.rev).flow -= tr;
            return tr;
        }
        return 0;
    }

    private int dinic(int s, int t, int limit) {
        int flow = 0;
        while (flow < limit && bfs(s, t)) {
            ptr = new int[N];
            while (flow < limit) {
                int pushed = dfs(s, t, limit - flow);
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
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int k = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
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

    def max_flow(self, s, t, limit):
        max_f = 0
        while max_f < limit and self.bfs(s, t):
            ptr = [0] * self.n
            while max_f < limit:
                pushed = self.dfs(s, t, limit - max_f, ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f

def has_k_edge_disjoint_paths(n: int, s: int, t: int, k: int, edges: list[tuple[int, int]]) -> bool:
    dinic = Dinic(n)
    for u, v in edges:
        dinic.add_edge(u, v, 1)
    return dinic.max_flow(s, t, k) >= k

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
        k = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print("YES" if has_k_edge_disjoint_paths(n, s, t, k, edges) else "NO")
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

struct Edge {
    int to;
    int cap;
    int flow;
    int rev;
};

class Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

public:
    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void addEdge(int from, int to, int cap) {
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

    int dfs(int u, int t, int pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (int& cid = ptr[u]; cid < adj[u].size(); ++cid) {
            auto& e = adj[u][cid];
            int tr = e.to;
            if (level[u] + 1 != level[tr] || e.cap - e.flow == 0) continue;
            int push = dfs(tr, t, min(pushed, e.cap - e.flow));
            if (push == 0) continue;
            e.flow += push;
            adj[tr][e.rev].flow -= push;
            return push;
        }
        return 0;
    }

    int maxFlow(int s, int t, int limit) {
        int flow = 0;
        while (flow < limit && bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (flow < limit) {
                int pushed = dfs(s, t, limit - flow);
                if (pushed == 0) break;
                flow += pushed;
            }
        }
        return flow;
    }
};

class Solution {
public:
    bool hasKEdgeDisjointPaths(int n, int s, int t, int k, const vector<pair<int, int>>& edges) {
        Dinic dinic(n);
        for (const auto& e : edges) {
            dinic.addEdge(e.first, e.second, 1);
        }
        return dinic.maxFlow(s, t, k) >= k;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << (solution.hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
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
    this.graph[u].push({ to: v, cap: cap, flow: 0, rev: this.graph[v].length });
    this.graph[v].push({ to: u, cap: 0, flow: 0, rev: this.graph[u].length - 1 });
  }

  bfs(s, t) {
    this.level.fill(-1);
    this.level[s] = 0;
    const queue = [s];
    let head = 0;
    while (head < queue.length) {
      const u = queue[head++];
      for (const edge of this.graph[u]) {
        if (edge.cap - edge.flow > 0 && this.level[edge.to] === -1) {
          this.level[edge.to] = this.level[u] + 1;
          queue.push(edge.to);
        }
      }
    }
    return this.level[t] !== -1;
  }

  dfs(u, t, pushed, ptr) {
    if (pushed === 0 || u === t) return pushed;
    for (let i = ptr[u]; i < this.graph[u].length; i++) {
      ptr[u] = i;
      const edge = this.graph[u][i];
      if (this.level[u] + 1 !== this.level[edge.to] || edge.cap - edge.flow === 0) continue;
      
      let tr = pushed < (edge.cap - edge.flow) ? pushed : (edge.cap - edge.flow);
      const push = this.dfs(edge.to, t, tr, ptr);
      
      if (push === 0) continue;
      
      edge.flow += push;
      this.graph[edge.to][edge.rev].flow -= push;
      return push;
    }
    return 0;
  }

  maxFlow(s, t, limit) {
    let flow = 0;
    while (flow < limit && this.bfs(s, t)) {
      const ptr = new Int32Array(this.n).fill(0);
      while (flow < limit) {
        const pushed = this.dfs(s, t, limit - flow, ptr);
        if (pushed === 0) break;
        flow += pushed;
      }
    }
    return flow;
  }
}

class Solution {
  hasKEdgeDisjointPaths(n, s, t, k, edges) {
    const dinic = new Dinic(n);
    for (const [u, v] of edges) {
      dinic.addEdge(u, v, 1);
    }
    return dinic.maxFlow(s, t, k) >= k;
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
  const k = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4 0 3 2
0 1
1 3
0 2
2 3
```
-   `s=0, t=3, k=2`.
-   Edges: `0->1`, `1->3`, `0->2`, `2->3`.
-   **Dinic:**
    -   BFS: `0->1->3` (len 2), `0->2->3` (len 2).
    -   DFS:
        -   Push 1 along `0->1->3`. Flow=1.
        -   Push 1 along `0->2->3`. Flow=2.
    -   Limit reached (2). Return 2.
-   **Result:** `2 >= 2` -> YES.

## ✅ Proof of Correctness

-   **Menger's Theorem:** Max edge-disjoint paths = Max Flow with unit capacities.
-   **Dinic:** Correctly computes Max Flow.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Vertex-Disjoint:** Split each node `u` into `u_in` and `u_out` with capacity 1 edge.
-   **Weighted:** Min-cost k-disjoint paths (MCMF).
-   **Undirected:** Replace undirected edge `u-v` with `u->v` and `v->u` both capacity 1? No, that allows `u->v` and `v->u` simultaneously (cycle). For edge-disjoint in undirected, standard max flow works if we treat edge as a single capacity 1 link (flow in one direction blocks other).

### Common Mistakes to Avoid

1.  **Capacity:** Must be 1 for edge-disjoint.
2.  **Direction:** Respect edge direction.
3.  **Self-Loops:** Ignore or handle (though usually irrelevant for s-t paths).
