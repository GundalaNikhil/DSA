---
problem_id: GRP_ROBOTICS_WEIGHTED_REACH__9571
display_id: GRP-018
slug: robotics-weighted-reachability
title: Robotics Weighted Reachability
difficulty: Medium
difficulty_score: 50
topics:
- Graph Traversal
- BFS
- Edge Filtering
tags:
- graph
- bfs
- reachability
- weighted-graph
- medium
premium: true
subscription_tier: basic
---
# GRP-018: Robotics Weighted Reachability

## 📋 Problem Summary

Find all nodes reachable from a source using only edges with weight ≤ threshold. Use BFS/DFS with edge filtering to traverse only valid edges. Return list of reachable nodes.

## 🌍 Real-World Scenario

**Scenario Title:** Network Accessibility with Bandwidth Constraints

Imagine analyzing a computer network where you can only use connections with sufficient bandwidth (weight ≤ threshold). You need to find all servers reachable from a source server using only high-bandwidth connections.

This models real scenarios like finding accessible nodes in networks with quality constraints, routing with latency limits, or transportation with vehicle capacity restrictions. The key insight is filtering edges during traversal rather than modifying the graph.

**Why This Problem Matters:**

- **Network Analysis:** Reachability with quality constraints
- **Transportation:** Routes within capacity limits
- **Social Networks:** Connections above relationship strength threshold
- **Resource Planning:** Accessible locations with budget constraints

