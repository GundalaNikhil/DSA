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


### Python


### C++


### JavaScript


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
