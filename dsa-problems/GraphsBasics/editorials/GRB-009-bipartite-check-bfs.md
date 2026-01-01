---
problem_id: GRB_BIPARTITE_CHECK_BFS__5073
display_id: GRB-009
slug: bipartite-check-bfs
title: "Bipartite Check BFS"
difficulty: Easy
difficulty_score: 36
topics:
  - Graphs
  - BFS
  - Bipartite
tags:
  - graphs-basics
  - bipartite
  - bfs
  - easy
premium: true
subscription_tier: basic
---

# GRB-009: Bipartite Check BFS

## 📋 Problem Summary

Given an undirected graph, determine if it is **Bipartite**.
-   A graph is bipartite if its nodes can be divided into two disjoint sets (colors) such that every edge connects a node in one set to a node in the other set.
-   If it is bipartite, output `true` and the color of each node (0 or 1).
-   If not, output `false`.

## 🌍 Real-World Scenario

**Scenario Title:** Wedding Seating Plan

Imagine you are planning a wedding reception.
-   **Nodes** are guests.
-   **Edges** represent "rivalries" (people who hate each other).
-   **Goal:** You have two tables (Table 0 and Table 1). You must seat every guest at one of the two tables such that no two rivals sit at the same table.
-   If you can do this, the graph of rivalries is **Bipartite**. If you have a triangle of mutual enemies (A hates B, B hates C, C hates A), it's impossible (not bipartite).

![Real-World Application](../images/GRB-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Bipartite Graph:**
```
  (Set 0)    (Set 1)
    0 --------- 1
    |           |
    3 --------- 2
```
-   Color 0: {0, 2}
-   Color 1: {1, 3}
-   Edges: (0,1), (1,2), (2,3), (3,0). All edges go between Set 0 and Set 1.

**Non-Bipartite Graph (Odd Cycle):**
```
      0
     / \
    1---2
```
-   Color 0: {0}
-   Color 1: {1, 2} (Must be different from 0)
-   Edge (1, 2): Connects two nodes of Color 1. **Conflict!**

### Algorithm Steps (BFS Coloring)

1.  **Initialization:**
    -   `colors` array initialized to `-1` (uncolored).
2.  **Iterate Nodes:**
    -   Loop `i` from `0` to `n-1`. If `colors[i]` is `-1`, start BFS from `i`.
3.  **BFS(start):**
    -   `colors[start] = 0`. Push `start` to queue.
    -   While queue not empty:
        -   Pop `u`.
        -   For each neighbor `v`:
            -   If `colors[v] == -1`:
                -   `colors[v] = 1 - colors[u]` (Flip color).
                -   Push `v`.
            -   Else if `colors[v] == colors[u]`:
                -   **Conflict!** Return `false`.
4.  **Output:** If BFS finishes without conflict, return `true` and the `colors` array.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Disconnected Graph:** You must handle all components.
-   **Output Format:** If false, just print `false`. If true, print `true` then the colors.
-   **Valid Colors:** 0 and 1.

## Naive Approach

### Intuition

Try all possible colorings (2^N).

### Time Complexity

-   **Exponential**: O(2^N).

## Optimal Approach (BFS Coloring)

We greedily assign colors. Once the first node of a component is colored, all other nodes' colors are forced by the edges. If we encounter a contradiction, it's impossible.

### Time Complexity

-   **O(N + M)**: Standard BFS traversal.

### Space Complexity

-   **O(N + M)**: Adjacency list + Queue + Colors array.

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int[] bipartiteColors(int n, List<List<Integer>> adj) {
        int[] colors = new int[n];
        Arrays.fill(colors, -1);

        for (int i = 0; i < n; i++) {
            if (colors[i] == -1) {
                if (!bfs(i, adj, colors)) return null;
            }
        }
        return colors;
    }

    private boolean bfs(int start, List<List<Integer>> adj, int[] colors) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        colors[start] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj.get(u)) {
                if (colors[v] == -1) {
                    colors[v] = 1 - colors[u];
                    q.offer(v);
                } else if (colors[v] == colors[u]) {
                    return false;
                }
            }
        }
        return true;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Solution solution = new Solution();
        int[] colors = solution.bipartiteColors(n, adj);
        System.out.println(colors == null ? "0" : "1");
        sc.close();
    }
}
```

### Python
```python
import sys
from collections import deque

