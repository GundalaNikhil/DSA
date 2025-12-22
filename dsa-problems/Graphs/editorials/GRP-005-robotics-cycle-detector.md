---
problem_id: GRP_ROBOTICS_CYCLE_DETECTOR__8341
display_id: GRP-005
slug: robotics-cycle-detector
title: "Robotics Cycle Detector"
difficulty: Medium
difficulty_score: 45
topics:
  - Graph Traversal
  - Cycle Detection
  - DFS
tags:
  - graph
  - cycle-detection
  - dfs
  - undirected-graph
  - medium
premium: true
subscription_tier: basic
---

# GRP-005: Robotics Cycle Detector

## 📋 Problem Summary

Detect if an undirected graph contains a cycle using DFS with parent tracking. A cycle exists when we can start from a vertex and return to it through at least three edges without repeating any edge.

## 🌍 Real-World Scenario

**Scenario Title:** Robotics Path Validation System

Imagine designing a warehouse robotics system where robots follow predefined paths between stations. The paths form a network (graph) where stations are nodes and bidirectional paths are edges. Before deploying the system, you need to detect if there are any circular routes.

Cycles in the path network can be both beneficial and problematic. Beneficial: robots can continuously loop for repetitive tasks. Problematic: in systems where robots must visit each station exactly once, cycles create ambiguity in route planning and can lead to deadlocks or inefficient routing.

For safety and efficiency validation, detecting cycles is crucial. If a cycle exists, the system needs special handling - either breaking the cycle by making certain paths one-way, or implementing cycle-aware routing algorithms. DFS with parent tracking efficiently identifies these cycles during the network design phase.

**Why This Problem Matters:**

- **Deadlock Detection:** Finding circular dependencies in resource allocation
- **Network Topology:** Identifying redundant paths in communication networks  
- **Dependency Resolution:** Detecting circular dependencies in build systems
- **Route Planning:** Validating path networks for autonomous systems

![Real-World Application](../images/GRP-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Cycle Detection

```
Graph with cycle:

    0 --- 1
    |     |
    2 ----+

Edges: (0,1), (1,2), (2,0)

DFS from node 0:
Visit 0 (parent: -1)
  → Visit 1 (parent: 0)
    → Visit 2 (parent: 1)
      → Try to visit 0 (parent: 2)
        0 is visited AND 0 ≠ parent(2)
        → CYCLE DETECTED!

Legend:
--- = edge
→ = DFS traversal direction
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Cycle definition:** Path of ≥3 edges returning to starting vertex
- **Parent tracking:** Essential to avoid false positives from bidirectional edges
- **Back edge:** Edge to a visited node (not parent) indicates a cycle
- **Disconnected components:** Check all components by starting DFS from unvisited nodes

Common interpretation mistake:

- ❌ **Wrong:** Detecting edge (u,v) and (v,u) as a cycle
- ✅ **Correct:** Using parent tracking to ignore the immediate back-edge in undirected graphs

### Core Concept

In DFS, if we encounter a visited node that is NOT the parent of the current node, we've found a back edge, which indicates a cycle.

## Optimal Approach

### Algorithm

```
has_cycle(n, adj):
    visited = [false] * n
    
    for i in 0 to n-1:
        if not visited[i]:
            if dfs(i, -1, adj, visited):
                return true
    
    return false

dfs(node, parent, adj, visited):
    visited[node] = true
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node, adj, visited):
                return true
        elif neighbor != parent:
            return true  // Back edge found - cycle detected
    
    return false
```

### Time Complexity

- **O(V + E)** - Visit each vertex once, examine each edge once

### Space Complexity

- **O(V)** - Recursion stack and visited array

![Algorithm Visualization](../images/GRP-005/algorithm-visualization.png)

## Implementations

### Java

```java
import java.util.*;

class Solution {
    public boolean hasCycle(int n, List<List<Integer>> adj) {
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, -1, adj, visited)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    private boolean dfs(int node, int parent, List<List<Integer>> adj, boolean[] visited) {
        visited[node] = true;
        
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, adj, visited)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true; // Cycle detected
            }
        }
        
        return false;
    }
}
```

### Python

```python
from typing import List

