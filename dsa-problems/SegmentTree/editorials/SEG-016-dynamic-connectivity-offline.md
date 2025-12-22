---
title: Dynamic Connectivity Over Time (Offline)
slug: dynamic-connectivity-offline
difficulty: Hard
difficulty_score: 78
tags:
- Segment Tree
- DSU Rollback
- Offline Queries
problem_id: SEG_DYNAMIC_CONNECTIVITY_OFFLINE__6384
display_id: SEG-016
topics:
- Segment Tree
- DSU Rollback
- Offline Queries
---
# Dynamic Connectivity Over Time (Offline) - Editorial

## Problem Summary

You are given a sequence of `m` events on a graph with `n` nodes:
1.  **ADD u v**: Add an edge between `u` and `v`.
2.  **REMOVE u v**: Remove the edge between `u` and `v`.
3.  **QUERY u v**: Check if `u` and `v` are connected.

You must answer the queries in the order they appear.

## Real-World Scenario

Imagine a **Network Simulation Tool**.
-   You are simulating a network where links (cables) are constantly being plugged in and unplugged.
-   At various points in time, you need to verify if two servers can communicate.
-   Since this is a simulation (or a log replay), you have all events available beforehand (offline).

## Problem Exploration

### 1. Dynamic Connectivity
-   Fully dynamic connectivity (online) is very hard ($O(\log^2 N)$ or $O(\sqrt{N})$).
-   Offline dynamic connectivity is solvable using **Segment Tree over Time**.

### 2. Segment Tree over Time
-   The "time" is the index of the operation (0 to `m-1`).
-   An edge `(u, v)` exists for a set of time intervals.
    -   If added at $t_1$ and removed at $t_2$, it exists in $[t_1, t_2-1]$.
    -   If added at $t_1$ and never removed, it exists in $[t_1, m-1]$.
-   We can map each edge to a list of intervals.
-   We build a Segment Tree where leaves represent time points.
-   We add each edge to the Segment Tree nodes covering its intervals.
    -   Just like range updates, but instead of updating a value, we append the edge to a list in the node.

### 3. DFS Traversal with DSU Rollback
-   Traverse the Segment Tree (DFS).
-   When entering a node:
    -   Apply all edges stored in this node using DSU (Union-Find).
    -   Keep track of operations to rollback (store which nodes were merged and rank changes).
-   When reaching a leaf (time $t$):
    -   If the operation at $t$ is a QUERY, answer it using the current DSU state.
-   When exiting a node:
    -   Rollback the DSU operations performed at this node to restore state for the sibling.

### 4. Complexity
-   Each edge covers $O(\log m)$ nodes in the Segment Tree.
-   DSU operations take $O(\log n)$ or $O(\alpha(n))$ (with path compression, but rollback usually prevents path compression, so we use union by rank/size which is $O(\log n)$).
-   Total time: $O(m \log m \log n)$.

## Approaches

