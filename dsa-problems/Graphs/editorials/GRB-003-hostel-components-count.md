---
problem_id: GRB_HOSTEL_COMPONENTS_COUNT__3184
display_id: GRB-003
slug: hostel-components-count
title: "Hostel Components Count"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Graph Traversal
  - Connected Components
  - Union-Find
tags:
  - graph
  - connected-components
  - bfs
  - dfs
  - union-find
  - medium
premium: true
subscription_tier: basic
---

# GRB-003: Hostel Components Count

## 📋 Problem Summary

Count the number of connected components in an undirected graph. A connected component is a maximal set of nodes where every pair is connected by a path. This fundamental graph problem tests understanding of graph traversal and connectivity.

## 🌍 Real-World Scenario

**Scenario Title:** University Hostel Friend Groups Analysis

Imagine you're analyzing social connections in a university hostel system. Each student (node) may have friendships (edges) with other students. The hostel administration wants to understand how many distinct friend groups exist to plan social events, allocate common rooms, and identify isolated students who might need additional support.

Connected components naturally represent these friend groups. If student A is friends with B, and B is friends with C, then A, B, and C form one connected component (friend group), even if A and C aren't direct friends. Students with no friendships form singleton components.

This analysis helps in multiple ways: organizing floor-wise events for cohesive groups, identifying students who might benefit from introduction programs, and understanding the social fabric of the hostel. For example, if there are 100 students but only 5 connected components, it indicates strong social cohesion. Conversely, 80 components would suggest many isolated or small groups.

**Why This Problem Matters:**

- **Social Network Analysis:** Understanding community structure in networks
- **Network Reliability:** Identifying isolated subnets in computer networks
- **Image Segmentation:** Finding distinct regions in computer vision
- **Clustering:** Grouping related data points in machine learning

