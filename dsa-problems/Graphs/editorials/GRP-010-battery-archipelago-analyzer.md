---
problem_id: GRP_BATTERY_ARCHIPELAGO__3928
display_id: GRP-010
slug: battery-archipelago-analyzer
title: "Battery Archipelago Analyzer"
difficulty: Medium-Hard
difficulty_score: 65
topics:
  - Shortest Path
  - Dijkstra Variant
  - Custom Constraints
tags:
  - graph
  - dijkstra
  - shortest-path
  - constraints
  - hard
premium: true
subscription_tier: premium
---

# GRP-010: Battery Archipelago Analyzer

## 📋 Problem Summary

Find the minimum cost path between a source and destination in a weighted undirected graph, considering only edges with weights less than or equal to a battery capacity `B`.

## 🌍 Real-World Scenario

**Scenario Title:** EV Route Planning with Range Anxiety

Imagine planning a route for an Electric Vehicle (EV) across an archipelago of islands connected by bridges.
-   **Nodes:** Islands with charging stations.
-   **Edges:** Bridges with specific energy costs (lengths).
-   **Battery Capacity (B):** The maximum energy your car can spend on a *single* bridge crossing without running out of power mid-bridge.
-   **Goal:** Find the route that consumes the least total energy, but you can *only* cross bridges that your battery can handle in one go. If a bridge is too long (weight > B), it's impassable regardless of total path length.

![Real-World Application](../images/GRP-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Constrained Path

**Graph:**
```
      (10)        (50)
  S -------- A -------- D
  |          |          |
  | (20)     | (20)     | (5)
  |          |          |
  +--------- B ---------+
```
**Battery B = 25**

-   **Edge S-A (10):** OK (10 <= 25).
-   **Edge A-D (50):** BLOCKED (50 > 25).
-   **Edge S-B (20):** OK (20 <= 25).
-   **Edge A-B (20):** OK (20 <= 25).
-   **Edge B-D (5):** OK (5 <= 25).

**Valid Paths:**
1.  `S -> A -> B -> D`: Cost `10 + 20 + 5 = 35`.
2.  `S -> B -> D`: Cost `20 + 5 = 25`.

**Shortest Valid Path:** `S -> B -> D` (Cost 25).
Note that `S -> A -> D` would be length 60, but it's invalid because `A -> D` requires 50 battery.

### Algorithm: Constrained Dijkstra

1.  **Filter Edges:** Conceptually, remove all edges with `weight > B`.
2.  **Run Dijkstra:** Perform standard Dijkstra's algorithm on the filtered graph.
    -   Initialize `dist` array with infinity, `dist[s] = 0`.
    -   Use a Priority Queue to pick the node with the smallest distance.
    -   Relax neighbors: For neighbor `v` of `u` with weight `w`:
        -   **Constraint Check:** If `w <= B`:
            -   If `dist[u] + w < dist[v]`:
                -   `dist[v] = dist[u] + w`
                -   `pq.push(v, dist[v])`
3.  **Result:** Return `dist[d]`. If `dist[d]` is still infinity, return `-1`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Graph:** Undirected.
-   **Constraints:** `N` up to 10^5, `M` up to 2*10^5.
-   **Weights:** Up to 10^6.
-   **Battery B:** Up to 10^6.
-   **Output:** -1 if no path exists.

## Naive Approach

### Intuition

BFS or DFS to find all paths, check constraints, and pick minimum.

### Time Complexity

-   **Exponential:** Finding all paths is too slow.

## Optimal Approach (Dijkstra)

### Time Complexity

-   **O(M log N)**: Standard Dijkstra. The constraint check `w <= B` is O(1).

### Space Complexity

-   **O(N + M)**: Adjacency list and distance array.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int shortestPathWithBattery(int n, List<int[]> edges, int source, int dest, int battery) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(new int[]{e[1], e[2]});
            adj.get(e[1]).add(new int[]{e[0], e[2]});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[source] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{source, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0];
            int d = curr[1];

            if (d > dist[u]) continue;
            if (u == dest) return d;

            for (int[] neighbor : adj.get(u)) {
                int v = neighbor[0];
                int w = neighbor[1];

                if (w <= battery) { // Constraint Check
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                        pq.offer(new int[]{v, dist[v]});
                    }
                }
            }
        }

        return dist[dest] == Integer.MAX_VALUE ? -1 : dist[dest];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            edges.add(new int[]{u, v, w});
        }
        
        int source = sc.nextInt();
        int dest = sc.nextInt();
        int battery = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.shortestPathWithBattery(n, edges, source, dest, battery));
        sc.close();
    }
}
```

### Python

```python
import heapq
import sys