### Approach 1: Segment Tree Divide & Conquer (Offline)
-   Map edges to intervals.
-   Build Segment Tree.
-   DFS with DSU Rollback.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int u, v;
        Edge(int u, int v) {
            this.u = u;
            this.v = v;
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Edge edge = (Edge) o;
            return (u == edge.u && v == edge.v) || (u == edge.v && v == edge.u);
        }
        
        @Override
        public int hashCode() {
            return u < v ? Objects.hash(u, v) : Objects.hash(v, u);
        }
    }

    static class DSU {
        int[] parent;
        int[] rank;
        Stack<int[]> history;

        DSU(int n) {
            parent = new int[n + 1];
            rank = new int[n + 1];
            history = new Stack<>();
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
        }

        int find(int i) {
            if (parent[i] == i) return i;
            return find(parent[i]); // No path compression for rollback
        }

        void union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) {
                if (rank[rootI] < rank[rootJ]) {
                    int temp = rootI;
                    rootI = rootJ;
                    rootJ = temp;
                }
                parent[rootJ] = rootI;
                rank[rootI] += rank[rootJ];
                history.push(new int[]{rootJ, rootI});
            } else {
                history.push(new int[]{-1, -1});
            }
        }

        void rollback() {
            int[] op = history.pop();
            if (op[0] != -1) {
                int child = op[0];
                int parentNode = op[1];
                parent[child] = child;
                rank[parentNode] -= rank[child];
            }
        }
        
        boolean connected(int i, int j) {
            return find(i) == find(j);
        }
    }

    private List<Edge>[] tree;
    private List<String> results;
    private List<String[]> queries; // Store queries by time index

    public List<String> process(int n, List<String[]> events) {
        int m = events.size();
        tree = new ArrayList[4 * m];
        for (int i = 0; i < 4 * m; i++) tree[i] = new ArrayList<>();
        
        queries = new ArrayList<>();
        for(int i=0; i<m; i++) queries.add(null);
        
        Map<String, Integer> activeEdges = new HashMap<>();
        
        for (int i = 0; i < m; i++) {
            String[] ev = events.get(i);
            String type = ev[0];
            int u = Integer.parseInt(ev[1]);
            int v = Integer.parseInt(ev[2]);
            if (u > v) { int temp = u; u = v; v = temp; }
            String key = u + "," + v;
            
            if (type.equals("ADD")) {
                activeEdges.put(key, i);
            } else if (type.equals("REMOVE")) {
                if (activeEdges.containsKey(key)) {
                    int start = activeEdges.remove(key);
                    addEdge(0, 0, m - 1, start, i - 1, new Edge(u, v));
                }
            } else {
                queries.set(i, ev);
            }
        }
        
        for (Map.Entry<String, Integer> entry : activeEdges.entrySet()) {
            int start = entry.getValue();
            String[] parts = entry.getKey().split(",");
            int u = Integer.parseInt(parts[0]);
            int v = Integer.parseInt(parts[1]);
            addEdge(0, 0, m - 1, start, m - 1, new Edge(u, v));
        }
        
        results = new ArrayList<>();
        DSU dsu = new DSU(n);
        dfs(0, 0, m - 1, dsu);
        
        return results;
    }

    private void addEdge(int node, int start, int end, int l, int r, Edge e) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].add(e);
            return;
        }
        int mid = (start + end) / 2;
        addEdge(2 * node + 1, start, mid, l, r, e);
        addEdge(2 * node + 2, mid + 1, end, l, r, e);
    }

    private void dfs(int node, int start, int end, DSU dsu) {
        for (Edge e : tree[node]) {
            dsu.union(e.u, e.v);
        }
        
        if (start == end) {
            if (queries.get(start) != null) {
                String[] q = queries.get(start);
                int u = Integer.parseInt(q[1]);
                int v = Integer.parseInt(q[2]);
                results.add(dsu.connected(u, v) ? "true" : "false");
            }
        } else {
            int mid = (start + end) / 2;
            dfs(2 * node + 1, start, mid, dsu);
            dfs(2 * node + 2, mid + 1, end, dsu);
        }
        
        for (int i = 0; i < tree[node].size(); i++) {
            dsu.rollback();
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.history = []

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.rank[root_i] += self.rank[root_j]
            self.history.append((root_j, root_i))
            return True
        else:
            self.history.append((-1, -1))
            return False

    def rollback(self):
        child, parent_node = self.history.pop()
        if child != -1:
            self.parent[child] = child
            self.rank[parent_node] -= self.rank[child]

    def connected(self, i, j):
        return self.find(i) == self.find(j)

class Solution:
    def process(self, n: int, events: list[list[str]]) -> list[str]:
        m = len(events)
        tree = [[] for _ in range(4 * m)]
        queries = [None] * m
        active_edges = {}
        
        for i, ev in enumerate(events):
            type, u, v = ev[0], int(ev[1]), int(ev[2])
            if u > v: u, v = v, u
            key = (u, v)
            
            if type == "ADD":
                active_edges[key] = i
            elif type == "REMOVE":
                if key in active_edges:
                    start = active_edges.pop(key)
                    self.add_edge(tree, 0, 0, m - 1, start, i - 1, (u, v))
            else:
                queries[i] = (u, v)
                
        for key, start in active_edges.items():
            self.add_edge(tree, 0, 0, m - 1, start, m - 1, key)
            
        dsu = DSU(n)
        results = []
        self.dfs(tree, 0, 0, m - 1, dsu, queries, results)
        return results

    def add_edge(self, tree, node, start, end, l, r, edge):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            tree[node].append(edge)
            return
        mid = (start + end) // 2
        self.add_edge(tree, 2 * node + 1, start, mid, l, r, edge)
        self.add_edge(tree, 2 * node + 2, mid + 1, end, l, r, edge)

    def dfs(self, tree, node, start, end, dsu, queries, results):
        ops = 0
        for u, v in tree[node]:
            dsu.union(u, v)
            ops += 1
            
        if start == end:
            if queries[start]:
                u, v = queries[start]
                results.append("true" if dsu.connected(u, v) else "false")
        else:
            mid = (start + end) // 2
            self.dfs(tree, 2 * node + 1, start, mid, dsu, queries, results)
            self.dfs(tree, 2 * node + 2, mid + 1, end, dsu, queries, results)
            
        for _ in range(ops):
            dsu.rollback()

def process(n, events):
    return Solution().process(n, events)
```

### C++

```cpp
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

struct Edge {
    int u, v;
};

struct DSU {
    vector<int> parent;
    vector<int> rank;
    struct RollbackInfo {
        int child, parent;
    };
    stack<RollbackInfo> history;

    DSU(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 1);
        for (int i = 1; i <= n; i++) parent[i] = i;
    }

    int find(int i) {
        if (parent[i] == i) return i;
        return find(parent[i]);
    }

    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            if (rank[rootI] < rank[rootJ]) swap(rootI, rootJ);
            parent[rootJ] = rootI;
            rank[rootI] += rank[rootJ];
            history.push({rootJ, rootI});
        } else {
            history.push({-1, -1});
        }
    }

    void rollback() {
        RollbackInfo op = history.top();
        history.pop();
        if (op.child != -1) {
            parent[op.child] = op.child;
            rank[op.parent] -= rank[op.child];
        }
    }

    bool connected(int i, int j) {
        return find(i) == find(j);
    }
};

