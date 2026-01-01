---
problem_id: GRB_SHORTEST_PATH_DAG__7291
display_id: GRB-014
slug: shortest-path-dag
title: "Shortest Path in DAG"
difficulty: Easy
difficulty_score: 38
topics:
  - Graphs
  - DAG
  - Shortest Path
tags:
  - graphs-basics
  - dag
  - shortest-path
  - easy
premium: true
subscription_tier: basic
---

# GRB-014: Shortest Path in DAG

## 📋 Problem Summary

Given a **Directed Acyclic Graph (DAG)** with weighted edges (possibly negative), find the shortest path distance from a source node `s` to all other nodes. If a node is unreachable, output `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** Project Scheduling (Critical Path)

Imagine managing a software project.
-   **Nodes** are milestones (e.g., "Design Complete", "Backend Ready").
-   **Edges** are tasks with durations (weights). `A -> B` with weight 5 means task A must finish before B, taking 5 days.
-   **DAG:** There are no cycles (you can't need B to finish A if A is needed for B).
-   **Shortest Path?** In scheduling, we often look for the *Longest Path* (Critical Path) to determine minimum project duration. However, finding the *Shortest Path* is mathematically identical (just negate weights).
-   This algorithm is used in tools like Jira or Asana to calculate dependencies and timelines efficiently.

![Real-World Application](../images/GRB-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (2)      (1)
  0 ------> 1 ------> 3
  |         ^
  | (5)     | (-2)
  v         |
  2 --------+
```
**Topological Sort:** `0, 2, 1, 3` (One valid order).

**Relaxation Order:**
1.  **Process 0:** `dist[0]=0`.
    -   `0->1` (w=2): `dist[1] = min(inf, 0+2) = 2`.
    -   `0->2` (w=5): `dist[2] = min(inf, 0+5) = 5`.
2.  **Process 2:** `dist[2]=5`.
    -   `2->1` (w=-2): `dist[1] = min(2, 5-2) = 3`. (Updated!)
3.  **Process 1:** `dist[1]=3`.
    -   `1->3` (w=1): `dist[3] = min(inf, 3+1) = 4`.
4.  **Process 3:** `dist[3]=4`. No outgoing edges.

**Final Distances:** `0:0, 1:3, 2:5, 3:4`.

### Algorithm Steps

