---
problem_id: AGR_K_SHORTEST_LOOPLESS_PATHS__2749
display_id: AGR-003
slug: k-shortest-loopless-paths
title: "K Shortest Paths (Loopless)"
difficulty: Medium
difficulty_score: 62
topics:
  - Graphs
  - Shortest Path
  - Yen Algorithm
tags:
  - advanced-graphs
  - k-shortest
  - yen
  - medium
premium: true
subscription_tier: basic
---

# AGR-003: K Shortest Paths (Loopless)

## 📋 Problem Summary

Find the `K` shortest **simple** paths (paths without repeated vertices) from a source `s` to a target `t`. Output their lengths in ascending order.

## 🌍 Real-World Scenario

**Scenario Title:** GPS Route Alternatives

When you use Google Maps, it doesn't just show the single fastest route. It often suggests "Route 1 (20 mins)", "Route 2 (22 mins)", etc.
-   **Constraint:** Drivers don't want to drive in circles (loops).
-   **Goal:** Provide the top `K` distinct, loop-free options so the user can choose based on preference (e.g., avoiding highways).

![Real-World Application](../images/AGR-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)      (1)
  A -----> B -----> C
  |                 ^
  |       (3)       |
  +-----------------+
```
**Paths from A to C:**
1.  `A -> B -> C`: Cost `1 + 1 = 2`. (Shortest)
2.  `A -> C`: Cost `3`. (2nd Shortest)

**Yen's Algorithm Logic:**
-   Find 1st shortest: `P1 = [A, B, C]`.
-   **Deviate from A:** Ban edge `A->B`. Find shortest `A->...->C`. Result: `A->C` (cost 3).
-   **Deviate from B:** Ban edge `B->C`. Find shortest `B->...->C`. No other path.
-   Candidate: `A->C`. Add to results.

### Algorithm: Yen's Algorithm

Yen's algorithm finds the `k`-th shortest path by exploring deviations from the `(k-1)`-th shortest path.

1.  **Initialization:** Find the 1st shortest path `A[0]` using Dijkstra. Add to `result`.
2.  **Iterate k from 1 to K-1:**
    -   Let `prevPath = A[k-1]`.
    -   For each node `spurNode` in `prevPath` (except the last one):
        -   **Root Path:** The sub-path from `source` to `spurNode`.
        -   **Spur Path:** Find the shortest path from `spurNode` to `target` in the graph, subject to:
            -   **Edge Constraints:** Remove edges that were part of previous shortest paths starting with the same Root Path (to force a new route).
            -   **Node Constraints:** Remove nodes in Root Path (to ensure the path is simple/loopless).
        -   **Total Path:** Root Path + Spur Path. Add to `candidates` heap.
    -   Extract the shortest path from `candidates`. This is `A[k]`.
    -   Add `A[k]` to `result`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Simple Paths:** Crucial. Standard Eppstein’s algorithm finds paths with loops. Yen's handles simple paths if we explicitly block Root Path nodes.
-   **Output:** Only lengths. If fewer than K exist, output as many as found.
-   **Constraints:** N=500, K=50. Yen's is `O(K * N * (M + N log N))`. With N=500, this is roughly `50 * 500 * 5000` ops, which is heavy but passable in 2s.

## Naive Approach

### Intuition

DFS to find ALL paths, sort them, pick top K.

### Time Complexity

-   **Exponential**: Number of simple paths can be `N!`. Impossible for N=500.

## Optimal Approach (Yen's Algorithm)

### Time Complexity

-   **O(K * N * (M + N log N))**: In each of K iterations, we run Dijkstra up to N times (once for each spur node).

### Space Complexity

-   **O(N^2 + K * N)**: Storing graph and K paths.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        int weight;
        Edge(int to, int weight) { this.to = to; this.weight = weight; }
    }

    static class Path implements Comparable<Path> {
        List<Integer> nodes;
        long cost;

        Path(List<Integer> nodes, long cost) {
            this.nodes = new ArrayList<>(nodes);
            this.cost = cost;
        }

        @Override
        public int compareTo(Path other) {
            return Long.compare(this.cost, other.cost);
        }
    }

    public long[] kShortestPaths(int n, List<List<int[]>> adjList, int s, int t, int k) {
        // Convert to easier format
        List<List<Edge>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int u = 0; u < n; u++) {
            for (int[] e : adjList.get(u)) {
                adj.get(u).add(new Edge(e[0], e[1]));
            }
        }

        List<Path> A = new ArrayList<>();
        PriorityQueue<Path> B = new PriorityQueue<>();

        // 1. First shortest path
        Path p0 = getShortestPath(n, adj, s, t, new HashSet<>(), new HashSet<>());
        if (p0 == null) return new long[0];
        A.add(p0);

        // 2. Find k-1 more
        for (int i = 1; i < k; i++) {
            Path prevPath = A.get(i - 1);
            
            // Spur node ranges from first node to second-to-last node
            for (int j = 0; j < prevPath.nodes.size() - 1; j++) {
                int spurNode = prevPath.nodes.get(j);
                List<Integer> rootPathNodes = prevPath.nodes.subList(0, j + 1);
                long rootPathCost = 0;
                // Calculate root path cost (could optimize)
                // We assume prevPath is valid, so we can just sum edges? 
                // Better: store costs in Path or recompute. Recomputing is safer.
                
                // Constraints
                Set<Integer> forbiddenNodes = new HashSet<>(rootPathNodes);
                forbiddenNodes.remove(spurNode); // Spur node is allowed as start
                
                Set<String> forbiddenEdges = new HashSet<>();
                for (Path p : A) {
                    if (p.nodes.size() > j && p.nodes.subList(0, j + 1).equals(rootPathNodes)) {
                        int u = p.nodes.get(j);
                        int v = p.nodes.get(j + 1);
                        forbiddenEdges.add(u + "," + v);
                    }
                }

                Path spurPath = getShortestPath(n, adj, spurNode, t, forbiddenNodes, forbiddenEdges);
                
                if (spurPath != null) {
                    List<Integer> totalNodes = new ArrayList<>(rootPathNodes);
                    totalNodes.remove(totalNodes.size() - 1); // Remove duplicate spurNode
                    totalNodes.addAll(spurPath.nodes);
                    
                    // Calculate total cost
                    // We need exact cost. getShortestPath returns cost of spur part.
                    // We need cost of root part.
                    long currentRootCost = 0;
                    for(int x=0; x<j; x++) {
                        int u = prevPath.nodes.get(x);
                        int v = prevPath.nodes.get(x+1);
                        for(Edge e : adj.get(u)) if(e.to == v) { currentRootCost += e.weight; break; }
                    }
                    
                    Path totalPath = new Path(totalNodes, currentRootCost + spurPath.cost);
                    
                    // Avoid duplicates in B
                    boolean exists = false;
                    for(Path p : B) {
                        if (p.nodes.equals(totalPath.nodes)) { exists = true; break; }
                    }
                    if (!exists) B.add(totalPath);
                }
            }

            if (B.isEmpty()) break;
            A.add(B.poll());
        }

        long[] result = new long[A.size()];
        for (int i = 0; i < A.size(); i++) result[i] = A.get(i).cost;
        return result;
    }

    private Path getShortestPath(int n, List<List<Edge>> adj, int s, int t, 
                                 Set<Integer> forbiddenNodes, Set<String> forbiddenEdges) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        dist[s] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.add(new long[]{0, s});

        while (!pq.isEmpty()) {
            long[] top = pq.poll();
            long d = top[0];
            int u = (int) top[1];

            if (d > dist[u]) continue;
            if (u == t) break;

            for (Edge e : adj.get(u)) {
                if (forbiddenNodes.contains(e.to)) continue;
                if (forbiddenEdges.contains(u + "," + e.to)) continue;

                if (dist[u] + e.weight < dist[e.to]) {
                    dist[e.to] = dist[u] + e.weight;
                    parent[e.to] = u;
                    pq.add(new long[]{dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == Long.MAX_VALUE) return null;

        List<Integer> nodes = new ArrayList<>();
        int curr = t;
        while (curr != -1) {
            nodes.add(curr);
            curr = parent[curr];
        }
        Collections.reverse(nodes);
        return new Path(nodes, dist[t]);
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
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] paths = solution.kShortestPaths(n, adj, s, t, k);
        StringBuilder sb = new StringBuilder();
        sb.append(paths.length).append('\n');
        for (int i = 0; i < paths.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(paths[i]);
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

def k_shortest_paths(n: int, adj: list[list[tuple[int, int]]], s: int, t: int, k: int) -> list[int]:
    
    def get_shortest_path(start_node, end_node, forbidden_nodes, forbidden_edges):
        dist = {i: float('inf') for i in range(n)}
        parent = {i: -1 for i in range(n)}
        dist[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]: continue
            if u == end_node: break
            
            for v, w in adj[u]:
                if v in forbidden_nodes: continue
                if (u, v) in forbidden_edges: continue
                
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
                    
        if dist[end_node] == float('inf'):
            return None, float('inf')
            
        path = []
        curr = end_node
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        return path[::-1], dist[end_node]

    A = [] # List of (cost, path)
    B = [] # Heap of (cost, path)
    
    # 1. First shortest path
    path0, cost0 = get_shortest_path(s, t, set(), set())
    if not path0:
        return []
    A.append((cost0, path0))
    
    # 2. Find k-1 more
    for k_idx in range(1, k):
        prev_path = A[-1][1]
        
        for i in range(len(prev_path) - 1):
            spur_node = prev_path[i]
            root_path = prev_path[:i+1]
            
            # Calculate root path cost
            root_cost = 0
            for j in range(i):
                u, v = root_path[j], root_path[j+1]
                for neighbor, weight in adj[u]:
                    if neighbor == v:
                        root_cost += weight
                        break
            
            forbidden_nodes = set(root_path)
            forbidden_nodes.remove(spur_node)
            
            forbidden_edges = set()
            for cost, path in A:
                if len(path) > i and path[:i+1] == root_path:
                    forbidden_edges.add((path[i], path[i+1]))
            
            spur_path, spur_cost = get_shortest_path(spur_node, t, forbidden_nodes, forbidden_edges)
            
            if spur_path:
                total_path = root_path[:-1] + spur_path
                total_cost = root_cost + spur_cost
                
                # Check duplicates (inefficient but simple for small K)
                is_duplicate = False
                for cost, path in B:
                    if path == total_path:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    heapq.heappush(B, (total_cost, total_path))
                    
        if not B:
            break
            
        # Extract best from B
        # Note: B might contain duplicates if we pushed same path from different spur nodes
        # We handled check before push, but let's be safe.
        
        while B:
            cost, path = heapq.heappop(B)
            # Check if already in A
            in_A = False
            for ac, ap in A:
                if ap == path:
                    in_A = True
                    break
            if not in_A:
                A.append((cost, path))
                break
        
        if len(A) <= k_idx: # Could not find new path
            break
            
    return [cost for cost, path in A]

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
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        paths = k_shortest_paths(n, adj, s, t, k)
        print(len(paths))
        print(" ".join(map(str, paths)))
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
#include <set>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    int weight;
};

struct Path {
    vector<int> nodes;
    long long cost;

    bool operator<(const Path& other) const {
        if (cost != other.cost) return cost < other.cost;
        return nodes < other.nodes;
    }
    bool operator>(const Path& other) const {
        return other < *this;
    }
    bool operator==(const Path& other) const {
        return cost == other.cost && nodes == other.nodes;
    }
};

class Solution {
    vector<vector<Edge>> adj;
    int N;

    Path getShortestPath(int s, int t, const set<int>& forbiddenNodes, const set<pair<int, int>>& forbiddenEdges) {
        vector<long long> dist(N, INF);
        vector<int> parent(N, -1);
        dist[s] = 0;

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, s});

        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;
            if (u == t) break;

            for (const auto& e : adj[u]) {
                if (forbiddenNodes.count(e.to)) continue;
                if (forbiddenEdges.count({u, e.to})) continue;

                if (dist[u] + e.weight < dist[e.to]) {
                    dist[e.to] = dist[u] + e.weight;
                    parent[e.to] = u;
                    pq.push({dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == INF) return {{}, -1};

        vector<int> nodes;
        int curr = t;
        while (curr != -1) {
            nodes.push_back(curr);
            curr = parent[curr];
        }
        reverse(nodes.begin(), nodes.end());
        return {nodes, dist[t]};
    }

public:
    vector<long long> kShortestPaths(int n, const vector<vector<pair<int, int>>>& adjList, int s, int t, int k) {
        N = n;
        adj.assign(n, vector<Edge>());
        for (int u = 0; u < n; u++) {
            for (auto& p : adjList[u]) {
                adj[u].push_back({p.first, p.second});
            }
        }

        vector<Path> A;
        set<Path> B; // Use set to keep sorted and unique candidates

        Path p0 = getShortestPath(s, t, {}, {});
        if (p0.cost == -1) return {};
        A.push_back(p0);

        for (int i = 1; i < k; i++) {
            Path prevPath = A.back();

            for (size_t j = 0; j < prevPath.nodes.size() - 1; j++) {
                int spurNode = prevPath.nodes[j];
                vector<int> rootPathNodes(prevPath.nodes.begin(), prevPath.nodes.begin() + j + 1);
                
                long long rootCost = 0;
                for (size_t x = 0; x < j; x++) {
                    int u = prevPath.nodes[x];
                    int v = prevPath.nodes[x+1];
                    for (auto& e : adj[u]) if (e.to == v) { rootCost += e.weight; break; }
                }

                set<int> forbiddenNodes(rootPathNodes.begin(), rootPathNodes.end());
                forbiddenNodes.erase(spurNode);

                set<pair<int, int>> forbiddenEdges;
                for (const auto& p : A) {
                    if (p.nodes.size() > j && 
                        vector<int>(p.nodes.begin(), p.nodes.begin() + j + 1) == rootPathNodes) {
                        forbiddenEdges.insert({p.nodes[j], p.nodes[j+1]});
                    }
                }

                Path spurPath = getShortestPath(spurNode, t, forbiddenNodes, forbiddenEdges);

                if (spurPath.cost != -1) {
                    vector<int> totalNodes = rootPathNodes;
                    totalNodes.pop_back();
                    totalNodes.insert(totalNodes.end(), spurPath.nodes.begin(), spurPath.nodes.end());
                    
                    Path totalPath = {totalNodes, rootCost + spurPath.cost};
                    B.insert(totalPath);
                }
            }

            if (B.empty()) break;
            
            // Move best from B to A
            // Since B is a set, begin() is the smallest
            A.push_back(*B.begin());
            B.erase(B.begin());
        }

        vector<long long> result;
        for (const auto& p : A) result.push_back(p.cost);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> paths = solution.kShortestPaths(n, adj, s, t, k);
    cout << paths.size() << "\n";
    for (int i = 0; i < (int)paths.size(); i++) {
        if (i) cout << ' ';
        cout << paths[i];
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
  kShortestPaths(n, adj, s, t, k) {
    const INF = 1e15;

    const getShortestPath = (start, end, forbiddenNodes, forbiddenEdges) => {
      const dist = new Array(n).fill(INF);
      const parent = new Array(n).fill(-1);
      dist[start] = 0;
      
      const pq = new PriorityQueue((a, b) => a.d - b.d);
      pq.push({ d: 0, u: start });

      while (!pq.isEmpty()) {
        const { d, u } = pq.pop();
        if (d > dist[u]) continue;
        if (u === end) break;

        for (const [v, w] of adj[u]) {
          if (forbiddenNodes.has(v)) continue;
          if (forbiddenEdges.has(`${u},${v}`)) continue;

          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            parent[v] = u;
            pq.push({ d: dist[v], u: v });
          }
        }
      }

      if (dist[end] === INF) return null;

      const path = [];
      let curr = end;
      while (curr !== -1) {
        path.push(curr);
        curr = parent[curr];
      }
      path.reverse();
      return { nodes: path, cost: dist[end] };
    };

    const A = [];
    const B = new PriorityQueue((a, b) => a.cost - b.cost);
    const B_set = new Set(); // To avoid duplicates in B

    const p0 = getShortestPath(s, t, new Set(), new Set());
    if (!p0) return [];
    A.push(p0);

    for (let i = 1; i < k; i++) {
      const prevPath = A[A.length - 1];

      for (let j = 0; j < prevPath.nodes.length - 1; j++) {
        const spurNode = prevPath.nodes[j];
        const rootPathNodes = prevPath.nodes.slice(0, j + 1);
        
        let rootCost = 0;
        for (let x = 0; x < j; x++) {
          const u = prevPath.nodes[x];
          const v = prevPath.nodes[x + 1];
          for (const [neighbor, w] of adj[u]) {
            if (neighbor === v) { rootCost += w; break; }
          }
        }

        const forbiddenNodes = new Set(rootPathNodes);
        forbiddenNodes.delete(spurNode);

        const forbiddenEdges = new Set();
        for (const p of A) {
          if (p.nodes.length > j && 
              p.nodes.slice(0, j + 1).every((val, idx) => val === rootPathNodes[idx])) {
            forbiddenEdges.add(`${p.nodes[j]},${p.nodes[j + 1]}`);
          }
        }

        const spurPath = getShortestPath(spurNode, t, forbiddenNodes, forbiddenEdges);

        if (spurPath) {
          const totalNodes = rootPathNodes.slice(0, -1).concat(spurPath.nodes);
          const totalCost = rootCost + spurPath.cost;
          const totalPathStr = JSON.stringify(totalNodes);

          if (!B_set.has(totalPathStr)) {
            B.push({ nodes: totalNodes, cost: totalCost, str: totalPathStr });
            B_set.add(totalPathStr);
          }
        }
      }

      if (B.isEmpty()) break;
      
      // Extract best unique path
      // B might contain paths already in A?
      // No, because we forbid edges used in A.
      // But we should check just in case logic is loose.
      // Standard Yen guarantees new paths.
      
      const best = B.pop();
      A.push(best);
    }

    return A.map(p => p.cost);
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const paths = solution.kShortestPaths(n, adj, s, t, k);
  console.log(paths.length.toString());
  console.log(paths.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3 0 2 2
0 1 1
1 2 1
0 2 3
```
**Initialization:**
-   Shortest path `p0`: `0->1->2` (cost 2). `A = [p0]`.

