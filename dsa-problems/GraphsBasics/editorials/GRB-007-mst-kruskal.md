---
problem_id: GRB_MST_KRUSKAL__2657
display_id: GRB-007
slug: mst-kruskal
title: "MST Kruskal"
difficulty: Medium
difficulty_score: 42
topics:
  - Graphs
  - MST
  - DSU
tags:
  - graphs-basics
  - mst
  - dsu
  - medium
premium: true
subscription_tier: basic
---

# GRB-007: MST Kruskal

## 📋 Problem Summary

Given a connected, undirected, weighted graph, find the **Minimum Spanning Tree (MST)**. An MST is a subset of edges that connects all vertices together, without any cycles, and with the minimum possible total edge weight. You must use **Kruskal's Algorithm**.

## 🌍 Real-World Scenario

**Scenario Title:** Power Grid Expansion

Imagine you are an electrical engineer tasked with connecting `N` cities to the power grid.
-   **Nodes** are cities.
-   **Edges** are potential power lines.
-   **Weights** are the costs to build those lines (based on distance, terrain, etc.).
-   **Goal:** Connect all cities so that electricity can flow to everyone, but do it as cheaply as possible. You don't need redundant loops (cycles); you just need a single connected network. This is exactly what an MST is.

![Real-World Application](../images/GRB-007/real-world-scenario.png)

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
**Edges:** `(0,1,1), (1,2,2), (0,2,3), (0,3,4), (2,3,5)`

**Kruskal's Steps:**
1.  **Sort Edges:** `(0,1,1), (1,2,2), (0,2,3), (0,3,4), (2,3,5)`
2.  **Pick (0,1,1):** Connects 0 and 1. OK. (Cost: 1)
3.  **Pick (1,2,2):** Connects 1 and 2. OK. (Cost: 1+2=3)
4.  **Pick (0,2,3):** 0 and 2 are already connected (via 1). **Cycle!** Skip.
5.  **Pick (0,3,4):** Connects 0 and 3. OK. (Cost: 3+4=7)
6.  **Pick (2,3,5):** 2 and 3 are already connected. Skip.

**MST Weight:** 7.

### Algorithm Steps

1.  **Sort Edges:** Sort all edges in ascending order of their weights.
2.  **Initialize DSU:** Create a Disjoint Set Union (DSU) structure where each node starts in its own set.
3.  **Iterate Edges:**
    -   For each edge `(u, v, w)`:
        -   Use DSU `find(u)` and `find(v)` to check if they are already in the same component.
        -   If they are different:
            -   Add `w` to total MST weight.
            -   Use DSU `union(u, v)` to merge the components.
            -   Increment edge count. If count reaches `N-1`, stop (optimization).
4.  **Output:** Total weight.

## ✅ Input/Output Clarifications (Read This Before Coding)

-   **Connected Graph:** The input is guaranteed to be connected, so an MST always exists.
-   **Weights:** Can be large, so use 64-bit integers (`long` in Java/C++) for the sum.
-   **Multiple Edges:** Kruskal's handles them naturally (duplicates or heavier parallel edges are skipped).

## Naive Approach

### Intuition

Try every possible subset of edges, check if it's a spanning tree, and find the minimum weight.

### Time Complexity

-   **Exponential**: O(2^M). Completely infeasible.

## Optimal Approach (Kruskal's Algorithm)

Kruskal's is a greedy algorithm. It always picks the cheapest available edge that doesn't form a cycle.

### Time Complexity

-   **O(M log M)** or **O(M log N)**: Dominated by sorting the edges. DSU operations are nearly constant time (Inverse Ackermann function, α(N)).

### Space Complexity

-   **O(N + M)**: To store edges and DSU structures.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
3 3
0 1 1
1 2 2
0 2 3
```

**Initialization:**
-   `edges`: `[(0,1,1), (1,2,2), (0,2,3)]` (Already sorted)
-   `dsu`: `{0:0, 1:1, 2:2}`
-   `mstWeight`: 0

**Iteration 1:**
-   Edge `(0, 1, 1)`. `find(0)=0`, `find(1)=1`. Different.
-   Union(0, 1). `dsu`: `{0:1, 1:1, 2:2}`.
-   `mstWeight` += 1.

**Iteration 2:**
-   Edge `(1, 2, 2)`. `find(1)=1`, `find(2)=2`. Different.
-   Union(1, 2). `dsu`: `{0:1, 1:2, 2:2}`.
-   `mstWeight` += 2. Total: 3.

**Iteration 3:**
-   Edge `(0, 2, 3)`. `find(0)=2`, `find(2)=2`. Same. Skip.

**Result:** 3.

## ✅ Proof of Correctness

Kruskal's algorithm is based on the **Cut Property**: For any cut (a partition of the vertices into two disjoint sets), if an edge has the minimum weight among all edges crossing the cut, then this edge belongs to some MST. Kruskal's effectively picks the minimum weight edge crossing the cut between two currently disconnected components at each step.

## 💡 Interview Extensions (High-Value Add-ons)

-   **Prim's Algorithm:** Another MST algorithm. Better for dense graphs (O(M + N log N) or O(N^2)).
-   **Maximum Spanning Tree:** Just sort edges in descending order.
-   **Second Best MST:** Find MST, then try swapping one edge out for the next best one.

### Common Mistakes to Avoid

1.  **Not Sorting:** Kruskal's relies entirely on processing edges from smallest to largest.
2.  **Cycle Detection:** Using DFS/BFS for cycle detection is O(N) per edge, making the total O(M*N). DSU is O(M α(N)), which is much faster.
3.  **Disconnected Graph:** If the graph isn't connected, Kruskal's finds a Minimum Spanning *Forest*.
