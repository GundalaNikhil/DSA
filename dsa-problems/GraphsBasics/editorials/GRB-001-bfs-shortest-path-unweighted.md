---
problem_id: GRB_BFS_SHORTEST_PATH_UNWEIGHTED__4821
display_id: GRB-001
slug: bfs-shortest-path-unweighted
title: "BFS Shortest Path in Unweighted Graph"
difficulty: Easy
difficulty_score: 25
topics:
  - Graphs
  - BFS
  - Shortest Path
tags:
  - graphs-basics
  - bfs
  - shortest-path
  - easy
premium: true
subscription_tier: basic
---

# GRB-001: BFS Shortest Path in Unweighted Graph

## 📋 Problem Summary

You are given an undirected, unweighted graph with `n` nodes and `m` edges. You need to find the shortest distance from a starting node `s` to all other nodes. If a node is unreachable, its distance is `-1`.

## 🌍 Real-World Scenario

**Scenario Title:** The "Six Degrees of Separation" Game

Imagine a social network where people are nodes and friendships are edges.
-   **You** are the source node `s`.
-   **Your friends** are 1 step away (distance 1).
-   **Friends of your friends** (who aren't already your friends) are 2 steps away (distance 2).
-   And so on.

The goal is to find out how many "handshakes" away everyone else is from you. If someone is completely disconnected from your social circle, they are unreachable (distance -1). BFS is exactly how social networks suggest "People You May Know" (2nd degree connections) or calculate your "Bacon Number".

![Real-World Application](../images/GRB-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    0 -- 1 -- 2
    |
    3
```
**Source:** 0

**BFS Layers:**
-   **Layer 0:** Node 0 (Distance 0)
-   **Layer 1:** Neighbors of 0 -> Nodes 1, 3 (Distance 1)
-   **Layer 2:** Neighbors of 1 -> Node 2 (Distance 2). (3 is already visited).

**Result:**
-   0: 0
-   1: 1
-   2: 2
-   3: 1

### Algorithm Steps

1.  **Adjacency List:** Convert the input edge list into an adjacency list `adj` where `adj[u]` contains all neighbors of `u`.
2.  **Queue & Distance Array:**
    -   Create a `queue` for BFS and add the source `s`.
    -   Create a `dist` array of size `n`, initialized to `-1` (to mark unvisited).
    -   Set `dist[s] = 0`.
3.  **BFS Loop:**
    -   While the queue is not empty:
        -   Dequeue the current node `u`.
        -   For each neighbor `v` of `u`:
            -   If `dist[v] == -1` (unvisited):
                -   Set `dist[v] = dist[u] + 1`.
                -   Enqueue `v`.
4.  **Output:** Return the `dist` array.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Graph Type:** Undirected. If `u-v` is an edge, you can go `u->v` and `v->u`.
-   **Unweighted:** All edges have weight 1.
-   **Disconnected Components:** Nodes not reachable from `s` will remain `-1` in the `dist` array, which matches the required output.
-   **Self-loops/Multi-edges:** Constraints say they don't exist, so no need to handle them specifically.

## Naive Approach

### Intuition

A naive approach might be to use DFS (Depth First Search) to find paths. However, DFS does **not** guarantee the shortest path in an unweighted graph. It might go deep down a long path before finding a shorter one. To make DFS work, you'd have to explore *all* paths and keep the minimum length found, which is exponential in time complexity.

### Time Complexity

-   **Exponential**: O(N!) in the worst case for finding shortest paths via exhaustive DFS.

## Optimal Approach (BFS)

Breadth-First Search (BFS) explores the graph layer by layer. It visits all nodes at distance 1, then all at distance 2, etc. The first time BFS reaches a node, it is guaranteed to be via the shortest path.

### Algorithm

1.  Initialize `dist` array with `-1`.
2.  `dist[s] = 0`, `queue.push(s)`.
3.  While `queue` not empty:
    -   `u = queue.pop()`.
    -   For `v` in `adj[u]`:
        -   If `dist[v] == -1`:
            -   `dist[v] = dist[u] + 1`
            -   `queue.push(v)`

### Time Complexity

-   **O(N + M)**: We visit every node once and process every edge once (twice in undirected graph).

### Space Complexity

-   **O(N + M)**: To store the adjacency list and the distance array/queue.

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int[] shortestPath(int n, int[][] edges, int s) {
        // 1. Build Adjacency List
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        // 2. Initialize Distance Array
        int[] dist = new int[n];
        Arrays.fill(dist, -1);

        // 3. BFS
        Queue<Integer> q = new LinkedList<>();
        q.offer(s);
        dist[s] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.offer(v);
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

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] result = solution.shortestPath(n, edges, s);

        for (int i = 0; i < n; i++) {
            System.out.print(result[i]);
            if (i < n - 1) System.out.print(" ");
        }
        System.out.println();
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

def shortest_path(n: int, edges: list, s: int) -> list:
    # 1. Build Adjacency List
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # 2. Initialize Distance Array
    dist = [-1] * n
    
    # 3. BFS
    queue = deque([s])
    dist[s] = 0
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                
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
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])
            
        result = shortest_path(n, edges, s)
        print(' '.join(map(str, result)))
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

class Solution {
public:
    vector<int> shortestPath(int n, vector<vector<int>>& edges, int s) {
        // 1. Build Adjacency List
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        // 2. Initialize Distance Array
        vector<int> dist(n, -1);

        // 3. BFS
        queue<int> q;
        q.push(s);
        dist[s] = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
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

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution solution;
    vector<int> result = solution.shortestPath(n, edges, s);

    for (int i = 0; i < n; i++) {
        cout << result[i];
        if (i < n - 1) cout << " ";
    }
    cout << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestPath(n, edges, s) {
    // 1. Build Adjacency List
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    // 2. Initialize Distance Array
    const dist = new Array(n).fill(-1);

    // 3. BFS
    const queue = [s];
    dist[s] = 0;
    let head = 0; // Use pointer for O(1) dequeue

    while (head < queue.length) {
      const u = queue[head++];
      for (const v of adj[u]) {
        if (dist[v] === -1) {
          dist[v] = dist[u] + 1;
          queue.push(v);
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
  
  // Flatten data array to handle multiple numbers on one line
  const tokens = data.join(" ").trim().split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);
  const s = Number(tokens[ptr++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.shortestPath(n, edges, s);
  console.log(result.join(" "));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 3 0
0 1
1 2
0 3
```

**Initialization:**
-   `n=4`, `s=0`
-   `adj`: `0:[1,3], 1:[0,2], 2:[1], 3:[0]`
-   `dist`: `[-1, -1, -1, -1]`
-   `queue`: `[0]`
-   `dist[0] = 0` -> `[0, -1, -1, -1]`

**Iteration 1:**
-   Pop `0`. Neighbors: `1, 3`.
-   Visit `1`: `dist[1] = 0 + 1 = 1`. Queue: `[1]`.
-   Visit `3`: `dist[3] = 0 + 1 = 1`. Queue: `[1, 3]`.
-   `dist`: `[0, 1, -1, 1]`

**Iteration 2:**
-   Pop `1`. Neighbors: `0, 2`.
-   `0` visited.
-   Visit `2`: `dist[2] = 1 + 1 = 2`. Queue: `[3, 2]`.
-   `dist`: `[0, 1, 2, 1]`

**Iteration 3:**
-   Pop `3`. Neighbors: `0`.
-   `0` visited. Queue: `[2]`.

**Iteration 4:**
-   Pop `2`. Neighbors: `1`.
-   `1` visited. Queue: `[]`.

**Result:** `0 1 2 1`

## ✅ Proof of Correctness

BFS guarantees finding the shortest path in unweighted graphs because:
1.  It explores nodes in increasing order of their distance from the source (layer by layer).
2.  The first time a node is visited, it is reached via the minimum number of edges possible.
3.  Since edge weights are uniform (1), minimum edges = minimum distance.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Path Reconstruction:** How would you print the actual path? (Store `parent` pointers).
-   **0-1 BFS:** What if edges have weights 0 or 1? (Use Deque).
-   **Multi-Source BFS:** Find shortest distance from *any* of multiple sources (Initialize queue with all sources).

### C++ommon Mistakes to Avoid

1.  **Not marking visited:** Forgetting to check `if dist[v] == -1` leads to infinite loops in cyclic graphs.
2.  **Using DFS:** DFS does not guarantee shortest paths in unweighted graphs.
3.  **Queue Operations:** In JavaScript/Python, using `shift()` or `pop(0)` is O(N), making BFS O(N^2). Use a pointer or `deque`.
