---
problem_id: GRB_MST_PRIM__9142
display_id: GRB-008
slug: mst-prim
title: "MST Prim"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - Priority Queue
tags:
  - graphs-basics
  - mst
  - prim
  - medium
premium: true
subscription_tier: basic
---

# GRB-008: MST Prim

## 📋 Problem Summary

Given a connected, undirected, weighted graph, find the **Minimum Spanning Tree (MST)** using **Prim's Algorithm**.

## 🌍 Real-World Scenario

**Scenario Title:** Road Paving

Imagine you are a city planner who needs to pave roads to connect `N` neighborhoods.
-   **Nodes** are neighborhoods.
-   **Edges** are unpaved dirt roads.
-   **Weights** are the costs to pave them.
-   **Prim's Strategy:** Start from one neighborhood (say, Downtown). Look at all dirt roads leading out of Downtown. Pave the cheapest one to reach a new neighborhood. Now you have a connected cluster of 2 neighborhoods. Look at all dirt roads leading out of *either* of these 2. Pave the cheapest one that leads to a *new* (unconnected) neighborhood. Repeat until everyone is connected.

This "growing blob" approach is Prim's Algorithm.

![Real-World Application](../images/GRB-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (1)
  0 ------- 1
  | \       |
  |  \ (3)  | (2)
  |   \     |
 (4)   \    |
  |     \   |
  3 ------- 2
      (5)
```
**Start at 0.**
1.  **Neighbors of 0:** `1(1), 2(3), 3(4)`.
2.  **Pick Min:** `(0, 1)` with weight 1.
    -   **MST:** `{0, 1}`. Cost: 1.
3.  **Neighbors of {0, 1}:** `2(3)` [from 0], `3(4)` [from 0], `2(2)` [from 1].
4.  **Pick Min:** `(1, 2)` with weight 2.
    -   **MST:** `{0, 1, 2}`. Cost: 1+2=3.
5.  **Neighbors of {0, 1, 2}:** `3(4)` [from 0], `3(5)` [from 2]. (Note: `(0,2)` is internal now).
6.  **Pick Min:** `(0, 3)` with weight 4.
    -   **MST:** `{0, 1, 2, 3}`. Cost: 3+4=7.

**Total Weight:** 7.

### Algorithm Steps

1.  **Initialization:**
    -   `visited` array (boolean).
    -   Min-Priority Queue `pq` storing `{weight, node}`.
    -   Start from node 0. Push `{0, 0}` to `pq`.
2.  **Loop:**
    -   While `pq` is not empty:
        -   Pop `{w, u}` with smallest `w`.
        -   If `u` is already visited, continue.
        -   Mark `u` as visited. Add `w` to total MST weight.
        -   For each neighbor `v` of `u` with weight `edgeW`:
            -   If `v` is not visited, push `{edgeW, v}` to `pq`.
3.  **Output:** Total weight.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Connected:** Graph is guaranteed connected.
-   **Weights:** Non-negative.
-   **Start Node:** You can start Prim's from *any* node (usually 0). The MST weight will be the same.

## Naive Approach

### Intuition

Similar to Dijkstra, a naive implementation uses an array to find the minimum weight edge connecting the visited set to the unvisited set.

### Time Complexity

-   **O(N^2)**: Good for dense graphs (M ≈ N^2).

## Optimal Approach (Prim's with Binary Heap)

Using a Min-Heap allows us to efficiently retrieve the minimum weight edge.

### Time Complexity

-   **O(M log N)**: Each edge is pushed to the heap at most once.

### Space Complexity

-   **O(N + M)**: Adjacency list + Heap.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public long mstPrim(int n, List<List<int[]>> adj) {
        long mstWeight = 0;
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        
        // {weight, node}
        pq.offer(new int[]{0, 0});
        
        int nodesCount = 0;
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int w = curr[0];
            int u = curr[1];
            
            if (visited[u]) continue;
            
            visited[u] = true;
            mstWeight += w;
            nodesCount++;
            
            if (nodesCount == n) break; // Optimization
            
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int weight = edge[1];
                if (!visited[v]) {
                    pq.offer(new int[]{weight, v});
                }
            }
        }
        
        return mstWeight;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
            adj.get(v).add(new int[]{u, w});
        }

        Solution solution = new Solution();
        System.out.println(solution.mstPrim(n, adj));
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def mst_prim(n: int, adj: list[list[tuple[int, int]]]) -> int:
    mst_weight = 0
    visited = [False] * n
    pq = [(0, 0)] # (weight, node)
    nodes_count = 0
    
    while pq:
        w, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
            
        visited[u] = True
        mst_weight += w
        nodes_count += 1
        
        if nodes_count == n:
            break
            
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
                
    return mst_weight

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        print(mst_prim(n, adj))
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
    long long mstPrim(int n, const vector<vector<pair<int, int>>>& adj) {
        long long mstWeight = 0;
        vector<bool> visited(n, false);
        
        // Min-heap: {weight, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        
        int nodesCount = 0;
        
        while (!pq.empty()) {
            int w = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            if (visited[u]) continue;
            
            visited[u] = true;
            mstWeight += w;
            nodesCount++;
            
            if (nodesCount == n) break;
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;
                if (!visited[v]) {
                    pq.push({weight, v});
                }
            }
        }
        
        return mstWeight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    Solution solution;
    cout << solution.mstPrim(n, adj) << "\n";
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
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    const element = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (element.w >= parent.w) break;
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
        if (leftChild.w < element.w) swap = leftChildIdx;
      }
      if (rightChildIdx < length) {
        let rightChild = this.heap[rightChildIdx];
        if ((swap === null && rightChild.w < element.w) || (swap !== null && rightChild.w < this.heap[swap].w)) {
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
  mstPrim(n, adj) {
    let mstWeight = 0n;
    const visited = new Int8Array(n).fill(0);
    const pq = new MinPriorityQueue();
    
    pq.push({ w: 0, u: 0 });
    let nodesCount = 0;
    
    while (!pq.isEmpty()) {
      const { w, u } = pq.pop();
      
      if (visited[u]) continue;
      
      visited[u] = 1;
      mstWeight += BigInt(w);
      nodesCount++;
      
      if (nodesCount === n) break;
      
      for (const [v, weight] of adj[u]) {
        if (!visited[v]) {
          pq.push({ w: weight, u: v });
        }
      }
    }
    
    return mstWeight.toString();
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
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const solution = new Solution();
  console.log(solution.mstPrim(n, adj));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1 1
1 2 2
0 2 3
```

**Initialization:**
-   `pq`: `[{0, 0}]`
-   `visited`: `[F, F, F]`

**Step 1:**
-   Pop `{0, 0}`. Mark 0 visited. `mstWeight` = 0.
-   Neighbors of 0: `1(1), 2(3)`. Push `{1, 1}, {3, 2}`.
-   `pq`: `[{1, 1}, {3, 2}]`

**Step 2:**
-   Pop `{1, 1}`. Mark 1 visited. `mstWeight` = 1.
-   Neighbors of 1: `0(1)` [visited], `2(2)`. Push `{2, 2}`.
-   `pq`: `[{2, 2}, {3, 2}]`

**Step 3:**
-   Pop `{2, 2}`. Mark 2 visited. `mstWeight` = 1+2 = 3.
-   Neighbors of 2: `0(3)` [visited], `1(2)` [visited].
-   `pq`: `[{3, 2}]`

**Step 4:**
-   Pop `{3, 2}`. 2 is already visited. Ignore.

**Result:** 3.

## ✅ Proof of Correctness

Prim's algorithm is also based on the **Cut Property**. At each step, the set of visited nodes `S` and unvisited nodes `V-S` form a cut. Prim's greedily picks the minimum weight edge crossing this cut, which is guaranteed to be part of the MST.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Kruskal vs Prim:** Kruskal's is better for sparse graphs (O(M log M)) and easier to implement. Prim's (O(M log N) or O(N^2)) is better for dense graphs.
-   **Prim's Optimization:** You can use an indexed priority queue or a simple `min_dist` array to update keys instead of pushing duplicates to the heap, reducing heap size to `N`.

### Common Mistakes to Avoid

1.  **Directed Graph:** Prim's is for undirected graphs.
2.  **Disconnected Graph:** Standard Prim's only finds the MST of the component containing the start node. To find the Minimum Spanning Forest, run Prim's on every unvisited node.
3.  **Priority Queue:** Don't forget to check `if (visited[u]) continue` when popping from the heap, because the heap might contain multiple entries for the same node with different weights.