def shortest_path_with_battery(n: int, edges: list[tuple[int, int, int]], 
                                source: int, dest: int, battery: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    dist = [float('inf')] * n
    dist[source] = 0
    
    pq = [(0, source)] # (cost, u)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        if u == dest:
            return d
            
        for v, w in adj[u]:
            if w <= battery: # Constraint Check
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
    return -1 if dist[dest] == float('inf') else dist[dest]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        source = int(next(iterator))
        dest = int(next(iterator))
        battery = int(next(iterator))
        
        print(shortest_path_with_battery(n, edges, source, dest, battery))
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
#include <limits>

using namespace std;

class Solution {
public:
    int shortestPathWithBattery(int n, vector<vector<int>>& edges, int source, int dest, int battery) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> dist(n, numeric_limits<int>::max());

        dist[source] = 0;
        pq.push({0, source});

        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;
            if (u == dest) return d;

            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;

                if (w <= battery) { // Constraint Check
                    if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                        pq.push({dist[v], v});
                    }
                }
            }
        }

        return dist[dest] == numeric_limits<int>::max() ? -1 : dist[dest];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<vector<int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }
    
    int source, dest, battery;
    cin >> source >> dest >> battery;
    
    Solution solution;
    cout << solution.shortestPathWithBattery(n, edges, source, dest, battery) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class MinPriorityQueue {
  constructor() {
    this.heap = [];
  }
  
  push(val) {
    this.heap.push(val);
    this._bubbleUp(this.heap.length - 1);
  }
  
  pop() {
    if (this.heap.length === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = bottom;
      this._bubbleDown(0);
    }
    return top;
  }
  
  isEmpty() {
    return this.heap.length === 0;
  }
  
  _bubbleUp(idx) {
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[idx][0] >= this.heap[parentIdx][0]) break;
      [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
      idx = parentIdx;
    }
  }
  
  _bubbleDown(idx) {
    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let smallest = idx;
      
      if (leftIdx < this.heap.length && this.heap[leftIdx][0] < this.heap[smallest][0]) {
        smallest = leftIdx;
      }
      if (rightIdx < this.heap.length && this.heap[rightIdx][0] < this.heap[smallest][0]) {
        smallest = rightIdx;
      }
      if (smallest === idx) break;
      [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
      idx = smallest;
    }
  }
}

class Solution {
  shortestPathWithBattery(n, edges, source, dest, battery) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
      adj[u].push([v, w]);
      adj[v].push([u, w]);
    }
    
    const dist = new Int32Array(n).fill(2147483647); // Max int
    dist[source] = 0;
    
    const pq = new MinPriorityQueue();
    pq.push([0, source]);
    
    while (!pq.isEmpty()) {
      const [d, u] = pq.pop();
      
      if (d > dist[u]) continue;
      if (u === dest) return d;
      
      for (const [v, w] of adj[u]) {
        if (w <= battery) {
          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.push([dist[v], v]);
          }
        }
      }
    }
    
    return dist[dest] === 2147483647 ? -1 : dist[dest];
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
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  const m = parseInt(data[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[ptr++], 10);
    const v = parseInt(data[ptr++], 10);
    const w = parseInt(data[ptr++], 10);
    edges.push([u, v, w]);
  }
  
  const source = parseInt(data[ptr++], 10);
  const dest = parseInt(data[ptr++], 10);
  const battery = parseInt(data[ptr++], 10);
  
  const solution = new Solution();
  console.log(solution.shortestPathWithBattery(n, edges, source, dest, battery));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 5
0 1 10
0 2 50
1 2 20
1 3 30
2 3 5
0 3 25
```
**Battery B = 25**

1.  **Init:** `dist=[0, INF, INF, INF]`, `pq=[(0, 0)]`.
2.  **Pop (0, 0):**
    -   Neighbors of 0:
        -   1 (w=10): 10 <= 25. Update `dist[1]=10`. Push `(10, 1)`.
        -   2 (w=50): 50 > 25. Skip.
3.  **Pop (10, 1):**
    -   Neighbors of 1:
        -   0 (w=10): `10+10 >= 0`. Skip.
        -   2 (w=20): 20 <= 25. Update `dist[2]=10+20=30`. Push `(30, 2)`.
        -   3 (w=30): 30 > 25. Skip.
4.  **Pop (30, 2):**
    -   Neighbors of 2:
        -   0 (w=50): Skip.
        -   1 (w=20): `30+20 >= 10`. Skip.
        -   3 (w=5): 5 <= 25. Update `dist[3]=30+5=35`. Push `(35, 3)`.
5.  **Pop (35, 3):**
    -   Target reached? Yes. Return `dist[3]=35`.

    **Final Output:** 35.

    **Verification:**
    -   Path 0->1->2->3 uses edges with weights 10, 20, 5.
    -   All weights are <= 25 (Battery).
    -   Total Cost: 10 + 20 + 5 = 35.
    -   Other paths like 0->1->3 involve edge 1-3 (weight 30 > 25), so they are invalid.
    -   The logic holds.

## ✅ Proof of Correctness

-   **Dijkstra's Optimality:** Dijkstra guarantees shortest path in non-negative weighted graphs.
-   **Constraint Handling:** By ignoring edges with `w > B`, we effectively run Dijkstra on the subgraph of valid edges. The shortest path in this subgraph is the answer.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Max Capacity Path:** Find path maximizing the bottleneck capacity (Modified Prim's/Dijkstra).
-   **Battery Charging:** If nodes are charging stations, how to reach D with min time? (State space search `(u, charge)`).

### C++ommon Mistakes to Avoid

1.  **Summing Weights vs Max Weight:** The constraint is on *individual* edge weights, not the sum.
2.  **Directed vs Undirected:** Problem is undirected.
3.  **Infinity Check:** Return -1 if destination is unreachable.
