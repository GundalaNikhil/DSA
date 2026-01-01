---
problem_id: AGR_BRIDGES_AND_2ECC__3471
display_id: AGR-005
slug: bridges-and-2ecc
title: "Bridges and 2-Edge-Connected Components"
difficulty: Medium
difficulty_score: 54
topics:
  - Graphs
  - Bridges
  - Components
tags:
  - advanced-graphs
  - bridges
  - components
  - medium
premium: true
subscription_tier: basic
---

# AGR-005: Bridges and 2-Edge-Connected Components

## 📋 Problem Summary

Identify all **bridges** in a graph and partition the vertices into **2-Edge-Connected Components (2ECCs)**. A 2ECC is a subgraph where removing any single edge does not disconnect the subgraph.

## 🌍 Real-World Scenario

**Scenario Title:** Critical Infrastructure Links

Imagine a network of islands connected by bridges.
-   **Bridge (Graph Term):** A literal bridge that, if destroyed, makes it impossible to travel between two parts of the map.
-   **2ECC:** A group of islands that are "robustly" connected. Even if one bridge within the group fails, there's always an alternative route (a cycle) to keep them connected.
-   **Goal:** Identify the critical vulnerabilities (bridges) and the safe zones (2ECCs).

![Real-World Application](../images/AGR-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

**Graph:**
```
    (0) --- (1)
     |       |
     \       /
      \     /
        (2)
         |
         |  <-- Bridge
         |
        (3) --- (4)
```
-   **Cycle:** 0-1-2-0. No single edge removal disconnects {0, 1, 2}.
-   **Bridge:** Edge (2, 3). Removing it separates {0, 1, 2} from {3, 4}.
-   **Edge (3, 4):** Is it a bridge? Yes, removing it isolates 4.
-   **2ECCs:**
    1.  `{0, 1, 2}` (Robust)
    2.  `{3}` (Single node)
    3.  `{4}` (Single node)

### Algorithm: Tarjan's Bridge-Finding + Component Labeling

1.  **Find Bridges:**
    -   Use **DFS** with `tin` (time of insertion) and `low` (lowest `tin` reachable via back-edge).
    -   For edge `u -> v`:
        -   If `v` is parent, ignore.
        -   If `v` visited, `low[u] = min(low[u], tin[v])`.
        -   If `v` unvisited:
            -   DFS(v).
            -   `low[u] = min(low[u], low[v])`.
            -   If `low[v] > tin[u]`, then `(u, v)` is a **bridge**.
2.  **Find 2ECCs:**
    -   Remove all bridges from the graph.
    -   Run a traversal (DFS/BFS) or use DSU on the remaining edges.
    -   All nodes in a connected component form a 2ECC.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Parallel Edges:** The problem doesn't explicitly forbid them. If parallel edges exist between `u` and `v`, `(u, v)` is NOT a bridge (unless all but one are removed, but here we consider the static graph). Standard logic: pass edge index to DFS to distinguish parallel edges.
-   **Output Order:** Bridges must be printed in the order they appear in the input. Store `is_bridge[edge_index]`.
-   **Component IDs:** 1-based.

## Naive Approach

### Intuition

For every edge, remove it, run BFS to check connectivity. If disconnected, it's a bridge.

### Time Complexity

-   **O(M * (N + M))**: Too slow for M=200,000.

## Optimal Approach (DFS Low-Link)

### Time Complexity

-   **O(N + M)**: One DFS pass for bridges, one pass for components.

### Space Complexity

-   **O(N + M)**: Recursion stack and adjacency list.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 4
0 1
1 2
2 0
2 3
```
**DFS Trace:**
1.  Start at 0. `tin[0]=0`.
2.  Go to 1. `tin[1]=1`.
3.  Go to 2. `tin[2]=2`.
4.  From 2, see 0 (visited). `low[2] = min(2, tin[0]=0) = 0`.
5.  From 2, see 3. `tin[3]=3`.
6.  From 3, no neighbors. Return. `low[3]=3`.
7.  Back at 2. `low[2] = min(0, 3) = 0`. Check bridge: `low[3] (3) > tin[2] (2)`? Yes. **(2,3) is Bridge**.
8.  Back at 1. `low[1] = min(1, low[2]=0) = 0`. Check bridge: `low[2] (0) > tin[1] (1)`? No.
9.  Back at 0. `low[0] = min(0, low[1]=0) = 0`. Check bridge: `low[1] (0) > tin[0] (0)`? No.

**Components:**
-   Remove (2,3).
-   Start BFS at 0 -> 1 -> 2. Comp 1.
-   Start BFS at 3. Comp 2.
-   Result: `1 1 1 2`.

## ✅ Proof of Correctness

-   **Bridges:** An edge `(u, v)` is a bridge iff there is no back-edge from the subtree of `v` to `u` or an ancestor of `u`. This is captured by `low[v] > tin[u]`.
-   **2ECC:** By definition, 2ECCs are components formed by removing all bridges. Our algorithm does exactly this.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Bridge Tree:** If we contract each 2ECC into a single node, the resulting structure is a tree (the Bridge Tree). This is useful for path queries.
-   **Articulation Points:** Similar logic (`low[v] >= tin[u]`), but for vertices.
-   **Dynamic Bridges:** Maintaining bridges under edge insertions/deletions (fully dynamic graph algorithms).

### Common Mistakes to Avoid

1.  **Parent Edge:** In undirected graphs, do not go back to the parent immediately. Pass `parentEdgeIndex` to distinguish parallel edges.
2.  **Disconnected Graph:** The graph can be disconnected. Run DFS on all unvisited nodes.
3.  **Output Order:** Bridges must be printed in input order. Don't just print `u v` as you find them; store flags.