def bipartite_colors(n: int, adj: list[list[int]]):
    colors = [-1] * n
    
    for i in range(n):
        if colors[i] == -1:
            queue = deque([i])
            colors[i] = 0
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return None
                        
    return colors

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
            adj[u].append(v)
            adj[v].append(u)
            
        colors = bipartite_colors(n, adj)
        if colors is None:
            print("0")
        else:
            print("1")
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

using namespace std;

class Solution {
public:
    vector<int> bipartiteColors(int n, const vector<vector<int>>& adj) {
        vector<int> colors(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (colors[i] == -1) {
                queue<int> q;
                q.push(i);
                colors[i] = 0;
                
                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    
                    for (int v : adj[u]) {
                        if (colors[v] == -1) {
                            colors[v] = 1 - colors[u];
                            q.push(v);
                        } else if (colors[v] == colors[u]) {
                            return {}; // Empty vector signals false
                        }
                    }
                }
            }
        }
        return colors;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    Solution solution;
    vector<int> colors = solution.bipartiteColors(n, adj);
    
    cout << (colors.empty() ? "0" : "1");
    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  bipartiteColors(n, adj) {
    const colors = new Int32Array(n).fill(-1);

    for (let i = 0; i < n; i++) {
      if (colors[i] === -1) {
        const queue = [i];
        colors[i] = 0;
        let head = 0;
        
        while (head < queue.length) {
          const u = queue[head++];
          
          for (const v of adj[u]) {
            if (colors[v] === -1) {
              colors[v] = 1 - colors[u];
              queue.push(v);
            } else if (colors[v] === colors[u]) {
              return null;
            }
          }
        }
      }
    }
    return colors;
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
    adj[u].push(v);
    adj[v].push(u);
  }

  const solution = new Solution();
  const colors = solution.bipartiteColors(n, adj);
  
  console.log(colors === null ? "0" : "1");
});
```

## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1
1 2
2 0
```

**Initialization:**
-   `colors`: `[-1, -1, -1]`

**BFS(0):**
-   `colors[0] = 0`. Queue: `[0]`.
-   Pop `0`. Neighbors `1, 2`.
    -   `colors[1] = 1`. Queue: `[1]`.
    -   `colors[2] = 1`. Queue: `[1, 2]`.
-   Pop `1`. Neighbors `0, 2`.
    -   `0` is colored 0 (OK).
    -   `2` is colored 1. `colors[1] == colors[2]`. **Conflict!**
-   Return `false`.

## ✅ Proof of Correctness

A graph is bipartite if and only if it contains no odd cycles. BFS naturally finds the shortest path in unweighted graphs. If there is an edge between two nodes at the same BFS level (or levels with same parity), it implies an odd cycle exists. Our coloring logic `color[v] = 1 - color[u]` enforces that neighbors must have different parities. A conflict means an odd cycle was found.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Maximum Bipartite Matching:** If a graph is bipartite, finding the maximum matching is a classic problem (solved via Max Flow).
-   **DFS vs BFS:** DFS can also check bipartiteness. BFS is often preferred for finding the *shortest* odd cycle if one exists.

### Common Mistakes to Avoid

1.  **Disconnected Components:** Forgetting to loop `0..n-1` and only running BFS from node 0.
2.  **Assuming Tree:** Trees are always bipartite. Don't overcomplicate if the input is guaranteed to be a tree.
3.  **Coloring Logic:** Ensure you check `colors[v] == colors[u]` specifically.