![Real-World Application](../images/GRB-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Connected Components

```
Graph with 5 nodes and 2 edges:

    0 --- 1        2 --- 3        4

Adjacency List:
0: [1]
1: [0]
2: [3]
3: [2]
4: []

Connected Components:
Component 1: {0, 1}
Component 2: {2, 3}
Component 3: {4}

Total: 3 components

Legend:
--- = edge
{ } = nodes in same component
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Component definition:** Maximal set of nodes where any two nodes have a path between them
- **Isolated nodes:** A node with no edges forms its own component of size 1
- **Disconnected graph:** Multiple components exist when graph isn't fully connected
- **Edge representation:** Each edge (u,v) is bidirectional, add to both adj[u] and adj[v]

Common interpretation mistake:

- ❌ **Wrong:** Counting only nodes with edges as components
- ✅ **Correct:** Every node belongs to exactly one component (including isolated nodes)

### Core Concept

A connected component is found by starting from an unvisited node and exploring all reachable nodes using BFS or DFS. Each time we start a new traversal from an unvisited node, we've found a new component.

## Naive Approach

### Intuition

Iterate through all nodes. For each unvisited node, perform BFS/DFS to mark all nodes in its component as visited, and increment the component count.

### Algorithm

1. Initialize visited array of size n (all false)
2. Initialize component count = 0
3. For each node i from 0 to n-1:
   - If not visited[i]:
     - Increment component count
     - Run BFS/DFS from node i to mark all reachable nodes as visited
4. Return component count

### Time Complexity

- **O(V + E)** where V = vertices, E = edges
- Each node visited once, each edge examined once

### Space Complexity

- **O(V)** for visited array and BFS queue/DFS stack

### Why This Works

Each BFS/DFS explores exactly one connected component. By starting from unvisited nodes, we ensure we discover all components without double-counting.

### Decision Tree

```
For each node 0 to n-1:
│
├─ If visited: skip
│
└─ If not visited:
   ├─ Increment component count
   └─ BFS/DFS from this node:
      ├─ Mark current node visited
      ├─ Add to queue/stack
      └─ Process all neighbors:
         └─ Mark reachable nodes visited
```

## Optimal Approach

### Key Insight

The naive approach is already optimal. We can use either BFS, DFS, or Union-Find (DSU). All have O(V + E) complexity, but Union-Find can be useful when edges arrive dynamically.

### Algorithm (BFS Approach)

```
count_components(n, adj):
    visited = [false] * n
    components = 0
    
    for i in 0 to n-1:
        if not visited[i]:
            components++
            bfs(i, adj, visited)
    
    return components

bfs(start, adj, visited):
    queue = [start]
    visited[start] = true
    
    while queue not empty:
        node = queue.dequeue()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = true
                queue.enqueue(neighbor)
```

### Time Complexity

- **O(V + E)** - Optimal for this problem

### Space Complexity

- **O(V)** - For visited array and queue

### Why This Is Optimal

We must examine every node at least once to determine which component it belongs to, making O(V) a lower bound. We must also examine edges to determine connectivity, adding O(E). Therefore O(V + E) is optimal.

![Algorithm Visualization](../images/GRB-003/algorithm-visualization.png)
![Algorithm Steps](../images/GRB-003/algorithm-steps.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public int countComponents(int n, List<List<Integer>> adj) {
        boolean[] visited = new boolean[n];
        int components = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                components++;
                bfs(i, adj, visited);
            }
        }
        
        return components;
    }
    
    private void bfs(int start, List<List<Integer>> adj, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int neighbor : adj.get(node)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        
        Solution solution = new Solution();
        System.out.println(solution.countComponents(n, adj));
        sc.close();
    }
}
```

### Python

```python
from collections import deque
from typing import List

def count_components(n: int, adj: List[List[int]]) -> int:
    """
    Count connected components using BFS.
    
    Args:
        n: Number of nodes
        adj: Adjacency list
    
    Returns:
        Number of connected components
    """
    visited = [False] * n
    components = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    for i in range(n):
        if not visited[i]:
            components += 1
            bfs(i)
    
    return components

def main():
    n = int(input())
    m = int(input())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    result = count_components(n, adj)
    print(result)

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
private:
    void bfs(int start, vector<vector<int>>& adj, vector<bool>& visited) {
        queue<int> q;
        q.push(start);
        visited[start] = true;
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
    }
    
public:
    int countComponents(int n, vector<vector<int>>& adj) {
        vector<bool> visited(n, false);
        int components = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                components++;
                bfs(i, adj, visited);
            }
        }
        
        return components;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> adj(n);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    Solution solution;
    cout << solution.countComponents(n, adj) << "\n";
    
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  countComponents(n, adj) {
    const visited = new Array(n).fill(false);
    let components = 0;
    
    const bfs = (start) => {
      const queue = [start];
      visited[start] = true;
      
      while (queue.length > 0) {
        const node = queue.shift();
        
        for (const neighbor of adj[node]) {
          if (!visited[neighbor]) {
            visited[neighbor] = true;
            queue.push(neighbor);
          }
        }
      }
    };
    
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        components++;
        bfs(i);
      }
    }
    
    return components;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const m = parseInt(data[ptr++]);
  
  const adj = Array.from({ length: n }, () => []);
  
  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }
  
  const solution = new Solution();
  console.log(solution.countComponents(n, adj));
});
```

## 🧪 Test Case Walkthrough (Dry Run)

Use the sample:
- n = 5 nodes
- m = 2 edges
- Edges: (0,1), (2,3)

Adjacency list:
- 0: [1]
- 1: [0]
- 2: [3]
- 3: [2]
- 4: []

Initialize:
- visited = [false, false, false, false, false]
- components = 0

Iteration:

| Node | Visited? | Action | Components | Visited After BFS |
|-----:|:--------:|:-------|:----------:|:------------------|
| 0 | No | Start BFS, mark 0,1 visited | 1 | [T,T,F,F,F] |
| 1 | Yes | Skip | 1 | [T,T,F,F,F] |
| 2 | No | Start BFS, mark 2,3 visited | 2 | [T,T,T,T,F] |
| 3 | Yes | Skip | 2 | [T,T,T,T,F] |
| 4 | No | Start BFS, mark 4 visited | 3 | [T,T,T,T,T] |

**BFS Details:**
- BFS from 0: Visits 0 → 1 (component 1)
- BFS from 2: Visits 2 → 3 (component 2)
- BFS from 4: Visits 4 only (component 3)

Answer is `3`.

![Example Visualization](../images/GRB-003/example-1.png)

## ✅ Proof of Correctness

### Invariant

After processing node i, all nodes in components containing nodes 0 through i have been discovered and counted.

### Why the approach is correct

**Completeness:** We iterate through all nodes, so no component is missed.

**No double-counting:** The visited array ensures each node is processed exactly once. Once a component is discovered via BFS/DFS, all its nodes are marked visited, preventing them from starting new component searches.

**Component integrity:** BFS/DFS from a node discovers exactly all nodes reachable from it, which by definition is one complete connected component.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Return the size of each component, not just the count
- **Extension 2:** Find the largest connected component
- **Extension 3:** Implement using Union-Find (DSU) for dynamic edge additions
- **Extension 4:** Determine if adding a specific edge would merge two components

## Common Mistakes to Avoid

1. **Forgetting Isolated Nodes**

   - ❌ Wrong: Only counting components with edges
   - ✅ Correct: Every node belongs to a component, including isolated nodes
   - **Impact:** Undercounting components

2. **Not Marking Nodes Visited**

   - ❌ Wrong: Running BFS without tracking visited nodes
   - ✅ Correct: Mark nodes as visited to avoid infinite loops and double-counting
   - **Description:** Can cause infinite loops in cyclic graphs

3. **Incorrect Edge Representation**

   - ❌ Wrong: Only adding edge (u,v) to adj[u]
   - ✅ Correct: For undirected graphs, add to both adj[u] and adj[v]
   - **Prevention:** Remember undirected edges go both ways

4. **Starting BFS from Already Visited Nodes**

   - ❌ Wrong: Not checking if node is visited before starting BFS
   - ✅ Correct: Only start BFS from unvisited nodes
   - **Description:** Leads to overcounting components

5. **Confusing Components with Edges**

   - ❌ Wrong: Thinking number of components equals number of edges
   - ✅ Correct: Components are groups of connected nodes; a tree with n nodes has n-1 edges but 1 component
   - **Description:** Fundamental misunderstanding of the concept

## Related Concepts

- **Union-Find (DSU):** Alternative approach for counting components with better performance for dynamic graphs
- **Strongly Connected Components:** Directed graph variant using Kosaraju's or Tarjan's algorithm
- **Minimum Spanning Tree:** Finding a tree that connects all nodes in a weighted graph
- **Graph Coloring:** Related problem of assigning colors to nodes
- **Clustering Algorithms:** Machine learning applications of component detection