def has_cycle(n: int, adj: List[List[int]]) -> bool:
    visited = [False] * n
    
    def dfs(node, parent):
        visited[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Cycle detected
        
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
        visited[node] = true;
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, adj, visited)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true; // Cycle detected
            }
        }
        
        return false;
    }
    
public:
    bool hasCycle(int n, vector<vector<int>>& adj) {
        vector<bool> visited(n, false);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, -1, adj, visited)) {
                    return true;
                }
            }
        }
        
        return false;
    }
};
```

### JavaScript

```javascript
class Solution {
  hasCycle(n, adj) {
    const visited = new Array(n).fill(false);
    
    const dfs = (node, parent) => {
      visited[node] = true;
      
      for (const neighbor of adj[node]) {
        if (!visited[neighbor]) {
          if (dfs(neighbor, node)) {
            return true;
          }
        } else if (neighbor !== parent) {
          return true; // Cycle detected
        }
      }
      
      return false;
    };
    
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        if (dfs(i, -1)) {
          return true;
        }
      }
    }
    
    return false;
  }
}
```

## 🧪 Test Case Walkthrough (Dry Run)

Graph: nodes {0,1,2}, edges (0,1), (1,2), (2,0)

| Step | Node | Parent | Neighbor | Visited[Neighbor] | Neighbor==Parent? | Result |
|-----:|:----:|:------:|:--------:|:-----------------:|:-----------------:|:-------|
| 1 | 0 | -1 | 1 | false | - | Call dfs(1,0) |
| 2 | 1 | 0 | 0 | true | Yes | Skip (parent) |
| 3 | 1 | 0 | 2 | false | - | Call dfs(2,1) |
| 4 | 2 | 1 | 1 | true | Yes | Skip (parent) |
| 5 | 2 | 1 | 0 | true | No | **CYCLE!** |

Answer: `true`

![Example Visualization](../images/GRP-005/example-1.png)

## ✅ Proof of Correctness

**Theorem:** In an undirected graph, a back edge (edge to a visited non-parent node) exists if and only if a cycle exists.

**Proof:** 
- If cycle exists → there's a path from u back to u → DFS will find a back edge
- If back edge exists → edge connects to ancestor in DFS tree → forms cycle

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Return the actual cycle path, not just true/false
- **Extension 2:** Count the total number of cycles
- **Extension 3:** Find the shortest cycle in the graph
- **Extension 4:** Detect cycles in directed graphs (requires different approach)

## Common Mistakes to Avoid

1. **Forgetting Parent Check**
   - ❌ Wrong: `if visited[neighbor]: return true`
   - ✅ Correct: `if visited[neighbor] and neighbor != parent: return true`
   - **Impact:** False positive from bidirectional edge

2. **Not Checking All Components**
   - ❌ Wrong: Only running DFS from node 0
   - ✅ Correct: Check all unvisited nodes
   - **Description:** Misses cycles in disconnected components

3. **Using BFS Instead of DFS**
   - ❌ Wrong: BFS with parent tracking is more complex
   - ✅ Correct: DFS naturally handles parent tracking via recursion
   - **Description:** BFS requires additional state management

4. **Incorrect Parent Initialization**
   - ❌ Wrong: Starting with parent = 0
   - ✅ Correct: Starting with parent = -1 (or any invalid node)
   - **Prevention:** Ensures first node doesn't skip its own edges

5. **Confusing with Directed Graph Cycle Detection**
   - ❌ Wrong: Using recursion stack approach (for directed graphs)
   - ✅ Correct: Using parent tracking (for undirected graphs)
   - **Description:** Different algorithms for directed vs undirected

## Related Concepts

- **Directed Graph Cycle Detection:** Uses recursion stack instead of parent tracking
- **Union-Find:** Alternative approach for cycle detection
- **Topological Sort:** Related to DAG (Directed Acyclic Graph) verification
- **Bridges and Articulation Points:** Advanced graph structure analysis
- **Minimum Spanning Tree:** Kruskal's algorithm uses cycle detection
