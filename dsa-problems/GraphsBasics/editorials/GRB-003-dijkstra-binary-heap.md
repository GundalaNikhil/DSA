---
problem_id: GRB_DIJKSTRA_BINARY_HEAP__6041
display_id: GRB-003
slug: dijkstra-binary-heap
title: "Dijkstra with Binary Heap"
difficulty: Medium
difficulty_score: 45
topics:
  - Graphs
  - Dijkstra
  - Shortest Path
tags:
  - graphs-basics
  - dijkstra
  - shortest-path
  - medium
premium: true
subscription_tier: basic
---

# GRB-003: Dijkstra with Binary Heap

## 📋 Problem Summary

You are given a directed graph with **non-negative** edge weights. Find the shortest path distance from a source node `s` to all other nodes. If a node is unreachable, the distance is `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** GPS Navigation

Imagine you are driving from your home (source `s`) to various destinations in a city.
-   **Intersections** are nodes.
-   **Roads** are edges.
-   **Traffic/Time** is the edge weight (cost).
-   Some roads are one-way (directed).

You want to find the fastest route to every other location. Unlike the "Six Degrees" game (BFS), roads have different travel times. A short road with heavy traffic (high weight) might be slower than a longer, empty highway (low weight). Dijkstra's algorithm helps your GPS find the path with the minimum total travel time.

![Real-World Application](../images/GRB-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)
  0 ------> 1
  |         |
  | (5)     | (2)
  v         v
  2 <------ 3
      (1)
```
**Source:** 0

**Steps:**
1.  **Start at 0:** Dist to 0 is 0. Push `(0, 0)` to Min-Heap.
2.  **Pop (0, 0):** Neighbors:
    -   1: Cost `0 + 1 = 1`. Push `(1, 1)`.
    -   2: Cost `0 + 5 = 5`. Push `(5, 2)`.
3.  **Pop (1, 1):** Neighbors:
    -   3: Cost `1 + 2 = 3`. Push `(3, 3)`.
4.  **Pop (3, 3):** Neighbors:
    -   2: Cost `3 + 1 = 4`.
    -   Current dist to 2 is 5. `4 < 5`, so update dist to 2. Push `(4, 2)`.
5.  **Pop (4, 2):** No neighbors.
6.  **Pop (5, 2):** Old entry for node 2. `5 > 4` (current best). Ignore.

**Result:** `0:0, 1:1, 2:4, 3:3`

### Algorithm Steps

1.  **Initialization:**
    -   `dist` array initialized to Infinity (`-1` for unreachable in output).
    -   `dist[s] = 0`.
    -   Min-Heap (Priority Queue) storing pairs `(distance, node)`. Push `(0, s)`.
2.  **Processing:**
    -   While heap is not empty:
        -   Pop the element with the smallest distance: `(d, u)`.
        -   **Lazy Deletion Check:** If `d > dist[u]`, this is an outdated entry. Continue/Skip.
        -   For each neighbor `v` of `u` with weight `w`:
            -   If `dist[u] + w < dist[v]`:
                -   `dist[v] = dist[u] + w`
                -   Push `(dist[v], v)` to heap.
3.  **Output:** Convert Infinity to `-1` if necessary and return.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Weights:** Non-negative. This is crucial for Dijkstra.
-   **Large Distances:** Sum of weights can exceed 2^31-1. Use 64-bit integers (`long` in Java/C++, `Number` is safe in JS up to 2^53).
-   **Unreachable:** Output `-1`.

## Naive Approach

### Intuition

We could use a simple array to find the minimum distance node at each step instead of a heap.

### Time Complexity

-   **O(N^2)**: Finding the minimum distance node takes O(N), and we do this N times. This is fine for dense graphs but slow for sparse ones (large N, small M).

## Optimal Approach (Binary Heap)

Using a Min-Heap allows us to extract the closest node in O(log N) time.

### Algorithm

(Described in "Algorithm Steps" above).

### Time Complexity

-   **O(M log N)**: Each edge is processed once, potentially adding an entry to the heap. Heap operations take O(log N).

### Space Complexity

