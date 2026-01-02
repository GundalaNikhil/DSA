---
problem_id: AGR_MINCOST_FLOW_DEMANDS__7702
display_id: AGR-012
slug: mincost-flow-demands
title: "Minimum-Cost Flow With Demands"
difficulty: Hard
difficulty_score: 70
topics:
  - Graphs
  - Min-Cost Flow
  - Circulation
tags:
  - advanced-graphs
  - min-cost-flow
  - demands
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-012: Minimum-Cost Flow With Demands

## Problem Statement

You are given a directed graph with lower and upper bounds on edges and a supply/demand value at each node. Find a feasible circulation that satisfies all demands and minimizes total cost.

If no feasible flow exists, output `INFEASIBLE`.

![Problem Illustration](../images/AGR-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers `b[i]` (positive = supply, negative = demand)
- Next `m` lines: `u v low high cost` for edge `u -> v`

## Output Format

- If infeasible: print `INFEASIBLE`
- Otherwise: print `FEASIBLE` and a line with the minimum total cost

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 2000`
- `-10^9 <= b[i] <= 10^9`
- `0 <= low <= high <= 10^9`
- `-10^6 <= cost <= 10^6`

## Example

**Input:**

```
2 1
5 -5
0 1 2 5 1
```

**Output:**

```
FEASIBLE
5
```

**Explanation:**

Send 5 units from 0 to 1. Total cost is 5.

![Example Visualization](../images/AGR-012/example-1.png)

## Notes

- Convert to circulation with a super source and super sink.
- Use potentials and Dijkstra/SPFA for min-cost max-flow.
- Use 64-bit integers for costs and flows.

## Related Topics

Min-Cost Flow, Circulation, Potentials

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        int rev;
        long cap;
        long flow;
        long cost;
        Edge(int to, int rev, long cap, long cost) {
            this.to = to;
            this.rev = rev;
            this.cap = cap;
            this.cost = cost;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private long[] dist;
    private long[] h;
    private int[] parentNode;
    private int[] parentEdge;
    private int N;
    private final long INF = Long.MAX_VALUE / 2;

    public Long minCostFlow(int n, long[] b, int[][] edges) {
        return 0;
    }

    private void addEdge(int u, int v, long cap, long cost) {
    }

    private long[] mcmf(int s, int t) {
        return null;
    }

    private boolean spfa(int s) {
        return false;
    }

    private boolean dijkstra(int s, int t) {
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[] b = new long[n];
        for (int i = 0; i < n; i++) b[i] = sc.nextLong();
        int[][] edges = new int[m][5];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
            edges[i][3] = sc.nextInt();
            edges[i][4] = sc.nextInt();
        }

        Solution solution = new Solution();
        Long ans = solution.minCostFlow(n, b, edges);
        if (ans == null) {
            System.out.print("INFEASIBLE");
        } else {
            System.out.print("FEASIBLE\n" + ans);
        }
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

# Increase recursion depth
sys.setrecursionlimit(300000)

class MinCostMaxFlow:
    def __init__(self, n):
        return 0
    def add_edge(self, u, v, cap, cost):
        return 0
    def spfa(self, s):
        return 0
    def dijkstra(self, s, t):
        return 0
    def solve(self, s, t):
        return 0
def min_cost_flow(n: int, b: list[int], edges: list[tuple[int, int, int, int, int]]):
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
        b = [int(next(iterator)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            low = int(next(iterator))
            high = int(next(iterator))
            cost = int(next(iterator))
            edges.append((u, v, low, high, cost))
            
        ans = min_cost_flow(n, b, edges)
        if ans is None:
            sys.stdout.write("INFEASIBLE")
        else:
            sys.stdout.write("FEASIBLE\n" + str(ans))
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
#include <tuple>
#include <array>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    long long flow;
    long long cost;
    int rev;
};

class MinCostMaxFlow {
    int n;
    vector<vector<Edge>> adj;
    vector<long long> dist;
    vector<long long> h;
    vector<int> parentNode;
    vector<int> parentEdge;

public:
    MinCostMaxFlow(int n) : n(n), adj(n), dist(n), h(n), parentNode(n), parentEdge(n) {}

    void addEdge(int u, int v, long long cap, long long cost) {
        Edge a = {v, cap, 0, cost, (int)adj[v].size()};
        Edge b = {u, 0, 0, -cost, (int)adj[u].size()};
        adj[u].push_back(a);
        adj[v].push_back(b);
    }

    bool spfa(int s) {
        fill(h.begin(), h.end(), INF);
        h[s] = 0;
        vector<bool> inQueue(n, false);
        queue<int> q;
        q.push(s);
        inQueue[s] = true;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            inQueue[u] = false;
            for (const auto& e : adj[u]) {
                if (e.cap - e.flow > 0 && h[e.to] > h[u] + e.cost) {
                    h[e.to] = h[u] + e.cost;
                    if (!inQueue[e.to]) {
                        q.push(e.to);
                        inQueue[e.to] = true;
                    }
                }
            }
        }
        return h[s] != INF; // Should check if any reachable
    }

    bool dijkstra(int s, int t) {
        fill(dist.begin(), dist.end(), INF);
        dist[s] = 0;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, s});

        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;

            for (int i = 0; i < adj[u].size(); ++i) {
                const auto& e = adj[u][i];
                long long reducedCost = e.cost + h[u] - h[e.to];
                if (e.cap - e.flow > 0 && dist[e.to] > dist[u] + reducedCost) {
                    dist[e.to] = dist[u] + reducedCost;
                    parentNode[e.to] = u;
                    parentEdge[e.to] = i;
                    pq.push({dist[e.to], e.to});
                }
            }
        }
        return dist[t] != INF;
    }

    pair<long long, long long> solve(int s, int t) {
        long long flow = 0;
        long long cost = 0;
        spfa(s); // Init potentials

        while (dijkstra(s, t)) {
            for (int i = 0; i < n; ++i) {
                if (dist[i] != INF) h[i] += dist[i];
            }

            long long push = INF;
            int curr = t;
            while (curr != s) {
                int p = parentNode[curr];
                int idx = parentEdge[curr];
                push = min(push, adj[p][idx].cap - adj[p][idx].flow);
                curr = p;
            }

            flow += push;
            curr = t;
            while (curr != s) {
                int p = parentNode[curr];
                int idx = parentEdge[curr];
                adj[p][idx].flow += push;
                int revIdx = adj[p][idx].rev;
                adj[curr][revIdx].flow -= push;
                cost += push * adj[p][idx].cost;
                curr = p;
            }
        }
        return {flow, cost};
    }
};

class Solution {
public:
    bool minCostFlow(int n, const vector<long long>& b, const vector<array<int, 5>>& edges, long long& costOut) {
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> b(n);
    for (int i = 0; i < n; i++) cin >> b[i];
    vector<array<int, 5>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2] >> edges[i][3] >> edges[i][4];
    }

    Solution solution;
    long long cost = 0;
    bool ok = solution.minCostFlow(n, b, edges, cost);
    if (!ok) {
        cout << "INFEASIBLE";
    } else {
        cout << "FEASIBLE\n" << cost;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MinCostMaxFlow {
  constructor(n) {
    this.n = n;
    this.graph = Array.from({ length: n }, () => []);
    this.dist = new Array(n);
    this.h = new Array(n).fill(0);
    this.parentNode = new Int32Array(n);
    this.parentEdge = new Int32Array(n);
    this.INF = 1000000000000000000; // Large number
  }

  addEdge(u, v, cap, cost) {
    this.graph[u].push({ to: v, cap: cap, flow: 0, cost: cost, rev: this.graph[v].length });
    this.graph[v].push({ to: u, cap: 0, flow: 0, cost: -cost, rev: this.graph[u].length - 1 });
  }

  spfa(s) {
    this.h.fill(this.INF);
    this.h[s] = 0;
    const inQueue = new Int8Array(this.n).fill(0);
    const queue = [s];
    inQueue[s] = 1;
    
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        inQueue[u] = 0;
        for (const edge of this.graph[u]) {
            if (edge.cap - edge.flow > 0 && this.h[edge.to] > this.h[u] + edge.cost) {
                this.h[edge.to] = this.h[u] + edge.cost;
                if (!inQueue[edge.to]) {
                    queue.push(edge.to);
                    inQueue[edge.to] = 1;
                }
            }
        }
    }
  }

  dijkstra(s, t) {
    this.dist.fill(this.INF);
    this.dist[s] = 0;
    // Simple priority queue implementation or array scan for O(V^2)
    // Since N=500, O(V^2) is fine.
    const visited = new Int8Array(this.n).fill(0);
    
    for (let i = 0; i < this.n; i++) {
        let u = -1;
        let bestDist = this.INF;
        for (let j = 0; j < this.n; j++) {
            if (!visited[j] && this.dist[j] < bestDist) {
                u = j;
                bestDist = this.dist[j];
            }
        }
        
        if (u === -1 || bestDist === this.INF) break;
        visited[u] = 1;
        
        for (let k = 0; k < this.graph[u].length; k++) {
            const edge = this.graph[u][k];
            const reducedCost = edge.cost + this.h[u] - this.h[edge.to];
            if (edge.cap - edge.flow > 0 && this.dist[edge.to] > this.dist[u] + reducedCost) {
                this.dist[edge.to] = this.dist[u] + reducedCost;
                this.parentNode[edge.to] = u;
                this.parentEdge[edge.to] = k;
            }
        }
    }
    return this.dist[t] !== this.INF;
  }

  solve(s, t) {
    let flow = 0;
    let cost = 0;
    this.spfa(s);

    while (this.dijkstra(s, t)) {
        for (let i = 0; i < this.n; i++) {
            if (this.dist[i] !== this.INF) this.h[i] += this.dist[i];
        }

        let push = this.INF;
        let curr = t;
        while (curr !== s) {
            const p = this.parentNode[curr];
            const idx = this.parentEdge[curr];
            const edge = this.graph[p][idx];
            push = Math.min(push, edge.cap - edge.flow);
            curr = p;
        }

        flow += push;
        curr = t;
        while (curr !== s) {
            const p = this.parentNode[curr];
            const idx = this.parentEdge[curr];
            const edge = this.graph[p][idx];
            edge.flow += push;
            const revIdx = edge.rev;
            this.graph[curr][revIdx].flow -= push;
            cost += push * edge.cost;
            curr = p;
        }
    }
    return [flow, cost];
  }
}

class Solution {
  minCostFlow(n, b, edges) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const b = [];
  for (let i = 0; i < n; i++) b.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const low = parseInt(data[idx++], 10);
    const high = parseInt(data[idx++], 10);
    const cost = parseInt(data[idx++], 10);
    edges.push([u, v, low, high, cost]);
  }

  const solution = new Solution();
  const ans = solution.minCostFlow(n, b, edges);
  if (ans === null) {
    console.log("INFEASIBLE");
  } else {
    console.log("FEASIBLE");
    console.log(ans);
  }
});
```

