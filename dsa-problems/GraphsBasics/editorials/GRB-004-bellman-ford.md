---
problem_id: GRB_BELLMAN_FORD__3812
display_id: GRB-004
slug: bellman-ford
title: "Bellman-Ford with Negative Edges"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
  - Shortest Path
  - Bellman-Ford
tags:
  - graphs-basics
  - bellman-ford
  - shortest-path
  - medium
premium: true
subscription_tier: basic
---

# GRB-004: Bellman-Ford with Negative Edges

## 📋 Problem Summary

You are given a directed graph with edges that can have **negative weights**. Find the shortest path distance from a source node `s` to all other nodes. If the graph contains a **negative cycle** reachable from `s`, output `NEGATIVE CYCLE`.

## 🌍 Real-World Scenario

**Scenario Title:** Currency Arbitrage

Imagine you are trading currencies.
-   **Nodes** are currencies (USD, EUR, JPY).
-   **Edges** are exchange rates.
-   **Weights:** Usually, we multiply rates, but if we take logarithms, we can turn multiplication into addition. A "negative weight" in this context could represent a profitable trade loop.
-   **Negative Cycle:** This is an "infinite money glitch" (Arbitrage). If you can trade USD -> EUR -> JPY -> USD and end up with *more* USD than you started, you can repeat this forever for infinite profit. In shortest path terms, the "cost" keeps decreasing forever.

The Bellman-Ford algorithm detects if such a loop exists.

