---
problem_id: AGR_DINIC_WITH_SCALING__5083
display_id: AGR-011
slug: dinic-with-scaling
title: "Dinic With Scaling"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Max Flow
  - Scaling
tags:
  - advanced-graphs
  - max-flow
  - dinic
  - medium
premium: true
subscription_tier: basic
---

# AGR-011: Dinic With Scaling

## 📋 Problem Summary

Compute the maximum flow in a directed graph using **Dinic's Algorithm with Capacity Scaling**. This optimization helps when edge capacities are very large.

## 🌍 Real-World Scenario

**Scenario Title:** High-Volume Data Pipeline

Imagine a data center network transferring petabytes of data.
-   **Capacities:** Links have massive bandwidths (e.g., 100 Gbps, 10 Gbps).
-   **Challenge:** Standard augmenting path algorithms might waste time finding tiny flows (1 bit) when huge pipes are available.
-   **Scaling:** First, route traffic only through the "thickest" pipes (e.g., > 64 Gbps). Once saturated, use the > 32 Gbps pipes, and so on. This ensures we make significant progress quickly.

![Real-World Application](../images/AGR-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (100)
  S ---------> A
  |            |
  | (1)        | (100)
  v            v
  B ---------> T
      (100)
```
-   **Without Scaling:** Might find path `S->B->T` (100) then `S->A->T` (100).
-   **With Scaling (Delta=64):**
    -   Edges `S->A` (100), `A->T` (100), `S->B` (1), `B->T` (100).
    -   Only consider edges with cap >= 64.
    -   Path `S->A->T` is valid. Push 100.
    -   Path `S->B->T` invalid (`S->B` cap 1 < 64).
-   **Delta=32...1:**
    -   Eventually consider `S->B`.

### Algorithm: Capacity Scaling

1.  **Initialize Delta:** Let `U` be the max capacity. Set `delta` to the largest power of 2 less than or equal to `U`.
2.  **Iterate:** While `delta >= 1`:
    -   Run Dinic's Algorithm (BFS levels + DFS blocking flow), but **ignore edges** where `residual_capacity < delta`.
    -   `delta /= 2`.
3.  **Result:** Sum of all flows pushed.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Large Capacities:** Up to `10^9`. Scaling is effective here.
-   **Flow:** Use `long` (64-bit).
-   **Complexity:** Scaling adds a `log(MaxCap)` factor but reduces the dependence on E in practice for some cases, or ensures polynomial time `O(E^2 log C)` independent of flow value.

## Naive Approach

### Intuition

Standard Edmonds-Karp (BFS).

### Time Complexity

-   **O(V * E^2)**: Theoretically fine for small graphs, but slow if flow is large and many augmentations needed.

## Optimal Approach (Dinic + Scaling)

### Time Complexity

-   **O(E^2 log C)**: The number of scaling phases is `log C`. In each phase, we do at most `2E` augmentations (roughly).

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

    public long maxFlow(int n, int s, int t, int[][] edges) {
        N = n;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        long maxCap = 0;
        for (int[] e : edges) {
            addEdge(e[0], e[1], e[2]);
            maxCap = Math.max(maxCap, e[2]);
        }

        long flow = 0;
        long delta = 1;
        while (delta * 2 <= maxCap) delta *= 2;

        for (; delta >= 1; delta /= 2) {
            while (bfs(s, t, delta)) {
                ptr = new int[N];
                while (true) {
                    long pushed = dfs(s, t, Long.MAX_VALUE, delta);
                    if (pushed == 0) break;
                    flow += pushed;
                }
            }
        }

        return flow;
    }

    private void addEdge(int from, int to, long cap) {
        Edge a = new Edge(to, adj.get(to).size(), cap);
        Edge b = new Edge(from, adj.get(from).size(), 0);
        adj.get(from).add(a);
        adj.get(to).add(b);
    }

    private boolean bfs(int s, int t, long delta) {
        level = new int[N];
        Arrays.fill(level, -1);
        level[s] = 0;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(s);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (Edge e : adj.get(u)) {
                if (e.cap - e.flow >= delta && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.add(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    private long dfs(int u, int t, long pushed, long delta) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (; ptr[u] < adj.get(u).size(); ptr[u]++) {
            Edge e = adj.get(u).get(ptr[u]);
            if (level[u] + 1 != level[e.to] || e.cap - e.flow < delta) continue;
            long tr = dfs(e.to, t, Math.min(pushed, e.cap - e.flow), delta);
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
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxFlow(n, s, t, edges));
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

    def bfs(self, s, t, delta):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, rev in self.graph[u]:
                if cap >= delta and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, flow, ptr, delta):
        if u == t or flow == 0:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap >= delta:
                pushed = self.dfs(v, t, min(flow, cap), ptr, delta)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_cap = 0
        for u in range(self.n):
            for v, cap, rev in self.graph[u]:
                max_cap = max(max_cap, cap)
        
        delta = 1
        while delta * 2 <= max_cap:
            delta *= 2
            
        max_f = 0
        while delta >= 1:
            while self.bfs(s, t, delta):
                ptr = [0] * self.n
                while True:
                    pushed = self.dfs(s, t, float('inf'), ptr, delta)
                    if pushed == 0:
                        break
                    max_f += pushed
            delta //= 2
        return max_f

def max_flow(n: int, s: int, t: int, edges: list[tuple[int, int, int]]) -> int:
    dinic = Dinic(n)
    for u, v, c in edges:
        dinic.add_edge(u, v, c)
    return dinic.max_flow(s, t)

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
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
            
        print(max_flow(n, s, t, edges))
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

    bool bfs(int s, int t, long long delta) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (const auto& e : adj[u]) {
                if (e.cap - e.flow >= delta && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int u, int t, long long pushed, long long delta) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (int& cid = ptr[u]; cid < adj[u].size(); ++cid) {
            auto& e = adj[u][cid];
            int tr = e.to;
            if (level[u] + 1 != level[tr] || e.cap - e.flow < delta) continue;
            long long push = dfs(tr, t, min(pushed, e.cap - e.flow), delta);
            if (push == 0) continue;
            e.flow += push;
            adj[tr][e.rev].flow -= push;
            return push;
        }
        return 0;
    }

    long long maxFlow(int s, int t) {
        long long maxCap = 0;
        for(const auto& list : adj) {
            for(const auto& e : list) maxCap = max(maxCap, e.cap);
        }
        
        long long delta = 1;
        while (delta * 2 <= maxCap) delta *= 2;

        long long flow = 0;
        for (; delta >= 1; delta /= 2) {
            while (bfs(s, t, delta)) {
                fill(ptr.begin(), ptr.end(), 0);
                while (long long pushed = dfs(s, t, INF, delta)) {
                    flow += pushed;
                }
            }
        }
        return flow;
    }
};

class Solution {
public:
    long long maxFlow(int n, int s, int t, const vector<array<int, 3>>& edges) {
        Dinic dinic(n);
        for (const auto& e : edges) {
            dinic.addEdge(e[0], e[1], e[2]);
        }
        return dinic.maxFlow(s, t);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.maxFlow(n, s, t, edges) << "\n";
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

  bfs(s, t, delta) {
    this.level.fill(-1);
    this.level[s] = 0;
    const queue = [s];
    let head = 0;
    while (head < queue.length) {
      const u = queue[head++];
      for (const edge of this.graph[u]) {
        if (edge.cap - edge.flow >= delta && this.level[edge.to] === -1) {
          this.level[edge.to] = this.level[u] + 1;
          queue.push(edge.to);
        }
      }
    }
    return this.level[t] !== -1;
  }

  dfs(u, t, pushed, ptr, delta) {
    if (pushed === 0n || u === t) return pushed;
    for (let i = ptr[u]; i < this.graph[u].length; i++) {
      ptr[u] = i;
      const edge = this.graph[u][i];
      if (this.level[u] + 1 !== this.level[edge.to] || edge.cap - edge.flow < delta) continue;
      
      let tr = pushed < (edge.cap - edge.flow) ? pushed : (edge.cap - edge.flow);
      const push = this.dfs(edge.to, t, tr, ptr, delta);
      
      if (push === 0n) continue;
      
      edge.flow += push;
      this.graph[edge.to][edge.rev].flow -= push;
      return push;
    }
    return 0n;
  }

  maxFlow(s, t) {
    let maxCap = 0n;
    for (const list of this.graph) {
        for (const e of list) {
            if (e.cap > maxCap) maxCap = e.cap;
        }
    }
      
    let delta = 1n;
    while (delta * 2n <= maxCap) delta *= 2n;
      
    let flow = 0n;
    while (delta >= 1n) {
        while (this.bfs(s, t, delta)) {
          const ptr = new Int32Array(this.n).fill(0);
          while (true) {
            const pushed = this.dfs(s, t, 1000000000000000000n, ptr, delta);
            if (pushed === 0n) break;
            flow += pushed;
          }
        }
        delta /= 2n;
    }
    return flow;
  }
}

class Solution {
  maxFlow(n, s, t, edges) {
    const dinic = new Dinic(n);
    for (const [u, v, c] of edges) {
      dinic.addEdge(u, v, c);
    }
    return dinic.maxFlow(s, t);
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  console.log(solution.maxFlow(n, s, t, edges).toString());
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4 0 3
0 1 10
0 2 5
1 3 7
2 3 8
```
-   Max Cap = 10. `delta` starts at 8.
-   **Delta = 8:**
    -   Edges >= 8: `0->1` (10), `2->3` (8).
    -   BFS: `0->1`. `1->3` (7 < 8) ignored. `0->2` (5 < 8) ignored.
    -   No path to 3.
-   **Delta = 4:**
    -   Edges >= 4: All.
    -   BFS: `0->1->3` (10, 7), `0->2->3` (5, 8).
    -   DFS `0->1->3`: Push `min(10, 7) = 7`. Flow=7.
    -   DFS `0->2->3`: Push `min(5, 8) = 5`. Flow=12.
    -   Total Flow = 12.
-   **Delta = 2, 1:**
    -   Residuals: `0->1` (3), `1->3` (0), `0->2` (0), `2->3` (3).
    -   No path.

**Result:** 12. Correct.

## ✅ Proof of Correctness

-   **Scaling:** In each phase `delta`, we push flow along paths with bottleneck >= `delta`.
-   **Termination:** When `delta=1`, we consider all edges with residual capacity >= 1. Since capacities are integers, this finds the exact max flow.
-   **Complexity:** The scaling ensures we don't "nibble" at the flow with small augmentations when large ones are possible.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Why Scaling?** Standard Dinic is `O(V^2 E)`. On a graph with `V=2`, `E=2`, caps `10^9`, Dinic is fast (1 step). But on specific "bad" graphs, scaling guarantees polynomial time in `log C`.
-   **Edmonds-Karp:** Scaling can also be applied to Edmonds-Karp (BFS), making it `O(E^2 log C)`.
-   **Real-valued Capacities:** Scaling doesn't work directly; requires integer capacities.

### C++ommon Mistakes to Avoid

1.  **Delta Initialization:** Start with largest power of 2 <= max_cap.
2.  **Loop Condition:** `delta >= 1`.
3.  **Residual Check:** `cap - flow >= delta`.
