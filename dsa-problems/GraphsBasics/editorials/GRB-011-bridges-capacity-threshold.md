---
problem_id: GRB_BRIDGES_CAPACITY_THRESHOLD__4509
display_id: GRB-011
slug: bridges-capacity-threshold
title: "Bridges With Capacity Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Graphs
  - Bridges
  - DFS
tags:
  - graphs-basics
  - bridges
  - dfs
  - medium
premium: true
subscription_tier: basic
---

# GRB-011: Bridges With Capacity Threshold

## 📋 Problem Summary

You are given an undirected graph where each edge has a **capacity**. You need to find all edges that are **critical**. An edge is critical if:
1.  It is a **Bridge** (removing it disconnects the graph).
2.  Its capacity is strictly less than a threshold `T`.

Return these edges in the order they appear in the input.

## 🌍 Real-World Scenario

**Scenario Title:** Supply Chain Bottlenecks

Imagine a logistics network where trucks deliver goods between warehouses.
-   **Nodes** are warehouses.
-   **Edges** are roads.
-   **Capacity** is the max weight a road can handle.
-   **Bridge:** A road is a "bridge" if it's the *only* way to get from one group of warehouses to another. If this road collapses, the network is split.
-   **Threshold:** You have a heavy shipment of weight `T`.
-   **Critical Edge:** A road that is both vital (a bridge) AND too weak to support your shipment (capacity < T). These are the bottlenecks you must upgrade immediately.

![Real-World Application](../images/GRB-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
      (5)
  0 ------- 1
  | \       |
  |  \ (2)  | (5)
  |   \     |
 (5)   \    |
  |     \   |
  3 ------- 2
      (1)
```
**Threshold T = 3**

**Bridges:**
-   Edges in cycle `0-1-2-0` are NOT bridges.
-   Edge `(2,3)` connects the cycle to node 3. It IS a bridge.

**Capacities:**
-   Edges `(0,1), (0,2), (1,2), (0,3)` have capacities >= 3. Not critical.
-   Edge `(2,3)` has capacity 1. `1 < 3`.

**Result:** Edge `(2,3)` is critical.

### Algorithm Steps

1.  **Identify Bridges:** Use Tarjan's Bridge-Finding Algorithm (DFS with `discovery_time` and `low_link`).
    -   `disc[u]`: Time when `u` was first visited.
    -   `low[u]`: Lowest `disc` value reachable from `u` (including back-edges).
    -   Edge `(u, v)` is a bridge if `low[v] > disc[u]`.
2.  **Filter by Capacity:**
    -   While running the algorithm, if we identify `(u, v)` as a bridge, check if `capacity < T`.
    -   If yes, mark it as critical.
3.  **Maintain Order:**
    -   The problem requires output in input order.
    -   Store the original index of each edge.
    -   Collect indices of critical edges, sort them, and then output the corresponding `u v`.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Input Order:** Output must preserve the relative order of edges from the input.
-   **Multiple Edges:** The problem implies a simple graph or standard multigraph handling. Tarjan's handles multigraphs if implemented carefully (don't go back to parent via the *same* edge index).
-   **Disconnected Graph:** Handle all components.

## Naive Approach

### Intuition

For every edge:
1.  Temporarily remove it.
2.  Run BFS/DFS to check connectivity.
3.  If disconnected AND capacity < T, add to result.

### Time Complexity

-   **O(M * (N + M))**: Too slow for M=200,000.

## Optimal Approach (Tarjan's Bridge Algorithm)

We find all bridges in a single DFS pass.

### Algorithm Details

1.  `timer = 0`, `disc` array, `low` array.
2.  DFS from each unvisited node.
3.  For edge `u -> v`:
    -   If `v` is parent of `u`, skip.
    -   If `v` is visited: `low[u] = min(low[u], disc[v])`.
    -   If `v` is unvisited:
        -   `dfs(v, u)`
        -   `low[u] = min(low[u], low[v])`
        -   If `low[v] > disc[u]`: **Bridge Found!**
            -   Check capacity. If `< T`, add edge index to a list.

### Handling Parallel Edges
If there are multiple edges between `u` and `v`, only one can be the "parent" edge. The others are back-edges. To handle this robustly, pass the `edgeIndex` of the parent edge to the DFS, not just the `parent` node.

### Time Complexity

-   **O(N + M)**: Single DFS.

### Space Complexity

-   **O(N + M)**: Recursion stack and arrays.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4 3
0 1 1
1 2 5
2 0 1
1 3 2
```
**Edges:**
0. `(0, 1, 1)`
1. `(1, 2, 5)`
2. `(2, 0, 1)`
3. `(1, 3, 2)`

**DFS(0):**
-   `disc[0]=1, low[0]=1`.
-   **Neighbor 1 (Edge 0):**
    -   `dfs(1, 0)`. `disc[1]=2, low[1]=2`.
    -   **Neighbor 2 (Edge 1):**
        -   `dfs(2, 1)`. `disc[2]=3, low[2]=3`.
        -   **Neighbor 0 (Edge 2):**
            -   Visited. `low[2] = min(3, disc[0]=1) = 1`.
        -   Back to 1. `low[1] = min(2, low[2]=1) = 1`.
    -   **Neighbor 3 (Edge 3):**
        -   `dfs(3, 3)`. `disc[3]=4, low[3]=4`.
        -   No neighbors.
        -   Back to 1. `low[1] = min(1, low[3]=4) = 1`.
        -   Check Bridge: `low[3] (4) > disc[1] (2)`. **Bridge!**
        -   Check Cap: `cap=2 < T=3`. **Critical!** Add index 3.
    -   Back to 0. `low[0] = min(1, low[1]=1) = 1`.

**Result:** Index 3 -> Edge `(1, 3)`.

## ✅ Proof of Correctness

1.  **Bridge Property:** `low[v] > disc[u]` implies there is no back-edge from `v` or its descendants to `u` or its ancestors. Thus, `(u, v)` is the only path.
2.  **Capacity Check:** We strictly follow the problem statement: if it's a bridge AND capacity < T.
3.  **Ordering:** We store indices and sort them at the end, ensuring input order is preserved.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Dynamic Bridges:** How to maintain bridges if edges are added/removed? (Link-Cut Trees or dynamic graph algorithms).
-   **2-Edge-Connected Components:** Condense the graph by shrinking all cycles. The remaining edges are bridges.

### Common Mistakes to Avoid

1.  **Parent Node vs Parent Edge:** In multigraphs (parallel edges), checking `v != parent` is insufficient. You must check `edgeIndex != parentEdgeIndex`.
2.  **Sorting Output:** The problem asks for edges in input order. Don't just print them as you find them (DFS order != Input order).
3.  **Capacity Threshold:** Ensure strict inequality `< T` vs `<= T` based on problem statement.