![Real-World Application](../images/GRB-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      -1
  0 -----> 1
  ^        |
  | -1     | -1
  |        v
  3 <----- 2
```
**Cycle:** `0 -> 1 -> 2 -> 3 -> 0`
**Total Weight:** `-1 + (-1) + (-1) + (-1) = -4`.

**Analysis:**
-   Every time you go around this loop, the total distance decreases by 4.
-   Shortest path to any node in this loop is effectively $-\infty$.
-   Bellman-Ford detects this because distances keep updating even after `N-1` iterations.

### Algorithm Steps

1.  **Initialization:**
    -   `dist` array initialized to Infinity (`1e18` or similar large value).
    -   `dist[s] = 0`.
2.  **Relaxation (N-1 times):**
    -   Loop `i` from `1` to `n-1`.
    -   For every edge `(u, v, w)` in the graph:
        -   If `dist[u] != Infinity` and `dist[u] + w < dist[v]`:
            -   `dist[v] = dist[u] + w`.
3.  **Negative Cycle Check (N-th iteration):**
    -   Iterate through all edges one last time.
    -   If any edge `(u, v, w)` can *still* be relaxed (`dist[u] + w < dist[v]`), it means there is a negative cycle reachable from `s`.
4.  **Output:**
    -   If cycle detected: Print `NEGATIVE CYCLE`.
    -   Else: Print `dist` array (convert Infinity to `-1`).

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Negative Weights:** Allowed.
-   **Negative Cycle:** A cycle where the sum of edge weights is negative.
-   **Reachable:** The cycle must be reachable from `s`. An unreachable negative cycle doesn't affect the shortest path from `s`.
-   **Infinity:** Use a value larger than any possible path (e.g., `1e18` for 64-bit integers).

## Naive Approach

### Intuition

Dijkstra's algorithm is the standard for shortest paths, but it fails with negative edges because it assumes that once a node is visited, its distance cannot be improved. With negative edges, you might find a "longer" path (more edges) that has a smaller total weight later on.

### Failure Case

`A -> B (cost 2)`, `A -> C (cost 5)`, `C -> B (cost -10)`.
Dijkstra might finalize B at cost 2. But `A -> C -> B` costs `5 - 10 = -5`. Dijkstra misses this.

## Optimal Approach (Bellman-Ford)

Bellman-Ford relaxes *all* edges `N-1` times. The intuition is that the shortest path in a graph with `N` nodes can have at most `N-1` edges (if it's simple). If we can still improve a path after `N-1` iterations, it must be because we are finding a path with `N` edges or more, which implies a cycle. If that cycle reduces the cost, it's a negative cycle.

### Time Complexity

-   **O(N * M)**: We iterate `N` times, and in each iteration, we check all `M` edges.

### Space Complexity

-   **O(N)**: Only need to store the `dist` array.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long[] bellmanFord(int n, int s, int[][] edges) {
        long[] dist = new long[n];
        long INF = (long) 1e18;
        Arrays.fill(dist, INF);
        dist[s] = 0;

        // Relax edges N-1 times
        for (int i = 0; i < n - 1; i++) {
            boolean changed = false;
            for (int[] edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if (dist[u] != INF && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    changed = true;
                }
            }
            if (!changed) break; // Optimization
        }

        // Check for negative cycle
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (dist[u] != INF && dist[u] + w < dist[v]) {
                return null; // Negative cycle detected
            }
        }

        // Convert INF to -1 for output
        for (int i = 0; i < n; i++) {
            if (dist[i] == INF) dist[i] = -1;
        }

        return dist;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        long[] dist = solution.bellmanFord(n, s, edges);
        if (dist == null) {
            System.out.print("NEGATIVE CYCLE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i > 0) sb.append(' ');
                sb.append(dist[i]);
            }
            System.out.print(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
import sys

def bellman_ford(n: int, s: int, edges: list[tuple[int, int, int]]):
    INF = float('inf')
    dist = [INF] * n
    dist[s] = 0
    
    # Relax edges N-1 times
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
            
    # Check for negative cycle
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None # Negative cycle detected
            
    # Convert INF to -1
    return [-1 if d == INF else d for d in dist]

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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        dist = bellman_ford(n, s, edges)
        if dist is None:
            print("NEGATIVE CYCLE")
        else:
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
#include <array>

using namespace std;

class Solution {
public:
    vector<long long> bellmanFord(int n, int s, const vector<array<int, 3>>& edges) {
        const long long INF = 1e18;
        vector<long long> dist(n, INF);
        dist[s] = 0;

        // Relax edges N-1 times
        for (int i = 0; i < n - 1; ++i) {
            bool changed = false;
            for (const auto& edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if (dist[u] != INF && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    changed = true;
                }
            }
            if (!changed) break;
        }

        // Check for negative cycle
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (dist[u] != INF && dist[u] + w < dist[v]) {
                return {}; // Empty vector signals negative cycle
            }
        }

        for (int i = 0; i < n; ++i) {
            if (dist[i] == INF) dist[i] = -1;
        }

        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<long long> dist = solution.bellmanFord(n, s, edges);

    if (dist.empty()) {
        cout << "NEGATIVE CYCLE";
    } else {
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << dist[i];
        }
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  bellmanFord(n, s, edges) {
    const INF = Number.MAX_SAFE_INTEGER;
    const dist = new Array(n).fill(INF);
    dist[s] = 0;

    // Relax edges N-1 times
    for (let i = 0; i < n - 1; i++) {
      let changed = false;
      for (const [u, v, w] of edges) {
        if (dist[u] !== INF && dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          changed = true;
        }
      }
      if (!changed) break;
    }

    // Check for negative cycle
    for (const [u, v, w] of edges) {
      if (dist[u] !== INF && dist[u] + w < dist[v]) {
        return null; // Negative cycle
      }
    }

    // Convert INF to -1
    for (let i = 0; i < n; i++) {
      if (dist[i] === INF) dist[i] = -1;
    }

    return dist;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = parseInt(tokens[ptr++], 10);
  const m = parseInt(tokens[ptr++], 10);
  const s = parseInt(tokens[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(tokens[ptr++], 10);
    const v = parseInt(tokens[ptr++], 10);
    const w = parseInt(tokens[ptr++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  const dist = solution.bellmanFord(n, s, edges);
  
  if (dist === null) {
    console.log("NEGATIVE CYCLE");
  } else {
    console.log(dist.join(" "));
  }
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
2 2 0
0 1 -1
1 0 -1
```

**Initialization:**
-   `dist`: `[0, INF]`

**Iteration 1:**
-   Edge `0 -> 1` (w=-1): `dist[0] != INF`. `0 + (-1) < INF`. Update `dist[1] = -1`.
-   Edge `1 -> 0` (w=-1): `dist[1] != INF`. `-1 + (-1) < 0`. Update `dist[0] = -2`.
-   `dist`: `[-2, -1]`

**Iteration 2 (Negative Cycle Check):**
-   Edge `0 -> 1` (w=-1): `dist[0] = -2`. `-2 + (-1) = -3`. `dist[1] = -1`.
-   `-3 < -1`. Condition holds!
-   **Output:** `NEGATIVE CYCLE`.

## ✅ Proof of Correctness

1.  **Shortest Path Property:** A shortest path in a graph with `N` nodes and no negative cycles can have at most `N-1` edges.
2.  **Relaxation:** After `k` iterations of relaxing all edges, we have found the shortest paths with at most `k` edges.
3.  **Convergence:** After `N-1` iterations, all shortest paths (without cycles) are found.
4.  **Detection:** If a distance can still be reduced after `N-1` iterations, it implies a path with `N` edges is shorter, which means a node is repeated, forming a cycle with negative total weight.

## 💡 Interview Extensions (High-Value Add-ons)

-   **SPFA (Shortest Path Faster Algorithm):** An optimization of Bellman-Ford using a queue. Faster on average (O(kM)), but worst case is still exponential.
-   **Find the Cycle:** Instead of just returning true/false, reconstruct the nodes in the negative cycle (use `parent` array).
-   **Longest Path:** In a DAG, negate weights and run Bellman-Ford (or just use Topo Sort).

### C++ommon Mistakes to Avoid

1.  **Unreachable Nodes:** Don't relax edges coming from `INF` distance nodes (`if dist[u] != INF`).
2.  **Disconnected Negative Cycles:** A negative cycle might exist but be unreachable from `s`. The problem usually asks for cycles *reachable* from `s`. Our implementation handles this by checking `dist[u] != INF`.
3.  **Order of Edges:** The order in which edges are processed can affect how quickly distances converge, but the result after `N-1` iterations is guaranteed to be correct.