**Iteration k=1:**
-   `prevPath = 0->1->2`.
-   **Spur Node 0:**
    -   Root Path: `[0]`. Root Cost: 0.
    -   Forbidden Edges: `(0,1)` (from p0).
    -   Shortest path `0->2` avoiding `(0,1)`: `0->2` (cost 3).
    -   Total: `0->2` (cost 3). Add to B.
-   **Spur Node 1:**
    -   Root Path: `[0, 1]`. Root Cost: 1.
    -   Forbidden Edges: `(1,2)` (from p0).
    -   Forbidden Nodes: `0`.
    -   Shortest path `1->2` avoiding `(1,2)`: None.
-   **Best from B:** `0->2` (cost 3). `A = [p0, p1]`.

**Result:** 2 paths, costs 2 and 3.

## ✅ Proof of Correctness

Yen's algorithm partitions the set of all simple paths. By systematically deviating from every node of every previously found shortest path, it ensures that no path is missed. The use of a heap guarantees we always pick the next smallest cost.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Eppstein's Algorithm:** Finds K shortest paths *allowing loops* in `O(M + N log N + K)`. Much faster but harder to implement.
-   **A* Search:** Use A* with Yen's for faster spur path finding if coordinates are available.

### C++ommon Mistakes to Avoid

1.  **Loopless Constraint:** Yen's naturally handles loops if you don't block root path nodes. For *simple* paths, you MUST block nodes in `rootPath` (except `spurNode`).
2.  **Duplicate Paths:** Different spur nodes can generate the same path. Use a Set or check before adding to heap.
3.  **Edge Removal:** Only remove the specific edge `u->v`, not all edges between `u` and `v` (if multigraph).