![Real-World Application](../images/GRP-018/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Reachability with Edge Filtering

```
Weighted graph:
    0 --3--> 1 --2--> 2
    |        |
    5        1
    |        |
    v        v
    3 --4--> 4

Source: 0, Threshold: 3

Valid edges (weight ≤ 3):
    0 --3--> 1 --2--> 2
             |
             1
             |
             v
             4

Reachable: {0, 1, 2, 4}
Unreachable: {3} (edge 0→3 has weight 5 > 3)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Edge filtering:** Only traverse edges with weight ≤ threshold
- **Directed edges:** Respect edge direction
- **Source included:** Source is always reachable
- **Return:** List/set of all reachable node IDs

## Optimal Approach

### Algorithm

```
reachable_nodes(n, adj, source, threshold):
    visited = set()
    queue = [source]
    visited.add(source)
    
    while queue not empty:
        node = queue.dequeue()
        
        for (neighbor, weight) in adj[node]:
            if weight <= threshold and neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    
    return list(visited)
```

### Time Complexity: **O(V + E)**
### Space Complexity: **O(V)**

![Algorithm Visualization](../images/GRP-018/algorithm-visualization.png)

## Implementations

### Java
```java
import java.util.*;

class Solution {
    public int countReachable(int n, List<List<int[]>> adj, int threshold) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(0);
        visited.add(0);

        while (!queue.isEmpty()) {
            int node = queue.poll();

            // Sort neighbors for deterministic behavior
            List<int[]> neighbors = new ArrayList<>(adj.get(node));
            neighbors.sort((a, b) -> Integer.compare(a[0], b[0]));

            for (int[] edge : neighbors) {
                int neighbor = edge[0];
                int weight = edge[1];

                if (weight <= threshold && !visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }

        return visited.size();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int threshold = sc.nextInt();
        int m = sc.nextInt();

        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();

            if (w <= threshold) {
                adj.get(u).add(new int[]{v, w});
                adj.get(v).add(new int[]{u, w});
            }
        }

        Solution solution = new Solution();
        int result = solution.countReachable(n, adj, threshold);
        System.out.println(result);
        sc.close();
    }
}
```

### Python
```python
import sys
sys.setrecursionlimit(200000)
from collections import deque
from typing import List

def count_reachable(n: int, edges: List[tuple], threshold: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        if w <= threshold:
            adj[u].append(v)
            adj[v].append(u)
            
    visited = set()
    queue = deque([0])
    visited.add(0)
    
    while queue:
        node = queue.popleft()
        # Sort for deterministic
        adj[node].sort() 
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited)

def main():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return
        
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        threshold = int(next(iterator))
        m = int(next(iterator))
        
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        result = count_reachable(n, edges, threshold)
        print(result)
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
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int countReachable(int n, vector<tuple<int,int,int>>& edges, int threshold) {
        vector<vector<pair<int,int>>> adj(n);

        // Build adjacency list only with edges within threshold
        for (auto& [u, v, w] : edges) {
            if (w <= threshold) {
                adj[u].push_back({v, w});
                adj[v].push_back({u, w});
            }
        }

        // BFS from node 0
        unordered_set<int> visited;
        queue<int> q;

        q.push(0);
        visited.insert(0);

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            // Sort neighbors for deterministic traversal
            sort(adj[node].begin(), adj[node].end());

            for (auto& [neighbor, weight] : adj[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }

        return visited.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, threshold, m;
    cin >> n >> threshold >> m;

    vector<tuple<int,int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }

    Solution solution;
    cout << solution.countReachable(n, edges, threshold) << endl;

    return 0;
}
```

### JavaScript
```javascript
const readline = require("readline");

class Solution {
  countReachable(n, edges, threshold) {
    const adj = Array.from({ length: n }, () => []);

    // Build adjacency list with weight filter
    for (const [u, v, w] of edges) {
      if (w <= threshold) {
        adj[u].push(v);
        adj[v].push(u);
      }
    }

    const visited = new Set();
    const queue = [0];
    visited.add(0);

    while (queue.length > 0) {
      const node = queue.shift();

      // Sort for deterministic traversal
      adj[node].sort((a, b) => a - b);

      for (const neighbor of adj[node]) {
        if (!visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
        }
      }
    }

    return visited.size;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const threshold = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    const w = Number(tokens[ptr++]);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.countReachable(n, edges, threshold));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

adj: [[(1,3),(3,5)], [(2,2),(4,1)], [], [(4,4)], []]
source: 0, threshold: 3

| Step | Queue | Visited | Action |
|-----:|:------|:--------|:-------|
| 0 | [0] | {0} | Start |
| 1 | [1] | {0,1} | From 0: add 1 (weight 3≤3), skip 3 (weight 5>3) |
| 2 | [2,4] | {0,1,2,4} | From 1: add 2 (weight 2≤3), add 4 (weight 1≤3) |
| 3 | [4] | {0,1,2,4} | From 2: no neighbors |
| 4 | [] | {0,1,2,4} | From 4: no neighbors |

Reachable: [0, 1, 2, 4]

![Example Visualization](../images/GRP-018/example-1.png)

## ✅ Proof of Correctness

**Theorem:** BFS with edge filtering correctly finds all reachable nodes.

**Proof:** BFS explores all nodes reachable via valid edges. The weight check ensures only edges ≤ threshold are traversed. The visited set prevents cycles and duplicate processing.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Find shortest path using only valid edges
- **Extension 2:** Count number of valid paths to each node
- **Extension 3:** Find minimum threshold to reach all nodes
- **Extension 4:** Handle dynamic threshold updates

### Common Mistakes to Avoid

1. **Modifying Graph Instead of Filtering**
   - ❌ Wrong: Removing edges from graph first
   - ✅ Correct: Filter during traversal
   - **Impact:** Inefficient and modifies input

2. **Wrong Weight Comparison**
   - ❌ Wrong: `weight < threshold` (strict inequality)
   - ✅ Correct: `weight <= threshold` (inclusive)
   - **Description:** Off-by-one error

3. **Not Checking Visited**
   - ❌ Wrong: Only checking weight condition
   - ✅ Correct: Check both weight AND visited status
   - **Prevention:** Prevents infinite loops in cycles

4. **Forgetting to Add Source**
   - ❌ Wrong: Starting with empty visited set
   - ✅ Correct: Initialize visited with source
   - **Description:** Source is always reachable

5. **Using DFS Without Visited Check**
   - ❌ Wrong: DFS without marking visited
   - ✅ Correct: Mark visited before recursive calls
   - **Description:** Stack overflow in cycles

## Related Concepts

- **Standard BFS/DFS:** Without edge filtering
- **Dijkstra's Algorithm:** Shortest path with weights
- **Minimum Spanning Tree:** Connecting all nodes with minimum weight
- **Network Flow:** Capacity constraints
- **Graph Connectivity:** Reachability analysis
