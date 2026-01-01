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