class Solution {
    vector<vector<Edge>> tree;
    vector<pair<int, int>> queries;
    vector<string> results;

    void addEdge(int node, int start, int end, int l, int r, Edge e) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].push_back(e);
            return;
        }
        int mid = (start + end) / 2;
        addEdge(2 * node + 1, start, mid, l, r, e);
        addEdge(2 * node + 2, mid + 1, end, l, r, e);
    }

    void dfs(int node, int start, int end, DSU& dsu) {
        for (const auto& e : tree[node]) {
            dsu.unite(e.u, e.v);
        }

        if (start == end) {
            if (queries[start].first != -1) {
                results.push_back(dsu.connected(queries[start].first, queries[start].second) ? "true" : "false");
            }
        } else {
            int mid = (start + end) / 2;
            dfs(2 * node + 1, start, mid, dsu);
            dfs(2 * node + 2, mid + 1, end, dsu);
        }

        for (size_t i = 0; i < tree[node].size(); i++) {
            dsu.rollback();
        }
    }

public:
    vector<string> process(int n, const vector<vector<string>>& events) {
        int m = events.size();
        tree.resize(4 * m);
        queries.assign(m, {-1, -1});
        
        map<pair<int, int>, int> activeEdges;
        
        for (int i = 0; i < m; i++) {
            string type = events[i][0];
            int u = stoi(events[i][1]);
            int v = stoi(events[i][2]);
            if (u > v) swap(u, v);
            
            if (type == "ADD") {
                activeEdges[{u, v}] = i;
            } else if (type == "REMOVE") {
                if (activeEdges.count({u, v})) {
                    int start = activeEdges[{u, v}];
                    activeEdges.erase({u, v});
                    addEdge(0, 0, m - 1, start, i - 1, {u, v});
                }
            } else {
                queries[i] = {u, v};
            }
        }
        
        for (auto const& [edge, start] : activeEdges) {
            addEdge(0, 0, m - 1, start, m - 1, {edge.first, edge.second});
        }
        
        DSU dsu(n);
        dfs(0, 0, m - 1, dsu);
        
        return results;
    }
};
```

### JavaScript

```javascript
class Solution {
  process(n, events) {
    const m = events.length;
    const tree = Array.from({ length: 4 * m }, () => []);
    const queries = new Array(m).fill(null);
    const activeEdges = new Map();

    const addEdge = (node, start, end, l, r, edge) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        tree[node].push(edge);
        return;
      }
      const mid = Math.floor((start + end) / 2);
      addEdge(2 * node + 1, start, mid, l, r, edge);
      addEdge(2 * node + 2, mid + 1, end, l, r, edge);
    };

    for (let i = 0; i < m; i++) {
      const type = events[i][0];
      let u = parseInt(events[i][1], 10);
      let v = parseInt(events[i][2], 10);
      if (u > v) [u, v] = [v, u];
      const key = `${u},${v}`;

      if (type === "ADD") {
        activeEdges.set(key, i);
      } else if (type === "REMOVE") {
        if (activeEdges.has(key)) {
          const start = activeEdges.get(key);
          activeEdges.delete(key);
          addEdge(0, 0, m - 1, start, i - 1, { u, v });
        }
      } else {
        queries[i] = { u, v };
      }
    }

    for (const [key, start] of activeEdges.entries()) {
      const [u, v] = key.split(",").map(Number);
      addEdge(0, 0, m - 1, start, m - 1, { u, v });
    }

    // DSU
    const parent = new Int32Array(n + 1);
    const rank = new Int32Array(n + 1);
    for (let i = 1; i <= n; i++) {
      parent[i] = i;
      rank[i] = 1;
    }
    const history = [];

    const find = (i) => {
      if (parent[i] === i) return i;
      return find(parent[i]);
    };

    const union = (i, j) => {
      let rootI = find(i);
      let rootJ = find(j);
      if (rootI !== rootJ) {
        if (rank[rootI] < rank[rootJ]) {
          const temp = rootI;
          rootI = rootJ;
          rootJ = temp;
        }
        parent[rootJ] = rootI;
        rank[rootI] += rank[rootJ];
        history.push({ child: rootJ, parent: rootI });
      } else {
        history.push({ child: -1, parent: -1 });
      }
    };

    const rollback = () => {
      const op = history.pop();
      if (op.child !== -1) {
        parent[op.child] = op.child;
        rank[op.parent] -= rank[op.child];
      }
    };

    const connected = (i, j) => find(i) === find(j);

    const results = [];

    const dfs = (node, start, end) => {
      for (const e of tree[node]) {
        union(e.u, e.v);
      }

      if (start === end) {
        if (queries[start]) {
          results.push(connected(queries[start].u, queries[start].v) ? "true" : "false");
        }
      } else {
        const mid = Math.floor((start + end) / 2);
        dfs(2 * node + 1, start, mid);
        dfs(2 * node + 2, mid + 1, end);
      }

      for (let i = 0; i < tree[node].length; i++) {
        rollback();
      }
    };

    dfs(0, 0, m - 1);
    return results;
  }
}
```

## Test Case Walkthrough

**Input:**
`3 4`
`ADD 1 2`
`QUERY 1 2`
`REMOVE 1 2`
`QUERY 1 2`

1.  **Events**:
    -   0: ADD 1 2. Active.
    -   1: QUERY 1 2.
    -   2: REMOVE 1 2. Edge (1,2) interval: `[0, 1]`.
    -   3: QUERY 1 2.
2.  **Segment Tree**:
    -   Edge (1,2) added to range `[0, 1]`.
3.  **DFS**:
    -   Enter `[0, 1]`: Union(1, 2).
    -   Leaf 0: No query.
    -   Leaf 1: Query 1 2. Connected? Yes. Output `true`.
    -   Exit `[0, 1]`: Rollback.
    -   Enter `[2, 3]`: No edges.
    -   Leaf 2: No query.
    -   Leaf 3: Query 1 2. Connected? No. Output `false`.

## Proof of Correctness

-   **Time Intervals**: Correctly maps edge lifespan to segment tree nodes.
-   **DSU Rollback**: Ensures state is valid for the current time interval during DFS traversal.
-   **Offline**: All queries processed in correct temporal order.

## Interview Extensions

1.  **Dynamic MST?**
    -   Same approach, but maintain MST edges. Rollback is harder if we need to query total weight efficiently.
2.  **Bipartite Check?**
    -   Maintain bipartite property in DSU (distance to root parity).

### C++ommon Mistakes

-   **Path Compression**: Cannot use path compression with rollback easily (it destroys structure). Must use Union by Rank/Size only.
-   **Edge Intervals**: Be careful with indices (inclusive/exclusive) when edge is removed.