1.  **Topological Sort:** Perform a topological sort (using DFS or Kahn's Algorithm) to get a linear ordering of nodes.
2.  **Initialize Distances:** `dist[s] = 0`, all others `infinity`.
3.  **Relax in Order:** Iterate through nodes `u` in topological order.
    -   If `dist[u]` is `infinity`, skip (unreachable).
    -   For each neighbor `v` with weight `w`:
        -   `dist[v] = min(dist[v], dist[u] + w)`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Negative Weights:** Allowed! Standard Dijkstra fails here, but DAG property makes it solvable in linear time.
-   **Unreachable:** Output `-1`.
-   **Infinity:** Use a sufficiently large number (e.g., `1e18` for 64-bit integers).

## Naive Approach

### Intuition

Run Bellman-Ford.

### Time Complexity

-   **O(N * M)**: Works, but overkill. DAGs allow O(N+M).

## Optimal Approach (Topological Sort + Relaxation)

By processing nodes in topological order, we guarantee that when we visit node `u`, we have already processed all possible predecessors of `u`. Thus, `dist[u]` is already final.

### Time Complexity

-   **O(N + M)**: Linear time. Much faster than Dijkstra (O(M log N)) or Bellman-Ford (O(NM)).

### Space Complexity

-   **O(N + M)**: Adjacency list + Recursion stack/Queue.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    private Stack<Integer> stack;
    private boolean[] visited;

    public long[] shortestPathDAG(int n, List<List<int[]>> adj, int s) {
        stack = new Stack<>();
        visited = new boolean[n];

        // 1. Topological Sort
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs(i, adj);
        }

        // 2. Initialize Distances
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[s] = 0;

        // 3. Relax in Topological Order
        while (!stack.isEmpty()) {
            int u = stack.pop();
            
            if (dist[u] != Long.MAX_VALUE) {
                for (int[] edge : adj.get(u)) {
                    int v = edge[0];
                    int w = edge[1];
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        // Convert unreachable to -1
        for (int i = 0; i < n; i++) {
            if (dist[i] == Long.MAX_VALUE) dist[i] = -1;
        }
        
        return dist;
    }

    private void dfs(int u, List<List<int[]>> adj) {
        visited[u] = true;
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            if (!visited[v]) dfs(v, adj);
        }
        stack.push(u);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] dist = solution.shortestPathDAG(n, adj, s);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(dist[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python
```python
import sys

# Increase recursion depth
sys.setrecursionlimit(200000)

def shortest_path_dag(n: int, adj: list[list[tuple[int, int]]], s: int) -> list[int]:
    visited = [False] * n
    stack = []
    
    def dfs(u):
        visited[u] = True
        for v, w in adj[u]:
            if not visited[v]:
                dfs(v)
        stack.append(u)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            
    # Stack has reverse topological order (sink first)
    # We pop from stack to get topological order
    
    dist = [float('inf')] * n
    dist[s] = 0
    
    while stack:
        u = stack.pop()
        
        if dist[u] != float('inf'):
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
    return [d if d != float('inf') else -1 for d in dist]

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
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        dist = shortest_path_dag(n, adj, s)
        print(" ".join(map(str, dist)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++
```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
    vector<bool> visited;
    stack<int> st;

    void dfs(int u, const vector<vector<pair<int, int>>>& adj) {
        visited[u] = true;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            if (!visited[v]) dfs(v, adj);
        }
        st.push(u);
    }

public:
    vector<long long> shortestPathDAG(int n, const vector<vector<pair<int, int>>>& adj, int s) {
        visited.assign(n, false);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs(i, adj);
        }

        vector<long long> dist(n, 2e18); // Large value for infinity
        dist[s] = 0;

        while (!st.empty()) {
            int u = st.top();
            st.pop();

            if (dist[u] != 2e18) {
                for (auto& edge : adj[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (dist[i] == 2e18) dist[i] = -1;
        }
        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> dist = solution.shortestPathDAG(n, adj, s);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << dist[i];
    }
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  shortestPathDAG(n, adj, s) {
    const visited = new Int8Array(n).fill(0);
    const stack = [];

    const dfs = (u) => {
      visited[u] = 1;
      for (const [v, w] of adj[u]) {
        if (!visited[v]) dfs(v);
      }
      stack.push(u);
    };

    for (let i = 0; i < n; i++) {
      if (!visited[i]) dfs(i);
    }

    // Initialize distances
    // Use BigInt for safety with large weights, though Number is usually fine up to 2^53
    // Problem constraints 10^9 * 10^5 = 10^14, fits in Number.
    const INF = 1e15;
    const dist = new Array(n).fill(INF);
    dist[s] = 0;

    // Process in topological order (reverse of post-order stack)
    while (stack.length > 0) {
      const u = stack.pop();

      if (dist[u] !== INF) {
        for (const [v, w] of adj[u]) {
          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
          }
        }
      }
    }

    return dist.map((d) => (d === INF ? -1 : d));
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const dist = solution.shortestPathDAG(n, adj, s);
  console.log(dist.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 2 0
0 1 1
1 2 2
```
**Graph:** `0 -> 1 (1)`, `1 -> 2 (2)`.

**Topological Sort:**
-   DFS(0) -> DFS(1) -> DFS(2) -> Push 2 -> Push 1 -> Push 0.
-   Stack: `[2, 1, 0]` (Top is 0).

**Relaxation:**
1.  Pop 0. `dist[0]=0`.
    -   `0->1`: `dist[1] = min(inf, 1) = 1`.
2.  Pop 1. `dist[1]=1`.
    -   `1->2`: `dist[2] = min(inf, 1+2) = 3`.
3.  Pop 2. `dist[2]=3`. No neighbors.

**Output:** `0 1 3`.

## ✅ Proof of Correctness

In a DAG, if there is a path from `u` to `v`, `u` must appear before `v` in the topological sort. When we relax edges from `u`, `dist[u]` is guaranteed to be the shortest distance because all paths to `u` come from nodes that have already been processed.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Longest Path:** Just negate edge weights (or use `max` instead of `min`) and run the same algorithm.
-   **Count Paths:** Use DP on the topological order to count the number of paths from `s` to `t`.
-   **All-Pairs Shortest Path:** In DAG, can be done in O(N*(N+M)) by running this from every node.

### Common Mistakes to Avoid

1.  **Cycle Detection:** This algorithm assumes input is a DAG. If there's a cycle, topological sort is invalid (or partial), and results are meaningless.
2.  **Unreachable Nodes:** Don't relax edges starting from an unreachable node (`dist[u] == INF`).
3.  **Recursion Depth:** For deep DAGs (like a line), Python/JS recursion limit might be hit. Use iterative DFS (Kahn's Algorithm) if needed.
