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
time_limit: 2000
memory_limit: 256
---
# AGR-009: Maximum Matching with Node Capacities

## Problem Statement

You are given a bipartite graph with left part `U` and right part `V`. Each node `u` in `U` has capacity `capU[u]` (maximum number of matches it can take), and each node `v` in `V` has capacity `capV[v]`.

Find the maximum matching size respecting these capacities.

![Problem Illustration](../images/AGR-009/problem-illustration.png)

## Input Format

- First line: integers `nU`, `nV`, and `m`
- Second line: `nU` integers `capU`
- Third line: `nV` integers `capV`
- Next `m` lines: `u v` describing an edge from `u` in `U` to `v` in `V`

## Output Format

- Single integer: maximum feasible matching size

## Constraints

- `1 <= nU + nV <= 100000`
- `0 <= m <= 200000`
- `0 <= capU[i], capV[j] <= 10^9`
- `0 <= u < nU`, `0 <= v < nV`

## Example

**Input:**

```
2 2 3
1 2
1 1
0 0
1 0
1 1
```

**Output:**

```
2
```

**Explanation:**

The capacities limit the matching to size 2.

![Example Visualization](../images/AGR-009/example-1.png)

## Notes

- Convert to a flow network with source->U capacities, V->sink capacities, and edges U->V with capacity 1.
- Use Dinic for efficiency.
- Use 64-bit integers for flow values.

## Related Topics

Bipartite Matching, Max Flow, Capacity Constraints

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
        return 0;
    }

    private void addEdge(int from, int to, long cap) {
    }

    private boolean bfs(int s, int t) {
        return false;
    }

    private long dfs(int u, int t, long pushed) {
        return 0;
    }

    private long dinic(int s, int t) {
        return 0;
    }
}

class Main {
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
        return 0
    def add_edge(self, u, v, capacity):
        return 0
    def bfs(self, s, t):
        return 0
    def dfs(self, u, t, flow, ptr):
        return 0
    def max_flow(self, s, t):
        return 0
def max_matching(nU: int, nV: int, capU: list[int], capV: list[int], edges: list[tuple[int, int]]) -> int:
    return 0
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