-   **O(N + M)**: Adjacency list + Heap + Distance array.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long[] dijkstra(int n, List<List<int[]>> adj, int s) {
        long[] dist = new long[n];
        Arrays.fill(dist, -1);
        
        // PriorityQueue stores {distance, node}
        // Use Long for distance to prevent overflow
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        
        dist[s] = 0;
        pq.offer(new long[]{0, s});
        
        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long d = curr[0];
            int u = (int) curr[1];
            
            // Lazy deletion: if we found a shorter path to u before processing this entry, skip
            if (d > dist[u] && dist[u] != -1) continue;
            
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int w = edge[1];
                
                if (dist[v] == -1 || dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.offer(new long[]{dist[v], v});
                }
            }
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
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] dist = solution.dijkstra(n, adj, s);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(dist[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def dijkstra(n: int, adj: list[list[tuple[int, int]]], s: int) -> list[int]:
    dist = [-1] * n
    dist[s] = 0
    
    # Min-heap stores (distance, node)
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Lazy deletion check
        if dist[u] != -1 and d > dist[u]:
            continue
        
        for v, w in adj[u]:
            if dist[v] == -1 or dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

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
            
        dist = dijkstra(n, adj, s)
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
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    vector<long long> dijkstra(int n, const vector<vector<pair<int, int>>>& adj, int s) {
        vector<long long> dist(n, -1);
        
        // Min-priority queue: stores {distance, node}
        // Use greater to make it a min-heap
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        
        dist[s] = 0;
        pq.push({0, s});
        
        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            // Lazy deletion check
            if (dist[u] != -1 && d > dist[u]) continue;
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                
                if (dist[v] == -1 || dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
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
    vector<long long> dist = solution.dijkstra(n, adj, s);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << dist[i];
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

// Simple MinPriorityQueue implementation since JS doesn't have a built-in one
class MinPriorityQueue {
  constructor() {
    this.heap = [];
  }

  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }

  pop() {
    if (this.heap.length === 0) return null;
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.sinkDown(0);
    }
    return min;
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  bubbleUp(idx) {
    const element = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (element.priority >= parent.priority) break;
      this.heap[parentIdx] = element;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
  }

  sinkDown(idx) {
    const length = this.heap.length;
    const element = this.heap[idx];
    while (true) {
      let leftChildIdx = 2 * idx + 1;
      let rightChildIdx = 2 * idx + 2;
      let swap = null;

      if (leftChildIdx < length) {
        let leftChild = this.heap[leftChildIdx];
        if (leftChild.priority < element.priority) {
          swap = leftChildIdx;
        }
      }

      if (rightChildIdx < length) {
        let rightChild = this.heap[rightChildIdx];
        if (
          (swap === null && rightChild.priority < element.priority) ||
          (swap !== null && rightChild.priority < this.heap[swap].priority)
        ) {
          swap = rightChildIdx;
        }
      }

      if (swap === null) break;
      this.heap[idx] = this.heap[swap];
      this.heap[swap] = element;
      idx = swap;
    }
  }
}

class Solution {
  dijkstra(n, adj, s) {
    const dist = new Array(n).fill(-1);
    const pq = new MinPriorityQueue();

    dist[s] = 0;
    pq.push({ priority: 0, node: s });

    while (!pq.isEmpty()) {
      const { priority: d, node: u } = pq.pop();

      if (dist[u] !== -1 && d > dist[u]) continue;

      for (const [v, w] of adj[u]) {
        if (dist[v] === -1 || dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          pq.push({ priority: dist[v], node: v });
        }
      }
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
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(tokens[ptr++], 10);
    const v = parseInt(tokens[ptr++], 10);
    const w = parseInt(tokens[ptr++], 10);
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const dist = solution.dijkstra(n, adj, s);
  console.log(dist.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3 0
0 1 1
1 2 2
0 2 5
```

**Initialization:**
-   `dist`: `[0, -1, -1]`
-   `pq`: `[(0, 0)]`

**Step 1:**
-   Pop `(0, 0)`. Neighbors: `1 (w=1)`, `2 (w=5)`.
-   Update `dist[1] = 1`. Push `(1, 1)`.
-   Update `dist[2] = 5`. Push `(5, 2)`.
-   `pq`: `[(1, 1), (5, 2)]`

**Step 2:**
-   Pop `(1, 1)`. Neighbors: `2 (w=2)`.
-   New path to 2: `dist[1] + 2 = 1 + 2 = 3`.
-   `3 < 5` (current `dist[2]`). Update `dist[2] = 3`. Push `(3, 2)`.
-   `pq`: `[(3, 2), (5, 2)]` (Note: `(5, 2)` is now outdated).

**Step 3:**
-   Pop `(3, 2)`. Neighbors: None.

**Step 4:**
-   Pop `(5, 2)`. `dist[2]` is 3. `5 > 3`. Ignore.

**Result:** `0 1 3`

## ✅ Proof of Correctness

Dijkstra's greedy strategy works because:
1.  We always process the closest unvisited node.
2.  Since weights are non-negative, extending a path can never reduce its total weight.
3.  Therefore, once we extract a node from the heap, we have found the absolute shortest path to it.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Path Restoration:** Store `parent[v] = u` when relaxing edges to reconstruct the path.
-   **Dense Graphs:** For dense graphs (M ≈ N^2), the O(N^2) array implementation is actually faster than O(M log N) heap implementation.
-   **Negative Weights:** Dijkstra fails. Use Bellman-Ford.

### Common Mistakes to Avoid

1.  **Negative Edges:** Dijkstra loops infinitely or gives wrong answers with negative weights.
2.  **Visited Array:** Standard Dijkstra doesn't use a simple boolean `visited` array like BFS. It uses the distance check `d > dist[u]` to handle re-visits/updates.
3.  **Integer Overflow:** Edge weights can sum up to > 2 billion. Use `long long` in C++ / `long` in Java.
