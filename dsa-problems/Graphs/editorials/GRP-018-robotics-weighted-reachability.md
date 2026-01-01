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


### Python


### C++


### JavaScript


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
